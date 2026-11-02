#!/usr/bin/env python3
"""Exact standalone checks for radius-two hypercube mixing.
Only Python standard-library modules are used.
"""
from fractions import Fraction as F
from itertools import combinations

checks = 0

def check(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)

def optimum(d):
    if d == 2:
        return F(1,4), F(1,2), F(1,4), F(0)
    if d == 3:
        return F(1,7), F(3,7), F(3,7), F(1,7)
    return F(0), F(2,d+1), F(d-1,d+1), F(d-3,d+1)

def eig(d, k, a0, a1, a2):
    s=d-2*k
    return a0 + a1*F(s,d) + a2*F(s*s-d,d*(d-1))

def matrix(d, special=F(0)):
    N=1<<d
    a0,a1,a2,t=optimum(d)
    P=[[F(0) for _ in range(N)] for _ in range(N)]
    for x in range(N):
        P[x][x]=a0
        for i in range(d):
            flip=1<<i
            weight=a1/F(d)
            if special and d>=5:
                if i==1:weight-=special
                if i==2:weight+=special
            P[x][x^flip]=weight
        for i,j in combinations(range(d),2):
            flip=(1<<i)|(1<<j)
            weight=a2/F(d*(d-1),2)
            if special and d>=5:
                if (i,j)==(0,1):weight+=special
                if (i,j)==(0,2):weight-=special
            P[x][x^flip]=weight
    return P

def verify_mat(d, special=F(0)):
    N=1<<d
    a0,a1,a2,t=optimum(d)
    P=matrix(d,special)
    for x in range(N):
        check(sum(P[x])==1,('row sum',d,x,special))
        for y in range(N):
            check(P[x][y]>=0,('nonnegative',d,x,y,special))
            check(P[x][y]==P[y][x],('symmetric',d,x,y,special))
            check((x^y).bit_count()<=2 or P[x][y]==0,('support',d,x,y))
    for S in range(N):
        e=sum(P[0][y] * (-1 if (y&S).bit_count()%2 else 1) for y in range(N))
        if special==0:
            check(e==eig(d,S.bit_count(),a0,a1,a2),('Walsh eigenvalue',d,S))
        if S:
            check(abs(e)<=t,('spectral bound',d,S,e,t,special))
    return P

# Exact algebra and mode bound over a large finite test range, supplementing the universal proof.
for d in range(2,121):
    a0,a1,a2,t=optimum(d)
    check((a0+a1+a2)==1,('probability simplex',d))
    check(min(a0,a1,a2)>=0,('positive shell masses',d))
    check(eig(d,0,a0,a1,a2)==1,('stationary eigenvalue',d))
    for k in range(1,d+1):
        E=eig(d,k,a0,a1,a2)
        check(abs(E)<=t,('extreme eigenvalue',d,k,E,t))
    check(abs(eig(d,1,a0,a1,a2))==t,('first mode active',d))
    check(abs(eig(d,d,a0,a1,a2))==t if d>2 else True,('last mode active',d))
    if d>=4:
        check(a0==0 and a1==F(2,d+1),('equal nonzero edge weights',d))
        check(eig(d,1,a0,a1,a2)==t and eig(d,d,a0,a1,a2)==t,
              ('positive endpoint eigenspaces',d))
    if d>=5:
        for k in range(2,d):
            check(abs(eig(d,k,a0,a1,a2))<t,('interior strict gap',d,k))
        w=F(2,d*(d+1))
        eps=w/16
        def changed_eigen(S):
            b0=(S>>0)&1; b1=(S>>1)&1; b2=(S>>2)&1
            return eps*(1-(-1)**b0)*((-1)**b2-(-1)**b1)
        for k in range(2,d):
            # The maximum perturbation is 4 eps; strict gap is checked directly.
            check(abs(eig(d,k,a0,a1,a2))+4*eps<t,
                  ('perturbation safety',d,k))

# Interpolation certificates yield matching universal lower bounds in dimension three.
for basis in (lambda s:F(1), lambda s:F(s), lambda s:F(s*s)):
    check(basis(3)==3*basis(1)-3*basis(-1)+basis(-3), 'd3 interpolation')
# The support transition at dimension four and rigidity of all nonconstant Walsh modes.
for d in (3,4):
    a0,a1,a2,t=optimum(d)
    for k in range(1,d+1):
        check(abs(eig(d,k,a0,a1,a2))==t,('all modes tight',d,k))

for d in range(2,8):
    verify_mat(d)
for d in (5,6,7):
    w=F(2,d*(d+1))
    P=verify_mat(d,w/16)
    check(P[0][(1<<0)|(1<<1)]!=matrix(d)[0][(1<<0)|(1<<1)],
          ('distinct nonsymmetric-coordinate optimizer',d))

# Independent edge-pair directions span an affine family of dimension C(d,2)-1.
# Each direction transfers pair-flip probability between two unordered pairs,
# and compensates the induced coordinate degree changes at single-bit edges.
for d in range(5,11):
    a0,a1,a2,t=optimum(d)
    base=(0,1)
    pairs=list(combinations(range(d),2))
    eps=F(2,d*(d+1)*1000)
    for alt in pairs[1:]:
        q_delta={base:-eps, alt:eps}
        degree=[F(0)]*d
        for (i,j),amount in q_delta.items():
            degree[i]+=amount; degree[j]+=amount
        p_delta=[-v for v in degree]
        check(sum(p_delta)+sum(q_delta.values())==0,('direction normalization',d,alt))
        check(all(abs(v)<F(2,d*(d+1)) for v in p_delta),('positive single weights',d,alt))
        check(all(abs(v)<F(2,d*(d+1)) for v in q_delta.values()),('positive pair weights',d,alt))
        check(sum(q_delta.values())==0,('zero total pair perturbation',d,alt))
        for i in range(d):
            check(p_delta[i]+sum(q_delta.get(tuple(sorted((i,j))),F(0))
                                for j in range(d) if j!=i)==0,
                  ('coordinate marginal invariant',d,alt,i))
        for S in range(1,1<<d):
            delta=sum(p_delta[i] * (-1 if S&(1<<i) else 1) for i in range(d))
            delta+=sum(v * (-1 if (S&(1<<i)).bit_count()+(S&(1<<j)).bit_count()==1 else 1)
                       for (i,j),v in q_delta.items())
            check(abs(eig(d,S.bit_count(),a0,a1,a2)+delta)<=t,
                  ('face direction spectral safety',d,alt,S))

print('VERIFY_OK',checks,'exact assertions')
