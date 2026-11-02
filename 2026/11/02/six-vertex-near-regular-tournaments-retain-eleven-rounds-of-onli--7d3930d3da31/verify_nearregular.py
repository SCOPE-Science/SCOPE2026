"""Independent standard-library-only exhaustive verification of score-constrained orientation shattering."""
import itertools,json,collections,pathlib
N=6
EDGES=list(itertools.combinations(range(N),2)); M=len(EDGES)
H=[]
for code in range(1<<M):
 score=[0]*N
 for k,(a,b) in enumerate(EDGES):score[a if code>>k&1 else b]+=1
 if sorted(score)==[2,2,2,3,3,3]:H.append(code)
assert len(H)==2640

# Exhaustive trace computation directly from score-constrained orientations.
profile=collections.Counter();maxima=[]
for support in range(1<<M):
 k=support.bit_count()
 if len({h&support for h in H})==(1<<k):
  profile[k]+=1
  if k==7:maxima.append(support)
assert [profile[i] for i in range(8)]==[1,15,105,455,1335,2697,3355,1185]
assert sum(profile.values())==9148
print('DIRECT_TRACE_PROFILE_PASS',len(H),'hypotheses',sum(profile.values()),'shattered_supports')

# Independently derive and check the cut-inequality feasibility test.
cuts=[]
for u in range(1,1<<(N-1)):
 r=u.bit_count()
 mask=sum(1<<j for j,(a,b) in enumerate(EDGES) if ((u>>a)&1)!=((u>>b)&1))
 bound=min(r*(N+1-r),(N-r)*(r+1))//2
 cuts.append((mask,bound))
alt=collections.Counter()
for s in range(1<<M):
 if all((s&c).bit_count()<=b for c,b in cuts):alt[s.bit_count()]+=1
assert alt==profile
print('CUT_CHARACTERIZATION_PASS',1<<M,'supports')

# Canonical adjacency masks, independent of graph-isomorphism software.
edge_index={e:i for i,e in enumerate(EDGES)}
permutation_images=[]
for perm in itertools.permutations(range(N)):
 permutation_images.append([1<<edge_index[tuple(sorted((perm[a],perm[b])))] for a,b in EDGES])
def canonical(s):
 active=[j for j in range(M) if s>>j&1]
 return min(sum(mapping[j] for j in active) for mapping in permutation_images)
classes=collections.Counter(map(canonical,maxima))
assert sorted(classes.values())==[15,90,360,360,360],classes
assert len(classes)==5 and sum(classes.values())==1185
# Distinguish the five types by degree sequence and triangle count.
signatures=[]
for mask,count in classes.items():
 deg=[0]*N
 for j,(a,b) in enumerate(EDGES):
  if mask>>j&1:deg[a]+=1;deg[b]+=1
 tri=sum(all(mask>>edge_index[tuple(sorted((a,b)))]&1 for a,b in ((i,j),(i,k),(j,k))) for i,j,k in itertools.combinations(range(N),3))
 signatures.append((tuple(sorted(deg)),tri,count))
assert sorted(signatures)==sorted([
 ((1,1,3,3,3,3),4,15),
 ((1,2,2,3,3,3),1,360),
 ((1,2,2,3,3,3),2,360),
 ((2,2,2,2,3,3),1,360),
 ((2,2,2,2,3,3),2,90),
])
print('FIVE_MAX_SUPPORT_ISOMORPHISM_TYPES_PASS',sorted(classes.values()))

# The complete binary tree includes an explicit valid hypothesis at each of 2048 leaves.
p=pathlib.Path(__file__).with_name('nearregular_depth11_certificate.json')
cert=json.loads(p.read_text(encoding='utf8'))
assert cert['edge_order']==[list(q) for q in EDGES]
assert len(cert['queries_heap'])==2047 and len(cert['leaf_witnesses_heap'])==2048
assert len(set(cert['leaf_witnesses_heap']))==2048
assert set(cert['leaf_witnesses_heap'])<=set(H)
for leaf,witness in enumerate(cert['leaf_witnesses_heap'],start=2048):
 node=leaf
 for _ in range(11):
  parent=node//2
  q=cert['queries_heap'][parent-1]
  assert 0<=q<15 and ((witness>>q)&1)==(node&1)
  node=parent
assert 2048<=len(H)<4096
print('ONLINE_CERTIFICATE_PASS',2048,'distinct feasible leaves; depth 12 excluded')

# Small even-order boundary independently re-enumerated.
for n,expected in [(2,([1,1],1)),(4,([1,6,15,16],4))]:
 e=list(itertools.combinations(range(n),2));h=[]
 for bits in range(1<<len(e)):
  w=[0]*n
  for j,(a,b) in enumerate(e):w[a if bits>>j&1 else b]+=1
  if sorted(w)==[n//2-1]*(n//2)+[n//2]*(n//2):h.append(bits)
 prof=collections.Counter()
 for s in range(1<<len(e)):
  if len({z&s for z in h})==1<<s.bit_count():prof[s.bit_count()]+=1
 assert [prof[i] for i in range(len(expected[0]))]==expected[0]
 # The lower online bound is established by a complete recurrence.
 qmask=[sum(1<<i for i,z in enumerate(h) if z>>j&1) for j in range(len(e))]
 from functools import lru_cache
 @lru_cache(None)
 def depth(z):
  return max((1+min(depth(z&q),depth(z^(z&q))) for q in qmask if z&q and z^(z&q)),default=0)
 assert depth((1<<len(h))-1)==expected[1]
print('SMALL_EVEN_BOUNDARIES_PASS n=2,4')
print('ALL_NEARREGULAR_TOURNAMENT_CHECKS_PASS')
