"""Direct finite checks of a prime-power recurrence moment theorem.

All arithmetic is integer arithmetic. Run: python VERIFY.py
"""
from collections import Counter
from fractions import Fraction


def cycle_counts(p, d, k, step):
    m = p**k
    N = m**d
    seen = bytearray(N)
    counts = Counter()
    for idx in range(N):
        if seen[idx]:
            continue
        x = []
        t = idx
        for _ in range(d):
            x.append(t % m)
            t //= m
        if all(v % p == 0 for v in x):
            continue
        x = tuple(x)
        hits = 0
        length = 0
        while True:
            z = sum(x[i] * m**i for i in range(d))
            if seen[z]:
                break
            seen[z] = 1
            length += 1
            hits += (x[0] == 0)
            x = step(x, m)
        T = (sum(p**i for i in range(d))) * p**(k-1)
        assert length == T, (p,d,k,length,T)
        counts[hits] += 1
    H = (p**(d-1)-1)//(p-1)
    num = sum(counts.values())
    mean = Fraction(sum(h * v for h, v in counts.items()), num)
    var = Fraction(sum(h*h * v for h,v in counts.items()), num) - mean*mean
    assert num == (p-1)*p**((d-1)*(k-1)), (p,d,k,num)
    assert mean == H, (p,d,k,mean,H)
    assert var == (p**(d-2)-1)*(k-1), (p,d,k,var)
    return dict(sorted(counts.items()))


def mm(a,b,m):
    d=len(a)
    return tuple(tuple(sum(a[i][r]*b[r][j] for r in range(d))%m
                       for j in range(d)) for i in range(d))

def mpow(a,n,m):
    d=len(a)
    r=tuple(tuple(int(i==j) for j in range(d)) for i in range(d))
    while n:
        if n&1:r=mm(r,a,m)
        a=mm(a,a,m);n//=2
    return r

def verify_matrix(A,p,prime_divisors):
    d=len(A)
    L=sum(p**i for i in range(d))
    I=tuple(tuple(int(i==j) for j in range(d)) for i in range(d))
    assert mpow(A,L,p)==I
    assert all(mpow(A,L//q,p)!=I for q in prime_divisors)
    assert mpow(A,L,p*p)!=I
    W=mpow(A,L,p*p)
    B=tuple(tuple((W[i][j]-I[i][j])% (p*p)//p for j in range(d)) for i in range(d))
    assert any(B[i][j]%p for i in range(d) for j in range(d) if i!=j),B
    return B

A3=((0,1,0),(0,0,1),(1,1,0))
A5=((0,0,0,0,-2),(1,0,0,0,0),(0,1,0,0,0),(0,0,1,0,-2),(0,0,0,1,-2))
assert verify_matrix(A3,3,[13])==((2,1,0),(0,2,1),(1,1,2))
assert verify_matrix(A3,29,[13,67])
assert verify_matrix(A5,3,[11])
for k in range(1,5):
    hist=cycle_counts(3,3,k,lambda x,m:(x[1],x[2],(x[0]+x[1])%m))
    print('p=3,d=3,k=',k,'hist=',hist)
print('p=29,d=3,k=1:',cycle_counts(29,3,1,lambda x,m:(x[1],x[2],(x[0]+x[1])%m)))
for k in (1,2):
    hist=cycle_counts(3,5,k,lambda x,m:((-2*x[4])%m,x[0],x[1],(x[2]-2*x[4])%m,(x[3]-2*x[4])%m))
    print('p=3,d=5,k=',k,'hist=',hist)
print('VERIFY_OK')
