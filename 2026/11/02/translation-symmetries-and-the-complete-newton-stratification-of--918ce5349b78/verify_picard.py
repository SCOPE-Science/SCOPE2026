"""Exact finite-field and symbolic checks for characteristic-two cubic covers.
No external packages required; Python 3.9+.
"""
from itertools import product

IRREDUCIBLE = {1:0b11, 2:0b111, 3:0b1011, 4:0b10011}

def mul(a,b,m):
    modulus=IRREDUCIBLE[m]; top=1<<m; out=0
    while b:
        if b&1:out ^= a
        a <<= 1
        if a&top:a ^= modulus
        b >>= 1
    return out

def power(a,n,m):
    out=1
    while n:
        if n&1:out=mul(out,a,m)
        a=mul(a,a,m);n >>= 1
    return out

def discr(a,b,c,d,m):
    return mul(c,c,m)^mul(mul(a,b,m),c,m)^mul(mul(a,a,m),d,m)

def rank(M,m):
    a=[r[:] for r in M]; row=0
    for col in range(3):
        pivot=next((i for i in range(row,3) if a[i][col]),None)
        if pivot is None:continue
        a[pivot],a[row]=a[row],a[pivot]
        inv=power(a[row][col],(1<<m)-2,m)
        a[row]=[mul(inv,v,m) for v in a[row]]
        for i in range(3):
            if i!=row and a[i][col]:
                t=a[i][col]
                a[i]=[u^mul(t,v,m) for u,v in zip(a[i],a[row])]
        row +=1
    return row

def matmul(A,B,m):
    return [[mul(A[i][k],B[k][j],m)^mul(A[i][(k+1)%3],B[(k+1)%3][j],m)^mul(A[i][(k+2)%3],B[(k+2)%3][j],m) for j in range(3)] for i in range(3) for k in [0]]

def stable_rank(a,c,m):
    s=lambda x:power(x,1<<(m-1),m)
    M=[[0,0,s(c)],[0,0,s(a)],[0,1,0]]
    P=[[int(i==j) for j in range(3)] for i in range(3)]
    B=[r[:] for r in M]
    for _ in range(9):
        P=matmul(P,B,m)
        B=[[s(x) for x in row] for row in B]
    return rank(P,m),rank(M,m)

def points(cs,m):
    q=1<<m
    n=1
    freq=[0]*q
    for y in range(q):freq[power(y,3,m)]+=1
    for x in range(q):
        a,b,c,d=cs
        f=power(x,4,m)^mul(a,power(x,3,m),m)^mul(b,power(x,2,m),m)^mul(c,x,m)^d
        n+=freq[f]
    return n

for m in (1,2):
    q=1<<m; count={0:0,2:0}; nonsmooth=0
    for a,b,c,d in product(range(q),repeat=4):
        if discr(a,b,c,d,m)==0:
            nonsmooth+=1; continue
        p_rank,cartier_rank=stable_rank(a,c,m)
        assert cartier_rank==2 and p_rank==(0 if a==0 else 2)
        count[p_rank]+=1
    assert count == {0:q*q*(q-1),2:q*q*(q-1)*(q-1)}
    assert nonsmooth==q**4-q**3*(q-1)
    print('FIELD',q,'smooth_rank_distribution',count,'nonsmooth',nonsmooth)

# Verify quotient polynomial identities at every base-field parameter and root t.
for m in (1,2,3,4):
    q=1<<m
    total=0
    for b,c,t in product(range(q),repeat=3):
        if not c or not t or power(t,3,m)^mul(b,t,m)^c:continue
        alpha=b^mul(t,t,m)
        assert alpha==mul(c,power(t,q-2,m),m) and alpha!=0
        for x in range(q):
            u=mul(x,x,m)^mul(t,x,m)
            lhs=power(x,4,m)^mul(b,power(x,2,m),m)^mul(c,x,m)
            rhs=mul(u,u,m)^mul(alpha,u,m)
            assert lhs==rhs
        total+=1
    print('QUOTIENT_IDENTITY_FIELD',q,'admissible_(b,c,t)',total)

for coeff in [(0,0,1,0),(1,0,0,1),(1,0,1,1)]:
    n=[points(coeff,m) for m in (1,2,3,4)]
    c1=n[0]-3;c2=(n[1]-5+c1*c1)//2
    c3=(n[2]-9-c1**3+3*c1*c2)//3
    print('MODEL',coeff,'point_counts',n,'L_mod_2',(1,c1%2,c2%2,c3%2))
    assert (c1%2,c2%2,c3%2)==((0,0,0) if coeff[0]==0 else (0,1,0))
print('VERIFY_OK')
