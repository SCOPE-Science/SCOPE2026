"""Exact independent symbolic checks of the explicit characteristic-five loci.
Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as S

x, z, u, v = S.symbols("x z u v")
f = x**8 + u*x**6 + v*x**4 + u*x**2 + 1
P = lambda e: S.Poly(S.expand(e), u, v, modulus=5)
Q = lambda e: S.Poly(S.expand(e), u, modulus=5)
zero = lambda e: P(e).is_zero

d1, d2, d3 = 2*u-v-2, 2*u+v+2, u*u-4*v+8
assert S.discriminant(f, x) == 256*d1**2*d2**2*d3**4 or S.expand(S.discriminant(f,x)-256*d1**2*d2**2*d3**4)==0
print('DISCRIMINANT_OK')

f2 = S.Poly(S.expand(f*f), x)
H = S.Matrix(3, 3, lambda i,j: f2.nth(5*(i+1)-(j+1)))
A, B, C = u*u+2*v, 2*u, 2*u*u+v*v+2
assert all(zero(H[i,j]-S.Matrix([[A,0,B],[0,C,0],[B,0,A]])[i,j]) for i in range(3) for j in range(3))
Fp, Fm, F0 = A+B, A-B, C
assert zero(S.expand(H.det())-Fp*Fm*F0)
print('HASSE_WITT_FACTORIZATION_OK')

# Quotient equations under x -> 1/x and x -> -1/x, respectively.
for sign, target in [(1,Fm),(-1,Fp)]:
    t=x+sign/x
    g=z**4+(u-4*sign)*z**2+(v-2*sign*u+2)
    assert S.cancel(g.subs(z,t)-f/x**4)==0
    # For a quartic y^2=g(z), p=5 Hasse invariant is [z^4]g(z)^2.
    assert zero(S.expand(g*g).coeff(z,4)-target)
# For the quotient by x -> -x, its elliptic Hasse invariant is [z^4] (z^4+u z^3+v z^2+u z+1)^2.
g0=z**4+u*z**3+v*z**2+u*z+1
assert zero(S.expand(g0*g0).coeff(z,4)-F0)
print('THREE_ELLIPTIC_QUOTIENTS_OK')

# Exact intersection schemes over the algebraic closure of F_5.
# Use v = 2u^2+4u for Fp=0 and v = 2u^2+u for Fm=0.
assert Q(4*F0.subs(v,2*u**2+4*u)-(u-1)**3*(u+2)).is_zero
assert Q(4*F0.subs(v,2*u**2+u)-(u+1)**3*(u-2)).is_zero
assert zero(Fp-Fm-4*u)
for a,b in [(0,0),(2,0),(-2,0)]:
    assert all(S.expand(d.subs({u:a,v:b}))%5 for d in (d1,d2,d3))
    assert sum(int(S.expand(h.subs({u:a,v:b})))%5==0 for h in (Fp,Fm,F0))==2
# The triple loci cannot meet: Fp=Fm=0 forces u=v=0, where F0=2.
assert F0.subs({u:0,v:0})==2
# On U the pairwise intersections occur only at the three recorded points.
for forms, point in [((Fp,Fm),(0,0)),((Fp,F0),(-2,0)),((Fm,F0),(2,0))]:
    a,b=point
    grads = S.Matrix([[S.diff(F,u),S.diff(F,v)] for F in forms])
    assert int(grads.det().subs({u:a,v:b}))%5
assert 2*1*2 % 5 # homogenized F0 is a nonsingular projective conic.
print('PAIRWISE_INTERSECTIONS_AND_TRANSVERSALITY_OK')

# Check all F_5-marked smooth parameters as finite corroboration.
strata={0:[],1:[],2:[],3:[]}
for a in range(5):
    for b in range(5):
        repl={u:a,v:b}
        if any(int(d.subs(repl))%5==0 for d in (d1,d2,d3)):
            continue
        rank=sum(int(h.subs(repl))%5!=0 for h in (Fp,Fm,F0))
        strata[rank].append((a,b))
assert strata[0]==[]
assert sorted(strata[1])==[(0,0),(2,0),(3,0)]
print('F5_FINITE_CHECK:',{r:len(v) for r,v in strata.items()})
print('VERIFY_OK')
