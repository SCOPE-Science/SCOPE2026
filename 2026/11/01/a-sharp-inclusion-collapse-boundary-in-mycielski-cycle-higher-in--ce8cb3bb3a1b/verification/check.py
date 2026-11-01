#!/usr/bin/env python3
"""Exact finite verification for the first Mycielski-cycle higher-independence transition.

Uses only the Python standard library. Vertices are numbered v_i=i, u_i=n+i,
w=2*n. A subset is an integer bitmask with those bit positions.
"""

from collections import Counter, defaultdict, deque
from math import gcd


def graph(n):
    assert 3 <= n <= 6
    size = 2*n+1
    adjacency = [0]*size
    def edge(a,b):
        assert a!=b
        adjacency[a] |= 1<<b
        adjacency[b] |= 1<<a
    for i in range(n):
        edge(i,(i+1)%n)
        edge(n+i,(i+1)%n)
        edge(n+i,(i-1)%n)
        edge(2*n,n+i)
    assert all((adjacency[i]>>j&1)==(adjacency[j]>>i&1)
               for i in range(size) for j in range(size))
    return size,adjacency


def face_by_degree(mask,adjacency,r):
    return all(not(mask>>i&1) or (adjacency[i]&mask).bit_count()<r
               for i in range(len(adjacency)))


def face_by_components(mask,adjacency,r):
    remaining=mask
    while remaining:
        seed=remaining & -remaining
        reached=0
        frontier=seed
        while frontier:
            reached |= frontier
            neighbors=0
            for i in range(len(adjacency)):
                if frontier>>i&1:
                    neighbors |= adjacency[i]
            frontier = neighbors & mask & ~reached
        if reached.bit_count()>r:
            return False
        remaining &= ~reached
    return True


def complexes(n):
    size,adj=graph(n)
    ordinary=set()
    extended=set()
    for mask in range(1<<size):
        first=face_by_degree(mask,adj,1)
        second=face_by_degree(mask,adj,2)
        assert first==face_by_components(mask,adj,1)
        assert second==face_by_components(mask,adj,2)
        assert not first or second
        if first:ordinary.add(mask)
        if second:extended.add(mask)
    return size,ordinary,extended


def toggle_matching(cells,size,order=None):
    rest=set(cells)
    pairs=[]
    for i in (range(size) if order is None else order):
        lows=sorted(m for m in rest if not(m>>i&1) and (m|(1<<i)) in rest)
        pairs.extend((m,m|(1<<i)) for m in lows)
        rest.difference_update(lows)
        rest.difference_update(m|(1<<i) for m in lows)
    assert 2*len(pairs)+len(rest)==len(cells)
    return pairs,rest


def acyclic_hasse(cells,pairs,size):
    mates={h:l for l,h in pairs}
    assert len(mates)==len(pairs)
    indegree={m:0 for m in cells}
    outgoing=defaultdict(list)
    incidences=0
    for high in cells:
        for i in range(size):
            if high>>i&1:
                low=high^(1<<i)
                if low not in cells:continue
                src,dst=(low,high) if mates.get(high)==low else (high,low)
                outgoing[src].append(dst)
                indegree[dst]+=1
                incidences+=1
    queue=deque(m for m in cells if indegree[m]==0)
    visited=0
    while queue:
        m=queue.popleft();visited+=1
        for other in outgoing[m]:
            indegree[other]-=1
            if indegree[other]==0:queue.append(other)
    assert visited==len(cells), "matching has a directed cycle"
    return incidences


def elementary_collapse(ordinary,extended,pairs):
    remaining=set(extended)
    untouched=set(range(len(pairs)))
    while untouched:
        choice=None
        for index in sorted(untouched):
            low,high=pairs[index]
            strict=[m for m in remaining if m!=low and (m&low)==low]
            if len(strict)==1 and strict[0]==high:
                choice=index
                break
        assert choice is not None, "not all matching pairs are elementary collapses"
        low,high=pairs[choice]
        assert low not in ordinary and high not in ordinary
        remaining.remove(low)
        remaining.remove(high)
        untouched.remove(choice)
    assert remaining==ordinary
    return len(pairs)


def face_boundary(mask,size,available):
    return {mask^(1<<i): (-1)**((mask&((1<<i)-1)).bit_count())
            for i in range(size)
            if (mask>>i&1) and ((mask^(1<<i)) in available)}


def check_boundary_squared(columns):
    for top,low_terms in columns.items():
        result=defaultdict(int)
        for mid,coefficient in low_terms.items():
            for lower,entry in columns.get(mid,{}).items():
                result[lower] += coefficient*entry
        assert all(v==0 for v in result.values()), (top,result)


