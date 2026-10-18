"""Independent finite-field matrix checks for truncated cyclic path-algebra Jordan census.
Usage: python nakayama_jordan_check.py
"""
from collections import Counter
from itertools import product
from random import Random

def rank(M,p):
    B=[row[:] for row in M]; r=0; nc=len(B[0]) if B else 0
    for c in range(nc):
        pivot=next((i for i in range(r,len(B)) if B[i][c]%p),None)
        if pivot is None: continue
        B[r],B[pivot]=B[pivot],B[r]
        inv=pow(B[r][c],-1,p)
        B[r]=[(v*inv)%p for v in B[r]]
        for i in range(len(B)):
            if i!=r and B[i][c]%p:
                fac=B[i][c]
                B[i]=[(x-fac*y)%p for x,y in zip(B[i],B[r])]
        r+=1
        if r==len(B):break
    return r

def mult(M,N,p):
    d=len(M); return [[sum(M[i][k]*N[k][j] for k in range(d))%p for j in range(d)] for i in range(d)]

def leftmatrix(n,p,x,y):
    basis=[(v,l) for l in range(3) for v in range(n)]
    idx={a:i for i,a in enumerate(basis)}
    M=[[0]*(3*n) for _ in range(3*n)]
    coeff={(i,1):x[i] for i in range(n)}
    coeff.update({(i,2):y[i] for i in range(n)})
    for (i,l), val in coeff.items():
        if not val: continue
        for col,(j,m) in enumerate(basis):
            if (i+l)%n == j and l+m<3:
                M[idx[(i,l+m)]][col] = (M[idx[(i,l+m)]][col]+val)%p
    return M

def add(A,B):
    C=Counter(A)
    for k,v in B.items(): C[k]+=v
    return C

def mulpoly(A,B):
    C=Counter()
    for (a,b,c),x in A.items():
        for (d,e,f),y in B.items(): C[(a+d,b+e,c+f)]+=x*y
    return C

def poly_matmul(A,B):
    C=[[Counter() for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2): C[i][j]=add(C[i][j],mulpoly(A[i][k],B[k][j]))
    return C

def transfer_counts(n,q):
    # U exponent = #3-blocks; V = #2-blocks; W = #trivial 3-blocks
    M=[[{(0,0,1):1,(0,1,0):q-1},{(0,1,0):q}],
       [{(0,1,0):q*(q-1)},{(1,0,0):q*(q-1)}]]
    I=[[{(0,0,0):1},{}],[{},{(0,0,0):1}]]
    for _ in range(n): I=poly_matmul(I,M)
    return add(I[0][0],I[1][1])

def direct_counts(n,q,limit=None):
    C=Counter(); num=0
    itr=product(range(q),repeat=2*n)
    for vals in itr:
        x=vals[:n]; y=vals[n:]
        M=leftmatrix(n,q,x,y)
        r=rank(M,q); s=rank(mult(M,M,q),q)
        a=s; b=r-2*s; c=n-a-b
        assert min(a,b,c)>=0 and a+b+c==n,(vals,r,s)
        # Check higher nilpotency and block restriction directly.
        if num<10: assert not any(any(row) for row in mult(mult(M,M,q),M,q))
        C[(a,b,c)]+=1;num+=1
        if limit and num>=limit:break
    return C,num

def full():
    for q,n in [(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)]:
        got,count=direct_counts(n,q)
        exp=transfer_counts(n,q)
        assert got==exp,(q,n,got,exp)
        assert count==q**(2*n)==sum(exp.values())
        print('full',q,n,count, sorted(got.items()))
    rng=Random(20261017)
    for q,n in [(5,3),(5,4),(7,3),(3,7)]:
        for _ in range(256):
            x=[rng.randrange(q) for _ in range(n)]
            y=[rng.randrange(q) for _ in range(n)]
            M=leftmatrix(n,q,x,y)
            r=rank(M,q); s=rank(mult(M,M,q),q)
            a=sum(x[i]!=0 and x[(i+1)%n]!=0 for i in range(n))
            c=sum(x[i]==0 and x[(i+1)%n]==0 and y[i]==0 for i in range(n))
            b=n-a-c
            assert (r,s)==(2*a+b,a),(q,n,x,y,r,s,a,b,c)
        print('sampled',q,n,256)
    print('ALL_TRUNCATED_CYCLIC_JORDAN_CHECKS_PASSED')
if __name__=='__main__':full()
