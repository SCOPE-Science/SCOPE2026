"""Reproduce the exact integer metric distortion for the four-block map.
Unit: one edge in the m-point geodesic circle, or 2*pi/m.
All assertions are finite spot-checks; the proof in RESULT.md is uniform in k.
"""
from itertools import combinations


def round_distance(i, j, m):
    d = abs(i-j) % m
    return min(d, m-d)


def block_map(k):
    sizes = (k+1, k, k+1, k)
    labels = []
    for label, size in enumerate(sizes):
        labels.extend([label] * size)
    assert len(labels) == 4*k+2
    return labels


def test(k):
    m = 4*k+2
    f = block_map(k)
    # Use doubled units to keep the target 4-gon distances integral.
    errors = [abs(2*round_distance(i,j,m) - m//2*round_distance(f[i],f[j],4))
              for i in range(m) for j in range(m)]
    # m/4=(2k+1)/2 steps; 2*(m/4)=2k+1=m//2.
    assert max(errors) == 2*k, (k, max(errors))
    # A fiber contains k+1 points, with intrafiber diameter k steps.
    assert round_distance(0,k,m)==k
    return k,m,max(errors)

if __name__ == '__main__':
    for k in range(1,101):
        test(k)
    for k in range(1,5):
        m=4*k+2
        for subset in combinations(range(m),k+1):
            assert max(round_distance(i,j,m) for i in subset for j in subset)>=k
        print(f'packing brute check k={k}, m={m}, subsets checked')
    print('All 100 block-map instances satisfy maximum distortion exactly k steps.')
