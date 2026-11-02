"""Finite exact checks for greedy independent-set occupancy on paths, cycles, and wheels.
Python >=3.10; only the standard library is required. These checks do not
constitute a proof of the asymptotic statements.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from math import factorial

checks = 0

def require(x, msg):
    global checks
    checks += 1
    if not x:
        raise AssertionError(msg)

def adjacency(kind, n):
    # n rim/path vertices; wheel has n+1 vertices.
    size = n + (kind == 'wheel')
    adj = [set() for _ in range(size)]
    for i in range(n-1):
        adj[i].add(i+1); adj[i+1].add(i)
    if kind != 'path':
        adj[n-1].add(0); adj[0].add(n-1)
    if kind == 'wheel':
        for i in range(n):
            adj[i].add(n); adj[n].add(i)
    return adj

def greedy(adj, order):
    taken = set()
    for v in order:
        if not (adj[v] & taken):
            taken.add(v)
    return len(taken)

def full_law(kind, n):
    a = adjacency(kind, n)
    counts = Counter(greedy(a, order) for order in permutations(range(len(a))))
    denom = factorial(len(a))
    return {k:Fraction(v, denom) for k,v in counts.items()}

def add_to_law(law, shift):
    return {k+shift:v for k,v in law.items()}

def expected(law, f=lambda k:k):
    return sum((q*f(k) for k,q in law.items()),Fraction(0))

# Generate path laws by splitting at the first accepted priority.
P = [{0:Fraction(1)}]
for n in range(1,15):
    law = Counter()
    for k in range(n):
        left = P[max(k-1,0)] if k>=1 else P[0] # length k-1, because first root is index k
        right = P[max(n-k-2,0)]
        for a,pa in left.items():
            for b,pb in right.items():
                law[1+a+b] += pa*pb/Fraction(n)
    P.append(dict(law))
    require(sum(P[-1].values()) == 1, 'path law normalization')

# Coefficients of exact analytic path moment generating functions.
# M(x)=(1-exp(-2x))/[2(1-x)^2],
# F(x)=sum E[X_n(X_n-1)]x^n
#   = x^2(1-exp(-2x))^2/[2(1-x)^3]
#     + [(2x-1)+(2x+1)exp(-4x)]/[4(1-x)^2].
def exp_coeff(r, j):
    return Fraction(r**j, factorial(j)) if j>=0 else Fraction(0)
def binom2(j):
    return j+1 if j>=0 else 0
def binom3(j):
    return (j+1)*(j+2)//2 if j>=0 else 0

def mean_formula(n):
    return sum((Fraction(j+1,2)*(int(k==0)-exp_coeff(-2,k))
                for k in range(n+1) for j in [n-k]), Fraction(0))

def factorial_formula(n):
    # coefficient x^2(1-2e^-2x+e^-4x)/[2(1-x)^3]
    lhs = sum((Fraction(binom3(n-2-k),2)*(
        (1 if k==0 else 0)-2*exp_coeff(-2,k)+exp_coeff(-4,k))
        for k in range(n-1)),Fraction(0))
    # coefficient ((2x-1)+(2x+1)e^-4x)/(4(1-x)^2)
    rhs = sum((Fraction(binom2(n-k),4)*(
            (2 if k==1 else 0)-(1 if k==0 else 0)
            + 2*exp_coeff(-4,k-1)+exp_coeff(-4,k))
            for k in range(n+1)),Fraction(0))
    return lhs+rhs

for n in range(1,15):
    mu = expected(P[n]); ff = expected(P[n], lambda k:k*(k-1))
    require(mu == mean_formula(n), f'path mean coefficient n={n}')
    require(ff == factorial_formula(n), f'path factorial second coefficient n={n}')
for n in range(1,8):
    require(full_law('path',n)==P[n],f'path brute n={n}')
for n in range(3,8):
    cyc = full_law('cycle',n)
    require(cyc==add_to_law(P[n-3],1),f'cycle first-vertex split n={n}')
for n in range(3,7):
    wheel = full_law('wheel',n)
    cyc = full_law('cycle',n)
    expected_w = Counter({1:Fraction(1,n+1)})
    for x,q in cyc.items():
        expected_w[x] += q*Fraction(n,n+1)
    require(wheel==dict(expected_w),f'wheel exact mixture n={n}')
    mu = expected(cyc); vv=expected(cyc,lambda k:k*k)-mu*mu
    wy=expected(wheel)
    wv=expected(wheel,lambda k:k*k)-wy*wy
    require(wv==Fraction(n,n+1)*vv + Fraction(n,(n+1)**2)*(mu-1)**2,
            f'wheel variance n={n}')

print(f'PASS: {checks} exact rational assertions, including independent permutation enumeration')
