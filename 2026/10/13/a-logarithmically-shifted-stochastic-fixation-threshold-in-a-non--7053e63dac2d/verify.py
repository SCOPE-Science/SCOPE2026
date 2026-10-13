"""Reproduce exact polynomial identities and numerical large-population fixation asymptotics.
Uses Python standard library only. This checks finite cases; the full theorem is proved analytically.
"""
from fractions import Fraction as Q
import math

CASES = [
    (Q(125,54), Q(1,10), Q(2,5), -1),
    (Q(1920,829), Q(1,8), Q(3,8), 0),
    (Q(1500,647), Q(1,5), Q(3,10), 1),
]

def logsumexp(values):
    x = max(values)
    return x + math.log(math.fsum(math.exp(t-x) for t in values))

def log_c(r,a,b,w):
    f0=float(r*a*b/30)
    d=float(r*(b-a)/30)
    return .5*math.log(w*d/(2*math.pi))-math.log(2*math.sinh(w*f0/2))

def finite_log_fixes(r,a,b,N,w):
    # Closed form sum of quadratic payoff at lattice sites 1,...,k.
    rr=float(r)/30
    aa=float(a);bb=float(b)
    weights=[]
    for k in range(N):
        s=rr*(k*(k+1)*(2*k+1)/(6*N*N)
              -(aa+bb)*k*(k+1)/(2*N) + aa*bb*k)
        weights.append(-w*s)
    i=int(N*aa)
    assert 0<i<N
    den=logsumexp(weights)
    return logsumexp(weights[:i])-den, logsumexp(weights[i:])-den

def run():
    for r,a,b,regime in CASES:
        # Coefficients of F: (r/30)*x^2-(r/60)*x+(13*r/30-1).
        A=r/30
        assert a+b==Q(1,2)
        assert A*a*b==Q(13,30)*r-1
        assert A*(a+b)==r/60
        assert Q(0)<a<b<Q(1)
        D=A*b*b*(3*a-b)/6
        assert (D>0)-(D<0)==regime
        expected_D = {Q(125,54): Q(-1,4860), Q(1920,829): Q(0), Q(1500,647): Q(9,25880)}
        assert D == expected_D[r]
        w=100.0
        C=log_c(r,a,b,w)
        for N in (1000,3000,6000):
            logh, logq=finite_log_fixes(r,a,b,N,w)
            target=C-.5*math.log(N)+N*w*float(D)
            if regime == 1:
                prediction=-C+.5*math.log(N)-N*w*float(D)
                assert abs(logq-prediction)<0.3, (r,N,logq,prediction)
            else:
                assert abs(logh-target)<0.3,(r,N,logh,target)
        print('ok r=',r,'D=',D,'class=',regime)
    # Moving-parameter logarithmic crossover, here tested at z=0.
    rc = float(Q(1920,829))
    derivative = float(Q(829,5120))
    logC = log_c(Q(1920,829), Q(1,8), Q(3,8), 100.0)
    expected = 1.0/(1.0+math.exp(-logC))
    for N in (3000, 10000, 30000):
        r = rc + (0.5*math.log(N))/(N*100.0*derivative)
        t = math.sqrt(30.0/r-207.0/16.0)
        a,b = .25-t,.25+t
        logh,_ = finite_log_fixes(r,a,b,N,100.0)
        assert abs(math.exp(logh)-expected)<0.015, (N,math.exp(logh),expected)
    print('VERIFY_OK: rational identities, all three asymptotic regimes, and logarithmic crossover')

if __name__ == '__main__':
    run()
