from functools import lru_cache

def prefix(a,b):return len(a)<len(b) and b.startswith(a)

def diag(words):
 return tuple(0 if x==y else 1 if prefix(x,y) else 2 if prefix(y,x) else 3 for i,x in enumerate(words) for y in words[i+1:])

def canonical_pair(d1,d2,ell):
 x='0'*d1
 if ell==min(d1,d2): y='0'*d2
 else:y='0'*ell+'1'*(d2-ell)
 return x,y

def z_orbits(x,y,b,h):
 out=['']
 def walk(p):
  if len(p)==h:return
  active=[w for w in (x,y) if w.startswith(p) and len(w)>len(p)]
  symbols={w[len(p)] for w in active}
  choices=sorted(symbols)
  if len(symbols)<b:
   new=next(str(k) for k in range(3) if str(k) not in symbols)
   choices.append(new)
  for digit in choices:
   q=p+digit
   if not any(w.startswith(q) for w in (x,y)):
    for l in range(len(q),h+1):out.append(q+'0'*(l-len(q)))
   else:
    out.append(q);walk(q)
 walk(''); return set(out)

def profile(b,h):
 @lru_cache(None)
 def pair_type(d1,d2,ell):
  x,y=canonical_pair(d1,d2,ell)
  return (diag((x,y)),frozenset(diag((x,y,z)) for z in z_orbits(x,y,b,h)))
 type1=[]
 for d in range(h+1):
  tp=frozenset(pair_type(d,e,ell) for e in range(h+1) for ell in range(min(d,e)+1))
  type1.append(tp)
 return frozenset(type1)

if __name__=='__main__':
 seen={}
 for b in [2,3,4]:
  print('b=',b, flush=True)
  for h in range(0,17):
   x=profile(b,h)
   key=next((k for k,v in seen.items() if v==x),None)
   if key is None: key=(b,h); seen[key]=x
   print(h,'class',key,'types1',len(x),flush=True)
