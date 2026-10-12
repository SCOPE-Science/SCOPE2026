"""Independent finite-dimensional checks of a collective-phase entanglement formula.

Python 3, NumPy >= 1.24. Execute: python verify.py
"""
import math
import numpy as np


def negativity_formula(c, theta):
    x = math.cos(theta) ** c
    y = math.cos(2 * theta) ** c
    a = 1.0 - y
    b = 16.0 * x * x * math.sin(theta) ** 2
    # Numerically stable rationalized form of the negative eigenvalue.
    if b == 0:
        return 0.0
    return (b / (8.0 * (math.sqrt(a*a+b)+a)))


def quantum_state(c, theta):
    states = np.arange(1 << (c+2))
    s = (1 - 2*((states >> (c+1)) & 1))
    t = (1 - 2*((states >> c) & 1))
    rest = np.zeros_like(states)
    for k in range(c):
        rest += 1 - 2*((states >> k) & 1)
    amp = np.exp(-0.5j * theta * (s*t + (s+t)*rest))/math.sqrt(2**(c+2))
    return amp.reshape((4,2**c))


def pt_spectrum(c,theta):
    state=quantum_state(c,theta)
    rho=state @ state.conj().T
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    return np.linalg.eigvalsh(pt), rho


def golden_peak(fun,lo=0.7,hi=1.8):
    g=(math.sqrt(5)-1)/2
    x=hi-g*(hi-lo)
    y=lo+g*(hi-lo)
    for _ in range(120):
        if fun(x)<fun(y): lo=x;x=y;y=lo+g*(hi-lo)
        else: hi=y;y=x;x=hi-g*(hi-lo)
    z=(lo+hi)/2
    return z,fun(z)


def run():
    checks=0
    for c in range(1,8):
        for theta in (0.0,0.01,0.19,0.39,math.pi/4,0.93,1.31,math.pi/2,2.2,math.pi):
            e,rho=pt_spectrum(c,theta)
            neg=max(0.0,-float(e[0]))
            theoretical=negativity_formula(c,theta)
            assert abs(neg-theoretical)<3e-12, (c,theta,neg,theoretical)
            assert abs(np.trace(rho)-1)<2e-12
            assert np.linalg.eigvalsh(rho)[0]>=-2e-12
            x=math.cos(theta)**c
            y=math.cos(2*theta)**c
            analytic=sorted([(1-y-math.hypot(1-y,4*x*math.sin(theta)))/8,
                (1-y+math.hypot(1-y,4*x*math.sin(theta)))/8,
                (3+y-math.hypot(1-y,4*x*math.cos(theta)))/8,
                (3+y+math.hypot(1-y,4*x*math.cos(theta)))/8])
            assert np.allclose(e,analytic,atol=3e-12), (c,theta,e,analytic)
            checks+=4
    for c in range(1,41):
        for th in [i*math.pi/200 for i in range(1,100)]:
            p=math.sin(th)**2
            q=math.cos(th)**2
            lhs=(1-math.cos(2*th)**c)/2
            rhs=sum(math.comb(c,j)*p**j*q**(c-j) for j in range(1,c+1,2))
            assert abs(lhs-rhs)<1e-12
            assert negativity_formula(c,th)<=1/(2*c)+1e-12
            checks+=2
    # Exact c=1 optimum, achieved at sin(theta)^2=1/3.
    th=math.asin(1/math.sqrt(3))
    assert abs(negativity_formula(1,th)-1/6)<1e-14
    checks+=1
    target_z=3**(1/6)
    target_const=3**(2/3)/4
    for c in [100,300,1000,3000,10000]:
        def f(z):return negativity_formula(c,z*c**(-2/3))
        z,opt=golden_peak(f)
        assert abs(z-target_z)<0.1, (c,z)
        assert abs(c**(5/3)*(1/(2*c)-opt)-target_const)<0.2
        print(f'c={c}: z={z:.9f}, c*N={c*opt:.9f}, correction={c**(5/3)*(1/(2*c)-opt):.9f}')
        checks+=2
    print('VERIFY_OK',checks,'checks')

if __name__=='__main__':run()
