"""Reproduction of the two-reflection momentum mean-square result (standard library)."""
from fractions import Fraction as F
from itertools import product
from math import sqrt

R1=((-1,0),(0,1))
R2=((1,0),(0,-1))
I=((1,0),(0,1))
NI=((-1,0),(0,-1))

def multiply(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

pairs=[]
for p,q in product((R1,R2),repeat=2):
    pairs.append(multiply(q,p))
assert pairs.count(I)==2 and pairs.count(NI)==2

def mm(a,b):
    mu=1-a
    s=1-2*a+2*a*a
    return ((s+2*mu*b+b*b,-2*b*(mu+b),b*b),
            (mu+b,-b,F(0)),(F(1),F(0),F(0)))

def mv(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def char_coeffs(M):
    tr=M[0][0]+M[1][1]+M[2][2]
    minors=sum(M[i][i]*M[j][j]-M[i][j]*M[j][i] for i,j in ((0,1),(0,2),(1,2)))
    return (F(1),-tr,minors,-det3(M))

a=F(1,4);b=F(1,10)
M=mm(a,b)
assert M==((F(157,200),F(-17,100),F(1,100)),
           (F(17,20),F(-1,10),F(0)),(F(1),F(0),F(0)))
assert char_coeffs(M)==(F(1),F(-685,1000),F(56,1000),F(-1,1000))

def cubic(x):return 1000*x*x*x-685*x*x+56*x-1
intervals=((F(1,50),F(3,100)),(F(3,50),F(7,100)),(F(59,100),F(3,5)))
for lo,hi in intervals:
    assert cubic(lo)*cubic(hi)<0
assert intervals[-1][1]<F(5,8)

# For any nonzero equal source states, the common scalar multiplier scales both coordinates.
# Enumerate all 2^k independent multiplier histories exactly, then check the three-state recurrence.
cvals=(F(1),F(1)-2*a)
state=(F(1),F(1),F(1)) # U1,V1,W1 for unit initial state.
for steps in range(8):
    enumerated=[]
    for choices in product(cvals,repeat=steps):
        xprev=x=F(1)
        for c in choices:
            xnew=(c+b)*x-b*xprev
            xprev,x=x,xnew
        enumerated.append((x*x,x*xprev,xprev*xprev))
    mean=tuple(sum(v[i] for v in enumerated)/len(enumerated) for i in range(3))
    assert mean==state
    state=mv(M,state)

# Analytic eigenvalue derivative from the exact right/left eigenvectors at beta=0.
for a in (F(1,8),F(1,4),F(2,5),F(1,2),F(3,5),F(3,4)):
    mu=1-a;s=1-2*a+2*a*a
    slope=2*mu-2*mu*mu/s
    closed=2*a*(1-a)*(2*a-1)/s
    assert slope==closed
    if a<F(1,2):assert slope<0
    elif a>F(1,2):assert slope>0
    else:assert slope==0

# Critical alpha=1/2 polynomial and its beta-squared Taylor coefficient.
for b0 in (F(0),F(1,100),F(1,20),F(1,10)):
    coeff=char_coeffs(mm(F(1,2),b0))
    assert coeff==(F(1),-(F(1,2)+b0*b0),b0**3,-b0**3)
# Plugging z=1/2+c beta^2 yields leading beta^2 coefficient (c-1)/4.
def p_half(z,b):
    return z**3-(F(1,2)+b*b)*z*z+b**3*z-b**3
for b0 in (F(1,100),F(1,200),F(1,400)):
    assert abs(p_half(F(1,2)+b0*b0,b0)) <= 2*b0**3

# Reconstruct published sufficient-bound coefficients at the rational witness.
mu=1-a # overwritten in slope loop; use a new name below
alpha=F(1,4);beta=F(1,10)
Q=F(0) # [1-2 sigma_min^2/||A||_F^2]^2 on identity is zero.
g1=alpha**2+(1-alpha)**2+(2*alpha*(1-alpha)+3*alpha*beta)*Q +2*beta**2+3*(1-alpha)*beta
g2=2*beta**2+(1-alpha)*beta+alpha*beta*Q
assert g1==F(87,100) and g2==F(19,200) and g1+g2==F(193,200)<1
q=(float(g1)+sqrt(float(g1*g1+4*g2)))/2
assert .9681<q<.9682
assert q>float(F(5,8))

# A deterministic bracket for the largest root is the exact acceleration certificate.
lo,hi=F(59,100),F(3,5)
for _ in range(60):
    mid=(lo+hi)/2
    if cubic(mid)<0:lo=mid
    else:hi=mid
rho=float((lo+hi)/2)
assert abs(rho-.593480527629743)<2e-12
print('verification passed')
