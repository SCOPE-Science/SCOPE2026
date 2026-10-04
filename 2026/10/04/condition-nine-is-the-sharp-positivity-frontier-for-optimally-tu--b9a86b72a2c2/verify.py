from fractions import Fraction as F

def matvec(A,x):
    return [sum((A[i][j]*x[j] for j in range(len(x))), F(0)) for i in range(len(A))]

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def sub(x,y):
    return [a-b for a,b in zip(x,y)]

def scale(c,x):
    return [c*a for a in x]

def hb_two(A,b,alpha,beta):
    xminus=[F(0)]*len(b)
    x0=[F(0)]*len(b)
    r0=sub(b,matvec(A,x0))
    x1=add(add(x0,scale(beta,sub(x0,xminus))),scale(alpha,r0))
    r1=sub(b,matvec(A,x1))
    x2=add(add(x1,scale(beta,sub(x1,x0))),scale(alpha,r1))
    return x1,x2

# Verify x2 = alpha[(2+beta)I-alpha A]b.
examples=[
    (
        [[F(3),F(-1)],[F(-1),F(2)]],
        [F(2),F(5)],
        F(1,5),F(1,3)
    ),
    (
        [[F(4),F(-1),F(0)],[F(-1),F(5),F(-1)],[F(0),F(-1),F(3)]],
        [F(1),F(2),F(4)],
        F(1,7),F(2,5)
    ),
]
for A,b,a,be in examples:
    x1,x2=hb_two(A,b,a,be)
    B=[[(F(2)+be if i==j else F(0))-a*A[i][j]
        for j in range(len(A))] for i in range(len(A))]
    rhs=scale(a,matvec(B,b))
    assert x1==scale(a,b)
    assert x2==rhs

# Polyak optimal parameters for square condition numbers kappa=r^2,
# normalized to mu=1.
for r in [F(2),F(3),F(4),F(5)]:
    L=r*r
    alpha=F(4)/(r+1)**2
    beta=(r-1)**2/(r+1)**2
    safe=(alpha*L <= F(2)+beta)
    assert safe == (r <= 3)

# Explicit kappa=16 witness.
A=[[F(1),F(0)],[F(0),F(16)]]
b=[F(1),F(1)]
alpha=F(4,25)
beta=F(9,25)
x1,x2=hb_two(A,b,alpha,beta)
assert x1==[F(4,25),F(4,25)]
assert x2==[F(44,125),F(-4,125)]
assert [F(1),F(1,16)] == [b[0]/A[0][0],b[1]/A[1][1]]

def U(k,c):
    if k==-1:
        return F(0)
    if k==0:
        return F(1)
    u0=F(1)
    u1=2*c
    if k==1:
        return u1
    for _ in range(1,k):
        u0,u1=u1,2*c*u1-u0
    return u1

# Verify recurrence and Chebyshev-U representation.
for q in [F(1,5),F(1,3),F(1,2),F(3,5)]:
    for c in [F(-1),F(-1,2),F(0),F(1,3),F(1)]:
        e0=F(1)
        e1=q*(2*c-q)
        vals=[e0,e1]
        for k in range(1,12):
            vals.append(2*q*c*vals[-1]-q*q*vals[-2])
        for k,e in enumerate(vals):
            closed=q**k*(U(k,c)-q*U(k-1,c))
            assert e==closed

# High-curvature endpoint c=-1.
for q in [F(1,3),F(1,2),F(3,5),F(2,3)]:
    e2=q*q*(3+2*q)
    recurrence=2*q*F(-1)*(q*(F(-2)-q))-q*q
    assert recurrence==e2
assert F(1,2)**2*(3+2*F(1,2)) == 1
assert F(3,5)**2*(3+2*F(3,5)) > 1

# Finite corroboration of the analytic all-iterate bound q<=1/2.
for q in [F(1,10),F(1,4),F(1,3),F(1,2)]:
    for k in range(2,30):
        bound=q**k*(F(k+1)+q*k)
        assert bound <= 1

print("VERIFY_OK")
