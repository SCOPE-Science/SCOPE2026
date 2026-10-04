from math import gcd

def factor(n):
    out=[]
    m=n
    p=2
    while p*p<=m:
        if m%p==0:
            a=0
            while m%p==0:
                m//=p
                a+=1
            out.append((p,a))
        p+=1
    if m>1:
        out.append((m,1))
    return out

def formula(n):
    fac=factor(n)
    T=1
    S=1
    for p,a in fac:
        T*=p**(a-1)*((a+1)*p-a)
        S*=p**(a//2)
    E=(T-S)//2
    W=n*(n-1)-E
    return T,S,E,W

def brute(n):
    E=0
    for x in range(n):
        for y in range(x+1,n):
            if (x*y)%n==0:
                E+=1
    W=n*(n-1)-E
    return E,W

for n in range(2,301):
    T,S,E,W=formula(n)
    Eb,Wb=brute(n)
    assert E==Eb, (n,E,Eb)
    assert W==Wb, (n,W,Wb)
    assert T==sum(gcd(x,n) for x in range(n))
    assert S==sum(1 for x in range(n) if (x*x)%n==0)

# Published 2024 special-case formulas.
primes=[2,3,5,7,11]
for p in primes:
    n=p*p
    W=formula(n)[3]
    assert W==p*(p-1)*(2*p*p+2*p-3)//2
    n=p**3
    W=formula(n)[3]
    assert W==p*(p-1)*(2*p**4+2*p**3+2*p**2-4*p-1)//2

for p in [2,3,5,7]:
    for q in [3,5,7,11]:
        if p==q:
            continue
        n=p*q
        W=formula(n)[3]
        assert W==p*p*q*q-3*p*q+p+q
        n=p*p*q
        W=formula(n)[3]
        rhs=(2*p**4*q**2-8*p**2*q+3*p**2+4*p*q-p)//2
        assert W==rhs, (p,q,W,rhs)
        n=p*p*q*q
        W=formula(n)[3]
        rhs=(2*p**4*q**4-11*p**2*q**2+6*p**2*q+6*p*q**2-3*p*q)//2
        assert W==rhs, (p,q,W,rhs)

for p,q,r in [(2,3,5),(2,3,7),(3,5,7),(3,5,11)]:
    n=p*q*r
    W=formula(n)[3]
    rhs=p*p*q*q*r*r-5*p*q*r+2*(p*q+p*r+q*r)-(p+q+r)+1
    assert W==rhs, (p,q,r,W,rhs)

print("VERIFY_OK")
