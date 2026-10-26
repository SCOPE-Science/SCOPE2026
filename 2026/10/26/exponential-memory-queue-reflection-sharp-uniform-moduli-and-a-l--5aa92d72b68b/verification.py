"""Reproducible finite-step checks for exponentially weighted Skorokhod reflection.

These finite tests do not replace the analytic arguments for arbitrary cadlag paths.
Standard-library Python 3 only. Run: python verification.py
"""
import math
import random


def evaluate(events, beta, t):
    """Exact memory and regulator for right-continuous step input.

    events = sorted (time, raw level), starting with (0, level <=1).
    The recursion accounts for continuous regulator growth between jumps.
    """
    assert events[0][0] == 0 and events[0][1] <= 1
    curr, m, integ = 0.0, 0.0, 0.0
    level = events[0][1]
    for tt, lev in [(tt,lev) for tt,lev in events[1:] if tt<=t] + [(t, None)]:
        d = tt-curr
        assert d>=0
        b = max(0.0, level-1.0)
        if beta == 0:
            integ += m*d
        elif m <= b:
            integ += b*d
            m = b
        elif b == 0:
            integ += m*(-math.expm1(-beta*d))/beta
            m *= math.exp(-beta*d)
        else:
            crossing = min(d, math.log(m/b)/beta)
            integ += m*(-math.expm1(-beta*crossing))/beta + b*(d-crossing)
            m = max(b, m*math.exp(-beta*d))
        curr = tt
        if lev is not None:
            level = lev
            m = max(m, level-1.0)
    eta = m + beta*integ
    return (level-m, m, eta)


def grid_memory(events, beta, t):
    # Independent analytic variational formula, including left limits.
    vals=[]
    for i, (a, level) in enumerate(events):
        if a>t:
            break
        b=min(t, events[i+1][0] if i+1<len(events) else t)
        # The maximum of e^(beta*s)*(level-1)_+ occurs as s approaches b.
        vals.append(max(0., level-1.)*math.exp(-beta*(t-b)))
    return max([0.]+vals)


def input_value(events, t):
    return next(level for tt,level in reversed(events) if tt<=t)


def checks():
    random.seed(20261019)
    count=0
    for _ in range(320):
        beta=random.choice([0.,0.07,0.5,1.4,4.])
        jumps=sorted(random.sample(range(1,160), random.randint(1,9)))
        levels=[random.uniform(-2,1)]+[random.uniform(-2,4) for _ in jumps]
        events=list(zip([0.]+[x/200. for x in jumps],levels))
        for j in range(2,200):
            t=j/200.
            val,m,eta=evaluate(events,beta,t)
            independently=grid_memory(events,beta,t)
            assert abs(m-independently)<3e-12, (events,beta,t,m,independently)
            assert abs(val-(input_value(events,t)-m))<1e-11
            assert val<=1+1e-11
            assert eta>=-1e-11
            count+=1

    # Equal-time vertical perturbations and optimal uniform constants.
    for beta in (0.,0.2,1.,3.):
        ref=[(0.,1.)]
        for delta in (0.3,0.9,1.7):
            alt=[(0.,1.),(.15,1.+delta),(.15001,1.-delta)]
            val,_,_=evaluate(alt,beta,.15001)
            r,_,_=evaluate(ref,beta,.15001)
            assert abs(val-r)<=2*delta+1e-10
            assert abs(val-r)>1.9999*delta
            # Regulator grows at rate beta*delta when input remains 1+delta.
            alt2=[(0.,1.),(.000001,1.+delta)]
            _,_,eta=evaluate(alt2,beta,1.)
            assert abs(eta-delta*(1+beta*(1.-.000001)))<1e-9
            count+=1

    # Non-global J1 bound: endpoints after shifted square pulses.
    a,b,shift=.2,.4,.01
    for beta in (.1,1.,3.):
        for H in (1.,10.,100.):
            rho=[(0.,0.),(a,1+H),(b,0.)]
            shifted=[(0.,0.),(a+shift,1+H),(b+shift,0.)]
            v1,m1,_=evaluate(rho,beta,1.)
            v2,m2,_=evaluate(shifted,beta,1.)
            expect=H*math.exp(-beta*(1-b))*(math.exp(beta*shift)-1)
            assert abs(abs(v1-v2)-expect)<1e-10
            count+=1
    # A pulse ending later changes cumulative losses by beta * H * shift,
    # despite a small J1 time shift that aligns the pulse endpoints.
    for beta in (0.1,0.7,2.5):
        for H in (0.2,4.,80.):
            short=[(0.,0.),(.2,1+H),(.4,0.)]
            long=[(0.,0.),(.2,1+H),(.41,0.)]
            _,_,e_short=evaluate(short,beta,1.)
            _,_,e_long=evaluate(long,beta,1.)
            assert abs((e_long-e_short)-beta*H*.01)<1e-10
            count+=1
    print('PASS',count,'finite step/time comparisons and boundary checks')

if __name__=='__main__':
    checks()
