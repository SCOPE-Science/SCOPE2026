"""Independent elementary checks for the nearest-neighbor adsorption gap law.

The analytical proof is in RESULT.md; this checker does not certify infinite-volume theorems.
Only Python standard library is needed.
"""
import math
import random

ASSERTIONS = 0

def near(a, b, tol=1e-11):
    global ASSERTIONS
    ASSERTIONS += 1
    assert math.isclose(a, b, rel_tol=tol, abs_tol=tol), (a, b, tol)

def affirmative(p):
    global ASSERTIONS
    ASSERTIONS += 1
    assert p

def simpson(fun, a, b, n=4000):
    assert n % 2 == 0
    h = (b-a)/n
    return h/3*(fun(a)+fun(b)+4*sum(fun(a+i*h) for i in range(1,n,2))
               +2*sum(fun(a+i*h) for i in range(2,n,2)))

def density(t):
    return (1-math.exp(-2*t))/2

def mix_density(u,t):
    return 2*math.exp(-2*u)/(1-math.exp(-2*t))

def z(u,t):
    return (1-u)*math.exp(u-t)

def cov_theory(t):
    den = math.expm1(2*t)
    return 2*(t-t*t+t*t*t/3)/den-(2*t/den)**2

# Numerical integration of the conditional two-half-line mixture.
for k in range(1,21):
    t = k/20
    near(simpson(lambda u: mix_density(u,t),0,t),1,1e-10)
    p3=simpson(lambda u: mix_density(u,t)*z(u,t),0,t)
    p33=simpson(lambda u: mix_density(u,t)*z(u,t)**2,0,t)
    near(p3,2*t/math.expm1(2*t),1e-10)
    near(p33,2*(t-t*t+t**3/3)/math.expm1(2*t),1e-10)
    near(p33-p3**2,cov_theory(t),1e-10)
    affirmative(cov_theory(t)>0)
    # One-site acceptance law and the half-line conditional occupation probability.
    near(density(t), (1-math.exp(-2*t))/2)

# The exact Palm joint probabilities in the jammed state.
e2=math.exp(2)
a=e2-1
joint={(3,3):2/(3*a),(3,2):4/(3*a),(2,3):4/(3*a),(2,2):1-10/(3*a)}
near(sum(joint.values()),1)
for key,val in joint.items():
    affirmative(0 < val < 1)
near(joint[3,3]+joint[3,2],2/a)
near(joint[3,3]-4/(a*a),2*(e2-7)/(3*a*a))
affirmative(joint[3,3]-4/(a*a)>0)

# Independent greedy-order simulation of finite periodic systems. The ring is long
# enough for the limiting infinite-volume local law to be a reliable comparison;
# this stochastic diagnostic is not used as an infinite-volume proof.
rng=random.Random(20261018)
counts={(x,y):0 for x in (2,3) for y in (2,3)}
N=350
TRIALS=1100
for repeat in range(TRIALS):
    order=list(range(N))
    rng.shuffle(order)
    occupied=[False]*N
    for i in order:
        if not occupied[(i-1)%N] and not occupied[(i+1)%N]:
            occupied[i]=True
    for i in range(N):
        if not occupied[i]:
            continue
        l=2 if occupied[(i-2)%N] else 3
        r=2 if occupied[(i+2)%N] else 3
        affirmative(occupied[(i-l)%N] and occupied[(i+r)%N])
        counts[l,r]+=1
sample=sum(counts.values())
for key,prob in joint.items():
    near(counts[key]/sample,prob,0.012)

print('passed_assertions=',ASSERTIONS)
print('sample_occupied_roots=',sample)
print('empirical=',{str(k):v/sample for k,v in counts.items()})
print('theoretical=',{str(k):v for k,v in joint.items()})
print('exact_covariance=',joint[3,3]-4/a**2)
