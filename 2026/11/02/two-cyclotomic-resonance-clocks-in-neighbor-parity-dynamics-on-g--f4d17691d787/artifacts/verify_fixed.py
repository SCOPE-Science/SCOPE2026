"""Independent polynomial-Smith verification of all-time periodic point census on GP(n,2)."""
from verify import adjacency, rank, mul

def pmul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1
        a<<=1
    return c

def pdivmod(a,b):
    assert b
    q=0
    db=b.bit_length()-1
    while a and a.bit_length()-1>=db:
        d=a.bit_length()-1-db
        q^=1<<d
        a^=b<<d
    return q,a

def pgcd(a,b):
    while b:
        _,r=pdivmod(a,b)
        a,b=b,r
    return a

def pdeg(a):return a.bit_length()-1

def mmul(a,b):
    return ((pmul(a[0],b[0]) ^pmul(a[1],b[2]),pmul(a[0],b[1]) ^pmul(a[1],b[3]),
             pmul(a[2],b[0]) ^pmul(a[3],b[2]),pmul(a[2],b[1]) ^pmul(a[3],b[3])))

def mpow(a,t):
    X=(1,0,0,1)
    while t:
        if t&1:X=mmul(X,a)
        t//=2
        if t:a=mmul(a,a)
    return X

def nullity_poly(n,t):
    z=1<<2
    B=((1<<3)^(1<<1),z,z,(1<<4)^1)
    H=list(mpow(B,t))
    H[0]^=1<<(2*t)
    H[3]^=1<<(2*t)
    d1=0
    for p in H:d1=pgcd(d1,p)
    det=pmul(H[0],H[3])^pmul(H[1],H[2])
    d2,r=pdivmod(det,d1)
    assert r==0
    poly=(1<<n)^1
    return pdeg(pgcd(poly,d1))+pdeg(pgcd(poly,d2))

def actual_nullity(n,t):
    A=adjacency(n)
    N=2*n
    X=[1<<i for i in range(N)]
    while t:
        if t&1:X=mul(X,A,N)
        t//=2
        if t:A=mul(A,A,N)
    X=[row^(1<<i) for i,row in enumerate(X)]
    return N-rank(X,N)

def verify():
    cases=0
    for n in range(5,31):
        for t in range(1,33):
            a=nullity_poly(n,t)
            b=actual_nullity(n,t)
            assert a==b,(n,t,a,b)
            cases+=1
    print('OK exact temporal fixed point counts',cases,'matrix/Smith pairs')
    for n in (5,6,10,15):
        print('n',n,'fixed exponent t=1..12',[nullity_poly(n,t) for t in range(1,13)])
if __name__=='__main__':verify()
