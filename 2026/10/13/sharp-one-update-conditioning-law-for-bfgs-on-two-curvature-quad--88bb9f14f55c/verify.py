from fractions import Fraction as F
from decimal import Decimal, getcontext

getcontext().prec = 70
D = Decimal

def qstar(k):
    return F(3)*k/(k+F(2))

# Exact rational identities at the extremal Rayleigh quotient.
for k in map(F, [2,3,4,7,10,25]):
    q = qstar(k)
    assert F(1) < q < k
    m2 = (q-F(1))*(k-q)
    T = q+F(1)+m2/q
    assert T == k+F(2)-k/q
    # R'(q) has numerator 3k-(k+2)q.
    assert F(3)*k-(k+F(2))*q == 0
    # Extremal endpoint weight on the k-eigenspace.
    w = (q-F(1))/(k-F(1))
    assert w == F(2)/(k+F(2))

def gamma_closed(k):
    k=D(k)
    num=(k+D(2))**D("1.5") + (k-D(1))*(k+D(8)).sqrt()
    return num*num/(D(27)*k)

def gamma_from_trace(k):
    k=D(k)
    q=D(3)*k/(k+D(2))
    T=k+D(2)-k/q
    eta=T/q.sqrt()
    root=(eta+(eta*eta-D(4)).sqrt())/D(2)
    return root*root

for ks in ["1","1.1","2","4","10","100"]:
    g1=gamma_closed(ks)
    g2=gamma_from_trace(ks)
    assert abs(g1-g2) < D("1e-55")
    if D(ks) > 1:
        assert g1 > D(ks)

# Exact comparison factorization:
# 4(k+2)^3 - 27(k+1)^2 = (k-1)^2(4k+5).
for k in map(F,[1,2,4,9,20]):
    lhs=F(4)*(k+F(2))**3-F(27)*(k+F(1))**2
    rhs=(k-F(1))**2*(F(4)*k+F(5))
    assert lhs==rhs

# kappa=4 witness: B1 has trace 4 and determinant 2.
tr=F(4)
det=F(2)
disc_q=tr*tr-F(4)*det
disc=(D(disc_q.numerator)/D(disc_q.denominator)).sqrt()
trD=D(tr.numerator)/D(tr.denominator)
lam_plus=(trD+disc)/D(2)
lam_minus=(trD-disc)/D(2)
ratio=lam_plus/lam_minus
target=D(3)+D(2)*D(2).sqrt()
assert abs(ratio-target) < D("1e-60")
assert ratio > D(4)

print("VERIFY_OK")
print("kappa4_condition", ratio)
print("kappa10_worst", gamma_closed("10"))
print("kappa100_worst", gamma_closed("100"))
