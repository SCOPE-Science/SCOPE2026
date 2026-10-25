"""Exact tests of spherical-cap angular-order concentration identities.

The arguments for arbitrary degree are in RESULT.md. This script only performs
finite symbolic spot checks and algebraic crossing-count checks.
Requires Python 3 and SymPy.
"""
import sympy as sp

x,t=sp.symbols('x t',real=True)
assertions=0
max_degree=11
for ell in range(1,max_degree+1):
    P=sp.legendre(ell,t)
    eigen=[]
    ders=[]
    for m in range(ell+1):
        deriv=sp.diff(P,t,m)
        ders.append(deriv)
        density=sp.Rational(2*ell+1,2)*sp.factorial(ell-m)/sp.factorial(ell+m)*(1-t*t)**m*deriv**2
        val=sp.integrate(density, (t,x,1))
        eigen.append(sp.factor(val))
        assert sp.simplify(val.subs(x,0)-sp.Rational(1,2))==0
        assertions+=1
    for m in range(ell):
        R=sp.Rational(2*ell+1,2)*sp.factorial(ell-m-1)/sp.factorial(ell+m+1)*(1-x*x)**(m+1)*ders[m].subs(t,x)*ders[m+1].subs(t,x)
        assert sp.expand(eigen[m]-eigen[m+1]-R)==0,(ell,m)
        assertions+=1
        zeros_m=sp.polys.polytools.intervals(sp.Poly(ders[m],t),eps=sp.Rational(1,10**11))
        zeros_m1=sp.polys.polytools.intervals(sp.Poly(ders[m+1],t),eps=sp.Rational(1,10**11))
        count=sum(1 for (a,b),_mult in zeros_m if a>0) + sum(1 for (a,b),_mult in zeros_m1 if a>0)
        assert count==ell-m-1,(ell,m,count)
        assertions+=1
    for j in range(1,ell):
        zeros_j=sp.polys.polytools.intervals(sp.Poly(ders[j],t),eps=sp.Rational(1,10**11))
        assert sum(1 for (a,b),_mult in zeros_j if a>0)==(ell-j)//2,(ell,j)
        assertions+=1
        g=sp.Poly(sp.gcd(ders[j-1],ders[j+1]),t)
        assert all(not (sp.Rational(a)>0) for (a,b),_mul in sp.polys.polytools.intervals(g)),(ell,j,g)
        assertions+=1
    # The modal coefficient controlling the near-hemisphere deficit decreases
    # along the parity-compatible ladder, as predicted by the proof.
    odd_modes=[m for m in range(ell+1) if (ell-m)%2==1]
    vals=[]
    for m in odd_modes:
        fp=sp.diff((1-t*t)**sp.Rational(m,2)*ders[m],t).subs(t,0)
        norm=sp.factorial(ell-m)/sp.factorial(ell+m)
        vals.append(sp.simplify(fp*fp*norm))
    assert len(vals)>0
    assert all(vals[k]>vals[k+1] for k in range(len(vals)-1)),(ell,vals)
    assertions+=1
print('PASS', assertions, 'exact assertion groups, degrees 1..',max_degree)
print('Verified: exact spectral integrals, boundary product, crossing counts,')
print('positive-root triple patterns, two-step coprimality, equator ordering.')
print('Finite tests do not certify the all-degree theorem; see analytical proof.')
