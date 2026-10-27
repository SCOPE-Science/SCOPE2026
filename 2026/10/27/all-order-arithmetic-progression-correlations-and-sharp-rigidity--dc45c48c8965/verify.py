"""Exact recurrence and independently computed periodic-cylinder tests for the
period-doubling arithmetic-progression correlation theorem.
No statistical simulation; arbitrary precision rational arithmetic is used.
"""
from fractions import Fraction
import math


def values(max_m):
    c=[Fraction(1), Fraction(1,3)]
    for m in range(2,max_m+1):
        if m%2==0:
            c.append((-1)**(m//2)*c[m//2])
        else:
            k=m//2
            c.append(((-1)**(k+1)*c[k+1]+(-1)**k*c[k])/2)
    return c

def predict(c,m,h):
    a=(h&-h).bit_length()-1
    if m%2==0:
        return 1-Fraction(1,2**a)+c[m]/2**a
    return Fraction(1,3)+Fraction((-1)**a,2**a)*(c[m]-Fraction(1,3))

def fast_period_average(m,h,L):
    size=1<<L
    mask=size-1
    # independently encode the finite cylinders from the original valuation definition.
    v=[1]*size
    for x in range(1,size):
        t=(x & -x).bit_length()-1
        v[x]=1 if t%2==0 else -1
    total=0
    for x in range(size):
        prod=1
        for j in range(m):
            prod*=v[(x+j*h)&mask]
        total+=prod
    return Fraction(total,size)

def test():
    c=values(4096)
    assert c[0]==1 and c[1]==Fraction(1,3)
    exc={2**k for k in range(13)}|{3*2**k for k in range(11)}
    exc={m for m in exc if m<=4096}
    actual={m for m in range(1,4097) if abs(c[m])==Fraction(1,3)}
    assert exc==actual,(sorted(exc^actual))
    assert all(abs(c[m])<=Fraction(1,3) for m in range(1,4097))
    # Test against an independent finite-cylinder evaluation for all below.
    tests=0
    for m in range(1,17):
        for h in (1,2,3,4,5,6,7,8,10,12,15,16,19,24,31,32):
            L=11
            finite=fast_period_average(m,h,L)
            exact=predict(c,m,h)
            assert abs(finite-exact)<=Fraction(2*m,2**L),(m,h,finite,exact)
            tests+=1
    assert c[2]==Fraction(-1,3) and c[3]==Fraction(-1,3)
    assert c[4]==Fraction(-1,3) and c[6]==Fraction(1,3)
    assert c[5]==0 and c[7]==0
    for m in range(2,4097,2):
        for h in (1,2,3,4,6,8,12,16):
            C=predict(c,m,h)
            if h%2:assert abs(C)<=Fraction(1,3)
            else:assert C>=Fraction(1,3)
    print(f'VERIFY_OK: {len(c)-1} exact all-order recurrence values; {len(exc)} precisely predicted sharp orders; {tests} independently evaluated 2-adic cylinder tests with error bounds; even-order parity separation checked for 2048 lengths')

if __name__=='__main__': test()
