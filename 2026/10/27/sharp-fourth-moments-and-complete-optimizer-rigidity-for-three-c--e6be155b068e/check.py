"""Independent arithmetic checks for the three-consecutive-character SU(2) fourth moment.
Run: python3 check.py
Requires sympy; scipy is optional for numerical quadrature.
"""
from fractions import Fraction
from math import comb
import random
import sympy as S

n,t,u=S.symbols('n t u', nonnegative=True)
q=1+t**2+u
P=S.expand(q**2+n*(q+2*t)**2+(u+1+2*t)**2+1+4*(n+1)*u*(t+1)**2+4*u)
A=S.expand(S.diff(P,u).subs(u,0))
C=S.expand(P.subs(u,0))
alpha=S.expand(P).coeff(u,2)
ustar=(t+1)*(2*n*t**3+2*n+2*t**3+4*t**2-t+3)/(2*n*t**2+6*n*t+2*n+t**2+6*t+4)
Rnum=(8*n**2*t**4+32*n**2*t**3+48*n**2*t**2+32*n**2*t+8*n**2
      +15*n*t**4+64*n*t**3+108*n*t**2+96*n*t+31*n
      +7*t**4+36*t**3+60*t**2+64*t+30)
Rden=(4*n*t**4+8*n*t**3+4*n*t**2+8*n*t+4*n
      +3*t**4+12*t**3+8*t**2+8*t+7)
H=((8*n**2+13*n+6)*t**3+(8*n**2+29*n+20)*t**2
   +(-8*n**2-5*n+10)*t-(8*n**2+21*n+13))
assert S.cancel((A*(1+t**2)-2*C)/(A-2*alpha*(1+t**2))-ustar)==0
assert S.cancel(P.subs(u,ustar)/q.subs(u,ustar)**2-Rnum/Rden)==0
assert S.cancel(S.diff(Rnum/Rden,t)+4*(t+1)*(2*n*t**2+6*n*t+2*n+t**2+6*t+4)*H/Rden**2)==0
assert S.simplify(A-2*alpha*(1+t**2)-2*(2*n*t**2+6*n*t+2*n+t**2+6*t+4))==0

# Direct convolution uses only the SU(2) tensor-product index rule.
def fourth_cg(N, coeff):
    z={}
    for i, ai in enumerate(coeff):
        for j, aj in enumerate(coeff):
            for m in range(abs((N+i)-(N+j)),2*N+i+j+1,2):
                z[m]=z.get(m,0)+ai*aj
    return sum(abs(v)**2 for v in z.values())

# An independent route: integrate products of Chebyshev polynomials U_m(v/2)
# against semicircle probability, using Catalan moments of v=2 cos(theta).
v=S.symbols('v',real=True)
U=[S.Integer(1),v]
for j in range(2,12):U.append(S.expand(v*U[-1]-U[-2]))
def moment_poly(poly):
    poly=S.Poly(S.expand(poly),v)
    return sum(c* (S.Integer(comb(k,k//2)//(k//2+1)) if k%2==0 else S.Integer(0))
               for (k,),c in poly.terms())

rng=random.Random(20261018)
checks=4
for N in range(0,9):
    for _ in range(18):
        c=[rng.randint(-3,3)+S.I*rng.randint(-3,3) for _ in range(3)]
        poly=sum(c[j]*U[N+j] for j in range(3))
        exact=moment_poly(S.expand(poly*S.conjugate(poly))**2)
        tensor=S.expand(fourth_cg(N,c))
        assert S.simplify(exact-tensor)==0,(N,c,exact,tensor)
        checks+=1

# Check the compact closed formula against direct Clebsch-Gordan moments.
for N in range(0,20):
    for a,b,c in [(1,1,1),(2,3,4),(1,0,2),(0,2,1),(1,2,0)]:
        direct=fourth_cg(N,[a,b,c]); norm=a*a+b*b+c*c
        rr=S.Rational(a,c) if c else None
        if rr is not None:
            uu=S.Rational(b*b,c*c)
            assert direct*S.Integer(1)==P.subs({n:N,t:rr,u:uu})*c**4
        checks+=1

for N in [0,1,2,3,4,5,10,50,100]:
    poly=S.Poly(H.subs(n,N),t)
    roots=S.nroots(poly,n=20,maxsteps=100)
    pos=[float(S.re(x)) for x in roots if abs(float(S.im(x)))<1e-12 and float(S.re(x))>0]
    assert len(pos)==1 and 0<pos[0]<1
    xx=pos[0]
    uu=float(ustar.subs({n:N,t:xx}))
    assert uu>0
    a=xx/(1+xx*xx+uu)**0.5
    b=uu**0.5/(1+xx*xx+uu)**0.5
    c=1/(1+xx*xx+uu)**0.5
    val=float((Rnum/Rden).subs({n:N,t:xx}))
    assert abs(fourth_cg(N,[a,b,c])-val)<1e-8*max(1,val)
    assert val>=N+3
    checks+=4

# The finite-term high-weight asymptotic is derived from the cubic root expansion.
assert S.simplify(H.subs(t,1))==16*n+23
assert S.limit(Rnum/Rden/n,n,S.oo).subs(t,1)==S.Rational(32,7)
assert S.limit((Rnum/Rden-S.Rational(32,7)*n).subs(t,1-S.Rational(1,2)/n),n,S.oo)==S.Rational(491,98)
assert S.limit(n*(ustar.subs(t,1-S.Rational(1,2)/n)-S.Rational(4,5)),n,S.oo)==S.Rational(8,25)
print(f'PASS: {checks+4} independent exact/symbolic/numerical assertions')
