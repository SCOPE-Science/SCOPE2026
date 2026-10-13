from itertools import product
from collections import Counter

def friendship(r):
    n = 2*r + 1
    adj = [set() for _ in range(n)]
    for i in range(r):
        a, b = 1+2*i, 2+2*i
        for u,v in ((0,a),(0,b),(a,b)):
            adj[u].add(v)
            adj[v].add(u)
    return adj

def direct_tdrd(adj, f):
    positive = {v for v,x in enumerate(f) if x != 0}
    for v,x in enumerate(f):
        if x == 0:
            if not (any(f[u] == 3 for u in adj[v]) or
                    sum(f[u] == 2 for u in adj[v]) >= 2):
                return False
        elif x == 1:
            if not any(f[u] >= 2 for u in adj[v]):
                return False
    for v in positive:
        if not any(u in positive for u in adj[v]):
            return False
    return True

def mul(a,b):
    c = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j] += x*y
    return c

def power(a,r):
    c=[1]
    for _ in range(r):
        c=mul(c,a)
    return c

def shift(a,k):
    return [0]*k + a

def add(*ps):
    m=max(len(p) for p in ps)
    c=[0]*m
    for p in ps:
        for i,x in enumerate(p):
            c[i]+=x
    return c

P  = [1,1,1,1]
Q2 = [0,0,3,4,3,2,1]
Q1 = [0,0,0,4,3,2,1]
Q0 = [0,0,0,2,3,2,1]

def formula(r):
    a = power(P,2*r)
    a[0] -= 1
    return add(
        shift(a,3),
        shift(power(Q2,r),2),
        shift(power(Q1,r),1),
        power(Q0,r)
    )

labelings=0
for r in range(2,5):
    adj=friendship(r)
    actual=Counter()
    for f in product(range(4), repeat=2*r+1):
        labelings += 1
        if direct_tdrd(adj,f):
            actual[sum(f)] += 1
    predicted=formula(r)
    got=[actual[k] for k in range(len(predicted))]
    assert got == predicted, (r, got, predicted)
    gamma=min(actual)
    assert gamma == 4, (r,gamma)
    assert actual[4] == 2*r, (r,actual[4])
    assert sum(predicted) == (16**r - 1) + 13**r + 10**r + 8**r

print("VERIFY_OK")
print("friendship_parameters_checked = 2..4")
print("labelings_checked =", labelings)
print("all weight-enumerator coefficients matched")
print("all minimum weights matched 4")
print("all minimum-function counts matched 2r")
print("all total-function counts matched 16^r - 1 + 13^r + 10^r + 8^r")
