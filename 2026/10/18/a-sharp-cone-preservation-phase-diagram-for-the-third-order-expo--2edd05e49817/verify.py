"""Reproduce finite algebraic and numerical checks for an exponential Rosenbrock Riccati positivity classification.
No third-party dependencies. Exact rational checks and floating-point sampling are
supporting diagnostics; mathematical quantifiers are established by the proof.
"""
from fractions import Fraction as F
import math
import random

passed=0

def check(ok,description='check'):
    global passed
    if not ok:
        raise AssertionError(description)
    passed+=1

def phi(k,z):
    # Dedicated stable functions for z<=0; direct expression for large |z|.
    if abs(z)<0.25:
        term=1.0/math.factorial(k); value=term
        for j in range(1,100):
            term *= z/(k+j); value+=term
            if abs(term)<1e-17: break
        return value
    if k==1: return -math.expm1(z)/(-z)
    if k==3:
        t=-z
        return (1-t+0.5*t*t-math.exp(-t))/(t*t*t)
    raise ValueError(k)

def kappa(a,h):
    z=-2*a*h
    return 2*h*h*phi(1,z)*phi(3,z)

def critical(a,mu):
    if a>0 and mu<=4*a*a: return math.inf
    lo,hi=0.0,1.0
    while mu*kappa(a,hi)<1: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if mu*kappa(a,mid)<1:lo=mid
        else:hi=mid
    return (hi+lo)/2

def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def eigsym2(a):
    tr=a[0][0]+a[1][1];disc=(a[0][0]-a[1][1])**2+4*a[0][1]**2
    return (tr-math.sqrt(disc))/2,(tr+math.sqrt(disc))/2

def test_scalar(y,t):
    z=-2*t*y
    delta=t*phi(1,z)*(1-y*y)
    return y+delta-2*t*phi(3,z)*delta*delta

# Exact rational end-step algebra at a=0, Q,G noncommuting.
qs=[[[F(2),F(1)],[F(1),F(3)]],[[F(4),F(1)],[F(1),F(1)]]]
gs=[[[F(3),F(1)],[F(1),F(2)]],[[F(5),F(-1)],[F(-1),F(2)]]]
for Q in qs:
    for G in gs:
        QGQ=mm(mm(Q,G),Q)
        for h in [F(1,8),F(1,3),F(1),F(2),F(3,2),F(7,4)]:
            # From original exprb32 at X0=0: X2=hQ, D2=-h^2 QGQ, X+=X2+(h/3)D2.
            direct=[[h*Q[i][j]-h**3*QGQ[i][j]/3 for j in range(2)] for i in range(2)]
            spectral=[[h*(Q[i][j]-h*h*QGQ[i][j]/3) for j in range(2)] for i in range(2)]
            check(direct==spectral,'exact rational matrix identity')
            check(direct[0][1]==direct[1][0],'exact symmetry')
        check(mm(Q,G)!=mm(G,Q),'noncommuting example')

# Scalar exact-rational zero-state identity; threshold sqrt(3).
for q in (F(1,2),F(1),F(3),F(7,2)):
    for g in (F(1,3),F(1),F(2),F(4)):
        for h in (F(1,8),F(1),F(2),F(4)):
            Y=h*q
            X=Y-h**3*q*q*g/3
            check((X>=0)==(h*h*q*g<=3),'zero-state if-and-only-if')
            check(X==h*q*(1-h*h*q*g/3),'rational factorization')

# Floating-point full-cone scalar condition.  Check y=0 and arbitrary y>=0.
for t in [0.0001,0.1,0.5,1.0,1.5,1.7320508075688772]:
    for j in range(801):
        y=(j/800)*8
        check(test_scalar(y,t)>-5e-13,'scalar all-state positivity on grid')
for t in [1.8,2.2,5.0,10.0]:
    check(test_scalar(0,t)<0,'sharp scalar zero witness')
    for y in [1,1.01,1.5,2,5,10,100]:
        check(test_scalar(y,t)>0,'large-state positivity beyond threshold')

# Spectral equivalence for 2x2 positive definite Q,G, including noncommuting.
rng=random.Random(260326429)
for trial in range(200):
    # Q=L L^T and G=K K^T with positive diagonal factors.
    L=[[rng.uniform(0.4,2),0],[rng.uniform(-0.5,0.5),rng.uniform(0.4,2)]]
    K=[[rng.uniform(0.4,2),0],[rng.uniform(-0.5,0.5),rng.uniform(0.4,2)]]
    def gram(U):return [[sum(U[i][k]*U[j][k] for k in range(2)) for j in range(2)] for i in range(2)]
    Q=gram(L);G=gram(K);QG=mm(Q,G);QGQ=mm(QG,Q)
    tr=QG[0][0]+QG[1][1]
    det=QG[0][0]*QG[1][1]-QG[0][1]*QG[1][0]
    eigs=((tr-math.sqrt(max(0,tr*tr-4*det)))/2,(tr+math.sqrt(max(0,tr*tr-4*det)))/2)
    a=rng.choice([0,0.2,1.0,2.0]);h=rng.uniform(0.05,5)
    c=h*phi(1,-2*a*h);k=kappa(a,h)
    P=[[c*Q[i][j]-2*h*phi(3,-2*a*h)*c*c*QGQ[i][j] for j in range(2)] for i in range(2)]
    pmin,pmax=eigsym2(P)
    is_psd=(pmin>=-1e-9)
    predicted=(k*eigs[1]<=1+1e-10)
    check(is_psd==predicted,'spectral matrix PSD equivalence')
    check(abs(P[0][1]-P[1][0])<1e-10,'numerical matrix symmetry')
    # Congruence preserves determinant ratio.
    detP=P[0][0]*P[1][1]-P[0][1]*P[1][0]
    detQ=Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]
    predicted_det=c*c*detQ*(1-k*eigs[0])*(1-k*eigs[1])
    check(abs(detP-predicted_det)<=1e-8*(1+abs(detP)+abs(predicted_det)),'determinant formula')

# Monotonicity and threshold asymptotics: analytic proof independent of sampling.
for a in (0,0.01,0.2,0.7,1.5,3):
    hist=[kappa(a,10**(-3+j/20)) for j in range(101)]
    check(all(v>u for u,v in zip(hist,hist[1:])),'strictly increasing kappa sampled')
    for mu in (0,0.25,1,9,36):
        crit=critical(a,mu) if mu>0 else math.inf
        if a and mu<=4*a*a:check(math.isinf(crit),'unconditional damping')
        elif mu>0:
            check(math.isfinite(crit),'finite critical step')
            check(mu*kappa(a,crit*0.999)<1,'before barrier')
            check(mu*kappa(a,crit*1.001)>1,'after barrier')
for a in (1.4,1.48,1.495,1.499):
    mu=9
    hstar=critical(a,mu)
    estimate=1/(a*(1-4*a*a/mu))
    check(abs(hstar/estimate-1)<0.14,'near-boundary critical time asymptotic')
for a in (0,1e-4,1e-3,1e-2):
    hstar=critical(a,9)
    check(abs(hstar-math.sqrt(1/3))<0.015,'small damping critical limit')
print('PASS:',passed,'checks')
