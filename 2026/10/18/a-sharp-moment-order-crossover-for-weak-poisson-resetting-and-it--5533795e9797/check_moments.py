"""Standalone finite checks for the Poisson-versus-Gaussian moment crossover.

Only finite algebra and numerical illustrations are checked; asymptotic statements
require the accompanying analytical argument.
"""
from fractions import Fraction
import math

checks = 0

def verify(predicate, label):
    global checks
    if not predicate:
        raise AssertionError(label)
    checks += 1


def denominators(j, lam, gam, s):
    n = 2*j
    jump = (lam/s)*(1-(1-s)**n)-n*gam
    gauss = n*(lam-gam)-lam*s*j*(2*j-1)
    return jump, gauss


def log_ratio_float(m, lam, gam, s):
    log_q=math.log1p(-s)
    acc=0.0
    for j in range(1,m+1):
        n=2*j
        jump=(-lam/s)*math.expm1(n*log_q)-n*gam
        gauss=n*(lam-gam)-lam*s*j*(2*j-1)
        verify(jump>0 and gauss>0, 'positive denominators')
        acc+=math.log(gauss/jump)
    return acc


def phi_jump(p,beta,s):
    return beta*p+math.expm1(p*math.log1p(-s))/s


def root_jump(beta,s):
    lo=1.0e-8
    verify(phi_jump(lo,beta,s)<0,'negative log growth')
    hi=1.0/s
    while phi_jump(hi,beta,s)<0:hi*=2
    for _ in range(110):
        mid=(lo+hi)/2
        if phi_jump(mid,beta,s)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2

# The two equations have exactly the same stationary variance. The next
# polynomial coefficient is strictly positive on the jump side.
for s in (Fraction(1,20),Fraction(1,10),Fraction(1,4)):
    for j in range(1,9):
        a,b=denominators(j,Fraction(1),Fraction(1,2),s)
        verify(a-b==0 if j==1 else a-b>0,'exact Taylor remainder')
    if s == Fraction(1,20):
        mj=Fraction(1);mg=Fraction(1)
        for j in range(1,9):
            a,b=denominators(j,Fraction(1),Fraction(1,2),s)
            verify(a>0 and b>0,'finite moments')
            common=2*j*(2*j-1)*Fraction(1,3)
            mj*=common/a;mg*=common/b
            verify(mj/mg<=1,'moments ordered')
            verify((mj/mg==1) == (j==1),'strict higher moments')

# At fixed beta, the Poisson cutoff exceeds the Gaussian cutoff for small s.
for beta in (0.2,0.5,0.8):
    for s in (1e-2,1e-3,1e-4):
        c=root_jump(beta,s)
        g=1+2*(1-beta)/s
        verify(c>g, 'higher Poisson moment cutoff')
        verify(abs(phi_jump(c,beta,s))<1e-7, 'root residual')
        verify(c>0 and g>0, 'positive critical orders')

# The crossover constant is checked at decreasing reset sizes. Error scales
# as an approximate positive fractional power; no finite test proves a limit.
for beta in (0.25,0.5,0.75):
    mu=1-beta
    for c in (0.6,1.0,1.3):
        values=[]
        for s in (1e-3,1e-4,1e-5,1e-6):
            m=max(1,round(c*s**(-2/3)))
            if m*s >= mu/2:
                continue
            v=log_ratio_float(m,1.0,beta,s)
            values.append((s,v))
            verify(v<=0,'moment ratio at most one')
        verify(len(values)>=2,'comparison sequence')
        target=-2*c**3/(9*mu)
        verify(abs(values[-1][1]-target)<0.07,'asymptotic constant numeric')

# Reproduce the exact finite-ratio value at rational parameters.
a,b=denominators(2,Fraction(1),Fraction(1,2),Fraction(1,4))
verify(a==Fraction(47,64),'rational Poisson denominator')
verify(b==Fraction(1,2),'rational Gaussian denominator')
verify(b/a==Fraction(32,47),'exact fourth-moment ratio')
print(f'{checks} deterministic finite checks passed')
