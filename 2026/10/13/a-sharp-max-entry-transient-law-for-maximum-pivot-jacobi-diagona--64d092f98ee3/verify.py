from decimal import Decimal, getcontext

getcontext().prec = 80
D = Decimal
zero=D(0); one=D(1); two=D(2)

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def add_shift(A,c):
    B=[row[:] for row in A]
    for i in range(len(B)):
        B[i][i]+=c
    return B

sqrt2=D(2).sqrt()
tau=D(3)/D(4)
kappa=D(2)

B=[
    [zero,one,tau],
    [one,zero,-tau],
    [tau,-tau,zero]
]
q=one/sqrt2
Q=[
    [q,q,zero],
    [-q,q,zero],
    [zero,zero,one]
]
T=mm(transpose(Q),mm(B,Q))
target=[
    [-one,zero,sqrt2*tau],
    [zero,one,zero],
    [sqrt2*tau,zero,zero]
]
for i in range(3):
    for j in range(3):
        assert abs(T[i][j]-target[i][j]) < D("1e-70")

# Unique pre-step maximum and exact sharp factor.
pre=[abs(B[0][1]),abs(B[0][2]),abs(B[1][2])]
assert pre[0] == one
assert pre[1] == pre[2] == tau
postmax=abs(T[0][2])
assert abs(postmax-sqrt2*tau) < D("1e-70")
assert postmax > one

# Spectrum and exact prescribed condition number.
disc=(one+D(8)*tau*tau).sqrt()
beta_minus=(-one-disc)/two
beta_plus=(-one+disc)/two
assert beta_minus < zero < beta_plus < one
c=(one-kappa*beta_minus)/(kappa-one)
lam_min=c+beta_minus
lam_mid=c+beta_plus
lam_max=c+one
assert lam_min > zero
assert lam_min < lam_mid < lam_max
assert abs(lam_max/lam_min-kappa) < D("1e-70")

A=add_shift(B,c)
TA=mm(transpose(Q),mm(A,Q))
# Shift does not change off-diagonal output.
assert abs(TA[0][2]-sqrt2*tau) < D("1e-70")
assert abs(TA[0][1]) < D("1e-70")
assert abs(TA[1][2]) < D("1e-70")

# Generic upper-bound probes: any orthogonal combination of two entries
# individually bounded by s has every output component <= sqrt(2) s.
probes=[
    (D("0.75"),D("-0.75"),D("0.6"),D("0.8")),
    (D("0.4"),D("0.7"),D("0.8"),D("0.6")),
    (D("-0.9"),D("0.2"),D("1"),D("0")),
]
for x,y,c0,s0 in probes:
    bound=max(abs(x),abs(y))
    u=c0*x+s0*y
    v=-s0*x+c0*y
    assert abs(c0*c0+s0*s0-one) < D("1e-70")
    assert abs(u) <= sqrt2*bound + D("1e-70")
    assert abs(v) <= sqrt2*bound + D("1e-70")

print("VERIFY_OK")
print("tau", tau)
print("condition_number", lam_max/lam_min)
print("max_entry_amplification", postmax)
