"""Exact integer-coefficient and exhaustive checks for mixed-involution universality.

Uses the standard library only. The theorem's proof is combinatorial; these
finite tests are independent checks, not an infinite proof.
"""
from itertools import product
from math import comb


def onto(j, h):
    if j == 0:
        return int(h == 0)
    return sum((-1) ** (j - a) * comb(j, a) * a ** h
               for a in range(j + 1))


def predicted(q, f, d, nmax):
    assert q == f + 2 * d and f > 0 and d > 0
    hmax = nmax // 2
    B = [[onto(j, h) for h in range(hmax + 1)]
         for j in range(q + 1)]
    R = [sum(comb(q, j) * B[j][h] for j in range(q))
         for h in range(hmax + 1)]
    E = [sum(comb(d, r) * 2 ** (d-r) * B[f+d+r][h]
             for r in range(d)) for h in range(hmax + 1)]
    O = [sum(comb(d, r) * 2 ** (d-r) * B[f-1+d+r][h]
             for r in range(d+1))
         +sum(comb(d, r) * 2 ** (d-r) * B[f+d+r][h]
              for r in range(d)) for h in range(hmax + 1)]
    A = [q * B[q-1][h-1] if h else 0 for h in range(hmax+1)]
    powers = [[1] + [0] * hmax]
    for t in range(1, 1 + hmax // q):
        old = powers[-1]
        powers.append([sum(old[a] * A[h-a] for a in range(h+1))
                       for h in range(hmax+1)])
    result = {}
    for n in range(nmax + 1):
        h = n//2
        base = R
        good = E if n%2==0 else O
        multiplier = 1 if n%2==0 else f
        for t, ap in enumerate(powers):
            nbad = multiplier*sum(ap[a]*(base[h-a]-good[h-a])
                                  for a in range(h+1))
            ngood = multiplier*sum(ap[a]*good[h-a]
                                   for a in range(h+1))
            if nbad:
                result[n,2*t] = result.get((n,2*t),0)+nbad
            if ngood:
                result[n,2*t+1] = result.get((n,2*t+1),0)+ngood
    assert all(x>=0 for x in result.values())
    return result


def theta_words(q, f, n):
    pi = list(range(q))
    for x in range(f,q,2):
        pi[x],pi[x+1] = x+1,x
    for first in product(range(q),repeat=n//2):
        last = tuple(pi[x] for x in first[::-1])
        if n % 2 == 0:
            yield first+last
        else:
            for mid in range(f):
                yield first+(mid,)+last


def index_greedy(word,q):
    mask = 0
    count = 0
    for x in word:
        mask |= 1<<x
        if mask==(1<<q)-1:
            count += 1
            mask = 0
    return count


def compute_actual(q,f,nmax):
    out = {}
    for n in range(nmax+1):
        for word in theta_words(q,f,n):
            j = index_greedy(word,q)
            out[n,j] = out.get((n,j),0)+1
    return out


def main():
    cases=[(3,1,1,12),(4,2,1,12),(5,1,2,10),
           (5,3,1,9),(6,2,2,8),(6,4,1,8)]
    for q,f,d,N in cases:
        predicted_counts=predicted(q,f,d,N)
        actual_counts=compute_actual(q,f,N)
        assert predicted_counts==actual_counts,(q,f,d,predicted_counts,actual_counts)
        for n in range(N+1):
            assert sum(v for (size,j),v in actual_counts.items() if size==n)==q**(n//2)*(f if n%2 else 1)
        print('q=%d f=%d d=%d through_n=%d coefficients=%d total_words=%d PASS' %
              (q,f,d,N,len(actual_counts),sum(actual_counts.values())))
    print('VERIFY_OK')


if __name__=='__main__':
    main()
