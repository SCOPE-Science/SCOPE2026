"""Finite diagnostics for palindromic factors of modular-difference lifts."""
from itertools import product


def predicted(q, m, L, n):
    if n <= m:
        return q ** ((n + 1) // 2)
    if n > m + L:
        return 0
    t = n - 1
    fixed = sum(1 for r in range(m) if (2*r-t) % m == 0)
    return q ** ((m + fixed) // 2)


def count_from_base(q, m, n, base_factors):
    count = set()
    for prefix in product(range(q), repeat=m):
        for y in base_factors:
            x = list(prefix)
            while len(x) < n:
                i = len(x) - m
                x.append((x[i] + y[i]) % q)
            w = tuple(x[:n])
            if w == w[::-1]:
                count.add(w)
    return len(count)


def subwords(a, length):
    if length == 0:
        return {()}
    return {tuple(a[j:j+length]) for j in range(len(a)-length+1)}


def fibonacci_word(limit):
    w = '0'
    while len(w) < limit:
        w = ''.join('01' if z == '0' else '0' for z in w)
    return [int(z) for z in w[:limit]]


def run():
    checks = 0
    systems = [('Fibonacci', fibonacci_word(2048), 2)]
    for word, L in [([0,0,0,1],3),([0,0,1],2),([0,1],1),([0,0,2,0,1],2)]:
        systems.append(('periodic_'+str(word), word*300, L))
    for name, base, L in systems:
        for q in (3, 4, 5):
            if max(base) >= q or (set(base) & {(-a) % q for a in set(base)}) != {0}:
                continue
            for m in range(1,5):
                for n in range(1,m+L+3):
                    # The projected block required by an n-block of a lift has length max(0,n-m).
                    factors = subwords(base,max(0,n-m))
                    actual=count_from_base(q,m,n,factors)
                    expected=predicted(q,m,L,n)
                    assert actual == expected, (name,q,m,n,actual,expected)
                    checks+=1
    # Algebraic reflection counts without using predicted formula's orbit count.
    for q in (3,4,5,7):
        for m in range(1,8):
            for n in range(m+1,m+5):
                reflected=[]
                for c in product(range(q),repeat=m):
                    w=tuple(c[i % m] for i in range(n))
                    if w==w[::-1]:
                        reflected.append(w)
                assert len(set(reflected))==predicted(q,m,20,n)
                checks+=1
    print(f'PASS {checks} independent finite palindrome-count checks')

if __name__ == '__main__':
    run()
