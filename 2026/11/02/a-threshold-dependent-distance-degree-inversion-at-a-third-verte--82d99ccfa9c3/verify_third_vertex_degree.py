"""Exact checks of the third-marked-vertex degree law for uniform labeled trees.

Run with Python 3. No third-party packages needed. Numerical asymptotic tests
are additional diagnostics and not a proof of the infinite-range statements.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, exp, sqrt, pi

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def tree_from_prufer(code, n):
    degree = [1] * n
    for value in code:
        degree[value] += 1
    adj = [[] for _ in range(n)]
    for value in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        adj[leaf].append(value)
        adj[value].append(leaf)
        degree[leaf] -= 1
        degree[value] -= 1
    endpoints = [i for i in range(n) if degree[i] == 1]
    a, b = endpoints
    adj[a].append(b)
    adj[b].append(a)
    return adj

def marked_tree_stats(adj):
    parent = [-1] * len(adj)
    parent[0] = 0
    queue = [0]
    for v in queue:
        for w in adj[v]:
            if parent[w] == -1:
                parent[w] = v
                queue.append(w)
    path = [1]
    while path[-1] != 0:
        path.append(parent[path[-1]])
    return len(path)-1, 2 in path, len(adj[2])

def conditional_joint(n, length):
    """Joint probabilities of on-path status and degree, exactly."""
    r = n - length - 1
    if r == 0:
        return {(True, 2): F(1)}
    p = F(length - 1, n - 2)
    out = Counter()
    for j in range(r):
        b = F(comb(r - 1, j) * (n - 1)**(r - 1 - j), n**(r - 1))
        out[(False, 1+j)] += (1-p)*b
        out[(True, 2+j)] += p*b*F(length, length+1)
        out[(True, 3+j)] += p*b*F(1, length+1)
    return dict(out)

def distance_pmf(n, length):
    return F((length+1)*factorial(n-2), factorial(n-length-1)*n**length)

def leaf_prob(n, length):
    r = n - length - 1
    if r == 0:
        return F(0)
    return F(r,n-2)*F((n-1)**(r-1),n**(r-1))

for n in range(3,9):
    observed = Counter()
    for code in product(range(n), repeat=n-2):
        observed[marked_tree_stats(tree_from_prufer(code,n))] += 1
    verify(sum(observed.values()) == n**(n-2), (n,'tree count'))
    for length in range(1,n):
        den = sum(c for (l,on,d),c in observed.items() if l==length)
        verify(F(den,n**(n-2)) == distance_pmf(n,length), (n,length,'distance'))
        pred = conditional_joint(n,length)
        verify(sum(pred.values()) == 1,(n,length,'mass'))
        for on in (False, True):
            for degree in range(1,n):
                real = F(observed.get((length,on,degree),0),den)
                verify(real == pred.get((on,degree),0), (n,length,on,degree,real,pred.get((on,degree),0)))
        mean = sum(degree*prob for (on,degree),prob in pred.items())
        formula = 2-F(2*(length+2)*(n-length-1),n*(length+1)*(n-2))
        verify(mean==formula,(n,length,'mean'))
        verify(sum(p for (on,d),p in pred.items() if d==1)==leaf_prob(n,length), (n,length,'leaf'))

for n in range(3,105):
    verify(sum(distance_pmf(n,l) for l in range(1,n))==1,(n,'distance pmf'))
    for l in range(1,n-1):
        verify(leaf_prob(n,l)>leaf_prob(n,l+1),(n,l,'strict leaf regression'))
        h=lambda t: 2-F(2*(t+2)*(n-t-1),n*(t+1)*(n-2))
        verify(h(l+1)>h(l),(n,l,'mean regression'))
    if n>=4:
        law1 = conditional_joint(n,n-2)
        law2 = conditional_joint(n,n-1)
        verify(sum(p for (on,d),p in law1.items() if d>=3)>0,(n,'stochastic crossing >=3'))
        verify(sum(p for (on,d),p in law1.items() if d>=2)<1,(n,'stochastic crossing >=2'))
        verify(law2=={(True,2):F(1)},(n,'endpoint'))

# Independent exact covariance via conditioning plus degree-sum identity.
for n in range(3,55):
    P={l:distance_pmf(n,l) for l in range(1,n)}
    EL=sum(l*p for l,p in P.items())
    Edeg=F(2*(n-1),n)
    ELD=sum(l*p*sum(d*q for (on,d),q in conditional_joint(n,l).items()) for l,p in P.items())
    cov=ELD-EL*Edeg
    endpoint_cov=1-F(sum(l*(l+1)*p for l,p in P.items()),n)
    verify(cov==-F(2,n-2)*endpoint_cov,(n,'total-degree covariance identity'))
    verify(cov>0,(n,'positive degree covariance'))

# Additional high-precision independent numerical trend checks, not infinite proofs.
def conditional_tail_float(n,l,threshold):
    r=n-l-1
    if r==0:
        return float(2>=threshold)
    p=(l-1)/(n-2)
    binom=(1-1/n)**(r-1)
    ans=0.0
    for j in range(r):
        if j+1>=threshold: ans+=(1-p)*binom
        if j+2>=threshold: ans+=p*binom*l/(l+1)
        if j+3>=threshold: ans+=p*binom/(l+1)
        if j<r-1: binom*=(r-1-j)/(j+1)/(n-1)
    return ans

for n in (200,500,1000):
    P={}
    prob=2/n
    for l in range(1,n):
        if l>1: prob*=F(l+1,l)*(1-l/n)
        P[l]=float(prob)
    EL=sum(l*p for l,p in P.items())
    for q in (2,4,5,6):
        cov=sum(p*(l-EL)*conditional_tail_float(n,l,q) for l,p in P.items())
        verify(cov>0 if q==2 else cov<0, (n,q,'asymptotic sign diagnostic'))
    verify(abs(sum(P.values())-1)<1e-11, (n,'mass float'))

print('PASS: %d exact-or-numerical assertions; all Cayley trees n=3..8 enumerated.'%checks)
