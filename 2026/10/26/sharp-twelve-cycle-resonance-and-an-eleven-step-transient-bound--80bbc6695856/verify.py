"""Finite certificates for threshold-two three-state excitation on K_{a,b,c}.

The quotient is exact for every triple of positive part sizes because the
neighbour-excitation condition depends only on state-one counts capped at 2.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial

BASE = 3
PARTS = 3
QCOUNT = 3 ** 9
POW = [3 ** k for k in range(9)]


def decode(q):
    return tuple(tuple((q // POW[3*i+j]) % 3 for j in range(3)) for i in range(3))


def encode(rows):
    return sum(rows[i][j] * POW[3*i+j] for i in range(3) for j in range(3))


def quotient(q):
    rows = decode(q)
    total = sum(row[1] for row in rows)
    active = tuple(total - rows[i][1] >= 2 for i in range(3))
    result = []
    for i, (z, e, f) in enumerate(rows):
        result.append((min(2, f + (0 if active[i] else z)),
                       min(2, z) if active[i] else 0, e))
    return encode(result), active


def next_tag(s, trigger):
    return 2 if s == 1 else (0 if s == 2 else int(trigger))


# This certifies the finite transition graph without a numerical simulation
# of any particular graph size.  Every original vertex follows one of the
# tagged trajectories in the product graph.
qnext = [0] * QCOUNT
act = [None] * QCOUNT
for q in range(QCOUNT):
    qnext[q], act[q] = quotient(q)
assert len(qnext) == 19683

STATES = QCOUNT * 9
next_full = [0] * STATES
for q in range(QCOUNT):
    for i in range(3):
        for s in range(3):
            next_full[9*q + 3*i + s] = 9*qnext[q] + 3*i + next_tag(s, act[q][i])

one = list(range(STATES))
twelve = list(range(STATES))
for _ in range(12):
    twelve = [next_full[z] for z in twelve]
remaining_at_ten = None
for t in range(12):
    mismatches = sum(x != y for x, y in zip(one, twelve))
    if t == 10:
        remaining_at_ten = mismatches
        assert mismatches == 108
    if t == 11:
        assert mismatches == 0, 'universal F^23=F^11 certificate failed'
    else:
        assert mismatches > 0
        one = [next_full[z] for z in one]
        twelve = [next_full[z] for z in twelve]

# For an initial capped profile, every occupied (part,state) tagged vertex
# must return to its own state to have a periodic labelled configuration.
checks = {}
for period in (1, 2, 3, 4, 6, 12):
    qpath = list(range(QCOUNT))
    tags = [list(range(3))*QCOUNT for _ in range(3)]
    for _ in range(period):
        old = qpath
        for i in range(3):
            tags[i] = [next_tag(tags[i][3*q+s], act[old[q]][i])
                       for q in range(QCOUNT) for s in range(3)]
        qpath = [qnext[q] for q in old]
    checks[period] = (qpath, tags)


def is_periodic_profile(q, period):
    qpath, tags = checks[period]
    if qpath[q] != q:
        return False
    rows = decode(q)
    return all(tags[i][3*q+s] == s for i in range(3)
               for s in range(3) if rows[i][s] > 0)

assert all(not is_periodic_profile(q, 2) or is_periodic_profile(q, 1)
           for q in range(QCOUNT))
assert all(not is_periodic_profile(q, 6) or is_periodic_profile(q, 3)
           for q in range(QCOUNT))

prime_twelve = {q for q in range(QCOUNT)
                if is_periodic_profile(q, 12)
                and not is_periodic_profile(q, 3)
                and not is_periodic_profile(q, 4)}
expected = set()
for small in range(3):
    two_large = [i for i in range(3) if i != small]
    for swap in (False, True):
        big_0, big_1 = two_large[::-1] if swap else two_large
        for mask in range(1, 8):
            rows = [[0, 0, 0] for _ in range(3)]
            rows[big_0] = [2, 0, 2]
            rows[big_1] = [2, 2, 0]
            rows[small] = [(mask >> j) & 1 for j in range(3)]
            expected.add(encode(rows))
assert len(prime_twelve) == 42
assert prime_twelve == expected, 'exact resonance-profile classification failed'


def B2(n):
    return sum(comb(n,j) for j in range(2,n-1)) if n >= 4 else 0


def falling3(n):
    return factorial(3)//factorial(3-n) if 1 <= n <= 3 else 0


def twelve_states(sizes):
    return sum(2 * falling3(sizes[i]) * B2(sizes[(i+1)%3]) * B2(sizes[(i+2)%3])
               for i in range(3))


def step_direct(x, sizes):
    positions=[]
    offset=0
    for n in sizes:
        positions.append(list(range(offset,offset+n)))
        offset+=n
    cur=[(x//(3**j))%3 for j in range(offset)]
    excitation=[sum(cur[j]==1 for j in part) for part in positions]
    tot=sum(excitation)
    out=0
    for i,part in enumerate(positions):
        threshold=tot-excitation[i]>=2
        for j in part:
            z=cur[j]
            upd=2 if z==1 else (0 if z==2 else int(threshold))
            out+=upd*3**j
    return out


def direct_cycle_census(sizes):
    count=3**sum(sizes)
    follow=[step_direct(x,sizes) for x in range(count)]
    visited=bytearray(count)
    prim=Counter()
    for start in range(count):
        if visited[start]:
            continue
        sequence=[]
        local={}
        current=start
        while current not in local and not visited[current]:
            local[current]=len(sequence)
            sequence.append(current)
            current=follow[current]
        if current in local:
            period=len(sequence)-local[current]
            prim[period]+=period
        for x in sequence:
            visited[x]=1
    return prim, follow


def profile_fixes(sizes, period):
    # Exact labelled multinomial census from capped occupation profiles.
    allrows=[]
    for n in sizes:
        choices=[]
        for z in range(n+1):
            for e in range(n-z+1):
                f=n-z-e
                choices.append(((min(2,z),min(2,e),min(2,f)),
                                comb(n,z)*comb(n-z,e)))
        allrows.append(choices)
    result=0
    for row0,w0 in allrows[0]:
        for row1,w1 in allrows[1]:
            for row2,w2 in allrows[2]:
                q=encode((row0,row1,row2))
                if is_periodic_profile(q,period):
                    result+=w0*w1*w2
    return result

# Fully independent vertex-level tests; quotient is not used to generate
# these direct transitions or their cycle structure.
examples = [(2,2,1), (2,2,2), (3,3,3), (2,4,2),
            (4,4,1), (4,4,2), (4,4,3), (4,4,4), (5,5,1)]
observed=[]
for sizes in examples:
    census, follow=direct_cycle_census(sizes)
    assert set(census) <= {1,3,4,12}, (sizes,census)
    assert census[12] == twelve_states(sizes), (sizes,census,twelve_states(sizes))
    for period in (1,3,4,12):
        count=sum(value for d,value in census.items() if period % d==0)
        assert count == profile_fixes(sizes,period), (sizes,period,count)
    observed.append((sizes,dict(sorted(census.items()))))

# Constructive proof that eleven steps are sometimes necessary.
sharp_sizes = (5,2,3)
sharp = [0,1,1,2,2] + [0,2] + [0,1,1]
x0=sum(s*3**i for i,s in enumerate(sharp))
z=x0
states=[z]
for _ in range(23):
    z=step_direct(z,sharp_sizes)
    states.append(z)
assert states[10] != states[22]
assert states[11] == states[23]
assert all(step_direct(states[t],sharp_sizes)==states[t+1] for t in range(23))

print('CERTIFICATE_OK')
print('capped_profiles=19683 tagged_states=177147')
print('universal_identity=F^23_equals_F^11; unmatched_at_10=',remaining_at_ten)
print('period_2_implies_period_1=True; period_6_implies_period_3=True')
print('primitive_12_profiles=42; exact_shape_match=True')
print('sharp_transient_witness=K_(5,2,3)',sharp,'time_10_not_time_22=True')
for sizes,census in observed:
    print('direct',sizes,'states',3**sum(sizes),'periodic_states',census,'R12',twelve_states(sizes))
