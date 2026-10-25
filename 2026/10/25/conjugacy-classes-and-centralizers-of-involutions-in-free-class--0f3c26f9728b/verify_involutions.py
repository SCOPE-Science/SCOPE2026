"""Direct finite-field matrix check of order-two automorphisms (prime fields only)."""
from itertools import product
from math import comb, prod

def rank(A,p):
    if not A:return 0
    a=[list(map(lambda x:x%p,row)) for row in A];h=len(a);w=len(a[0]);k=0
    for j in range(w):
        z=next((i for i in range(k,h) if a[i][j]),None)
        if z is None:continue
        a[k],a[z]=a[z],a[k];u=pow(a[k][j],-1,p)
        a[k]=[(u*x)%p for x in a[k]]
        for i in range(h):
            if i!=k and a[i][j]:
                t=a[i][j];a[i]=[(x-t*y)%p for x,y in zip(a[i],a[k])]
        k+=1
        if k==h:break
    return k

def gauss(n,k,q):
    return prod((q**(n-j)-1)//1 for j in range(k))//prod((q**(k-j)-1) for j in range(k))

def gl(n,q):
    return prod(q**n-q**j for j in range(n))

def direct(n,p):
    pairs=list((i,j) for i in range(n) for j in range(i+1,n));m=len(pairs);tot={r:0 for r in range(n+1)}
    tested=0
    for nums in product(range(p),repeat=n*n):
        a=[nums[i*n:(i+1)*n] for i in range(n)]
        if rank(a,p)!=n:continue
        A2=[[sum(a[i][k]*a[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]
        if any(A2[i][j]!=(i==j) for i in range(n) for j in range(n)):continue
        r=n-rank([[a[i][j]-(i==j) for j in range(n)] for i in range(n)],p)
        w=[[ (a[i][u]*a[j][v]-a[i][v]*a[j][u])%p for u,v in pairs] for i,j in pairs]
        # action on a central map f: f*A + wedge(A)*f, indexed (center row, V column)
        h=m*n; M=[[0]*h for _ in range(h)]
        for ci in range(m):
            for j in range(n):
                row=ci*n+j
                for ck in range(m):
                    for k in range(n):
                        col=ck*n+k
                        M[row][col]=((a[k][j] if ci==ck else 0)+(w[ci][ck] if j==k else 0))%p
        nullity=h-rank(M,p)
        tot[r]+=p**nullity
        tested+=1
    exp={}
    for r in range(n+1):
        t=n-r;m0=comb(r,2)+comb(t,2);m1=r*t
        exp[r]=gauss(n,r,p)*p**(r*t+r*m1+t*m0)
    print('n',n,'q',p,'involutive_matrices',tested,'direct',tot,'predicted',exp)
    assert tot==exp
    if n==3 and p==3:
        # Check centralizer/class-size identity for all r.
        for r in range(n+1):
            t=n-r;m0=comb(r,2)+comb(t,2);m1=r*t
            c=gl(r,p)*gl(t,p)*p**(r*m0+t*m1)
            g=gl(n,p)*p**(n*comb(n,2))
            assert g//c==tot[r] and g%c==0

for args in [(2,3),(2,5),(3,3)]:direct(*args)
print('ALL_INVOLUTION_CHECKS_OK')
