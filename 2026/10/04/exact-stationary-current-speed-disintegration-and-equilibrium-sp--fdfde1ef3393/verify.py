import sympy as s

x,y,z,alpha,beta,kappa,lam=s.symbols('x y z alpha beta kappa lam', nonzero=True)
fx=x*(y-1)-beta*z
fy=alpha*(1-x**2)-kappa*y
fz=x-lam*z

def L(F):
    return s.expand(s.diff(F,x)*fx+s.diff(F,y)*fy+s.diff(F,z)*fz)

assert s.simplify(L(x**2/s.Integer(2))-(x**2*(y-1)-beta*x*z))==0
assert s.simplify(L(z**2/s.Integer(2))-(x*z-lam*z**2))==0
assert s.simplify(L(y)-fy)==0
assert s.simplify(L(z)-fz)==0

X2,Z2=s.symbols('X2 Z2', positive=True)
left=1+beta*lam*Z2/X2
right=1+beta/lam-beta*(X2-lam**2*Z2)/(lam*X2)
assert s.simplify(left-right)==0

ystar=1+beta/lam
q2=1-(kappa/alpha)*ystar
assert s.simplify(alpha*(1-q2)-kappa*ystar)==0
# On z=x/lam and y=ystar, the x and z equations vanish.
assert s.simplify((x*(ystar-1)-beta*(x/lam)))==0
assert s.simplify(x-lam*(x/lam))==0

print('VERIFY_OK')
