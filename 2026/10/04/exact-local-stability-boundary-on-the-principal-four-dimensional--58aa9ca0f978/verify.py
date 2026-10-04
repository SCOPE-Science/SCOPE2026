from fractions import Fraction as F
from itertools import permutations
from math import sqrt

# Polynomial in (lambda,k): dict[(lambda_degree,k_degree)] -> rational coefficient.
def add(a,b):
    c=dict(a)
    for m,v in b.items():
        c[m]=c.get(m,F(0))+v
        if c[m]==0: del c[m]
    return c

def mul(a,b):
    c={}
    for (i,j),u in a.items():
        for (r,s),v in b.items():
            m=(i+r,j+s)
            c[m]=c.get(m,F(0))+u*v
    return {m:v for m,v in c.items() if v}

def neg(a): return {m:-v for m,v in a.items()}
def C(x): return {(0,0):F(x)} if x else {}
def L(c=1): return {(1,0):F(c)}
def K(c=1): return {(0,1):F(c)}

def sgn_perm(p):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
    return -1 if inv%2 else 1

def det4(M):
    out={}
    for p in permutations(range(4)):
        t=C(sgn_perm(p))
        for i in range(4): t=mul(t,M[i][p[i]])
        out=add(out,t)
    return out

# lambda I - J for sigma=4, delta=1/2, b=2 at x1=x2=k, x3=k/2, x4=q.
M=[
 [add(L(),C(4)), C(-4), {}, {}],
 [C(F(-5,4)), add(L(),C(1)), C(F(1,2)), K()],
 [{}, C(F(-1,2)), add(L(),C(1)), {}],
 [K(-1), K(-1), {}, add(L(),C(2))],
]
got=det4(M)
want={
 (4,0):F(1), (3,0):F(8), (2,0):F(65,4), (2,2):F(1),
 (1,0):F(17,2), (1,2):F(9), (0,2):F(8)
}
assert got==want, (got,want)

# One-variable q polynomials, coefficients ascending.
def padd(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i in range(n): c[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def pscale(a,s): return [F(s)*x for x in a]
a1=[F(8)]
a2=[F(65,4),F(2)]
a3=[F(17,2),F(18)]
a4=[F(0),F(16)]
D2=padd(pmul(a1,a2),pscale(a3,-1))
D3=padd(padd(pmul(pmul(a1,a2),a3),pscale(pmul(a3,a3),-1)),pscale(pmul(pmul(a1,a1),a4),-1))
assert D2==[F(243,2),F(-2)]
assert D3==[F(4131,4),F(1146),F(-36)]

# Exact arithmetic in Q(s), s^2=10153.
def qa(x,y=0): return (F(x),F(y))
def qadd(u,v): return (u[0]+v[0],u[1]+v[1])
def qmul(u,v): return (u[0]*v[0]+F(10153)*u[1]*v[1],u[0]*v[1]+u[1]*v[0])
def qscale(u,c): return (u[0]*F(c),u[1]*F(c))
def qpow2(u): return qmul(u,u)
qh=(F(191,12),F(1,6))
rh=qadd(qh,qa(F(5,4)))
assert rh==(F(103,6),F(1,6))
# 48 qh^2 - 1528 qh - 1377 = 0.
expr=qadd(qadd(qscale(qpow2(qh),48),qscale(qh,-1528)),qa(-1377))
assert expr==(F(0),F(0))
assert float(qh[0])+float(qh[1])*sqrt(10153) < F(243,4)
assert abs((float(rh[0])+float(rh[1])*sqrt(10153))-33.9603493413446) < 1e-12

omega2=(F(295,8),F(3,8))
beta=(F(269,24),F(-1,24))
# omega^2 = a3(qh)/8.
a3qh=qadd(qa(F(17,2)),qscale(qh,18))
assert qscale(a3qh,F(1,8))==omega2
# beta>0.
assert float(beta[0])+float(beta[1])*sqrt(10153)>0
# Factorization coefficients: (l^2+omega2)(l^2+8l+beta).
assert qadd(beta,omega2)==qadd(qa(F(65,4)),qscale(qh,2))
assert qscale(omega2,8)==a3qh
assert qmul(omega2,beta)==qscale(qh,16)

# Routh signs: qH<q<243/4 gives +,+,+,-,+; q>243/4 gives +,+,-,+,+.
# D3 has exactly one positive root because 48q^2-1528q-1377 has negative constant and positive leading coefficient.
assert F(-1377)<0 and F(48)>0
# Any nonzero imaginary root must satisfy omega^2=a3/8 and then Delta3=0,
# so qH is the only positive imaginary-axis parameter. q=243/4 is therefore not a crossing.
assert qh != (F(243,4),F(0))
print('VERIFY_OK')
