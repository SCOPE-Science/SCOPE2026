#!/usr/bin/env python3
from itertools import product, combinations
from math import comb

N = 6
R = 2
WORDS = [''.join(p) for p in product('01', repeat=N)]

def derivative(x):
    return tuple((ord(x[i])-48) ^ (ord(x[i+1])-48) for i in range(len(x)-1))

def reconstruct(first, d):
    bits=[int(first)]
    for z in d:
        bits.append(bits[-1] ^ z)
    return ''.join(str(b) for b in bits)

def repeat_once(x):
    return {x[:i+1] + x[i] + x[i+1:] for i in range(len(x))}

def descendants(x, t):
    s={x}
    for _ in range(t):
        u=set()
        for y in s:
            u.update(repeat_once(y))
        s=u
    return s

def insert_zero(d, j):
    return d[:j] + (0,) + d[j:]

def bins(d):
    out=[]
    z=0
    for bit in d:
        if bit==0:
            z += 1
        else:
            out.append(z)
            z=0
    out.append(z)
    return tuple(out)

def l1(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))

def compatible_direct(x,y,t=2):
    return descendants(x,t).isdisjoint(descendants(y,t))

def max_subsets(vs):
    good={}
    for a,b in combinations(vs,2):
        good[(a,b)] = compatible_direct(a,b,R)
    best=[]
    for k in range(1,len(vs)+1):
        cur=[]
        for ss in combinations(vs,k):
            if all(good[(a,b)] for a,b in combinations(ss,2)):
                cur.append(ss)
        if not cur:
            break
        best=cur
    return best

# The first bit plus derivative is a bijection, and one repetition becomes one zero insertion.
for x in WORDS:
    d=derivative(x)
    assert reconstruct(x[0],d)==x
    direct={(y[0],derivative(y)) for y in repeat_once(x)}
    via={(x[0],insert_zero(d,j)) for j in range(len(d)+1)}
    assert direct==via

# Exact-two disjointness implies exact-one disjointness here; check it on every pair.
pair_checks=0
for x,y in combinations(WORDS,2):
    pair_checks += 1
    if compatible_direct(x,y,2):
        assert compatible_direct(x,y,1)

# Verify the bin-vector criterion against direct descendant balls on every same-sector pair.
for first in '01':
    for w in range(6):
        layer=[x for x in WORDS if x[0]==first and sum(derivative(x))==w]
        for x,y in combinations(layer,2):
            bx,by=bins(derivative(x)),bins(derivative(y))
            assert (compatible_direct(x,y,2) == (l1(bx,by)>=6))

# Exhaustively enumerate all maximizing subsets inside each layer.
expected_opt=[1,2,3,1,1,1]
expected_counts=[1,3,1,10,5,1]
all_layer_max={}
for first in '01':
    opts=[]; counts=[]
    for w in range(6):
        layer=[x for x in WORDS if x[0]==first and sum(derivative(x))==w]
        ms=max_subsets(layer)
        opts.append(len(ms[0]))
        counts.append(len(ms))
        all_layer_max[(first,w)] = ms
    assert opts==expected_opt
    assert counts==expected_counts

# Check the structural descriptions of the only nontrivial layers.
for first in '01':
    # Weight one: derivative has one 1, and exactly three pairs have one-positions separated by at least three.
    m1=all_layer_max[(first,1)]
    pospairs=[]
    for ss in m1:
        ps=sorted(derivative(x).index(1) for x in ss)
        assert ps[1]-ps[0]>=3
        pospairs.append(tuple(ps))
    assert set(pospairs)=={(0,3),(0,4),(1,4)}
    # Weight two: unique maximum corresponds to zero-bin vectors 3e_i.
    m2=all_layer_max[(first,2)]
    assert len(m2)==1 and len(m2[0])==3
    assert set(bins(derivative(x)) for x in m2[0])=={(3,0,0),(0,3,0),(0,0,3)}

# Construct all 150 sector maxima and check direct correction and coverage.
sector_codes={}
for first in '01':
    choices=[all_layer_max[(first,w)] for w in range(6)]
    codes=[]
    for pick in product(*choices):
        code=tuple(sorted(x for block in pick for x in block))
        assert len(code)==9
        for x,y in combinations(code,2):
            assert compatible_direct(x,y,2)
            assert compatible_direct(x,y,1)
        covered=set().union(*(descendants(x,2) for x in code))
        assert len(covered)==71
        codes.append(code)
    assert len(codes)==150 and len(set(codes))==150
    sector_codes[first]=codes

# The first bit is invariant under repetition, so the two sectors combine independently.
global_max=sum(expected_opt)*2
labeled_maxima=len(sector_codes['0'])*len(sector_codes['1'])
assert global_max==18
assert labeled_maxima==22500

# Direct descendant-ball sizes depend only on derivative weight and match weak compositions of two zeros.
for x in WORDS:
    w=sum(derivative(x))
    assert len(descendants(x,2))==comb(w+2,2)

coverage=71*2
assert coverage==142 and 2**8==256
print('VERIFY_OK words=64 pair_checks=2016 layer_optima=1,2,3,1,1,1 layer_counts=1,3,1,10,5,1 sector_max=9 sector_maxima=150 global_max=18 labeled_maxima=22500 coverage=142/256')
