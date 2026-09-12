import sys
sys.path = [p for p in sys.path if p not in ('/tmp','')]
import sympy as sp
s1,s2,b,al,ga,de,J1,J3,J5=sp.symbols('s1 s2 b al ga de J1 J3 J5')
# V(s)=(al s^2+ga s+de)/(s+b); collision numerator:
N = (al*s1**2+ga*s1+de)*(s2+b)-(al*s2**2+ga*s2+de)*(s1+b)
sp.factor(N)
print(sp.factor(N))
# substitute de=-(al J5+ga J3)/J1, b=-J3/J1 ; F = de-al s1 s2 - b(al(s1+s2)+ga)
F = de-al*s1*s2-b*(al*(s1+s2)+ga)
Fsub = sp.simplify(F.subs({de:-(al*J5+ga*J3)/J1, b:-J3/J1}))
print(sp.factor(Fsub))
print(sp.simplify(Fsub + al*(J5-(s1+s2)*J3+s1*s2*J1)/J1))
