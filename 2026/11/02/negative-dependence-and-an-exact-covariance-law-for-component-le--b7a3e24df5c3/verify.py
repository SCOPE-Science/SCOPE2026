#!/usr/bin/env python3
"""Exact finite checks for cross-root leaf dependence in a multinomial Hoppe forest.

Only Python's standard library is required. Run: python multihoppe_checker.py
The enumeration considers every possible sequence of attachments, weighted by its
exact rational probability; the unbounded theorems require the written proofs.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial

assertions = 0
assignments = 0

def check(cond, label):
    global assertions
    assert cond, label
    assertions += 1

def rise(x, n):
    out = F(1)
    for i in range(n):
        out *= x + i
    return out

def exact_distribution(weights, n):
    """Returns the exact joint probability law of (colors' leaves, colors' sizes)."""
    global assignments
    d = len(weights)
    theta = sum(weights)
    probs = {}
    parents, colors = [], []
    def visit(t, probability):
        global assignments
        if t == n:
            assignments += 1
            childcounts = [0] * n
            sizes = [0] * d
            for i, par in enumerate(parents):
                sizes[colors[i]] += 1
                if par >= 0:
                    childcounts[par] += 1
            leaves = [0] * d
            for i, c in enumerate(colors):
                if childcounts[i] == 0:
                    leaves[c] += 1
            key = tuple(leaves), tuple(sizes)
            probs[key] = probs.get(key, F(0)) + probability
            return
        denominator = theta + t
        for j, w in enumerate(weights):
            parents.append(-j - 1)
            colors.append(j)
            visit(t+1, probability * w / denominator)
            parents.pop(); colors.pop()
        for i in range(t):
            parents.append(i)
            colors.append(colors[i])
            visit(t+1, probability / denominator)
            parents.pop(); colors.pop()
    visit(0, F(1))
    return probs

def closed_mu(n, theta):
    if n == 0:
        return F(0)
    return F(n*(n+2*theta-1),2*(n+theta-1))

def closed_h(n, theta):
    if n <= 1:
        return F(0)
    return F(n*(n-1)*(2*theta+n), 2*theta*(theta+1)*(theta+n-1))

def closed_j(n, theta):
    if n <= 1:
        return F(0)
    num = n*(n-1)*(4*theta**2+4*(n-1)*theta+n*(n-1)-2)
    den = 4*theta*(theta+1)*(theta+n-2)*(theta+n-1)
    return num/den

def test_recurrence(theta, maximum_n=40):
    mu, h, j = F(0), F(0), F(0)
    for n in range(maximum_n+1):
        check(mu == closed_mu(n, theta), ('mean recurrence',theta,n))
        check(h == closed_h(n, theta), ('size-leaf recurrence',theta,n))
        check(j == closed_j(n, theta), ('leaf-pair recurrence',theta,n))
        if n == maximum_n:
            break
        new_j = (1-F(2,theta+n))*j + (2*mu/theta+2*h)/(theta+n)
        new_h = h + (mu/theta+F(n,theta)+F(n*(n-1),theta*(theta+1)))/(theta+n)
        new_mu = (1-F(1,theta+n))*mu + 1
        j, h, mu = new_j, new_h, new_mu

def test_enumeration(weights, n):
    theta = sum(weights)
    d = len(weights)
    dist = exact_distribution(weights, n)
    check(sum(dist.values()) == 1, ('normalization',weights,n))
    mu = closed_mu(n, theta)
    h, j = closed_h(n, theta), closed_j(n, theta)
    sizes = [sum(p*s[i] for (l,s),p in dist.items()) for i in range(d)]
    means = [sum(p*l[i] for (l,s),p in dist.items()) for i in range(d)]
    for i in range(d):
        check(sizes[i] == F(n)*weights[i]/theta, ('size means',weights,n,i))
        check(means[i] == weights[i]*mu/theta, ('leaf means',weights,n,i))
    for i,k in combinations(range(d),2):
        mixed = sum(p*l[i]*l[k] for (l,s),p in dist.items())
        size_leaf = sum(p*s[i]*l[k] for (l,s),p in dist.items())
        check(mixed == weights[i]*weights[k]*j, ('mixed leaf formula',weights,n,i,k))
        check(size_leaf == weights[i]*weights[k]*h, ('mixed size-leaf formula',weights,n,i,k))
        check(mixed < means[i]*means[k], ('strict negative covariance',weights,n,i,k))
        for a in range(1,n+1):
            p_a = sum(p for (l,s),p in dist.items() if l[i] >= a)
            for b in range(1,n+1):
                p_b = sum(p for (l,s),p in dist.items() if l[k] >= b)
                p_ab = sum(p for (l,s),p in dist.items() if l[i] >= a and l[k] >= b)
                check(p_ab <= p_a*p_b, ('negative quadrant',weights,n,i,k,a,b))
    for s_tuple in set(s for l,s in dist):
        p_size = sum(p for (l,s),p in dist.items() if s == s_tuple)
        target = F(factorial(n),1)/rise(theta,n)
        for i, z in enumerate(s_tuple):
            target *= rise(weights[i],z)/factorial(z)
        check(p_size == target, ('size law',weights,n,s_tuple))

for w in ((F(1),F(1)), (F(1,2),F(3,2)), (F(1),F(2),F(3,2))):
    test_recurrence(sum(w), 40)
    for n in range(1,7 if len(w)==2 else 6):
        test_enumeration(w,n)
print('PASS assertions=', assertions, ' attachment_histories=', assignments)
