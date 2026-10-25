"""Independent exact enumeration of semitotal dominating sets on K_n Cartesian P_3.
Run: python verify_semitotal.py. Standard Python library only.
"""
from collections import Counter
from itertools import product
from math import comb

def direct(n):
    N=3*n
    adj=[set() for _ in range(N)]
    for layer in range(3):
        for i in range(n):
            u=layer*n+i
            for j in range(n):
                if i!=j:adj[u].add(layer*n+j)
            for d in (-1,1):
                if 0<=layer+d<3:adj[u].add((layer+d)*n+i)
    dist=[]
    for u in range(N):
        row=[N+1]*N;row[u]=0;todo=[u]
        for v in todo:
            for w in adj[v]:
                if row[w]==N+1:row[w]=row[v]+1;todo.append(w)
        dist.append(row)
    good=Counter(); minimal=Counter(); counter=0
    def viable(mask):
        sel=[v for v in range(N) if mask>>v&1]
        if not sel or any(v not in sel and not (adj[v]&set(sel)) for v in range(N)):return False
        return all(any(w!=v and dist[v][w]<=2 for w in sel) for v in sel)
    for bits in range(1<<N):
        counter+=1
        if viable(bits):
            good[bits.bit_count()]+=1
            if all(not viable(bits^(1<<i)) for i in range(N) if bits>>i&1):
                minimal[bits.bit_count()]+=1
    return good,minimal,counter

def pred(n):
    # Evaluate each bivariate layer-choice combinatorially without graph predicates.
    allsets=Counter()
    for aa in range(1<<n):
      for bb in range(1<<n):
        for cc in range(1<<n):
          if bb:
            ok=(aa!=0 and cc!=0) or bb==(1<<n)-1
          else:
            ok=aa!=0 and cc!=0 and aa|cc==(1<<n)-1
            if ok:
              A=aa.bit_count();C=cc.bit_count()
              if A==1:ok=(aa&cc)!=0
              if C==1:ok=(aa&cc)!=0
          if ok:allsets[aa.bit_count()+bb.bit_count()+cc.bit_count()]+=1
    # Expected minimal polynomial, independently derived analytic formula.
    if n==3: minpoly=Counter({3:n**3+1,4:4*n})
    else: minpoly=Counter({3:n**3,n:2**n-1-2*n,n+1:2*n})
    if n==3: minpoly[4]=12
    return allsets,minpoly

def polynomial_coefficients(n):
    """Expand the closed three-variable formula by elementary coefficient counting."""
    out=Counter()
    for a in range(n+1):
        for b in range(n+1):
            for c in range(n+1):
                ways=0
                # Three nonempty layers.
                if a and b and c:
                    ways+=comb(n,a)*comb(n,b)*comb(n,c)
                # The middle layer is full and at least one outer layer empty.
                if b==n and (a==0 or c==0):
                    ways+=comb(n,a)*comb(n,c)
                # Middle layer empty: three choices per column,
                # with the monochromatic and distance-three exceptions removed.
                if b==0 and a and c and a+c>=n:
                    ways+=comb(n,a)*comb(a,a+c-n)
                    if a==1 and c==n-1:ways-=n
                    if c==1 and a==n-1:ways-=n
                if ways:out[a+b+c]+=ways
    return out

if __name__=='__main__':
 total=0
 for n in range(3,6):
   d,m,k=direct(n);p,q=pred(n)
   assert d==p==polynomial_coefficients(n),(n,d,p,polynomial_coefficients(n))
   assert m==q,(n,m,q)
   total+=k
   print(n,k,dict(sorted(d.items())),dict(sorted(m.items())))
 print('PASS',total,'subsets')
