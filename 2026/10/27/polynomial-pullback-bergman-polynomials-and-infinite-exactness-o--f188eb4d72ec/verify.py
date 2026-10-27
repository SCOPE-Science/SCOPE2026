"""Finite exact-algebra diagnostics for polynomial-pullback Bergman orthogonality.

This is a diagnostic, not a replacement for the general proof in RESULT.md.
Run with python verify.py; requires sympy.
"""
import sympy as S

z,w=S.symbols('z w')
cases=[z+2,z**2+z+1,z**3+2*z+1,z**4+z**3-2*z+3,z**5+z**2+1]
count=0
for P in cases:
    P=S.Poly(P,z)
    d=P.degree()
    for m in range(4):
        n=d*(m+1)-1
        q=S.Poly(S.diff(P.as_expr(),z)*P.as_expr()**m/d,z)
        assert q.degree()==n and q.LC()==1
        for j in range(n):
            rem=S.rem(z**j,P.as_expr()-w,z)
            trace=S.Poly(S.expand(rem),z).nth(d-1)
            if trace!=0:
                assert S.Poly(trace,w).degree()<m, (P,m,j,trace)
            count+=1
            # The same trace equals the coefficient of 1/z at infinity.
            # Expand in u=1/z without floating point operations.
            u=S.Symbol('u')
            expr=S.cancel(z**j/(P.as_expr()-w)).subs(z,1/u)
            residue=S.series(expr,u,0,2).removeO().expand().coeff(u,1)
            assert S.simplify(residue-trace)==0,(P,m,j,trace,residue)

# Exact integral normalization for disk |w| <= R follows directly:
# \int_{|w|<=R} |w|^(2m) dA = pi*R^(2m+2)/(m+1).
# Finite polynomial identity for monic derivative minimizer:
for d in range(1,7):
    for k in range(1,5):
        n=d*k
        P=z**d+2*z+3 if d>1 else z+3
        q=S.expand(S.diff(P,z)*P**(k-1)/d)
        assert S.Poly(q,z).LC()==1 and S.degree(q,z)==n-1
        assert S.simplify(S.diff(P**k,z)-n*q)==0
print('CHECK_OK: %d exact polynomial-trace, Laurent-residue and derivative identities' % count)
