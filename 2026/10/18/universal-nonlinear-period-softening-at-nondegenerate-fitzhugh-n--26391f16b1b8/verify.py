"""Symbolic Hopf-branch identities and numerical period checks for the classical planar FHN flow."""

from math import pi, sqrt
import sympy as S
from scipy.integrate import solve_ivp
from scipy.optimize import root


def exact_checks():
    c, w, s, m, nu, t = S.symbols('c w s m nu t', real=True, nonzero=True)
    x = S.cos(t)
    second = -c*s/(2*w**2) + c*s*S.cos(2*t)/(6*w**2) - s*S.sin(2*t)/(3*w)
    # Direct second-order balance in physical-time normalization:
    second_lhs = w**2*(S.diff(second,t,2) + second)
    second_rhs = -2*s*w*x*S.diff(x,t)-c*s*x*x
    assert S.simplify(S.trigsimp(second_lhs-second_rhs)) == 0
    forcing = (m*w*S.diff(x,t)+c*m*x-2*s*w*(x*S.diff(second,t)+second*S.diff(x,t))
               -2*c*s*x*second-w*x*x*S.diff(x,t)-c*x*x*x/3)
    cosine = S.factor(S.integrate(S.expand_trig(forcing*S.cos(t)), (t,0,2*S.pi))/S.pi)
    sine = S.factor(S.integrate(S.expand_trig(forcing*S.sin(t)), (t,0,2*S.pi))/S.pi)
    m_exact=(w**2-2*c*s**2)/(4*w**2)
    nu_exact=-s**2*(c**2+w**2)/(6*w**3)
    assert S.simplify(sine.subs(m,m_exact)) == 0
    assert S.simplify((cosine+2*w*nu).subs({m:m_exact,nu:nu_exact})) == 0
    assert S.simplify(-nu_exact/w - s**2*(c**2+w**2)/(6*w**4)) == 0
    print('Exact symbolic Hopf threshold, Fourier correction, resonance equations: PASS')


def periodic_check(c,w,trial_r):
    epsilon=w*w+c*c
    beta=c/epsilon
    s=sqrt(1-c)
    m=(w*w-2*c*s*s)/(4*w*w)
    assert abs(m)>1e-9
    mu=m*trial_r**2
    U=sqrt(1-c-mu)
    T0=2*pi/w
    k=s*s*(c*c+w*w)/(6*w**4)

    def vector(_,point):
        x,q=point
        return [(c+mu)*x-q-U*x*x-x*x*x/3,epsilon*x-c*q]

    def residual(params):
        x0,T=params
        q0=(c+mu)*x0-U*x0*x0-x0*x0*x0/3
        end=solve_ivp(vector,[0,T],[x0,q0],rtol=2e-11,atol=2e-12).y[:,-1]
        return [end[0]-x0,end[1]-q0]

    start=[trial_r-c*s*trial_r**2/(3*w*w),T0*(1+k*trial_r**2)]
    solution=root(residual,start,tol=1e-10)
    x0,T=solution.x
    assert solution.success, solution.message
    assert max(abs(z) for z in residual(solution.x))<1e-9
    predicted_ratio=k
    observed_ratio=(T/T0-1)/trial_r**2
    assert abs(observed_ratio-predicted_ratio)<0.01
    assert T>T0
    print(f'Numerical closed orbit: c={c:.2f}, w={w:.2f}, chosen amp={trial_r:.3f}, '
          f'coefficient estimate={observed_ratio:.8f}, theory={predicted_ratio:.8f}, '
          f'endpoint={max(abs(z) for z in residual(solution.x)):.2g}')


if __name__=='__main__':
    exact_checks()
    for triple in [(0.3,1.0,0.08),(0.3,1.0,0.04),(0.5,0.5,0.06),
                   (0.5,0.5,0.03),(0.9,0.5,0.04)]:
        periodic_check(*triple)
    print('All checks passed.')
