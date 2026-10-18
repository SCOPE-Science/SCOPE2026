#!/usr/bin/env python3
"""Direct finite checks of consecutive-cycle first-gap and dyadic exception formulas."""
from math import isqrt

def triangular(t):
    if t <= 0:
        return False
    d = 8*t+1
    s = isqrt(d)
    return s*s == d and (s-1)%2 == 0

def first_gap(n):
    seen = bytearray(n*(n+1)//2 + 1)
    for i in range(n):
        val=0
        for length in range(1,n+1):
            val+=1+(i+length-1)%n
            seen[val]=1
    return next(k for k in range(1,len(seen)) if not seen[k])

def exception_formula(M):
    return M-2+sum((isqrt((1 << (m+2))-7)-1)//2 for m in range(4,M+1))

exception_count=0
for n in range(8,257):
    p=1<<n.bit_length()
    predicted=(n & (n-1))!=0 and not triangular(p-n)
    mu=first_gap(n)
    assert (mu==p)==predicted,(n,mu,p,predicted)
    if mu>p:
        exception_count+=1
    if n & (n-1)==0:
        assert exception_count == exception_formula(n.bit_length()-1)
print('VERIFY_OK first_gaps=249 dyadic_endpoints=5 exceptions_at_256='+str(exception_count))
