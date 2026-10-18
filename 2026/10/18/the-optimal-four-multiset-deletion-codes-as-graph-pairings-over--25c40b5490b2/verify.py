#!/usr/bin/env python3
"""Reproducible finite checks for single-deletion codes on size-four multisets."""
from itertools import combinations, combinations_with_replacement
from collections import Counter
from math import comb

def packing(q):
    if q < 4:
        return []
    if q == 4 or q == 5:
        return [tuple(range(4))]
    if q == 6:
        return [tuple(i for i in range(6) if i not in pair)
                for pair in [(0, 1), (2, 3), (4, 5)]]
    if q == 7:
        lines = {tuple(sorted((a - 1, b - 1, (a ^ b) - 1)))
                 for a in range(1, 8) for b in range(a + 1, 8)}
        assert len(lines) == 7
        return [tuple(i for i in range(7) if i not in line)
                for line in sorted(lines)]
    if q == 8:
        return sorted({tuple(sorted((a, b, c, a ^ b ^ c)))
                       for a, b, c in combinations(range(8), 3)})
    raise ValueError('Small verification implemented for q<=8')

def deletions(word):
    return {word[:i] + word[i+1:] for i in range(len(word))}

def main():
    sizes = {2:3, 3:6, 4:11, 5:16, 6:24, 7:35, 8:50}
    packing_sizes = {2:0, 3:0, 4:1, 5:1, 6:3, 7:7, 8:14}
    for q in range(2, 9):
        blocks = packing(q)
        assert len(blocks) == packing_sizes[q]
        triples = [u for block in blocks for u in combinations(block, 3)]
        assert len(triples) == len(set(triples))
        code = [(i,)*4 for i in range(q)]
        code += [(i,i,j,j) for i,j in combinations(range(q),2)]
        code += blocks
        assert len(code) == sizes[q] == q+comb(q,2)+len(blocks)
        shadows = [deletions(w) for w in code]
        seen = set()
        for shadow in shadows:
            assert not (shadow & seen), (q, shadow & seen)
            seen.update(shadow)
        for w in combinations_with_replacement(range(q), 4):
            pat = tuple(sorted(Counter(w).values(), reverse=True))
            expected = {(4,): (1,0,0), (3,1):(1,1,0),
                        (2,2):(0,2,0), (2,1,1):(0,2,1),
                        (1,1,1,1):(0,0,4)}[pat]
            sh = deletions(w)
            types = [tuple(sorted(Counter(y).values(),reverse=True)) for y in sh]
            got=(types.count((3,)),types.count((2,1)),types.count((1,1,1)))
            assert expected==got, (q,w,got,expected)
        if q == 6:
            assert 3*4 <= comb(6,3)
            assert all(len(set(b)&set(c))<=2 for b,c in combinations(blocks,2))
        if q == 7:
            uncovered=set(combinations(range(7),3))-set(triples)
            assert len(uncovered)==7
            assert all(sum(set(pair)<=set(t) for t in uncovered)==1
                       for pair in combinations(range(7),2))
        if q == 8:
            assert len(triples)==comb(8,3)
        print('q=%d: %d blocks, %d codewords, %d distinct received words' %
              (q,len(blocks),len(code),len(seen)))
    # Noncanonical six-symbol optimum supplied by a six-cycle's pairings.
    q = 6
    cycle = (0,2,4,1,3,5)
    B = packing(q)
    covered = {frozenset(t) for block in B for t in combinations(block,3)}
    edges = {frozenset((cycle[i],cycle[(i+1)%6])) for i in range(6)}
    assert len(edges)==6
    wedges = []
    assigned = []
    for i in range(6):
        center=cycle[i]
        left=cycle[(i-1)%6]
        right=cycle[(i+1)%6]
        triple=frozenset((left,center,right))
        assert triple not in covered
        assigned.append(triple)
        wedges.append(tuple(sorted((center,center,left,right))))
    assert len(set(assigned)) == 6
    # Each vertex has degree two and all its incident missing-pair arcs
    # are covered exactly once by its centered mixed word.
    for v in range(6):
        neighbors={u for e in edges for u in e if v in e and u!=v}
        assert len(neighbors)==2
        w=next(w for w in wedges if w.count(v)==2)
        assert set(w)-{v} == neighbors
    noncanonical = [(i,)*4 for i in range(q)]
    noncanonical += [(i,i,j,j) for i,j in combinations(range(q),2)
                     if frozenset((i,j)) not in edges]
    noncanonical += wedges + B
    assert len(noncanonical)==24 and len(set(noncanonical))==24
    outs=set()
    for w in noncanonical:
        sh=deletions(w)
        assert not (sh & outs),(w,sh & outs)
        outs |= sh
    assert len(outs)==54
    assert len([w for w in noncanonical if sorted(Counter(w).values())==[1,1,2]])==6
    print('q=6 noncanonical cycle construction: 24 words, 54 distinct outputs')
    print('VERIFY_OK')

if __name__=='__main__':main()
