"""Exact-rational, self-contained checks for star-conditioned cut/elliptope formulas.

Proof is analytic and appears in RESULT.md. Finite checks are supplementary.
Run: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product

def g(n,k):
    return k*(n-k)

def values(n,p):
    assert n >= 2 and F(0) <= p <= F(1,2)
    t=n*p
    k=t.numerator//t.denominator
    z=t-k
    cut=(1-z)*g(n,k)+z*g(n,k+1)
    bare=n*n*p*(1-p)
    tr=min(n*(n-1)*p,bare, F(n*(n-1),3) if n>=3 else F(1000000))
    return bare,tr,cut,k,z

count=0
for n in range(2,25):
    parameters={F(0),F(1,2),F(1,n)}
    parameters|={F(j,200) for j in range(101)}
    parameters|={F(j,2*n) for j in range(n+1)}
    for p in sorted(parameters):
        if p>F(1,2): continue
        bare,tr,cut,k,z=values(n,p)
        # Concave discrete chord and its exact distance to quadratic envelope.
        assert bare-cut==z*(1-z)
        assert cut<=tr<=bare
        assert tr==cut if n<=3 else tr-cut==(F(0) if p<=F(1,n) else z*(1-z))
        q=2*tr/(n*(n-1)); b=1-2*q; a=1-2*p
        # Exact Schur-complement PSD conditions for the symmetric Gram matrix.
        assert 1-b>=0 and 1+(n-1)*b-n*a*a>=0
        assert F(0)<=q<=1 and q<=2*p and q+2*p<=2
        assert n==2 or 3*q<=2
        if n>=4 and p>=F(1,n): assert tr==bare
        if n==3 and p>=F(1,3): assert tr==2
        count+=1
    # For all possible cut sizes, a chord lies above the discrete cut profile.
    for k in range(n):
        for s in range(n+1):
            chord=g(n,k)+(s-k)*(g(n,k+1)-g(n,k))
            assert chord-g(n,s)==(s-k)*(s-k-1)>=0
            count+=1

# Exhaustive cut enumeration checks for each size and a family of exact mixtures.
for n in range(2,9):
    for k in range(n+1):
        subsets=[mask for mask in product((0,1),repeat=n) if sum(mask)==k]
        assert len(subsets)>0
        objective=F(sum(sum(mask[i]!=mask[j] for i in range(n)
                       for j in range(i+1,n)) for mask in subsets),len(subsets))
        leaf_marginal=F(sum(mask[0] for mask in subsets),len(subsets))
        assert objective==g(n,k) and leaf_marginal==F(k,n)
        count+=1

# Exact examples of gap 1/4 and its first possible appearance.
for n in range(4,25):
    p=F(3,2*n)
    assert F(0)<p<=F(1,2)
    _,tri,cut,_,_=values(n,p)
    assert tri-cut==F(1,4)
    count+=1
print('VERIFY_OK',count,'exact-rational tests')

# Optional independent numerical LP over all sign vectors (requires NumPy/SciPy).
# Run: python3 verify.py --lp
if __import__('sys').argv[1:] == ['--lp']:
    import numpy as np
    from scipy.optimize import linprog
    lp_checks=0
    for n in range(2,7):
        vectors=list(product((0,1),repeat=n))
        scores=np.array([sum(z[i]!=z[j] for i in range(n)
                             for j in range(i+1,n)) for z in vectors],float)
        A=np.array(vectors,float).T
        for j in range(1,20):
            p=F(j,40)
            target=float(values(n,p)[2])
            ans=linprog(-scores,A_ub=A,b_ub=np.full(n,float(p)),
                        A_eq=np.ones((1,len(vectors))),b_eq=[1],
                        bounds=(0,None),method='highs')
            assert ans.success and abs(-ans.fun-target)<1e-8
            lp_checks+=1
    print('LP_OK',lp_checks,'independent finite linear programs')
