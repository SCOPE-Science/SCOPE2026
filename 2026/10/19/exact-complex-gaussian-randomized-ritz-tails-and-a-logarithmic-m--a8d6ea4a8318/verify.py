"""Reproduce the exact square-complex-Gaussian randomized Ritz laws.
Run: python verify.py
Requires Python 3, NumPy and mpmath; no external data.
"""
import math
import numpy as np
import mpmath as mp


def law(theta, a, b):
    s, c = math.sin(theta), math.cos(theta)
    beta, gamma = b * s*s, b * s*c
    q = gamma*gamma / ((a-beta)**2 + gamma*gamma)
    if abs(q-1) < 1e-12:
        mt = .5
    elif q < .9:
        mt = q*(q-1-math.log(q)) / (1-q)**2
    else:
        mt = float(mp.mpf(str(q))*(mp.mpf(str(q))-1-mp.log(mp.mpf(str(q))))/(1-mp.mpf(str(q)))**2)
    return s*s+c*c*mt, q, beta, gamma


def empirical(n=110000, seed=20261016):
    rng = np.random.default_rng(seed)
    for theta in (0.06, 0.18, 0.47, math.pi / 4):
        a,b = 1.,2.
        s,c=math.sin(theta),math.cos(theta)
        W=np.array([[c,0],[0,1],[s,0]],dtype=complex)
        AW=np.array([[0,0],[0,a],[b*s,0]],dtype=complex)
        Om=(rng.standard_normal((n,3,2))+1j*rng.standard_normal((n,3,2)))/math.sqrt(2)
        OH=Om.conj().transpose(0,2,1)
        M=np.linalg.solve(OH@W,OH@AW)
        assert np.max(np.abs(M[:,0,1]))<1.e-8
        assert np.max(np.abs(M[:,1,1]-a))<1.e-8
        mu=M[:,0,0]
        t=M[:,1,0]/(mu-a)
        T=np.abs(t)**2/(1+np.abs(t)**2)
        S=s*s+c*c*T
        mean,q,beta,gamma=law(theta,a,b)
        assert abs(S.mean()-mean)<0.009, (theta,S.mean(),mean)
        for x in (0.1,0.25,0.5,0.75,0.9):
            pred=x/(q+(1-q)*x)
            assert abs((T<=x).mean()-pred)<0.009, (theta,x,(T<=x).mean(),pred)
        # The unrefined eigenvalue has a shifted complex Cauchy law.
        for x in (0.5, 1, 2, 4):
            observed=(np.abs(mu-beta)>abs(gamma)*x).mean()
            predicted=1/(1+x*x)
            assert abs(observed-predicted)<0.01,(theta,x,observed,predicted)
        print(f"theta={theta:.9f}, q={q:.9f}, expected_S={mean:.9f}, empirical_S={S.mean():.9f}")


def analytic_checks():
    mp.mp.dps=60
    for q in ('0.000001','0.004','0.07','0.34','0.88','0.999'):
        v=mp.mpf(q)
        analytic=v*(v-1-mp.log(v))/(1-v)**2
        integral=mp.quad(lambda r: v/((r+v)*(1+r)**2), [0,1,10,mp.inf])
        assert abs(analytic-integral)<mp.mpf('1.e-48')
    for theta in (1.e-2, 3.e-3, 1.e-3, 3.e-4):
        e,_,_,_=law(theta,1.,2.)
        quotient=e/(8*theta**2*math.log(1/theta))
        print('theta',theta,'asymptotic quotient',quotient)
        assert 0.7 < quotient <1.2
    # Resonance: a=b*sin(theta)**2, q=1, T exactly uniform.
    expected,q,_,_=law(math.pi/4,1.,2.)
    assert abs(q-1)<1.e-12 and abs(expected-.75)<1.e-12
    print('symbolic and asymptotic checks OK')

if __name__ == '__main__':
    analytic_checks()
    empirical()
    print('ALL CHECKS PASSED')
