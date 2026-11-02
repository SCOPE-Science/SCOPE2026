import sympy as S
z,e,a,b,c,h=S.symbols('z e a b c h',real=True)
v=1+e*z
L=(a-1)*S.log(v)-b*v-1/(2*e**2)*S.log(1+v)-(1/e**2+c/2+h*e**2/2)/(1+v)
series=S.series(L,e,0,4).removeO().expand()
A=[S.expand(series.coeff(e,k)) for k in [1,2,3]]
print('A1',A[0]);print('A2',A[1]);print('A3',A[2])
def gauss(P):
 P=S.Poly(S.expand(P),z)
 v=0
 for (n,),coef in P.terms():
  if n%2==0:v+=coef*S.factorial2(n-1)*8**(n//2) if n else coef
 return S.factor(v)
A1,A2,A3=A
low=S.factor(gauss(z*A1))
third=S.factor(gauss(z*(A3+A1*A2+A1**3/S.Integer(6)))-low*gauss(A2+A1**2/S.Integer(2)))
print('low',low)
print('third full',third)
c0=8*(b-a)
third0=S.factor(third.subs(c,c0))
print('third at c0',third0)
h0=S.solve(third0,h)[0]
print('coefficient h0',S.factor(h0))

assert S.simplify(low-(8*a-8*b+c))==0
assert S.simplify(third0-(16*a-16*b+h-16))==0
assert S.simplify(h0-16*(1+b-a))==0
print('PASS symbolic saddle-coefficient identities')
