from itertools import product
P=3

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P for j in range(len(B[0]))] for i in range(len(A))]
def add(A,B):
    return [[(A[i][j]+B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def eq(A,B): return A==B
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def zero(m,n): return [[0]*n for _ in range(m)]
def rank(A):
    M=[row[:] for row in A]; m=len(M); n=len(M[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if M[i][c]%P),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c],-1,P)
        M[r]=[(x*inv)%P for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]%P:
                a=M[i][c]%P
                M[i]=[(M[i][j]-a*M[r][j])%P for j in range(n)]
        r+=1
    return r

def mat(vals,m,n):
    it=iter(vals); return [[next(it) for _ in range(n)] for _ in range(m)]
def blockdiag(A,B):
    m=len(A); n=len(B)
    C=zero(m+n,m+n)
    for i in range(m):
        for j in range(m): C[i][j]=A[i][j]
    for i in range(n):
        for j in range(n): C[m+i][m+j]=B[i][j]
    return C

n,k=5,2
A=blockdiag(eye(3),zero(2,2))
E=[[0,0],[0,0],[0,0],[1,0],[0,1]]
F=[[0,0,0,1,0],[0,0,0,0,1]]
X=[row[:] for row in E]
G=blockdiag(eye(3),zero(2,2))
Y=[row[:] for row in F]
T1=add(A,mm(E,F))
assert T1==eye(n)
count=0
for vals in product(range(P), repeat=4):
    D=mat(vals,2,2)
    TD=add(A,mm(mm(E,D),F))
    # factorization and rank-defect transfer
    DI=add(D, [[-1%P,0],[0,-1%P]])
    JD=add(eye(n),mm(mm(X,DI),F))
    assert TD==mm(T1,JD)
    assert rank(TD)==n-k+rank(D)
    # find a reflexive generalized inverse H for D and transfer it
    Hfound=None
    for hvals in product(range(P), repeat=4):
        H=mat(hvals,2,2)
        if mm(mm(D,H),D)==D and mm(mm(H,D),H)==H:
            Hfound=H; break
    assert Hfound is not None
    H=Hfound
    S=add(G,mm(mm(X,H),Y))
    assert mm(mm(TD,S),TD)==TD
    assert mm(mm(S,TD),S)==S
    # converse: F S E is an inner inverse of D
    H2=mm(mm(F,S),E)
    assert mm(mm(D,H2),D)==D
    count+=1
print(f'field=F_{P}')
print(f'checked_D={count}')
print('factorization_ok=true')
print('rank_transfer_ok=true')
print('reflexive_inverse_transfer_ok=true')
print('converse_inner_inverse_ok=true')
print('CHECK_OK')
