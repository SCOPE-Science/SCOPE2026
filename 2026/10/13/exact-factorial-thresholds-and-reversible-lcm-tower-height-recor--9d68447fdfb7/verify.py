"""Exact reproducible boundary checks for tower height at factorial and lcm arguments."""
from functools import lru_cache


def primes_up_to(limit):
    if limit < 2:
        return []
    s = bytearray(b'\x01') * (limit + 1)
    s[0:2] = b'\x00\x00'
    for p in range(2, int(limit ** 0.5) + 1):
        if s[p]:
            s[p*p:limit+1:p] = b'\x00' * (((limit-p*p)//p)+1)
    return [p for p in range(2,limit+1) if s[p]]


@lru_cache(None)
def height_of_integer(n):
    if n == 1:
        return 0
    assert n > 1
    largest = 0
    d = 2
    while d*d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            largest = max(largest, height_of_integer(e))
        d += 1 if d == 2 else 2
    if n > 1:
        largest = max(largest, height_of_integer(1))
    return 1 + largest


def factorial_height(N):
    largest = 0
    for p in primes_up_to(N):
        e = 0
        q = p
        while q <= N:
            e += N // q
            q *= p
        largest = max(largest, height_of_integer(e))
    return largest + 1 if N >= 2 else 0


def lcm_height(N):
    largest = 0
    for p in primes_up_to(N):
        e = 0
        q = p
        while q <= N:
            e += 1
            q *= p
        largest = max(largest, height_of_integer(e))
    return largest + 1 if N >= 2 else 0


def main():
    E={1:2,2:4,3:16,4:65536}
    F={1:2,2:4,3:6,4:18,5:65538}
    for k,N in F.items():
        lo = factorial_height(N-1)
        hi = factorial_height(N)
        assert lo < k, (k,N,lo)
        assert hi == k, (k,N,hi)
        print('factorial_first',k,N,'prev_height',lo,'height',hi)
    for k,N in E.items():
        lo=lcm_height(N-1)
        hi=lcm_height(N)
        assert lo < k and hi == k,(k,N,lo,hi)
        print('lcm_first',k,N,'prev_height',lo,'height',hi)
        if k>=3:
            before=lcm_height(2*N-1)
            after=lcm_height(2*N)
            assert before==k and after==k-1,(k,N,before,after)
            print('plateau_end',k,2*N,'before_height',before,'after_height',after)
    maxima=[]
    for N in range(2,513):
        v=lcm_height(N)
        if not maxima or v>maxima[-1][1]:
            maxima.append((N,v))
    assert maxima==[(2,1),(4,2),(16,3)]
    print('small_range_records',maxima)
    print('VERIFY_OK factorial_levels=1..5 lcm_levels=1..4 lcm_drop_levels=3..4 checked_up_to=131072')

if __name__=='__main__':
    main()
