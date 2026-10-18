#!/usr/bin/env python3
"""Exhaustive small-parameter checks for flag-marked subspace posets."""
from itertools import combinations, product
from collections import Counter
from math import prod


def enumerate_subspaces(p,n):
    vectors=list(product(range(p),repeat=n))
    ans={}
    for k in range(n+1):
        for piv in combinations(range(n),k):
            free=[(i,j) for i in range(k) for j in range(piv[i]+1,n) if j not in piv]
            for vals in product(range(p),repeat=len(free)):
                rows=[[0]*n for _ in range(k)]
                for i,j in enumerate(piv): rows[i][j]=1
                for (i,j),v in zip(free,vals): rows[i][j]=v
                pts=set()
                for coeffs in product(range(p),repeat=k):
                    pts.add(tuple(sum(coeffs[i]*rows[i][j] for i in range(k))%p for j in range(n)))
                key=frozenset(pts)
                ans[key]=k
    return list(ans.items())

def refine(subs,flags):
    N=len(subs)
    dim=[d for s,d in subs]
    below=[[i for i in range(N) if i!=j and subs[i][0]<=subs[j][0]] for j in range(N)]
    above=[[] for _ in range(N)]
    for j in range(N):
        for i in below[j]: above[i].append(j)
    old=[flags.index(j)+1 if j in flags else 0 for j in range(N)]
    history=[old]
    for _ in range(5):
        keys=[(old[j],tuple(sorted(Counter(old[i] for i in below[j]).items())),tuple(sorted(Counter(old[i] for i in above[j]).items()))) for j in range(N)]
        dic={k:i for i,k in enumerate(sorted(set(keys)))}
        now=[dic[k] for k in keys]
        # Partition comparison, labels may change between steps.
        history.append(now)
        if all((old[i]==old[j])==(now[i]==now[j]) for i in range(N) for j in range(N)):
            break
        old=now
    return history,below

def expected_profile(subs,flags):
    N=len(subs)
    f=[0]+flags+[next(i for i,(s,d) in enumerate(subs) if d==max(x[1] for x in subs))]
    dimensions=[subs[i][1] for i in f]
    ds=[dimensions[i+1]-dimensions[i] for i in range(len(dimensions)-1)]
    # Flags are ordered by inclusion; assume unique bottom/top and no intermediate duplicated.
    signatures=[]
    for s,dim in subs:
        es=[len(s & subs[i][0]) for i in f]
        # size of an e-dimensional vector space q^e
        q=next(p for p in [2,3,5] if p**dim==len(s)) if dim else next(p for p in [2,3,5] if p**max(x[1] for x in subs)==len(max(subs,key=lambda x:x[1])[0]))
        ix=[0 if z==1 else next(e for e in range(1,dimensions[-1]+1) if q**e==z) for z in es]
        signatures.append(tuple(ix[i+1]-ix[i] for i in range(len(ds))))
    return ds,signatures

def check(p,n,max_flags=200):
    subs=enumerate_subspaces(p,n)
    dims=[d for s,d in subs]
    zero=next(i for i,d in enumerate(dims) if d==0)
    whole=next(i for i,d in enumerate(dims) if d==n)
    inter=[i for i,d in enumerate(dims) if 0<d<n]
    flags=[()]
    def walk(path,last):
        if len(flags)>=max_flags: return
        for i in inter:
            if len(flags)>=max_flags: break
            if (not path or subs[last][0]<subs[i][0]) and i not in path:
                flags.append(path+(i,))
                walk(path+(i,),i)
    walk((),zero)
    tests=0
    for flag in flags:
        H,below=refine(subs,flag)
        ds,sigs=expected_profile(subs,list(flag))
        r2=H[2] if len(H)>2 else H[-1]
        # If process converges at round1, then class equality at round2 is same.
        for i in range(len(subs)):
            for j in range(i):
                assert (r2[i]==r2[j])==(sigs[i]==sigs[j]),(p,n,flag,i,j,sigs[i],sigs[j])
        assert len(set(r2))==prod(d+1 for d in ds),(p,n,ds,len(set(r2)))
        tests+=1
    return len(subs),tests

if __name__=='__main__':
    for p,n,limit in [(2,2,15),(2,3,50),(2,4,110),(3,2,15),(3,3,50)]:
        N,tests=check(p,n,limit)
        print(f'PASS q={p} n={n} subspaces={N} flags={tests}')

# A sharpness witness: in F_2^4 mark U=<e_1,e_2>. The 2-planes
# W_0=<e_3,e_4> and W_1=<e_1,e_3> are equally coloured at round 1
# but not at round 2.
def sharpness_witness():
    subs=enumerate_subspaces(2,4)
    idx={s:i for i,(s,d) in enumerate(subs)}
    def span(basis):
        return frozenset(tuple(sum(c*v[j] for c,v in zip(a,basis))%2 for j in range(4))
            for a in product(range(2),repeat=len(basis)))
    e=[tuple(int(i==j) for j in range(4)) for i in range(4)]
    U=idx[span([e[0],e[1]])]
    W0=idx[span([e[2],e[3]])]
    W1=idx[span([e[0],e[2]])]
    colors,below=refine(subs,[U])
    assert colors[1][W0]==colors[1][W1]
    assert colors[2][W0]!=colors[2][W1]
    print('PASS sharpness q=2 n=4 one-flag strict two-round witness')

if __name__=='__main__':
    sharpness_witness()
