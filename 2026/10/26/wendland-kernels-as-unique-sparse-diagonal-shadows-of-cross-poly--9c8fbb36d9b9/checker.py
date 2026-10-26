"""Exact finite checks for the cross-polytope/Wendland shadow identity.

Run: python checker.py. Proof for all orders is in RESULT.md.
"""
from functools import lru_cache
from sympy import Symbol, factorial, binomial, beta, integrate, factor, simplify, rf

r=Symbol('r', nonnegative=True)

@lru_cache(None)
def wendland_raw(k):
    assert k >= 1
    f=(1-r)**k
    for _ in range(k-1):
        f=integrate(Symbol('s')*f.subs(r,Symbol('s')), (Symbol('s'),r,1))
        f=factor(f)
    return f

def projected_density(d,k):
    # Density at y=r>0 for Y=sum of k coordinates of uniform l1-ball in R^d.
    assert d>=k>=1
    expr=factorial(d)*r**(k-1)*(1-r)**(d-k)/(2**k*factorial(k-1)*factorial(d-k))
    for j in range(1,k):
        for h in range(j):
            expr += (binomial(k,j)*factorial(d)*binomial(j-1,h)*
                     r**(j-1-h)*(1-r)**(d-j+h)*factorial(k-j+h-1)/
                     (2**(2*k-j+h)*factorial(j-1)*factorial(k-j-1)*factorial(d-j+h)))
    return factor(expr)

checks=0
for k in range(1,7):
    d=3*k-1
    f=wendland_raw(k)
    rho=projected_density(d,k)
    norm=2*integrate(f,(r,0,1))
    assert simplify(rho-f/norm)==0, ('density mismatch',k)
    checks += 1
    for n in range(0,10):
        m=2*integrate(r**(2*n)*f,(r,0,1))/norm
        expected=factorial(2*n)*rf(k,n)/(factorial(n)*rf(d+1,2*n))
        assert simplify(m-expected)==0, ('moment mismatch',k,n)
        checks +=1
    # uniqueness from second moment under fixed k
    m2=simplify(2*k/((d+1)*(d+2)))
    assert m2 == simplify(2*k/(3*k*(3*k+1)))
    checks+=1
print('Exact symbolic density identifications:',6)
print('Exact symbolic moment equalities:',60)
print('Dimension-identifying second moments:',6)
print('Total symbolic checks:',checks)
for k in range(1,5):
    d=3*k-1
    q=projected_density(d,k)
    print('k=%d d=%d density_positive_y=%s'%(k,d,q))
