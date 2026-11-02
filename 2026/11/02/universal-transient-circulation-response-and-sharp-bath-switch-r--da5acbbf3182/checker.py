"""Independent finite-dimensional numerical checks of a harmonic diffusion response law.

Requires numpy and scipy. Numerical checks support, but do not establish, the
all-parameter and all-measurable-protocol theorem.
"""
import math
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.linalg import solve_continuous_lyapunov

rng = np.random.default_rng(20874)
count = 0
for case in range(180):
    a = rng.uniform(0.6, 3.7)
    b = rng.uniform(0.6, 3.7)
    c = rng.uniform(-0.82, 0.82) * math.sqrt(a*b)
    s = a + b
    tx0, ty0 = rng.uniform(0.2, 4.0, 2)
    tx1, ty1 = rng.uniform(0.2, 4.0, 2)
    A = np.array([[a,c],[c,b]])
    # Prepare arbitrary Gaussian or deterministic initial second-moment matrices;
    # the theorem applies beyond Gaussian laws as it uses only raw second moments.
    if case % 3 == 0:
        M0 = solve_continuous_lyapunov(A, np.diag([2*tx0,2*ty0]))
    else:
        H = rng.normal(size=(2,2))
        M0 = H @ H.T
    D1 = np.diag([tx1,ty1])
    def ode(t,v):
        M = np.array([[v[0],v[1]],[v[1],v[2]]])
        R = -A @ M - M @ A + 2*D1
        return [R[0,0], R[0,1], R[1,1]]
    def q(v):
        return c*(v[2]-v[0]) + (a-b)*v[1]
    q0 = q([M0[0,0],M0[0,1],M0[1,1]])
    qinf = 2*c*(ty1-tx1)/s
    horizon = 5/s
    sol = solve_ivp(ode,(0,horizon),[M0[0,0],M0[0,1],M0[1,1]],rtol=1e-11,atol=1e-12,dense_output=True)
    assert sol.success
    for t in np.linspace(0,horizon,9):
        direct = q(sol.sol(t))
        reduced = qinf + (q0-qinf)*math.exp(-s*t)
        assert abs(direct-reduced) < 1e-8*(1+abs(reduced)), (case,t,direct,reduced)
        count+=1

# Sharp sign reversal, stationary preparation and maximally negative controls.
for case in range(120):
    a,b = rng.uniform(0.5,4,2)
    c = rng.uniform(0.03,0.75)*math.sqrt(a*b)
    s = a+b
    delta0 = rng.uniform(0.05,4)
    B = rng.uniform(0.05,4)
    tstar = math.log1p(delta0/B)/s
    # Exact stationary prep is possible with positive temperatures.
    tempmean = 1+max(delta0,B)
    M0 = solve_continuous_lyapunov(np.array([[a,c],[c,b]]),
        np.diag([2*(tempmean-delta0/2),2*(tempmean+delta0/2)]))
    q0 = c*(M0[1,1]-M0[0,0])+(a-b)*M0[0,1]
    assert abs(q0 - 2*c*delta0/s) < 1e-10
    def qext(t):
        return (2*c/s)*(-B + (delta0+B)*math.exp(-s*t))
    assert qext(tstar*0.999)>0 and abs(qext(tstar))<1e-12 and qext(tstar*1.001)<0
    # Any protocol Delta >= -B has Q >= Q_ext via positive convolution.
    for t in [0,tstar/2,tstar,2*tstar]:
        def fn(u):
            delta=-B+0.1*(1+math.sin(3*u))
            return math.exp(-s*(t-u))*delta
        qc=math.exp(-s*t)*q0+2*c*quad(fn,0,t,epsabs=1e-12)[0]
        assert qc>=qext(t)-1e-10
        count+=1
print(f"PASS: {count} independently assembled finite-parameter response/control comparisons")
