"""Exact-rational checks for bounded-edge-error gradient reconstruction on bicyclic graphs.

No finite enumeration in this file is used as proof of the all-size theorem.
"""
from fractions import Fraction as F
import itertools
import networkx as nx
import sympy as sp

checks=0

def assert_equal(a,b,msg=''):
 global checks
 assert a==b,(msg,a,b)
 checks+=1

def P_matrix(G):
 edges=sorted(tuple(sorted(e)) for e in G.edges())
 verts=sorted(G.nodes())
 B=sp.zeros(len(verts),len(edges));ind={v:i for i,v in enumerate(verts)}
 for j,(a,b) in enumerate(edges): B[ind[a],j]=1;B[ind[b],j]=-1
 C=sp.Matrix.hstack(*B.nullspace())
 assert C.cols==2
 return sp.eye(len(edges))-C*(C.T*C).inv()*C.T,edges

def norm(P): return max(sum(abs(P[i,j]) for j in range(P.cols)) for i in range(P.rows))

def theta(L):
 G=nx.Graph();G.add_nodes_from((0,1));p=2; branches=[]
 for length in L:
  cur=0;branch=[]
  for i in range(length):
   nex=1 if i==length-1 else p
   if nex==p:p+=1
   G.add_edge(cur,nex);branch.append(tuple(sorted((cur,nex))))
   cur=nex
  branches.append(branch)
 return G,branches

def R(L):
 S=sum((F(1,z) for z in L),F(0));return [F(2)-F(2,x)+F(x+2,x*x)/S for x in L]

def M(m):
 if m==5:return F(3,2)
 if m==6:return F(5,3)
 if m%2:return F(3*(m-1),m+3)
 return F(3*m*(m-2),m*m+2*m-4)

def extremal_lengths(m):
 if m==6:return (2,2,2)
 return (1,(m-1)//2,m//2)

# Check each parametrized arm triple, exact row sums and exact best topology.
for m in range(5,24):
 triples=[]
 for a in range(1,m):
  for b in range(max(2,a),m):
   c=m-a-b
   if c<max(b,2):continue
   triples.append((a,b,c))
   G,paths=theta((a,b,c));P,edges=P_matrix(G)
   rows=[sum(abs(P[i,j]) for j in range(P.cols)) for i in range(P.rows)]
   expected=R((a,b,c));edgidx={e:i for i,e in enumerate(edges)}
   for z,path in enumerate(paths):
    for e in path:assert_equal(rows[edgidx[e]],expected[z],f'row {m} {(a,b,c)} {e}')
   assert_equal(max(rows),max(expected),'theta norm')
   assert_equal(nx.is_connected(G),True,'connected')
  
 if m<=17:
  extrema=[]
  for a in range(1,m):
   for b in range(max(2,a),m):
    c=m-a-b
    if c<max(b,2):continue
    extrema.append((max(R((a,b,c))),(a,b,c)))
  best=max(q[0] for q in extrema)
  assert_equal(best,M(m),f'best value m={m}')
  assert_equal([q[1] for q in extrema if q[0]==best],[extremal_lengths(m)],f'unique m={m}')

# Independent graph atlas classification for all connected, simple bicyclic atlas graphs.
for G in nx.graph_atlas_g():
 if len(G)<4 or not nx.is_connected(G):continue
 m=G.number_of_edges()
 if m-len(G)+1 !=2:continue
 P,edges=P_matrix(G)
 assert_equal(norm(P)<=M(m),True,f'atlas m={m} {edges}')
 if norm(P)==M(m):
  H,_=theta(extremal_lengths(m))
  assert_equal(nx.is_isomorphic(G,H),True,f'equality m={m}')

# Analytical finite crossover and strict growth assertions (not a substitute for proof).
for m in range(5,60):
 assert_equal(M(m)<M(m+1),True,'monotonic')
 assert_equal((M(m)>2)==(m>=10),True,'above two threshold')
print('ALL EXACT CHECKS PASSED:',checks)
