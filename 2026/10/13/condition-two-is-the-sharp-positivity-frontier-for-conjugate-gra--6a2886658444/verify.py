from fractions import Fraction as F

def cg_diag(lam,b,steps):
    n=len(lam)
    x=[F(0) for _ in range(n)]
    r=[F(v) for v in b]
    p=r[:]
    hist=[]
    for _ in range(steps):
        rr=sum(v*v for v in r)
        if rr == 0:
            hist.append((x[:],r[:],None,None))
            continue
        Ap=[lam[i]*p[i] for i in range(n)]
        alpha=rr/sum(p[i]*Ap[i] for i in range(n))
        x=[x[i]+alpha*p[i] for i in range(n)]
        r2=[r[i]-alpha*Ap[i] for i in range(n)]
        rr2=sum(v*v for v in r2)
        beta=rr2/rr
        p=[r2[i]+beta*p[i] for i in range(n)]
        hist.append((x[:],r2[:],alpha,beta))
        r=r2
    return hist

# Sharp three-dimensional witness.
lam=[F(1),F(2),F(4)]
b=[F(1),F(1),F(1,10)]
h=cg_diag(lam,b,3)
x1,r1,a0,beta0=h[0]
x2,r2,a1,beta1=h[1]
x3,r3,a2,beta2=h[2]
assert a0 == F(201,304)
assert a1 == F(8588,13467)
assert x2 == [F(64,67),F(143,268),F(-83,2680)]
assert x2[2] < 0
xstar=[b[i]/lam[i] for i in range(3)]
assert x3 == xstar
assert r3 == [F(0),F(0),F(0)]

# Two active modes terminate by the second step, with a positive first step.
lam2=[F(3),F(11)]
b2=[F(5),F(7)]
h2=cg_diag(lam2,b2,2)
assert all(v >= 0 for v in h2[0][0])
assert h2[1][0] == [b2[i]/lam2[i] for i in range(2)]
assert all(v >= 0 for v in h2[1][0])

print("VERIFY_OK")
