#!/usr/bin/env python3
"""Exact finite-field witnesses for a nodal cubic surface and its six-point conic.
No external mathematical libraries are required. Finite checks support, but do not
replace, the characteristic-five geometric proof in RESULT.md.
"""
from itertools import combinations, permutations, product

p = 5

def norm(v):
    v = tuple(x % p for x in v)
    k = next(i for i,x in enumerate(v) if x)
    t = pow(v[k], -1, p)
    return tuple((t*x)%p for x in v)

def Q(v):
    a,b,c=v
    d=(-a-b-c)%5
    return (a*a+b*b+c*c+d*d)%5

def C(v):
    a,b,c=v
    d=(-a-b-c)%5
    return (a**3+b**3+c**3+d**3)%5

P2 = {norm(x) for x in product(range(5),repeat=3) if any(x)}
conic = {x for x in P2 if Q(x)==0}
base = {x for x in conic if C(x)==0}
assert len(P2)==31 and len(conic)==6 and len(base)==6
assert conic==base

P=(1,1,1,1,1)

def lift_direction(abc):
    a,b,c=abc
    return (a,b,c,(-a-b-c)%5,0)

# The natural permutation action of S5 on the six directions, with the
# distinguished singular vector removed as a projective gauge.
action=set()
for sig in permutations(range(5)):
    perm=[]
    for v in sorted(base):
        y=lift_direction(v)
        z=[y[sig[j]] for j in range(5)]
        w=[(z[j]-z[4])%5 for j in range(5)]
        target=norm(w[:3])
        assert target in base
        perm.append(sorted(base).index(target))
    action.add(tuple(perm))
assert len(action)==120  # faithful six-point action of S5

# Number of lines over F5, independently of the 15+6 geometric formulas.
def line_equations(u,v):
    u5=tuple(u)+((-sum(u))%5,)
    v5=tuple(v)+((-sum(v))%5,)
    return (sum(x**3 for x in u5)%5,
            sum(x*x*y for x,y in zip(u5,v5))%5,
            sum(x*y*y for x,y in zip(u5,v5))%5,
            sum(y**3 for y in v5)%5)

lines=[]
for i,j in combinations(range(4),2):
    free0=[k for k in range(i+1,4) if k!=j]
    free1=list(range(j+1,4))
    for coeffs in product(range(5),repeat=len(free0)+len(free1)):
        u=[0]*4;v=[0]*4;u[i]=1;v[j]=1
        for k,x in zip(free0,coeffs[:len(free0)]):u[k]=x
        for k,x in zip(free1,coeffs[len(free0):]):v[k]=x
        if line_equations(u,v)==(0,0,0,0):lines.append((tuple(u),tuple(v)))
assert len(lines)==21, len(lines)

def contains_P(u,v):
    return any(all((a*u[k]+b*v[k])%5==1 for k in range(4))
               for a,b in product(range(5),repeat=2))
assert sum(contains_P(u,v) for u,v in lines)==6

# Differential of the four line equations: the Jacobian rank is 4 for
# the fifteen lines away from the node, 3 for the six node-lines.
def rank_mod5(M):
    M=[list(map(lambda a:a%5,row)) for row in M];r=0
    for c in range(len(M[0])):
        t=next((k for k in range(r,len(M)) if M[k][c]),None)
        if t is None:continue
        M[t],M[r]=M[r],M[t]
        z=pow(M[r][c],-1,5)
        M[r]=[z*v%5 for v in M[r]]
        for k in range(len(M)):
            if k!=r and M[k][c]:
                z=M[k][c];M[k]=[(a-z*b)%5 for a,b in zip(M[k],M[r])]
        r+=1
    return r

def tangent_rank(u,v):
    # Pick a basis of the quotient of F5^4 by <u,v>.
    e=[]
    for j in range(4):
        x=tuple(int(i==j) for i in range(4))
        if rank_mod5(list(zip(*(list(u),list(v),*e,x))))==len(e)+3:
            e.append(x)
            if len(e)==2:break
    assert len(e)==2
    U=tuple(u)+((-sum(u))%5,)
    V=tuple(v)+((-sum(v))%5,)
    matrix=[[0]*4 for _ in range(4)]
    for t in range(4):
        du=(e[t] if t<2 else (0,0,0,0))
        dv=(e[t-2] if t>=2 else (0,0,0,0))
        dU=tuple(du)+((-sum(du))%5,)
        dV=tuple(dv)+((-sum(dv))%5,)
        matrix[0][t]=sum(3*a*a*d for a,d in zip(U,dU))%5
        matrix[1][t]=sum(2*a*b*d+a*a*e0 for a,b,d,e0 in zip(U,V,dU,dV))%5
        matrix[2][t]=sum(b*b*d+2*a*b*e0 for a,b,d,e0 in zip(U,V,dU,dV))%5
        matrix[3][t]=sum(3*b*b*e0 for b,e0 in zip(V,dV))%5
    return rank_mod5(matrix)

from collections import Counter
profile=Counter((contains_P(u,v),tangent_rank(u,v)) for u,v in lines)
assert profile==Counter({(False,4):15,(True,3):6}),profile

# Independent projective counts for F5 and F25 = F5[u]/(u^2-2).
def make_field(extension):
    if extension==1:
        elems=tuple(range(5));size=5
        add=lambda a,b:(a+b)%5
        mul=lambda a,b:(a*b)%5
    else:
        elems=tuple(range(25));size=25
        add=lambda a,b:((a%5+b%5)%5)+5*((a//5+b//5)%5)
        mul=lambda a,b:((a%5)*(b%5)+2*(a//5)*(b//5))%5+5*(((a%5)*(b//5)+(a//5)*(b%5))%5)
    A=[[add(a,b) for b in elems] for a in elems]
    M=[[mul(a,b) for b in elems] for a in elems]
    cubes=[M[M[a][a]][a] for a in elems]
    def neg(a):return (-a)%5+5*((-(a//5))%5) if extension==2 else (-a)%5
    count=0
    for pivot in range(4):
        for tail in product(elems,repeat=3-pivot):
            coords=(0,)*pivot+(1,)+tail
            fifth=neg(A[A[A[coords[0]][coords[1]]][coords[2]]][coords[3]])
            S=0
            for x in coords+(fifth,):S=A[S][cubes[x]]
            if S==0:count+=1
    assert count==size*size+6*size+1,(size,count)
    return size,count

print('P2_CONIC_POINTS',len(conic),'BASE_EQUALS_ALL_F5_CONIC_POINTS',base==conic)
print('S5_SIX_POINT_PERMUTATION_ORDER',len(action))
print('FANO_RATIONAL_LINES',len(lines),'TANGENT_RANK_PROFILE',sorted(profile.items()))
print('POINT_COUNTS',[make_field(1),make_field(2)])
print('CLEBSCH_CHAR5_BLOWUP_AUT_ZETA_PASS')
