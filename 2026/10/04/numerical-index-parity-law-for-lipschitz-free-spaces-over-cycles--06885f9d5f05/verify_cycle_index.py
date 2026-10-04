from fractions import Fraction
from itertools import combinations, product

def ext_dual(n):
    if n % 2 == 0:
        k=n//2; out=[]
        for P in combinations(range(n),k):
            P=set(P); out.append(tuple(1 if i in P else -1 for i in range(n)))
        return out
    k=(n-1)//2; out=[]
    for z in range(n):
        rem=[i for i in range(n) if i!=z]
        for P0 in combinations(rem,k):
            P=set(P0); out.append(tuple(0 if i==z else (1 if i in P else -1) for i in range(n)))
    return out

def qnorm(a):
    s=sorted(a); n=len(a)
    if n%2: t=s[n//2]
    else: t=(s[n//2-1]+s[n//2])/2
    return sum(abs(x-t) for x in a)

def ci(a,i):
    return max(abs(sum(x*y for x,y in zip(a,h))) for h in ext_dual(len(a)) if h[i]==1)

def witness_row(n,i):
    assert n%2==1
    k=(n-1)//2; d=Fraction(1,n-1)
    w=[0]+[1]*k+[-1]*k
    return [d*w[(j-i)%n] for j in range(n)]

for n in range(6,11):
    E=ext_dual(n)
    if n%2==0:
        assert all(all(abs(x)==1 for x in h) for h in E)
    else:
        alpha=Fraction(n-2,n-1)
        rows=[witness_row(n,i) for i in range(n)]
        assert all(qnorm(r)==1 and ci(r,i)==alpha for i,r in enumerate(rows))
        assert all(sum(rows[i][j] for i in range(n))==0 for j in range(n))
print('WITNESS_OK n=6..10')

# finite stress test of the lower inequality at n=7 on all {-1,0,1}^7 representatives
n=7; alpha=Fraction(n-2,n-1)
for a0 in product([-1,0,1], repeat=n):
    a=tuple(Fraction(x) for x in a0); N=qnorm(a)
    if N==0: continue
    for i in range(n):
        assert ci(a,i) >= alpha*N
print('LOWER_STRESS_OK n=7 coefficients={-1,0,1}')
