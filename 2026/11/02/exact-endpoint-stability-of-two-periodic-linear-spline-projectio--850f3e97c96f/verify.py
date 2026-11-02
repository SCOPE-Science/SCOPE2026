"""Reproducible exact tests for two-periodic linear-spline endpoint norms.
Dependencies: Python 3, SymPy. No network access or external data.
"""
from fractions import Fraction as Q
import sympy as sp


def exact_cycle(a,b,m):
    """L-infinity operator norm via independently inverted exact hat Gram matrix."""
    n=2*m
    h=[sp.Rational(a) if j%2==0 else sp.Rational(b) for j in range(n)]
    G=sp.zeros(n)
    for j in range(n):
        G[j,j]+=(h[j-1]+h[j])/3
        G[j,(j+1)%n]+=h[j]/6
        G[(j+1)%n,j]+=h[j]/6
    Gi=G.inv()
    vals=[]
    for i in range(n):
        g=list(Gi.row(i))
        total=sp.S.Zero
        for j in range(n):
            u,v=g[j],g[(j+1)%n]
            assert u*v<0
            U,V=abs(u),abs(v)
            total+=h[j]*(U*U+V*V)/(2*(U+V))
        vals.append(sp.factor(total))
    assert len(set(vals))==1, vals
    return vals[0]


def infinite_formula(a,b):
    s=sp.Rational(a)+sp.Rational(b)
    p=sp.Rational(a)*sp.Rational(b)
    return sp.factor((5*s*s+12*p)/(3*s*s+4*p))


def symbolic_identity():
    a,b,z=sp.symbols('a b z', positive=True)
    s=a+b; p=a*b; tau=(a+b*z)/(2*s); sig=(a*z+b)/(2*s)
    T=(a*(1+tau**2)/(1+tau)+b*(tau**2+z**2)/(tau+z)
       +a*(z**2+sig**2)/(z+sig)+b*(sig**2+1)/(sig+1))
    U=6*s*z*T/(p*(1-z)**2*(1+z))
    f=sp.factor((sp.together(U-sp.factor((5*s*s+12*p)/(3*s*s+4*p)))))
    num=sp.together(f).as_numer_denom()[0]
    # On-shell identity for z+z^-1=2+3s^2/p, equivalently
    # p*z^2 - (3*s^2+2*p)*z+p=0.
    eq=p*z*z-(3*s*s+2*p)*z+p
    assert sp.rem(sp.Poly(num,z),sp.Poly(eq,z)).is_zero
    return True

assert symbolic_identity()
profiles=0
for a,b in [(1,1),(1,2),(1,3),(1,4),(1,10),(2,3),(3,7)]:
    cap=infinite_formula(a,b)
    for m in range(2,9):
        val=exact_cycle(a,b,m)
        assert val < cap,(a,b,m,val,cap)
        profiles+=1
    print('profile',a,b,'infinite',str(cap),'finite m=8',str(exact_cycle(a,b,8)))
assert infinite_formula(1,1)==2
assert infinite_formula(1,2)==sp.Rational(69,35)
assert infinite_formula(1,4)==sp.Rational(173,91)
print('PASS symbolic identity,', profiles, 'finite exact cyclic profiles, equal vertex rows, strict bounds')
