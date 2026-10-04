from fractions import Fraction as F

def matvec(A,x):
    return [sum((A[i][j]*x[j] for j in range(len(x))), F(0)) for i in range(len(A))]

def dot(x,y):
    return sum((a*b for a,b in zip(x,y)), F(0))

def sub(x,y):
    return [a-b for a,b in zip(x,y)]

def add(x,y):
    return [a+b for a,b in zip(x,y)]

def scale(c,x):
    return [c*a for a in x]

def sd_steps(A,b,kmax):
    n=len(b)
    x=[F(0)]*n
    out=[]
    for _ in range(kmax):
        r=sub(b,matvec(A,x))
        if all(v==0 for v in r):
            out.append((x[:],None,r[:],None))
            continue
        Ar=matvec(A,r)
        alpha=dot(r,r)/dot(r,Ar)
        mu=F(1)/alpha
        x=add(x,scale(alpha,r))
        out.append((x[:],alpha,r[:],mu))
    return out

# General exact identity on rational Stieltjes examples.
examples=[
    (
        [[F(3),F(-1),F(0)],[F(-1),F(4),F(-1)],[F(0),F(-1),F(3)]],
        [F(2),F(1),F(3)]
    ),
    (
        [[F(5),F(-1)],[F(-1),F(2)]],
        [F(3),F(4)]
    ),
]
for A,b in examples:
    out=sd_steps(A,b,2)
    x1,a0,r0,m0=out[0]
    x2,a1,r1,m1=out[1]
    if a1 is not None:
        n=len(b)
        M=[[((m0+m1) if i==j else F(0))-A[i][j] for j in range(n)] for i in range(n)]
        rhs=scale(a0*a1,matvec(M,b))
        assert x2==rhs

# Exact kappa=4 witness.
A=[[F(1),F(0),F(0)],[F(0),F(2),F(0)],[F(0),F(0),F(4)]]
b=[F(1),F(1),F(1,5)]
out=sd_steps(A,b,2)
x1,a0,r0,m0=out[0]
x2,a1,r1,m1=out[1]
assert a0==F(51,79)
assert x1==[F(51,79),F(51,79),F(51,395)]
assert a1==F(969,2171)
assert x2==[F(137853,171509),F(88434,171509),F(-10404,857545)]
assert [b[0]/F(1),b[1]/F(2),b[2]/F(4)] == [F(1),F(1,2),F(1,20)]

# Sharpness-family identity for rational kappa > 2.
for K in [F(5,2),F(3),F(7,2),F(4),F(6)]:
    C=K**3+8*K**2-16*K+8
    tcrit=(K-2)**3/C
    for t,expected in [(tcrit/F(2),1),(tcrit*F(2),-1)]:
        # use epsilon^2=t algebraically in weighted Rayleigh calculations
        s=K/F(2)
        weights=[F(1),F(1),t]
        lambdas=[F(1),s,K]
        S=sum(weights,F(0))
        mu=sum((weights[i]*lambdas[i] for i in range(3)),F(0))/S
        var=sum((weights[i]*(lambdas[i]-mu)**2 for i in range(3)),F(0))
        nu=sum((weights[i]*lambdas[i]*(lambdas[i]-mu)**2 for i in range(3)),F(0))/var
        lhs=K-(mu+nu)
        closed=((K-2)**3-t*C)/(2*((K-2)**2+t*(5*K**2-8*K+4)))
        assert lhs==closed
        if expected>0:
            assert lhs>0
        else:
            assert lhs<0

# Two-mode exact cycle on diagonal examples.
for l1,l2,b1,b2 in [
    (F(1),F(3),F(2),F(5)),
    (F(2),F(7),F(4),F(1)),
    (F(3),F(5),F(7),F(2)),
]:
    A=[[l1,F(0)],[F(0),l2]]
    b=[b1,b2]
    out=sd_steps(A,b,6)
    p=b1*b1
    q=b2*b2
    rho=p*q*(l2-l1)**2/((l1*p+l2*q)*(l1*q+l2*p))
    assert F(0)<=rho<F(1)
    xstar=[b1/l1,b2/l2]
    alpha0=out[0][1]
    for m in range(3):
        xeven=out[2*m-1][0] if m>0 else [F(0),F(0)]
        expected_even=scale(F(1)-rho**m,xstar)
        assert xeven==expected_even
        if 2*m < len(out):
            xodd=out[2*m][0]
            expected_odd=add(scale(F(1)-rho**m,xstar),scale(rho**m*alpha0,b))
            assert xodd==expected_odd

print("VERIFY_OK")
