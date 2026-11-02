"""Independent exact rational-enclosure checks for characteristic mechanical words."""
from collections import defaultdict
from fractions import Fraction
from math import isqrt

def sqrt_interval(k, digits=46):
    scale=10**digits
    v=isqrt(k*scale*scale)
    return Fraction(v,scale),Fraction(v+1,scale)

def samples():
    l2,h2=sqrt_interval(2)
    l5,h5=sqrt_interval(5)
    return [
        ('near_one_third',Fraction(1,3)+l2/1000,Fraction(1,3)+h2/1000),
        ('fibonacci',(3-h5)/2,(3-l5)/2),
        ('near_two_fifths',Fraction(2,5)-h2/1000,Fraction(2,5)-l2/1000),
    ]

def word_from_bounds(low,high,N):
    assert Fraction(1,3)<low<high<Fraction(2,5)
    floors=[]
    for j in range(1,N+3):
        a=j*low.numerator//low.denominator
        b=j*high.numerator//high.denominator
        assert a==b, ('insufficient exact enclosure',j)
        floors.append(a)
    return ''.join(str(floors[i+1]-floors[i]) for i in range(N))

def stack_tortoise(w):
    # Stack simulation: cannot push a character on equal or smaller top.
    stack=[]; out=[]
    for c in w:
        while stack and stack[-1]<=c: out.append(stack.pop())
        stack.append(c)
    while stack: out.append(stack.pop())
    return ''.join(out)

N=15000
for label,lo,hi in samples():
    word=word_from_bounds(lo,hi,N)
    assert word.startswith('01')
    for n in range(1,91):
        factors={word[i:i+n] for i in range(N-n+1)}
        assert len(factors)==n+1,(label,n,len(factors))
        fibers=defaultdict(set)
        for v in factors: fibers[stack_tortoise(v)].add(v)
        assert len(fibers)==(2 if n<=2 else n-1),(label,n,len(fibers))
        if n>=4:
            a=frozenset(('10'+word[:n-2],'01'+word[:n-2]))
            b=frozenset(('001'+word[:n-3],'010'+word[:n-3]))
            actual={frozenset(v) for v in fibers.values() if len(v)>1}
            assert actual=={a,b},(label,n,actual)
    print('PASS:',label,'certified mechanical prefix; fibers n=1..90')
print('PASS: independent exact-rational interval arithmetic and stack simulation')
