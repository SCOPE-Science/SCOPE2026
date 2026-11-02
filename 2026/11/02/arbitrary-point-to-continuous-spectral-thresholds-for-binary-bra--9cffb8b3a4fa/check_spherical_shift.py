"""Finite, reproducible checks for the two-valued branching shift theorem.

Usage: python check_spherical_shift.py
The theorem and infinite convergence arguments are analytic; these tests check
finite combinatorial identities and selected operator equations only.
"""
from fractions import Fraction
from math import floor, log2, ceil, sqrt
from itertools import product


def count_profile(degrees):
    counts = [1]
    for d in degrees:
        assert d in (1, 2)
        counts.append(counts[-1] * d)
    return counts


def build_tree(degrees):
    levels = [[0]]
    children = {}
    k = 1
    for d in degrees:
        new = []
        for v in levels[-1]:
            children[v] = list(range(k, k+d))
            new.extend(children[v])
            k += d
        levels.append(new)
    for v in levels[-1]:
        children[v] = []
    return levels, children


def check_prefix_eigenvector(degrees, eig):
    levels, children = build_tree(degrees)
    P = count_profile(degrees)
    entries = {v: eig**depth / P[depth]
               for depth, level in enumerate(levels) for v in level}
    assert all(len(level) == P[i] for i, level in enumerate(levels))
    for level in levels[:-1]:
        for v in level:
            assert sum((entries[c] for c in children[v]), Fraction(0)) == eig*entries[v]
    # Layer square mass of the formal radial vector is exactly |eig|^(2n)/P_n.
    for j, level in enumerate(levels):
        assert sum((entries[v]**2 for v in level), Fraction(0)) == eig**(2*j) / P[j]


def check_finite_wavelet(degrees, start, m, eig):
    assert all(d == 2 for d in degrees[start:start+m+1])
    levels, children = build_tree(degrees)
    parent = levels[start][0]
    kids = children[parent]
    # h_0 = (delta_first - delta_second)/sqrt(2), encoded by squared-normalization 2.
    h = {kids[0]: Fraction(1), kids[1]: Fraction(-1)}
    waves = [h]
    for j in range(m):
        h = {c: coeff for v, coeff in h.items() for c in children[v]}
        waves.append(h)
    # Unnormalized h_j has square norm 2^(j+1), and S h_j = 2 h_(j-1).
    for j, wave in enumerate(waves):
        assert sum(t*t for t in wave.values()) == 2**(j+1)
        if j:
            for p, coeff in waves[j-1].items():
                assert sum(wave.get(c, 0) for c in children[p]) == 2*coeff
    # For the normalized h_j, the ratio of consecutive norms is sqrt(2).
    # Directly test the telescoping approximate eigenvector S(sum eig^j / 2^j h_j).
    vec = {}
    for j, wave in enumerate(waves):
        fac = eig**j / 2**j
        for v, t in wave.items():
            vec[v] = vec.get(v, Fraction(0)) + fac*t
    Sv = {}
    for v, kids in children.items():
        q = sum((vec.get(c, 0) for c in kids), Fraction(0))
        if q:
            Sv[v] = q
    residual = {v: Sv.get(v, Fraction(0))-eig*vec.get(v, Fraction(0))
                for v in set(Sv)|set(vec)}
    expected = {v: -eig*(eig**m / 2**m)*w for v,w in waves[m].items()}
    assert {v:q for v,q in residual.items() if q} == {v:q for v,q in expected.items() if q}


def balanced_windows(theta, a, n0, windows, N):
    # This finite model uses a deliberately large n0 so the baseline increments
    # form a binary word. A finite initial prefix is chosen with the correct count.
    def B(n):
        return floor(theta*n + a*log2(n+2))
    assert 0 <= B(n0) <= n0
    arr = [1]*B(n0) + [0]*(n0-B(n0))
    arr += [B(j+1)-B(j) for j in range(n0, N)]
    assert all(q in (0,1) for q in arr)
    for start,k in windows:
        L = ceil(3*k/min(theta, 1-theta))
        assert n0 <= start and start+L <= N
        word = arr[start:start+L]
        assert sum(word)>=k and L-sum(word)>=k
        reordered = [0]*k+[1]*k+[0]*(L-sum(word)-k)+[1]*(sum(word)-k)
        assert len(reordered) == L and sum(word) == sum(reordered)
        arr[start:start+L] = reordered
        assert arr[start:start+k] == [0]*k
        assert arr[start+k:start+2*k] == [1]*k
    running = 0
    diffs = []
    for i, bit in enumerate(arr):
        running += bit
        if i+1 >= n0:
            diffs.append(abs(running-B(i+1)))
    assert max(diffs) <= max(ceil(3*k/min(theta, 1-theta)) for _,k in windows)
    for start,k in windows:
        L = ceil(3*k/min(theta, 1-theta))
        assert sum(arr[:start]) == B(start)
        assert sum(arr[:start+L]) == B(start+L)
    return arr


def run():
    checks = 0
    for n in range(1,9):
        for w in product((1,2), repeat=n):
            for lam in (Fraction(0),Fraction(1,3),Fraction(-2,5)):
                check_prefix_eigenvector(w,lam)
                checks+=1
            for j in range(n):
                for m in range(n-j):
                    if all(q==2 for q in w[j:j+m+1]):
                        check_finite_wavelet(w,j,m,Fraction(1,2))
                        checks+=1
    for theta in (0.3,0.41,0.68):
        for a in (0,2):
            balanced_windows(theta,a,512,[(1024,2),(3000,3),(5500,4)],8000)
            checks+=1
    print(f'PASS: {checks} finite operator/combinatorial test cases')

if __name__ == '__main__':
    run()
