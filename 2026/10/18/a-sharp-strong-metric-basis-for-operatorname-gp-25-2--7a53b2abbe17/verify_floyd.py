"""Floyd-Warshall and local graph certificates for strong metric resolution in GP(25,2)."""
import json
n=25;vertices=2*n;large=1000
mat=[[0 if a==b else large for b in range(vertices)] for a in range(vertices)]
for i in range(n):
  for a,b in ((i,(i+1)%n),(i,n+i),(n+i,n+(i+2)%n)):
    mat[a][b]=mat[b][a]=1
for k in range(vertices):
  for i in range(vertices):
    ik=mat[i][k]
    if ik==large:continue
    for j in range(vertices):
      val=ik+mat[k][j]
      if val<mat[i][j]:mat[i][j]=val
nbr=[{j for j in range(vertices) if mat[i][j]==1} for i in range(vertices)]
mm=set()
for a in range(vertices):
 for b in range(a+1,vertices):
  dab=mat[a][b]
  if max(mat[t][b] for t in nbr[a])<=dab and max(mat[a][t] for t in nbr[b])<=dab:
   mm.add((a,b))
def linked(a,b):return tuple(sorted((a,b))) in mm
# A clique covering for all vertices not adjacent to outer vertex u_0.
cliques=((2,15,22),(4,17,24),(1,6,19),(3,8,21),(10,23))
nonneighbors={i for i in range(1,n) if not linked(0,i)}
assert {i for C in cliques for i in C}==nonneighbors
assert sum(map(len,cliques))==14
for C in cliques:
 assert all(linked(C[i],C[j]) for i in range(len(C)) for j in range(i+1,len(C)))
# Five disjoint odd cycles in the inner mutually-maximally-distant graph.
cycles=[]
for t in range(0,n,5):
 C=[(t+9*k)%n for k in range(5)]
 assert len(set(C))==5
 assert all(linked(n+C[j],n+C[(j+1)%5]) for j in range(5))
 cycles.append(C)
assert set(sum(cycles,[]))==set(range(n))
# Thus any independent set on the outer layer has <= 1+5=6,
# and on the inner layer has <=5*2=10.
outer={0,2,4,6,8,10}
inner={0,2,5,7,10,12,15,17,20,22}
assert all(not linked(a,b) for a in outer for b in outer if a<b)
assert all(not linked(n+a,n+b) for a in inner for b in inner if a<b)
assert all(not linked(a,n+b) for a in range(n) for b in range(n))
assert len(mm)==175
assert len(outer)==6 and len(inner)==10
print(json.dumps({'Floyd_MMD_edges':len(mm),'outer_nonadjacent_to_zero':sorted(nonneighbors),'outer_five_cliques':[list(C) for C in cliques],'outer_independence_upper':6,'inner_odd_cycles':cycles,'inner_independence_upper':10,'constructed_independent_set_size':len(outer)+len(inner),'independence_number':16,'strong_metric_dimension':vertices-16,'2017_conjectured_value_at_k_6':5*6+5},sort_keys=True))
