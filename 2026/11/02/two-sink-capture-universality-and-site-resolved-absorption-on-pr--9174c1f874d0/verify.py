import itertools
import numpy as np
import networkx as nx


def srg_params(a):
 n=len(a);k=int(a[0].sum())
 assert 0<k<n-1
 assert all(int(row.sum())==k for row in a)
 pairs=[(int(a[i]@a[j]), int(a[i,j])) for i in range(n) for j in range(i+1,n)]
 lam=set(t for t,adj in pairs if adj==1)
 mu=set(t for t,adj in pairs if adj==0)
 assert len(lam)==1 and len(mu)==1, (lam,mu)
 return n,k,lam.pop(),mu.pop()

def proj(a):
 n,k,lam,mu=srg_params(a)
 dr=np.sqrt((lam-mu)**2+4*(k-mu))
 r=(lam-mu+dr)/2
 s=(lam-mu-dr)/2
 R=np.full((n,n),1/n)
 Er=(a-s*np.eye(n)-(k-s)*R)/(r-s)
 Es=np.eye(n)-R-Er
 mr=round(np.trace(Er));ms=round(np.trace(Es))
 assert np.max(abs(Er@Er-Er))<1e-9
 return [(r,Er,mr),(s,Es,ms)],R

def test(name,graph):
 a=nx.to_numpy_array(graph,dtype=int).astype(float)
 n,k,lam,mu=srg_params(a)
 theta,R=proj(a)
 q=n-k-1
 maxdiff=0;mineta=2; maxeta=-1; count=0
 for i in range(n):
  for j in range(i+1,n):
   B=np.vstack((np.eye(n)[:,i],np.eye(n)[:,j])).T
   kry=np.column_stack([a@B, a@a@B, B])
   u,sigs,vh=np.linalg.svd(kry,full_matrices=False)
   rank=np.sum(sigs>1e-7)
   assert rank==5,(name,i,j,rank,sigs)
   Q=u[:,:5]@u[:,:5].T
   P=R.copy()
   for eig,E,m in theta:
    t=E@B
    P+=t@np.linalg.inv(B.T@E@B)@t.T
   err=np.max(abs(P-Q))
   maxdiff=max(maxdiff,err)
   assert err<1e-8,(name,err)
   assert abs(np.trace(P)-5)<1e-8
   assert abs(P[i,i]-1)<1e-8 and abs(P[j,j]-1)<1e-8
   assert abs(sum(P[x,x] for x in range(n) if x not in (i,j))-3)<1e-8
   for x in range(n):
    formula=1/n
    for eig,E,m in theta:
     def coeff(z,y):
      if z==y:return 1.
      return eig/k if a[z,y]==1 else -(1+eig)/q
     c=coeff(i,j);d=coeff(x,i);e=coeff(x,j)
     formula+=(m/n)*(d*d+e*e-2*c*d*e)/(1-c*c)
    assert abs(formula-P[x,x])<1e-8,(name,i,j,x,formula,P[x,x])
    if x not in (i,j):
     mineta=min(mineta,formula); maxeta=max(maxeta,formula)
   count+=1
 print(name, (n,k,lam,mu), 'pairs',count, 'maxdiff', maxdiff, 'nontrap range',mineta,maxeta,'mean',3/(n-2))


def shrikhande_graph():
 g=nx.Graph();vs=list(itertools.product(range(4),repeat=2));g.add_nodes_from(vs)
 for a,b in vs:
  for da,db in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)]:
   g.add_edge((a,b),((a+da)%4,(b+db)%4))
 return g

def clebsch_graph():
 g=nx.hypercube_graph(4)
 for a in list(g.nodes):g.add_edge(a,tuple(1-x for x in a))
 return g

def graph_mat(a):
 return nx.from_numpy_array(np.array(a,dtype=int))

def hamming_graph():
 return nx.cartesian_product(nx.complete_graph(4),nx.complete_graph(4))

def triangular_graph(n):
 pairs=list(itertools.combinations(range(n),2))
 g=nx.Graph();g.add_nodes_from(range(len(pairs)))
 for i in range(len(pairs)):
  for j in range(i+1,len(pairs)):
   if len(set(pairs[i])&set(pairs[j]))>0:g.add_edge(i,j)
 return g

def paley_graph(p):
 residues={x*x%p for x in range(1,p)}
 return nx.from_numpy_array(np.array([[0 if i==j else int((i-j)%p in residues) for j in range(p)] for i in range(p)]))

def cocktail_graph(m):
 g=nx.complete_graph(2*m)
 for i in range(m):g.remove_edge(2*i,2*i+1)
 return g

if __name__=='__main__':
 for name,g in [
 ('C5',nx.cycle_graph(5)),
 ('Petersen',nx.petersen_graph()),
 ('Rook4x4',hamming_graph()),
 ('Shrikhande',shrikhande_graph()),
 ('Triangular6',triangular_graph(6)),
 ('Paley13',paley_graph(13)),
 ('Clebsch',clebsch_graph()),
 ]:
  test(name,g)
 for name,g,pairs in [('Cocktail6',cocktail_graph(3),[(0,1),(0,2)]),('K222',nx.complete_multipartite_graph(2,2,2),[(0,1),(0,2)])]:
  a=nx.to_numpy_array(g);n=a.shape[0]
  for i,j in pairs:
   B=np.vstack([np.eye(n)[:,i],np.eye(n)[:,j]]).T
   kry=np.column_stack([B,a@B,a@a@B])
   print(name,(i,j),'bright_dim',np.linalg.matrix_rank(kry, tol=1e-8),'capture_mix',np.linalg.matrix_rank(kry, tol=1e-8)/n)
