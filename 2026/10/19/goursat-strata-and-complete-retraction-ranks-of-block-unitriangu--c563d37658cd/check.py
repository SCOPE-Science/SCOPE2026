"""Direct finite-field checks for the rank distribution of retracts of
nilpotent block-matrix algebras. Python 3 standard library only.
Run: python check.py
"""
from itertools import product, combinations
from math import prod
from collections import Counter

def add(a,b,q): return a^b if q==4 else (a+b)%q
def mul(a,b,q):
    if q!=4: return a*b%q
    t=0
    while b:
        if b&1:t^=a
        b>>=1; a<<=1
        if a&4:a^=7
    return t

def matmul(A,B,q):
    d=len(A)
    return [[reduce_add((mul(A[i][k],B[k][j],q) for k in range(d)),q) for j in range(d)] for i in range(d)]
def reduce_add(vals,q):
    z=0
    for v in vals:z=add(z,v,q)
    return z

def rank(A,q):
    A=[row[:] for row in A];m=len(A);n=len(A[0]) if m else 0;j=0
    for c in range(n):
        k=next((i for i in range(j,m) if A[i][c]),None)
        if k is None: continue
        A[j],A[k]=A[k],A[j]
        inv=next(i for i in range(1,q) if mul(i,A[j][c],q)==1)
        A[j]=[mul(v,inv,q) for v in A[j]]
        for i in range(m):
            if i!=j and A[i][c]:
                fac=A[i][c]
                A[i]=[add(x,-mul(fac,y,q)%q,q) if q!=4 else add(x,mul(fac,y,q),q) for x,y in zip(A[i],A[j])]
        j+=1
        if j==m:break
    return j

def binomq(n,r,q):
    if r<0 or r>n:return 0
    numer=prod(q**(n-i)-1 for i in range(r))
    denom=prod(q**(r-i)-1 for i in range(r))
    return numer//denom

def gl(t,q):return prod(q**t-q**i for i in range(t))
def H(n,q):
    out=Counter()
    for a in range(n+1):
        for b in range(n-a+1):
            for t in range(min(a,b)+1):
                out[a+b-t]+=binomq(n,a,q)*binomq(n-a,b,q)*binomq(a,t,q)*binomq(b,t,q)*gl(t,q)
    return out

def expected(n,q):
    return Counter({**{r:H(n,q)[r]*q**(r*(2*n-r+1)) for r in range(n+1)},2*n+1:1})

def basis_prods(n):
    d=2*n+1
    return [(i,n+i,d-1) for i in range(n)]

def raw(q,n):
    d=2*n+1;B=basis_prods(n);count=Counter()
    for vals in product(range(q),repeat=d*d):
        A=[list(vals[i*d:(i+1)*d]) for i in range(d)]
        if matmul(A,A,q)!=A:continue
        # column i is value of algebra basis element e_i
        good=True
        for i in range(d):
            for j in range(d):
                expected_product=next((k for x,y,k in B if (x,y)==(i,j)),None)
                z=reduce_add((mul(A[k][i],A[n+k][j],q) for k in range(n)),q)
                if expected_product is None:
                    if z!=0:good=False;break
                else:
                    if any(A[t][expected_product]!=(z if t==d-1 else 0) for t in range(d)):good=False;break
            if not good:break
        if good:count[rank(A,q)]+=1
    return count

def all_subspaces_q2(d):
    # Enumerate row spaces by unique reduced row echelon matrices.
    for r in range(d+1):
        for pivots in combinations(range(d),r):
            nonpiv=[c for c in range(d) if c not in pivots]
            free=[(i,c) for i,p in enumerate(pivots) for c in nonpiv if c>p]
            for mask in range(1<<len(free)):
                rows=[[0]*d for _ in range(r)]
                for i,p in enumerate(pivots):rows[i][p]=1
                for j,(i,c) in enumerate(free):rows[i][c]=(mask>>j)&1
                yield rows

def independent_subspace_counts(n):
    count=Counter()
    for rows in all_subspaces_q2(2*n):
        if all(sum(x[i]*y[n+i] for i in range(n))%2==0 for x in rows for y in rows):
            count[len(rows)]+=1
    return count

def projection_count_q2(n):
    # Directly enumerate quotient matrices, not subspaces or complements.
    d=2*n; total=Counter()
    for bits in range(1<<(d*d)):
        T=[[(bits>>(i*d+j))&1 for j in range(d)] for i in range(d)]
        if matmul(T,T,2)!=T:continue
        if any(sum(T[k][i]*T[n+k][j] for k in range(n))%2 for i in range(d) for j in range(d)):
            continue
        total[rank(T,2)]+=2**rank(T,2)
    total[2*n+1]+=1
    return total

if __name__=='__main__':
    for q in (2,3,4):
        got=raw(q,1);ex=expected(1,q)
        assert got==ex,(q,got,ex)
        print('RAW_MATRIX_CHECK',q,1,sorted(got.items()))
    for n in (1,2,3):
        got=independent_subspace_counts(n);ex=H(n,2)
        assert got==ex,(n,got,ex)
        print('SUBSPACE_RREF_CHECK',n,sorted(got.items()))
    got=projection_count_q2(2);ex=expected(2,2)
    assert got==ex,(got,ex)
    print('DIRECT_PROJECTION_CHECK',2,2,sorted(got.items()))
    for n in (2,3):
        print('PREDICTED_RETRACTION_RANKS',n,sorted(expected(n,2).items()))
    print('ALL_EXACT_CHECKS_PASSED')
