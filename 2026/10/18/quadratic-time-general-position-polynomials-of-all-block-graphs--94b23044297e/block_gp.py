"""Exact general-position polynomial of a connected block graph.

Input: n >= 1 and an iterable of unordered edges (u,v), 0 <= u,v < n.
Output: coefficients [a_0,...,a_n] of sum a_k z^k.
Uses only the Python standard library. Rejects non-block graphs.
"""
import sys

def polyadd(a,b):
 out=[0]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=x
 return out

def polymul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):out[i+j]+=x*y
 return out

def _blocks(n,edges):
 if n<1:raise ValueError('n must be positive')
 E=set()
 for u,v in edges:
  if not(0<=u<n and 0<=v<n and u!=v):raise ValueError('invalid edge')
  if u>v:u,v=v,u
  if (u,v) in E:raise ValueError('parallel edge')
  E.add((u,v))
 adj=[[] for _ in range(n)]
 for u,v in E:adj[u].append(v);adj[v].append(u)
 disc=[-1]*n;low=[0]*n;stack=[];out=[];clock=[0]
 sys.setrecursionlimit(max(sys.getrecursionlimit(),n*5+100))
 def dfs(v,parent):
  disc[v]=low[v]=clock[0];clock[0]+=1
  for w in adj[v]:
   if disc[w]<0:
    stack.append((v,w));dfs(w,v);low[v]=min(low[v],low[w])
    if low[w]>=disc[v]:
     block=set()
     while True:
      e=stack.pop();block.update(e)
      if e==(v,w):break
     out.append(sorted(block))
   elif w!=parent and disc[w]<disc[v]:
    stack.append((v,w));low[v]=min(low[v],disc[w])
 dfs(0,-1)
 if -1 in disc:raise ValueError('graph not connected')
 for block in out:
  for i,u in enumerate(block):
   for v in block[i+1:]:
    if (u,v) not in E:raise ValueError('graph is not a block graph')
 return out

def gp_polynomial(n,edges):
 """Compute every general-position-set count in O(n^2) coefficient operations
 after the graph's block decomposition (including all bookkeeping).
 """
 blocks=_blocks(n,edges)
 if n==1:return [1,1]
 T=[[] for _ in range(n+len(blocks))]
 for j,vs in enumerate(blocks):
  b=n+j
  for v in vs:T[b].append(v);T[v].append(b)
 def rec(v,parent):
  child=[rec(w,v) for w in T[v] if w!=parent]
  P=[1];B=[0];AS=[0]
  for A,C in child:
   P=polymul(P,polyadd([1],A))
   B=polyadd(B,C)
   AS=polyadd(AS,A)
  P=polyadd(P,[-1])
  if v<n:return polyadd(P,[0,1]),polyadd(B,[0]+AS)
  return P,B
 A,B=rec(n,-1)
 p=polyadd([1],polyadd(A,B))
 return p+[0]*(n+1-len(p))

if __name__=='__main__':
 print(gp_polynomial(7,[(0,1),(0,2),(1,2),(2,3),(2,4),(3,4),(4,5),(4,6),(5,6)]))
