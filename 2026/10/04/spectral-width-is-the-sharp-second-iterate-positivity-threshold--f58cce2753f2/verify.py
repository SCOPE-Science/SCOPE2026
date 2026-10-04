from fractions import Fraction as F

def matvec(A,x):
    return [sum((A[i][j]*x[j] for j in range(len(x))),F(0)) for i in range(len(A))]

def add(x,y): return [a+b for a,b in zip(x,y)]
def sub(x,y): return [a-b for a,b in zip(x,y)]
def scale(c,x): return [c*a for a in x]
def dot(x,y): return sum((a*b for a,b in zip(x,y)),F(0))

def solve(A,b):
    n=len(A)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for c in range(n):
        p=next(r for r in range(c,n) if M[r][c])
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[v/q for v in M[c]]
        for r in range(n):
            if r==c: continue
            q=M[r][c]
            if q:
                M[r]=[M[r][j]-q*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def outer(u,v): return [[a*b for b in v] for a in u]

def good_broyden_two(A,b,gamma):
    n=len(b)
    x0=[F(0)]*n
    x1=scale(F(1,gamma),b)
    s0=x1
    y0=matvec(A,s0)
    B0=[[gamma if i==j else F(0) for j in range(n)] for i in range(n)]
    corr=sub(y0,matvec(B0,s0))
    den=dot(s0,s0)
    B1=[[B0[i][j]+corr[i]*s0[j]/den for j in range(n)] for i in range(n)]
    f1=sub(matvec(A,x1),b)
    step=solve(B1,f1)
    x2=sub(x1,step)
    return x1,x2,B1

def closed(A,b,gamma):
    rho=dot(b,matvec(A,b))/dot(b,b)
    n=len(b)
    M=[[(rho+gamma if i==j else F(0))-A[i][j] for j in range(n)] for i in range(n)]
    return scale(F(1,1)/(gamma*rho),matvec(M,b)),rho

examples=[
    ([[F(2),F(-1)],[F(-1),F(3)]],[F(2),F(1)],F(3)),
    ([[F(4),F(-1),F(0)],[F(-1),F(5),F(-1)],[F(0),F(-1),F(3)]],[F(1),F(2),F(3)],F(5)),
    ([[F(3),F(-1),F(-1)],[F(-1),F(4),F(0)],[F(-1),F(0),F(5)]],[F(3),F(1),F(2)],F(4)),
]
for A,b,g in examples:
    x1,x2,B1=good_broyden_two(A,b,g)
    xc,rho=closed(A,b,g)
    assert x1==scale(F(1,g),b)
    assert x2==xc
    # Check the secant condition B1 s0 = A s0.
    s0=x1
    assert matvec(B1,s0)==matvec(A,s0)

# Sharp diagonal family: one safe-side and one failure-side point for several parameters.
for mu,L,g in [(F(1),F(4),F(2)),(F(2),F(7),F(3)),(F(3),F(10),F(5))]:
    assert 0<g<L-mu
    tstar=(L-mu-g)/g
    for t,sign in [(tstar/F(2),-1),(tstar*F(2),1)]:
        # Work with epsilon only when t is a rational square in the explicit checks below;
        # here the sign formula itself is checked algebraically in t.
        rho=(mu+L*t)/(1+t)
        val=rho+g-L
        assert (val<0) if sign<0 else (val>0)

# Exact witness.
A=[[F(1),F(0)],[F(0),F(4)]]
b=[F(1),F(1,2)]
g=F(2)
x1,x2,B1=good_broyden_two(A,b,g)
xc,rho=closed(A,b,g)
assert rho==F(8,5)
assert x1==[F(1,2),F(1,4)]
assert x2==xc==[F(13,16),F(-1,16)]
assert solve(A,b)==[F(1),F(1,8)]

# One-dimensional case terminates at the exact positive solution at the second step.
for a,bv,g in [(F(5),F(3),F(2)),(F(7,2),F(4),F(9,2))]:
    A=[[a]]; b=[bv]
    _,x2,_=good_broyden_two(A,b,g)
    assert x2==[bv/a]

print('VERIFY_OK')
