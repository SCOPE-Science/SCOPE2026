"""Independent exact enumeration of Nash stability on friendship networks.
Run with Python 3 standard library: python verify.py
"""
from fractions import Fraction
from math import comb, factorial

def parts(n):
    # Generate all set partitions in canonical restricted-growth form.
    z=[0]*n
    def rec(i,mx):
        if i==n:
            yield tuple(z); return
        for v in range(mx+2):
            z[i]=v
            yield from rec(i+1,max(mx,v))
    yield from rec(1,0)

def b_restricted(t,cap):
    arr=[0]*(t+1);arr[0]=1
    for i in range(1,t+1):
        arr[i]=sum(comb(i-1,j-1)*arr[i-j] for j in range(1,min(cap,i)+1))
    return arr[t]

def theo(m):
    return sum(comb(m,s)*b_restricted(m-s,s) for s in range(1,m+1))

def check(m):
    n=2*m+1; neighbors=[0]*n
    for i in range(m):
        a,b=2*i+1,2*i+2
        for x,y in [(0,a),(0,b),(a,b)]:
            neighbors[x]|=1<<y;neighbors[y]|=1<<x
    stable=0;wo=Fraction(-1);wn=Fraction(10**9);wb=Fraction(-1);bad=[];npart=0;maxcount=0;minstablecount=0;beststablecount=0
    for profile in parts(n):
        npart+=1;k=1+max(profile); masks=[0]*k; sizes=[0]*k
        for v,g in enumerate(profile):masks[g]|=1<<v;sizes[g]+=1
        incident=[(neighbors[v]&masks[profile[v]]).bit_count() for v in range(n)]
        welfare=sum((Fraction(incident[v],sizes[profile[v]]) for v in range(n)),Fraction(0))
        if welfare>wo:wo=welfare;maxcount=1
        elif welfare==wo:maxcount+=1
        eq=True
        for v in range(n):
            cur=profile[v];g=incident[v];den=sizes[cur]
            for dest in range(k):
                if dest==cur:continue
                if (neighbors[v]&masks[dest]).bit_count()*den>g*(sizes[dest]+1):
                    eq=False;break
            if not eq:break
        if not eq:continue
        stable+=1
        if welfare<wn:wn=welfare;minstablecount=1
        elif welfare==wn:minstablecount+=1
        if welfare>wb:wb=welfare;beststablecount=1
        elif welfare==wb:beststablecount+=1
        home=profile[0]
        selected=[];outside=[]
        for i in range(m):
            x,y=2*i+1,2*i+2
            if profile[x]==home and profile[y]==home:selected.append(i)
            elif profile[x]==home or profile[y]==home:bad.append(('split hub',profile))
            elif profile[x]!=profile[y]:bad.append(('split pair',profile))
            else:outside.append(profile[x])
        s=len(selected)
        if not s or any(outside.count(t)>s for t in set(outside)):
            bad.append(('threshold',profile))
    expected_worst=Fraction(6*m,2*m+1)
    assert not bad, bad[:3]
    assert stable==theo(m),(m,stable,theo(m))
    assert wo==m+1,(m,wo,m+1)
    assert wn==expected_worst,(m,wn,expected_worst)
    assert wb==m+1,(m,wb,m+1)
    assert maxcount==m,(m,maxcount)
    assert beststablecount==m,(m,beststablecount)
    assert minstablecount==1,(m,minstablecount)
    print('m',m,'partitions',npart,'Nash',stable,'welfare_max',wo,'Nash_min',wn,'Nash_max',wb,'welfare-opt-count',maxcount,'unique-worst',minstablecount,'PASS')

if __name__=='__main__':
    for m in range(1,6):check(m)
