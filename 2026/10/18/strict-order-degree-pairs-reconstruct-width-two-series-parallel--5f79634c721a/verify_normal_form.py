"""Independent exhaustive small-order check of the degree-pair reconstruction theorem.
All mathematics is over the strict order relation, not the Hasse edges.
Requires Python 3.10+ standard library only.
"""
from functools import lru_cache
from collections import Counter

@lru_cache(None)
def forms(n):
    if n==0: return ((),)
    out=[]
    out.extend((('S',),)+s for s in forms(n-1))
    for a in range(1,n+1):
        for b in range(a,n-a+1):
            out.extend((('P',a,b),)+s for s in forms(n-a-b))
    return tuple(out)

def strict_order(f):
    n=sum(1 if x[0]=='S' else x[1]+x[2] for x in f)
    E=set(); idx=0; prior=[]; orbit=[]
    for k,block in enumerate(f):
        if block[0]=='S':
            sets=[list(range(idx,idx+1))];idx+=1
        else:
            a,b=block[1:];sets=[list(range(idx,idx+a)),list(range(idx+a,idx+a+b))];idx+=a+b
        nodes=[x for one in sets for x in one]
        E.update((x,y) for x in prior for y in nodes)
        for one in sets:
            E.update((one[i],one[j]) for i in range(len(one)) for j in range(i+1,len(one)))
        if block[0]=='S':orbit.append((k,'S',0))
        else:
            for side,one in enumerate(sets):
                for t in range(len(one)):
                    orbit.append((k,len(one),t))
        prior.extend(nodes)
    assert idx==n
    return E,orbit

def degrees(E,n):
    lower=[0]*n; upper=[0]*n
    for x,y in E:lower[y]+=1;upper[x]+=1
    return tuple(zip(lower,upper))

def invert(deg):
    """Only the unordered multiset of degree pairs is used."""
    raw=Counter(deg)
    n=sum(raw.values());p=0;answer=[]
    while p<n:
        top=[(u,c) for (l,u),c in raw.items() if l==p]
        assert sum(c for u,c in top) in (1,2),(p,top,raw)
        if sum(c for u,c in top)==1:
            assert top==[(n-p-1,1)],(p,top)
            block=('S',);m=1
        else:
            outs=sorted([u for u,c in top for _ in range(c)])
            a,b=sorted([n-p-1-u for u in outs])
            assert a>=1 and b>=1
            block=('P',a,b);m=a+b
        # After the block, all remaining vertices lie strictly above it.
        for (l,u),c in list(raw.items()):
            if p<=l<p+m:
                assert c>0
                del raw[(l,u)]
        answer.append(block);p+=m
    assert not raw
    return tuple(answer)

def run(limit=12):
    total=0
    for n in range(1,limit+1):
        seen={}
        for f in forms(n):
            E,orbit=strict_order(f)
            d=degrees(E,n)
            # Reconstruction from the degree multiset.
            q=invert(d)
            assert q==f,('reconstruction',n,f,q)
            key=tuple(sorted(d))
            assert key not in seen,('degree collision',n,f,seen.get(key))
            seen[key]=f
            for i in range(n):
                for j in range(n):
                    assert (d[i]==d[j])==(orbit[i]==orbit[j]),('orbit',n,f,i,j)
            total+=1
        print('n=%2d normal_forms=%6d unique_degree_profiles=%6d' %(n,len(forms(n)),len(seen)))
    print('NORMAL_FORM_VERIFY_PASS total=%d' %total)

if __name__=='__main__':run()
