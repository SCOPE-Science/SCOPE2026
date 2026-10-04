from itertools import combinations

# Part I: exact order-8 combinatorial core.
points=range(7)
triples=[frozenset(c) for c in combinations(points,3)]
families=[]
def dfs(chosen,start):
    if len(chosen)==7:
        families.append(tuple(chosen)); return
    for i in range(start,len(triples)):
        t=triples[i]
        if all(len(t & s)==1 for s in chosen):
            dfs(chosen+[t],i+1)
dfs([],0)
assert len(families)==30

def row(C):
    return (1,)+tuple(1 if j in C else -1 for j in points)
def mul(a,b):
    return tuple(x*y for x,y in zip(a,b))
for fam in families:
    R={(1,)*8}|{row(C) for C in fam}
    assert len(R)==8
    assert all(sum(x*y for x,y in zip(a,b))==(8 if a==b else 0) for a in R for b in R)
    assert all(mul(a,b) in R for a in R for b in R)

# Part II: independent order-12 Paley witness.
q=11
residues={x*x % q for x in range(1,q)}
def chi(a):
    a%=q
    if a==0: return 0
    return 1 if a in residues else -1
H=[[1]*12 for _ in range(12)]
for i in range(q):
    for j in range(q):
        H[i+1][j+1]=chi(i-j)-(1 if i==j else 0)
for i in range(12):
    for j in range(12):
        dot=sum(H[i][k]*H[j][k] for k in range(12))
        assert dot==(12 if i==j else 0)
M=[[1 if H[i][j]==-1 else 0 for j in range(12)] for i in range(12)]
assert all(v==0 for v in M[0]) and all(M[i][0]==0 for i in range(12))

def rref_rank_pivots(A):
    A=[r[:] for r in A]; m=len(A); n=len(A[0]); r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    return r,piv
rank,pivcols=rref_rank_pivots(M)
assert rank==10
C=[[M[i][c] for c in pivcols] for i in range(12)]
# Solve C x = each column of M by Gauss-Jordan on augmented matrices.
def solve(C,b):
    A=[C[i][:]+[b[i]] for i in range(len(C))]
    m=len(A); n=len(C[0]); r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        assert p is not None
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
    for i in range(r,m): assert not A[i][-1]
    x=[0]*n
    for i,c in enumerate(piv): x[c]=A[i][-1]
    return x
R=[]
for j in range(12):
    b=[M[i][j] for i in range(12)]
    R.append(solve(C,b))
# R currently stores coefficient column-vectors; B rows are those vectors.
B=R
A=C
for i in range(12):
    for j in range(12):
        assert sum(A[i][k]*B[j][k] for k in range(10))%2==M[i][j]
assert len({tuple(x) for x in A})==12
assert len({tuple(x) for x in B})==12
assert 1024 % 12 != 0
print('STS7_LABELED_COUNT=30')
print('PALEY12_BINARY_RANK=10')
print('SPECTRAL_PAIR_SIZE=12 DIMENSION=10')
print('VERIFY_OK')
