"""Finite reproducibility checks for shortest no-11 cyclic word covers."""
from collections import Counter, defaultdict
from itertools import product


def fibonacci(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def allowed(n):
    return [''.join(t) for t in product('01', repeat=n) if '11' not in ''.join(t)]


def extras(n):
    return [s for s in allowed(n) if s[0] == s[-1] == '0' and '1' in s]


def phi(s):
    return s.find('1') if '1' in s else len(s)


def cyclic_windows(word, n):
    return [ ''.join(word[(i+j) % len(word)] for j in range(n))
             for i in range(len(word)) ]


def euler_word(n):
    edges = allowed(n) + extras(n)
    adj = defaultdict(list)
    for e in sorted(edges, reverse=True):
        adj[e[:-1]].append(e[-1])
    source = '0' * (n - 1)
    vertices = [source]
    letters = []
    output = []
    while vertices:
        v = vertices[-1]
        if adj[v]:
            letter = adj[v].pop()
            vertices.append(v[1:] + letter)
            letters.append(letter)
        else:
            vertices.pop()
            if letters:
                output.append(letters.pop())
    result = ''.join(reversed(output))
    assert len(result) == len(edges)
    return result


def certify(n):
    base, duplicate = allowed(n), extras(n)
    degree = defaultdict(lambda: [0, 0])
    for e in base + duplicate:
        degree[e[:-1]][0] += 1
        degree[e[1:]][1] += 1
    assert all(out == inc for out, inc in degree.values()), ('balance', n)
    assert len(base) == fibonacci(n+2)
    assert len(duplicate) == fibonacci(n)-1
    assert all(phi(e[:-1]) - phi(e[1:]) <= 1 for e in base)
    assert all(phi(e[:-1]) - phi(e[1:]) == 1 for e in duplicate)
    difference = sum(phi(v) * (sum(e[1:] == v for e in base) -
                               sum(e[:-1] == v for e in base)) for v in degree)
    assert difference == len(duplicate), ('dual', n, difference)
    cycle = euler_word(n)
    windows = Counter(cyclic_windows(cycle, n))
    assert set(windows) == set(base)
    assert sum(windows.values()) == fibonacci(n+2)+fibonacci(n)-1
    assert '11' not in cycle+cycle[:1]
    assert all(windows[e] == 2 for e in duplicate)
    assert all(windows[e] == 1 for e in base if e not in duplicate)
    return cycle


def small_exhaustion(n, target):
    needed = set(allowed(n))
    # Every binary cyclic candidate below the target, including illegal
    # cyclic outputs, is excluded by exact binary enumeration.
    tested = 0
    for L in range(1, target):
        for bits in product('01', repeat=L):
            x = ''.join(bits)
            if '11' in x + x[0]:
                continue
            tested += 1
            if L >= n and needed.issubset(cyclic_windows(x, n)):
                raise AssertionError(('shorter covering cycle', n, L, x))
    return tested


def main():
    for n in range(2, 18):
        u = certify(n)
        print('n={} admissible={} extra={} optimum={} checked_windows={}'.format(
            n, fibonacci(n+2), fibonacci(n)-1, len(u), len(cyclic_windows(u,n))))
    for n in range(2, 6):
        count = small_exhaustion(n, fibonacci(n+2)+fibonacci(n)-1)
        print('exhausted all shorter legal cyclic candidates n={} tested={}'.format(n, count))
    print('VERIFIED: construction, dual bound, exact length, coverage, and finite exclusions')


if __name__ == '__main__':
    main()
