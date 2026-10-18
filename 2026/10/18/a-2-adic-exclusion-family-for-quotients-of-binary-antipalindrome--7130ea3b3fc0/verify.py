from fractions import Fraction
from decimal import Decimal, getcontext

def antipals(half):
    for first in range(1 << (half-1),1 << half):
        b=f'{first:0{half}b}'
        yield (first<<half)|int(''.join('1' if c=='0' else '0' for c in b[::-1]),2)

def is_apal(n):
    if n<2:return False
    b=f'{n:b}'
    return len(b)%2==0 and all(b[i]!=b[-1-i] for i in range(len(b)//2))

def excluded(n):
    if n<=1 or not (n&1):return False
    j=(n.bit_length()-2)//2
    if j<0:return False
    q=1<<(2*j)
    if not (2*q<=n<4*q):return False
    h=((n-1)&-(n-1)).bit_length()-1
    if h<1:return False
    t=1<<h
    return n*(t+1)<4*t*q

for m in range(1,9):
    for b in antipals(m):
        for n in range(2,5000):
            if excluded(n): assert not is_apal(n*b),(n,b,n*b)
print('No excluded quotient for antipalindromic denominators up to 16 bits, n<5000')
for j in range(1,9):
    q=4**j
    obs=sum(excluded(n) for n in range(2*q,4*q))
    print('j',j,'q',q,'excluded',obs,'coefficient',round(obs/q,10))
getcontext().prec=60
v=sum((Decimal(1)/(Decimal(2)**h*(Decimal(2)**h+1)) for h in range(1,180)),Decimal(0))
d=(Decimal(1)/6-v/3)
print('exact-series-density',d)
assert d>Decimal('0.088') and d<Decimal('0.089')
for m in range(1,9):
    for b in antipals(m):
        for n in range(1,256,2):
            a=n*b
            if is_apal(a): assert not excluded(n)
print('Additional independent finite ratio checks passed')
