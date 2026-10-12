#!/usr/bin/env python3
"""Finite checks for the symplectic classification of group Rota--Baxter maps.
All computations use explicit finite-field group products, independent of symbolic proof.
"""
from itertools import product
from math import prod

def omega(v,w,p):
    n=len(v)//2
    return sum(v[i]*w[n+i]-v[n+i]*w[i] for i in range(n))%p

def add(v,w,p):return tuple((a+b)%p for a,b in zip(v,w))
def matvec(rows,v,p):return tuple(sum(a*b for a,b in zip(row,v))%p for row in rows)
def law(g,h,p):
    v,z=g;w,t=h
    return (add(v,w,p),(z+t+pow(2,-1,p)*omega(v,w,p))%p)
def inverse(g,p):return (tuple(-x%p for x in g[0]),-g[1]%p)
def B_of(rows,alpha,ell,g,p):
    v,z=g; Lv=matvec(rows,v,p)
    return Lv,(alpha*z+sum(a*b for a,b in zip(ell,v))-alpha*pow(2,-1,p)*omega(Lv,v,p))%p

def criterion(rows,alpha,p):
    d=len(rows)
    E=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    for v in E:
      for w in E:
        lv=matvec(rows,v,p);lw=matvec(rows,w,p)
        if (omega(lv,lw,p)-alpha*(omega(v,w,p)+omega(lv,w,p)+omega(v,lw,p)))%p:return False
    return True

def group_valid(rows,alpha,ell,p,n,maxpairs=None):
    Vs=list(product(range(p),repeat=2*n))
    G=[(v,z) for v in Vs for z in range(p)]
    B={g:B_of(rows,alpha,ell,g,p) for g in G}
    if maxpairs is None:
      pairs=((g,h) for g in G for h in G)
    else:
      # Deterministic spread across coordinates; NOT exhaustive.
      from random import Random
      rng=Random(1717+p*37+n)
      pairs=((G[rng.randrange(len(G))],G[rng.randrange(len(G))]) for _ in range(maxpairs))
    for g,h in pairs:
        bg=B[g]
        lhs=law(bg,B[h],p)
        rhs=B[law(law(g,bg,p),law(h,inverse(bg,p),p),p)]
        if lhs!=rhs:return False
    return True

def zero_stratum_count(p,n):
    # Gaussian factor [n choose r]_p, isotropic Grassmannian count.
    total=0; ranks=[]
    for r in range(n+1):
      ga=prod(p**(n-i)-1 for i in range(r))//prod(p**(r-i)-1 for i in range(r)) if r else 1
      # Integer division of entire rational product, not each factor.
      iso=ga*prod(p**(n-i)+1 for i in range(r))
      onto=prod(p**(2*n)-p**i for i in range(r))
      ranks.append((r,iso,onto,iso*onto))
      total+=iso*onto
    return p**(2*n)*total,ranks

def independent_symplectic_counts():
    p=3
    Vs=[v for v in product(range(p),repeat=4) if any(v)]
    lines={frozenset(tuple((c*x)%p for x in v) for c in range(p)) for v in Vs}
    assert len(lines)==40
    planes=set()
    for v in Vs:
      for w in Vs:
        if omega(v,w,p):continue
        span=frozenset(tuple((a*x+b*y)%p for x,y in zip(v,w)) for a in range(p) for b in range(p))
        if len(span)==p*p:planes.add(span)
    assert len(planes)==40,len(planes)
    U=frozenset((a,b,0,0) for a in range(p) for b in range(p))
    zero=(0,0,0,0)
    complements=sum(1 for W in planes if W.intersection(U)=={zero})
    assert complements==27,complements
    return len(lines),len(planes),complements

def run():
    assert independent_symplectic_counts()==(40,40,27)
    for p in [3,5,7]:
      total,rows=zero_stratum_count(p,2)
      assert rows[0][3]==1
      assert rows[1][1]==(p**4-1)//(p-1)
      assert rows[2][1]==(p+1)*(p*p+1)
      assert total>0
    # All quotient-linear operators in dimension 2, p=3. The group law is checked
    # for one canonical quadratic central function on all candidates, including
    # those failing the matrix criterion, and for every central linear twist on
    # each admissible candidate.
    p=3;n=1;D=2
    C={alpha:0 for alpha in range(p)}
    tested=0
    for entries in product(range(p),repeat=D*D):
      rows=tuple(entries[i*D:(i+1)*D] for i in range(D))
      for alpha in range(p):
        valid=criterion(rows,alpha,p)
        ok=group_valid(rows,alpha,(0,0),p,n)
        assert ok==valid,(rows,alpha,ok,valid)
        tested+=1
        if valid:
          C[alpha]+=1
          for ell in product(range(p),repeat=D):
            assert group_valid(rows,alpha,ell,p,n),(rows,alpha,ell)
    assert C[0]==C[p-1]==33,C
    # 5-dimensional odd extraspecial example: the extremal central scalars,
    # Lagrangian splitting maps, and a nonsplitting invertible example over F5.
    for p in [3,5]:
      n=2; D=4
      def diag(a):return tuple(tuple(a[i] if i==j else 0 for j in range(D)) for i in range(D))
      for alpha,a in [(0,(1,1,0,0)),(p-1,(0,0,p-1,p-1)),(1,(p-1,p-1,0,0))]:
        rows=diag(a)
        assert criterion(rows,alpha,p),(p,alpha,rows)
        assert group_valid(rows,alpha,(1,2,0,1),p,n,maxpairs=None if p==3 else 8000),(p,alpha,rows)
      if p==5:
        rows=diag((2,2,3,3));alpha=1
        assert criterion(rows,alpha,p)
        assert group_valid(rows,alpha,(1,2,3,4),p,n,maxpairs=8000)
    # Exhaust matrix condition for p=5, n=1, plus checks of boundary counts.
    p=5;n=1; counts={a:0 for a in range(p)}
    for entries in product(range(p),repeat=4):
      rows=(entries[:2],entries[2:])
      for a in range(p):
        if criterion(rows,a,p):counts[a]+=1
    zero,_=zero_stratum_count(p,1)
    assert counts[0]==counts[p-1]==zero//p**2,(counts,zero)
    print('VERIFY_OK',{'all_small_matrices':tested,'p3_counts_by_alpha':C,'p5_counts_by_alpha':counts,'p3_n2_alpha0_count':zero_stratum_count(3,2)[0],'p3_n2_lagrangian_rank_sector':3**4*(3+1)*(3**2+1)*3**3})

if __name__=='__main__':run()
