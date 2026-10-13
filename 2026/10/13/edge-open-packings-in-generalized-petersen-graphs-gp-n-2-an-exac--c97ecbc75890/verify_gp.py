#!/usr/bin/env python3
"""Exact finite witness for a generalized-Petersen edge-packing formula.
Run with Python 3 standard library only: python3 verify_gp.py
"""
from functools import lru_cache
from itertools import product

# O_i=u_i u_{i+1}, S_i=u_i v_i, I_i=v_i v_{i+2}; mask bits O,S,I.
# Each tuple (a,b) in CONFLICT[d] disallows an edge of type a at column i
# together with an edge of type b at column i+d.  The table follows directly
# from inspecting third edges joining endpoints in the graph definition.
CONFLICT = (
    ((0, 2), (2, 0)),
    ((0, 2), (1, 0), (1, 1), (2, 0)),
    ((0, 0), (0, 1), (1, 1), (1, 2), (2, 0)),
    (),
    ((2, 1), (2, 2)),
)
CONFLICT = tuple(set(x) for x in CONFLICT)
POTENTIAL = (
17,14,12,3,15,6,17,10,12,3,16,10,10,17,7,13,2,7,4,17,
15,17,16,10,10,17,14,17,17,14,12,11,6,14,0,11,7,11,2,7,
0,14,11,17,14,12,3,15,6,17,7,13,2,17,15,17,14,17,17,17,
14,12,3,15,6,17,10,12,3,14,12,11,6,17,14,12,3,15,6,16,
12,9,3,10,0,16,10,7,7,4,0,7,4,16,12,7,14,9,0,0,
14,0,7,7,0,0,7,0,14,7,16,12,9,3,10,0,14,9,0,0)

# Explicit cyclic words.  Values 0..7 encode selected edge types.
BASE = {
 5:(0,1,3,0,0),
 6:(0,2,4,0,2,4),
 7:(4,2,0,1,0,4,4),
 8:(0,0,1,0,4,4,6,4),
 9:(2,4,0,6,4,0,2,0,1),
10:(2,4,0,6,0,0,3,0,0,1),
11:(2,4,0,6,4,0,6,0,0,0,1),
12:(2,4,0,6,4,0,2,0,1,2,0,1),
13:(2,4,0,6,4,0,6,0,0,3,0,0,1),
14:(2,4,0,6,4,0,6,0,0,4,0,2,0,1),
15:(2,4,0,6,4,0,6,0,0,6,0,0,2,0,1),
16:(2,4,0,6,4,0,6,0,0,3,0,0,1,2,0,1),
17:(2,4,0,6,4,0,6,0,0,3,0,0,1,3,0,0,1),
}

def okay(a,b,d):
    return all(not ((a>>i)&1 and (b>>j)&1) for i,j in CONFLICT[d])

def finite_automaton():
    masks=tuple(a for a in range(8) if okay(a,a,0))
    states=tuple(s for s in product(masks,repeat=4)
                 if all(okay(s[i],s[j],j-i)
                        for i in range(4) for j in range(i+1,4)))
    ids={s:i for i,s in enumerate(states)}
    arcs=[]
    for i,s in enumerate(states):
        for a in masks:
            if all(okay(s[3-j],a,j+1) for j in range(4)):
                arcs.append((i,ids[s[1:]+(a,)],a.bit_count()))
    return masks,states,arcs

def graph_edges(n):
    assert n>=5
    return ([(i,(i+1)%n) for i in range(n)]
            +[(i,n+i) for i in range(n)]
            +[(n+i,n+(i+2)%n) for i in range(n)])

def direct_conflicts(n):
    edges=graph_edges(n)
    assert len(set(tuple(sorted(x)) for x in edges))==3*n
    inc=[[] for _ in range(2*n)]
    for k,(u,v) in enumerate(edges):inc[u].append(k);inc[v].append(k)
    found=set()
    for k,(u,v) in enumerate(edges):
        for i in inc[u]:
            if i==k:continue
            for j in inc[v]:
                if j!=k and i!=j:found.add(tuple(sorted((i,j))))
    return edges,sorted(found)

