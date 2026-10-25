"""Finite sanity tests for a forward gadget interpretation of finite digraphs.
All tests are supplementary to the mathematical proof."""
from itertools import combinations,product

def induced(G,S):
    return (tuple(x for x in G[0] if x in S),set((x,y) for (x,y) in G[1] if x in S and y in S))

def succ_closed(G,S):
    return all(y in S for x,y in G[1] if x in S)

def label(E,v,i):
    # C_1 is sink; C_{j+1} has exactly one successor satisfying C_j
    def C(z,j):
        succ=[y for (x,y) in E if x==z]
        if j==1:return len(succ)==0
        return len(succ)==1 and C(succ[0],j-1)
    return any(C(y,i) for x,y in E if x==v)

def interpret(G,r):
    V,E=G; O={x for x in V if (x,x) in E}
    Rs=[set() for _ in range(r)]
    for a in O:
      for z in V:
       if z in O or (a,z) not in E:continue
       for b in O:
        if (z,b) in E:
         for i in range(1,r+1):
          if label(E,z,i):Rs[i-1].add((a,b))
    return O,Rs

def encode(A,r):
    O,Rs=A; V=set(O);E={(a,a) for a in O}
    for i,rel in enumerate(Rs,1):
      for a,b in rel:
       v=('e',i,a,b);V.add(v);E|={(a,v),(v,b)}
       for j in range(1,i+1):V.add(('t',i,j,a,b))
       E.add((v,('t',i,1,a,b)))
       for j in range(1,i):E.add((('t',i,j,a,b),('t',i,j+1,a,b)))
    return tuple(V),E

checks=0
for r in range(1,4):
  for n in range(0,3):
    O=set(range(n)); pairs=list(product(range(n),repeat=2))
    if len(pairs)*r>11: continue
    for bits in product((0,1),repeat=len(pairs)*r):
      Rs=[{p for j,p in enumerate(pairs) if bits[i*len(pairs)+j]} for i in range(r)]
      G=encode((O,Rs),r)
      U,R=interpret(G,r)
      assert U==O and all(R[i]==Rs[i] for i in range(r))
      checks+=1
for n in range(1,4):
  V=tuple(range(n)); pairs=list(product(V,repeat=2))
  for bits in product((0,1),repeat=len(pairs)):
    E={p for p,v in zip(pairs,bits) if v}; G=(V,E)
    O,Rs=interpret(G,3)
    for mask in product((0,1),repeat=n):
      S={v for v,m in zip(V,mask) if m}
      if not succ_closed(G,S):continue
      Oh,Rh=interpret(induced(G,S),3)
      assert Oh==O.intersection(S)
      assert all(Rh[i]=={p for p in Rs[i] if p[0] in S and p[1] in S} for i in range(3))
      assert all(b in Oh for R in Rs for a,b in R if a in Oh)
      checks+=1
print('FORWARD_GADGET_FINITE_SANITY_OK',checks)
