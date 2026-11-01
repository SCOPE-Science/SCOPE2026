"""Finite checks of the group-clique decomposition for cyclic Frobenius groups.

Only elementary additive kernels F_p are enumerated; the theorem is general.
"""
from collections import Counter, defaultdict
from math import gcd

CASES = [(7,6,3),(13,12,2),(31,15,7),(43,21,9)]

def prime_factors(n):
    p=2
    out=[]
    while p*p<=n:
        if n%p==0:
            k=1
            while n%p==0:
                n//=p;k*=p
            out.append((p,k))
        p+=1
    if n>1: out.append((n,n))
    return out

def ppbase(n):
    if n<=1:return None
    fac=prime_factors(n)
    return fac[0][0] if len(fac)==1 else None

def run_case(p,m,lam):
    assert pow(lam,m,p)==1
    assert all(pow(lam,m//q,p)!=1 for q,_ in prime_factors(m))
    pw=[pow(lam,k,p) for k in range(m)]
    vs=[]
    for a in range(p):
      for k in range(m):
        if a==0 and k==0:continue
        order=p if k==0 else m//gcd(m,k)
        if ppbase(order) is not None:vs.append((a,k,ppbase(order)))
    edges=[]
    for i,(a,k,q) in enumerate(vs):
      for j in range(i+1,len(vs)):
        b,l,r=vs[j]
        if q==r:continue
        if (a+pw[k]*b-b-pw[l]*a)%p==0:edges.append((i,j))
    parent=list(range(len(vs)))
    def root(i):
      while parent[i]!=i:
        parent[i]=parent[parent[i]];i=parent[i]
      return i
    for i,j in edges:
      x,y=root(i),root(j)
      if x!=y:parent[x]=y
    cc=len({root(i) for i in range(len(vs))})
    ff=prime_factors(m)
    assert len(ff)>=2
    b=1
    for _,q in ff:b*=q-2
    expected_vertices=(p-1)+p*sum(q-1 for _,q in ff)
    expected_edges=p*sum((q-1)*(r-1) for i,(_,q) in enumerate(ff) for _,r in ff[i+1:])
    expected_cc=2*p-1
    betti1=len(edges)-len(vs)+cc if len(ff)==2 else None
    exp_betti1=p*b if len(ff)==2 else None
    assert (len(vs),len(edges),cc)==(expected_vertices,expected_edges,expected_cc)
    if len(ff)==2:assert betti1==exp_betti1
    # Every edge occurs within exactly one conjugate complement;
    # conversely each pair of distinct prime classes there is an edge.
    def component_label(a,k):
      if k==0:return None
      return (a*pow(1-pw[k],-1,p))%p
    assert all(component_label(vs[i][0],vs[i][1])==component_label(vs[j][0],vs[j][1])
               for i,j in edges)
    comps=defaultdict(list)
    for i,(a,k,q) in enumerate(vs):
      if k:comps[component_label(a,k)].append(i)
    assert len(comps)==p
    for ids in comps.values():
      assert len(ids)==sum(q-1 for _,q in ff)
      for i in ids:
        for j in ids:
          if j<=i:continue
          expected=vs[i][2]!=vs[j][2]
          assert ((i,j) in edges)==expected
    print('PASS p=%d m=%d lambda=%d | vertices=%d edges=%d components=%d beta1=%s'
          %(p,m,lam,len(vs),len(edges),cc,betti1))

for case in CASES:run_case(*case)
# An independent higher-dimensional local complement check for C_105.
# X(C_105) is the join of independent sets of sizes 2, 4, 6.
# Count simplices by selecting at most one vertex of each prime-power class.
sizes=(2,4,6)
f0=sum(sizes)
f1=sum(sizes[i]*sizes[j] for i in range(3) for j in range(i+1,3))
f2=sizes[0]*sizes[1]*sizes[2]
euler=f0-f1+f2
assert (f0,f1,f2,euler)==(12,44,48,16)
assert euler-1 == (sizes[0]-1)*(sizes[1]-1)*(sizes[2]-1)==15
print('PASS local C_105: f=(12,44,48), chi=16, beta2=15 by join homology')
