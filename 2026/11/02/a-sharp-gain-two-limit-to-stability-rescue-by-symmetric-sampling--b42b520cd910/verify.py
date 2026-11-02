"""Exact-algebra checks for the scalar sampled-feedback jitter frontier."""
import sympy as S
from fractions import Fraction as Q

k, q, c, s, t = S.symbols('k q c s t', real=True)
F = (k+1)**2*(2*c*c-1)*q*q - 2*k*(k+1)*q*c + k*k-1
V = F+1
assert S.expand(F.subs({q:(k-1)/(k+1)})) == S.expand(2*(k-1)*(c-1)*((k-1)*c-1))
assert S.factor(S.discriminant(F,q)-4*(k+1)**2*((k*k-1)-(k*k-2)*c*c))==0
assert S.factor((k*k-1+k*s+s*s/2)-(k-1)**2-(s+2)*(2*k+s-2)/2)==0
# Exact two-interval moment identity using e^d=t and e^-d=1/t.
mc=(k+1)*q*t-k
mp=(k+1)*q/t-k
assert S.factor(((mc*mc+mp*mp)/2-V.subs(c,(t+1/t)/2)))==0
kw,cw,qw=S.Rational(3,2),S.Rational(6,5),S.Rational(19,100)
vw=S.factor(V.subs({k:kw,c:cw,q:qw}))
assert vw==S.Rational(38567,40000)
assert S.factor(((kw+1)*qw-kw))==-S.Rational(41,40)
assert S.Rational(41,40)**2==S.Rational(1681,1600)
assert S.factor(F.subs({k:kw,c:cw,q:(kw-1)/(kw+1)}))==-S.Rational(2,25)
# Under k>=2, q <= (k-1)/(k+1), c>=1, the exact algebraic
# certificate in the proof excludes V<1, not just this finite test.
count=0
for nk in range(2,16):
    kk=Q(nk,1)
    bound=(kk-1)/(kk+1)
    for nq in range(1,101):
        qq=bound*Q(nq,100)
        for nc in range(1,31):
            cc=Q(nc+9,10)
            vv=(kk+1)**2*(2*cc*cc-1)*qq*qq-2*kk*(kk+1)*qq*cc+kk*kk
            assert vv>=1
            count+=1
print('PASSED symbolic identities, exact witness, and',count,'rational no-go evaluations')
