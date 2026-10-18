"""Reproduce finite Fourier and feasibility checks for fastest-mixing cycle products.

Requires only the Python standard library. This script checks examples, not the
infinite-family proof, which is the accompanying analytical argument.
"""
import itertools
import math
import random

checks = 0

def check(condition, message="check failed"):
    global checks
    assert condition, message
    checks += 1

def nearly(a, b, tolerance=5e-10):
    return abs(a-b) <= tolerance

def parameters(sizes):
    delta = [2-2*math.cos(2*math.pi/n) for n in sizes]
    Delta = [2-2*math.cos(2*math.pi*(n//2)/n) for n in sizes]
    S = sum(1/q for q in delta)
    R = sum(v/q for v,q in zip(Delta,delta))
    K = 4*S-R
    t = min(1/(2*S), 2/(1+R))
    weights = [t/q for q in delta]
    hold = 1-2*sum(weights)
    return delta, Delta, S, R, K, t, weights, hold

def full_fourier_slem(sizes, weights):
    mu = 0.0
    eigen = []
    for indices in itertools.product(*(range(n) for n in sizes)):
        v = 1-sum(w*(2-2*math.cos(2*math.pi*k/n))
                  for w,k,n in zip(weights,indices,sizes))
        if any(indices):
            mu = max(mu,abs(v))
            eigen.append(v)
        else:
            check(nearly(v,1))
    return mu,eigen

families = [
    (3,3), (3,4), (3,5), (4,4), (5,7), (5,8),
    (3,3,3), (3,3,4), (3,4,5), (3,5,7), (4,6,8),
    (3,3,3,3), (3,3,4,6), (3,5,7,9), (3,5,8,9), (4,5,6,7),
]
rng = random.Random(2027)
for sizes in families:
    delta,Delta,S,R,K,t,weights,hold = parameters(sizes)
    check(len(weights)==len(sizes))
    check(all(w>0 for w in weights))
    check(hold>=-1e-12)
    check(nearly(1-hold,2*sum(weights)))
    check(nearly(4*S-R,K))
    check(nearly(t,min(1/(2*S),2/(1+R))))
    mu,eigen = full_fourier_slem(sizes,weights)
    check(nearly(mu,1-t),str(sizes))
    check(nearly(max(eigen),1-t),str(sizes))
    check(nearly(min(eigen),1-sum(w*D for w,D in zip(weights,Delta))))
    check((K<1-1e-12 and hold>0) or (K>=1-1e-12 and abs(hold)<1e-11))
    odd = [n for n in sizes if n%2]
    predicted_zero = (len(odd)>=4 or (len(odd)==3 and all(n==3 for n in odd)))
    check((abs(hold)<1e-11)==predicted_zero,str(sizes))
    check(nearly(K,sum(1/(4*math.cos(math.pi/(2*n))**2) for n in odd)))
    # Feasible nonsymmetric orbit rates: feasible random point cannot beat the theorem.
    for _ in range(80):
        raw = [rng.expovariate(1) for _ in sizes]
        factor = rng.random()/(2*sum(raw))
        trial = [x*factor for x in raw]
        score,_ = full_fourier_slem(sizes,trial)
        check(score>=mu-5e-11)

# Algebraic boundary instances whose spectral values are rational.
for sizes, expected_K in [((3,3),2/3),((3,3,3),1),((3,3,3,3),4/3),((3,3,4,6),2/3)]:
    p=parameters(sizes)
    check(nearly(p[4],expected_K))

# The exact odd-axis count threshold and its range check to order 199.
for n in range(3,200,2):
    k=1/(4*math.cos(math.pi/(2*n))**2)
    check(1/4<k<=1/3+1e-13)
    if n>3:
        check(k<1/3)

# Elongated torus: speedup over the best COMMON edge rate approaches dimension.
for short_sizes in [(3,5),(4,6),(3,4,5),(3,5,7)]:
    d=len(short_sizes)+1
    for N in [101,301,1001]:
        sizes=(N,)+short_sizes
        delta,Delta,S,R,K,t,weights,hold=parameters(sizes)
        equal_weight=min(1/(2*d),2/(min(delta)+sum(Delta)))
        equal_gap=min(equal_weight*min(delta),2-equal_weight*sum(Delta))
        ratio=t/equal_gap
        check(abs(ratio-d)<0.15, (sizes,ratio))
        check(abs(N*N*t-2*math.pi**2)<0.25)

print("verification_pass:",checks,"assertions")
