"""Independent finite-dimensional checks of the Bessel auxiliary kernel.

Uses only the mathematical definitions in the accompanying result.
Finite tests cannot replace the infinite-dimensional proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import iv, ive
from scipy.stats import ncx2
from numpy.polynomial.legendre import leggauss

checks = 0


def check(predicate, description):
    global checks
    checks += 1
    if not predicate:
        raise AssertionError(description)


def kernel(x, y):
    if x == 0:
        return y * math.exp(-y)
    return math.exp(-x-y) * math.sqrt(y/x) * iv(1, 2*math.sqrt(x*y))


def poisson_gamma(x, y, n=70):
    return math.exp(-x-y) * sum(
        x**k * y**(k+1) / (math.factorial(k)*math.factorial(k+1))
        for k in range(n))


for x in [0, 0.04, 0.3, 1.0, 2.5]:
    for y in [0.02, 0.2, 0.8, 3.0]:
        p = kernel(x, y)
        check(abs(p-poisson_gamma(x, y)) < 3e-12,
              "kernel/Poisson-Gamma series disagrees")

for s in [0.25, 1.0, 3.0, 6.0]:
    q = 1-(1+s)*math.exp(-s)
    for x in [0, 0.04, 0.25, 1.0, 3.0, 7.0]:
        val = quad(lambda y: kernel(x, y), 0, s, epsabs=2e-11)[0]
        prob = ncx2.cdf(2*s, df=4, nc=2*x)
        check(abs(val-prob) < 2e-10,
              "row probability/cdf normalization disagrees")
        check(val <= q+3e-12, "gamma stochastic bound fails")
        if x == 0:
            check(abs(val-q)<1e-11, "sharp row-supremum limit fails")

for x in [.15,.55,1.4,3.2]:
    for y in [.18,.75,2.3,3.7]:
        check(abs(x*kernel(x,y)-y*kernel(y,x)) < 2e-13,
              "weighted detailed balance fails")


def sym_nystrom(s, n):
    nodes, weights = leggauss(n)
    nodes = (nodes+1)*s/2
    weights = weights*s/2
    arg = 2*np.sqrt(np.outer(nodes, nodes))
    # ive(1,z) is exp(-z)*I_1(z) for positive z.
    sym = np.exp(-nodes[:,None]-nodes[None,:]+arg)*ive(1,arg)
    return nodes, weights, sym*np.sqrt(np.outer(weights,weights))


for s in [0.25, 0.8, 2., 5., 10.]:
    q = 1-(1+s)*math.exp(-s)
    nodes,weights,A = sym_nystrom(s, 74)
    vals = np.linalg.eigvalsh(A)
    check(float(vals[0]) > -2e-12, "positive kernel spectrum")
    check(float(vals[-1]) <= q+1e-11, "spectral contraction")
    actual_trace = quad(lambda x: ive(1,2*x),0,s,epsabs=2e-11)[0]
    check(abs(np.trace(A)-actual_trace)<1e-10, "trace quadrature")
    for omega in [-1., -.7, 0., 2., 6.]:
        check(all(1+omega*vals > 0), "physical resolvent positivity")
        z = float(np.prod(1+omega*vals))
        check(z>0, "Fredholm approximation positive")
        bound = (1+omega*q)**-1 if omega<0 else 1.
        check(float(1/min(1+omega*vals)) <= bound+3e-11,
              "physical resolvent bound")

nodes,w,A=sym_nystrom(2,72)
v=np.cos(nodes)+.1
omega=-1
exact = np.linalg.solve(np.eye(len(v))+omega*A,v)
powers=v.copy()
approx=np.zeros_like(v)
for k in range(80):
    approx+=powers
    powers=(-omega)*(A@powers)
check(np.linalg.norm(exact-approx) < 2e-9, "geometric expansion")

xvalues = [0.24,0.72,1.83,4.20]
yvalues = [0.30,1.08,2.66,5.10]
for n in range(1,5):
    mat=np.array([[kernel(x,y) for y in yvalues[:n]]
                  for x in xvalues[:n]])
    check(float(np.linalg.det(mat))>0, "strict ordered minor")

for s in [100., 200., 1500.]:
    val=quad(lambda z: ive(1,2*z), 0, s,
             epsabs=1e-9, limit=300)[0]
    asym=math.sqrt(s/math.pi)
    check(val>0 and abs(val/asym-1)<0.10,
          "trace square-root growth")

print("PASS: {} independent finite checks".format(checks))
print("Tests: series identity, noncentral-chi-square CDF, detailed balance,")
print("ordered minors, positive spectral quadrature, trace, inverse norms,")
print("Neumann expansion, and long-time trace consistency.")
print("All-order/infinite-dimensional claims are analytic, not numerically certified.")
