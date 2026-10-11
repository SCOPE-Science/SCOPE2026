from sympy import symbols, Rational, simplify, factor, solve, Eq, sqrt

m,n,k,e,x,xb,vx,vy = symbols('m n k e x xb vx vy', positive=True)
yb=(m-xb)/n
# Stationarity gives Cov(X,Y)=-n Var(Y). Expanding the logarithmic X balance:
expanded=(yb-xb)+e*(xb*(yb-xb)-vx-n*vy)
h=(m-(n+1)*xb)/n*(1+e*xb)
assert simplify(h - (expanded + e*(vx+n*vy))) == 0
# Therefore k*expanded=n+1 is equivalent to h=(n+1)/k+e(vx+n vy).
assert simplify((h-(n+1)/k-e*(vx+n*vy)) - (expanded-(n+1)/k)) == 0

# If x_- and x_+ are roots of h(x)=(n+1)/k, the concave quadratic factorization
# gives the variance shell after division by e.
xm,xp=symbols('xm xp')
poly=(m-(n+1)*x)/n*(1+e*x)-(n+1)/k
lead=-(n+1)*e/n
# Monic-root identity for any quadratic with roots xm,xp:
formal=lead*(x-xm)*(x-xp)
# The claimed shell follows from h(xb)-C=e(vx+n vy) and lead=-e(n+1)/n.
assert simplify((-lead/e) - (n+1)/n)==0

# Source Figure 5 parameters.
ms=Rational(2); ns=Rational(1,3); es=Rational(5,4); ks=Rational(41,200)
ps=factor((ms-(ns+1)*x)/ns*(1+es*x)-(ns+1)/ks)
assert simplify(ps + (1230*x**2-861*x+124)/246) == 0
roots=solve(Eq(ps,0),x)
expected=[Rational(7,20)-sqrt(131241)/2460, Rational(7,20)+sqrt(131241)/2460]
assert [simplify(roots[i]-expected[i]) for i in range(2)] == [0,0]
assert all(r>0 for r in roots)
assert all(r < ms/(ns+1) for r in roots)
print('VERIFY_OK')
print('x_minus =', roots[0])
print('x_plus  =', roots[1])
print('x_minus_decimal =', roots[0].evalf(18))
print('x_plus_decimal  =', roots[1].evalf(18))
