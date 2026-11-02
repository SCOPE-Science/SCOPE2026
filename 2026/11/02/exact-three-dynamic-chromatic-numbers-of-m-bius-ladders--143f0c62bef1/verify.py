from itertools import combinations

def graph(m):
  N=2*m
  return [set(((i-1)%N,(i+1)%N,(i+m)%N)) for i in range(N)]

def square(m):
  A=graph(m)
  return [A[i]|set().union(*(A[x] for x in A[i]))-{i} for i in range(2*m)]

def check(m,top,bottom):
  assert len(top)==len(bottom)==m
  C=[int(v) for v in top+bottom]
  S=square(m)
  for i in range(2*m):
    for j in S[i]:
      if C[i]==C[j]:raise AssertionError((m,i,j,C[i]))
  return len(set(C))

bases={5:('02104','13423'),7:('0213024','1302413'),8:('02130425','13021534'),12:('021302140324','130214032413')}
for m,(t,b) in bases.items():print('BASE',m,check(m,t,b))

def expanded(t,b):
  return (t[:2]+ b[0]+b[1]+t[0]+t[1]+t[2:], b[:2]+t[0]+t[1]+b[0]+b[1]+b[2:])
for base in (5,7,12):
  t,b=bases[base]
  for k in range(30):
    m=len(t)
    assert check(m,t,b)==5
    t,b=expanded(t,b)
  print('FAMILY',base,'OK')
for m in range(6,202,4):
  z=[(0,1),(2,3),(1,0),(3,2)]
  t=''.join(str(z[i%4][0]) for i in range(m))
  b=''.join(str(z[i%4][1]) for i in range(m))
  assert check(m,t,b)==4
print('FOUR FAMILY OK')
for m in (3,4):
  sq=square(m)
  print('SMALL',m,'full=',all(len(x)==2*m-1 for x in sq))
m=8
S=square(m)
num4=sum(1 for X in combinations(range(2*m),4) if all((v not in S[u]) for u,v in combinations(X,2)))
num3=sum(1 for X in combinations(range(2*m),3) if all((v not in S[u]) for u,v in combinations(X,2)))
print('m8 independent quadruples:',num4,'triples:',num3)
print('VERIFY_OK')
