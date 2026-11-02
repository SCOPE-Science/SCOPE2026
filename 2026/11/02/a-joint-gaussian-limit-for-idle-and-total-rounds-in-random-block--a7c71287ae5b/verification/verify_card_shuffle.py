"""Reproducible independent finite tests for stochastic shuffling moments."""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial, exp, sqrt
import math

CHECKS = 0

def check(test, message):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(message)

def exact_probs(k):
    p = []
    for r in range(k):
        q = sum((Fraction((-1)**j, factorial(j)) * Fraction(k-r-j, k)
                 for j in range(k-r)), Fraction(0))
        p.append(q / factorial(r))
    return p

def enum_probs(k):
    cnt = Counter()
    for perm in permutations(range(k)):
        hits = sum(perm[i+1] == perm[i]+1 for i in range(k-1))
        cnt[hits] += 1
    return [Fraction(cnt[r], factorial(k)) for r in range(k)]

def moment_table(probs):
    # Vectors of raw moments (T,Q,T^2,Q^2,TQ), where Q is the number of idle rounds.
    M = [None,(Fraction(0),)*5]
    for k in range(2, len(probs)):
        pr = probs[k]
        p0 = pr[0]
        a = 1-p0
        t = (1+sum((pr[r]*M[k-r][0] for r in range(1,k)),Fraction(0))) / a
        q = (p0+sum((pr[r]*M[k-r][1] for r in range(1,k)),Fraction(0))) / a
        tt = (2*t-1+sum((pr[r]*M[k-r][2] for r in range(1,k)),Fraction(0))) / a
        qq = (p0*(1+2*q)+sum((pr[r]*M[k-r][3] for r in range(1,k)),Fraction(0))) / a
        tq = (p0*(1+t+q)+sum((pr[r]*(M[k-r][1]+M[k-r][4]) for r in range(1,k)),Fraction(0))) / a
        M.append((t,q,tt,qq,tq))
    return M

# Verify exact factorial-moment formula and combinatorial distribution, not just simulator.
for k in range(2,9):
    ex = exact_probs(k)
    en = enum_probs(k)
    for r in range(k):
        check(ex[r] == en[r], f"distribution k={k} r={r}")
    check(sum(ex) == 1, f"mass k={k}")
    for r in range(k):
        actual = sum((ex[v] * (factorial(v)//factorial(v-r)) for v in range(r,k)),Fraction(0))
        check(actual == Fraction(k-r,k), f"factorial k={k} r={r}")

# Independent renewal calculation for state k=2: geometric waiting with success probability 1/2.
pr = [None, None]+[exact_probs(k) for k in range(2,24)]
M = moment_table(pr)
check(M[2] == (Fraction(2),Fraction(1),Fraction(6),Fraction(3),Fraction(4)), "k=2 moments")
for k in range(2,24):
    t,q,tt,qq,tq=M[k]
    check(t>0 and 0<=q<t, f"means k={k}")
    check(tt-t*t>=0 and qq-q*q>=0, f"variance positivity k={k}")
    check((tt-t*t)*(qq-q*q) >= (tq-t*q)**2, f"covariance Cauchy k={k}")

# Numerical large-state test with exact finite transition coefficients evaluated as floats.
# We keep all probabilities above 1e-18 and renormalize to avoid floating underflow.
def approx_probs(k):
    if k < 40:
        return [float(v) for v in exact_probs(k)]
    R=min(20,k-1)
    p=[math.exp(-1)/factorial(r)*(1-(r-1)/k) for r in range(R+1)]
    p[0] += 1-sum(p)
    return p

last=3500
q0=exp(-1)
arr=[None,(0.,0.,0.,0.,0.)]
for k in range(2,last+1):
    p=approx_probs(k)
    p0=p[0]
    a=1-p0
    t=(1+sum(p[r]*arr[k-r][0] for r in range(1,len(p))))/a
    q=(p0+sum(p[r]*arr[k-r][1] for r in range(1,len(p))))/a
    tt=(2*t-1+sum(p[r]*arr[k-r][2] for r in range(1,len(p))))/a
    qq=(p0*(1+2*q)+sum(p[r]*arr[k-r][3] for r in range(1,len(p))))/a
    tq=(p0*(1+t+q)+sum(p[r]*(arr[k-r][1]+arr[k-r][4]) for r in range(1,len(p))))/a
    arr.append((t,q,tt,qq,tq))

for n in (500,1200,3500):
    t,q,tt,qq,tq=arr[n]
    st=(tt-t*t)/n
    sq=(qq-q*q)/n
    stq=(tq-t*q)/n
    check(abs(t/n-1)<0.04, f"T/n n={n}")
    check(abs(q/n-q0)<0.04, f"Q/n n={n}")
    tol=0.11 if n==500 else (0.07 if n==1200 else 0.035)
    check(abs(st-1)<tol, f"VarT/n n={n} got {st}")
    check(abs(sq-(q0+2*q0*q0))<tol, f"VarQ/n n={n} got {sq}")
    check(abs(stq-2*q0)<tol, f"Cov/n n={n} got {stq}")
    print(f"n={n}  E[T]/n={t/n:.8f}  E[Q]/n={q/n:.8f} "
          f"VarT/n={st:.8f} VarQ/n={sq:.8f} Cov/n={stq:.8f}")

print('PASS', CHECKS, 'checks')
