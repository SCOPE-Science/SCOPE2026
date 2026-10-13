# Exact checker for the Hom-Leibniz algebra [e2,e2]=e1.

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def scale(s,x): return (s*x[0],s*x[1])

def bracket(x,y):
    # Only [e2,e2]=e1.
    return (x[1]*y[1],0)

def mat_vec(M,x):
    return (M[0][0]*x[0]+M[0][1]*x[1],
            M[1][0]*x[0]+M[1][1]*x[1])

def mat_mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))

def mat_sub(A,B):
    return tuple(tuple(A[i][j]-B[i][j] for j in range(2)) for i in range(2))

def is_derivation(M):
    e=((1,0),(0,1))
    for x in e:
        for y in e:
            lhs=mat_vec(M,bracket(x,y))
            rhs=add(bracket(mat_vec(M,x),y), bracket(x,mat_vec(M,y)))
            if lhs!=rhs: return False
    return True

H=((2,0),(0,1))
E=((0,1),(0,0))
assert is_derivation(H)
assert is_derivation(E)
assert mat_sub(mat_mul(H,E),mat_mul(E,H))==E

# Representative exact combinations of the full symbolic family.
for d in (-3,-1,0,2,5):
    for b in (-4,0,1,7):
        M=((2*d,b),(0,d))
        assert is_derivation(M)

# Necessary constraints are genuinely restrictive.
assert not is_derivation(((1,0),(0,1)))   # a != 2d
assert not is_derivation(((0,0),(1,0)))   # c != 0

# The lower-central generator persists under repeated adjoint action by H.
X=E
for _ in range(8):
    X=mat_sub(mat_mul(H,X),mat_mul(X,H))
    assert X==E

print('VERIFY_OK')
