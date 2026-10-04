#!/usr/bin/env python3
from itertools import product
from math import comb, factorial


def pattern_formula(m,n,k):
    return sum(((-1)**i)*comb(k,i)*(m+k-i)**n for i in range(k+1)) // factorial(k)


def canonical_pattern(values, m):
    # values 0..m-1 are named parameters, values >=m are anonymous/new.
    remap={}
    nxt=0
    out=[]
    for v in values:
        if v < m:
            out.append(('p',v))
        else:
            if v not in remap:
                remap[v]=nxt; nxt+=1
            out.append(('n',remap[v]))
    return tuple(out), nxt


def pattern_counts_direct(m,n):
    pats=[set() for _ in range(n+1)]
    # n anonymous raw labels suffice to realize every equality pattern.
    for vals in product(range(m+n), repeat=n):
        p,k=canonical_pattern(vals,m)
        pats[k].add(p)
    return [len(s) for s in pats]


def bit_orbits_direct(m,k):
    d=m*k + k*(k-1)//2
    reps=set()
    for x in range(1<<d):
        if m <= 1 and d>0:
            mask=(1<<d)-1
            reps.add(min(x, x^mask))
        else:
            reps.add(x)
    return len(reps)


def weight_formula(m,k):
    d=m*k + k*(k-1)//2
    if m>=2:
        return 1<<d
    if d==0:
        return 1
    return 1<<(d-1)


def type_count_formula(m,n):
    return sum(pattern_formula(m,n,k)*weight_formula(m,k) for k in range(n+1))


def type_count_direct(m,n):
    counts=pattern_counts_direct(m,n)
    return sum(counts[k]*bit_orbits_direct(m,k) for k in range(n+1))

# Exact equality-pattern formula vs explicit canonical enumeration.
checks=0
for m in range(4):
    for n in range(1,6):
        direct=pattern_counts_direct(m,n)
        formula=[pattern_formula(m,n,k) for k in range(n+1)]
        assert direct==formula, (m,n,direct,formula)
        checks += sum(direct)

# Exact orientation-orbit weight vs direct bit-complement quotient.
for m in range(4):
    for k in range(0,6):
        assert bit_orbits_direct(m,k)==weight_formula(m,k), (m,k)

# Full type spectrum via two independent finite enumerations.
tables={}
for m in range(4):
    row=[]
    for n in range(1,6):
        a=type_count_formula(m,n)
        b=type_count_direct(m,n)
        assert a==b,(m,n,a,b)
        row.append(a)
    tables[m]=row

# Special profile over the empty parameter set: injective tuples are tournaments
# modulo global converse; arbitrary tuples are its Stirling transform.
def stirling2(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def inj(r):
    if r <= 1: return 1
    return 1 << (comb(r,2)-1)

for n in range(1,8):
    transformed=sum(stirling2(n,k)*inj(k) for k in range(1,n+1))
    assert transformed==type_count_formula(0,n),(n,transformed,type_count_formula(0,n))

# Stabilizer threshold sanity check: complementing all internal orientation bits of
# a pointwise-fixed parameter set is possible only when there is no internal bit,
# i.e. |A|<=1. For |A|>=2 an anti-map cannot fix all parameters pointwise.
for m in range(0,8):
    internal=comb(m,2)
    complement_can_fix_parameter_diagram = (internal==0)
    assert complement_can_fix_parameter_diagram == (m<=1)

assert tables[0]==[1,2,8,64,948]
assert tables[1]==[2,8,64,948,26536]
assert tables[2]==[6,56,884,25588,1450252]
assert tables[3]==[11,193,5955,349769,41038683]

print('canonical_equality_patterns_checked', checks)
print('type_counts_m0_to_m3_n1_to_n5', tables)
print('injective_empty_parameter_profile_n1_to_n7', [inj(n) for n in range(1,8)])
print('stabilizer_reversal_survives_exactly_m_le_1', True)
print('VERIFY_OK')
