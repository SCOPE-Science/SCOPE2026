"""Independent checks of an exit-time variance transition for a run-and-tumble particle.

Dependencies: sympy, mpmath.  Run with `python verify_escape_variance.py`.
The infinite-parameter claims rest on the accompanying analytic proof.
"""
import sympy as sp
import mpmath as mp
x, a, g = sp.symbols('x a g', positive=True)
checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

# Exact backward generator for moments of the first exit time:
#  +-partial_x u_n^+- + (a/2)(u_n^mp - u_n^pm) = -n u_(n-1)^pm.
# Left wall stuck-inward state detaches after Exp((a+g)/2) wait.
ss = [sp.Integer(2)]
dd = [sp.Integer(0)]
for n in (1, 2):
    C, E = sp.symbols('C E')
    d = sp.integrate(-n*ss[-1], x) + C
    s = sp.integrate(-n*dd[-1] + a*d, x) + E
    bcs = [d.subs(x, -1) + n/(a+g)*(ss[-1]-dd[-1]).subs(x, -1),
           (s+d).subs(x, 1)]
    sol = sp.solve(bcs, (C, E))
    dd.append(sp.factor(d.subs(sol)))
    ss.append(sp.factor(s.subs(sol)))
    check(sp.simplify(sp.diff(dd[n],x)+n*ss[n-1])==0)
    check(sp.simplify(sp.diff(ss[n],x)+n*dd[n-1]-a*dd[n])==0)
    check(sp.simplify(dd[n].subs(x,-1)+n/(a+g)*(ss[n-1]-dd[n-1]).subs(x,-1))==0)
    check(sp.simplify((ss[n]+dd[n]).subs(x,1))==0)

m1 = sp.factor(ss[1].subs(x,0)/2)
m2 = sp.factor(ss[2].subs(x,0)/2)
variance = sp.factor(m2-m1**2)
m1_expected = (3*a*a+3*a*g+6*a+4*g+2)/(2*(a+g))
var_expected = (15*a**4+30*a**3*g+60*a**3+15*a*a*g*g+92*a*a*g+72*a*a + 32*a*g*g+60*a*g+48*a +6*g*g+12*g+18)/(6*(a+g)**2)
check(sp.simplify(m1-m1_expected)==0)
check(sp.simplify(variance-var_expected)==0)
P = (15*a**4+(45*g+30)*a**3+(45*g*g+90*g)*a*a
     +(15*g**3+76*g*g+42*g-24)*a
     +16*g**3+24*g*g+12*g-18)
check(sp.simplify(sp.diff(variance,a)-P/(3*(a+g)**3))==0)
check(sp.simplify(P.subs(a,0)-2*((2*g+1)**3-10))==0)
check(sp.simplify(sp.diff(m1,a)-sp.Rational(3,2)-(g-1)/(a+g)**2)==0)
check(sp.simplify((15*g**3+76*g*g+42*g-24).subs(g,sp.Rational(1,2))-sp.Rational(143,8))==0)

# Independent matrix-exponential backward-transform calculation.
mp.mp.dps=65

def laplace_transform(z, alpha, gamma):
    flip=(alpha+gamma)/(alpha+gamma+2*z)
    M=mp.matrix([[z+alpha/2,-alpha/2],[alpha/2,-z-alpha/2]])
    u0=mp.matrix([1,flip])
    transfer=mp.expm(2*M)
    norm=(transfer*u0)[0]
    start=mp.expm(M)*u0
    return (start[0]+start[1])/(2*norm)

samples=[('1','0'),('1','0.1'),('0.15','0.55'),('0.1','0.57'),('0.2','0.6'),('3.5','2')]
for aa,gg in samples:
    aa=mp.mpf(aa);gg=mp.mpf(gg)
    f=lambda z:laplace_transform(z,aa,gg)
    first=-mp.diff(f,mp.mpf('0'),1)
    second=mp.diff(f,mp.mpf('0'),2)
    v=second-first**2
    E=sp.lambdify((a,g),m1,'mpmath')(aa,gg)
    V=sp.lambdify((a,g),variance,'mpmath')(aa,gg)
    check(abs(first-E)<mp.mpf('1e-40'))
    check(abs(v-V)<mp.mpf('1e-40'))
    check(abs(f(mp.mpf('0'))-1)<mp.mpf('1e-40'))

# Exact one-positive-root argument is in the accompanying proof; numerical
# sampling here detects implementation errors, not logical counterexamples.
for gg in ['0','0.1','0.3','0.5','0.55','0.57','0.5775','0.6','0.8','2']:
    gv=mp.mpf(gg)
    coeff=[15,45*gv+30,45*gv**2+90*gv,15*gv**3+76*gv**2+42*gv-24,16*gv**3+24*gv**2+12*gv-18]
    positives=sorted(float(mp.re(r)) for r in mp.polyroots(coeff,maxsteps=1000,error=False) if abs(mp.im(r))<mp.mpf('1e-30') and mp.re(r)>0)
    if gv<(mp.root(10,3)-1)/2:
        check(len(positives)==1)
    else:
        check(len(positives)==0)

print('PASS',checks,'exact symbolic, independent Laplace, and parameter-sample checks')
print('mean threshold:',float((mp.sqrt(7)-1)/3))
print('variance threshold:',float((mp.root(10,3)-1)/2))
