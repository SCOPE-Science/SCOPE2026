from fractions import Fraction as F

def T3(x):
    return 4*x*x*x-3*x

def q_scalar(mu,L,lam):
    if L==mu:
        return F(1,mu)
    p=T3((L+mu-2*lam)/(L-mu))/T3((L+mu)/(L-mu))
    return (1-p)/lam

def q_closed(mu,L,lam):
    D=(L+mu)*(L*L+14*L*mu+mu*mu)
    return 2*(16*lam*lam-24*(L+mu)*lam+9*L*L+30*L*mu+9*mu*mu)/D

for mu,L in [(F(1),F(2)),(F(2),F(7)),(F(3,2),F(9,2)),(F(5),F(17))]:
    for lam in [mu,(2*mu+L)/3,(mu+2*L)/3,L]:
        assert q_scalar(mu,L,lam)==q_closed(mu,L,lam)
        assert q_closed(mu,L,lam)>0

def matmul(A,B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
             for j in range(len(B[0]))] for i in range(len(A))]

def matvec(A,x):
    return [sum((A[i][j]*x[j] for j in range(len(x))),F(0)) for i in range(len(A))]

def q_matrix(A,mu,L):
    n=len(A)
    A2=matmul(A,A)
    D=(L+mu)*(L*L+14*L*mu+mu*mu)
    K=9*L*L+30*L*mu+9*mu*mu
    return [[2*(16*A2[i][j]-24*(L+mu)*A[i][j]+(K if i==j else 0))/D
             for j in range(n)] for i in range(n)]

# General sharpness-family identity at rational points.
for kappa in [F(7,2),F(4),F(5),F(8)]:
    for c in [F(1,100), (kappa-3)/F(8)]:
        assert c>0 and c<(kappa-3)/4
        A=[
            [kappa-c,-c,F(0)],
            [-c,kappa-c,F(0)],
            [F(0),F(0),F(1)]
        ]
        Q=q_matrix(A,F(1),kappa)
        D=(kappa+1)*(kappa*kappa+14*kappa+1)
        expected=16*c*(3-kappa+4*c)/D
        assert Q[0][1]==expected
        assert expected<0

# Explicit kappa=4 witness.
A=[
    [F(31,8),F(-1,8),F(0)],
    [F(-1,8),F(31,8),F(0)],
    [F(0),F(0),F(1)]
]
Q=q_matrix(A,F(1),F(4))
assert Q==[
    [F(97,365),F(-1,365),F(0)],
    [F(-1,365),F(97,365),F(0)],
    [F(0),F(0),F(338,365)]
]
b=[F(1,194),F(1),F(1,194)]
x=matvec(Q,b)
assert x==[F(-1,730),F(18817,70810),F(169,35405)]

# Exact inverse action for the witness.
xstar=[F(15,1552),F(401,1552),F(1,194)]
assert matvec(A,xstar)==b
assert all(v>0 for v in xstar)
assert all(v>0 for v in b)
assert x[0]<0

# Some exact kappa<=3 Stieltjes checks.
safe_examples=[
    (
      [[F(2),F(-1),F(0)],[F(-1),F(2),F(0)],[F(0),F(0),F(1)]],
      F(1),F(3)
    ),
    (
      [[F(3,2),F(-1,2)],[F(-1,2),F(3,2)]],
      F(1),F(2)
    )
]
for A,mu,L in safe_examples:
    Q=q_matrix(A,mu,L)
    assert all(v>=0 for row in Q for v in row)

print("VERIFY_OK")
