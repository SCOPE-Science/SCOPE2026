import sympy as sp

n,y = sp.symbols('n y', real=True)
A=(n+1)*(4*n**2+5*n+2)
B=2*(n+1)*(4*n+3)
C=-n**2+7*n+6
E=sp.expand(A*y**3+B*y**2+C*y+2)
D=(n+1)*y+1
S=(n+1)*(2*n+1)*y**2+2*(n+1)*y-(n-1)
r=sp.cancel(n*y*S/(2*D**3))
# Q(x)/x = r(y), with y=x^n.
assert sp.simplify((r+1)-E/(2*D**3)) == 0

disc=sp.factor(sp.discriminant(E,y))
expected_disc=4*n**6*(n+1)*(4*n**2-63*n-59)
assert sp.expand(disc-expected_disc)==0

Ep=sp.diff(E,y)
H=sp.expand(n*y*Ep-4*D**3)
# At a root E=0, Q'(x)-1 = H/(2D^3).
R=16*n**4-216*n**3-815*n**2-931*n-356
res=sp.factor(sp.resultant(E,H,y))
expected_res=8*n**9*(n+1)**2*R
assert sp.expand(res-expected_res)==0

# Exact n=18 anchor for the outer positive root.
E18=sp.Poly(E.subs(n,18),y)
H18=sp.Poly(H.subs(n,18),y)
assert E18.as_expr()==26372*y**3+2850*y**2-192*y+2
assert E18.eval(sp.Rational(1,28)) == sp.Rational(-113,5488)
assert E18.eval(sp.Rational(1,27)) == sp.Rational(2720,19683)
assert H18.eval(sp.Rational(1,28)) == sp.Rational(293023,5488)
Hp18=sp.diff(H18.as_expr(),y)
assert sp.expand(Hp18)==4189956*y**2+196536*y-3684
assert Hp18.subs(y,sp.Rational(1,28)) > 0
# H'' > 0 for y>0, so H' and H stay positive on [1/28,infinity).
assert sp.diff(Hp18,y).subs(y,sp.Rational(1,28)) > 0

# Resultant factor R has no zero for n>=18: R,R',R'',R''' are positive at 18,
# and R''' is increasing/positive there onward.
Rp=sp.diff(R,n); Rpp=sp.diff(Rp,n); Rppp=sp.diff(Rpp,n)
assert (R.subs(n,18),Rp.subs(n,18),Rpp.subs(n,18),Rppp.subs(n,18)) == (138730,133025,37250,5616)
assert sp.diff(Rppp,n) == 384

# Critical-value ratio threshold used to locate one root on each side of c_tilde.
T=sp.expand((n-1)**2*(2*n+1)-27*(n+1)**2)
assert T.subs(n,17)==212
assert sp.diff(T,n).subs(n,17)>0
assert sp.diff(T,n,2).subs(n,17)>0

print('VERIFY_OK')
