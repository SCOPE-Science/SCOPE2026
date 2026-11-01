#!/usr/bin/env python3
"""Independent finite-state checker and explicit construction for binary connected EF1-outer biclique fair division."""
from functools import lru_cache

def outer_valued(c):
    a1,a0,b1,b0=c
    A=a1+a0;B=b1+b0;size=A+B
    return bool((a1 and (size<=2 or (A>=2 and B>=1))) or
                (b1 and (size<=2 or (B>=2 and A>=1))))

def valid(groups, a,b,k,u,v):
    if len(groups)!=k:return False
    if tuple(map(sum,zip(*groups)))!=(u,a-u,v,b-v):return False
    vals=[]
    for c in groups:
        A=c[0]+c[1];B=c[2]+c[3];size=A+B
        if not(size>=1 and (size==1 or (A>=1 and B>=1))):return False
        vals.append(c[0]+c[2])
    low=min(vals)
    return all(val<=low+1 and (val==low or outer_valued(c)) for c,val in zip(groups,vals))

def make(a,b,k,u,v):
    assert a>=b>=1 and 1<=k<=a+b and (k<=b or k>=a)
    orig_u,orig_v=u,v
    ans=[[0,0,0,0] for _ in range(k)]
    if k<=b:
        # Equalize total valued items, then supply a connector from each side.
        W=u+v;lo,r=divmod(W,k)
        for j in range(u):ans[j%k][0]+=1
        for j in range(u,u+v):ans[j%k][2]+=1
        missingA=[i for i,g in enumerate(ans) if g[0]==0]
        missingB=[i for i,g in enumerate(ans) if g[2]==0]
        for i in missingA: ans[i][1]+=1
        for i in missingB: ans[i][3]+=1
        extrasA=(a-u)-len(missingA)
        extrasB=(b-v)-len(missingB)
        assert extrasA>=0 and extrasB>=0
        depot=r if r else 0
        ans[depot][1]+=extrasA;ans[depot][3]+=extrasB
    else:
        p=a+b-k
        A0=a-u;B0=b-v
        # Split into p connected cross-part pairs, and k-p singleton vertices.
        if u+v<=k:
            # Never pair two valuable vertices.
            t=min(p,A0,v)
            ans[:t]=[[0,1,1,0] for _ in range(t)]
            A0-=t;v-=t;p-=t
            t=min(p,u,B0)
            ans[a+b-k-p:a+b-k-p+t]=[[1,0,0,1] for _ in range(t)]
            u-=t;B0-=t;p-=t
            t=min(p,A0,B0)
            ans[a+b-k-p:a+b-k-p+t]=[[0,1,0,1] for _ in range(t)]
            A0-=t;B0-=t;p-=t
            assert p==0
        else:
            # All zeros must be paired with a valued vertex of the opposite side.
            t=A0
            ans[:t]=[[0,1,1,0] for _ in range(t)]
            v-=t
            t2=B0
            ans[t:t+t2]=[[1,0,0,1] for _ in range(t2)]
            u-=t2
            p-=t+t2
            assert p>=0 and u>=p and v>=p
            ans[t+t2:t+t2+p]=[[1,0,1,0] for _ in range(p)]
            u-=p;v-=p
            A0=B0=0
        i=a+b-k
        for idx,rem in enumerate((u,A0,v,B0)):
            for _ in range(rem):
                assert i<k
                ans[i][idx]=1;i+=1
        assert i==k
    assert valid(ans,a,b,k,orig_u,orig_v),(a,b,k,orig_u,orig_v,ans)
    return ans

# Exact independent oracle: unordered connected bundle types, no reliance on construction.
def oracle(a,b,k,u,v):
    init=(u,a-u,v,b-v)
    W=u+v;q,r=divmod(W,k)
    items=[]
    for a1 in range(u+1):
      for a0 in range(a-u+1):
       for b1 in range(v+1):
        for b0 in range(b-v+1):
         c=(a1,a0,b1,b0)
         A=a1+a0;B=b1+b0
         if A+B<1 or (A+B>1 and (A==0 or B==0)):continue
         val=a1+b1
         if val!=q and val!=q+1:continue
         if val==q+1 and not outer_valued(c):continue
         items.append((c,val==q+1))
    @lru_cache(None)
    def f(rem,num,extra):
        if num==0:return extra==0 and rem==(0,0,0,0)
        if sum(rem)<num:return False
        for c,e in items:
            if e>extra:continue
            if all(c[i]<=rem[i] for i in range(4)):
                if f(tuple(rem[i]-c[i] for i in range(4)),num-1,extra-e):return True
        return False
    return f(init,k,r)

def run():
    cnt=0;neg=0;construct=0
    for a in range(1,9):
        for b in range(1,min(a,5)+1):
            for k in range(1,a+b+1):
                expected=k<=b or k>=a
                for u in range(a+1):
                    for v in range(b+1):
                        if expected:
                            g=make(a,b,k,u,v)
                            assert valid(g,a,b,k,u,v), ('construct',a,b,k,u,v,g)
                            construct+=1
                        else:
                            if u==a and v==b:assert not oracle(a,b,k,u,v)
                        if a<=7 and b<=4:
                            actual=oracle(a,b,k,u,v)
                            assert actual or not expected,(a,b,k,u,v)
                            if u==a and v==b and not expected:assert not actual
                            cnt+=1
                if not expected:neg+=1
    print('VERIFY_OK exact_profile_cases=',cnt,'constructive_profiles=',construct,'negative_spectrum_cells=',neg)

if __name__=='__main__':run()
