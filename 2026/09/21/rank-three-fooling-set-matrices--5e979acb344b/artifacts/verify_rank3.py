from itertools import combinations

# Exact integer arithmetic utilities.
def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def det3(X):
    return (X[0][0]*(X[1][1]*X[2][2]-X[1][2]*X[2][1])
            -X[0][1]*(X[1][0]*X[2][2]-X[1][2]*X[2][0])
            +X[0][2]*(X[1][0]*X[2][1]-X[1][1]*X[2][0]))

def fooling(M, mod=None):
    n=len(M)
    val=lambda x: x if mod is None else x%mod
    return all(val(M[i][i]) != 0 for i in range(n)) and all(
        val(M[i][j])*val(M[j][i]) == 0 for i in range(n) for j in range(i+1,n))

def rank_mod(M,p):
    A=[[x%p for x in row] for row in M]
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

M3=[[1,0,1],[1,1,0],[0,-1,1]]
assert fooling(M3)
assert det3(M3)==0
assert M3[0][0]*M3[1][1]-M3[0][1]*M3[1][0] == 1

C=[
[ 1,1,0],
[ 0,1,0],
[-1,1,1],
[-1,0,1],
[ 1,0,0],
[ 0,1,1],
]
D=[
[1,0,0, 1, 1,1],
[0,1,0,-1,-1,0],
[0,0,1, 2, 1,1],
]
M6=[
[ 1, 1, 0, 0, 0, 1],
[ 0, 1, 0,-1,-1, 0],
[-1, 1, 1, 0,-1, 0],
[-1, 0, 1, 1, 0, 0],
[ 1, 0, 0, 1, 1, 1],
[ 0, 1, 1, 1, 0, 1],
]
assert matmul(C,D)==M6
assert fooling(M6)
assert det3(C[:3])==1
assert det3([row[:3] for row in D])==1
# Hence rank(M6)=3 over every field: factorization gives <=3 and the leading 3x3 minor of M6 is 1.
assert det3([row[:3] for row in M6])==1

U=[
[0,0,1],
[0,1,0],
[0,1,1],
[1,0,0],
[1,0,1],
[1,1,0],
[1,1,1],
]
V=[
[0,0,1],
[0,1,1],
[1,1,0],
[1,1,1],
[1,0,0],
[1,0,1],
[0,1,0],
]
M7=[[x%2 for x in row] for row in matmul(U, [list(col) for col in zip(*V)])]
M7_expected=[
[1,1,0,1,0,1,0],
[0,1,1,1,0,0,1],
[1,0,1,0,0,1,1],
[0,0,1,1,1,1,0],
[1,1,1,0,1,0,0],
[0,1,0,0,1,1,1],
[1,0,0,1,1,0,1],
]
assert M7==M7_expected
assert fooling(M7,2)
assert rank_mod(M7,2)==3
minor=[[M7[i][j] for j in (0,1,2)] for i in (0,1,3)]
assert det3(minor)%2==1

# Coordinate obstruction for an embedded Fano plane in P^2(F):
p3=[1,1,0]; p5=[1,0,1]; p6=[0,1,1]
fano_det=det3([p3,p5,p6])
assert fano_det==-2

print('M3: fooling=yes, rank=2 over every field (unit 2x2 minor; determinant 0)')
print('M6: fooling=yes, rank=3 over every field (integer factorization plus unit 3x3 minor)')
print('M7 over F2: fooling=yes, rank=3, factorization U V^T verified')
print('Fano final-line determinant:', fano_det)
print('verified=rank3_fooling_set_low_rank_constructions')
