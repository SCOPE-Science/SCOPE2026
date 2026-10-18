"""Exact, finite tests of three-round refinement on two-point-marked Kneser graphs.
Run with Python 3.9 or newer. No external dependencies.
"""
from itertools import combinations
from collections import Counter, defaultdict

def one_case(n, k, b):
    A = frozenset(range(k))
    B = frozenset(list(range(b)) + list(range(k, k + (k-b))))
    vertices = [frozenset(x) for x in combinations(range(n), k)]
    regions = (A & B, A-B, B-A, frozenset(range(n))-(A|B))
    profiles = [tuple(len(x & R) for R in regions) for x in vertices]
    neighbors = [[j for j,y in enumerate(vertices) if x.isdisjoint(y)] for x in vertices]
    colors = [1 if x == A else (2 if x == B else 0) for x in vertices]
    round_counts = [len(set(colors))]
    for _ in range(3):
        sig = [(colors[i], tuple(sorted(Counter(colors[j] for j in neighbors[i]).items()))) for i in range(len(vertices))]
        ids = {z: index for index,z in enumerate(sorted(set(sig)))}
        colors = [ids[z] for z in sig]
        round_counts.append(len(ids))
    cp, pc = defaultdict(set), defaultdict(set)
    for color, profile in zip(colors, profiles):
        cp[color].add(profile)
        pc[profile].add(color)
    assert all(len(x) == 1 for x in cp.values()), (n,k,b, 'orbit merged')
    assert all(len(x) == 1 for x in pc.values()), (n,k,b, 'orbit split')
    assert len(cp) == len(pc)
    return len(vertices), round_counts

def main():
    count=0
    seen=0
    max_classes=0
    for k in range(2,5):
        for n in range(3*k-1, min(3*k+5, 14)):
            for b in range(k):
                size, rounds=one_case(n,k,b)
                count+=1;seen+=size;max_classes=max(max_classes,rounds[-1])
    assert one_case(8,3,1)[1] == [3,6,13,14]
    print('PASS: cases=',count,'total vertex-instances=',seen,'maximum final orbit classes=',max_classes)
    print('SHARPNESS KG(8,3) anchor intersection=1: round classes 3,6,13,14')

if __name__ == '__main__':
    main()
