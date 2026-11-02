"""Independent finite-chain and asymptotic checks for weak-decay excursion heights."""
from fractions import Fraction
from math import exp, log, isclose
from scipy.special import spence, logsumexp
from scipy.integrate import quad
from scipy.optimize import brentq

passed = 0

def check(assertion, message):
    global passed
    if not assertion:
        raise AssertionError(message)
    passed += 1

def finite_scale(n, r, p):
    term = Fraction(1)
    S = term
    for j in range(1,n):
        term *= (1 - r**j*p)/(r**j*p)
        S += term
    return p/S

def finite_dirichlet(n, r, p):
    # Independent tridiagonal recurrence solved by exact Gaussian elimination.
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    y = [Fraction(0) for _ in range(n)]
    A[0][0]=Fraction(1)
    y[0]=Fraction(0)
    for k in range(1,n):
        q=r**k*p
        A[k][k]=Fraction(1)
        A[k][k-1]=-(1-q)
        if k+1<n:
            A[k][k+1]=-q
        else:
            y[k]=q
    for j in range(n):
        pivot=A[j][j]
        check(pivot!=0, 'singular')
        for k in range(j+1,n):
            v=A[k][j]/pivot
            for l in range(j,n): A[k][l]-=v*A[j][l]
            y[k]-=v*y[j]
    x=[Fraction(0) for _ in range(n)]
    for j in range(n-1,-1,-1):
        x[j]=(y[j]-sum(A[j][l]*x[l] for l in range(j+1,n)))/A[j][j]
    return p*x[1]

for r in [Fraction(1,3),Fraction(3,4),Fraction(9,10)]:
    for p in [Fraction(1,4),Fraction(1,2),Fraction(4,5)]:
        for n in range(2,11):
            v=finite_scale(n,r,p)
            check(v==finite_dirichlet(n,r,p), f'finite mismatch {n} {r} {p}')
            check(0<v<p,'invalid prob')

def action(p,t):
    return t*t/2-t*log(p)+spence(1-p*exp(-t))-spence(1-p)

tstar=brentq(lambda t:action(1.0,t),1.5,2.0,xtol=5e-15)
check(1.7054<tstar<1.7055,'tstar range')

def root_p(t):
    return brentq(lambda p:action(p,t),0.50000000001,0.999999999999,xtol=4e-15)

def q_eps(p,eps,t):
    n=max(2,int(t/eps))
    if p==0: return 0
    acc=0.0
    logs=[0.0]
    for j in range(1,n):
        q=p*exp(-eps*j)
        acc+=log1pm(q)-log(q)
        logs.append(acc)
    return p*exp(-logsumexp(logs))

def log1pm(q):
    from math import log1p
    return log1p(-q)

for t in [0.5,1.0,1.5]:
    pc=root_p(t)
    target=pc*(1-pc)
    check(0.5<pc<1,'pc range')
    check(abs(action(pc,t))<1e-9,'action root')
    # Conditional fixed-p phase limits, one point on each side.
    pbelow=(pc+0.5)/2
    pabove=(pc+1)/2
    for eps in [0.025,0.0125,0.00625]:
        f=q_eps(pabove,eps,t)
        g=q_eps(pbelow,eps,t)
        check(0<=f<=1 and 0<=g<=1,'probabilities')
    # Asymptotic tests for eps sequence against integral (small eps may be slow near threshold).
    vals=[]
    for eps in [0.04,0.02,0.01]:
        integral=quad(lambda p:q_eps(p,eps,t),0,1,epsabs=5e-9,limit=250,points=[0.5,pc])[0]
        vals.append(integral)
        check(0<integral<1,'integral range')
    check(abs(vals[2]-target)<abs(vals[0]-target),'integral not converging')
    check(abs(vals[2]-target)<0.035,'integral poor agreement')
    print(f't={t:.2f}, p_t={pc:.9f}, predicted tail={target:.9f}, finite eps=.04,.02,.01: '+', '.join(f'{v:.9f}' for v in vals))

for t in [1.60,1.65,1.68,1.69,1.70]:
    p=root_p(t)
    tail=p*(1-p)
    edge=log(exp(tstar)-1)*(tstar-t)/log(1/(tstar-t))
    check(tail>0 and edge>0,'edge sign')
    print(f'edge t={t:.3f} tail={tail:.9f} leading={edge:.9f} ratio={tail/edge:.6f}')
print(f'tstar={tstar:.14f}; {passed} checks passed')
