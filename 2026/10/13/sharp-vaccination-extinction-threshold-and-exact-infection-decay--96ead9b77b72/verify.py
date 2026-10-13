"""Exact rational and numerical spot-checks for the Holling-II SVEIR theorem.

The mathematical proof is analytical; finite integrations here test its normalization
and provide reproducible illustrations, not a proof for all initial conditions.
"""
from fractions import Fraction as Q
from math import isfinite


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def determinant3(A):
    a,b,c=A[0]; d,e,f=A[1]; g,h,i=A[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def polyadd(x,y):
    z=[Q(0)]*max(len(x),len(y))
    for i,v in enumerate(x):z[i]+=v
    for i,v in enumerate(y):z[i]+=v
    return z

def polymul(x,y):
    z=[Q(0)]*(len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y): z[i+j]+=a*b
    return z

def polynomial_factor(B):
    # det(tI-B), polynomial coefficients from constant upward
    from itertools import permutations
    S=[Q(0)]
    for perm in permutations(range(3)):
        inv=sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        product=[Q(1)]
        for i,j in enumerate(perm):
            product=polymul(product,[-B[i][j],Q(1)] if i==j else [-B[i][j]])
        S=polyadd(S, [(-1 if inv%2 else 1)*v for v in product])
    return S


def params(mult):
    mu=eta=xi=kappa=omega=phi=L=Q(1)
    sigma=Q(9); p=Q(1,2); gamma=d=Q(1,2)
    beta1=alpha1=Q(3)*mult
    beta2=alpha2=mult
    D=mu*(mu+eta)+sigma*(mu+p*eta)
    S0=L*(mu+eta)/D; V0=L*sigma/D
    b=beta1*S0+beta2*V0
    a=alpha1*S0+alpha2*V0
    Rc=xi/(xi+mu)/(gamma+d+mu)*(b+phi*a/(kappa*omega))
    Jc=(L/mu)*xi/(xi+mu)/(gamma+d+mu)*(beta1+alpha1*phi/(kappa*omega))
    B=[[-(xi+mu),b,a/kappa], [xi,-(gamma+d+mu),Q(0)], [Q(0),phi,-omega]]
    return S0,V0,Rc,Jc,B

s,v,r,j,B=params(Q(1))
assert (s,v,r,j)==(Q(4,31),Q(18,31),Q(15,31),Q(3,2))
assert polynomial_factor(B)==[Q(64,31),Q(218,31),Q(5),Q(1)]
assert determinant3(B)==-Q(64,31)
s,v,r,j,B=params(Q(31,15))
assert (s,v,r,j)==(Q(4,31),Q(18,31),Q(1),Q(31,10))
assert polynomial_factor(B)==[Q(0),Q(6),Q(5),Q(1)]
assert B==[[-2,2,2],[1,-2,0],[0,1,-1]]
assert [sum([Q(1),Q(2),Q(2)][i]*B[i][k] for i in range(3)) for k in range(3)]==[0,0,0]


def rhs(t, Y, m):
    S,E,I,V,R,C=Y
    mu=eta=xi=kappa=omega=phi=L=1.0
    sigma=9.0; p=.5; gamma=d=.5
    beta1=alpha1=3.0*m; beta2=alpha2=m
    g=C/(kappa+C)
    return [L-beta1*S*I-sigma*S+(1-p)*eta*V-alpha1*S*g-mu*S,
            (beta1*S+beta2*V)*I+(alpha1*S+alpha2*V)*g-(xi+mu)*E,
            xi*E-(gamma+d+mu)*I,
            sigma*S-beta2*V*I-(eta+mu)*V-alpha2*V*g,
            gamma*I-mu*R+p*eta*V,
            phi*I-omega*C]


def rk4(Y,h,m,t=0.0):
    k1=rhs(t,Y,m)
    k2=rhs(t+h/2,[y+h*k/2 for y,k in zip(Y,k1)],m)
    k3=rhs(t+h/2,[y+h*k/2 for y,k in zip(Y,k2)],m)
    k4=rhs(t+h,[y+h*k for y,k in zip(Y,k3)],m)
    return [y+h*(a+2*b+2*c+d)/6 for y,a,b,c,d in zip(Y,k1,k2,k3,k4)]

for m, total in [(1.0,300.0),(31/15,15000.0)]:
    for y0 in ([.7,.05,.07,.05,.03,.02], [0.01,0.05,0.3,0.05,0.0,0.8]):
        Y=list(y0); h=0.01
        for _ in range(round(total/h)):
            Y=rk4(Y,h,m)
            if min(Y)<-1e-11 or not all(map(isfinite,Y)):
                raise AssertionError('numerical trajectory left nonnegative state cone')
        target=[4/31,0,0,18/31,(9/31),0] # p*eta*V0/mu = 9/31
        if max(abs(Y[i]-target[i]) for i in [0,3,4])>2e-3:
            raise AssertionError(('DFE susceptible/vaccinated/recovered check',m,Y))
        if max(Y[i] for i in [1,2,5])>5e-3:
            raise AssertionError(('infection trend',m,Y))
print('VERIFY_OK: exact rational matrices, critical kernel, and non-proof trajectories')
