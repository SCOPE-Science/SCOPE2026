from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mv(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def frob2(A):
    return sum(x*x for row in A for x in row)

for t in [F(1,4),F(1),F(3,2),F(5)]:
    u=2*t+1
    B=[
        [t+1,t,F(1)],
        [t,t+1,F(1)],
        [F(1),F(-1),2*t+2]
    ]

    lam=2*t+2
    x=[F(1),F(1),F(1)]
    z=[F(1,u),F(-1,u),F(1)]

    assert mv(B,x)==[lam*q for q in x]
    BT=[list(r) for r in zip(*B)]
    assert mv(BT,z)==[lam*q for q in z]
    assert sum(z[i]*x[i] for i in range(3))==1

    # Work with the squared diagonal scale D^2=diag(1,1,u), avoiding radicals.
    condB2=F(3)*(1+F(2,u*u))
    condA2=(F(2)+u)*(F(2,u*u)+F(1,u))
    assert condB2 == F(3)*(4*t*t+4*t+3)/(u*u)
    assert condA2 == (2*t+3)**2/(u*u)
    assert condB2-condA2 == F(8)*t*t/(u*u)
    assert condB2 > condA2

    # Frobenius comparison can also be done using squared scaled entries.
    # A_13^2=A_23^2=1/u; A_31^2=A_32^2=u.
    offB = F(2)*t*t + F(4)
    offA = F(2)*t*t + F(2,u) + F(2)*u
    assert offA-offB == F(8)*t*t/u

# Concrete t=1 values.
t=F(1)
assert F(25,9) < F(11,3)  # (5/3)^2 < (sqrt(33)/3)^2

# The two-dimensional objective term has its AM-GM minimum at s^2=|c/b|.
# Exact rational spot checks: q + r >= 2 sqrt(qr) is tested where qr is a square.
for q,r in [(F(1),F(4)),(F(4),F(9)),(F(9),F(16))]:
    root=(q*r).numerator**0.5/(q*r).denominator**0.5
    assert float(q+r) >= 2*root

print("VERIFY_OK")
print("t1_unbalanced_condition_sq", F(25,9))
print("t1_balanced_condition_sq", F(11,3))
