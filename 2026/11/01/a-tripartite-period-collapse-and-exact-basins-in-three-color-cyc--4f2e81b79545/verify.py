"""Independent finite-state certificate for three-color cyclic cellular automata.
Only standard Python 3 is required. Prints CCA_TRIPARTITE_CERTIFICATE_OK.
"""
from itertools import product
from collections import Counter


def update_blocks(blocks):
    out=[]
    for i,block in enumerate(blocks):
        neighbor=0
        for j,other in enumerate(blocks):
            if i!=j:
                for color in other:
                    neighbor|=1<<color
        out.append(tuple((color+1)%3 if ((neighbor>>((color+1)%3))&1) else color for color in block))
    return tuple(out)


def masks(blocks):
    out=[]
    for block in blocks:
        bits=0
        for color in block:bits|=1<<color
        out.append(bits)
    return tuple(out)


def representative(supports):
    return tuple(tuple(color for color in range(3) if mask&(1<<color)) for mask in supports)


def temporal_class(blocks):
    seen={}; t=0; x=blocks
    while x not in seen:
        assert t<=8,('long trajectory',blocks)
        seen[x]=t
        x=update_blocks(x);t+=1
    return seen[x],t-seen[x]

# Exhaust ALL capped multiplicity patterns of the seven initial shore supports:
# 0, 1 or at least 2 shores of that support. Two representatives preserve
# every inter-shore existence test, and each present color is represented.
patterns=0
for multiplicities in product(range(3),repeat=7):
    if sum(multiplicities)<3:
        continue
    supports=tuple(mask+1 for mask,count in enumerate(multiplicities) for _ in range(count))
    x=representative(supports)
    images=[x]
    for _ in range(5):images.append(update_blocks(images[-1]))
    assert images[2]==images[5],('F5 identity',multiplicities)
    patterns+=1
assert patterns==2151

# Classify each of the 343 tripartite nonempty support triples, including
# the special support-fixed class (7,7,7) that rotates all vertex colors.
class_by_support={}
counts=Counter()
for support in product(range(1,8),repeat=3):
    cl=temporal_class(representative(support))
    assert cl[0] in (0,1,2) and cl[1] in (1,3)
    class_by_support[support]=cl
    counts[cl]+=1
assert sum(counts.values())==343
assert counts=={(0,1):3,(0,3):121,(1,1):66,(1,3):90,(2,1):27,(2,3):36},counts

def closed_sync(a,b,c):
    return 3*(2**(a+b+c)+3**a+3**b+3**c-2**(a+1)-2**(b+1)-2**(c+1)+2)

def support_weight(mask,n):
    size=mask.bit_count()
    return {1:1,2:2**n-2,3:3**n-3*2**n+3}[size]

def closed_periodic(a,b,c):
    u=[2**k-2 for k in (a,b,c)]
    r=[3**k-3*2**k+3 for k in (a,b,c)]
    sum_pairs=lambda z:sum(z[i]*z[j] for i in range(3) for j in range(i+1,3))
    return (r[0]*r[1]*r[2]+6+6*sum(u)+9*sum_pairs(u)
            +15*u[0]*u[1]*u[2]
            +3*sum(r[i]*u[j] for i in range(3) for j in range(3) if i!=j)
            +3*sum_pairs(r)
            +6*sum(r[i]*u[(i+1)%3]*u[(i+2)%3] for i in range(3))
            +3*sum(u[i]*r[(i+1)%3]*r[(i+2)%3] for i in range(3)))

def symbolic_counts(sizes):
    result=Counter()
    for support,cl in class_by_support.items():
        weight=1
        for mask,n in zip(support,sizes):weight*=support_weight(mask,n)
        result[cl]+=weight
    return result

checks=0
for sizes in product(range(1,5),repeat=3):
    co=symbolic_counts(sizes)
    assert sum(co.values())==3**sum(sizes)
    assert co[(0,1)]==3
    assert co[(0,1)]+co[(1,1)]+co[(2,1)]==closed_sync(*sizes),sizes
    assert co[(0,3)]==closed_periodic(*sizes),sizes
    assert co[(0,3)]%3==0, sizes
    checks+=1
assert checks==64

# Independent vertex-level exhaustive simulation, WITHOUT support reduction.
# Includes each of 27+81+243+729+2187+6561+19683 microstates depending on sizes.
brute_states=0
for sizes in ((1,1,1),(1,1,2),(1,2,2),(2,2,2),(2,2,3),(3,3,3),(1,3,3)):
    actual=Counter()
    for state in product(range(3),repeat=sum(sizes)):
        blocks=[];idx=0
        for n in sizes:
            blocks.append(tuple(state[idx:idx+n]));idx+=n
        actual[temporal_class(tuple(blocks))]+=1
        brute_states+=1
    assert actual==symbolic_counts(sizes),(sizes,actual,symbolic_counts(sizes))
assert brute_states==sum(3**sum(k) for k in ((1,1,1),(1,1,2),(1,2,2),(2,2,2),(2,2,3),(3,3,3),(1,3,3)))

# Tight two-step entry witness (initial shore supports 1,1,3 on K_{1,1,2}).
assert temporal_class(((0,),(0,),(0,1)))==(2,1)

print('capped_patterns=',patterns)
print('tripartite_support_patterns=',sum(counts.values()))
print('support_class_counts=',sorted(counts.items()))
print('symbolic_shore_size_cases=',checks)
print('independent_microstates=',brute_states)
print('CCA_TRIPARTITE_CERTIFICATE_OK')
