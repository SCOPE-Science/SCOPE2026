"""Independent exact checks for Frobenius-twisted cyclic hypersurface degeneration.

Requires Python 3 and SymPy. Only finite samples and polynomial identities are checked;
the universal statements are proved in the accompanying theorem.
"""
from math import comb, gcd
from itertools import product
import sympy as sp

def predicted_mu(a, r):
    return sum((-1)**j * a**(r-j) for j in range(r+1))

def hilbert_weights(a, r):
    D=a**r
    W=[0]*r
    W[-1]=D//a
    for j in range(r-2,-1,-1):
        W[j]=(D-W[j+1])//a
        assert a*W[j]+W[j+1]==D
    return D,W

def jacobian_length_by_groebner(a, r, p):
    assert a>=2 and (a+1)%p==0
    u=sp.symbols('u1:'+str(r+1))
    f=sum(u[i]**a*u[i+1] for i in range(r-1))+u[-1]**a
    jac=[sp.diff(f,t) for t in u]
    G=sp.groebner(jac,*u,order='lex', modulus=p)
    lead=[tuple(poly.LM(order=G.order).exponents) for poly in G.polys]
    bounds=[]
    for i in range(r):
        pure=[e[i] for e in lead if e[i]>0 and all(e[j]==0 for j in range(r) if j!=i)]
        assert pure,(a,r,p,i,lead)
        bounds.append(min(pure))
    count=sum(1 for e in product(*(range(B) for B in bounds)) if not any(all(e[j]>=L[j] for j in range(r)) for L in lead))
    D,W=hilbert_weights(a,r)
    assert count==predicted_mu(a,r)==sp.prod(sp.Rational(D-w,w) for w in W)
    # Weighted Euler identity is the algebraic statement f in its Jacobian ideal.
    assert sp.Poly(D*f-sum(W[i]*u[i]*jac[i] for i in range(r)),*u).is_zero
    return count,len(G.polys),bounds

def strata(q,m,s):
    Q=q**s; g=gcd(m,s); ell=m//g
    data={}
    for k in range(1,g+1):
        num=comb(g,k)*(Q**ell-1)**k
        assert num%(Q-1)==0
        data[m-k*ell]=num//(Q-1)
    assert sum(data.values())==(Q**m-1)//(Q-1)
    assert data.get(0,0)==(Q**ell-1)**g//(Q-1)
    return data

def main():
    # Coefficients, local analytic models, and Jacobian colengths are checked
    # in three distinct characteristics/dimensions.
    cases=[(3,2,2),(2,3,3),(3,4,2)]
    for a,r,p in cases:
        mu,N,bounds=jacobian_length_by_groebner(a,r,p)
        print('Jacobian quotient',dict(d=a+1,m=r+1,p=p,mu=mu,groebner_generators=N,staircase_bounds=bounds))
    examples=[(2,3,1),(2,3,2),(2,3,3),(2,3,6),(3,4,1),(3,4,2),(3,4,3),(3,4,4),(2,5,1),(2,5,5)]
    for q,m,s in examples:
        print('Extension arithmetic',dict(q=q,m=m,s=s,counts_by_missing_coefficients=strata(q,m,s)))
    # Direct support-count check in the fully split F_8-parameter example.
    q,m,s=2,3,3
    Q=q**s
    counts={}
    for c in product(range(Q),repeat=m):
        if all(v==0 for v in c): continue
        dimension=sum(v==0 for v in c)
        counts[dimension]=counts.get(dimension,0)+1
    assert all(v%(Q-1)==0 for v in counts.values())
    observed={k:v//(Q-1) for k,v in counts.items()}
    assert observed==strata(q,m,s)
    print('F8 split parameter full exhaustive support census:',observed)
    print('AGR_CYCLIC_DISCRIMINANT_TORUS_CHAIN_MU_EXTENSION_DISTRIBUTION_PASS')

if __name__=='__main__': main()
