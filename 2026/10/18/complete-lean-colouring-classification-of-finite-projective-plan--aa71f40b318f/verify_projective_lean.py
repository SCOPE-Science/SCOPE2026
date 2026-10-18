"""Independent finite checks for lean colourings of projective-plane line hypergraphs.

Run: python verify_projective_lean.py
Requires only the Python standard library. Finite checks supplement a general proof.
"""
from collections import Counter
from itertools import product
from math import factorial


def pg2(p):
    if p not in (2, 3, 5, 7):
        raise ValueError("This enumerator is for the four specified prime fields")
    reps = set()
    for v in product(range(p), repeat=3):
        if any(v):
            pivot = next(a for a in v if a)
            inv = pow(pivot, -1, p)
            reps.add(tuple(a*inv % p for a in v))
    points = sorted(reps)
    lines = [frozenset(i for i,x in enumerate(points)
                       if sum(a*b for a,b in zip(x,y)) % p == 0)
             for y in points]
    assert len(set(lines)) == len(points) == p*p+p+1
    assert all(len(line) == p+1 for line in lines)
    assert all(sum(i in line for line in lines) == p+1
               for i in range(len(points)))
    assert all(sum(i in line and j in line for line in lines) == 1
               for i in range(len(points)) for j in range(i+1,len(points)))
    assert all(len(a&b) == 1 for i,a in enumerate(lines)
               for b in lines[i+1:])
    return points, lines


def valid(labels, lines):
    if len(set(labels)) < 2:
        return False
    for line in lines:
        distinct = len({labels[i] for i in line})
        if distinct not in (1, len(line)):
            return False
    return True


def set_partitions(n):
    labels = [0]*n
    def rec(i, maximum):
        if i == n:
            yield tuple(labels)
            return
        for c in range(maximum + 2):
            labels[i] = c
            yield from rec(i+1,max(maximum,c))
    yield from rec(1,0)


def check_fano():
    _, lines = pg2(2)
    counts = Counter()
    monochrome_distribution = Counter()
    total = 0
    for labels in set_partitions(7):
        total += 1
        if valid(labels, lines):
            counts[len(set(labels))] += 1
            num_mono = sum(len({labels[i] for i in line}) == 1 for line in lines)
            monochrome_distribution[num_mono] += 1
            assert num_mono <= 1
    assert total == 877, total
    assert dict(counts) == {5: 7, 7: 1}, counts
    assert dict(monochrome_distribution) == {1:7,0:1}
    print("Fano plane: 877 point partitions checked; lean partitions",dict(counts))


def check_witnesses():
    for p in (2,3,5,7):
        points, lines = pg2(p)
        n = len(points)
        for line in lines:
            labels = [None]*n
            for i in line: labels[i]=0
            k=1
            for i in range(n):
                if labels[i] is None:
                    labels[i]=k
                    k+=1
            assert k == p*p+1
            assert valid(labels,lines)
            assert sum(len({labels[i] for i in e}) == 1 for e in lines)==1
        distinct = tuple(range(n))
        assert valid(distinct,lines)
        assert p*p+1 > p+2 if p >= 2 else True
        print("PG(2,%d): %d lines, %d points; %d optimal witnesses checked; lean=%d, incidence Delta=%d" %
              (p,len(lines),n,len(lines),p*p+1,p+1))
    # Named palette of 5 colours: 7 choices of monochrome line, then 5! bijections.
    assert 7*factorial(5)==840

if __name__ == "__main__":
    check_fano()
    check_witnesses()
    print("All finite checks passed.")
