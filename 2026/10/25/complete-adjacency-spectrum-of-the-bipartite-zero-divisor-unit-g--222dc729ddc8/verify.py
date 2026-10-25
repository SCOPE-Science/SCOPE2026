"""Independently compute the bipartite zero-divisor--unit incidence spectrum.
For each finite field only the sizes of its nonzero coordinate sets matter.
Requires Python and NumPy for numerical diagonalization; graph construction is independent.
"""
from itertools import product, combinations
from math import prod
from collections import Counter


def expected(m):
    r=len(m)
    unit_size=prod(m)
    zero_div_size=prod(x+1 for x in m)-unit_size-1
    eig=Counter()
    for mask in range(1<<r):
        T=[i for i in range(r) if (mask>>i)&1]
        multiplicity=prod(m[i]-1 for i in T)
        if not multiplicity: continue
        if not T:
            lam=0
            for Jmask in range(1,(1<<r)-1):
                J=[i for i in range(r) if Jmask>>i&1]
                notJ=[i for i in range(r) if not Jmask>>i&1]
                lam += prod(m[i] for i in notJ)*(prod(m[i] for i in J)-prod(m[i]-1 for i in J))**2
        else:
            lam=0
            for Jmask in range(1,(1<<r)-1):
                if mask&Jmask!=mask: continue
                lam+=prod(m[i] for i in range(r) if not Jmask>>i&1)*prod((m[i]-1)**2 for i in range(r) if Jmask>>i&1 and not mask>>i&1)
        eig[lam]+=multiplicity
    F=prod(x-1 for x in m)
    closed_top=unit_size*prod(x+1 for x in m)-2*unit_size**2+prod(x*x-x+1 for x in m)-(unit_size-F)**2
    assert eig[closed_top]>=1, (m,closed_top,eig)
    assert sum(eig.values())==unit_size
    assert sum(k*v for k,v in eig.items())==sum(1 for z in product(*(range(x+1) for x in m)) if any(y==0 for y in z) and any(y!=0 for y in z) for u in product(*(range(1,x+1) for x in m)) if any(zi==ui for zi,ui in zip(z,u)))
    return eig,unit_size,zero_div_size


def incidence(m):
    zs=[z for z in product(*(range(x+1) for x in m)) if any(y==0 for y in z) and any(y!=0 for y in z)]
    us=list(product(*(range(1,x+1) for x in m)))
    return [[int(any(x!=0 and x==y for x,y in zip(z,u))) for u in us] for z in zs]


def verify_one(m):
    import numpy as np
    e,U,Z=expected(m)
    B=np.array(incidence(m),dtype=np.int64)
    assert B.shape==(Z,U)
    Gram=B.T@B
    vals=np.linalg.eigvalsh(Gram)
    want=sorted([x for x,c in e.items() for _ in range(c)])
    assert np.allclose(vals,want,rtol=0,atol=5e-8), (m,vals,want)
    rank=U-prod(x-1 for x in m)
    assert np.linalg.matrix_rank(Gram,tol=1e-6)==rank, (m,rank)
    return {'field_orders':[x+1 for x in m], 'units':U, 'nonzero_zero_divisors':Z,'rank':rank,'gram_eigenvalues':sorted(e.items())}

if __name__=='__main__':
    cases=[]
    for r in (2,3,4):
        for m in product((1,2,3,4),repeat=r):
            if prod(m)>45 or prod(x+1 for x in m)>110:continue
            cases.append(m)
    for m in cases:verify_one(m)
    print('SPECTRUM_VERIFY_OK',len(cases),'finite product sizes')
    for m in ((1,1),(1,2),(2,2),(2,3),(2,2,2),(1,2,3),(2,2,2,2)):
        print(verify_one(m))
