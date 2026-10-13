#!/usr/bin/env python3
"""Exact standard-library spectral and moment checks for the eight-cycle walk."""
from fractions import Fraction as F
from math import cos, sin, sqrt, factorial
import cmath

# Algebraic elements a+b sqrt(2), represented by pairs of rationals.
def q(a=0, b=0):
    return (F(a), F(b))

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def neg(x):
    return (-x[0], -x[1])

def mul(x, y):
    return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])

def scale(x, r):
    return (x[0]*r, x[1]*r)

def matmul(X,Y):
    n=len(X)
    return [[sum_q([mul(X[i][k],Y[k][j]) for k in range(n)]) for j in range(n)] for i in range(n)]

def sum_q(v):
    z=q()
    for x in v:
        z=add(z,x)
    return z

def matvec_plus(X,Y):
    return [[add(X[i][j],Y[i][j]) for j in range(len(X))] for i in range(len(X))]

N=8
A=[[q(int((i-j)%N in (1,N-1))) for j in range(N)] for i in range(N)]
I=[[q(int(i==j)) for j in range(N)] for i in range(N)]

# Fourier projectors for eigenvalues 2, sqrt(2), 0, -sqrt(2), -2.
# Distance classes 0,...,4 are sufficient by translation/reflection invariance.
c_plus={0:q(F(1,4)),1:q(0,F(1,8)),2:q(),3:q(0,F(-1,8)),4:q(-F(1,4))}
c_minus={0:q(F(1,4)),1:q(0,F(-1,8)),2:q(),3:q(0,F(1,8)),4:q(-F(1,4))}
c_zero={0:q(F(1,4)),1:q(),2:q(-F(1,4)),3:q(),4:q(F(1,4))}
coeff={
    '2':{d:q(F(1,8)) for d in range(5)},
    'sqrt2':c_plus,
    '0':c_zero,
    '-sqrt2':c_minus,
    '-2':{d:q(F((-1)**d,8)) for d in range(5)},
}
eigen={'2':q(2),'sqrt2':q(0,1),'0':q(),'-sqrt2':q(0,-1),'-2':q(-2)}
P={name:[[cd[min((i-j)%8,(j-i)%8)] for j in range(N)] for i in range(N)] for name,cd in coeff.items()}

for name,E in P.items():
    E2=matmul(E,E)
    assert E2==E, ('idempotent',name)
    assert matmul(A,E)==[[mul(eigen[name],E[i][j]) for j in range(N)] for i in range(N)], ('eigen',name)
for name,E in P.items():
    for name2,E2 in P.items():
        if name!=name2:
            assert matmul(E,E2)==[[q() for j in range(N)] for i in range(N)],('orthogonality',name,name2)
total=[[q() for j in range(N)] for i in range(N)]
for E in P.values():
    total=matvec_plus(total,E)
assert total==I
assert [sum(P[n][i][i][0] for i in range(N)) for n in ('2','sqrt2','0','-sqrt2','-2')]==[1,2,2,2,1]

# Moments of the product torus law
# fa(theta)=(1-(cos theta)/2)/(2pi), fb(phi)=(1-cos(2phi))/(2pi).
Ea=q(-F(1,4)); Ea2=q(F(1,2)); Eb=q(); Eb2=q(F(1,4))
Esina=q(); Esina2=q(F(1,2)); Esinb=q(); Esinb2=q(F(3,4))
# p0,p1,p2,p3,p4, with expectations evaluated exactly.
p0=scale(sum_q([Ea2, scale(Ea,2),q(1),scale(Eb2,4),scale(mul(Eb,add(Ea,q(1))),4)]),F(1,16))
p4=scale(sum_q([Ea2, scale(Ea,2),q(1),scale(Eb2,4),scale(mul(Eb,add(Ea,q(1))),-4)]),F(1,16))
p2=scale(sum_q([Ea2,scale(Ea,-2),q(1)]),F(1,16))
p1=scale(sum_q([Esina2,scale(Esinb2,2),scale(mul(Esina,Esinb),2)]),F(1,16))
p3=scale(sum_q([Esina2,scale(Esinb2,2),scale(mul(Esina,Esinb),-2)]),F(1,16))
expected=[p0,p1,p2,p3,p4]
assert expected==[q(F(1,8))]*5
assert p0[1]==p4[1]==p2[1]==p1[1]==p3[1]==0

# Independently compare the explicit phase-class formula against
# Fourier projector evolution and the direct Taylor series of exp(i t A).
lam={'2':2.0,'sqrt2':sqrt(2.0),'0':0.0,'-sqrt2':-sqrt(2.0),'-2':-2.0}
def project(t):
    return [[sum((float(E[i][j][0])+float(E[i][j][1])*sqrt(2.0))*cmath.exp(1j*t*lam[n]) for n,E in P.items()) for j in range(N)] for i in range(N)]

def taylor(t):
    out=[[complex(i==j) for j in range(N)] for i in range(N)]
    term=[[complex(i==j) for j in range(N)] for i in range(N)]
    for k in range(1,38):
        term=[[(1j*t/k)*sum(term[i][m]*int((m-j)%8 in (1,7)) for m in range(N)) for j in range(N)] for i in range(N)]
        out=[[out[i][j]+term[i][j] for j in range(N)] for i in range(N)]
    return out

for t in [0.0,0.13,0.37,0.81]:
    U=project(t);V=taylor(t)
    assert max(abs(U[i][j]-V[i][j]) for i in range(N) for j in range(N))<1e-12
    alpha=2*t;beta=sqrt(2)*t
    aa=cos(alpha);bb=sin(alpha);cc=cos(beta);dd=sin(beta)
    probs=[((aa+1+2*cc)**2)/16,((bb+sqrt(2)*dd)**2)/16,((aa-1)**2)/16,((bb-sqrt(2)*dd)**2)/16,((aa+1-2*cc)**2)/16]
    assert max(abs(abs(U[0][d])**2-probs[d]) for d in range(5))<1e-12
    assert abs(probs[0]+2*probs[1]+2*probs[2]+2*probs[3]+probs[4]-1)<1e-12

# The Cesaro mean of the distance-two probability is 3/32, not 1/8.
cesaro_p2=(F(1,2)+F(1))/16
assert cesaro_p2==F(3,32)

# Instantaneous uniformity would force cos(2t)=1-sqrt(2) and cos(sqrt(2)t)=0;
# then its distance-zero probability is unequal to 1/8.
contradiction=(2-sqrt(2))**2/16
assert abs(contradiction-1/8)>1e-3

print('VERIFY_OK spectral_projectors=5 exact_projector_entries=320 exact_mixing_classes=5 exact_cesaro=3/32 independent_taylor_entries=256')
