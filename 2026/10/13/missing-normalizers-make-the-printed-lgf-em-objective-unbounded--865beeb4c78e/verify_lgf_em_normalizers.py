import math
import numpy as np
from scipy.special import gammaln, digamma, logsumexp
from scipy.optimize import minimize_scalar

y=np.array([0.18,0.42,0.95,1.70,3.20],dtype=float)
theta0=1.1
lambda0=2.3
eta0=0.45
K=5000

# E-step moments under the source's posterior formulas.
def moments_one(obs):
    n=np.arange(1,K+1,dtype=float)
    lw=n*math.log(eta0)-(lambda0+1.0)*np.log(lambda0+n*theta0*obs)
    lw-=logsumexp(lw)
    w=np.exp(lw)
    ez=(lambda0+1.0)/(lambda0+n*theta0*obs)
    elogz=digamma(lambda0+1.0)-np.log(lambda0+n*theta0*obs)
    return (
        float(np.sum(w*n)),
        float(np.sum(w*ez)),
        float(np.sum(w*elogz)),
        float(np.sum(w*n*ez)),
        float(w[-1])
    )

mom=[moments_one(v) for v in y]
assert max(abs(v[4]) for v in mom) < 1e-100
m=len(y)
A=sum(v[0] for v in mom)
C=sum(v[1] for v in mom)
B=sum(v[2] for v in mom)
D=sum(obs*v[3] for obs,v in zip(y,mom))

def q_correct(theta,lam,eta):
    L=-math.log1p(-eta)
    return (A*math.log(eta)-m*math.log(L)+m*math.log(theta)
            +m*(lam*math.log(lam)-gammaln(lam))+lam*(B-C)-theta*D)

def q_print_45(theta,lam,eta):
    return (A*math.log(eta)+m*math.log(theta)
            +m*(lam+1.0)*math.log(lam)+lam*(B-C)-theta*D)

def q_print_44(theta,lam,eta):
    return (A*math.log(eta)+m*math.log(theta)
            +m*lam*math.log(lam)+lam*(B-C)-theta*D)

# Correct eta score, including the log-series normalizer omitted from Eq. (4.5).
eta=0.40
eta_score=A/eta-m/((1.0-eta)*(-math.log1p(-eta)))
h=1e-6
eta_fd=(q_correct(theta0,lambda0,eta+h)-q_correct(theta0,lambda0,eta-h))/(2*h)
assert abs(eta_score-eta_fd)<2e-8

# Correct lambda score, including the gamma normalizer.
lam=lambda0
lambda_score=m*(math.log(lam)+1.0-digamma(lam))+(B-C)
hl=1e-6
lambda_fd=(q_correct(theta0,lam+hl,eta0)-q_correct(theta0,lam-hl,eta0))/(2*hl)
assert abs(lambda_score-lambda_fd)<2e-8

# Correct Q has a finite maximum for this frozen E-step.
r=minimize_scalar(lambda z:-q_correct(theta0,z,eta0),bounds=(0.05,100.0),method='bounded',options={'xatol':1e-12})
lam_star=float(r.x)
assert abs(lam_star-2.49636096)<3e-6

# Printed Q increases without bound; finite boxes make the optimizer chase the cap.
box_results=[]
for upper in (5.0,10.0,30.0,100.0):
    rp=minimize_scalar(lambda z:-q_print_45(theta0,z,eta0),bounds=(0.05,upper),method='bounded',options={'xatol':1e-11})
    box_results.append((upper,float(rp.x)))
    assert upper-rp.x < 2e-5

# Both published complete-data variants have positive lambda-log-lambda divergence.
for large in (30.0,100.0,300.0):
    assert q_print_44(theta0,large,eta0) > q_print_44(theta0,large/3.0,eta0)
    assert q_print_45(theta0,large,eta0) > q_print_45(theta0,large/3.0,eta0)

# Coercivity diagnostic for the corrected Q.
assert q_correct(theta0,1e-6,eta0) < q_correct(theta0,lam_star,eta0)-20
assert q_correct(theta0,1000.0,eta0) < q_correct(theta0,lam_star,eta0)-100

print('VERIFY_OK')
print('A_EN',format(A,'.12f'))
print('B_ElogZ',format(B,'.12f'))
print('C_EZ',format(C,'.12f'))
print('eta_score',format(eta_score,'.12f'))
print('lambda_score_at_current',format(lambda_score,'.12f'))
print('lambda_correct_max',format(lam_star,'.12f'))
for upper,x in box_results:
    print('printed_box',format(upper,'.0f'),format(x,'.12f'))
