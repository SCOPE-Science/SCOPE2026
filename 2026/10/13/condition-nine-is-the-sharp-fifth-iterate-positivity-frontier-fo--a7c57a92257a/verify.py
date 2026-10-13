from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def smul(c,A):
    return [[c*v for v in row] for row in A]

def det(M):
    A=[row[:] for row in M]
    n=len(A); d=F(1)
    for k in range(n):
        p=next((i for i in range(k,n) if A[i][k]),None)
        assert p is not None
        if p!=k:
            A[k],A[p]=A[p],A[k]; d=-d
        piv=A[k][k]; d*=piv
        for i in range(k+1,n):
            if A[i][k]:
                q=A[i][k]/piv
                for j in range(k+1,n): A[i][j]-=q*A[k][j]
                A[i][k]=F(0)
    return d

def solve(A,b):
    n=len(A); M=[A[i][:]+[b[i]] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if M[i][k])
        M[k],M[p]=M[p],M[k]
        q=M[k][k]
        M[k]=[v/q for v in M[k]]
        for i in range(n):
            if i==k: continue
            q=M[i][k]
            if q: M[i]=[M[i][j]-q*M[k][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

A=[
 [F(398,25),F(-2,25),0,0,0],
 [F(-2,25),F(396,25),F(-2,25),0,0],
 [0,F(-2,25),F(396,25),F(-2,25),0],
 [0,0,F(-2,25),F(398,25),0],
 [0,0,0,0,F(1)],
]
b=[F(0),F(0),F(0),F(1),F(0)]
n=5
for i in range(n):
    for j in range(n):
        if i!=j: assert A[i][j] <= 0
for k in range(1,n+1): assert det([row[:k] for row in A[:k]]) > 0

I=eye(n)
B=madd(I,smul(F(-1,16),A))
C=[
 [F(1),F(1),0,0],
 [F(1),F(2),F(1),0],
 [0,F(1),F(2),F(1)],
 [0,0,F(1),F(1)],
]
for i in range(4):
    for j in range(4): assert B[i][j] == F(1,200)*C[i][j]
assert B[4][4] == F(15,16)
C2=mm(C,C); C3=mm(C2,C); C4=mm(C3,C)
assert C3[0][3] == 1 and C4[0][3] == 6

beta=F(3,5)
xm1=[F(0)]*n; x=[F(0)]*n; xs=[]
for _ in range(5):
    y=[x[i]+beta*(x[i]-xm1[i]) for i in range(n)]
    xn=[v + b[i]/F(16) for i,v in enumerate(mv(B,y))]
    xs.append(xn); xm1,x=x,xn
expected=[
 [0,0,0,F(1,16),0],
 [0,0,F(1,2000),F(63,1000),0],
 [0,F(1,250000),F(649,2000000),F(125641,2000000),0],
 [F(1,31250000),F(29,25000000),F(78947,250000000),F(3140733,50000000),0],
 [F(-77,31250000000),F(77381,50000000000),F(79289667,250000000000),F(7851951073,125000000000),0],
]
assert xs == [[F(v) for v in row] for row in expected]
assert xs[4][0] < 0 and all(v >= 0 for row in xs[:4] for v in row)
sol=solve(A,b)
assert sol == [F(1,124191936),F(199,124191936),F(39401,124191936),F(7801199,124191936),F(0)]
assert all(v>=0 for v in sol)

# Independent degree-four polynomial evaluation: p4(B)b / L.
B2=mm(B,B); B3=mm(B2,B); B4=mm(B3,B)
c3=(1+beta)**2*(1-2*beta); c4=(1+beta)**4
P=madd(madd(madd(I,B),B2),madd(smul(c3,B3),smul(c4,B4)))
x5_poly=[v/F(16) for v in mv(P,b)]
assert x5_poly == xs[4]
print('VERIFY_OK')
