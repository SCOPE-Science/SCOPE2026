from math import gcd, isqrt
from fractions import Fraction


def is_squarefree(n):
    p=2
    while p*p<=n:
        if n%(p*p)==0:
            return False
        p+=1
    return True


def descending(a,b):
    # well-formed sorted P(1,a,b): descending one-step mutation replaces b
    return b>=a+2 and ((a+1)*(a+1))%b==0


def brute(N):
    return sum(descending(a,b) for b in range(1,N+1) for a in range(1,b+1) if gcd(a,b)==1)


def divisor_count(N):
    tot=0
    for n in range(2,N):
        for d in range(n+1,N+1):
            if n*n%d==0:
                tot+=1
    return tot


def squarefree_count(N):
    tot=0
    for s in range(1,N+1):
        if is_squarefree(s):
            q=isqrt(N//s)
            tot += q*(q-1)//2
    return tot


def wf_count(N):
    return sum(1 for b in range(1,N+1) for a in range(1,b+1) if gcd(a,b)==1)

for N in list(range(2,80))+[100,200,500]:
    b=brute(N); d=divisor_count(N); s=squarefree_count(N)
    assert b==d==s,(N,b,d,s)

# test local descent comparison by direct height transformation wherever each mutation exists
for N in range(2,120):
    for b in range(1,N+1):
        for a in range(1,b+1):
            if gcd(a,b)!=1: continue
            h=1+a+b
            downs=[]
            # replace 1: always T since 1 divides; target (a+b)^2
            downs.append((a+b+(a+b)**2) < h)
            # replace a if allowed
            if (1+b)**2 % a == 0:
                downs.append(1+b+(1+b)**2//a < h)
            # replace b if allowed
            if (1+a)**2 % b == 0:
                downs.append(1+a+(1+a)**2//b < h)
            assert any(downs)==descending(a,b),(a,b,downs)

vals=[]
for N in [100,300,1000,3000,10000]:
    D=squarefree_count(N)
    W=wf_count(N) if N<=3000 else None
    vals.append((N,D,W))
print('VERIFY_OK')
print(vals)
