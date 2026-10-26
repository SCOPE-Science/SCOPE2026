"""Independent finite checks for one palindromic-duplication inverse lists."""
from itertools import product


def inverse_parents(y, k):
    n = len(y) - k
    result = set()
    for i in range(n - k + 1):
        block = y[i:i + 2*k]
        if block == block[::-1]:
            x = y[:i+k] + y[i+2*k:]
            assert len(x) == n
            # Reproduce the forward insertion without using the palindrome test.
            v = x[i:i+k]
            assert x[:i+k] + v[::-1] + x[i+k:] == y
            result.add(x)
    return result


def witness(k, n, a=0, b=1):
    period = (a, a, b, b) if k % 2 else (a, b, b, a)
    return tuple(period[i % 4] for i in range(n + k))


def exhaustive(q, k, n):
    m = n-k+1
    maximum, maximum_words = -1, []
    for y in product(range(q), repeat=n+k):
        c = len(inverse_parents(y, k))
        if c > maximum:
            maximum, maximum_words = c, [y]
        elif c == maximum:
            maximum_words.append(y)
    if k % 4:
        assert maximum == (m+1)//2, (q,k,n,maximum)
        if k >= 2 and m % 2 and m >= 3:
            expected = {witness(k,n,a,b) for a in range(q) for b in range(q) if a != b}
            assert set(maximum_words) == expected, (q,k,n,len(maximum_words))
    if k == 4 and n == 6:
        assert maximum == 1
    return (q,k,n,maximum,len(maximum_words))


def main():
    tests = [(2,k,n) for k in range(1,7) for n in range(k,min(k+5,10)) if n+k<=14]
    tests += [(3,k,k+2) for k in range(1,5) if 2*k+2<=10] + [(3,1,5),(3,2,6),(3,3,7)]
    tests += [(4,1,3),(4,2,4),(4,3,5)]
    for q,k,n in tests:
        print('exhaustive',*exhaustive(q,k,n))
    for k in range(1,81):
        if k % 4 == 0: continue
        for n in [k,k+1,k+2,k+3,k+4,k+9,k+21,k+70]:
            p = inverse_parents(witness(k,n),k)
            assert len(p) == (n-k+2)//2, (k,n,len(p))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
