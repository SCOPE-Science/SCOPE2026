"""Reproduce exact polynomial identities in the inverse starlike Hankel equality theorem.
Install SymPy, then run: python verify_exact.py
"""
import sympy as S
c,g,z,k,y,u,v=S.symbols('c g z k y u v', real=True)
h=z*(c/2+g*z)/(1+c*g*z/2)
p=(1+h)/(1-h)
series=S.series(p,z,0,5).removeO().expand()
coeff=[series.coeff(z,j) for j in range(1,5)]
a2=coeff[0]
a3=(coeff[1]+coeff[0]**2)/2
a4=(coeff[0]**3+3*coeff[0]*coeff[1]+2*coeff[2])/6
a5=(coeff[0]**4+6*coeff[0]**2*coeff[1]+3*coeff[1]**2+8*coeff[0]*coeff[2]+6*coeff[3])/24
A2=-a2;A3=2*a2**2-a3;A4=5*a2*a3-5*a2**3-a4
A5=14*a2**4-21*a3*a2**2+6*a2*a4+3*a3**2-a5
H=S.factor(2*A2*A3*A4-A3**3-A4**2+A3*A5-A2**2*A5)
As=18*c**6+51*g*c**4*(c**2-4)+g**2*c**2*(688-368*c**2+49*c**4)+g**3*(-1152+704*c**2-172*c**4+17*c**6)+g**4*c**2*(c**2-4)**2
assert S.simplify(1152*H-As)==0
assert S.simplify(H.subs(g,-1)-1)==0
assert S.simplify(H.subs(c,0)+g**3)==0
terms=[18*k**3,51*k**2*(k-4),k*(688-368*k+49*k**2),-1152+704*k-172*k**2+17*k**3,k*(k-4)**2]
B=[sum(terms[i]*terms[i+j] for i in range(5-j)) for j in range(5)]
mod_sq=S.expand(B[0]+2*sum(B[j]*S.chebyshevt(j,y) for j in range(1,5)))
P=(36*k**4*y**3+321*k**4*y**2+542*k**4*y+257*k**4-144*k**3*y**3-2136*k**3*y**2-3936*k**3*y-1944*k**3+6000*k**2*y**2+13032*k**2*y+7608*k**2-30752*k*y-14624*k+50688)
assert S.factor(1152**2-mod_sq-8*k*(4-k)*(1+y)*P)==0
expected=[
[[50688,50688,50688,50688],[58752,S.Rational(145504,3),S.Rational(114752,3),28000],[67200,S.Rational(141472,3),32448,23072],[76032,46528,28480,19584],[85248,S.Rational(139712,3),S.Rational(78784,3),19712]],
[[85248,S.Rational(139712,3),S.Rational(78784,3),19712],[94464,S.Rational(139840,3),S.Rational(72128,3),19840],[104064,47328,S.Rational(70720,3),23584],[114048,48672,24768,33120],[124416,50688,32256,69120]]]
for branch,k0 in enumerate([0,2]):
    Q=S.Poly(S.expand(P.subs({k:k0+2*u,y:2*v-1})),u,v)
    M=[[sum(Q.coeff_monomial(u**a*v**b)*S.binomial(i,a)/S.binomial(4,a)*S.binomial(j,b)/S.binomial(3,b) for a in range(i+1) for b in range(j+1)) for j in range(4)] for i in range(5)]
    assert M==expected[branch]
    assert all(x>0 for row in M for x in row)
print('PASS: exact coefficient expansion, determinant, phase identity, positive Bernstein certificates')
