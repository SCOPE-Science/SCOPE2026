#!/usr/bin/env python3
"""Exhaustive exact binary16 beta=3/2 Bernoulli graph verifier.

Only Python standard library and integer arithmetic. Rounds each multiplication
under IEEE 754 binary16 roundTiesToEven, then subtracts one in binary16 if
needed. All 15360 representable nonnegative inputs below 1 are included.
"""
from bisect import bisect_left
from collections import Counter, deque
from hashlib import sha256

U=1<<24
SIZE=0x3c00

def value_units(h):
    assert 0 <= h <= 0x4000
    e, f = h >> 10, h & 1023
    return f if not e else (1024+f) << (e-1)

values=[value_units(h) for h in range(0x4001)]
assert len(values)==len(set(values)) and values[SIZE]==U
bits_for_units={v:i for i,v in enumerate(values)}

def rounded_bits_twice(t2):
    # t2 is twice the exact nonnegative real in units of 2**-24.
    i=bisect_left(values,(t2+1)//2)
    if i == 0:return 0
    if i == len(values): return len(values)-1
    low,high=i-1,i
    dlow=t2-2*values[low]; dhigh=2*values[high]-t2
    if dlow<dhigh:return low
    if dhigh<dlow:return high
    return low if low%2==0 else high

def step(h):
    assert 0<=h<SIZE
    product=rounded_bits_twice(3*values[h])
    v=values[product]
    if v>=U:
        v-=U
        assert v in bits_for_units # subtraction is exactly representable
        product=bits_for_units[v]
    assert 0<=product<SIZE
    return product

edges=[step(i) for i in range(SIZE)]
assert all(0<=v<SIZE for v in edges)
# Exact independent graph decomposition: trim indegree-zero tails.
indeg=[0]*SIZE
for v in edges: indeg[v]+=1
q=deque(i for i in range(SIZE) if indeg[i]==0)
peel=[]
while q:
    u=q.popleft(); peel.append(u)
    v=edges[u]; indeg[v]-=1
    if indeg[v]==0:q.append(v)
cycle_ids=[-1]*SIZE
depths=[-1]*SIZE
cycles=[]
for root in range(SIZE):
    if indeg[root]==0 or cycle_ids[root]>=0:continue
    cid=len(cycles); c=[]; u=root
    while cycle_ids[u]<0:
        assert indeg[u]>0
        cycle_ids[u]=cid;depths[u]=0;c.append(u);u=edges[u]
    assert u==root
    cycles.append(tuple(c))
for u in reversed(peel):
    v=edges[u]
    assert cycle_ids[v]>=0 and depths[v]>=0
    cycle_ids[u]=cycle_ids[v]; depths[u]=depths[v]+1
assert all(i>=0 for i in cycle_ids) and all(i>=0 for i in depths)
records=sorted([(len(c),len([i for i in range(SIZE) if cycle_ids[i]==j]),min(c),max(depths[i] for i in range(SIZE) if cycle_ids[i]==j)) for j,c in enumerate(cycles)])
expected=sorted([(1,5705,0,155),(3,26,14012,15),(4,3138,13280,133),(24,2013,9472,77),(41,4478,10944,67)])
assert records==expected,(records,expected)
assert sum(record[1] for record in records)==SIZE
# A compact, platform-independent checksum of the entire transition function.
import struct
raw=b''.join(struct.pack('<H',e) for e in edges)
print('states',SIZE,'cycle_count',len(cycles),'periods',sorted(map(len,cycles)))
print('period_basin_minbit_maxdepth',records)
print('edge_sha256',sha256(raw).hexdigest())
print('global_max_entry_time',max(depths))
print('PASS: exhaustive exact integer-rounding finite graph certificate')
from fractions import Fraction
limit_mean=Fraction(0)
for j,c in enumerate(cycles):
    B=sum(1 for t in cycle_ids if t==j)
    limit_mean+=Fraction(B,SIZE*len(c))*sum((Fraction(values[h],U) for h in c),Fraction(0))
print('quantized_limit_mean',limit_mean,'decimal',float(limit_mean))
# Parry density: a_j=T^j(1), with beta=3/2.
a=Fraction(1); w=Fraction(1)
S1=Fraction(0); S2=Fraction(0)
for j in range(120):
    S1+=w*a
    S2+=w*a*a/Fraction(2)
    a=Fraction(3,2)*a
    a-=int(a)
    w*=Fraction(2,3)
tail=3*w
lo=S2/(S1+tail)
hi=(S2+tail/2)/S1
print('continuum_mean_interval',float(lo),float(hi),'width',float(hi-lo))
print('signed_mean_gap',float(limit_mean-hi),float(limit_mean-lo))
# Lebesgue-uniform real initial x in [0,1], round to nearest binary16,
# including endpoint 1.0 (which has a positive half Voronoi cell).
endpoint_target=bits_for_units[U//2]
endpoint_cid=cycle_ids[endpoint_target]
weights={}
for h in range(SIZE+1):
    left2=0 if h==0 else values[h-1]+values[h]
    right2=2*U if h==SIZE else values[h]+values[h+1]
    weights[h]=right2-left2
assert sum(weights.values())==2*U
basin_weights={j:sum(weights[h] for h in range(SIZE) if cycle_ids[h]==j)+(weights[SIZE] if j==endpoint_cid else 0) for j in range(len(cycles))}
weighted_mean=Fraction(0)
for j,c in enumerate(cycles):
    weighted_mean+=Fraction(basin_weights[j],2*U*len(c))*sum((Fraction(values[h],U) for h in c),Fraction(0))
print('Lebesgue_nearest_basins',(sorted((len(c),basin_weights[j]) for j,c in enumerate(cycles))))
print('Lebesgue_nearest_mean',weighted_mean,float(weighted_mean))
print('Lebesgue_nearest_gap',float(weighted_mean-hi),float(weighted_mean-lo))

# Required exact reference values and strict real-versus-rounded gap.
assert sha256(raw).hexdigest()=="5b2f33943cdf5fa52dafdaaa48c8b354e29542389d30954404fe1842cfe245e6"
assert limit_mean==Fraction(825722879,2751463424)
assert sorted((len(c),basin_weights[j]) for j,c in enumerate(cycles))==[(1,12777057),(3,68656),(4,7273607),(24,4398294),(41,9036818)]
assert weighted_mean==Fraction(13332128797227,45079976738816)
assert hi-lo<Fraction(104,10**23)
assert Fraction(103,1000)<lo-weighted_mean<=hi-weighted_mean<Fraction(104,1000)
print('PASS: exact weighted invariant Cesaro means and real-map gap bounds')
