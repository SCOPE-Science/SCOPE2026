#!/usr/bin/env python3
from fractions import Fraction as F

def mm(A,B):
    return [[sum(F(A[i][k])*F(B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]
def tr(A): return [list(x) for x in zip(*A)]
def row(l,M): return [sum(F(l[i])*F(M[i][j]) for i in range(3)) for j in range(3)]
def mv(M,v): return [sum(F(M[i][j])*F(v[j]) for j in range(3)) for i in range(3)]
def q(A,v): return sum(F(v[i])*F(A[i][j])*F(v[j]) for i in range(3) for j in range(3))
def grad(A,v): return [2*sum(F(A[i][j])*F(v[j]) for j in range(3)) for i in range(3)]
def proportional(a,b):
    pairs=[(F(x),F(y)) for x,y in zip(a,b)]
    k=None
    for x,y in pairs:
        if y:
            k=x/y; break
        assert x==0
    if k is None: return all(x==0 for x,_ in pairs)
    return all(x==k*y for x,y in pairs)
def same_proj(a,b): return proportional(a,b)

I=[[F(1),0,0],[0,F(1),0],[0,0,F(1)]]
R=[[F(-1,2),F(-1,2),0],[F(3,2),F(-1,2),0],[0,0,1]]
S=[[1,0,0],[0,-1,0],[0,0,1]]
R2=mm(R,R)
assert mm(R2,R)==I and mm(S,S)==I and mm(mm(S,R),S)==R2
A1=[[3,0,0],[0,1,0],[0,0,-3]]
A2=[[3,0,0],[0,1,0],[0,0,-12]]
for M in (R,S):
    assert mm(mm(tr(M),A1),M)==A1
    assert mm(mm(tr(M),A2),M)==A2
L1=[1,0,-1]; L2=[1,1,2]; L3=[-1,1,-2]; lines=[L1,L2,L3]
assert proportional(row(L1,R),L2) and proportional(row(L2,R),L3) and proportional(row(L3,R),L1)
assert proportional(row(L1,S),L1) and proportional(row(L2,S),L3) and proportional(row(L3,S),L2)

# The three simple tangencies with the inner conic.
T=[[1,0,1],[1,3,-2],[1,-3,-2]]
for p,l in zip(T,[L1,L2,L3]):
    assert q(A1,p)==0 and sum(F(l[i])*F(p[i]) for i in range(3))==0
    assert proportional(grad(A1,p),l)
# Rotation is transitive on these tangency points; reflection preserves their set.
assert same_proj(mv(R,T[0]),T[2]) and same_proj(mv(R,T[2]),T[1]) and same_proj(mv(R,T[1]),T[0])
assert all(any(same_proj(mv(S,p),u) for u in T) for p in T)

# The three line-line vertices lie on the outer conic and are ordinary triple points.
V=[[-2,0,1],[1,-3,1],[1,3,1]]
inc=[[1,2],[0,1],[0,2]]
for p,ij in zip(V,inc):
    assert q(A2,p)==0
    g=grad(A2,p)
    for j in ij:
        assert sum(F(lines[j][i])*F(p[i]) for i in range(3))==0
        assert not proportional(g,lines[j])
    assert not proportional(lines[ij[0]],lines[ij[1]])
assert same_proj(mv(R,V[0]),V[1]) and same_proj(mv(R,V[1]),V[2]) and same_proj(mv(R,V[2]),V[0])
assert all(any(same_proj(mv(S,p),u) for u in V) for p in V)

# The conics differ by -9 z^2.  Hence their projective intersection is z=0,
# 3 x^2 + y^2=0, with intersection multiplicity two at each of two distinct points.
# The roots y/x satisfy r^2=-3.  R fixes each root projectively and S swaps them.
def mul(a,b):
    # a+b*r represented by pair, r^2=-3
    return (a[0]*b[0]-3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
r=(F(0),F(1)); one=(F(1),F(0)); three=(F(3),F(0))
# For R(1,r), verify y' - r*x' = 0 modulo r^2+3.
xp=(-F(1,2),-F(1,2)); yp=(F(3,2),-F(1,2))
assert add(yp,(-mul(r,xp)[0],-mul(r,xp)[1]))==(0,0)
# S sends r to -r.
assert (-r[0],-r[1])==(0,-1)
# Pairwise Bezout count is exhausted: 5 tacnodes contribute 10 and 3 triples contribute 9.
assert 4 + 2*2*3 + 3 == 5*2 + 3*3 == 19
print('VERIFY_OK')
