from sympy import symbols, hermite_prob, assoc_laguerre, factorial, Rational, simplify, Poly, nroots, sqrt, S
x,t=symbols('x t')
checks=0
for n in range(2,15):
 m=n//2; alpha=Rational(-1,2) if n%2==0 else Rational(1,2)
 for b in [-10,-1,0,1,3,n-1,n,n+1,2*n+3]:
  pol=hermite_prob(n,x)+b*hermite_prob(n-2,x)
  expr=(-1)**m*2**m*factorial(m)*x**(n%2)*(assoc_laguerre(m,alpha,x*x/2)-Rational(b,2*m)*assoc_laguerre(m-1,alpha,x*x/2))
  assert simplify(pol-expr)==0,(n,b)
  checks+=1
 # critical coefficient of x² (even), x³ odd and higher
 bc=n-1 if n%2==0 else n
 p=Poly(hermite_prob(n,x)+bc*hermite_prob(n-2,x),x)
 z=n%2+2
 assert all(p.nth(i)==0 for i in range(z))
 assert p.nth(z)!=0
 checks+=1
 # local slope use derivative of laguerre quotient at zero
 R=assoc_laguerre(m,alpha,t)/assoc_laguerre(m-1,alpha,t)
 r0=R.subs(t,0)
 assert simplify(2*m*r0-bc)==0
 assert simplify(-2*m*R.diff(t).subs(t,0)-2*(m+alpha)/(alpha+1))==0
 checks+=2
 # numeric zeros at several b levels
 for eps in [Rational(1,4),Rational(3,2),Rational(11,1)]:
  q=Poly(hermite_prob(n,x)+(bc+eps)*hermite_prob(n-2,x),x)
  roots=q.nroots(maxsteps=200)
  nonreal=[complex(z) for z in roots if abs(float(z.as_real_imag()[1]))>1e-9]
  assert len(nonreal)==2,(n,eps,nonreal)
  assert max(abs(z.real) for z in nonreal)<1e-6
  yy=nonreal[0].imag**2
  c=float((alpha+1)/(m+alpha))
  assert yy >= c*float(eps)-1e-7,(n,eps,yy,c)
  assert yy <= float(eps)+1e-7,(n,eps,yy)
  checks+=1
print('CHECK_OK',checks)