def integer_morse_reduction(cells,pairs,size):
    # Each matched pivot is a unit. Elementary algebraic cancellation preserves
    # integral chain homotopy type, without any field or numerical rounding.
    columns={m:face_boundary(m,size,cells) for m in cells}
    check_boundary_squared(columns)
    remaining=set(cells)
    pivots=[]
    for low,high in pairs:
        assert low in remaining and high in remaining
        pivot=columns[high].get(low,0)
        assert abs(pivot)==1, (low,high,pivot)
        pivots.append(pivot)
        for other in sorted(remaining):
            if other==high or other.bit_count()!=high.bit_count():continue
            scalar=columns[other].get(low,0)
            if scalar:
                for face,entry in columns[high].items():
                    columns[other][face]=columns[other].get(face,0)-scalar*pivot*entry
                    if columns[other][face]==0:del columns[other][face]
        for other in remaining:
            if other!=high and other!=low and other.bit_count()==high.bit_count()+1:
                columns[other].pop(high,None)
        columns.pop(high)
        columns.pop(low,None)
        remaining.remove(low);remaining.remove(high)
    check_boundary_squared(columns)
    return remaining,columns,pivots


def rank_mod_two(rows):
    pivots={}
    for row in rows:
        while row:
            position=row.bit_length()-1
            if position in pivots:row ^= pivots[position]
            else:
                pivots[position]=row
                break
    return len(pivots)


def independent_relative_homology_mod_two(cells,size):
    by_dim=defaultdict(list)
    for m in cells:by_dim[m.bit_count()-1].append(m)
    dims=sorted(by_dim)
    ranks={}
    for d in dims:
        upper=sorted(by_dim[d])
        lower={m:j for j,m in enumerate(sorted(by_dim.get(d-1,[])))}
        cols=[]
        for mask in upper:
            value=0
            for i in range(size):
                if mask>>i&1:
                    child=mask^(1<<i)
                    if child in lower:value ^= 1<<lower[child]
            cols.append(value)
        ranks[d]=rank_mod_two(cols)
    betti={d:len(by_dim[d])-ranks[d]-ranks.get(d+1,0) for d in dims}
    return Counter({d:len(by_dim[d]) for d in dims}),ranks,betti


def main():
    sizes={}
    for n in (3,4,5,6):
        size,ordinary,extended=complexes(n)
        outside=extended-ordinary
        pairs,critical=toggle_matching(outside,size)
        incidences=acyclic_hasse(outside,pairs,size)
        sizes[n]=(len(ordinary),len(extended),len(outside),len(pairs),len(critical))
        if n<=5:
            assert critical==set()
            count=elementary_collapse(ordinary,extended,pairs)
            assert count=={3:12,4:28,5:105}[n]
        if n==5:
            ordinary_pairs,crit=toggle_matching(ordinary,size,list(range(size-1,-1,-1)))
            acyclic_hasse(ordinary,ordinary_pairs,size)
            assert len(crit)==1 and next(iter(crit)).bit_count()==3
            assert len(ordinary_pairs)==51
        if n==6:
            assert len(critical)==10
            assert Counter(m.bit_count()-1 for m in critical)==Counter({3:7,4:2,5:1})
            reduced,columns,pivots=integer_morse_reduction(outside,pairs,size)
            assert reduced==critical and len(pivots)==301
            crit3=sorted(m for m in critical if m.bit_count()==4)
            crit4=sorted(m for m in critical if m.bit_count()==5)
            crit5=sorted(m for m in critical if m.bit_count()==6)
            assert crit3==[154,308,360,801,1539,2092,3078]
            assert crit4==[936,2664] and crit5==[3016]
            v1=[columns[crit4[0]].get(c,0) for c in crit3]
            v2=[columns[crit4[1]].get(c,0) for c in crit3]
            w=[columns[crit5[0]].get(c,0) for c in crit4]
            assert v1==v2==[0,0,1,1,0,-1,0]
            assert w==[1,-1]
            assert gcd(*v1)==1
            dims,ranks,betti=independent_relative_homology_mod_two(outside,size)
            assert dict(sorted(dims.items()))=={1:24,2:126,3:231,4:171,5:54,6:6}
            assert {d:ranks[d] for d in sorted(ranks)}=={1:0,2:24,3:102,4:123,5:48,6:6}
            assert {d:betti[d] for d in sorted(betti)}=={1:0,2:0,3:6,4:0,5:0,6:0}
            print('n=6 integral Morse differential d4:',v1,v2)
            print('n=6 integral Morse differential d5:',w)
            print('n=6 relative homology: H_3 = Z^6; other degrees zero')
            print('n=6 independent mod-2 ranks:',ranks)
        print('n=',n,'ordinary,total,outside,pairs,unmatched=',sizes[n],
              'relative incidences=',incidences)
    assert sizes=={3:(18,42,24,12,0),4:(47,103,56,28,0),
                   5:(103,313,210,105,0),6:(254,866,612,301,10)}
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
