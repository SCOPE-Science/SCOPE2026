"""Exact enumeration verifier for fixed-site / descent locality of uniform involutions.

Uses only Python's standard library; does not claim to prove the infinite-size theorem.
Run: python verify.py
"""
from collections import Counter
from fractions import Fraction


def involutions(n):
    a = [-1] * n
    def rec():
        try:
            i = a.index(-1)
        except ValueError:
            yield tuple(v + 1 for v in a)
            return
        a[i] = i
        yield from rec()
        for j in range(i + 1, n):
            if a[j] == -1:
                a[i] = j
                a[j] = i
                yield from rec()
                a[j] = -1
        a[i] = -1
    yield from rec()


def telephone(n):
    a, b = 1, 1
    if n == 0:
        return a
    for k in range(2, n + 1):
        a, b = b, b + (k - 1) * a
    return b


def flip_local_descent(p, j):
    """Two-site fixed/paired toggle, otherwise conjugation by adjacent swap.

    p is a 1-based value tuple and j a 0-based adjacent-position index.
    """
    a, b = j + 1, j + 2
    q = list(p)
    if (p[j], p[j + 1]) == (a, b):
        q[j], q[j + 1] = b, a
    elif (p[j], p[j + 1]) == (b, a):
        q[j], q[j + 1] = a, b
    else:
        q[j], q[j + 1] = q[j + 1], q[j]
        q = [b if value == a else a if value == b else value for value in q]
    return tuple(q)


def verify():
    checks = 0
    for n in range(2, 11):
        permutations = list(involutions(n))
        count = len(permutations)
        assert count == telephone(n)
        checks += 1
        fix = [tuple(int(p[i] == i + 1) for i in range(n)) for p in permutations]
        descent = [tuple(int(p[j] > p[j+1]) for j in range(n-1)) for p in permutations]
        for j in range(n-1):
            for p in permutations:
                q = flip_local_descent(p, j)
                assert flip_local_descent(q, j) == p, ('map involution', n, j, p)
                checks += 1
                assert int(p[j] > p[j+1]) + int(q[j] > q[j+1]) == 1, ('descent complement', n, j, p)
                checks += 1
                assert all((p[i] == i+1) == (q[i] == i+1) for i in range(n) if i not in (j,j+1)), ('remote pattern', n, j, p)
                checks += 1
            total_d = sum(ds[j] for ds in descent)
            assert total_d * 2 == count
            checks += 1
            for i in range(n):
                total_i = sum(fs[i] for fs in fix)
                total_both = sum(fs[i] * ds[j] for fs, ds in zip(fix, descent))
                cov = Fraction(total_both, count) - Fraction(total_i*total_d, count*count)
                if i == j:
                    expected = -Fraction(telephone(n-1),2*telephone(n))
                    if n >= 3:
                        expected += Fraction((i)*telephone(n-3), telephone(n))
                elif i == j+1:
                    expected = -Fraction(telephone(n-1),2*telephone(n))
                    if n >= 3:
                        expected += Fraction((n-i-1)*telephone(n-3), telephone(n))
                else:
                    expected = 0
                assert cov == expected, ('coordinate', n, i+1, j+1, cov, expected)
                checks += 1
            total_F_D = sum(sum(fs)*ds[j] for fs, ds in zip(fix, descent))
            total_F = sum(map(sum, fix))
            assert Fraction(total_F_D,count)-Fraction(total_F*total_d,count*count) == -Fraction(telephone(n-2),telephone(n))
            checks += 1
            remote = tuple(i for i in range(n) if i not in (j,j+1))
            groups = Counter()
            group_desc = Counter()
            for fs, ds in zip(fix, descent):
                key = tuple(fs[i] for i in remote)
                groups[key] += 1
                group_desc[key] += ds[j]
            for key,c in groups.items():
                assert 2*group_desc[key] == c, ('joint independence',n,j,key,c,group_desc[key])
                checks += 1
        total_D = sum(map(sum, descent))
        total_F = sum(map(sum, fix))
        total_FD = sum(sum(fs)*sum(ds) for fs,ds in zip(fix,descent))
        assert Fraction(total_FD,count)-Fraction(total_F*total_D,count*count) == -Fraction((n-1)*telephone(n-2),telephone(n))
        checks += 1
        print('n =',n, 'involutions =',count, 'checks cumulative =',checks)
    print('PASS:', checks, 'exact assertions')

if __name__ == '__main__':
    verify()
