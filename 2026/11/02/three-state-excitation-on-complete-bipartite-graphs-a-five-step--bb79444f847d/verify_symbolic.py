"""Finite exhaustive proof and count-coefficient certificate for threshold-two excitation on K_{a,b}.

Run: python3 verify_symbolic.py
Only the Python standard library is required.
"""
from itertools import product
from collections import Counter
from math import factorial

# Capped multiplicity 2 means "at least two", not "exactly two".
profiles = [u for u in product(range(3), repeat=3) if sum(u) >= 2]
assert len(profiles) == 23


def tick(caps, labels):
    p, q = caps
    L, R = labels
    left_excited = min(2, sum(p[i] for i in range(3) if L[i] == 1))
    right_excited = min(2, sum(q[i] for i in range(3) if R[i] == 1))
    A = tuple((k + 1) % 3 if k else (1 if right_excited >= 2 else 0) for k in L)
    B = tuple((k + 1) % 3 if k else (1 if left_excited >= 2 else 0) for k in R)
    return A, B


def signature(caps, labels):
    return tuple(tuple(labels[s][j] if caps[s][j] else -1 for j in range(3)) for s in range(2))


def classify(caps):
    labels = ((0, 1, 2), (0, 1, 2))
    seen = {}
    for time in range(18):
        state = signature(caps, labels)
        if state in seen:
            return seen[state], time-seen[state]
        seen[state] = time
        labels = tick(caps, labels)
    raise AssertionError(('nonperiodic in tested horizon', caps))


def weight(n, profile):
    total = 0
    for k0 in range(n+1):
        for k1 in range(n-k0+1):
            k2 = n-k0-k1
            counts = k0,k1,k2
            if all(min(2, counts[j]) == profile[j] for j in range(3)):
                total += factorial(n)//(factorial(k0)*factorial(k1)*factorial(k2))
    return total


def P(n):
    if n < 4: return 0
    return (n+2)*2**(n-1)-2*n*n-2*n-2

def Q(n):
    return n*(n-1) if n >= 4 else 0

def H(n):
    if n < 4: return 0
    return 3**n - 3*2**n - 3*n*2**(n-1) + 3*(n*n+n+1)

def B4(a,b):
    pa,pb,qa,qb,ha,hb=P(a),P(b),Q(a),Q(b),H(a),H(b)
    return (6*pa*pb + 3*(pa*qb+qa*pb) + 2*qa*qb
            + (3*pa+qa)*hb + ha*(3*pb+qb))

# Exhaustive tagged transition certificate: actual vertices of the same
# initial color on a shore have identical future colors.  All operations
# involving their multiplicities are additions and comparisons to two.
classes = {}
periods = Counter()
entries = Counter()
for left, right in product(profiles, repeat=2):
    entry, period = classify((left, right))
    classes[left, right] = entry, period
    periods[period] += 1
    entries[entry, period] += 1
    assert entry <= 5
    assert period in (1,3,4)
assert len(classes) == 529
assert periods == {1:476, 3:1, 4:52}, periods
assert entries == {
    (0,1):1,(1,1):35,(2,1):223,(3,1):142,(4,1):51,(5,1):24,
    (0,3):1,
    (0,4):2,(1,4):10,(2,4):30,(3,4):8,(4,4):2,
}, entries
assert [(p,q) for (p,q),(t,d) in classes.items() if d==3] == [((2,2,2),(2,2,2))]
assert set((p,q) for (p,q),(t,d) in classes.items() if t==0 and d==4) == {
    ((2,0,2),(2,2,0)),((2,2,0),(2,0,2))}

# Coefficient matrix M: rows and columns ordered U,A,Q,H, corresponding
# to profiles with one 0 and two capped 2s; one 1 and two capped 2s;
# two 1s and one capped 2; three capped 2s, respectively.
def kind(profile):
    s = sorted(profile)
    return {(0,2,2):0,(1,2,2):1,(1,1,2):2,(2,2,2):3}.get(tuple(s),None)
M = [[0]*4 for _ in range(4)]
for (p,q),(t,d) in classes.items():
    if d==4:
        i,j=kind(p),kind(q)
        assert i is not None and j is not None
        M[i][j] += 1
assert M == [[6,6,3,3],[6,6,3,3],[3,3,2,1],[3,3,1,0]], M

# The sharp transient-time cases have these smallest-size witnesses.
witnesses = [
    (2,2,(0,2,0),(1,0,1),3),
    (2,3,(2,0,0),(0,2,1),4),
    (3,3,(0,2,1),(2,0,0),4),
    (3,4,(2,0,1),(0,2,2),5),
]
for a,b,p,q,t in witnesses:
    assert classify((p,q))[0] == t
    assert sum(max(2,v) if v == 2 else v for v in p) <= a
    assert sum(max(2,v) if v == 2 else v for v in q) <= b

def possible(n,p):
    needed = sum(2 if u==2 else u for u in p)
    return needed<=n and (2 in p or needed==n)

for a in range(2,11):
    for b in range(2,11):
        largest = max(t for (p,q),(t,d) in classes.items() if possible(a,p) and possible(b,q))
        predicted = (3 if a==b==2 else
                     4 if min(a,b)==2 or a==b==3 else 5)
        assert largest==predicted, (a,b,largest,predicted)

# Exact n-specific labelled-state verification for every 2 <= a,b <= 10;
# this cross-checks the closed formulas against the 529-class census.
for a in range(2,11):
    for b in range(2,11):
        W_a = {p:weight(a,p) for p in profiles}
        W_b = {p:weight(b,p) for p in profiles}
        vals = Counter()
        for (p,q),(t,period) in classes.items():
            vals[period] += W_a[p]*W_b[q]
        assert sum(vals.values())==3**(a+b), (a,b,vals)
        assert vals[3]==H(a)*H(b), (a,b,vals)
        assert vals[4]==B4(a,b), (a,b,vals,B4(a,b))
        assert vals[1]==3**(a+b)-H(a)*H(b)-B4(a,b)
print('PASS: 529 exhaustive tagged classes, 5-step bound, only periods 1,3,4')
print('PASS: period-4 coefficient matrix', M)
print('PASS: all 81 ordered sizes 2<=a,b<=10, exact weighted formula')
print('PASS: period-three condition, sharp period-four witness and all classes')