def by_table(n,a,b):
    t1,i=divmod(a,n);t2,j=divmod(b,n)
    d=(j-i)%n;e=(i-j)%n
    return (d<=4 and (t1,t2) in CONFLICT[d]) or (e<=4 and (t2,t1) in CONFLICT[e])

def valid_word(word,table_only=False):
    n=len(word)
    if any(not 0<=a<8 for a in word):return False
    edges,c=direct_conflicts(n)
    selected={t*n+i for i,mask in enumerate(word) for t in range(3) if mask>>t&1}
    return all(not (a in selected and b in selected) for a,b in c)

def word_for(n):
    if n<=17:return BASE[n]
    r=(n-9)%9
    p=BASE[9+r];q=BASE[9]
    # Starting after the shared state p[0:4] = q[0:4], each rotated
    # word returns the four-column finite-automaton state to itself.
    return (p[4:]+p[:4])+(q[4:]+q[:4])*((n-len(p))//9)

def small_exact(n):
    edges,conflicts=direct_conflicts(n);size=len(edges)
    bad=[0]*size
    for i,j in conflicts:bad[i]|=1<<j;bad[j]|=1<<i
    good=[((1<<size)-1)^(bad[i]|(1<<i)) for i in range(size)]
    @lru_cache(None)
    def maximum(mask):
        if not mask:return 0
        b=mask&-mask;i=b.bit_length()-1
        return max(maximum(mask^b),1+maximum(mask&good[i]))
    value=maximum((1<<size)-1)
    return value,maximum.cache_info().currsize

def main():
    masks,states,arcs=finite_automaton()
    assert masks==(0,1,2,3,4,6)
    assert len(states)==120 and len(arcs)==291 and len(POTENTIAL)==120
    assert min(POTENTIAL)==0 and max(POTENTIAL)==17
    assert all(POTENTIAL[i]>=POTENTIAL[j]+9*w-7 for i,j,w in arcs)
    print('upper-bound certificate: 120 states, 291 arcs, all 9w-7 potential inequalities valid')
    # Check that the table matches the original graph definition, not only itself.
    for n in (9,10,11,12,13,17,24,31):
        _,c=direct_conflicts(n)
        c=set(c)
        assert all(by_table(n,a,b)==((a,b) in c)
                   for a in range(3*n) for b in range(a+1,3*n))
    print('conflict-table vs direct graph: agreement at 9,10,11,12,13,17,24,31')
    for n in range(5,9):
        value,states_count=small_exact(n)
        assert value==(7*n)//9
        print('small case',n,'exact optimum',value,'memoized subsets',states_count)
    assert all(p[:4]==BASE[9][:4] for n,p in BASE.items() if n>=9)
    index={state:i for i,state in enumerate(states)}
    arcs_set=set(arcs)
    for n in range(9,18):
        p=BASE[n]
        state=p[:4]
        for mask in p[4:]+p[:4]:
            next_state=state[1:]+(mask,)
            assert (index[state],index[next_state],mask.bit_count()) in arcs_set
            state=next_state
        assert state==BASE[9][:4]
    print('based cycles: all nine words n=9..17 return to the common four-column state')
    for n,p in sorted(BASE.items()):
        assert len(p)==n and sum(x.bit_count() for x in p)==7*n//9
        assert valid_word(p)
    print('base construction certificates: n=5..17 all direct-edge valid')
    for n in list(range(18,181)) + [271,360,721]:
        p=word_for(n)
        assert len(p)==n and sum(x.bit_count() for x in p)==7*n//9
        assert valid_word(p)
    print('pumping construction: direct-edge valid for n=18..180,271,360,721')
    print('THEOREM VERIFIED (finite certificates plus general local-automaton and pumping argument)')

if __name__=='__main__':main()
