#!/usr/bin/env python3
"""Independent exact-rational checks for conditioned finite-state paths.

Run: python3 verify.py
Checks are finite diagnostics, not a proof of the general limit theorem.
"""
from fractions import Fraction as F
from math import comb

lam = F(1,4)
gam = F(1,8)
a = b = c = d = e = F(1,8)
Q = [[F(0) for _ in range(5)] for _ in range(5)]
for i in (0,1,3,4): Q[i][i] = lam
Q[2][2] = gam
for i,j,w in ((0,1,a),(0,2,b),(1,4,c),(2,3,d),(3,4,e)):
    Q[i][j] = w
assert all(sum(row) < 1 for row in Q)

def matmul(U,V):
    return [[sum(U[i][k]*V[k][j] for k in range(len(V)))
             for j in range(len(V[0]))] for i in range(len(U))]

def survival_matrix(n):
    M = [[F(int(i == j)) for j in range(5)] for i in range(5)]
    for _ in range(n):
        M = matmul(M,Q)
    return sum(M[0])

def enumerate_paths(n):
    paths = {(0,): F(1)}
    for _ in range(n):
        new = {}
        for path,prob in paths.items():
            i=path[-1]
            for j in range(5):
                if Q[i][j]:
                    p=path+(j,)
                    new[p]=prob*Q[i][j]
        paths=new
    return paths

def skeleton(path):
    ans=[]
    for j in path:
        if not ans or ans[-1]!=j:ans.append(j)
    return tuple(ans)

def exact_A(n):
    return comb(n,2)*lam**(n-2)*a*c

def exact_B(n):
    return sum(comb(n-1-s,2)*lam**(n-3-s)*gam**s*b*d*e
               for s in range(n-2))

checks_paths=0
checks_survival=0
checks_residence=0
for n in range(3,15):
    paths=enumerate_paths(n)
    s=sum(paths.values())
    assert s==survival_matrix(n)
    checks_survival+=1
    by={}
    for path,p in paths.items():
        chain=skeleton(path)
        by[chain]=by.get(chain,F(0))+p
    assert by.get((0,1,4),F(0))==exact_A(n)
    assert by.get((0,2,3,4),F(0))==exact_B(n)
    checks_paths+=2
    # Every composition of n-2 into the three critical holds has
    # identical weight when the path uses only critical states.
    target=lam**(n-2)*a*c
    vals=[]
    for path,p in paths.items():
        if skeleton(path)==(0,1,4):
            assert p==target
            vals.append((F(path.count(0),n+1),p))
            checks_residence+=1
    assert len(vals)==comb(n,2)
    mean=sum(x*p for x,p in vals)/exact_A(n)
    second=sum(x*x*p for x,p in vals)/exact_A(n)
    assert mean==F(1,3)
    assert second-mean**2==F(n-2,18*(n+1))
    checks_residence+=2

# Exact Perron projection in a non-scalar primitive component.
A = [[F(3,16),F(1,16)],[F(1,16),F(3,16)]]
P = [[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
I = [[F(1),F(0)],[F(0),F(1)]]
M = I
for n in range(12):
    RHS=[[lam**n*P[i][j]+F(1,8)**n*(I[i][j]-P[i][j])
           for j in range(2)] for i in range(2)]
    assert M==RHS
    M=matmul(M,A)
assert [sum(row)/lam for row in A]==[F(1),F(1)]

# Resolvent-weight route balance is 1:1 even though one route visits
# a strictly subcritical class.
RA = lam**(-2)*a*c
RB = lam**(-3)*b*d*e/(1-gam/lam)
assert RA==RB==F(1,4)
assert F(RA,RA+RB)==F(1,2)


# A genuine nonscalar subcritical communicating class: states 2,3 in
# a six-state matrix have primitive block [[3,1],[1,3]]/32,
# Perron root 1/8 and secondary root 1/16.
Q6 = [[F(0) for _ in range(6)] for _ in range(6)]
for i in (0,1,4,5): Q6[i][i] = lam
Q6[2][2]=Q6[3][3]=F(3,32)
Q6[2][3]=Q6[3][2]=F(1,32)
for i,j,v in ((0,1,F(1,8)),(0,2,F(1,8)),
              (1,5,F(1,8)),(3,4,F(1,8)),(4,5,F(1,8))):
    Q6[i][j]=v
assert all(sum(row)<1 for row in Q6)
R = [[F(5,3),F(1,3)],[F(1,3),F(5,3)]]
A_sub=[[F(3,32),F(1,32)],[F(1,32),F(3,32)]]
assert matmul([[int(i==j)-A_sub[i][j]/lam for j in range(2)] for i in range(2)],R)==I
assert lam**(-3)*F(1,8)**3*R[0][1]==F(1,24)
M_sub=I
sub_cross=[F(0)]*15
for m in range(15):
    sub_cross[m]=M_sub[0][1]
    assert M_sub[0][1]==(F(1,8)**m-F(1,16)**m)/2
    M_sub=matmul(M_sub,A_sub)
checks_sub=0
for n in range(4,12):
    paths={(0,):F(1)}
    for _ in range(n):
        nxt={}
        for path,prob in paths.items():
            for j,w in enumerate(Q6[path[-1]]):
                if w:nxt[path+(j,)]=prob*w
        paths=nxt
    M=[[F(int(i==j)) for j in range(6)] for i in range(6)]
    for _ in range(n):M=matmul(M,Q6)
    assert sum(paths.values())==sum(M[0])
    def comp_route(path):
        cs=[0,1,2,2,3,4]
        out=[]
        for j in path:
            c=cs[j]
            if not out or out[-1]!=c:out.append(c)
        return tuple(out)
    massB=sum(weight for path,weight in paths.items()
              if comp_route(path)==(0,2,3,4))
    expected=F(1,8)**3*sum(comb(n-1-m,2)*lam**(n-3-m)*sub_cross[m]
                             for m in range(n-2))
    assert massB==expected
    checks_sub+=2

print('VERIFY_OK: %d exact survival matrix/path comparisons; '
      '%d maximal-route identities; %d exact composition-moment checks; '
      '12 non-scalar Perron-projector checks; two resolved route weights; '
      '%d nonscalar subcritical resolvent/path comparisons'
      %(checks_survival,checks_paths,checks_residence,checks_sub))
