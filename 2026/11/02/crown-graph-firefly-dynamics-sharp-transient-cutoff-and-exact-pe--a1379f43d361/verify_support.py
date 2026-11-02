#!/usr/bin/env python3
"""Exact finite-state certificate for three-color inhibitory dynamics on matched-deleted bicliques."""
from collections import Counter
from itertools import product
from math import factorial, comb, lcm

STATES = tuple(product(range(3), repeat=9))

def next_symbol(j, cap):
    a, b = divmod(j, 3)
    a_one = min(2, cap[3] + cap[4] + cap[5])
    b_one = min(2, cap[1] + cap[4] + cap[7])
    if not (a == 2 and b_one - (b == 1) > 0):
        a = (a + 1) % 3
    if not (b == 2 and a_one - (j // 3 == 1) > 0):
        b = (b + 1) % 3
    return 3 * a + b

def next_cap(cap):
    new = [0] * 9
    for j, c in enumerate(cap):
        if c:
            k = next_symbol(j, cap)
            new[k] = min(2, new[k] + c)
    return tuple(new)

def dynamics(cap):
    seen, path = {}, []
    while cap not in seen:
        seen[cap] = len(path)
        path.append(cap)
        cap = next_cap(cap)
    entry = seen[cap]
    loop = path[entry:]
    support = {j for j, c in enumerate(loop[0]) if c}
    permutation = {}
    for j in support:
        v = j
        for stage in loop:
            v = next_symbol(v, stage)
        permutation[j] = v
    assert set(permutation) == set(permutation.values()) == support
    visited = set()
    order = 1
    for j in support:
        if j in visited:
            continue
        k, q = j, 0
        while k not in visited:
            visited.add(k)
            q += 1
            k = permutation[k]
        assert k == j
        order = lcm(order, q)
    return entry, len(loop) * order, tuple(loop)

# Coefficients of z^a y^b, where y=exp(z)-1-z.
P4_EXPECT = {
(0,2):4,(0,3):8,(0,4):2,(1,2):36,(1,3):24,(1,4):4,
(2,1):52,(2,2):68,(2,3):24,(2,4):2,
(3,1):72,(3,2):48,(3,3):8,(4,0):25,(4,1):39,
(4,2):12,(5,0):11,(5,1):8,(6,0):2,
}

all_by_period = Counter()
poly = {3:Counter(),4:Counter(),18:Counter(),1:Counter()}
recurrent = {3:Counter(),4:Counter(),18:Counter(),1:Counter()}
max_tau = Counter()
cyc = set()
cap_tau = {}
for state in STATES:
    tau, period, loop = dynamics(state)
    assert period in (1,3,4,18)
    assert (period == 1) == (sum(state) == 0)
    assert tau <= 13
    cyc.add(min(loop))
    all_by_period[period] += 1
    key = (state.count(1), state.count(2))
    poly[period][key] += 1
    if tau == 0:
        recurrent[period][key] += 1
    max_tau[period] = max(max_tau[period], tau)
    cap_tau[state] = tau

assert len(STATES) == 19683
assert len(cyc) == 33
assert poly[4] == Counter(P4_EXPECT)
assert poly[18] == Counter({(3,0):24})
assert max_tau[3] == 13 and max_tau[4] == 9 and max_tau[18] == 3
assert recurrent[18] == Counter({(3,0):12})
assert recurrent[4] == Counter({(0,4):2,(1,3):8,(0,3):8,
  (2,2):12,(1,2):16,(0,2):4,(4,1):1,(3,1):8,(2,1):8,(5,0):1,(4,0):3})
# The expected recurrent polynomial is equivalently:
# 2*y^4 + (8*z+8)*y^3 + (12*z^2+16*z+4)*y^2
# + (z^4+8*z^3+8*z^2)*y + z^5+3*z^4.

# A finite exact count of length-n words using symbolic multiplicity classes.
def at_least_two(n, b):
    ways = [0] * (n+1)
    ways[0] = 1
    for _ in range(b):
        nxt = [0] * (n+1)
        for s, v in enumerate(ways):
            if v:
                for k in range(2, n-s+1):
                    nxt[s+k] += v * comb(s+k, k)
        ways = nxt
    return ways[n]

def count_poly(period,n):
    total = 0
    for (a,b),coef in poly[period].items():
        if a+2*b>n:
            continue
        total += coef * (factorial(n)//factorial(n-a))*at_least_two(n-a,b)
    return total

def formula_4(n):
    return ((n*n+7*n+16)*4**n//8 - (n*n+5*n+8)*2**n
          - n*(n-1)*(n-2)*(n-3) + 4*n*(n-1)+8)

# Exact coefficient verification of the expanded exponential identity is
# certified by the 19 coefficient pairs above, rather than by sampled n.
for n in range(2,13):
    b4 = count_poly(4,n)
    b18 = count_poly(18,n)
    b3 = count_poly(3,n)
    assert b3+b4+b18 == 9**n
    assert b18 == (144 if n==3 else 0)
    if n>=4:
        assert b4 == formula_4(n)
    else:
        assert b4 == 0

# Exact period-entry maxima at low n are tested over all feasible capped types.
for n, wanted in [(2,3),(3,9),(4,9)]:
    feasible = []
    for s in STATES:
        ones, big = s.count(1),s.count(2)
        if ones+2*big<=n and (big>0 or ones==n):
            feasible.append(cap_tau[s])
    assert max(feasible)==wanted, (n,max(feasible))
witness = (0,0,2,1,0,0,0,0,2)
assert cap_tau[witness]==13
assert dynamics(witness)[1]==3

print('EXACT_SUPPORT_CERTIFICATE_OK')
print('capped_states=19683 recurrent_capped_cycles=33 max_transient=13')
print('abstract_classifications=',dict(sorted(all_by_period.items())))
print('max_transient_n=2:3, n=3:9, n=4:9, n>=5:13')
print('period_18_egf=24*z^3 period_4_polynomial_terms=19')
for n in range(2,10):
    print('n=%d B3=%d B4=%d B18=%d'%(n,count_poly(3,n),count_poly(4,n),count_poly(18,n)))
