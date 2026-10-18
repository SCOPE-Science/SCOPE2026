"""Separate exact checks for uniform minimum-gap subsequence universality.

Uses direct embedding enumeration for small words and a separate finite-series
convolution to compare the proved rational generating function.
"""
from itertools import product, combinations
from math import factorial, comb


def direct_universal(w, q, k, g):
    n = len(w)
    seen = set()
    for indices in combinations(range(n), k):
        if all(j-i-1 >= g for i, j in zip(indices, indices[1:])):
            seen.add(tuple(w[i] for i in indices))
    return len(seen) == q**k


def greedy_universal(w, q, k, g):
    start = 0
    for phase in range(k):
        first = {}
        for j in range(start, len(w)):
            first.setdefault(w[j], j)
            if len(first) == q:
                start = j+1
                break
        else:
            return False
        if phase+1 < k:
            start += g
    return True


def arch_count(q, length):
    if length < q:
        return 0
    # Last letter is new, previous positions surject onto the other q-1 letters.
    return q*sum((-1)**j*comb(q-1,j)*(q-1-j)**(length-1)
                 for j in range(q))


def predicted_count(q, k, g, n):
    # Exact coefficient of A_q(t)^k * (qt)^(g(k-1))/(1-qt).
    N = n - g*(k-1)
    if N < q*k:
        return 0
    current = [0]*(N+1)
    current[0] = 1
    for _ in range(k):
        nxt = [0]*(N+1)
        for m, coeff in enumerate(current):
            if not coeff:
                continue
            for length in range(q, N-m+1):
                a = arch_count(q, length)
                if a:
                    nxt[m+length] += coeff*a
        current = nxt
    return (q**(g*(k-1))) * sum(current[m] * q**(N-m)
                                     for m in range(N+1))


def exhaustive(q, g, k, max_n):
    results = []
    for n in range(max_n+1):
        observed = 0
        for w in product(range(q), repeat=n):
            direct = direct_universal(w, q, k, g)
            greedy = greedy_universal(w, q, k, g)
            assert direct == greedy, (q, g, k, w, direct, greedy)
            observed += direct
        predicted = predicted_count(q, k, g, n)
        assert observed == predicted, (q,g,k,n,observed,predicted)
        results.append((n, observed))
    return results


def check_index_distribution(q, g, max_n):
    # Literal histogram versus the telescoping coefficient of the bivariate formula.
    for n in range(max_n+1):
        max_index = (n+g)//(q+g)
        histogram = [0]*(max_index+1)
        for w in product(range(q), repeat=n):
            idx = max((k for k in range(max_index+1)
                       if k==0 or direct_universal(w, q, k, g)), default=0)
            histogram[idx] += 1
        predicted = []
        for k in range(max_index+1):
            current = q**n if k == 0 else predicted_count(q,k,g,n)
            nxt = predicted_count(q,k+1,g,n)
            predicted.append(current-nxt)
        assert histogram == predicted, (q,g,n,histogram,predicted)
    print('full index histogram verified q=%d g=%d n<=%d' % (q,g,max_n))


def main():
    cases = [(2,0,2,9),(2,1,2,9),(2,1,3,10),(2,2,2,8),
             (3,0,2,7),(3,1,2,8),(3,2,2,8),(4,1,2,7)]
    for q,g,k,n in cases:
        results = exhaustive(q,g,k,n)
        print('q=%d g=%d k=%d n<=%d: %s' % (q,g,k,n,results))
    for q,g,k in [(2,0,5),(2,1,5),(2,2,4),(3,0,4),(3,1,3),(4,1,3)]:
        n = q*k+g*(k-1)
        expected = factorial(q)**k * q**(g*(k-1))
        assert predicted_count(q,k,g,n)==expected
        print('minimal q=%d g=%d k=%d n=%d count=%d' %(q,g,k,n,expected))
    check_index_distribution(2,1,9)
    check_index_distribution(3,1,7)
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
