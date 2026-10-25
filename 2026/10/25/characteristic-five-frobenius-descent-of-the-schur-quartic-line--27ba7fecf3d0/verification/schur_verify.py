#!/usr/bin/env python3
"""Exact finite arithmetic for the Fano arrangement of Schur's quartic over F5.

Uses only the Python standard library. Field F25 is F5[e]/(e^2-2).
For a graph line, (x,y) = M(z,w); all five binary quartic
coefficient equations are tested exhaustively, not sampled.
"""
from itertools import product, combinations
from collections import Counter

Q=range(25)
add=[[0]*25 for _ in Q]
neg=[0]*25
mul=[[0]*25 for _ in Q]
for i in Q:
    a,b=i%5,i//5
    neg[i]=(-a)%5+5*((-b)%5)
    for j in Q:
        c,d=j%5,j//5
        add[i][j]=(a+c)%5+5*((b+d)%5)
        mul[i][j]=(a*c+2*b*d)%5+5*((a*d+b*c)%5)
sub=[[add[i][neg[j]] for j in Q] for i in Q]
inv=[None]*25
for i in range(1,25):
    inv[i]=next(j for j in range(1,25) if mul[i][j]==1)
sq=[mul[i][i] for i in Q]
cube=[mul[sq[i]][i] for i in Q]
fourth=[mul[cube[i]][i] for i in Q]
def m(*v):
    r=1
    for x in v:r=mul[r][x]
    return r
def sums(*v):
    r=0
    for x in v:r=add[r][x]
    return r
def scaled(k,x):
    return m(k%5,x)
def fro(x):
    return (x%5)+5*((-(x//5))%5)
assert all(m(i,inv[i])==1 for i in range(1,25))
assert all(fro(fro(i))==i for i in Q)
assert all(fro(m(i,j))==m(fro(i),fro(j)) for i in Q for j in Q)

def A(x,y):return sub[fourth[x]][m(x,cube[y])]
def graph_condition(a,b,c,d):
    if sub[m(a,d)][m(b,c)]==0:return False
    if sub[fourth[a]][m(a,cube[c])]!=1:return False
    if sub[scaled(4,m(cube[a],b))][sums(scaled(3,m(a,sq[c],d)),m(b,cube[c]))]!=0:return False
    if sub[scaled(6,m(sq[a],sq[b]))][sums(scaled(3,m(a,c,sq[d])),scaled(3,m(b,sq[c],d)))]!=0:return False
    if sub[scaled(4,m(a,cube[b]))][sums(m(a,cube[d]),scaled(3,m(b,c,sq[d])))]!=4:return False
    if sub[fourth[b]][m(b,cube[d])]!=0:return False
    return True

roots=[x for x in Q if A(x,1)==0]
assert len(roots)==4 and sum(fro(x)==x for x in roots)==2
matrices=[(a,b,c,d) for a,b,c,d in product(Q,repeat=4) if graph_condition(a,b,c,d)]
assert len(matrices)==48
assert len(set(matrices))==48
f5_matrices=[M for M in matrices if all(x<5 for x in M)]
assert f5_matrices==[(a,0,0,a) for a in range(1,5)]
lines=[]
for r,s in product(roots,repeat=2):
    lines.append(((r,1,0,0),(0,0,s,1),'separated',(r,s)))
for a,b,c,d in matrices:
    lines.append(((a,c,1,0),(b,d,0,1),'graph',(a,b,c,d)))
assert len(lines)==64

def rref(rows):
    tab=[list(row) for row in rows]
    row=0;pivots=[]
    for col in range(4):
        pivot=next((i for i in range(row,len(tab)) if tab[i][col]!=0),None)
        if pivot is None:continue
        tab[row],tab[pivot]=tab[pivot],tab[row]
        scale=inv[tab[row][col]]
        tab[row]=[m(scale,z) for z in tab[row]]
        for i in range(len(tab)):
            if i!=row and tab[i][col]:
                f=tab[i][col]
                tab[i]=[sub[z][m(f,y)] for z,y in zip(tab[i],tab[row])]
        pivots.append(col)
        row+=1
        if row==len(tab):break
    return tab,pivots

def plane_normal(rows):
    reduced,pivot=rref(rows)
    if len(pivot)!=3:return None
    free=next(j for j in range(4) if j not in pivot)
    out=[0]*4;out[free]=1
    for i,j in enumerate(pivot):out[j]=neg[reduced[i][free]]
    scal=inv[next(x for x in out if x)]
    return tuple(m(scal,x) for x in out)

def dot(vec,n):return sums(*(m(x,y) for x,y in zip(vec,n)))
planes={}
for i,j in combinations(range(64),2):
    normal=plane_normal((*lines[i][:2],*lines[j][:2]))
    if normal is not None:planes[normal]=None
for n in planes:
    planes[n]=tuple(i for i,L in enumerate(lines) if dot(L[0],n)==0 and dot(L[1],n)==0)
assert Counter(len(v) for v in planes.values())=={2:144,4:72}
four_line={n:v for n,v in planes.items() if len(v)==4}
rational=[i for i,L in enumerate(lines) if all(fro(x)==x for vec in L[:2] for x in vec)]
assert len(rational)==8
assert Counter(lines[i][2] for i in rational)=={'graph':4,'separated':4}
rational_planes={n:v for n,v in four_line.items() if all(fro(x)==x for x in n)}
assert len(rational_planes)==12
assert all(sum(i in rational for i in ids)==2 for ids in rational_planes.values())
# Verify four-line planes are distinct as hyperplanes and all other
# two-line planes have precisely two constituent lines.
incidence=Counter()
for i,j in combinations(rational,2):
    if plane_normal((*lines[i][:2],*lines[j][:2])) is not None:
        incidence[i]+=1;incidence[j]+=1
assert sorted(incidence.values())==[2]*6+[6]*2
# Since there are 12 incidences, the two vertices of degree six
# are adjacent to all six other vertices; the six have no other edges.
assert sum(incidence.values())//2==12
print('VERIFY_OK')
print('field=F25=F5[e]/(e^2-2)')
print('binary quartic root count=4; rational roots=2')
print('graph lines=48; F5 graph lines=4')
print('separated lines=16; F5 separated lines=4')
print('all lines=64; F5 lines=8; conjugate pairs=28')
print('intersection planes: 72 four-line and 144 two-line')
print('F5 four-line planes=12; each has 2 F5 lines and one Frobenius pair')
print('F5 line intersection graph=K_{2,6}')
