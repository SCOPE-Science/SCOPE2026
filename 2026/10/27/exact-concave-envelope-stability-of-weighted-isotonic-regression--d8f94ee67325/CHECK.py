"""Exact-rational checks for the weighted isotonic projection variation modulus.

Run: python CHECK.py
Requires only the Python standard library. These finite tests support, but
cannot replace, the theorem's proof for arbitrary lengths and real weights.
"""
from fractions import Fraction as F
from itertools import product
import random


def weighted_pav(y, a):
    """Nondecreasing weighted least-squares projection, exact rationals."""
    blocks = []
    for i, (v, mass) in enumerate(zip(y, a)):
        blocks.append([i, i, mass, mass*v])
        while len(blocks) >= 2 and blocks[-2][3]*blocks[-1][2] >= blocks[-1][3]*blocks[-2][2]:
            right = blocks.pop()
            left = blocks[-1]
            left[1] = right[1]
            left[2] += right[2]
            left[3] += right[3]
    out = [F(0) for _ in y]
    for first, last, mass, sm in blocks:
        for i in range(first, last + 1):
            out[i] = sm/mass
    return out


def var(y, q):
    return sum((wt*abs(y[i+1]-y[i]) for i, wt in enumerate(q)), F(0))


def chord_modulus(a, q):
    n = len(a)
    masses = [F(0)]
    for x in a:
        masses.append(masses[-1] + x)
    w = [F(0)] + list(q) + [F(0)]
    best = F(1)
    witness = None
    for k in range(1, n):
        for left in range(k):
            for right in range(k+1, n+1):
                value = (w[left]*(masses[right]-masses[k]) +
                         w[right]*(masses[k]-masses[left])) / ((masses[right]-masses[left])*w[k])
                if value > best:
                    best = value
                    witness = (left, k, right)
    return best, witness



def linear_time_hull_modulus(a, q):
    """Upper hull of mass-coordinate weights; O(n) arithmetic operations."""
    n = len(a)
    A = [F(0)]
    for mass in a:
        A.append(A[-1]+mass)
    w = [F(0)]+list(q)+[F(0)]
    hull = []
    for c in range(n+1):
        while len(hull) >= 2:
            left, mid = hull[-2], hull[-1]
            # Remove middle point when chord slopes fail concavity.
            if (w[mid]-w[left])*(A[c]-A[mid]) <= (w[c]-w[mid])*(A[mid]-A[left]):
                hull.pop()
            else:
                break
        hull.append(c)
    best = F(1)
    witness = None
    seg = 0
    for k in range(1,n):
        while seg+1 < len(hull)-1 and hull[seg+1] < k:
            seg += 1
        L, R = hull[seg], hull[seg+1]
        height = (w[L]*(A[R]-A[k])+w[R]*(A[k]-A[L]))/(A[R]-A[L])
        ratio = height/w[k]
        if ratio > best:
            best, witness = ratio, (L,k,R)
    return best, witness, hull

def partitions(n):
    for mask in range(1 << (n-1)):
        starts = [0] + [i+1 for i in range(n-1) if (mask >> i) & 1]
        ends = starts[1:] + [n]
        yield list(zip(starts, ends))


def partition_norm(a, q, blocks):
    n = len(a)
    answer = F(0)
    for k in range(1, n):
        step = [F(i >= k) for i in range(n)]
        proj = step[:]
        for lo, hi in blocks:
            value = sum((a[i]*step[i] for i in range(lo,hi)), F(0))/sum(a[lo:hi], F(0))
            proj[lo:hi] = [value]*(hi-lo)
        answer = max(answer, var(proj,q)/q[k-1])
    return answer


def attaining_pair(a, q, triple):
    n = len(a)
    L, k, R = triple  # boundary indices are 0..n; step begins at coordinate k (0-based)
    x = [F(0)]*n
    for i in range(n):
        if i < L:
            x[i] = F(-100*n+i)
        elif i < R:
            x[i] = F(R-i)
        else:
            x[i] = F(100*n+i)
    eps = F(1,1000)
    y = [x[i]+eps*F(i>=k) for i in range(n)]
    Px = weighted_pav(x, a)
    Py = weighted_pav(y, a)
    return var([Py[i]-Px[i] for i in range(n)],q)/var([y[i]-x[i] for i in range(n)],q)


def main():
    rand = random.Random(73421)
    exhaustive_partitions = 0
    rational_inequalities = 0
    attaining_checks = 0
    examples = 0
    for n in range(2,10):
        for _ in range(90):
            a = [F(rand.randint(1,10)) for _ in range(n)]
            q = [F(rand.randint(1,11)) for _ in range(n-1)]
            K, triple = chord_modulus(a,q)
            hull_K, hull_witness, hull = linear_time_hull_modulus(a,q)
            assert hull_K == K, (n,a,q,K,hull_K,hull)
            actual = max(partition_norm(a,q,b) for b in partitions(n))
            assert actual == K, (n,a,q,K,actual)
            exhaustive_partitions += 1 << (n-1)
            if triple is not None:
                got = attaining_pair(a,q,triple)
                assert got == K, (n,a,q,triple,K,got)
                attaining_checks += 1
            for _ in range(24):
                x = [F(rand.randint(-20,20)) for _ in range(n)]
                y = [F(rand.randint(-20,20)) for _ in range(n)]
                v = var([x[i]-y[i] for i in range(n)],q)
                if v:
                    lhs = var([u-v for u,v in zip(weighted_pav(x,a),weighted_pav(y,a))],q)
                    assert lhs <= K*v, (n,a,q,K,x,y,lhs,v)
                    rational_inequalities += 1
            examples += 1
    # Explicit mass-dependent concavity test: q_i = A_i (A_n - A_i).
    for n in range(2,12):
        a = [F(rand.randint(1,30)) for _ in range(n)]
        A = [F(0)]
        for val in a: A.append(A[-1]+val)
        q = [A[i]*(A[-1]-A[i]) for i in range(1,n)]
        assert chord_modulus(a,q)[0] == 1
    # A single small interior weight causes arbitrarily large modulus.
    assert chord_modulus([F(1)]*3,[F(1), F(1,1000)])[0] == 500
    print('PASS exact-rational checker')
    print('partition norms checked:',exhaustive_partitions)
    print('global two-input inequalities checked:',rational_inequalities)
    print('attaining-pair checks:',attaining_checks)
    print('parameter profiles:',examples)
    print('additional structural boundary checks: 11')
    print('linear-time concave-majorant comparisons:', examples)

if __name__ == '__main__':
    main()
