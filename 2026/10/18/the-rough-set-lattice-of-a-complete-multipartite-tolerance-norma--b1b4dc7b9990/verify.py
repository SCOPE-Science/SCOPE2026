import itertools

def rough(parts):
 n=sum(parts); p=[];o=0
 for t in parts:p.append(set(range(o,o+t)));o+=t
 neighbors=[]
 for x in range(n):neighbors.append({x}|{y for y in range(n) if not any(x in pi and y in pi for pi in p)})
 pairs=set()
 for bits in range(1<<n):
  X={x for x in range(n) if bits>>x&1}
  L=frozenset(x for x in range(n) if neighbors[x]<=X)
  U=frozenset(x for x in range(n) if neighbors[x]&X)
  pairs.add((L,U))
 return pairs

def check(parts):
 pairs=rough(parts); n=sum(parts)
 expected=3+2*sum(2**t-2 for t in parts)
 assert len(pairs)==expected,(parts,len(pairs),expected)
 predicted={(frozenset(),frozenset()),(frozenset(),frozenset(range(n))),(frozenset(range(n)),frozenset(range(n)))}
 off=0
 for s in parts:
  Pi=set(range(off,off+s));off+=s
  for bits in range(1,1<<s):
   A=frozenset(off-s+i for i in range(s) if bits>>i&1)
   if len(A)==s:continue
   predicted.add((frozenset(),frozenset(set(range(n))-Pi|set(A))))
   predicted.add((A,frozenset(range(n))))
 assert pairs==predicted,(parts,"normal form mismatch")
 for L,U in pairs:
  assert (frozenset(set(range(n))-set(U)),frozenset(set(range(n))-set(L))) in pairs
 p=list(pairs); m=len(p)
 le=lambda x,y:x[0]<=y[0] and x[1]<=y[1]
 meet={}; join={}
 for i,x in enumerate(p):
  for j,y in enumerate(p):
   lows=[z for z in p if le(z,x) and le(z,y)]
   up=[z for z in p if le(x,z) and le(y,z)]
   mins=[z for z in up if not any(z!=w and le(w,z) for w in up)]
   maxs=[z for z in lows if not any(z!=w and le(z,w) for w in lows)]
   assert len(mins)==len(maxs)==1,(parts,x,y)
   join[i,j]=p.index(mins[0]);meet[i,j]=p.index(maxs[0])
 modular=True;distrib=True
 for i in range(m):
  for j in range(m):
   for k in range(m):
    if le(p[i],p[k]) and join[i,meet[j,k]]!=meet[join[i,j],k]:modular=False
    if meet[i,join[j,k]]!=join[meet[i,j],meet[i,k]]:distrib=False
 active=[t for t in parts if t>=2]
 expmod=len(active)<=1 or all(t<=2 for t in parts)
 expdist=len(active)<=1
 assert modular==expmod and distrib==expdist,(parts,modular,distrib,expmod,expdist)
 return len(p),modular,distrib

if __name__=='__main__':
 count=0
 for n in range(2,9):
  for mask in range(1,1<<(n-1)):
   cuts=[i+1 for i in range(n-1) if mask>>i&1]
   parts=tuple(b-a for a,b in zip([0]+cuts,cuts+[n]))
   if n==8 and parts.count(1)<5:continue
   check(parts);count+=1
 print('VERIFY_OK multipartite_profiles=',count,' all_rough_pairs=PASS coordinate_order_lattice=PASS self_duality=PASS modular_distributive_boundaries=PASS')
