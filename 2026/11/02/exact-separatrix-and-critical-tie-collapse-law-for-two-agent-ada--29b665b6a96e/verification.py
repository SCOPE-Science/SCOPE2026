"""Exact phase boundary and critical exponents for two-agent adaptive ties.
Only mathematical reproducibility code; no external dependencies other than scipy, numpy.
"""
import math
from scipy.integrate import solve_ivp
from scipy.special import expi
from scipy.optimize import brentq

def H(alpha,d): return math.log(d)-0.5*expi(alpha*d)
def classify(alpha,d,w):
    dc=math.log(2)/alpha
    if d<=dc:return 'consensus',0.0
    C=math.atanh(w)+H(alpha,d)
    G=H(alpha,dc)
    if abs(C-G)<1e-12:return 'critical',dc
    if C>G:return 'consensus',0.0
    return 'polarized',brentq(lambda x: H(alpha,x)-C,dc,d)

def evolve(alpha,d,w,T):
    def rhs(t,y):
        d,w=y
        v=math.exp(-alpha*d)
        return [-2*w/(1+w)*v*d, w*(1-w)*(2*v-1)]
    s=solve_ivp(rhs,[0,T],[d,w],rtol=1e-11,atol=1e-13,method='DOP853',dense_output=True,max_step=2.0)
    assert s.success
    return s

N=0
for a in [0.5,1.0,2.0,3.0,5.0]:
    for d0 in [0.2,0.7,1.5,2.0]:
        for w0 in [0.01,0.1,0.3,0.8]:
            phase,dstar=classify(a,d0,w0)
            sol=evolve(a,d0,w0,1000)
            d,w=sol.y[:,-1]
            if phase=='polarized':
                assert abs(d-dstar)<2e-5,(a,d0,w0,phase,dstar,d,w)
                assert w<2e-5,(a,d0,w0,w)
            else:
                assert d<2e-5,(a,d0,w0,phase,d)
                assert w>0.9999,(a,d0,w0,phase,w)
            hstart=math.atanh(w0)+H(a,d0)
            for t in [0,0.2,1,3]:
                ds,ws=sol.sol(t)
                assert 0<ws<1 and ds>0 and abs((math.atanh(ws)+H(a,ds))-hstart)<2e-8,(a,d0,w0,t)
            N+=1
print('phase and invariant checks',N)
for a,d0 in [(1,2),(2,1.5)]:
    dc=math.log(2)/a
    wc=math.tanh(H(a,dc)-H(a,d0))
    sol=evolve(a,d0,wc,6000)
    for t in [1000,3000,6000]:
        d,w=sol.sol(t)
        assert abs(t*(d-dc)-2/a)<0.05,(a,t,d,2/a)
        assert abs(t*t*w-2/math.log(2))<0.15,(a,t,w)
    print('critical',a, 'threshold',wc,'scaled gap',6000*(sol.y[0,-1]-dc),'scaled weight',6000**2*sol.y[1,-1])
print('ALL CHECKS PASSED')

def rational_rhs(t,y):
    d,w=y
    phi=1/(1+d)
    return [-2*w/(1+w)*phi*d, w*(1-w)*(2*phi-1)]
def rational_H(d):return .5*(math.log(d)-d)
d0=2.;crit=math.tanh(rational_H(1.)-rational_H(d0))
for w0 in [.05,crit,.5]:
    sol=solve_ivp(rational_rhs,[0,6000],[d0,w0],rtol=2e-11,atol=1e-13,method='DOP853',dense_output=True,max_step=2.)
    assert sol.success
    invariant=math.atanh(w0)+rational_H(d0)
    for t in [0.,1.,4.,10.]:
        d,w=sol.sol(t)
        assert abs(math.atanh(w)+rational_H(d)-invariant)<1e-8
    d,w=sol.y[:,-1]
    if w0<crit:assert d>1 and w<1e-4
    elif w0>crit:assert d<1e-4 and w>.9999
    else:
        assert abs(6000*(d-1)-4)<.05
        assert abs(6000**2*w-4)<.1
print('rational kernel, three regimes PASS')
