from fractions import Fraction as F
from itertools import permutations

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0))
    while len(c)>1 and c[-1]==0:
        c.pop()
    return c

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    while len(c)>1 and c[-1]==0:
        c.pop()
    return c

def neg(a):
    return [-x for x in a]

def sub(a,b):
    return add(a,neg(b))

def parity_sign(p):
    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
    return -1 if inv%2 else 1

def determinant_polynomial(A):
    n=len(A); out=[F(0)]
    for p in permutations(range(n)):
        term=[F(parity_sign(p))]
        for i,j in enumerate(p):
            term=mul(term,A[i][j])
        out=add(out,term)
    return out

mu=F(4,100000)
eps=F(5,100)
Phi=F(25,100)
kappa=F(15,100)
Psi=F(2,100)
a1=F(14,100)
a2=F(30,100)
a3=F(20,100)
delta=F(1,1000)

d1=Phi+mu
d2=a1+kappa+mu
d3=a2+Psi+mu
d4=a3+mu

theta_I=d2/Phi+1+kappa/d3+Psi*kappa/(d3*d4)
theta_R=(a1+a2*kappa/d3+a3*Psi*kappa/(d3*d4))/(mu+delta)
L=theta_I+theta_R
B=d1*d2/(Phi*(1+eps*kappa/d3))
K=d1*d2/(Phi*L)

# r denotes the reproduction number. ell=K*(r-1).
ell=[-K,K]
const=lambda x:[F(x)]
M=[
    [sub(const(-Phi),ell),sub(const(B),ell),sub(const(eps*B),ell),neg(ell),neg(ell)],
    [const(Phi),const(-(a1+kappa)),const(0),const(0),const(0)],
    [const(0),const(kappa),const(-(a2+Psi)),const(0),const(0)],
    [const(0),const(0),const(Psi),const(-a3),const(0)],
    [const(0),const(a1),const(a2),const(a3),const(-delta)],
]

p=determinant_polynomial(M)
assert len(p)==2
c0,c1=p
root=-c0/c1
expected=F(386467087274709075099662209,386355335676178838352248250)
assert root==expected
assert c0>0 and c1<0
assert F(1)<root<F(101,100)
value=lambda r:c0+c1*r
assert value(F(1))>0
assert value((F(1)+root)/2)>0
assert value(root)==0
assert value(F(101,100))<0
print("VERIFY_OK")
print("R_CROSS="+str(root))
print("R_CROSS_FLOAT="+format(float(root),".15f"))
