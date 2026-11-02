#!/usr/bin/env python3
"""Exact exhaustive F_49 census of the genus-3 Ciani superspecial locus in char 7.
F_49=F_7[u]/(u^2-3); elements are encoded a+7b. No external packages.
The passage from this finite census to geometric exhaustiveness uses Ohashi's
published theorem: every smooth superspecial standard Ciani quartic in
characteristic p has its three coefficients in F_(p^2).
"""
from collections import Counter
from itertools import product, permutations
p=7; q=49
M=[[0]*q for _ in range(q)]
for x in range(q):
    for y in range(q):
        M[x][y]=((x%7)*(y%7)+3*(x//7)*(y//7))%7+7*(((x%7)*(y//7)+(x//7)*(y%7))%7)
def add(x,y): return ((x%7+y%7)%7)+7*((x//7+y//7)%7)
def neg(x):return ((-x%7)%7)+7*((-(x//7))%7)
def sub(x,y):return add(x,neg(y))
def mul(x,y):return M[x][y]
def c(x,n):return mul(x,n%7)
def det3(rows):
    a,b,d=rows
    return add(sub(mul(a[0],sub(mul(b[1],d[2]),mul(b[2],d[1]))),
                   mul(a[1],sub(mul(b[0],d[2]),mul(b[2],d[0])))),
               mul(a[2],sub(mul(b[0],d[1]),mul(b[1],d[0]))))
squares=[mul(x,x) for x in range(q)]

def factors(r,s,t):
    # x,y,z-involution factors, in this order
    B=[sub(c(mul(r,t),2),c(s,4)),sub(c(mul(r,s),2),c(t,4)),sub(c(mul(s,t),2),c(r,4))]
    A=[mul(sub(squares[r],4),sub(squares[t],4)),
       mul(sub(squares[r],4),sub(squares[s],4)),
       mul(sub(squares[s],4),sub(squares[t],4))]
    D=[sub(squares[B[i]],A[i]) for i in range(3)]
    return B,D

def smooth(r,s,t):
    R=mul(mul(r,s),t)
    delta=sub(sub(add(add(squares[r],squares[s]),squares[t]),R),4)
    return delta!=0 and all(squares[x]!=4 for x in (r,s,t))

def gradients(r,s,t,B):
    # Exact gradients of B_i,D_i in order r,s,t.
    gb=[[c(t,2),3,c(r,2)],[c(s,2),c(r,2),3],[3,c(t,2),c(s,2)]]
    ga=[[c(mul(r,sub(squares[t],4)),2),0,c(mul(t,sub(squares[r],4)),2)],
        [c(mul(r,sub(squares[s],4)),2),c(mul(s,sub(squares[r],4)),2),0],
        [0,c(mul(s,sub(squares[t],4)),2),c(mul(t,sub(squares[s],4)),2)]]
    gd=[[sub(c(mul(B[i],gb[i][j]),2),ga[i][j]) for j in range(3)] for i in range(3)]
    return gb,gd

found=set(); bad=[]; type_counts=Counter(); field_counts=Counter()
for r,s,t in product(range(q),repeat=3):
    B,D=factors(r,s,t)
    if any(B[i] and D[i] for i in range(3)):continue
    if not smooth(r,s,t):
        bad.append((r,s,t))
        continue
    typ=''.join('B' if B[i]==0 else 'D' for i in range(3))
    assert all((B[i]==0) != (D[i]==0) for i in range(3))
    gb,gd=gradients(r,s,t,B)
    rows=[gb[i] if typ[i]=='B' else gd[i] for i in range(3)]
    assert det3(rows)!=0,('non-transverse',r,s,t,typ)
    found.add((r,s,t)); type_counts[typ]+=1
    field_counts['F7' if r<7 and s<7 and t<7 else 'F49_strict']+=1
assert len(found)==23 and len(bad)==4
assert type_counts==Counter({'BBB':1,'BBD':2,'BDB':2,'DBB':2,'BDD':4,'DBD':4,'DDB':4,'DDD':4}),type_counts
assert field_counts==Counter({'F7':11,'F49_strict':12}),field_counts
u=7
expected={(0,0,0)}
for i in range(3):
    for a in [1,6]:
        v=[0,0,0];v[i]=a;expected.add(tuple(v))
for v in product([3,4],repeat=3):
    if mul(mul(v[0],v[1]),v[2])==1:expected.add(v)
for v in set(permutations((3,mul(3,u),mul(3,u)))) | set(permutations((4,mul(3,u),mul(3,u)))):
    pass
for coordinate in range(3):
    others=[j for j in range(3) if j!=coordinate]
    for a in (3,4):
        for b,c0 in product((mul(3,u),mul(4,u)),repeat=2):
            v=[0,0,0];v[coordinate]=a;v[others[0]]=b;v[others[1]]=c0
            if mul(mul(v[0],v[1]),v[2])==4:expected.add(tuple(v))
assert found==expected,(len(expected),found.symmetric_difference(expected))
print('CIANI_CHAR7_F49_EXHAUSTIVE_23_TRANSVERSE_POINTS_OK')
print('branch_counts',sorted(type_counts.items()))
print('field_counts',sorted(field_counts.items()))
print('singular_boundary_candidates',len(bad))
