"""Exact symbolic reconstruction of stationary directional third moments.

Requires SymPy (see requirements.txt). Run: python verify.py
No simulation or numerical root-finding is used as a substitute for a proof.
"""
from itertools import product
import sympy as S

r,p=S.symbols('r p', positive=True)
Q=r**7+9*r**6+38*r**5+84*r**4-402*r**2-567*r-123
P=(r**11+15*r**10+110*r**9+610*r**8+1985*r**7
    -2133*r**6-45871*r**5-165861*r**4-262410*r**3
    -166290*r**2-18999*r-9957)

# Generator identity for k>=1 and nonnegative Fourier index n:
# (r+k+n^2) M[k,n] = (kp/2)(M[k-1,n-1]+M[k-1,n+1])
#                      + k(k-1) M[k-2,n].
M={(0,n):(S.Integer(1) if n==0 else r/(r+n*n)) for n in range(5)}
for k in range(1,4):
    for n in range(4-k):
        val=(k*p*S.Rational(1,2)*(M[k-1,abs(n-1)]+M[k-1,n+1])
             +(k*(k-1)*M[k-2,n] if k>=2 else 0))/(r+k+n*n)
        M[k,n]=S.factor(val)

m1=p*r/(r+1)**2
m2=2/(r+2)+2*p**2/((r+2)*(r+4))
m3=12*p*r*(r+2)/((r+1)**2*(r+3)**2)+6*p**3*r*(r+5)/((r+1)**2*(r+3)**2*(r+9))
for k,expected in ((1,m1),(2,m2),(3,m3)):
    assert S.cancel(M[k,0]-expected)==0, ('raw moment',k)
C=S.factor(m3-3*m1*m2+2*m1**3)
A=6*r*(r*r+2*r-1)/((r+1)**2*(r+2)*(r+3)**2)
B=2*r*Q/((r+1)**6*(r+2)*(r+3)**2*(r+4)*(r+9))
assert S.cancel(C-p*(A+p*p*B))==0
assert S.cancel(C.subs(r,1)-p*(5-p*p)/80)==0

# Independent stationary reset-age reconstruction using Gaussian angles.
# T~Exp(r); A_T=int_0^T exp(-(T-s))cos(sqrt(2)W_s)ds.
EA=r/(r+1)**2
EA2=r/(r+2)**2*(1/r+1/(r+4))
assert S.cancel(EA2-2/((r+2)*(r+4)))==0
# Triple ordered cosines: eight Gaussian-sign terms, integrated in s1, s2-s1, s3-s2.
ordered_sum=sum(
    1/((r+(a+b+c)**2)*(r+1+(b+c)**2))
    for a,b,c in product((-1,1),repeat=3))
EA3=S.Rational(6,8)*r*ordered_sum/(r+3)**2
assert S.cancel(EA3-6*r*(r+5)/((r+1)**2*(r+3)**2*(r+9)))==0
assert S.cancel(m1-p*EA)==0
assert S.cancel(m2-(2/(r+2)+p*p*EA2))==0
assert S.cancel(m3-(p**3*EA3+3*p*(EA-r/(r+3)**2)))==0

# Exact monotonicity certificate.
H=-3*(r*r+2*r-1)*(r+1)**4*(r+4)*(r+9)/Q
assert S.cancel(S.diff(H,r)+3*(r+1)**3*P/Q**2)==0
assert Q.subs(r,0)<0 and Q.subs(r,1)<0 and Q.subs(r,2)>0
qsigns=[S.sign(x) for x in S.Poly(Q,r).all_coeffs() if x!=0]
assert sum(a!=b for a,b in zip(qsigns,qsigns[1:]))==1
# On (0,2], positive terms in P are bounded by 15124*r^5,
# while the explicit negative term alone is -45871*r^5.
assert 4*(2**4+15*2**3+110*2**2+610*2+1985)==15124
assert 15124<45871
# All other terms in P are strictly negative for r>0.
assert S.factor(S.limit(H,r,S.sqrt(2)-1,dir='+'))==0
assert S.limit(H,r,S.sqrt(2)-1,dir='+')==0
# Finite reference values / direct sample checks (not uniqueness evidence).
for rv,pv,sign in [(S.Rational(1,4),2,-1),(1,2,1),(1,3,-1),(3,3,1)]:
    actual=S.sign(C.subs({r:rv,p:pv}))
    assert actual==sign,(rv,pv,actual)
print('PASS: generator moments, independent renewal-age moments, cumulant,')
print('      exact polynomial boundary, positive-root count, and monotonicity certificate.')
