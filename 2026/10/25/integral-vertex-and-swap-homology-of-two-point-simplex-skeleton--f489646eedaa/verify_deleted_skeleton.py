#!/usr/bin/env python3
"""Exact signed cellular Lefschetz checks for deleted products of codimension-two simplex skeleta."""
from itertools import permutations
from collections import defaultdict

def pairs(n,full=False):
    out=defaultdict(list)
    for A in range(1,1<<n):
      if not full and A.bit_count()>n-2: continue
      for B in range(1,1<<n):
        if A&B:continue
        if not full and B.bit_count()>n-2:continue
        out[A.bit_count()+B.bit_count()-2].append((A,B))
    return out

def parity_perm(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def cell_sign(src,target,p,t):
    a,b=src; aa,bb=target
    def elem(mask): return [i for i in range(len(p)) if mask>>i&1]
    if t: a,b=b,a
    def parity_of_images(mask):
       images=[p[x] for x in elem(mask)]
       return (-1)**sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
    return (-1)**((src[0].bit_count()-1)*(src[1].bit_count()-1)*t)*parity_of_images(a)*parity_of_images(b)

def lef(n,p,t):
    tr=0
    for k,cs in pairs(n).items():
      for A,B in cs:
        def pp(mask):return sum(1<<p[i] for i in range(n) if mask>>i&1)
        target=(pp(B),pp(A)) if t else (pp(A),pp(B))
        if target==(A,B):tr+=(-1)**k*cell_sign((A,B),target,p,t)
    return tr

def rank_mod2(columns):
    piv={}
    for x in columns:
      while x:
        i=x.bit_length()-1
        if i in piv:x^=piv[i]
        else:piv[i]=x; break
    return len(piv)

def test_homology(n):
    cells=pairs(n)
    ranks={}
    for k in range(1,n-1):
      idx={c:i for i,c in enumerate(cells[k-1])}
      cols=[]
      for A,B in cells[k]:
        col=0
        for i in range(n):
          if A>>i&1 and A.bit_count()>1:col^=1<<idx[(A^(1<<i),B)]
          if B>>i&1 and B.bit_count()>1:col^=1<<idx[(A,B^(1<<i))]
        cols.append(col)
      ranks[k]=rank_mod2(cols)
    return {k:len(cs)-ranks.get(k,0)-ranks.get(k+1,0) for k,cs in cells.items()}

def run():
  tests=0
  for n in range(4,8):
    ps=[tuple(range(n)),tuple([1,0]+list(range(2,n))),tuple(list(range(1,n))+[0]),tuple(reversed(range(n)))]
    for p in ps:
      for t in range(2):
        L=lef(n,p,t)
        actual=(-1)**(n-3)*(L-1)
        f=sum(p[i]==i for i in range(n))
        pred=parity_perm(p)*((2*f-1) if t==0 else (-1)**n)
        assert actual==pred,(n,p,t,L,actual,pred)
        tests+=1
    if n<=6:
      hs=test_homology(n)
      assert hs.get(0)==1 and hs.get(n-3)==2*n-1 and all(v==0 for k,v in hs.items() if k not in (0,n-3)),(n,hs)
      print('MOD2_HOMOLOGY_CHECK',n,hs)
  print('SIGNED_CELLULAR_LEFSCHETZ_VERIFIED',tests,'cases for n=4..7')
if __name__=='__main__':run()

def top_orientation_check(n):
    """Produce the primitive fundamental cellular cycle of the full deleted product."""
    cs=pairs(n,full=True)
    tops=cs[n-2]
    ridges=defaultdict(list)
    for A,B in tops:
        aa=[i for i in range(n) if A>>i&1]
        bb=[i for i in range(n) if B>>i&1]
        for j,i in enumerate(aa):
            if len(aa)>1:ridges[(A^(1<<i),B)].append(((A,B),(-1)**j))
        for j,i in enumerate(bb):
            if len(bb)>1:ridges[(A,B^(1<<i))].append(((A,B),(-1)**(len(aa)-1+j)))
    assert all(len(x)==2 for x in ridges.values()), ('not pseudomanifold',n)
    adj=defaultdict(list)
    for ridge,entries in ridges.items():
        (u,a),(v,b)=entries
        adj[u].append((v,-a*b))
        adj[v].append((u,-b*a))
    c={tops[0]:1}; queue=[tops[0]]
    for u in queue:
        for v,s in adj[u]:
            if v not in c: c[v]=s*c[u];queue.append(v)
            else: assert c[v]==s*c[u]
    assert len(c)==len(tops)
    removed=[cell for cell in tops if max(cell[0].bit_count(),cell[1].bit_count())==n-1]
    assert len(removed)==2*n and all(abs(c[x])==1 for x in removed)
    for p in [tuple(range(n)),tuple([1,0]+list(range(2,n))),tuple(list(range(1,n))+[0]),tuple(reversed(range(n)))]:
      def pp(mask):return sum(1<<p[i] for i in range(n) if mask>>i&1)
      for t in (0,1):
        deg=parity_perm(p)*(-1)**((n-1)*t)
        for u in tops:
          a,b=u
          v=(pp(b),pp(a)) if t else (pp(a),pp(b))
          assert c[u]*cell_sign(u,v,p,t)==deg*c[v],(n,p,t,u,v)
    print('PRIMITIVE_RELATIVE_FUNDAMENTAL_CYCLE_VERIFIED',n,'top_cells',len(tops),'removed',len(removed))

if __name__=='__main__':
    for n in range(4,8):top_orientation_check(n)
