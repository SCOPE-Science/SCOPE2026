from fractions import Fraction

n=3
zero=(Fraction(0),)*n
e2=(Fraction(0),Fraction(1),Fraction(0))

def table(pairs):
    return {(i,j):(e2 if (i,j) in pairs else zero) for i in range(n) for j in range(n)}

prec=table({(0,0),(0,2),(2,0)})
succ=table({(0,2),(2,0),(2,2)})
vee =table({(0,0),(0,2),(2,2)})
ops=[prec,succ,vee]
basis=[tuple(Fraction(int(i==j)) for i in range(n)) for j in range(n)]

def add(*vs):
    return tuple(sum(v[k] for v in vs) for k in range(n))

def smul(a,v):
    return tuple(a*x for x in v)

def prod(op,x,y):
    out=[Fraction(0) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if x[i] and y[j]:
                z=op[(i,j)]
                for k in range(n):
                    out[k]+=x[i]*y[j]*z[k]
    return tuple(out)

# Check the printed DT_3^1 table really satisfies all seven tridendriform identities.
for x in basis:
    for y in basis:
        for z in basis:
            yz_star=add(prod(prec,y,z),prod(succ,y,z),prod(vee,y,z))
            xy_star=add(prod(prec,x,y),prod(succ,x,y),prod(vee,x,y))
            checks=[
                (prod(prec,prod(prec,x,y),z),prod(prec,x,yz_star)),
                (prod(prec,prod(succ,x,y),z),prod(succ,x,prod(prec,y,z))),
                (prod(succ,xy_star,z),prod(succ,x,prod(succ,y,z))),
                (prod(vee,prod(succ,x,y),z),prod(succ,x,prod(vee,y,z))),
                (prod(vee,prod(prec,x,y),z),prod(vee,x,prod(succ,y,z))),
                (prod(prec,prod(vee,x,y),z),prod(vee,x,prod(prec,y,z))),
                (prod(vee,prod(vee,x,y),z),prod(vee,x,prod(vee,y,z))),
            ]
            assert all(a==b for a,b in checks)

# Matrices act on column vectors. Flatten variables row-major.
def matvec(M,x):
    return tuple(sum(M[r][c]*x[c] for c in range(n)) for r in range(n))

def basis_matrix(r,c):
    M=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    M[r][c]=Fraction(1)
    return tuple(tuple(row) for row in M)

matrix_basis=[basis_matrix(r,c) for r in range(n) for c in range(n)]

# Build homogeneous linear constraints by evaluating the derivation defect
# for each variable basis matrix, operation, ordered input pair, and output coordinate.
rows=[]
for op in ops:
    for x in basis:
        for y in basis:
            coeffs_by_var=[]
            xy=prod(op,x,y)
            for M in matrix_basis:
                defect=add(matvec(M,xy),smul(-1,prod(op,matvec(M,x),y)),smul(-1,prod(op,x,matvec(M,y))))
                coeffs_by_var.append(defect)
            for k in range(n):
                row=[coeffs_by_var[j][k] for j in range(n*n)]
                if any(row): rows.append(row)

def rank(A):
    A=[row[:] for row in A]
    r=0
    cols=len(A[0]) if A else 0
    for c in range(cols):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        p=A[r][c]
        A[r]=[x/p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(cols)]
        r+=1
        if r==len(A): break
    return r

rk=rank(rows)
assert rk==6
assert 9-rk==3

def is_derivation(M):
    for op in ops:
        for x in basis:
            for y in basis:
                lhs=matvec(M,prod(op,x,y))
                rhs=add(prod(op,matvec(M,x),y),prod(op,x,matvec(M,y)))
                if lhs!=rhs: return False
    return True

H=((Fraction(1),0,0),(0,Fraction(2),0),(0,0,Fraction(1)))
U=((0,0,0),(Fraction(1),0,0),(0,0,0))
V=((0,0,0),(0,0,Fraction(1)),(0,0,0))
assert is_derivation(H) and is_derivation(U) and is_derivation(V)

# Linear independence of H,U,V plus nullity three proves they span the entire kernel.
def flatten(M): return tuple(M[r][c] for r in range(n) for c in range(n))
assert rank([list(flatten(H)),list(flatten(U)),list(flatten(V))])==3

def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)) for i in range(n))
def matsub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(n)) for i in range(n))
def comm(A,B): return matsub(matmul(A,B),matmul(B,A))
assert comm(H,U)==U
assert comm(H,V)==V
assert comm(U,V)==tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))

print({'constraint_rank':rk,'derivation_dimension':9-rk})
print('VERIFY_OK')
