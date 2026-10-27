"""Independent finite tests for Rule 184 iterated spatial images.

Only standard-library Python 3 is required. All finite checks are exhaustive
in the domains stated below; infinite assertions require the written proof.
"""
from itertools import product
from math import log, sqrt


def local(a, b, c):
    return (184 >> (4*a + 2*b + c)) & 1


def edge(a, b):
    return 1 if a == b == 1 else (-1 if a == b == 0 else 0)


def rule_on_ring(x):
    n = len(x)
    return tuple(local(x[(i-1) % n], x[i], x[(i+1) % n]) for i in range(n))


def allowed_ring(x, t):
    n = len(x)
    for k in range(t):
        forbidden = (1, 1) + (0, 1)*k + (0, 0)
        for i in range(n):
            if all(x[(i+j) % n] == a for j, a in enumerate(forbidden)):
                return False
    return True


def reverse_one_step(y):
    n = len(y)
    marked = {}
    for i in range(n):
        if y[i] == y[(i+1) % n]:
            j = (i+1 if y[i] else i-1) % n
            if j in marked and marked[j] != y[i]:
                return None
            marked[j] = y[i]
    if not marked:
        return tuple(1-a for a in y)
    for first in (0, 1):
        x = [first]
        for i in range(n-1):
            x.append(x[-1] if i in marked else 1-x[-1])
        if (all((x[i] == x[(i+1) % n]) == (i in marked)
                for i in range(n)) and
                all(x[i] == marked[i] for i in marked)):
            return tuple(x)
    return None


def iterated_local_map(t):
    width = 2*t+1
    ans = []
    for value in range(1 << width):
        bits = [(value >> (width-i-1)) & 1 for i in range(width)]
        for _ in range(t):
            bits = [local(bits[i], bits[i+1], bits[i+2])
                    for i in range(len(bits)-2)]
        ans.append(bits[0])
    return ans


def image_counts(t, maxn):
    if t == 0:
        return [1 << n for n in range(maxn+1)]
    states = 1 << (2*t)
    edges = [[0, 0] for _ in range(states)]
    outputs = iterated_local_map(t)
    for w, label in enumerate(outputs):
        src = w >> 1
        dst = w & (states-1)
        edges[src][label] |= 1 << dst
    cache = {}
    def step(s, bit):
        key = (s, bit)
        if key not in cache:
            acc = 0
            tmp = s
            while tmp:
                j = (tmp & -tmp).bit_length()-1
                tmp &= tmp-1
                acc |= edges[j][bit]
            cache[key] = acc
        return cache[key]
    current = {(1 << states)-1: 1}
    counts = [1]
    for _ in range(maxn):
        following = {}
        for state, count in current.items():
            for b in (0, 1):
                nxt = step(state, b)
                if nxt:
                    following[nxt] = following.get(nxt, 0) + count
        current = following
        counts.append(sum(current.values()))
    return counts


def predicted_counts(t, maxn):
    a = [1]
    for n in range(1, maxn+1):
        a.append(2*a[n-1] - sum(a[n-4-2*k] for k in range(t)
                                  if n >= 4+2*k))
    return a


def perron_root(t):
    phi = (1+sqrt(5))/2
    lo, hi = phi, 2.0
    for _ in range(100):
        mid = (lo+hi)/2
        if mid**t * (mid*mid-mid-1) < 1:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def check_all():
    cases = 0
    # The complete radius-one bond update is determined by 16 inputs.
    for a, b, c, d in product((0, 1), repeat=4):
        left, right = edge(a, b), edge(c, d)
        expected = (1 if right == 1 and left != -1 else
                    -1 if left == -1 and right != 1 else 0)
        assert edge(local(a, b, c), local(b, c, d)) == expected
        cases += 1

    # Independent subset-construction counts use the iterated local map,
    # not the proposed forbidden-word presentation.
    count_checks = 0
    for t in range(0, 5):
        real = image_counts(t, 15)
        formula = predicted_counts(t, 15)
        assert real == formula, (t, real, formula)
        count_checks += len(real)

    # Every cycle admitted by the (t+1)-st presentation has an explicitly
    # constructed cycle antecedent admitted by the t-th presentation.
    ring_checks = 0
    for n in range(1, 14):
        for y in product((0, 1), repeat=n):
            for t in range(0, 6):
                if allowed_ring(y, t+1):
                    x = reverse_one_step(y)
                    assert x is not None
                    assert allowed_ring(x, t)
                    assert rule_on_ring(x) == y
                    ring_checks += 1

    phi = (1+sqrt(5))/2
    numerical = []
    for t in (4, 8, 12, 20, 30):
        lam = perron_root(t)
        ratio = (log(lam)-log(phi))*sqrt(5)*phi**(t+1)
        numerical.append((t, ratio))
        assert lam > phi
    assert abs(numerical[-1][1]-1) < 0.001
    assert all(perron_root(t) > perron_root(t+1) > phi
               for t in range(1, 11))

    print('VERIFY_OK:', cases, 'exact four-cell updates;',
          count_checks, 'independent finite image-count comparisons;',
          ring_checks, 'exact cyclic lift comparisons;',
          'entropy-asymptotic ratio at t=30 =', round(numerical[-1][1], 8))


if __name__ == '__main__':
    check_all()
