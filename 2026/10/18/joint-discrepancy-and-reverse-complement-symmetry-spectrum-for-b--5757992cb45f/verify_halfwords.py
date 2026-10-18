from collections import Counter
N=32

def canonical(w):
 return min(w[i:]+w[:i] for i in range(len(w)))

def discr(w):
 p=[0]
 for v in w:p.append(p[-1]+(1 if v else -1))
 return max(p)-min(p)

def valid(w):
 words=set()
 for i in range(len(w)):
  x=0
  for j in range(5):x=2*x+w[(i+j)%len(w)]
  if x in words:return False
  words.add(x)
 return len(words)==len(w)

h=Counter();s=set();mapping={}
for k in range(1<<16):
 X=tuple((k>>i)&1 for i in range(16))
 w=X+tuple(1-z for z in X[::-1])
 if valid(w):
  a=canonical(w)
  s.add(a);mapping[k]=a
for a in s:h[discr(a)]+=1
assert len(mapping)==128 and len(s)==64
assert h=={5:16,6:16,7:24,8:8}
assert set(Counter(mapping.values()).values())=={2}
print('halfwords valid',len(mapping),'unique rotations',len(s),'hist',dict(sorted(h.items())))
print('min preimages',min(Counter(mapping.values()).values()),'max',max(Counter(mapping.values()).values()),'preimages histogram',Counter(Counter(mapping.values()).values()))
for d in sorted(h):
 a=next(w for w in sorted(s) if discr(w)==d)
 print('witness',d,''.join(map(str,a)))
print('HALFWORDS_OK')
