"""Reproducible finite verification of the rank-index formula for cycle partial isometries."""
from math import gcd
from itertools import combinations, permutations


def phi(k):
    return sum(gcd(k, j) == 1 for j in range(1, k + 1))


def poly_mul(a, b):
    ans = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            ans[i + j] += u * v
    return ans


def poly_power(p, k):
    ans = [1]
    for _ in range(k):
        ans = poly_mul(ans, p)
    return ans


def transfer_poly(t, h):
    """trace(T_h(x)^t), with states trailing-one-run lengths 0..h-1."""
    answer = [0] * (t + 1)
    for initial in range(h):
        paths = {(initial, 0): 1}
        for _ in range(t):
            nxt = {}
            for (state, weight), count in paths.items():
                k = (0, weight)
                nxt[k] = nxt.get(k, 0) + count
                if state + 1 < h:
                    k = (state + 1, weight + 1)
                    nxt[k] = nxt.get(k, 0) + count
            paths = nxt
        for (state, weight), count in paths.items():
            if state == initial:
                answer[weight] += count
    return answer


def direct_cyclic_subset_poly(t, h):
    ans = [0] * (t + 1)
    for mask in range(1 << t):
        if any(all(mask & (1 << ((i + j) % t)) for j in range(h)) for i in range(t)):
            continue
        ans[mask.bit_count()] += 1
    return ans


def formula(n, h):
    if h == 1:
        return [1] + [0] * n
    ans = [0] * (n + 1)
    for t in range(1, n + 1):
        if n % t == 0:
            coeffs = poly_power(transfer_poly(t, h), n // t)
            for r, count in enumerate(coeffs):
                ans[r] += phi(t) * count
    if n % 2:
        refl = poly_power([1, 2], (n - 1) // 2)
        for r, count in enumerate(refl):
            ans[r] += n * count
    else:
        for number_pairs in [(n - 2) // 2, n // 2]:
            refl = poly_power([1, 2], number_pairs)
            for r, count in enumerate(refl):
                ans[r] += n // 2 * count
    ans[0] -= 2 * n - 1
    ans[1] -= n * (n - 1)
    if not (n % 2):
        ans[2] -= n * (n - 2) // 2
    return ans


def enumerate_dihedral_restrictions(n):
    maps = set()
    for sign in [1, -1]:
        for shift in range(n):
            sigma = tuple((sign * v + shift) % n for v in range(n))
            for mask in range(1 << n):
                maps.add(tuple(sigma[i] if mask & (1 << i) else -1 for i in range(n)))
    return maps


def nilpotent_by_h(f, h):
    n = len(f)
    for start in range(n):
        v = start
        for _ in range(h):
            if f[v] < 0:
                break
            v = f[v]
        else:
            return False
    return True


def enumerate_polynomial(n, h, elements):
    coeffs = [0] * (n + 1)
    for f in elements:
        if nilpotent_by_h(f, h):
            coeffs[sum(v >= 0 for v in f)] += 1
    return coeffs


def is_isometry(f):
    n = len(f)
    domain = [i for i, v in enumerate(f) if v >= 0]
    return all(min(abs(i-j),n-abs(i-j)) == min(abs(f[i]-f[j]),n-abs(f[i]-f[j]))
               for i,j in combinations(domain,2))


def direct_isometries(n):
    result = set()
    vertices = range(n)
    for r in range(n + 1):
        for dom in combinations(vertices,r):
            for img in permutations(vertices,r):
                f = [-1] * n
                for a,b in zip(dom,img): f[a] = b
                tup = tuple(f)
                if is_isometry(tup): result.add(tup)
    return result


def main():
    for t in range(1, 11):
        for h in range(1, 12):
            assert transfer_poly(t, h) == direct_cyclic_subset_poly(t, h), (t,h)
    for n in range(3, 11):
        elements = enumerate_dihedral_restrictions(n)
        if n <= 6:
            assert elements == direct_isometries(n), ('isometries', n)
        prev = [0] * (n + 1)
        for h in range(1, n + 1):
            got = enumerate_polynomial(n, h, elements)
            expected = formula(n, h)
            assert got == expected, (n, h, got, expected)
            assert all(g >= p for g, p in zip(got, prev))
            prev = got
        assert prev[n] == 0
        assert prev[n - 1] == n * phi(n)
        print('n=%d total_nilpotent=%d ranks=%s' % (n, sum(prev), prev[:-1]))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
