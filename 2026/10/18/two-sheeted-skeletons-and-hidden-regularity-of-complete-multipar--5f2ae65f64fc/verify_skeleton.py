"""Reproducible finite linear-programming comparison for transportation-ball vertex adjacency."""
from itertools import combinations
from scipy.optimize import linprog
import numpy as np

def labels(parts): return [i for i,n in enumerate(parts) for _ in range(n)]
def edges(part):return [(i,j) for i in range(len(part)) for j in range(i+1,len(part)) if part[i]!=part[j]]
def adjacency_formula(a,b,p):
 u,v=a;s,t=b
 if a==(t,s):return False
 if u==s or v==t:return True
 if v==s or u==t:return False
 return p[u]==p[t] or p[s]==p[v]

def adjacency_lp(a,b,p):
 n=len(p); E=edges(p)
 if a[0]==b[1] and a[1]==b[0]: return False
 index={tuple(sorted(e)) for e in (a,b)}
 # Max epsilon, with equality on the two roots and strict margin on other edge constraints
 c=np.zeros(n+1);c[-1]=-1.
 A=[];bb=[]
 for i,j in E:
  if (i,j) in index:continue
  for u,v in [(i,j),(j,i)]:
   row=np.zeros(n+1);row[u]=1;row[v]=-1;row[-1]=1
   A.append(row);bb.append(1.)
 Aeq=[];beq=[]
 for u,v in [a,b]:
  row=np.zeros(n+1);row[u]=1;row[v]=-1
  Aeq.append(row);beq.append(1.)
 row=np.zeros(n+1);row[0]=1
 Aeq.append(row);beq.append(0.)
 result=linprog(c,A_ub=A,b_ub=bb,A_eq=Aeq,b_eq=beq,bounds=[(None,None)]*n+[(0,1)],method='highs')
 return result.success and result.x[-1]>1e-7

def test(parts):
 p=labels(parts);E=edges(p)
 roots=[(i,j) for i,j in E]+[(j,i) for i,j in E]
 ct=0;degrees=[0]*len(roots)
 for x,y in combinations(range(len(roots)),2):
  got=adjacency_lp(roots[x],roots[y],p)
  exp=adjacency_formula(roots[x],roots[y],p)
  if got!=exp:raise AssertionError((parts,roots[x],roots[y],got,exp))
  if got:ct+=1;degrees[x]+=1;degrees[y]+=1
 N=len(p)
 for i,(u,v) in enumerate(roots):
  a,b=parts[p[u]],parts[p[v]]
  degree=2*N-a-b-2+(b-1)*(N-b-1)+(a-1)*(N-a-1)-(a-1)*(b-1)
  if degree!=degrees[i]:raise AssertionError(('degree',parts,(u,v),degree,degrees[i]))
 # Two-sheeted projection check: each pair of base edges gives exactly
 # one incident neighbor per sheet exactly when their part-pairs overlap.
 for e,f in combinations(E,2):
  u,v=e;s,t=f
  covered=bool({p[u],p[v]} & {p[s],p[t]})
  for a in ((u,v),(v,u)):
   if sum(adjacency_formula(a,b,p) for b in ((s,t),(t,s)))!=int(covered):
    raise AssertionError(('cover',parts,e,f,a))
 if len(parts)==3 and len(set(degrees))!=1:raise AssertionError(('tripartite regularity',parts))
 print('PASS',parts, 'dimension',N-1,'vertices',len(roots),'edges',ct,'degree histogram', {d:degrees.count(d) for d in sorted(set(degrees))},flush=True)
 return ct

if __name__=='__main__':
 for parts in [(1,1,1),(2,1,1),(3,1,1),(2,2,1),(2,2,2),(3,2,1),(2,1,1,1),(3,1,1,1),(1,1,1,1)]:test(parts)
 print('ALL LP CROSS-CHECKS PASSED')
