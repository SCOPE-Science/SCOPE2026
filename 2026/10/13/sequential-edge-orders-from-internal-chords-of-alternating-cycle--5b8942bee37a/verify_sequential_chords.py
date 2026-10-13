#!/usr/bin/env python3
"""Direct finite checks of a constructive distinguishing edge order.
Uses only Python 3's standard library. These checks support, but do not prove,
the general graph-theoretic theorem.
"""
from itertools import combinations
from random import Random
from collections import Counter


def canonical(u, v):
    assert u != v
    return (u, v) if u < v else (v, u)


def build_order(cycles, matching):
    """Cycles are lists of vertices in natural alternating B/H order.
    Matching consists of unordered vertex pairs; each cycle must have a chord.
    Return an edge list of (u,v,color) in global order.
    """
    which = {v: i for i, cyc in enumerate(cycles) for v in cyc}
    assert len(which) == sum(map(len, cycles))
    matches = [canonical(*x) for x in matching]
    assert len(matches) == len(set(matches))
    assert len({v for e in matches for v in e}) == len(which)
    internal = [[] for _ in cycles]
    external = [[] for _ in cycles]
    for a, b in matches:
        i, j = which[a], which[b]
        if i == j:
            internal[i].append((a,b))
        else:
            external[min(i,j)].append((a,b))
    assert all(internal)
    ans=[]
    for z, cyc in enumerate(cycles):
        L=len(cyc)
        assert L>=4 and L%2==0
        root=internal[z][0][0]
        p=cyc.index(root)
        # Alternation: original (cyc[2k],cyc[2k+1]) is B.
        if p%2==0:
            seq=cyc[p:]+cyc[:p]
        else:
            seq=[cyc[(p-i)%L] for i in range(L)]
        assert seq[0]==root
        e=[]
        for j in range(L):
            a,b=seq[j],seq[(j+1)%L]
            c='B' if j%2==0 else 'H'
            e.append((*canonical(a,b),c))
        gaps=[[] for _ in range(L+1)]
        index={v:i for i,v in enumerate(seq)}
        for a,b in internal[z]:
            i,j=sorted((index[a], index[b]))
            assert (j-i) not in (1,L-1), (seq,a,b)
            gap=1 if i==0 else i+1
            assert gap<j
            gaps[gap].append((*canonical(a,b),'R'))
        for j in range(L):
            ans.extend(gaps[j])
            ans.append(e[j])
        ans.extend(gaps[L])
        ans.extend((*x,'R') for x in sorted(external[z]))
    return ans


def direct_check(cycles, matching):
    n=sum(map(len, cycles))
    ans=build_order(cycles,matching)
    assert len(ans)==3*n//2
    assert len(set(canonical(a,b) for a,b,_ in ans))==len(ans)
    inc={v: [] for cyc in cycles for v in cyc}
    for a,b,c in ans:
        inc[a].append(c)
        inc[b].append(c)
    assert all(sorted(s)==['B','H','R'] for s in inc.values())
    bad=[(a,b,inc[a],inc[b]) for a,b,_ in ans if inc[a]==inc[b]]
    assert not bad, (cycles, matching, bad)
    return True


def perfect_matchings(vertices):
    if not vertices:
        yield []
        return
    a=vertices[0]
    for k in range(1,len(vertices)):
        b=vertices[k]
        rest=vertices[1:k]+vertices[k+1:]
        for further in perfect_matchings(rest):
            yield [(a,b)]+further


def adjacent_cycles(cycles):
    es=set()
    for cyc in cycles:
        for k in range(len(cyc)):
            es.add(canonical(cyc[k],cyc[(k+1)%len(cyc)]))
    return es


def test_single():
    totals={}
    nonbip={}
    for n in (4,6,8,10,12):
        cycles=[list(range(n))]
        cyc_edges=adjacent_cycles(cycles)
        count=odd=0
        for m in perfect_matchings(list(range(n))):
            if any(canonical(*e) in cyc_edges for e in m):
                continue
            direct_check(cycles,m)
            count+=1
            # B/H cycle plus chord forms an odd cycle if a chord joins equal parity.
            if any((a-b)%2==0 for a,b in m):
                odd+=1
        totals[n]=count
        nonbip[n]=odd
    return totals,nonbip


def test_multicycle():
    rand=Random(172903)
    sizes_profiles=((4,4),(4,6),(6,6),(4,8),(4,4,4),(4,6,8),(6,6,6),(4,4,6,8))
    tally={}
    for sizes in sizes_profiles:
        cycles=[]; s=0
        for L in sizes:
            cycles.append(list(range(s,s+L)));s+=L
        v=list(range(s)); forbidden=adjacent_cycles(cycles)
        count=0
        for _ in range(8000):
            rand.shuffle(v)
            pairs=[canonical(v[i],v[i+1]) for i in range(0,s,2)]
            if any(e in forbidden for e in pairs):
                continue
            which={x:i for i,cyc in enumerate(cycles) for x in cyc}
            if any(not any(which[a]==which[b]==j for a,b in pairs) for j in range(len(cycles))):
                continue
            direct_check(cycles,pairs)
            count+=1
            if count==150:
                break
        if count==0:
            raise AssertionError((sizes,'no test fixture'))
        tally['x'.join(map(str,sizes))]=count
    return tally


def test_mobius():
    for k in range(1,26):
        n=4*k
        cyc=[list(range(n))]
        m=[(i,i+n//2) for i in range(n//2)]
        direct_check(cyc,m)


if __name__=='__main__':
    total,odd=test_single()
    print('ONE_CYCLE_MATCHING_COUNTS', sorted(total.items()))
    print('NONBIPARTITE_ONE_CYCLE_COUNTS', sorted(odd.items()))
    multi=test_multicycle()
    print('MULTI_CYCLE_PROFILE_COUNTS', sorted(multi.items()))
    test_mobius()
    print('MOBIUS_LADDER_CASES',25)
    print('VERIFICATION_OK')
