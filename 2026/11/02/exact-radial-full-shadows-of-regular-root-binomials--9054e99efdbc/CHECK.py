from sympy import symbols,Poly,diff,expand
x,y=symbols('x y')
tests=0
for d in range(2,7):
 for n in range(1,8):
  q=Poly((y-1)**n,y);r=0
  f=(x**d-1)**n
  for m in range(d*n):
   rec=expand(x**r*q.as_expr().subs(y,x**d))
   if expand(rec-diff(f,x,m))!=0:raise AssertionError((d,n,m,'reconstruction'))
   if q.degree()>0:
    roots=q.intervals(eps=__import__('sympy').Rational(1,10**6))
    assert sum(mult for _,mult in roots)==q.degree(),(d,n,m)
    assert all(0<interval[0] and interval[1]<=1 for interval,mult in roots),(d,n,m,roots)
   if m<d*n-1:
    if r>0:q=Poly(r*q.as_expr()+d*y*q.diff().as_expr(),y);r-=1
    else:q=Poly(d*q.diff().as_expr(),y);r=d-1
   tests+=1
print('CHECK_OK:', tests,'exact symbolic descendant identities and rational isolating intervals')
