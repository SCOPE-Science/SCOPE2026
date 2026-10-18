"""Independent exact-algebra and high-precision checks for a two-group renewal vaccination theorem.

Python 3, SymPy, mpmath required. Scientific evidence only; not an exhaustive
verification of every real parameter or a substitute for the analytic proof.
"""
import sympy as S
import mpmath as M

checks = 0

def require(condition, explanation):
    global checks
    if not bool(condition):
        raise AssertionError(explanation)
    checks += 1

def equal(a, b, explanation):
    require(S.simplify(S.expand((a - b).rewrite(S.exp))) == 0, explanation)

c, alpha, x, tau, nu = S.symbols('c alpha x tau nu', positive=True, real=True)
z = S.Symbol('z')
q = S.symbols('q', real=True)
t = alpha / 2
F = lambda y: (1+y)*S.exp(-2*y)

# Renewal identity integrating the Erlang-2 survival function.
y = S.symbols('y', positive=True)
u = S.symbols('u', positive=True)
rate = S.symbols('rate', positive=True)
survival = S.exp(-2*rate*u)*(1+2*rate*u)
reward = S.integrate(survival, (u, tau, S.oo))
equal(reward, S.exp(-2*rate*tau)*(tau+1/rate), 'renewal reward')
equal(reward*rate, F(rate*tau), 'mean susceptibility')
equal(S.diff(F(c),c), -S.exp(-2*c)*(1+2*c), 'F prime')
equal(S.diff(F(c),c,2), 4*c*S.exp(-2*c), 'F double prime')

# Exact two-group characteristic polynomial.
a, b = S.symbols('a b', positive=True, real=True)
K = S.Matrix([[1-t,t],[t,1-t]])
Q = K*S.diag(a,b)
char = S.expand(Q.charpoly(z).as_expr())
equal(char, z*z - (1-t)*(a+b)*z+(1-alpha)*a*b, 'char polynomial')

m = (a+b)/2
d = (a-b)/2
D = S.simplify(t*t*m*m+(1-2*t)*d*d)
equal(D, ((1-t)**2*(a-b)**2+alpha*alpha*a*b)/4, 'nonnegative root discriminant')

F1 = S.diff(F(c),c)
F2 = S.diff(F(c),c,2)
H = S.simplify(c*c*(F2+2*(1-alpha)/alpha*F1**2/F(c)))
Hformula = c*c*S.exp(-2*c)*(4*c+2*(1-alpha)*(1+2*c)**2/(alpha*(1+c)))
equal(H,Hformula,'Hessian formula')
ac = 2-1/(1+2*c+2*c*c)
require(S.simplify(ac.subs(c,S.Rational(3,8)))==S.Rational(98,65),'critical alpha')
equal(H.subs({c:S.Rational(3,8),alpha:S.Rational(3,2)}),3*S.exp(-S.Rational(3,4))/1408,'example second derivative')
require(S.Rational(3,2)<S.Rational(98,65),'strict local min')

# Exact characteristic comparison at concentrated allocation.
w=S.symbols('w',positive=True)
a_star = S.Rational(7,4)*w*w
P=S.expand(z*z-(1+a_star)*z/4-a_star/2)
zfair=S.Rational(11,8)*w
equal(S.expand(P.subs(z,zfair)),w*(130*w-44-77*w*w)/128,'characteristic polynomial comparison')
low=S.Rational(19339,40960)
require(low>S.Rational(47,100),'alternating Taylor lower bound')
# Upper bound e^-3/4 < 1/2: e^3/4 > 1 + 3/4 + (3/4)^2/2 > 2.
require(1+S.Rational(3,4)+S.Rational(9,32)>2,'upper exponential bound')
require(S.simplify((130*w-44-77*w*w).subs(w,S.Rational(47,100)))==S.Rational(907,10000),'quadratic at lower endpoint')
require(130-154*S.Rational(1,2)>0,'quadratic monotonicity')

# Verify memoryless renewal exactly and perfectly-crossing Erlang case.
s1=S.exp(-c*(1+x))
s2=S.exp(-c*(1-x))
expm=(s1+s2)/2
expd=(s1-s2)/2
memoryless=S.exp(-c)*((1-t)*S.cosh(c*x)+S.sqrt(t*t+(1-t)**2*S.sinh(c*x)**2))
equal(expm,S.exp(-c)*S.cosh(c*x),'exponential average')
equal(expd,-S.exp(-c)*S.sinh(c*x),'exponential difference')
equal((s1*s2).subs(x,0),S.exp(-2*c),'exponential product')
equal(F(c*(1+x))*F(c*(1-x)),S.exp(-4*c)*((1+c)**2-c*c*x*x),'Erlang product')

M.mp.dps=60
C=M.mpf(3)/8
Al=M.mpf(3)/2

def ff(yy): return (1+yy)*M.exp(-2*yy)
def pf(s, r, t):
    return ((1-t)*(s+r)+M.sqrt((1-t)**2*(s+r)**2-4*(1-2*t)*s*r))/2
fair=ff(C)
concentrated=pf(ff(2*C),ff(0),Al/2)
require(fair>concentrated,'certified example spectral direction (supporting check)')
require(abs(fair-M.mpf('0.64950401001889522231481400754699338'))<M.mpf('1e-30'),'fair high precision')
require(abs(concentrated-M.mpf('0.64862411761405242572429116315949340'))<M.mpf('1e-30'),'concentrated high precision')
# Budget consistency and symmetry at many admissible allocations.
for j in range(101):
    xx=M.mpf(j)/100
    n1=1+xx; n2=1-xx
    require(abs((n1+n2)/2-1)<M.mpf('1e-50'),'dose budget')
    require(abs(pf(ff(C*n1),ff(C*n2),Al/2)-pf(ff(C*n2),ff(C*n1),Al/2))<M.mpf('1e-50'),'two-group symmetry')
# Verify strict local min for a few tiny perturbations, not as a proof.
for eps in [M.mpf('1e-2'),M.mpf('1e-3'),M.mpf('1e-4'),M.mpf('1e-5')]:
    require(pf(ff(C*(1+eps)),ff(C*(1-eps)),Al/2)>fair,'local min sample')

print(f'PASS {checks} exact-symbolic and high-precision checks')
print('fair spectral factor:',M.nstr(fair,35))
print('concentrated spectral factor:',M.nstr(concentrated,35))
print('strict spectral gap:',M.nstr(fair-concentrated,30))
