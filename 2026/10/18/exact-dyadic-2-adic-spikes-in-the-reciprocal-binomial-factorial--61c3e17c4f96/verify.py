#!/usr/bin/env python3
"""Exact integer reproducibility checks for a dyadic valuation theorem."""
import math

def v2(n):
    assert isinstance(n, int) and n > 0
    return (n & -n).bit_length() - 1

def via_convolution(n):
    return sum(math.factorial(k)*math.factorial(n-1-k) for k in range(n))

def main():
    a, fact = 0, 1   # fact=(n-1)! before the nth update
    records = {}
    for n in range(1, 4097):
        num = n*a + 2*fact
        assert num % 2 == 0, (n, 'recurrence integrality check')
        a = num//2
        if n & (n-1) == 0:
            m = n.bit_length()-1
            records[m] = v2(a)
            if n <= 256:
                assert a == via_convolution(n), (n, 'independent formula')
            if m >= 4:
                assert v2(a) == n+2*m-3, (n, v2(a), n+2*m-3)
            else:
                assert v2(a) == {0:0,1:1,2:4,3:12}[m]
        fact *= n
    assert records[4] == 21 and records[12] == 4096+24-3
    print('PASS: independent factorial sums n=1,2,4,8,16,32,64,128,256')
    print('PASS: recurrence all n=1..4096 and dyadic valuations m=0..12')
    print('dyadic 2-adic valuations:', records)

if __name__=='__main__':
    main()
