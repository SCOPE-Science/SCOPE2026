"""Reproduce exact bounded-morphism counts for reflexive crown posets. No external dependencies."""
from itertools import product
from math import comb

def crown_relation(m):
    # minima 0..m-1, maxima m..2m-1, x_i<y_i and x_i<y_{i-1}
    N=2*m
    r=[[i==j for j in range(N)] for i in range(N)]
    for i in range(m):
        r[i][m+i]=True
        r[i][m+(i-1)%m]=True
    return r

def brute(n,m):
    S=crown_relation(n); T=crown_relation(m)
    srcup=[{j for j in range(2*n) if S[i][j]} for i in range(2*n)]
    tarup=[{j for j in range(2*m) if T[i][j]} for i in range(2*m)]
    # Surjective bounded morphism iff f(srcup[i]) = tarup[f(i)] and f onto.
    c=0
    for f in product(range(2*m),repeat=2*n):
        if len(set(f))<2*m: continue
        if all({f[j] for j in srcup[i]}==tarup[f[i]] for i in range(2*n)):
            c+=1
    return c

def walks(n,m):
    out=0
    for w in product(range(m),repeat=n):
        edges=set();good=True
        for i in range(n):
            x=w[i];y=w[(i+1)%n]
            if x==y: continue
            if (y-x)%m not in (1,m-1):good=False;break
            edges.add(tuple(sorted((x,y))))
        if good and len(edges)==m:out+=1
    return out

def matmul(A,B):
    z=len(A);return [[sum(A[i][k]*B[k][j] for k in range(z)) for j in range(z)] for i in range(z)]

def matrixpow(A,n):
    z=len(A); result=[[int(i==j) for j in range(z)] for i in range(z)]
    while n:
        if n&1:result=matmul(result,A)
        A=matmul(A,A);n//=2
    return result

def formula(n,m):
    E=[(i,(i+1)%m) for i in range(m)]
    ans=0
    for mask in range(1<<m):
        A=[[int(i==j) for j in range(m)] for i in range(m)]
        for k,(i,j) in enumerate(E):
            if (mask>>k)&1: A[i][j]=A[j][i]=1
        ans+=(-1)**(m-mask.bit_count())*sum(matrixpow(A,n)[i][i] for i in range(m))
    return ans

def trinomial_coef(n,r):
    # coefficient z^r of (z^-1+1+z)^n
    return sum(comb(n,p)*comb(n-p,p-r) for p in range(r,n+1) if 0<=p-r<=n-p)

if __name__=='__main__':
    checked=[]
    for m in range(3,6):
        for n in range(1,10):
            v=walks(n,m)
            f=formula(n,m)
            assert v==f,(n,m,v,f)
            if n<m:assert f==0
            if m<=n<2*m:assert f==2*m*trinomial_coef(n,m),(n,m,f)
            if n==2*m:
                assert f==2*m*(trinomial_coef(n,m)+trinomial_coef(n,2*m))+2*m*m,(n,m,f)
            checked.append((n,m,f))
    for n,m in [(1,3),(2,3),(3,3),(4,3),(2,4),(3,4)]:
        b=brute(n,m); assert b==formula(n,m),(n,m,b,formula(n,m))
    for n in range(2,6):
        target=3**n+(-1)**n-2**(n+1)+2
        assert brute(n,2)==target,(n,brute(n,2),target)
    for n in range(2,13):
        edge_sum=2*sum(comb(n,q)*(2**q-2) for q in range(2,n+1,2))
        assert edge_sum==3**n+(-1)**n-2**(n+1)+2
    print('PASS',len(checked),'matrix-vs-walk comparisons, 10 direct Kripke enumerations, 11 boundary formula checks')
    print('Counts by m and n:')
    for m in range(3,6): print('m=',m,[(n,formula(n,m)) for n in range(m,2*m+2)])
