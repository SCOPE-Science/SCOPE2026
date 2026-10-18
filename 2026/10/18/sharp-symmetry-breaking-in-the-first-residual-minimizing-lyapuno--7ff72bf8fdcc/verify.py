"""Reproducibility checks for the two-mode ADI residual-shift bifurcation.

Run: python verify.py
Uses only Python's standard library. The paper's symbolic proof, not the
finite tests below, establishes the global statements.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks = 0

def require(cond, detail):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(detail)

def f_of_p(a, b, p):
    return ((a-p)/(a+p))**2 + ((b-p)/(b+p))**2

def opt(a, b):
    k = b/a
    c = (sqrt(k)-1)/(sqrt(k)+1)
    x = c*c
    if x <= 1/3:
        return (sqrt(a*b),), 2*x
    w = (3*x-1)/(x*(3-x))
    z = sqrt(w)
    g = sqrt(a*b)
    return (g*(1-z)/(1+z), g*(1+z)/(1-z)), (6*x-x*x-1)/(4*x)

# Exact arithmetic: ADI residual is the outer product of the Cayley factor.
for a,b,p in [(F(1),F(49),F(7)), (F(2),F(5),F(3)),
              (F(1),F(9),F(3)), (F(3),F(11),F(2))]:
    w = [F(a-p,a+p), F(b-p,b+p)]
    X = [[2*p/((a_i+p)*(a_j+p)) for a_j in (a,b)]
         for a_i in (a,b)]
    R = [[F(1)- (a_i+a_j)*X[i][j] for j,a_j in enumerate((a,b))]
         for i,a_i in enumerate((a,b))]
    for i in range(2):
        for j in range(2):
            require(R[i][j] == w[i]*w[j], 'ADI residual factor')
    require(sum(wi*wi for wi in w) == f_of_p(a,b,p),'residual norm')

# Exact rational identity and derivative formula, verified at many rational arguments.
# The proof establishes identity for indeterminates, not merely these samples.
for ci in range(1,10):
    c = F(ci,11)
    for zi in range(-10,11):
        z=F(zi,13)
        w=z*z; x=c*c
        f=((z-c)/(1-c*z))**2 + ((z+c)/(1+c*z))**2
        f_reduced=2*(x+(1-4*x+x*x)*w+x*w*w)/(1-x*w)**2
        require(f == f_reduced, 'Cayley coordinate transformation')
        deriv_formula=2*(1-x)*((1-3*x)+x*(3-x)*w)/(1-x*w)**3
        # Exact formal quotient-rule derivative of N(w)/D(w).
        N=2*(x+(1-4*x+x*x)*w+x*w*w)
        Nprime=2*((1-4*x+x*x)+2*x*w)
        D=(1-x*w)**2
        Dprime=-2*x*(1-x*w)
        require((Nprime*D-N*Dprime)/D**2 == deriv_formula,'derivative identity')

c=F(3,4); x=c*c
wstar=(3*x-1)/(x*(3-x))
minval=(6*x-x*x-1)/(4*x)
require(wstar==F(176,351),'exact minimizer square at k=49')
require(minval==F(527,576),'exact minimum at k=49')
require(2*x==F(9,8),'exact geometric-mean residual at k=49')
require(minval < 2*x,'strict degradation at k=49')

kstar=(2+sqrt(3))**2
for k in (1.001,2.,4.,9.,13.,13.9,kstar*0.999):
    shifts, target=opt(1.,k)
    require(len(shifts)==1,'unsplit phase')
    require(isclose(shifts[0],sqrt(k),rel_tol=1e-13),'center optimum')
    require(isclose(f_of_p(1.,k,shifts[0]),target,rel_tol=2e-12,abs_tol=1e-14),'center minimum')
for k in (kstar*1.001,15.,20.,49.,100.,1000.):
    shifts, target=opt(1.,k)
    require(len(shifts)==2,'split phase')
    require(shifts[0] < sqrt(k) < shifts[1], 'two-sided shifts')
    require(isclose(shifts[0]*shifts[1],k,rel_tol=1e-10),'reflection product')
    for p in shifts:
        require(isclose(f_of_p(1.,k,p),target,rel_tol=2e-12),'split minimum')
        require(f_of_p(1.,k,p) < f_of_p(1.,k,sqrt(k)), 'center worsens')
        for factor in (0.96,0.99,1.01,1.04):
            require(f_of_p(1.,k,p*factor) > target-1e-10,'local optimality')

# Numerical sweep on compact intervals merely illustrates global proof.
for k in (2.,10.,49.,100.):
    shifts, best = opt(1.,k)
    for i in range(801):
        p=10**(-3 + 7*i/800)
        require(f_of_p(1.,k,p) >= best-1e-10, 'global scan')

# Asymptotic twofold disadvantage of the spectral minimax shift.
for k in (100.,1000.,10**5,10**8):
    shifts,best=opt(1.,k)
    ratio=f_of_p(1.,k,sqrt(k))/best
    require(1 < ratio < 2, 'finite ratio strict bound')
require(f_of_p(1.,10**8,10**4)/opt(1.,10**8)[1] > 1.99,
        'approach to sharp twofold loss')
print('PASS:',checks,'exact-rational and numerical consistency checks')
