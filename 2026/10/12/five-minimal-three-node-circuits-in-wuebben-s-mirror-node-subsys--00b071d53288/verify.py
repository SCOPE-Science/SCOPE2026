#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
from math import gcd
from functools import reduce

V = [
(1,0,0,0),(0,1,0,0),(1,-1,0,0),(0,0,1,0),(0,0,0,1),(0,0,1,-1),
(0,0,-1,1),(0,0,0,-1),(0,0,-1,0),(-1,1,0,0),(0,-1,0,0),(-1,1,-1,1),
(0,-1,0,-1),(0,-1,-1,0),(-1,1,-1,0),(-1,0,0,-1),(-1,0,-1,1),
(-1,-1,0,-1),(-2,1,-1,1),(-2,1,-1,0),(-1,-1,-1,0),(-2,0,-1,0)
]

def vgcd(xs):
    vals=[abs(int(x)) for x in xs if x]
    return reduce(gcd,vals,0) or 1

def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def normal4(points):
    p0=points[0]
    A=[[points[i][j]-p0[j] for j in range(4)] for i in range(1,4)]
    out=[]
    for j in range(4):
        M=[[row[k] for k in range(4) if k!=j] for row in A]
        out.append(((-1)**j)*det3(M))
    return tuple(out)

def rank_q(rows):
    if not rows:
        return 0
    M=[[Fraction(x) for x in row] for row in rows]
    m,n=len(M),len(M[0])
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if M[i][c]),None)
        if p is None:
            continue
        M[r],M[p]=M[p],M[r]
        z=M[r][c]
        M[r]=[x/z for x in M[r]]
        for i in range(m):
            if i==r or not M[i][c]:
                continue
            z=M[i][c]
            M[i]=[M[i][k]-z*M[r][k] for k in range(n)]
        r+=1
        if r==m:
            break
    return r

def affine_rank(points):
    if len(points)<=1:
        return 0
    return rank_q([[points[i][j]-points[0][j] for j in range(4)]
                   for i in range(1,len(points))])

def facets(vertices):
    out={}
    for S in combinations(range(len(vertices)),4):
        u=normal4([vertices[i] for i in S])
        if u==(0,0,0,0):
            continue
        c=sum(u[j]*vertices[S[0]][j] for j in range(4))
        vals=[sum(u[j]*x[j] for j in range(4)) for x in vertices]
        if all(x<=c for x in vals):
            pass
        elif all(x>=c for x in vals):
            u=tuple(-x for x in u); c=-c; vals=[-x for x in vals]
        else:
            continue
        g=vgcd(u)
        u=tuple(x//g for x in u)
        c=Fraction(c,g)
        I=frozenset(i for i,x in enumerate(vals) if Fraction(x,g)==c)
        out[(u,c)]=I
    return [(u,c,I) for (u,c),I in out.items()]

def two_faces(vertices,facs):
    out={}
    for i,j in combinations(range(len(facs)),2):
        I=facs[i][2] & facs[j][2]
        if len(I)>=3 and affine_rank([vertices[k] for k in I])==2:
            out.setdefault(I,set()).update((i,j))
    return list(out)

def diagonal_relation(vertices,face):
    face=tuple(sorted(face))
    pts=[vertices[i] for i in face]
    pairings=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
    good=[]
    for left,right in pairings:
        L=tuple(pts[left[0]][j]+pts[left[1]][j] for j in range(4))
        R=tuple(pts[right[0]][j]+pts[right[1]][j] for j in range(4))
        if L==R:
            good.append((left,right))
    assert len(good)==1
    left,right=good[0]
    row=[0]*len(vertices)
    for k in left:
        row[face[k]]=1
    for k in right:
        row[face[k]]=-1
    return face,row

f=facets(V)
assert len(f)==26 and all(c==1 for _,c,_ in f)
polar=[tuple(-x for x in u) for u,c,I in f]
pf=facets(polar)
assert len(pf)==22 and all(c==1 for _,c,_ in pf)
faces=two_faces(polar,pf)
squares=sorted(tuple(sorted(F)) for F in faces if len(F)==4)
assert len(squares)==26

records=[diagonal_relation(polar,F) for F in squares]
rows=[r for F,r in records]
assert rank_q(rows)==18

deletion_ranks=[rank_q(rows[:i]+rows[i+1:]) for i in range(26)]
coloops=[i for i,r in enumerate(deletion_ranks) if r<18]
assert coloops==[8,10]
assert [tuple(v+1 for v in records[i][0]) for i in coloops] == [
    (3,9,19,23),(4,10,15,24)
]
assert rank_q([r for i,r in enumerate(rows) if i not in coloops])==16

# Complete search for all 1-, 2-, and 3-row dependent supports.
# A 3-row dependent support is automatically a circuit because no 1- or 2-row dependence exists.
assert all(any(x for x in r) for r in rows)
two=[C for C in combinations(range(26),2) if rank_q([rows[i] for i in C])<2]
assert two==[]
three=[C for C in combinations(range(26),3) if rank_q([rows[i] for i in C])<3]
expected=[(6,7,21),(11,13,19),(12,13,22),(16,17,24),(18,19,25)]
assert three==expected

expected_faces=[
    [(3,5,13,16),(3,5,23,25),(13,16,23,25)],
    [(5,6,11,12),(5,6,25,26),(11,12,25,26)],
    [(5,6,15,16),(5,6,25,26),(15,16,25,26)],
    [(10,12,18,20),(10,12,24,26),(18,20,24,26)],
    [(11,12,19,20),(11,12,25,26),(19,20,25,26)]
]
actual_faces=[[tuple(v+1 for v in records[i][0]) for i in C] for C in three]
assert actual_faces==expected_faces

# Each listed circuit has a primitive ±1 dependence; check the displayed signs.
signs=[
    (1,-1,1),
    (1,-1,1),
    (1,-1,-1),
    (1,-1,1),
    (1,-1,1),
]
for C,s in zip(three,signs):
    total=[sum(s[j]*rows[C[j]][k] for j in range(3)) for k in range(26)]
    assert total==[0]*26

print("polar_vertices=26")
print("square_node_rows=26")
print("row_rank=18")
print("coloop_rows_one_based=9,11")
print("rank_after_deleting_both_coloops=16")
print("dependent_pairs=0")
print("three_row_circuits=5")
for i,(C,F,s) in enumerate(zip(three,actual_faces,signs),1):
    print(f"circuit_{i}_row_indices_one_based={tuple(x+1 for x in C)}")
    print(f"circuit_{i}_square_faces_one_based={F}")
    print(f"circuit_{i}_coefficients={s}")
print("VERIFY_OK")
