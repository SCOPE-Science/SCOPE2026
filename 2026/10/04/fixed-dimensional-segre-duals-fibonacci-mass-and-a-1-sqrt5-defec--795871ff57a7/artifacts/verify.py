#!/usr/bin/env python3
from math import comb, isqrt


def fib(k):
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def d(n, a):
    return comb(n - a + 1, a)


def q(n, a):
    return 5*a*a - (5*n + 2)*a + n*n - 1


def predicted_modes(n):
    # No floating point: d(a+1)>=d(a) iff q(n,a)>=0.
    lo, hi = 1, n//2
    if lo == hi:
        return {lo}
    last_nondec = 0
    for a in range(lo, hi):
        if q(n, a) >= 0:
            last_nondec = a
        else:
            break
    if last_nondec == 0:
        return {1}
    if q(n, last_nondec) == 0:
        return {last_nondec, last_nondec + 1}
    return {last_nondec + 1}


def verify(N=1000):
    tie_cases=[]
    for n in range(2, N+1):
        A=list(range(1, n//2 + 1))
        vals=[d(n,a) for a in A]
        m=max(vals)
        actual={a for a,v in zip(A,vals) if v==m}
        assert actual == predicted_modes(n), (n, actual, predicted_modes(n))

        ratios=[]
        for a in A[:-1]:
            lhs=d(n,a+1)-d(n,a)
            assert (lhs >= 0) == (q(n,a) >= 0), (n,a,lhs,q(n,a))
            ratios.append(((n-2*a+1)*(n-2*a), (a+1)*(n-a+1)))
        for i in range(len(ratios)-1):
            p1,q1=ratios[i]; p2,q2=ratios[i+1]; assert p1*q2 > p2*q1, (n,i,ratios[i],ratios[i+1])

        target=fib(n+2)-1-(n&1)
        assert sum(vals)==target, (n,sum(vals),target)

        D=5*n*n+20*n+24
        s=isqrt(D)
        if s*s==D and (5*n+2-s)%10==0:
            a=(5*n+2-s)//10
            if 1<=a<n//2+1 and q(n,a)==0:
                assert actual=={a,a+1}
                tie_cases.append((n,a))

    print('VERIFY_OK')
    print('checked_n=2..%d' % N)
    print('first_ties=' + repr(tie_cases[:8]))


if __name__ == '__main__':
    verify()
