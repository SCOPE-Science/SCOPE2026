from fractions import Fraction
from math import comb, sqrt, pi, e

def q(n,k,j):
    return Fraction(j*(j-1),1)-Fraction(2*(k-1)**2*j,n-2)+Fraction(k*k*(k-1)**2,(n-1)*(n-2))

def scale(n,k):
    return Fraction(n*(n-3)*(n-2)*(n-1),2*k*(k-1)*(n-k)*(n-k-1))

def w(n,k,j):
    if j<0 or j>k: return 0
    return comb(k,j)*comb(n-k,k-j)

def F(n,k,j):
    if j<0 or j>k: return 0
    return (k-j)**2*((n-2)*j-(k-1)**2)*w(n,k,j)

cases=0
for n in range(4,121):
    for k in range(2,n//2+1):
        N=comb(n,k); A=scale(n,k); d2=n*(n-3)//2; D=(n-1)*(n-2)
        vals=[q(n,k,j) for j in range(k+1)]
        assert vals[0]>0 and vals[-1]>0 and any(v<0 for v in vals)
        neg=[j for j,v in enumerate(vals) if v<0]
        assert neg==list(range(min(neg),max(neg)+1))
        a=min(neg)-1; b=max(neg)
        for j in range(k+1):
            assert D*q(n,k,j)*w(n,k,j)==F(n,k,j-1)-F(n,k,j)
        mean=sum(A*q(n,k,j)*w(n,k,j) for j in range(k+1))/N
        sq=sum((A*q(n,k,j))**2*w(n,k,j) for j in range(k+1))/N
        assert mean==0 and sq==d2 and A*q(n,k,k)==d2
        brute=sum(abs(A*q(n,k,j))*w(n,k,j) for j in range(k+1))/N
        boundary=Fraction(n*(n-3)*(F(n,k,b)-F(n,k,a)),k*(k-1)*(n-k)*(n-k-1)*N)
        assert brute==boundary
        cases+=1

def norm_float(n,k):
    N=comb(n,k); A=float(scale(n,k))
    return sum(abs(A*float(q(n,k,j)))*w(n,k,j) for j in range(k+1))/N

target=sqrt(2/(pi*e))
checks=[]
for rho in (0.2,1/3,0.5):
    n=600
    k=max(2,min(n//2,round(rho*n)))
    checks.append((rho,norm_float(n,k)/n))
print('VERIFY_OK exact_cases=%d target=%.12f bulk=%s' % (cases,target,','.join('%.3f:%.12f'%x for x in checks)))
