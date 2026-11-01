#!/usr/bin/env python3
"""Exact 5-state inhibitory dynamics on complete bipartite graphs.
Run: python3 fca5_bipartite_verifier.py
Only Python standard library is needed.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, lcm

Q=5; BLINK=2


def advance(mask, opposite):
    sees_blink=(opposite&(1<<BLINK))!=0
    result=0
    for c in range(Q):
        if mask&(1<<c):
            new_c=c if (sees_blink and c>BLINK) else (c+1)%Q
            result|=1<<new_c
    return result

states=list(product(range(1,1<<Q), repeat=2))
next_state={(s,t):(advance(s,t),advance(t,s)) for s,t in states}
assert len(states)==31**2 and len(next_state)==len(states)

# Enumerate the entire support functional digraph, not a sample.
cycles=[]; visited=set()
for state in states:
    if state in visited: continue
    seen_here={}; path=[]; z=state
    while z not in visited and z not in seen_here:
        seen_here[z]=len(path);path.append(z);z=next_state[z]
    if z in seen_here:
        cycles.append(tuple(path[seen_here[z]:]))
    visited.update(path)
assert visited==set(states)


def permutation_orders(cycle):
    start=cycle[0]
    result=[]
    for shore in (0,1):
        labels=[c for c in range(Q) if start[shore]&(1<<c)]
        after={c:c for c in labels}
        z=start
        for _ in cycle:
            other_blink=bool(z[1-shore]&(1<<BLINK))
            after={c:(d if other_blink and d>BLINK else (d+1)%Q) for c,d in after.items()}
            z=next_state[z]
        assert z==start and set(after.values())==set(labels)
        found=set(); lengths=[]
        for c in labels:
            if c in found:continue
            j=c;length=0
            while j not in found:
                found.add(j);j=after[j];length+=1
            assert j==c
            lengths.append(length)
        assert len(found)==len(labels)
        result.append(lcm(*lengths))
    return tuple(result)

support_cycle_period={}
cycle_info=[]
for cyc in cycles:
    mono=permutation_orders(cyc)
    p=len(cyc)*lcm(*mono)
    k,l=tuple(x.bit_count() for x in cyc[0])
    assert all(x.bit_count()==k and y.bit_count()==l for x,y in cyc)
    cycle_info.append((p,len(cyc),lcm(*mono),k,l))
    for s in cyc:support_cycle_period[s]=p
assert len(cycles)==16 and len(support_cycle_period)==49
assert Counter(len(c) for c in cycles)=={1:6,2:1,3:4,5:1,6:4}
assert Counter(p for p,_,_,_,_ in cycle_info)=={5:7,6:7,18:2}

# All 961 support states have a unique terminal cycle and exact first entry.
entry_depth={};eventual_period={}
for state in states:
    z=state; distance=0; local=set()
    while z not in support_cycle_period:
        assert z not in local
        local.add(z);z=next_state[z];distance+=1
    entry_depth[state]=distance
    eventual_period[state]=support_cycle_period[z]
assert max(entry_depth.values())==25
assert entry_depth[1,31]==25
assert entry_depth[31,31]==8 and eventual_period[31,31]==5
assert set(eventual_period.values())=={5,6,18}

A=Counter((k,l,eventual_period[(s,t)])
          for s,t in states
          for k,l in [(s.bit_count(),t.bit_count())])
assert sum(v for (k,l,p),v in A.items() if p==18)==6
assert all(entry_depth[s]==0 for s in states if eventual_period[s]==18)

@lru_cache(None)
def onto(n,k):
    return sum((-1)**j*comb(k,j)*(k-j)**n for j in range(k+1))


def orbit_count(a,b,p):
    out=0
    for pi,macro,ord_,k,l in cycle_info:
        if pi==p:
            u=onto(a,k)*onto(b,l)
            assert u%ord_==0
            out+=u//ord_
    return out


def formulas(a,b):
    u=lambda k,n:onto(n,k)
    return {
        5:1+(2**a*u(5,b)+2**b*u(5,a))//5,
        6:u(3,a)*u(3,b)//3+3*u(2,a)*u(2,b)+u(2,a)*u(3,b)+u(3,a)*u(2,b),
        18:(u(3,a)*u(4,b)+u(4,a)*u(3,b))//6,
    }

basin6=[[A[k,l,6] for l in range(1,6)] for k in range(1,6)]
assert basin6 == [
 [0,0,0,0,0],
 [0,30,28,5,0],
 [0,28,20,12,1],
 [0,5,12,3,1],
 [0,0,1,1,0],
]
assert [(k,l,A[k,l,18]) for k in range(1,6) for l in range(1,6) if A[k,l,18]]==[(3,4,3),(4,3,3)]

for a,b in product(range(1,9),repeat=2):
    values=formulas(a,b)
    for p in (5,6,18):
        assert orbit_count(a,b,p)==values[p],(a,b,p)
        basin=sum(A[k,l,p]*onto(a,k)*onto(b,l) for k in range(1,6) for l in range(1,6))
        if p==18:assert basin==18*values[p]
    total=sum(A[k,l,p]*onto(a,k)*onto(b,l)
              for k in range(1,6) for l in range(1,6) for p in (5,6,18))
    assert total==5**(a+b)

# Independent microscopic dynamics checks: state tuples rather than supports.
def F(x,a):
    left=x[:a]; right=x[a:]
    lb=BLINK in left; rb=BLINK in right
    return tuple((v if rb and v>BLINK else (v+1)%Q) for v in left)+tuple((v if lb and v>BLINK else (v+1)%Q) for v in right)

cases=[(1,1),(1,5),(2,2),(2,3),(3,4)]
micros=0
for a,b in cases:
    microcounts=Counter(); maxd=0
    for initial in product(range(Q),repeat=a+b):
        micros+=1
        # Derive p and depth using genuine microscopic dynamics, not support orbits.
        visit={};x=initial;step=0
        while x not in visit:
            visit[x]=step;x=F(x,a);step+=1
            assert step<100
        d=visit[x];p=step-d
        microcounts[p]+=1
        maxd=max(maxd,d)
        init_support=(sum(1<<v for v in set(initial[:a])),sum(1<<v for v in set(initial[a:])))
        assert p==eventual_period[init_support]
        assert d==entry_depth[init_support]
    assert set(microcounts)<={5,6,18}
    for p in (5,6,18):
        basin=sum(A[k,l,p]*onto(a,k)*onto(b,l) for k in range(1,6) for l in range(1,6))
        assert microcounts[p]==basin
    assert sum(microcounts.values())==Q**(a+b)
    if (a,b)==(1,5):assert maxd==25
    print('micro',a,b, 'states',Q**(a+b), 'period_basin',dict(sorted(microcounts.items())),'maxdepth',maxd)

print('support_states',len(states),'support_cycles',len(cycles),'support_periodic_states',len(support_cycle_period))
print('macro_cycle_lengths',dict(sorted(Counter(len(c) for c in cycles).items())))
print('micro_cycle_counts',dict(sorted(Counter(p for p,_,_,_,_ in cycle_info).items())))
print('maxdepth',max(entry_depth.values()),'witness',(1,31),'full_support_depth',entry_depth[31,31])
print('basin6_coefficients',basin6)
print('period18_basin_has_no_transients',True)
print('microscopic_states_tested',micros)
print('formula_pairs_tested',8*8)
print('FCA5_BIPARTITE_EXACT_VERIFY_OK')
