"""Independent reproducibility checks for asymmetric-local-reset current optimization.
Run: python3 verify.py (standard library only). Numerical tests support, not replace, the proof.
"""
from math import exp, tanh, sinh, isclose, sqrt

def coth(x):
    return 1.0 / tanh(x)

def log_derivative(y, delta, eta):
    return 2.0 / (y*(1.0 + eta*y*y)) + delta*coth(delta*y) - coth(y)

def optimum(delta, eta):
    a, b = 1e-7, 1.0
    assert 0.0 < delta < 1.0 and eta >= 0.0
    while log_derivative(b, delta, eta) > 0.0:
        b *= 2.0
        assert b < 1e9
    for _ in range(100):
        m = (a+b)/2
        if log_derivative(m, delta, eta) > 0.0: a=m
        else: b=m
    return (a+b)/2

def drift(y, delta, eta, diffusion=1.0, period=1.0):
    return (2*diffusion/period)*y*y/(1+eta*y*y)*sinh(delta*y)/sinh(y)

def jump_mean_tails(y, delta, terms=800):
    # L=1, position basin (-a,1-a); q=2y.
    a=(1+delta)/2
    q=2*y
    return sum((exp(-q*(n-a))-exp(-q*(n-1+a)))/2 for n in range(1,terms+1))

def check():
    tests=0
    for delta in (0.15,0.32,0.5,0.73,0.92):
        for eta in (0.0, 0.25, 1.0, 25.0):
            y=optimum(delta,eta)
            assert log_derivative(y*.9,delta,eta)>0
            assert log_derivative(y*1.1,delta,eta)<0
            assert drift(y,delta,eta)>drift(.92*y,delta,eta)
            assert drift(y,delta,eta)>drift(1.08*y,delta,eta)
            tests+=4
        assert optimum(delta,0)>optimum(delta,1)>optimum(delta,10)
        tests+=1
    for eta in (0.0,0.2,2.0):
        assert optimum(.2,eta)<optimum(.45,eta)<optimum(.7,eta)<optimum(.95,eta)
        tests+=1
    for y in (.18, .5, 1.25, 3.0):
        for delta in (.2, .6, .9):
            lhs=jump_mean_tails(y,delta)
            rhs=.5*sinh(delta*y)/sinh(y)
            assert isclose(lhs,rhs,rel_tol=3e-13,abs_tol=1e-13),(y,delta,lhs,rhs)
            tests+=1
    for delta in (.3,.5,.85):
        for eta in (0.0,.8,5.0):
            y=optimum(delta,eta)
            # Speed is mean jump length divided by mean cycle duration.
            r=4*y*y
            jump=jump_mean_tails(y,delta)
            v=jump/(1/r+eta/4)
            assert isclose(v,drift(y,delta,eta),rel_tol=1e-11)
            tests+=1
    for delta in (.2,.5,.8):
        eta=1e8
        y=optimum(delta,eta)
        asym=(6/(eta*(1-delta*delta)))**.25
        assert abs(y/asym-1)<.005,(delta,y,asym)
        tests+=1
    for eps in (.01,.003):
        y0=optimum(1-eps,0)
        yd=optimum(1-eps,5)
        assert abs(y0/(2/eps)-1)<1e-6
        assert abs(yd/((2/(5*eps))**(1/3))-1)<.08
        tests+=2
    print('PASS: %d reproducibility assertions (independent exponential-tail summation, monotonicity, rate optimality, crossover scales)'%tests)

if __name__=='__main__':check()
