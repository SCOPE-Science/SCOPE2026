from math import comb,gcd

def factor_series(e,N):
    a=[0]*(N+1); a[0]=1
    for k in range(1,N+1):
        f=[0]*(N+1)
        if e>=0:
            for j in range(0,N//k+1):
                f[j*k]=comb(e+j-1,j) if e>0 else (1 if j==0 else 0)
        else:
            m=-e
            for j in range(0,min(m,N//k)+1):
                f[j*k]=(-1)**j*comb(m,j)
        b=[0]*(N+1)
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(f[:N+1-i]):
                    if y: b[i+j]+=x*y
        a=b
    return a

def sigma1(n):
    return sum(d for d in range(1,n+1) if n%d==0)

EVALUES=[-12,-6,-4,3,4,6,8,9,12,18,24,30]
N=120
checks=0
for e in EVALUES:
    a=factor_series(e,N)
    for n in range(1,N+1):
        if e==0:
            assert a[n]==0
        else:
            d=abs(e)//gcd(abs(e),n)
            assert a[n]%d==0, (e,n,a[n],d)
        rhs=e*sum(sigma1(j)*a[n-j] for j in range(1,n+1))
        assert n*a[n]==rhs, (e,n,n*a[n],rhs)
        checks+=2

# named examples
k3=factor_series(24,80)
for n in range(1,81):
    assert k3[n]%(24//gcd(24,n))==0
p2=factor_series(3,80)
for n in range(1,81):
    assert p2[n]%(3//gcd(3,n))==0

print('VERIFY_OK')
print('independent_product_and_recurrence_checks',checks)
print('k3_first_12',k3[1:13])
print('p2_first_12',p2[1:13])
