"""Finite independent combinatorial checks for square-grid three-cut homology characters.

Requires Python 3 standard library only. Execute: python3 verify.py
The infinite-family theorem is proved separately; finite tests corroborate it.
"""
from itertools import combinations
from math import comb


def parity(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1


def square_grid(n):
    vs=[(r,c) for r in range(n) for c in range(n)]
    moves={
      'identity':lambda r,c:(r,c),
      'quarter_turn':lambda r,c:(c,n-1-r),
      'half_turn':lambda r,c:(n-1-r,n-1-c),
      'axis_reflection':lambda r,c:(r,n-1-c),
      'diagonal_reflection':lambda r,c:(c,r),
    }
    perms={name:tuple(vs.index(f(*v)) for v in vs) for name,f in moves.items()}
    adj=[set() for _ in vs]
    for i,(r,c) in enumerate(vs):
      for j,(s,t) in enumerate(vs):
        if abs(r-s)+abs(c-t)==1: adj[i].add(j)
    return vs,adj,perms


def invariant_orientation(items,p):
    images=[p[i] for i in items]
    if set(images)!=set(items): return 0
    vmap={z:i for i,z in enumerate(items)}
    return parity([vmap[x] for x in images])


def cycle_trace(n):
    vs,adj,perms=square_grid(n)
    N=len(vs)
    tri=[]
    for v in range(N):
       for a,b in combinations(sorted(adj[v]),2):
          tri.append(tuple(sorted((a,v,b))))
    assert len(tri)==6*n*n-12*n+4
    sq=[]
    for r in range(n-1):
       for c in range(n-1):
          sq.append(tuple(sorted(vs.index(v) for v in ((r,c),(r+1,c),(r,c+1),(r+1,c+1)))))
    assert len(sq)==(n-1)**2
    vals={}
    for name,p in perms.items():
       f=sum(p[i]==i for i in range(N))
       z2=sum(p[i]!=i and p[p[i]]==i for i in range(N))//2
       signed3=sum(invariant_orientation(S,p) for S in tri)
       signed4=sum(invariant_orientation(S,p) for S in sq)
       eps=parity(p)
       val=eps*(1-f+comb(f,2)-z2-signed3+signed4)
       vals[name]=(val,eps,f,z2,signed3,signed4)
    return vals


def closed_formula(n):
    B=(n**4-13*n*n+20*n-4)//2
    H=2-(n*n//2)
    if n%2:
      X=(-1)**((n-1)//2)*(3-n)
    else:
      X=n-n*n//2
    return {'identity':B,'quarter_turn':0,'half_turn':H,'axis_reflection':X,'diagonal_reflection':0}


def decomposed(n):
    t=closed_formula(n)
    B,H,X=t['identity'],t['half_turn'],t['axis_reflection']
    assert (B+H+2*X)%8==0 and (B+H-2*X)%8==0 and (B-H)%4==0
    a=(B+H+2*X)//8
    b=(B+H-2*X)//8
    c=(B-H)//4
    assert min(a,b,c)>=0
    assert B==2*a+2*b+2*c
    return (a,b,c)


def direct_complex_trace(n):
    """Enumerate every simplex from disconnected triples: independent of face-lattice formula."""
    vs,adj,perms=square_grid(n)
    N=len(vs)
    assert N<=16
    U=(1<<N)-1
    triple_masks=[]
    for aa,bb,cc in combinations(range(N),3):
      count=sum((b in adj[a]) for a,b in ((aa,bb),(aa,cc),(bb,cc)))
      if count<2: triple_masks.append((1<<aa)|(1<<bb)|(1<<cc))
    faces=[]
    for mask in range(1<<N):
      complement=U^mask
      if any((complement & t)==t for t in triple_masks):
        faces.append(mask)
    # empty face is included; orientation traces are reduced Euler traces.
    traces={k:0 for k in perms}
    for mask in faces:
      indices=tuple(i for i in range(N) if mask>>i &1)
      sign=-1 if len(indices)%2==0 else 1  # (-1)^(size-1)
      for name,p in perms.items():
        orient=invariant_orientation(indices,p)
        if orient:
          traces[name]+=sign*orient
    d=N-4
    return {name:(-1)**d*val for name,val in traces.items()}


def main():
    for n in range(3,13):
       combinatorial=cycle_trace(n)
       theoretical=closed_formula(n)
       for key,expected in theoretical.items():
          assert combinatorial[key][0]==expected,(n,key,combinatorial[key],expected)
       a,b,c=decomposed(n)
       print('n',n,'character',tuple(theoretical.values()),'irreducible_multiplicities',(a,b,c))
    for n in (3,4):
       direct=direct_complex_trace(n)
       expected=closed_formula(n)
       assert direct==expected,(n,direct,expected)
       print('direct_face_trace',n,'OK',direct)
    print('VERIFY_OK')

if __name__=='__main__': main()
