"""Finite brute-force verification for endomorphisms of S(n,k).

Represent elements as partial bijections on a chain of n points and a
separate cyclic permutation of k points.  All computations are exact.
"""
from collections import Counter, deque
from math import ceil, gcd


def compose(a, b):
    """Apply a, then b; -1 represents an undefined value."""
    return tuple(-1 if v < 0 else b[v] for v in a)


def inverse(a):
    out = [-1] * len(a)
    for i, j in enumerate(a):
        if j >= 0:
            out[j] = i
    return tuple(out)


def generated(n, k):
    N = n + k
    identity = tuple(range(N))
    generator = tuple(i + 1 if i < n - 1 else -1
                      for i in range(n)) + tuple(
                          n + (i + 1) % k for i in range(k))
    generators = ((1, generator), (-1, inverse(generator)))
    words = {identity: ()}
    queue = deque([identity])
    while queue:
        x = queue.popleft()
        for letter, g in generators:
            y = compose(x, g)
            if y not in words:
                words[y] = words[x] + (letter,)
                queue.append(y)
    return generator, words


def evaluate(word, y):
    identity = tuple(range(len(y)))
    neg = inverse(y)
    out = identity
    for letter in word:
        out = compose(out, y if letter == 1 else neg)
    return out


def divisor_phi(k):
    out = []
    for d in range(1, k + 1):
        if k % d:
            continue
        out.append((d, sum(gcd(d, j) == 1 for j in range(1, d + 1))))
    return out


def omega(k):
    n = k
    count = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            count += 1
            while n % d == 0:
                n //= d
        d += 1
    return count + (n > 1)


def predicted(n, k):
    hist = Counter({1: 1})
    hist[2] += n * (n + 1) // 2 - 1
    for d, multiplicity in divisor_phi(k):
        hist[d + 1] += multiplicity
    for h in range(1, n):
        period = k // gcd(k, h)
        for b in range(h, n):
            r = ceil((n - b) / h) + 1
            size = r * (r + 1) * (2 * r + 1) // 6 + period
            hist[size] += 2 * (b - h + 1)
    return hist


def check(n, k, full_homomorphism):
    gen, words = generated(n, k)
    size = len(words)
    expected_size = n * (n + 1) * (2 * n + 1) // 6 + k
    assert size == expected_size, (n, k, size, expected_size)
    elements = list(words)
    image_sizes = Counter()
    idempotent_endos = 0
    automorphisms = 0
    for y in elements:
        # Recompute endomorphism values from words; no image-size formula is
        # used in the following exhaustive enumeration.
        mapped = {a: evaluate(w, y) for a, w in words.items()}
        assert set(mapped.values()) <= set(words), (n, k, 'not closed')
        assert mapped[tuple(range(n + k))] == tuple(range(n + k))
        assert mapped[gen] == y
        if full_homomorphism:
            for a in elements:
                for b in elements:
                    assert mapped[compose(a, b)] == compose(mapped[a], mapped[b]), (
                        n, k, 'multiplication not preserved')
        image = set(mapped.values())
        image_sizes[len(image)] += 1
        if mapped[y] == y:
            idempotent_endos += 1
        if len(image) == size:
            automorphisms += 1
    expected = predicted(n, k)
    assert image_sizes == expected, (n, k, image_sizes, expected)
    expected_idempotents = n * (n + 1) // 2 + (1 << omega(k)) + 1
    assert idempotent_endos == expected_idempotents, (n, k, idempotent_endos, expected_idempotents)
    assert automorphisms == 2, (n, k, automorphisms)
    return size, len(elements), idempotent_endos, automorphisms, sorted(image_sizes.items())


def main():
    count = 0
    for n in range(2, 7):
        for k in (1, 2, 3, 4, 6):
            # Exhaustive multiplication preservation through n=4.
            result = check(n, k, full_homomorphism=(n <= 4))
            print('n=', n, 'k=', k, 'size=', result[0], 'idempotent_endos=',
                  result[2], 'automorphisms=', result[3], 'ranks=', result[4])
            count += 1
    print('VERIFY_OK', count, 'exact configurations')


if __name__ == '__main__':
    main()
