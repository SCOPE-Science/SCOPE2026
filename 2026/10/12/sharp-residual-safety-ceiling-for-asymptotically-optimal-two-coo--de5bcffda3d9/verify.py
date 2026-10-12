from fractions import Fraction as F
from decimal import Decimal, getcontext

def residual_map(rho,w):
    return [
        [F(1)-w+w*w*rho*rho, -w*rho],
        [-w*rho*(F(1)-w), F(1)-w],
    ]

def mv(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def transpose(A):
    return [list(r) for r in zip(*A)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

# Exact kappa=9 witness.
rho=F(4,5)
s=F(3,5)
wopt=F(5,4)
wsafe=F(30,31)
R=residual_map(rho,wopt)
assert R == [[F(3,4),F(-1)],[F(1,4),F(-1,4)]]
rp=mv(R,[F(0),F(1)])
assert rp == [F(-1),F(-1,4)]
assert rp[0]*rp[0]+rp[1]*rp[1] == F(17,16)
assert wsafe < wopt

# Boundary determinant checks for rational Pythagorean pairs.
pairs=[(F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(5,13),F(12,13))]
for s,rho in pairs:
    ws=2*s/(1+s-s*s)
    R=residual_map(rho,ws)
    RtR=mm(transpose(R),R)
    G=[[F(int(i==j))-RtR[i][j] for j in range(2)] for i in range(2)]
    assert det2(G)==0
    # Just below the boundary, determinant is positive.
    w=ws*F(999,1000)
    R=residual_map(rho,w)
    RtR=mm(transpose(R),R)
    G=[[F(int(i==j))-RtR[i][j] for j in range(2)] for i in range(2)]
    assert det2(G)>0

# High-precision sharp crossover.
getcontext().prec=70
D=Decimal
rt2=D(2).sqrt()
rho=(D(1)/D(2)).sqrt()
s=(D(1)-rho*rho).sqrt()
wE=D(2)*s/(D(1)+s-s*s)
wO=D(2)/(D(1)+s)
k=(D(1)+rho)/(D(1)-rho)
assert abs(wE-wO) < D("1e-60")
assert abs(k-(D(3)+D(2)*rt2)) < D("1e-60")

print("VERIFY_OK")
print("witness_wsafe", wsafe)
print("witness_wopt", wopt)
print("witness_squared_residual_ratio", F(17,16))
print("crossover_kappa", k)
