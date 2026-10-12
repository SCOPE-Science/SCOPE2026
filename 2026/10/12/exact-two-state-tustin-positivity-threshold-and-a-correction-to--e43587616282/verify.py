from fractions import Fraction as F

def inv2(A):
    a,b=A[0]
    c,d=A[1]
    det=a*d-b*c
    assert det != 0
    return [[d/det,-b/det],[-c/det,a/det]]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def add(A,B):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]

def scale(s,A):
    return [[s*x for x in row] for row in A]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def inv(A):
    n=len(A)
    M=[row[:] + eye(n)[i] for i,row in enumerate(A)]
    for col in range(n):
        piv=next(i for i in range(col,n) if M[i][col] != 0)
        M[col],M[piv]=M[piv],M[col]
        q=M[col][col]
        M[col]=[x/q for x in M[col]]
        for i in range(n):
            if i==col: continue
            q=M[i][col]
            if q:
                M[i]=[x-q*y for x,y in zip(M[i],M[col])]
    return [row[n:] for row in M]

def tustin(A,h):
    n=len(A); I=eye(n)
    P=add(I,scale(h/2,A))
    M=add(I,scale(-h/2,A))
    return mm(P,inv(M))

# Published determinant-only implication is false.
A=[[F(-10),F(0)],[F(0),F(-1)]]
h=F(1,2)
alpha=F(2)/h
Delta=F(10)
assert Delta <= alpha*alpha
T=tustin(A,h)
assert T == [[F(-3,7),F(0)],[F(0),F(3,5)]]
assert T[0][0] < 0

# Strongly coupled example: exact threshold h*=4, while safe diagonal bound is 2.
A=[[F(-1),F(3,4)],[F(1),F(-1)]]
for h,expected in [
    (F(3), [[F(7,73),F(36,73)],[F(48,73),F(7,73)]]),
    (F(4), [[F(0),F(1,2)],[F(2,3),F(0)]])
]:
    assert tustin(A,h)==expected
    assert all(v>=0 for row in expected for v in row)
T5=tustin(A,F(5))
assert T5[0][0] < 0 and T5[1][1] < 0

# General identity T = 2 M^{-1} - I on a 3-state Hurwitz Metzler example.
A3=[
    [F(-4),F(1),F(0)],
    [F(1),F(-5),F(1)],
    [F(0),F(1),F(-3)]
]
h=F(2,5)
I=eye(3)
M=add(I,scale(-h/2,A3))
Minv=inv(M)
T3=tustin(A3,h)
rhs=add(scale(F(2),Minv),scale(F(-1),I))
assert T3==rhs
assert all(Minv[i][j]>=0 for i in range(3) for j in range(3))
for i in range(3):
    for j in range(3):
        if i!=j:
            assert T3[i][j]>=0

print("VERIFY_OK")
