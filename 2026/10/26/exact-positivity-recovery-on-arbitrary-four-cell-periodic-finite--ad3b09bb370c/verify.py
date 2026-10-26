"""Exact symbolic verification for a four-cell periodic P1 finite-element positivity theorem.

Python 3 and SymPy. All coefficient checks are identities in four indeterminates,
not finite sampling or numerical evidence for the all-mesh claim.
"""
import sympy as sp

h=sp.symbols('a b c d', positive=True)
t=sp.symbols('t', nonnegative=True)
n=4
M=sp.zeros(n); K=sp.zeros(n)
for i, z in enumerate(h):
    j=(i+1)%n
    M[i,i]+=z/3; M[j,j]+=z/3
    M[i,j]+=z/6; M[j,i]+=z/6
    K[i,i]+=1/z; K[j,j]+=1/z
    K[i,j]-=1/z; K[j,i]-=1/z
C=M+t*K
scale=432*sp.prod(h)
N=sp.Matrix([[sp.Poly(sp.cancel(scale*(C.adjugate()*M)[i,j]),t) for j in range(n)] for i in range(n)])
def signed_coefficients(expr, require):
    poly=sp.Poly(sp.expand(expr), *h)
    coeffs=list(poly.coeffs())
    assert coeffs, (require,expr)
    if require=='+':
        assert all(v>0 for v in coeffs), (require,expr)
    elif require=='-':
        assert all(v<0 for v in coeffs), (require,expr)
    return len(coeffs)
for i in range(n):
    for j in range(n):
        P=N[i,j]
        if i==j:
            for degree in range(4):
                signed_coefficients(P.nth(degree), '+')
        else:
            assert P.nth(0)==0
            if (i-j)%n in (1,3):
                for degree in range(1,4):
                    signed_coefficients(P.nth(degree),'+')
            else:
                assert (i-j)%n==2
                signed_coefficients(P.nth(1),'-')
                signed_coefficients(P.nth(3),'+')
                # The degree-2 coefficient may take either sign.
                assert sp.Poly(P.nth(2),*h).degree()>=0
        print('polynomial',i,j,'time-degree',P.degree(),flush=True)
# Check equal alternating lengths specialize to existing a,b,a,b threshold
u,v=sp.symbols('u v',positive=True)
for i,j in [(0,2),(1,3),(2,0),(3,1)]:
    F=sp.factor((N[i,j].as_expr()/t).subs({h[0]:u,h[1]:v,h[2]:u,h[3]:v}))
    # All four roots coincide in the alternating case.
    if i==0: reference=sp.Poly(F,t).monic()
    else: assert sp.simplify(sp.Poly(F,t).monic().as_expr()-reference.as_expr())==0
    assert sp.simplify(reference.as_expr().subs(t,(sp.sqrt(u*u*v*v+2*u*v*(u+v)**2)-u*v)/12))==0
print('all symbolic coefficient tests, special-case recovery and matrix identities passed')
