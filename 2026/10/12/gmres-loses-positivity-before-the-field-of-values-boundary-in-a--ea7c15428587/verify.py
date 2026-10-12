from fractions import Fraction as F

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def sub(x,y):
    return [a-b for a,b in zip(x,y)]

def scale(c,x):
    return [c*a for a in x]

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def solve2(G,r):
    a,b=G[0]
    c,d=G[1]
    det=a*d-b*c
    assert det != 0
    return [(r[0]*d-b*r[1])/det,(a*r[1]-r[0]*c)/det]

def gmres2(t):
    A=[
        [F(1),-t,F(0),F(0)],
        [F(0),F(1),-t,F(0)],
        [F(0),F(0),F(1),-t],
        [F(0),F(0),F(0),F(1)],
    ]
    b=[F(1),F(2),F(2),F(1)]
    Ab=matvec(A,b)
    alpha=dot(Ab,b)/dot(Ab,Ab)
    x1=scale(alpha,b)

    A2b=matvec(A,Ab)
    G=[
        [dot(Ab,Ab),dot(Ab,A2b)],
        [dot(Ab,A2b),dot(A2b,A2b)],
    ]
    rhs=[dot(Ab,b),dot(A2b,b)]
    a,beta=solve2(G,rhs)
    x2=add(scale(a,[F(1),F(2),F(2),F(1)]),scale(beta,Ab))
    return A,[F(1),F(2),F(2),F(1)],alpha,x1,a,beta,x2

def closed_x2(t):
    D=9*t**4-32*t**3+58*t**2-56*t+26
    return [
        2*(4*t**3-5*t**2-2*t+13)/D,
        4*(-2*t**3+9*t**2-15*t+13)/D,
        2*(-10*t**3+32*t**2-43*t+26)/D,
        -2*(t-1)*(8*t**2-15*t+13)/D,
    ]

# Main exact witness.
t=F(6,5)
A,b,alpha,x1,a,beta,x2=gmres2(t)
assert alpha == F(5,47)
assert x1 == [F(5,47),F(10,47),F(10,47),F(5,47)]
assert a == F(2210,1777)
assert beta == F(-3025,1777)
assert x2 == [F(6445,1777),F(5630,1777),F(2000,1777),F(-815,1777)]
assert x2 == closed_x2(t)

# Positive exact solution from the finite Neumann series.
xstar=[F(1001,125),F(146,25),F(16,5),F(1)]
assert matvec(A,xstar) == b
assert all(v>0 for v in xstar)

# Residual norm still decreases.
r0=b
r1=sub(b,matvec(A,x1))
r2=sub(b,matvec(A,x2))
assert dot(r0,r0) == 10
assert dot(r1,r1) == F(468,47)
assert dot(r2,r2) == F(6480,1777)
assert dot(r2,r2) < dot(r1,r1) < dot(r0,r0)

# The rational witness lies before the field-of-values boundary:
# 6/5 < sqrt(5)-1 iff 11/5 < sqrt(5), and 121 < 125.
assert 121 < 125

# Closed-form second-step coordinates agree with direct normal equations
# below, at, and above the positivity threshold.
for q in [F(1,2),F(1),F(11,10),F(6,5)]:
    _,_,_,_,_,_,xdirect=gmres2(q)
    assert xdirect == closed_x2(q)

assert closed_x2(F(1,2))[3] > 0
assert closed_x2(F(1))[3] == 0
assert closed_x2(F(11,10))[3] < 0
assert closed_x2(F(6,5))[3] < 0

print("VERIFY_OK")
