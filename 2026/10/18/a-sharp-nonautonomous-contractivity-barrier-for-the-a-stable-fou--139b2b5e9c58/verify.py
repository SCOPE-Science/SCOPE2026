"""Exact symbolic and independent finite-sample checks for an implicit RK decay benchmark.

Run with Python 3 and SymPy installed: python verify.py.
All matrix entries below are rational and are taken from the printed nIRK4 tableau.
The analytical all-parameter conclusions are proved in RESULT.md.
"""
import sympy as sp

x, z = sp.symbols('x z', real=True)
A = sp.Matrix([
    [0, 0, 0, 0],
    [sp.Rational(47, 360), sp.Rational(89, 360), -sp.Rational(19, 360), sp.Rational(1, 120)],
    [sp.Rational(7, 60), sp.Rational(77, 180), sp.Rational(23, 180), -sp.Rational(1, 180)],
    [sp.Rational(1, 8), sp.Rational(3, 8), sp.Rational(3, 8), sp.Rational(1, 8)],
])
b = sp.Matrix([sp.Rational(1, 8), sp.Rational(3, 8), sp.Rational(3, 8), sp.Rational(1, 8)])
c = sp.Matrix([0, sp.Rational(1, 3), sp.Rational(2, 3), 1])
e = sp.ones(4, 1)
assert A.row(0) == sp.zeros(1, 4)
assert A.row(3) == b.T
assert A*e == c
assert sum(b) == 1

rate = sp.diag(*[x*(1-ci) for ci in c])
M = sp.eye(4) + A * rate
D = 13*x**2 + 224*x + 1080
N = -2*(x**3 - 18*x**2 + 158*x - 540)
R = sp.cancel((M.inv()*e)[3])
assert sp.simplify(R - N/D) == 0
assert sp.simplify(M.det() - D/1080) == 0
assert sp.simplify(R-1 + x*(2*x**2-23*x+540)/D) == 0
F = 2*x**3 - 49*x**2 + 92*x - 2160
assert sp.simplify(R+1 + F/D) == 0
assert sp.simplify(sp.diff(F,x)-2*(x-1)*(3*x-46)) == 0
assert F.subs(x,24) == -528 and F.subs(x,25) == 765
assert sp.discriminant(2*x**2-23*x+540,x) < 0
assert sp.simplify(sp.limit(R/x, x, sp.oo)+sp.Rational(2,13)) == 0
assert R.subs(x,25) == -sp.Rational(346,329)
assert R.subs(x,0) == 1

# Original method has [3/3] diagonal Pade stability multiplier, also Gauss 3-stage's.
Raut = sp.factor(1 + z*(b.T*(sp.eye(4)-z*A).inv()*e)[0])
pade33 = (120+60*z+12*z**2+z**3)/(120-60*z+12*z**2-z**3)
assert sp.simplify(Raut-pade33) == 0

# Build the independent three-stage Gauss method by integrating cardinal polynomials.
t = sp.symbols('t', real=True)
cg = sp.Matrix([sp.Rational(1,2)-sp.sqrt(15)/10, sp.Rational(1,2), sp.Rational(1,2)+sp.sqrt(15)/10])
L = [sp.prod([(t-cg[j])/(cg[k]-cg[j]) for j in range(3) if j!=k]) for k in range(3)]
bg = sp.Matrix([sp.simplify(sp.integrate(p,(t,0,1))) for p in L])
Ag = sp.Matrix(3,3,lambda i,j: sp.simplify(sp.integrate(L[j],(t,0,cg[i]))))
assert list(bg) == [sp.Rational(5,18), sp.Rational(4,9), sp.Rational(5,18)]
for i in range(3):
    for j in range(3):
        assert sp.simplify(bg[i]*Ag[i,j]+bg[j]*Ag[j,i]-bg[i]*bg[j]) == 0
Rg = 1+z*(bg.T*(sp.eye(3)-z*Ag).inv()*sp.ones(3,1))[0]
assert sp.simplify(Rg-pade33) == 0

# Cross-check stage equations independently at exact rational sample parameters.
for av in [sp.Rational(1,10), 1, 4, 10, 24, 25, 100, 1000]:
    av=sp.Rational(av)
    ratev=sp.diag(*[av*(1-ci) for ci in c])
    ys=(sp.eye(4)+A*ratev).inv()*e
    # Explicit RK output and stiffly accurate final stage agree.
    yout=1-(b.T*ratev*ys)[0]
    assert sp.simplify(yout-ys[3])==0
    assert sp.simplify(yout-R.subs(x,av))==0
    assert (yout < 1)
    assert (yout > -1) if av<=24 else (yout < -1)

critical = sp.nroots(F, maxsteps=100)[0]
# Sort only real algebraic root; complex order is not guaranteed.
critical = next(sp.re(v) for v in sp.nroots(F) if abs(float(sp.im(v)))<1e-12)
assert 24 < critical < 25
assert abs(float(critical)-24.4268678121564)<1e-11

# Symplectic identity gives Gauss contractivity for EVERY nonnegative rate profile,
# not merely the samples below: E_new-E_old=-2 sum_j b_j rate_j Y_j**2.
for av in [sp.Rational(1,3), 1, 5, 25, 100, 1000]:
    rates = [sp.N(av*(1-v),30) for v in cg]
    y = (sp.eye(3)+Ag*sp.diag(*rates)).evalf(30).inv()*sp.ones(3,1)
    val = sp.N(1-(bg.T*sp.diag(*rates)*y)[0],25)
    assert abs(float(val)) < 1.00000000001

print('PASS: exact nIRK4 table, stage determinant, sharp scalar frontier,')
print('autonomous Pade equivalence, Gauss algebraic identity, and rational checks.')
print('Unique critical parameter:', sp.N(critical, 16))
print('At parameter 25: nIRK4 =',R.subs(x,25),'while exact = exp(-25/2).')
