"""Reproducibility checks for the physical-time period in a quintic global-center family.

The universal inequalities and asymptotic limit still rely on the proof in RESULT.md;
finite numerical tests here are diagnostics, not substitutions for that proof.
"""
import sympy as sp
import mpmath as mp

x,y,al,be,z=sp.symbols('x y alpha beta z',real=True)
p=sp.exp(al*x**4/4)
# V'(x) = p(x)^2 x(1+beta*x^4).
Hx=sp.diff(p*p*y*y/sp.Integer(2),x)+p*p*x*(1+be*x**4)
Hy=p*p*y
assert sp.simplify(Hx*y+Hy*(-x-al*x**3*y*y-be*x**5))==0
Bprime=1-al*x**3*sp.Symbol('B')
c=x/(1+al*x**4)
assert sp.factor(sp.diff(c,x)+al*x**3*c-1)==-4*al*x**4/(1+al*x**4)**2
# Coordinate change: x = z-alpha*z**5/20+O(z**9).
x_inv=z-al*z**5/20
h=(sp.exp(al*x_inv**4/4)*x_inv*(1+be*x_inv**4)).series(z,0,7).removeO().expand()
assert sp.simplify(h-(z+(be+al/sp.Integer(5))*z**5))==0
assert sp.integrate(1+sp.sin(z)**2+sp.sin(z)**4,(z,0,sp.pi/2))==sp.Rational(15,16)*sp.pi

mp.mp.dps=38

def period(a,b,A):
    a=mp.mpf(a);b=mp.mpf(b); A=mp.mpf(A)
    def vdiff(t):
        # Scaled coordinate x=A(1-t), positive-energy difference.
        return mp.quad(lambda w: mp.exp(a*(A*(1-w))**4/2)*(A*(1-w))*(1+b*(A*(1-w))**4)*A,[0,t])
    def integrand(phi):
        xx=A*mp.sin(phi)
        # Smooth turning-point singularity by x=A*sin(phi).
        if mp.pi/2-phi < mp.mpf('1e-12'):return 1/mp.sqrt(1+b*A**4)
        return mp.exp(a*xx**4/4)*A*mp.cos(phi)/mp.sqrt(2*vdiff(1-xx/A))
    return 4*mp.quad(integrand,[0,mp.pi/4,mp.pi/2])

# Formula check via a single smooth integral for the pure quintic axis.
def pure_period(b,A):
    b=mp.mpf(b);A=mp.mpf(A)
    return 4*mp.quad(lambda phi: 1/mp.sqrt(1+b*A**4*(1+mp.sin(phi)**2+mp.sin(phi)**4)/3),[0,mp.pi/2])

for b in ['0','1','2']:
    assert abs(pure_period(b,mp.mpf('0.002'))/(2*mp.pi)-(1-5*mp.mpf(b)*mp.mpf('0.002')**4/16))<mp.mpf('1e-18')

for a,b,A in [(1,0,2),(1,1,2),(0,1,3)]:
    # Numerical IVP checks use a conservative-energy quadrature at moderate A.
    if a==0:
        t=pure_period(b,A)
    else:
        t=period(a,b,A)
    assert t>0
    print('sample',a,b,A,mp.nstr(t,14))

# Exact high-amplitude beta=0 and alpha=0 constants from the written theorem.
I=mp.quad(lambda u: 1/mp.sqrt(1-u**6),[0,1]); B=mp.beta(mp.mpf(1)/6,mp.mpf(1)/2)/6
assert abs(I-B)<mp.mpf('1e-18')
assert abs(mp.quad(lambda t:mp.exp(-t)/mp.sqrt(1-mp.exp(-2*t)), [0,1,mp.inf])-mp.pi/2)<mp.mpf('1e-18')
print('CHECK_OK')
