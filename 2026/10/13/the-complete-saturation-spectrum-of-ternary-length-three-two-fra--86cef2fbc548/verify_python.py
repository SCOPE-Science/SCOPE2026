"""Independent finite exhaustive checker for 3-symbol, 3-coordinate 2-frameproof saturation."""
from collections import Counter,defaultdict
from itertools import combinations, product
A=list(product(range(3),repeat=3)); assert len(A)==27
N=len(A)

def invalid_triple(a,b,c):
    w=[A[a],A[b],A[c]]
    return any(all(w[t][j] in (w[(t+1)%3][j],w[(t+2)%3][j]) for j in range(3)) for t in range(3))

BAD=set(tuple(t) for t in combinations(range(N),3) if invalid_triple(*t))

def feasible_extend(code,x):
    return all(tuple(sorted((a,b,x))) not in BAD for a,b in combinations(code,2))

C=[]; all_feasible=Counter(); maximal=defaultdict(list)
def recur(code,start):
    all_feasible[len(code)]+=1
    if code and not any(feasible_extend(code,x) for x in range(N) if x not in code):
        maximal[len(code)].append(sum(1<<v for v in code))
    for x in range(start,N):
        if feasible_extend(code,x):recur(code+[x],x+1)
recur([],0)
print('forbidden triples:',len(BAD))
print('feasible:',sorted(all_feasible.items()),'sum',sum(all_feasible.values()))
print('maximal:',[(s,len(v)) for s,v in sorted(maximal.items())],'sum',sum(map(len,maximal.values())))

def encode(w):return A.index(tuple(w))
perms=[]
for c in range(3):
 for perm in [(1,0,2),(1,2,0)]:
    mapping=[]
    for w in A:
        y=list(w);y[c]=perm[y[c]];mapping.append(encode(y))
    perms.append(mapping)
for ij in [(0,1),(1,2)]:
 mapping=[]
 for w in A:
    y=list(w);y[ij[0]],y[ij[1]]=y[ij[1]],y[ij[0]];mapping.append(encode(y))
 perms.append(mapping)
assert len(perms)==8

def act(mask,p):
 out=0
 while mask:
    low=mask & -mask; i=low.bit_length()-1
    out|=1<<p[i];mask-=low
 return out

orbit_info={}
for n,ms in sorted(maximal.items()):
 todo=set(ms); orbits=[]
 while todo:
    seed=min(todo); orbit={seed};front=[seed]
    for m in front:
        for p in perms:
            v=act(m,p)
            if v not in orbit:
                assert v in ms
                orbit.add(v);front.append(v)
    todo.difference_update(orbit)
    orbits.append((len(orbit),min(orbit)))
 orbit_info[n]=Counter(size for size,_ in orbits)
 print('size',n,'orbits',len(orbits),'orbit_size_distribution',sorted(orbit_info[n].items()))
# preserve labelled maximal set catalogue
with open('maximal_codes.txt','w',encoding='utf-8') as f:
 for n in sorted(maximal):
  for code in sorted(maximal[n]):
   f.write(str(n)+':' + ','.join(''.join(map(str,A[i])) for i in range(N) if code>>i&1)+'\n')

EXPECTED = {3:27, 4:162, 5:540, 6:27, 7:324, 9:12}
assert len(BAD)==972
assert dict((n,len(v)) for n,v in maximal.items()) == EXPECTED
assert sum(all_feasible.values())==14584
assert {n:sorted(orbit_info[n].elements()) for n in orbit_info} == {3:[27],4:[162],5:[54,162,324],6:[27],7:[108,216],9:[12]}
all8 = set()
for mask in maximal[9]:
 for i in range(N):
  if mask & (1<<i):
   all8.add(mask & ~(1<<i))
assert len(all8)==108
assert all_feasible[8] == 108
print('VERIFICATION_OK: complete maximality, histogram, 9 isometry orbits, unique eight-word completions')
