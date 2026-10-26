from itertools import combinations
from collections import Counter
points=list(range(1,16))
def symp(x,y):
 def bit(a,b):return ((x>>a)&1)*((y>>b)&1)
 return (bit(0,1)+bit(1,0)+bit(2,3)+bit(3,2))%2
lines=sorted({tuple(sorted((x,y,x^y))) for x,y in combinations(points,2) if symp(x,y)==0})
assert len(lines)==15
neighbors=[0]*30
for j,line in enumerate(lines):
 for x in line:
  i=points.index(x)
  neighbors[i]|=1<<(15+j)
  neighbors[15+j]|=1<<i
assert all(k.bit_count()==3 for k in neighbors)
# A fixed vertex bijection certifies that this symplectic presentation is
# the duad-syntheme (Cremona-Richmond) incidence graph.
from itertools import combinations as choose
pair_vertices = list(choose(range(6), 2))
def enumerate_1_factors(rest):
    if not rest:
        yield ()
        return
    a = rest[0]
    for b in rest[1:]:
        for tail in enumerate_1_factors(tuple(t for t in rest[1:] if t != b)):
            yield tuple(sorted(((a, b),) + tail))
factors = sorted(enumerate_1_factors(tuple(range(6))))
ISO = (0, 14, 1, 10, 6, 13, 2, 9, 5, 12, 3, 7, 8, 4, 11,
       17, 15, 16, 23, 24, 26, 20, 19, 18, 25, 22, 27, 28, 21, 29)
assert set(ISO) == set(range(30))
for i, e in enumerate(pair_vertices):
    for j, factor in enumerate(factors):
        assert ((neighbors[ISO[i]] >> ISO[15 + j]) & 1) == int(e in factor)
print('PRESENTATION_ISOMORPHISM_OK')
minimum=31; codes=[]; levels=Counter(); maximal=0
# Enumerate independent sets by recursively picking or omitting vertices.
def recur(avail, chosen):
 global minimum,maximal
 if avail==0:
  s=chosen
  if any(not (s & ((1<<v)|neighbors[v])) for v in range(30)):return
  k=s.bit_count();levels[k]+=1;maximal+=1
  if k<minimum:minimum=k;codes.clear()
  if k==minimum:codes.append(s)
  return
 bit=avail&-avail
 i=bit.bit_length()-1
 recur(avail^bit,chosen)
 recur(avail&~(bit|neighbors[i]),chosen|bit)
recur((1<<30)-1,0)
assert minimum==9 and len(codes)==90
setcodes=set(codes)
degree=[];ed=0;slide_arcs=0
for s in codes:
 neighbors_swap=set()
 for i in range(30):
  if not s>>i&1:continue
  for j in range(30):
   if s>>j&1:continue
   t=s^(1<<i)^(1<<j)
   if t in setcodes:
    neighbors_swap.add(t)
    if neighbors[i]>>j&1:slide_arcs+=1
 degree.append(len(neighbors_swap));ed+=len(neighbors_swap)
assert ed//2==45 and set(degree)=={1}
print('MODEL=symplectic_GQ_2_2')
print('points=15 lines=15 incidences=45')
print('maximal_independent_sets',maximal)
print('minimum_cardinality',minimum)
print('minimum_count',len(codes))
print('minimum_bipartition_counts',dict(sorted(Counter((s&((1<<15)-1)).bit_count() for s in codes).items())))
print('exchange_edges',ed//2)
print('token_slide_edges',slide_arcs//2)
assert slide_arcs==ed
print('exchange_degrees',dict(sorted(Counter(degree).items())))
print('other_ID_set_size_distribution',dict(sorted(levels.items())))
