"""Construct and test interval edge-colourings of bouquets of cycles.

Run: python verify.py
No third-party dependencies; exact integer checks only.
"""
from itertools import product
from collections import defaultdict
import random


def bouquet_coloring(lengths):
    assert lengths and all(length >= 3 for length in lengths)
    k = len(lengths)
    even = [i for i, length in enumerate(lengths) if length % 2 == 0]
    odd = [i for i, length in enumerate(lengths) if length % 2 == 1]
    r = len(even)
    s = len(odd)
    spoke_pairs = [None] * k
    for j, index in enumerate(even):
        spoke_pairs[index] = (2*j+1, 2*j+2)
    base = 2*r
    # At most one extra color at the hub; used by its pendant edge.
    odd_colors = list(range(base+1, 2*k+1+(s%2)))
    odds = [x for x in odd_colors if x % 2]
    evens = [x for x in odd_colors if x % 2 == 0]
    pairs = [(odds[j], odds[j+1]) for j in range(0,len(odds),2)]
    pairs += [(evens[j],evens[j+1]) for j in range(0,len(evens)-1,2)]
    assert len(pairs)==s
    for index,pair in zip(odd,pairs):spoke_pairs[index]=pair
    colored_edges = []
    next_vertex = 1
    for length,(a,b) in zip(lengths,spoke_pairs):
        vertices = [0]+list(range(next_vertex,next_vertex+length-1))
        next_vertex += length-1
        # one edge per pair of consecutive listed vertices, including final-to-root
        if (length % 2)==0:
            t = [a if j%2==0 else a+1 for j in range(length)]
        else:
            t = [a]+[a+1 if j%2 else a+2 for j in range(1,length)]
        assert t[-1]==b, (length,(a,b),t)
        for j in range(length):
            colored_edges.append((vertices[j],vertices[(j+1)%length],t[j]))
    if s%2:
        assert s%2==1
        # Last unused even color in odd-petal range.
        pendant_color=2*k
        colored_edges.append((0,next_vertex,pendant_color))
    return colored_edges, next_vertex + (s%2)


def check_one(lengths):
    edges,order = bouquet_coloring(lengths)
    assert len(edges)==sum(lengths)+(sum(x%2 for x in lengths)%2)
    at=defaultdict(set)
    degrees=defaultdict(int)
    simple=set()
    for u,v,c in edges:
        assert u!=v and 1<=c<=2*len(lengths)+(sum(x%2 for x in lengths)%2)
        assert tuple(sorted((u,v))) not in simple
        simple.add(tuple(sorted((u,v))))
        for w in (u,v):
            assert c not in at[w], ('improper',lengths,w,c)
            at[w].add(c)
            degrees[w]+=1
    assert len(at)==order
    assert len(at[0])==2*len(lengths)+(sum(x%2 for x in lengths)%2)
    for w,cols in at.items():
        assert len(cols)==degrees[w]
        assert max(cols)-min(cols)+1==len(cols),('noninterval',lengths,w,cols)
    all_colors=set(c for u,v,c in edges)
    assert all_colors == set(range(1,max(all_colors)+1))
    assert max(all_colors)==2*len(lengths)+(sum(x%2 for x in lengths)%2)


def main():
    total=0
    # Complete length-list census up to four petals, each length three to nine.
    for k in range(1,5):
        for lengths in product(range(3,10),repeat=k):
            check_one(lengths)
            total+=1
    rng=random.Random(790613)
    for _ in range(3000):
        k=rng.randrange(1,21)
        lengths=tuple(rng.randrange(3,100) for _ in range(k))
        check_one(lengths)
        total+=1
    print('CONSTRUCTIVE_CERTIFICATE_OK')
    print('instances=',total)
    print('complete_prefix_length_cases=',sum(7**k for k in range(1,5)))
    print('randomized_large_cases=3000 (fixed seed 790613)')
    print('covered_parity_classes=both')
    print('checks=proper, consecutive vertex spectra, consecutive global palette, matching hub degree')

if __name__=='__main__':main()
