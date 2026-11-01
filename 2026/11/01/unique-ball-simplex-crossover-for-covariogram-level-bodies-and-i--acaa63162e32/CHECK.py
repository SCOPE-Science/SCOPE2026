"""Independent numerical checks of spherical-lens/simplex comparison.
Scientific statements and their analytic proofs are in RESULT.md.
Requires scipy (and Python 3.10 or newer).
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import betainc, gammaln

def log_c(d):
    return (math.lgamma(2*d+1) - 2*math.lgamma(d+1))/d - math.log(2)

def c(d):
    return math.exp(log_c(d))

def lens(d,r):
    return float(betainc((d+1)/2, 0.5, 1-r*r))

def lens_quad(d,r):
    k_ratio=math.exp(math.lgamma(d/2+1)-math.lgamma((d+1)/2)-.5*math.log(math.pi))
    return 2*k_ratio*quad(lambda t:(1-t*t)**((d-1)/2),r,1,epsabs=5e-14)[0]

def root(d):
    cd=c(d)
    left=max(0.25, 1-1/cd+0.035)
    def f(s):
        r=cd*(1-s)
        return math.log(lens(d,r))-d*math.log(s)
    assert f(left)<0 and f(.85)>0
    return brentq(f,left,.85,xtol=1e-14)

count=0
for d in range(2,21):
    cd=c(d)
    assert 1<cd<2
    for j in range(1,16):
        r=j/16
        assert abs(lens(d,r)-lens_quad(d,r)) < 3e-11
        count+=1
        if d==2:
            explicit=(2/math.pi)*(math.acos(r)-r*math.sqrt(1-r*r))
            assert abs(lens(d,r)-explicit)<1e-13
            count+=1
    sd=root(d)
    sig=(cd*cd-1)/(cd*cd+1)
    assert sd>sig
    assert abs(lens(d,cd*(1-sd))-sd**d)<1e-12
    for p in (.15,.4,.7):
        sl=sig+(sd-sig)*p
        assert lens(d,cd*(1-sl))<sl**d
        sh=sd+(.95-sd)*p
        assert lens(d,cd*(1-sh))>sh**d
        count+=2
    count+=3
    # n-dimensional lens: beta derivative has the exact known sign.
    for j in range(1,15):
        r=j/15
        h=1e-5
        numeric=(lens(d,r+h)-lens(d,r-h))/(2*h)
        target=-2*math.exp(math.lgamma(d/2+1)-math.lgamma((d+1)/2)-.5*math.log(math.pi))*(1-r*r)**((d-1)/2)
        assert abs(numeric-target)<3e-8
        count+=1

for d in (20,40,80,100,200,500):
    sd=root(d)
    pred=.6-(7*math.log(math.pi*d)+18*math.log(3)-27*math.log(2))/(50*d)
    assert abs(sd-pred) < .09*math.log(d)**2/d**2
    constant=2**(.9)/(math.pi**(7/30)*3**(.6))
    scaled=(sd/.6)**d*d**(7/30)
    assert abs(scaled-constant)<.5*math.log(d)**2/d
    count+=2

for d in (2,3,4,10,50,100,200,500):
    sd=root(d)
    print('dimension',d,'simplex c',round(c(d),12), 'crude',round((c(d)**2-1)/(c(d)**2+1),12),'exact-crossing',round(sd,12))
print('PASS',count,'independent integration, derivative, transition and asymptotic comparisons')
