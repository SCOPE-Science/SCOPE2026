#!/usr/bin/env python3
"""Complete rational-line incidence calculation for the Klein cubic over F9.
Deterministic standard-library exact arithmetic. All 2-planes are RREF-enumerated.
"""
from itertools import combinations,product
from collections import Counter,deque

P=3;Q=9
# alpha^2=2 over F_3; x=3b+a represents a+b alpha.
DIG=[[x%3,x//3] for x in range(9)]
ADD=[[((DIG[x][0]+DIG[y][0])%3)+3*((DIG[x][1]+DIG[y][1])%3) for y in range(9)] for x in range(9)]
MUL=[[((DIG[x][0]*DIG[y][0]+2*DIG[x][1]*DIG[y][1])%3)+3*((DIG[x][0]*DIG[y][1]+DIG[x][1]*DIG[y][0])%3) for y in range(9)] for x in range(9)]
NEG=[MUL[2][x] for x in range(9)]
SUB=lambda a,b:ADD[a][NEG[b]]
INV=[None]+[next(y for y in range(1,9) if MUL[x][y]==1) for x in range(1,9)]
assert all(len(set(MUL[a]))==9 for a in range(1,9))

def f_coeff(a,b):
    z=[0]*4
    for i in range(5):
      j=(i+1)%5
      x,y,u,v=a[i],b[i],a[j],b[j]
      xx,yy,xy=MUL[x][x],MUL[y][y],MUL[x][y]
      z[0]=ADD[z[0]][MUL[xx][u]]
      z[1]=ADD[z[1]][ADD[MUL[xx][v]][MUL[2][MUL[xy][u]]]]
      z[2]=ADD[z[2]][ADD[MUL[yy][u]][MUL[2][MUL[xy][v]]]]
      z[3]=ADD[z[3]][MUL[yy][v]]
    return z

def canonical(a):
  a=[list(row) for row in a];r=0
  for j in range(5):
    k=next((k for k in range(r,len(a)) if a[k][j]),None)
    if k is None:continue
    a[r],a[k]=a[k],a[r]
    a[r]=[MUL[INV[a[r][j]]][v] for v in a[r]]
    for i in range(len(a)):
      if i!=r and a[i][j]:
        t=a[i][j]
        a[i]=[SUB(u,MUL[t][v]) for u,v in zip(a[i],a[r])]
    r+=1
    if r==len(a):break
  return r,tuple(tuple(row) for row in a)

def make_lines():
  S=[];total=0
  for piv in combinations(range(5),2):
    free=[(i,j) for i in range(2) for j in range(piv[i]+1,5) if j not in piv]
    for vals in product(range(9),repeat=len(free)):
      a=[[0]*5 for i in range(2)]
      for i,k in enumerate(piv):a[i][k]=1
      for (i,j),v in zip(free,vals):a[i][j]=v
      total+=1
      if f_coeff(*a)==[0,0,0,0]:S.append(tuple(map(tuple,a)))
  assert total==605242
  return S

def calculate():
 S=make_lines();assert len(S)==82
 A=[set() for _ in S];edges=0
 for i in range(len(S)):
  for j in range(i+1,len(S)):
    r,_=canonical(S[i]+S[j])
    if r==3:A[i].add(j);A[j].add(i);edges+=1
 assert edges==350
 degrees=Counter(map(len,A))
 assert degrees=={4:5,6:20,8:15,10:32,12:10},degrees
 triangles=sum(len(A[i]&A[j]) for i in range(82) for j in A[i] if i<j)//3
 assert triangles==190
 seen={0};queue=deque([0])
 while queue:
  for j in A[queue.popleft()]:
   if j not in seen:seen.add(j);queue.append(j)
 assert len(seen)==82
 fixed=[i for i,s in enumerate(S) if all(x<3 for row in s for x in row)]
 assert len(fixed)==10
 induced=[A[i]&set(fixed) for i in fixed]
 assert Counter(map(len,induced))=={0:5,2:5}
 assert sum(len(x) for x in induced)//2==5
 # Five degree-two vertices form one C5.
 v0=next(i for i in fixed if len(A[i]&set(fixed))==2)
 seen_cycle={v0};queue=deque([v0])
 while queue:
   for j in A[queue.popleft()]&set(fixed):
    if j not in seen_cycle:seen_cycle.add(j);queue.append(j)
 assert len(seen_cycle)==5
 # Cyclic coordinate symmetry, and 3-Frobenius on the coefficient field.
 index={x:i for i,x in enumerate(S)}
 cyc=[];fr=[]
 for s in S:
  r,c=canonical([row[1:]+row[:1] for row in s]);assert r==2
  cyc.append(index[c])
  r,c=canonical([[MUL[MUL[x][x]][x] for x in row] for row in s]);assert r==2
  fr.append(index[c])
 assert all(cyc[cyc[cyc[cyc[cyc[i]]]]]==i for i in range(82))
 assert all(fr[fr[i]]==i for i in range(82))
 assert all({cyc[j] for j in A[i]}==A[cyc[i]] for i in range(82))
 assert all({fr[j] for j in A[i]}==A[fr[i]] for i in range(82))
 cyc_fixed=[i for i in range(82) if cyc[i]==i]
 assert len(cyc_fixed)==2
 assert fr[cyc_fixed[0]]==cyc_fixed[1] and fr[cyc_fixed[1]]==cyc_fixed[0]
 assert cyc_fixed[1] not in A[cyc_fixed[0]]
 assert all(len(A[i])==10 for i in cyc_fixed)
 assert all(fr[i]==i for i in fixed)
 assert all(fr[i]!=i for i in range(82) if i not in fixed)
 print('RREF_Grassmannian=605242')
 print('contained_F9_lines=82')
 print('F9_incidence_edges=350')
 print('F9_degree_distribution='+str(sorted(degrees.items())))
 print('F9_incidence_triangles='+str(triangles))
 print('F9_incidence_graph_connected=True')
 print('F3_fixed_lines=10; induced_graph=C5_disjoint_union_5K1')
 print('C5_coordinate_shift_fixed_F9_lines=2; swapped_by_Frobenius=True; disjoint=True; degree=10')
 print('VERIFY_OK')
if __name__=='__main__':calculate()
