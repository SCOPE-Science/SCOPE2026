"""Direct finite-field enumeration for the Heisenberg retraction-rank formula.

Run: python verify_heisenberg.py
Uses no nonstandard packages. Checks defining endomorphism and idempotence
identities directly on matrices over small prime fields.
"""
from collections import Counter
from itertools import product
from math import prod


def matmul(a,b,q):
    d=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(d))%q for j in range(d)] for i in range(d)]


def rank(a,q):
    a=[r[:] for r in a]
    d=len(a)
    k=0
    for j in range(d):
        i=next((i for i in range(k,d) if a[i][j]%q),None)
        if i is None: continue
        a[k],a[i]=a[i],a[k]
        fac=pow(a[k][j],-1,q)
        a[k]=[(z*fac)%q for z in a[k]]
        for i in range(d):
            if i!=k:
                fac=a[i][j]
                a[i]=[(x-fac*y)%q for x,y in zip(a[i],a[k])]
        k+=1
        if k==d: break
    return k


def form(v,w,q):
    return sum(v[2*i]*w[2*i+1]-v[2*i+1]*w[2*i] for i in range(len(v)//2))%q


def isotropic_count(m,r,q):
    if r==0:return 1
    num=prod(q**(2*m-i)-q**i for i in range(r))
    den=prod(q**r-q**i for i in range(r))
    assert num%den==0
    return num//den


def predicted(m,q):
    return {r:isotropic_count(m,r,q)*q**(r*(2*m-r+1)) for r in range(m+1)}


def brute(m,q):
    d=2*m
    counts=Counter()
    identity_candidates=0
    for flat in product(range(q), repeat=d*d):
        a=[list(flat[i*d:(i+1)*d]) for i in range(d)]
        if matmul(a,a,q)!=a:continue
        # All possible central coefficients c satisfy c*c=c: c=0 or c=1.
        # The c=1 branch must preserve the full form and the additive center label.
        full_form=all(form([a[k][i] for k in range(d)],[a[k][j] for k in range(d)],q)==form([int(k==i) for k in range(d)],[int(k==j) for k in range(d)],q)
                      for i in range(d) for j in range(d))
        if full_form:
            for b in product(range(q), repeat=d):
                if all(sum(b[k]*a[k][i] for k in range(d))%q==0
                       for i in range(d)):
                    identity_candidates+=1
        if any(form([a[k][i] for k in range(d)],[a[k][j] for k in range(d)],q) for i in range(d) for j in range(i+1,d)):
            continue
        r=rank(a,q)
        # Central coordinate functional b must equal b applied after A.
        for b in product(range(q), repeat=d):
            if all(sum(b[k]*a[k][i] for k in range(d))%q==b[i] for i in range(d)):
                counts[r]+=1
    assert identity_candidates==1,(m,q,identity_candidates)
    return dict(counts)


def phase(m):
    scores=[(r,(8*m*r-5*r*r+3*r)//2) for r in range(1,m+1)]
    maxdegree=max(v for _,v in scores)
    return [r for r,v in scores if v==maxdegree]

if __name__=='__main__':
    for m,q in [(1,2),(1,3),(1,5),(2,2)]:
        obs=brute(m,q)
        exp=predicted(m,q)
        assert obs==exp,(m,q,obs,exp)
        print(f'CHECK_OK m={m} q={q} by_rank={obs} total={1+sum(obs.values())}')
    for m in range(1,31):
        E=[(8*m*r-5*r*r+3*r)//2 for r in range(1,m+1)]
        maxima={r for r in range(1,m+1) if E[r-1]==max(E)}
        analytic={r for r in range(1,m+1) if 4*m-5*r+4>=0 and (r==m or 4*m-5*(r+1)+4<=0)}
        assert maxima==analytic,(m,maxima,analytic)
    print('CHECK_OK rank-degree phase transitions m=1..30')
