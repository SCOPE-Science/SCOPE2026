from fractions import Fraction as F

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def mat_add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mat_scale(A,c):
    return [[c*x for x in row] for row in A]

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def inv(A):
    n=len(A)
    M=[row[:] + eye(n)[i] for i,row in enumerate(A)]
    for col in range(n):
        piv=next(i for i in range(col,n) if M[i][col] != 0)
        M[col],M[piv]=M[piv],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for i in range(n):
            if i==col:
                continue
            q=M[i][col]
            if q:
                M[i]=[M[i][j]-q*M[col][j] for j in range(2*n)]
    return [row[n:] for row in M]

def row_sums(A):
    return [sum(row,F(0)) for row in A]

def cn(Q,h):
    n=len(Q)
    s=h/2
    I=eye(n)
    R=inv(mat_add(I,mat_scale(Q,-s)))
    C=mat_add(mat_scale(R,F(2)) , mat_scale(I,F(-1)))
    # direct Cayley product
    direct=matmul(R,mat_add(I,mat_scale(Q,s)))
    assert C==direct
    return R,C

def is_nonnegative(A):
    return all(x>=0 for row in A for x in row)

# Two-state exact family.
pairs=[(F(1),F(1)),(F(2),F(1)),(F(3,2),F(5,3)),(F(7,4),F(2,5))]
for a,b in pairs:
    Q=[[-a,a],[b,-b]]
    if a==b:
        for h in [F(0),F(1),F(10),F(1000)]:
            R,C=cn(Q,h)
            assert is_nonnegative(C)
            assert row_sums(C)==[F(1),F(1)]
    else:
        hstar=F(2)/abs(a-b)
        for h,sgn in [(hstar/2,1),(hstar,0),(hstar*2,-1)]:
            R,C=cn(Q,h)
            assert row_sums(R)==[F(1),F(1)]
            assert row_sums(C)==[F(1),F(1)]
            assert all(C[i][j]>=0 for i in range(2) for j in range(2) if i!=j)
            if sgn>=0:
                assert is_nonnegative(C)
            else:
                assert not is_nonnegative(C)
            # Exact criterion.
            assert is_nonnegative(C) == all(R[i][i] >= F(1,2) for i in range(2))

# Complete graph family.
for n in range(3,21):
    for c in [F(1),F(2,3),F(5,2)]:
        Q=[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(-(n-1)*c if i==j else c)
            Q.append(row)
        hstar=F(2,c*(n-2))
        for h,expect in [(hstar/2,1),(hstar,0),(hstar*2,-1)]:
            R,C=cn(Q,h)
            assert row_sums(R)==[F(1)]*n
            assert row_sums(C)==[F(1)]*n
            assert all(C[i][j]>=0 for i in range(n) for j in range(n) if i!=j)
            assert is_nonnegative(C) == all(R[i][i]>=F(1,2) for i in range(n))
            if expect>=0:
                assert is_nonnegative(C)
            else:
                assert not is_nonnegative(C)
            if expect==0:
                assert all(C[i][i]==0 for i in range(n))

# Nonuniform reversible rational examples.
# Construct q_ij = conductance_ij / pi_i with symmetric conductances.
examples=[
    ([F(1,6),F(1,3),F(1,2)],
     [[F(0),F(1,12),F(1,18)],[F(1,12),F(0),F(1,10)],[F(1,18),F(1,10),F(0)]]),
    ([F(1,10),F(3,10),F(6,10)],
     [[F(0),F(1,20),F(1,25)],[F(1,20),F(0),F(3,40)],[F(1,25),F(3,40),F(0)]])
]
for pi,cond in examples:
    n=len(pi)
    Q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                Q[i][j]=cond[i][j]/pi[i]
        Q[i][i]=-sum((Q[i][j] for j in range(n) if j!=i),F(0))
    # detailed balance
    for i in range(n):
        for j in range(n):
            assert pi[i]*Q[i][j] == pi[j]*Q[j][i]
    for h in [F(1,10),F(1),F(10)]:
        R,C=cn(Q,h)
        assert row_sums(R)==[F(1)]*n
        assert row_sums(C)==[F(1)]*n
        assert all(C[i][j]>=0 for i in range(n) for j in range(n) if i!=j)
        assert is_nonnegative(C) == all(R[i][i]>=F(1,2) for i in range(n))

print("VERIFY_OK")
