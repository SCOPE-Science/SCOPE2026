"""Independent finite checks for partial-involution commuting-pair formulas.
Run: python3 verify.py. Python standard library only.
"""
from collections import Counter
from functools import lru_cache
from math import factorial, comb


def partial_involutions(n):
    """Build from undefined/fixed/transposed choices on the least unused point."""
    def extend(remaining, current):
        if not remaining:
            yield tuple(current)
            return
        x = remaining[0]
        rest = remaining[1:]
        current[x] = -1
        yield from extend(rest, current)
        current[x] = x
        yield from extend(rest, current)
        for y in rest:
            current[x] = y
            current[y] = x
            yield from extend(tuple(z for z in rest if z != y), current)
            current[y] = -1
        current[x] = -1
    yield from extend(tuple(range(n)), [-1] * n)


def compose(a, b):
    return tuple(-1 if y == -1 or a[y] == -1 else a[y] for y in b)


def product_type(h):
    n = len(h)
    fixed = sum(h[i] == i for i in range(n))
    pairs = sum(0 <= h[i] != i < h[i] for i in range(n))
    return fixed, pairs


def involution_number(f):
    return sum(factorial(f) // (2**j * factorial(j) * factorial(f-2*j))
               for j in range(f//2+1))


def wreath_involution_number(t):
    return sum(factorial(t)*2**(t-2*j)//(factorial(j)*factorial(t-2*j))
               for j in range(t//2+1))


def hole_number(m):
    return sum(factorial(m)*3**(m-2*j)//(factorial(j)*factorial(m-2*j))
               for j in range(m//2+1))


def total_recurrence(n):
    a = [0] * (max(0, n) + 1)
    a[0] = 1
    for k in range(1, n+1):
        a[k] = 4*a[k-1]
        if k>=2: a[k] += 5*(k-1)*a[k-2]
        if k>=4: a[k] += (k-1)*(k-2)*(k-3)*a[k-4]
    return a


def run():
    expected = total_recurrence(9)
    assert expected[:7] == [1,4,21,124,817,5844,45061], expected
    for n in range(7):
        invols = tuple(partial_involutions(n))
        buckets = Counter()
        fiber = Counter()
        total = 0
        for a in invols:
            for b in invols:
                ab = compose(a,b)
                if ab != compose(b,a):
                    continue
                total += 1
                f,t = product_type(ab)
                assert all(ab[x]==-1 or ab[ab[x]]==x for x in range(n))
                buckets[(f,t)] += 1
                fiber[ab] += 1
        assert total == expected[n], (n,total,expected[n])
        for h,actual in fiber.items():
            f,t=product_type(h)
            m=n-f-2*t
            predicted=involution_number(f)*wreath_involution_number(t)*hole_number(m)
            assert actual==predicted, (n,h,actual,predicted)
        # Independent labeled exponential-formula coefficient, marking product cycle type.
        polynomial = Counter({(0,0,0):1})
        # polynomial keys are (size, fixed-points-of-product, transpositions-of-product).
        # The differential equation F'(z)=P'(z) F(z) with four atom degrees.
        by_size = [Counter() for _ in range(n+1)]
        by_size[0][(0,0)]=1
        atoms = [ (1,0,0,3), (1,1,0,1),
                  (2,0,0,2), (2,2,0,1), (2,0,1,2), (4,0,2,6)]
        # Atoms: cardinality k and count of structures on a fixed labeled set.
        for size in range(1,n+1):
            for k,f,t,wt in atoms:
                if k>size: continue
                for (prev_f,prev_t),prior in by_size[size-k].items():
                    # Fix block containing smallest label to avoid overcounting.
                    by_size[size][(f+prev_f,t+prev_t)] += (
                        comb(size-1,k-1)*wt*prior)
        assert sum(by_size[n].values())==total,(n,by_size[n],total)
        assert dict(by_size[n])==dict(buckets),(n,by_size[n],buckets)
        print(f'n={n} involutions={len(invols)} commuting_ordered_pairs={total} profile_cells={len(buckets)}')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
