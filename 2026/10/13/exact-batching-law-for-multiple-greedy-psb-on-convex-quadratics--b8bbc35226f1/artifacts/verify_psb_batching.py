from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def eye(n):
    return [[F(int(i==j)) for j in range(n)] for i in range(n)]

def proj_complement(n,i):
    P=eye(n)
    P[i][i]=F(0)
    return P

def mask_update(R,i):
    P=proj_complement(len(R),i)
    return mm(mm(P,R),P)

def score(R,i):
    return R[i][i]

# Non-diagonal SPD example with L I - A positive semidefinite.
A = [
    [F(4), F(1), F(0)],
    [F(1), F(3), F(1,2)],
    [F(0), F(1,2), F(2)],
]
L=F(6)
R=[[L*F(int(i==j))-A[i][j] for j in range(3)] for i in range(3)]
# Sylvester checks for A and R.
assert A[0][0] > 0
assert A[0][0]*A[1][1]-A[0][1]*A[1][0] > 0
assert (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
        -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
        +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])) > 0
assert R[0][0] > 0
assert R[0][0]*R[1][1]-R[0][1]*R[1][0] > 0
assert (R[0][0]*(R[1][1]*R[2][2]-R[1][2]*R[2][1])
        -R[0][1]*(R[1][0]*R[2][2]-R[1][2]*R[2][0])
        +R[0][2]*(R[1][0]*R[2][1]-R[1][1]*R[2][0])) > 0
initial=[score(R,i) for i in range(3)]
order=[]
for _ in range(3):
    i=max(range(3), key=lambda j: score(R,j))
    assert score(R,i) == max(initial[j] for j in range(3) if j not in order)
    order.append(i)
    R=mask_update(R,i)
    for j in range(3):
        if j in order:
            assert score(R,j)==0
        else:
            assert score(R,j)==initial[j]
assert R == [[F(0)]*3 for _ in range(3)]
assert order == [2,1,0]  # deficits 4,3,2

# Sharp diagonal batching example: n=5, t=1, s=5.
eigs=[F(1),F(2),F(3),F(4),F(5)]
L=F(6)
n=5
t=1
G=[L for _ in range(n)]
x=[F(0),F(0),F(0),F(0),F(1)]
updates=0
outer=0

def primal_step(x,G):
    return [x[i] - (eigs[i]*x[i])/G[i] for i in range(n)]

def greedy_update(G):
    global updates
    deficits=[G[i]-eigs[i] for i in range(n)]
    m=max(deficits)
    if m==0:
        return G
    i=deficits.index(m)
    H=list(G)
    H[i]=eigs[i]
    updates += 1
    return H

while G != eigs:
    x=primal_step(x,G)
    # t internal updates plus one final update for G_{k+1}.
    for _ in range(t+1):
        G=greedy_update(G)
    outer += 1

assert updates == 5
assert outer == 3
assert x[4] != 0  # the last coordinate has not yet had a Newton step
x=primal_step(x,G)
assert x == [F(0)]*n
assert outer + 1 == 4

print('VERIFY_OK')
