"""Standalone finite checks for the Boolean-cube heat-derivative formulas.

Finite tests are consistency checks, not proofs of the universal theorem.
Run: python verify_hypercube.py
"""
import math
from fractions import Fraction

checks = 0

def check(cond, context):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(context)


def p_from_t(t):
    return -math.expm1(-2*t) / 2


def exact_norm(d, t):
    p = p_from_t(t)
    q = 1-p
    k = min(d-1, math.floor(d*p))
    log_mass=(math.lgamma(d)-math.lgamma(k+1)-math.lgamma(d-k)
              +k*math.log(p)+(d-1-k)*math.log(q))
    return 2*d*math.exp(-2*t+log_mass)


def direct_norm(d, t):
    p = p_from_t(t)
    q = 1-p
    dp = d*p
    pp = math.exp(-2*t)
    return (pp/(p*q))*sum(math.comb(d,k)*abs(k-dp)*(p**k)*(q**(d-k)) for k in range(d+1))


def correction(t, d):
    p = p_from_t(t)
    q = 1-p
    a = (d*p)%1
    b = 1/12 + (6*a*(1-a)-1)/(12*p*q)
    g = math.sqrt(8/math.pi)*t/math.sqrt(math.expm1(4*t))
    return math.sqrt(d)*g*(1+b/d)

# An exact rational check independent of log-gamma or floating arithmetic.
for d in range(1, 13):
    for num, den in [(1,11),(1,7),(1,4),(1,3),(2,5),(3,7),(4,9)]:
        p = Fraction(num,den)
        q = 1-p
        k = min(d-1,(d*num)//den)
        left = sum(math.comb(d,j)*abs(j-d*p)*p**j*q**(d-j) for j in range(d+1))
        right = 2*d*p*q*math.comb(d-1,k)*p**k*q**(d-1-k)
        check(left == right, ('exact-binomial',d,p,left,right))

# Derivative is computed by the difference quotient of the original kernel,
# independently of the sign-collapse identity.
for d in range(1, 9):
    for t in [.006,.024,.1,.23,.42,.73,1.7,2.3]:
        h=2e-6
        def mass(time,k):
            p=p_from_t(time)
            return p**k*(1-p)**(d-k)
        row_norm = sum(math.comb(d,k)*abs((mass(t+h,k)-mass(t-h,k))/(2*h)) for k in range(d+1))
        check(abs(row_norm-exact_norm(d,t)) < 4e-7 * (1+exact_norm(d,t)), ('kernel-difference',d,t,row_norm,exact_norm(d,t)))
        check(abs(direct_norm(d,t)-exact_norm(d,t)) < 2e-12*(1+direct_norm(d,t)),('norm-collapse',d,t))

# At each finite shell transition the two adjacent binomial masses coincide.
for d in range(3, 32):
    for k in range(1, (d-1)//2+1):
        p=Fraction(k,d)
        if 2*p>=1:continue
        q=1-p
        x=math.comb(d-1,k-1)*p**(k-1)*q**(d-k)
        y=math.comb(d-1,k)*p**k*q**(d-k-1)
        check(x==y,('shell-tie',d,k))

# The two-term local binomial expansion: evaluate at half-shells and
# ordinary non-half shell positions, with a justified asymptotic rather
# than asserting exact finite equality.
for d in [100,200,500,1000,2000]:
    for t in [.16,.29,.4,.7,1.1]:
        lhs=t*exact_norm(d,t)
        appr=correction(t,d)
        check(abs(lhs-appr)/(lhs) <= 10/d**2,('Stirling-remainder-envelope',d,t,lhs,appr))

# Sharp asymptotic optimizer and half-shell lattice phase.
def solve_tstar():
    a,b=.2,.5
    for _ in range(80):
        m=(a+b)/2
        if 1-math.exp(-4*m)-2*m>0:a=m
        else:b=m
    return (a+b)/2

tstar=solve_tstar()
cstar=math.sqrt(8/math.pi)*tstar/math.sqrt(math.expm1(4*tstar))
bstar=(1+tstar)/(12*tstar)
check(.3984<tstar<.3985,'tstar-range')
check(.3210<cstar<.3211,'cstar-range')
check(.2924<bstar<.2926,'bstar-range')
for d in [100,200,500,1000,2000]:
    pstar=p_from_t(tstar)
    h=round(d*pstar-.5)+.5
    p=h/d
    t=-math.log1p(-2*p)/2
    val=t*exact_norm(d,t)/math.sqrt(d)
    appr=cstar*(1+bstar/d)
    check(abs(val-appr) < 5/d**2,('optimized-two-term-test',d,val,appr))
    check(abs((d*p)%1-.5)<2e-12,('half-shell',d))

print('PASS:', checks,'deterministic exact-rational, finite-kernel and asymptotic consistency checks')
print('t_* = %.15f, leading = %.15f, relative_first_correction = %.15f'%(tstar,cstar,bstar))
