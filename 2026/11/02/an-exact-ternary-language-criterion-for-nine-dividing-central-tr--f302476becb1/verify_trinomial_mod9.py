#!/usr/bin/env python3
"""Standalone exact-arithmetic checks for the central-trinomial mod-nine theorem.

These finite tests corroborate; they do not replace the digit-inductive proof.
"""

def digits3(n):
    if n == 0:
        return '0'
    out = ''
    while n:
        out = str(n % 3) + out
        n //= 3
    return out


def predicts(n):
    s = digits3(n)
    if s.count('2') >= 2:
        return True
    if s.count('2') == 1:
        i = s.index('2')
        return 0 < i < len(s)-1 and s[i-1] == '1'
    return False


def verify(limit=3**8):
    assert limit >= 3
    ts=[1,1]
    for n in range(1,limit):
        num = (2*n+1)*ts[n] + 3*n*ts[n-1]
        assert num % (n+1) == 0
        ts.append(num//(n+1))
    count=0
    for n in range(limit):
        got=(ts[n]%9==0)
        assert got == predicts(n), (n,digits3(n),ts[n]%9,got)
        count+=got
    for m in range(1,(limit-3)//3):
        assert (ts[3*m]-ts[m]-6*m*ts[m-1])%9 == 0, ('r0',m)
        assert (ts[3*m+1]-ts[m]-3*m*(ts[m]+5*ts[m-1]))%9==0, ('r1',m)
        assert (ts[3*m+2]-3*(m+1)*ts[m])%9==0, ('r2',m)
    for k in range(2,9):
        N=3**k
        observed=sum(predicts(n) for n in range(N))
        expected=3**k-(k+6)*2**(k-2)
        assert observed==expected,(k,observed,expected)
        if N<=limit:
            assert sum(t%9==0 for t in ts[:N])==expected
    print('VERIFY_OK terms=%d zeros=%d recurrences=%d closed_counts=2..8 first_zeros=%s' % (
        limit, count, (limit-3)//3-1,
        [n for n in range(100) if ts[n]%9==0][:15]))

if __name__ == '__main__':
    verify()
