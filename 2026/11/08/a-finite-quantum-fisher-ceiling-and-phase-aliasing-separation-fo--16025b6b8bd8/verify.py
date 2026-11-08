"""Independent numerical diagnostics for globally reset Rabi-spin information.

Requires Python 3, numpy and scipy. Does not certify infinite-population limits.
"""
import math
from scipy.integrate import quad
from scipy.special import comb

A = math.pi / 2.0
checks = 0

def near(v, target, atol=1e-10, rtol=1e-8):
    global checks
    assert abs(v-target) <= atol + rtol*abs(target), (v,target)
    checks += 1

def strict(cond):
    global checks
    assert bool(cond)
    checks += 1

def g(theta,x):
    return x*math.cosh(x*(A-theta))/math.sinh(x*A)

def score_z(theta,x):
    return 1/x+(A-theta)*math.tanh(x*(A-theta))-A/math.tanh(x*A)

def phase_density(phi,x):
    return x*math.exp(-x*phi)/(-math.expm1(-math.pi*x))

def phase_score(phi,x):
    return 1/x-phi-math.pi/math.expm1(math.pi*x)

def phase_information(x):
    return 1/x**2-math.pi**2/(4*math.sinh(math.pi*x/2)**2)

def z_information(x):
    return quad(lambda th:g(th,x)*score_z(th,x)**2,0,A,epsabs=1e-13)[0]

def z_count(x,n):
    rows=[]
    for k in range(n+1):
        def kernel(th):
            return float(comb(n,k))*math.sin(th)**(2*k)*math.cos(th)**(2*(n-k))
        p=quad(lambda th:kernel(th)*g(th,x),0,A,epsabs=1e-13)[0]
        dp=quad(lambda th:kernel(th)*g(th,x)*score_z(th,x),0,A,epsabs=1e-13)[0]
        rows.append((p,dp))
    return rows

def count_info(rows):
    return sum(dp*dp/p for p,dp in rows)

for x in (0.04,0.15,0.6,1.0,2.0,5.0):
    near(quad(lambda th:g(th,x),0,A)[0],1.0)
    near(quad(lambda th:g(th,x)*score_z(th,x),0,A)[0],0.0,atol=2e-10)
    near(quad(lambda ph:phase_density(ph,x),0,math.pi)[0],1.0)
    near(quad(lambda ph:phase_density(ph,x)*phase_score(ph,x),0,math.pi)[0],0.0,atol=2e-10)
    j=quad(lambda ph:phase_density(ph,x)*phase_score(ph,x)**2,0,math.pi)[0]
    near(j,phase_information(x),atol=4e-12)
    strict(0<z_information(x)<j<1/x**2)
    for th in (0.12,0.56,1.21):
        near(g(th,x),phase_density(th,x)+phase_density(math.pi-th,x))
    last=0.0
    for n in (1,2,3,4,6,9,12):
        rows=z_count(x,n)
        near(sum(p for p,_ in rows),1)
        near(sum(dp for _,dp in rows),0,atol=1e-11)
        info=count_info(rows)
        strict(last < info < z_information(x))
        last=info
        if n==1:
            near(rows[0][0],1-2/(x*x+4),atol=3e-12)
            near(rows[1][0],2/(x*x+4),atol=3e-12)
            near(info,8*x*x/((x*x+4)**2*(x*x+2)),atol=1e-11)
        if n in (2,4):
            step=1e-5*max(1,x)
            hi=z_count(x+step,n)
            lo=z_count(x-step,n)
            for k in range(n+1):
                near((hi[k][0]-lo[k][0])/(2*step),rows[k][1],atol=2e-9,rtol=2e-6)

for x in (0.02,0.01):
    near(z_information(x)/(x*x),math.pi**4/180,rtol=0.003)
    near(phase_information(x),math.pi**2/12,rtol=0.0005)
for x in (8.0,12.0):
    near(x*x*z_information(x),1.0,rtol=0.00006)
    near(x*x*phase_information(x),1.0,rtol=0.00006)

print(f'PASS: {checks} finite diagnostics; no claim of infinite-proof certification.')

# Independent density-matrix quantum-Fisher check for small ensembles.
# This construction starts from the stationary density operator rather than
# the closed-form folded-phase Fisher integral.
import numpy as np
from numpy.polynomial.legendre import leggauss

nodes,weights=leggauss(180)
phis=(nodes+1)*math.pi/2
weights=weights*math.pi/2

def numerical_qfi(x,n):
    dim=2**n
    rho=np.zeros((dim,dim),dtype=complex)
    deriv=np.zeros_like(rho)
    for ph,w in zip(phis,weights):
        u=np.array([math.cos(ph),-1j*math.sin(ph)])
        v=u.copy()
        for _ in range(1,n):
            v=np.kron(v,u)
        pure=np.outer(v,v.conj())
        rho+=w*phase_density(ph,x)*pure
        deriv+=w*phase_density(ph,x)*phase_score(ph,x)*pure
    ev,U=np.linalg.eigh(rho)
    d=U.conj().T@deriv@U
    val=0.0
    for i in range(dim):
        for j in range(dim):
            denom=ev[i]+ev[j]
            if denom>1e-10:
                val+=2*abs(d[i,j])**2/denom
    return val,float(np.real(np.trace(rho))),float(np.real(np.trace(deriv)))

for x in (0.2,1.0,4.0):
    prev=0.0
    for n in (1,2,3,4):
        q,trace,trace_d=numerical_qfi(x,n)
        near(trace,1.0,atol=1e-11)
        near(trace_d,0.0,atol=1e-11)
        strict(0<q<=phase_information(x)+1e-10)
        strict(q>prev+1e-10)
        strict(q+1e-10>=count_info(z_count(x,n)))
        prev=q

# Independent physical-age renewal integral checks: the period-folding
# identity agrees with an exponential reset age measured in time units.
for x in (0.8,1.7):
    for n,k in ((1,1),(2,1),(4,2)):
        folded=z_count(x,n)[k][0]
        def unconditional(t):
            return x*math.exp(-x*t)*float(comb(n,k))*math.sin(t)**(2*k)*math.cos(t)**(2*(n-k))
        raw=quad(unconditional,0,45/x,epsabs=1e-12,limit=400)[0]
        near(folded,raw,atol=2e-11)
print(f'PASS including independent density-matrix replay: {checks} finite diagnostics.')
