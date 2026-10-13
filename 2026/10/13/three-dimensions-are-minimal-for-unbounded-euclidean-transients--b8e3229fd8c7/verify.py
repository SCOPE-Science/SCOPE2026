from fractions import Fraction as F

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def trans(A):
    return [list(r) for r in zip(*A)]

def add(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(c,A):
    return [[c*x for x in row] for row in A]

def inv2(A):
    d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def inv3(A):
    # Gauss-Jordan over Fractions.
    n=3
    T=[A[i][:]+eye(n)[i][:] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if T[i][j])
        T[j],T[p]=T[p],T[j]
        q=T[j][j]
        T[j]=[x/q for x in T[j]]
        for i in range(n):
            if i!=j and T[i][j]:
                q=T[i][j]
                T[i]=[T[i][k]-q*T[j][k] for k in range(2*n)]
    return [row[n:] for row in T]

def hss3(t):
    I=eye(3)
    H=[[F(1),0,0],[0,F(2),0],[0,0,F(4)]]
    S=[[0,t,0],[-t,0,-t],[0,t,0]]
    a=F(2)
    apS=add(scale(a,I),S)
    amS=add(scale(a,I),scale(F(-1),S))
    amH=add(scale(a,I),scale(F(-1),H))
    apH=add(scale(a,I),H)
    # apH diagonal.
    inv_apH=[[F(1,3),0,0],[0,F(1,4),0],[0,0,F(1,6)]]
    return mm(mm(mm(inv3(apS),amH),inv_apH),amS)

for t in (F(6),F(12)):
    M=hss3(t)
    y=mv(M,[F(0),F(1),F(0)])
    assert y==[-t/F(6),F(0),t/F(6)]
    ratio2=sum(v*v for v in y)
    assert ratio2==t*t/F(18)

# Exact entries at t=6.
M=hss3(F(6))
assert M == [
    [F(10,57),F(-1),F(3,19)],
    [F(1,19),F(0),F(-1,19)],
    [F(-3,19),F(1),F(-10,57)]
]

# Characteristic invariants for the claimed polynomial:
# trace=0, pairwise principal-minor sum=(t^2-2)/(9(t^2+2)), det=0.
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def pair_sum(A):
    return ((A[0][0]*A[1][1]-A[0][1]*A[1][0])
           +(A[0][0]*A[2][2]-A[0][2]*A[2][0])
           +(A[1][1]*A[2][2]-A[1][2]*A[2][1]))
for t in (F(1),F(2),F(6),F(12)):
    M=hss3(t)
    assert sum(M[i][i] for i in range(3))==0
    assert det3(M)==0
    assert pair_sum(M)==(t*t-F(2))/(F(9)*(t*t+F(2)))

# Nontrivial 2x2 sample: H=diag(1,3), alpha=2, S=5J.
I=eye(2)
H=[[F(1),0],[0,F(3)]]
S=[[0,F(5)],[F(-5),0]]
a=F(2)
apS=add(scale(a,I),S)
amS=add(scale(a,I),scale(F(-1),S))
amH=add(scale(a,I),scale(F(-1),H))
inv_apH=[[F(1,3),0],[0,F(1,5)]]
M2=mm(mm(mm(inv2(apS),amH),inv_apH),amS)
G=mm(trans(M2),M2)
d1=F(1,3)
d2=F(-1,5)
assert G[0][0]+G[1][1] == d1*d1+d2*d2
assert G[0][0]*G[1][1]-G[0][1]*G[1][0] == d1*d1*d2*d2

print("VERIFY_OK")
print("t6_squared_amplification", F(2))
print("t12_squared_amplification", F(8))
