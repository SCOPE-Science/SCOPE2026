import sympy as sp
from itertools import product
from collections import Counter

# Symbolic affine Lie algebra calculations.
p,q,r,s=sp.symbols("p q r s")
a,b,c,d=sp.symbols("a b c d")
Alpha=sp.Matrix([[p,q],[r,s]])
N=sp.Matrix([[a,b],[c,d]])
e1=sp.Matrix([1,0])
e2=sp.Matrix([0,1])

def lie(x,y):
    return sp.Matrix([0,sp.expand(x[0]*y[1]-x[1]*y[0])])

endo_def=sp.simplify(Alpha*lie(e1,e2)-lie(Alpha*e1,Alpha*e2))
assert endo_def==sp.Matrix([q, s-p*s+r*q])

# Under q=0 and s(1-p)=0, Yau bracket is s times the affine bracket.
def hbr(x,y):
    return sp.Matrix([0,sp.expand(s*(x[0]*y[1]-x[1]*y[0]))])

def torsion(x,y):
    Nx=N*x; Ny=N*y
    return sp.simplify(hbr(Nx,Ny)-N*(hbr(Nx,y)+hbr(x,Ny)-N*hbr(x,y)))

for x in (e1,e2):
    for y in (e1,e2):
        assert torsion(x,y)==sp.zeros(2,1)

def mm(A,B,pmod):
    return tuple(
        sum(A[2*i+k]*B[2*k+j] for k in range(2))%pmod
        for i in range(2) for j in range(2)
    )

def is_lie_endo(A,pmod):
    pp,qq,rr,ss=A
    return qq%pmod==0 and ss*(1-pp)%pmod==0

def commute(A,B,pmod):
    return mm(A,B,pmod)==mm(B,A,pmod)

def hbr_mod(A,x,y,pmod):
    # for eligible A, alpha([x,y]) = s*det(x,y)e2
    ss=A[3]
    return (0, ss*(x[0]*y[1]-x[1]*y[0])%pmod)

def mv(M,x,pmod):
    return (
        (M[0]*x[0]+M[1]*x[1])%pmod,
        (M[2]*x[0]+M[3]*x[1])%pmod,
    )

def is_nij_pair(A,M,pmod):
    if not is_lie_endo(A,pmod) or not commute(A,M,pmod):
        return False
    bas=((1,0),(0,1))
    for x in bas:
        for y in bas:
            Nx=mv(M,x,pmod); Ny=mv(M,y,pmod)
            lhs=hbr_mod(A,Nx,Ny,pmod)
            q1=hbr_mod(A,Nx,y,pmod)
            q2=hbr_mod(A,x,Ny,pmod)
            q3=mv(M,hbr_mod(A,x,y,pmod),pmod)
            inside=((q1[0]+q2[0]-q3[0])%pmod,(q1[1]+q2[1]-q3[1])%pmod)
            rhs=mv(M,inside,pmod)
            if lhs!=rhs:
                return False
    return True

for Q in (2,3,5,7):
    alphas=[A for A in product(range(Q),repeat=4) if is_lie_endo(A,Q)]
    assert len(alphas)==2*Q*Q-Q
    fibers=Counter()
    total=0
    for A in alphas:
        n=0
        for M in product(range(Q),repeat=4):
            good=is_nij_pair(A,M,Q)
            assert good==commute(A,M,Q)
            if good:
                n+=1
        fibers[n]+=1
        total+=n
    expected=4*Q**4-Q**3-2*Q**2
    assert total==expected,(Q,total,expected)
    assert fibers[Q**4]==2
    assert fibers[Q**2]==2*Q**2-Q-2
    print({"q":Q,"twists":len(alphas),"pairs":total,"fiber_distribution":dict(sorted(fibers.items()))})

print("VERIFY_OK")
