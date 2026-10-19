from math import gcd
from itertools import product
POLY={1:0b11,2:0b111,3:0b1011,4:0b10011}
def mul(a,b,f):
    p=POLY[f];v=0
    while b:
        if b&1:v^=a
        b>>=1;a<<=1
        if a&(1<<f):a^=p
    return v
def mul_sq(a,f):return mul(a,a,f)
def iterate(x,f):
    sq=[mul_sq(z,f) for z in x];s=0
    for z in sq:s^=z
    return tuple(s^z for z in sq)
def predicted(n,f,k):
    g=gcd(f,k)
    if n%2: return 2**(g*(n-1))
    if k%2==0 or ((f//g)%2==0):return 2**(g*n)
    return 2**(g*(n-1))
cases=0
for f,n in [(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3)]:
    q=1<<f
    states=list(product(range(q),repeat=n))
    for k in range(1,2*f+1):
        count=0
        for x in states:
            y=x
            for _ in range(k): y=iterate(y,f)
            count+=y==x
        expected=predicted(n,f,k)
        assert count==expected,(f,n,k,count,expected)
    if n%2:
        assert all(sum((z for z in iterate(x,f)),0) is not None for x in states)
        assert all(iterate(iterate(x,f),f)==iterate(tuple(mul_sq(z,f) for z in x),f) for x in states)
    else:
        assert all(iterate(iterate(x,f),f)==tuple(mul_sq(mul_sq(z,f),f) for z in x) for x in states)
    cases+=1
print('VERIFY_OK',cases,'field/dimension cases; fixed-points for all k <= 2f')
