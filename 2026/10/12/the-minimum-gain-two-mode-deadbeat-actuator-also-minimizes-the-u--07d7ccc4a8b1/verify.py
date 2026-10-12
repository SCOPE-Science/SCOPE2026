from fractions import Fraction as F

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def sub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def outer(u,v):
    return [[u[i]*v[j] for j in range(len(v))] for i in range(len(u))]

# Exact equality witness.
a,d=F(4,5),F(3,5)
b=[F(4,5),F(3,5)]
k=[F(4),F(-3)]
A=[[a,F(0)],[F(0),d]]
Ac=sub(A,outer(b,k))
assert Ac==[[F(-12,5),F(12,5)],[F(-12,5),F(12,5)]]
assert mm(Ac,Ac)==[[F(0),F(0)],[F(0),F(0)]]
assert k[0]*k[0]+k[1]*k[1]==F(25)
assert (a*a+d*d)/(a-d)==F(5)
# Rank-one Frobenius squared = spectral norm squared.
frob2=sum(x*x for row in Ac for x in row)
assert frob2==F(576,25)
assert F(2)*a*d/(a-d)==F(24,5)
assert frob2==F(24,5)**2

# Verify exact pole equations and closed-loop norm identity on rational squared weights.
for a,d,x in [
    (F(3,4),F(1,4),F(2,3)),
    (F(2,3),F(1,3),F(3,5)),
    (F(5,6),F(1,2),F(4,7)),
]:
    D=a-d
    y=1-x
    # Work with squared quantities; signs do not affect the norm formulas.
    k2=(a**4/x+d**4/y)/D**2
    assert k2 >= (a*a+d*d)**2/D**2
    ac2=(a*a*y+d*d*x)**2/(x*y*D**2)
    assert ac2 >= (F(2)*a*d/D)**2
    # Equality squared weight is a^2/(a^2+d^2).
    xe=a*a/(a*a+d*d); ye=1-xe
    ke=(a**4/xe+d**4/ye)/D**2
    ace=(a*a*ye+d*d*xe)**2/(xe*ye*D**2)
    assert ke==(a*a+d*d)**2/D**2
    assert ace==(F(2)*a*d/D)**2

# Trace/determinant equations for feedback products p=b1*k1, q=b2*k2.
for a,d in [(F(4,5),F(3,5)),(F(3,4),F(1,4)),(F(7,8),F(1,2))]:
    D=a-d
    p=a*a/D; q=-d*d/D
    assert p+q==a+d
    assert d*p+a*q==a*d

print('VERIFY_OK')
