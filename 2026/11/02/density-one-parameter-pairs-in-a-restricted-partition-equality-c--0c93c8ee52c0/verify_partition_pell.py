"""Integer checks for the restricted-partition Pell-family theorem.

The general theorem uses a symbolic Pell action; finite checks here do not
certify the infinite statement.
"""
from math import isqrt


def partition_count(a, N):
    return sum((N-a*t)//2+1 for t in range(N//a+1))


def quadratic_section(a, n):
    return a*n*n+(a//2+2)*n+1


def fundamental_pell(d):
    a0 = isqrt(d)
    assert a0*a0 != d and d > 0
    m, den, c = 0, 1, a0
    old_num, num = 0, 1
    old_den, den_conv = 1, 0
    while True:
        nxt_num = c*num+old_num
        nxt_den = c*den_conv+old_den
        if nxt_num*nxt_num-d*nxt_den*nxt_den == 1:
            return nxt_num, nxt_den
        old_num, num = num, nxt_num
        old_den, den_conv = den_conv, nxt_den
        m = den*c-m
        den = (d-m*m)//den
        c = (a0+m)//den


def multiply(A, B, modulus=None):
    result = (A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3],
              A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
    if modulus is not None:
        result = tuple(q % modulus for q in result)
    return result


def witness(a, b):
    u, v = fundamental_pell(a*b)
    T = (u, a*v, b*v, u)
    modulus = 2*a*b
    R = (1, 0, 0, 1)
    for h in range(1, 100001):
        R = multiply(R, T, modulus)
        if R == (1, 0, 0, 1):
            break
    else:
        raise AssertionError('unexpected modular order search bound')
    R = (1, 0, 0, 1)
    for _ in range(h):
        R = multiply(R, T)
    da, db = a//2+2, b//2+2
    X = R[0]*da+R[1]*db
    Y = R[2]*da+R[3]*db
    assert X % (2*a) == da and Y % (2*b) == db
    n, m = (X-da)//(2*a), (Y-db)//(2*b)
    assert n > 0 and m > 0
    assert b*X*X-a*Y*Y == b*da*da-a*db*db
    assert quadratic_section(a, n) == quadratic_section(b, m)
    return n, m


def main():
    section_checks = 0
    for a in range(3, 41):
        for n in range(0, 18):
            assert partition_count(a, 2*a*n) == quadratic_section(a, n)
            section_checks += 1
    assert partition_count(3, 42) == partition_count(4, 48) == 169
    nonsquare_pairs = 0
    for a in range(3, 16):
        for b in range(a+1, 17):
            if isqrt(a*b)**2 == a*b:
                continue
            witness(a, b)
            nonsquare_pairs += 1
    assert nonsquare_pairs >= 65
    print(f'VERIFY_OK section_checks={section_checks} pell_pairs={nonsquare_pairs}')


if __name__ == '__main__':
    main()
