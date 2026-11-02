"""Reproducibility checks for endpoint concavity in a symmetric Gaussian location mixture."""
import math
import numpy as np
from scipy.special import roots_hermitenorm, logsumexp

Z, W = roots_hermitenorm(140)
W = W / np.sqrt(2.0 * np.pi)
assert abs(float(np.sum(W))-1.0)<1e-13

def calc(alpha):
    assert 0 < alpha <= .5
    S=2-alpha
    sig=math.sqrt(S/2)
    mu=math.sqrt(alpha/2)
    c=mu/(sig*sig)
    v=alpha/S
    # E_U integrates a two-point shift of standard Gaussian.
    U=np.r_[sig*Z+mu, sig*Z-mu]
    wt=np.r_[W/2,W/2]
    T=c*U
    sech2=np.exp(-2*np.logaddexp(T,-T)+2*np.log(2.0))
    rho= -2*U/S+c*np.tanh(T)
    drho=-2/S+c*c*sech2
    B_one=float(wt@(drho**2)-(wt@(rho**4))/3)
    B_two=float(wt@(c**4*(4*sech2-6*sech2**2)))
    A=float(wt@((1+drho)**2))
    fourth=-alpha*alpha/2
    endpoint=-A/2-fourth*B_two/12
    assert abs(B_one-B_two)<2e-11,(alpha,B_one,B_two)
    assert A>0 and B_one<0 and fourth<0 and endpoint<0
    # The strict expectation bound is responsible for the sign.
    normal=math.sqrt(v)*Z
    sh=1/np.cosh(normal)
    ratio=float((W@(sh**3))/(W@sh))
    assert ratio>1-v>=2/3
    return endpoint,A,B_two

def entropy(alpha,t):
    S=2-alpha
    sig=math.sqrt(S/2)
    mu=math.sqrt(alpha/2)
    means=mu*np.array([aa*math.sqrt(1-t)+bb*math.sqrt(t) for aa in (-1,1) for bb in (-1,1)])
    centers=means[:,None]+sig*Z[None,:]
    logterms=-0.5*((centers[:,:,None]-means[None,None,:])/sig)**2
    logdens=logsumexp(logterms,axis=-1)-math.log(4*sig*math.sqrt(2*math.pi))
    return -float(W@logdens.mean(axis=0))

def run():
    count=0
    for alpha in [0.001,.005,.01,.02,.05,.1,.2,.3,.4,.5]:
        cur,A,B=calc(alpha)
        count+=5
        if alpha>=.1:
            step=.005
            v0=entropy(alpha,0)
            v1=entropy(alpha,step)
            v2=entropy(alpha,2*step)
            v3=entropy(alpha,3*step)
            # Cubic-interpolation second derivative at left endpoint,
            # error O(step**2), independently from score-identity formula.
            est=(2*v0-5*v1+4*v2-v3)/(step*step)
            assert abs(est-cur)<1.2e-5,(alpha,est,cur)
            count+=1
    ratios=[calc(alpha)[0]/alpha**4 for alpha in [.04,.02,.01,.005]]
    assert abs(ratios[-1]+1/12)<1e-3,ratios
    assert abs(ratios[-1]+1/12)<abs(ratios[0]+1/12)
    count+=2
    print(f'PASS: {count} independent quadrature, identity, sign and asymptotic checks')
    print('Alpha 0.5: endpoint curvature = %.12g, A = %.12g, B = %.12g'%calc(.5))
    print('Alpha 0.005: curvature/alpha^4 = %.12g (limit -1/12)'%ratios[-1])

if __name__=='__main__':
    run()
