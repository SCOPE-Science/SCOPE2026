import networkx as nx, collections, functools, itertools
N=9
@functools.lru_cache(None)
def rooted_form(neighbors,root,par):
 return '('+''.join(sorted(rooted_form(neighbors,i,root) for i in neighbors[root] if i!=par))+')'
trees_by_n=collections.defaultdict(list);decor={}
for n in range(1,N+1):
 for t in ([nx.empty_graph(1)] if n==1 else nx.nonisomorphic_trees(n)):
  nei=tuple(tuple(t.neighbors(v)) for v in range(n))
  trees_by_n[n].append(t)
  for v in range(n):
   rf=rooted_form(nei,v,-1)
   decor[(n,rf)]=None

def rooted_graph(form):
 g=nx.Graph();g.add_node(0); stack=[]; counter=0
 for c in form:
  if c=='(':
   if stack:
    counter+=1;g.add_edge(stack[-1],counter);stack.append(counter)
   else:stack.append(0)
  else:stack.pop()
 return g
alphabet=sorted(decor)

def canonical(seq):
 n=len(seq);r=seq[::-1];return min([tuple(seq[i:]+seq[:i]) for i in range(n)]+[tuple(r[i:]+r[:i]) for i in range(n)])
bracelets=set()
def enum(seq,lo,remaining):
 if len(seq)>=3:bracelets.add(canonical(seq))
 for i in range(lo,len(alphabet)):
  w=alphabet[i][0]
  if w>remaining:break
  enum(seq+[i],0,remaining-w)
for i,(w,_) in enumerate(alphabet):
 if w>N:break
 enum([i],i,N-w)
print('unicyclic types',len(bracelets),flush=True)
comps=[]
for n,ts in trees_by_n.items():
 for t in ts:comps.append((n,t))
for seq in bracelets:
 g=nx.cycle_graph(len(seq));node=len(seq)
 for r,i in enumerate(seq):
  t=rooted_graph(alphabet[i][1]);copy={0:r}
  for v in list(t.nodes())[1:]:copy[v]=node;node+=1
  for a,b in t.edges:g.add_edge(copy[a],copy[b])
 assert len(g)==sum(alphabet[i][0] for i in seq)
 comps.append((len(g),g))
comps.sort(key=lambda x:x[0])
print('components',len(comps),'by order',collections.Counter(n for n,_ in comps),flush=True)
# recursively build all unlabelled pseudoforests by multiset of unicyclic/tree component classes
by_n=collections.defaultdict(list)
def rec(indices,start,n):
 by_n[n].append(tuple(indices))
 for j in range(start,len(comps)):
  w=comps[j][0]
  if n+w>N:break
  rec(indices+[j],j,n+w)
rec([],0,0)
print('pseudoforest isomorphism classes',dict((k,len(v)) for k,v in by_n.items()),flush=True)
hashcounts={}
for n,ls in sorted(by_n.items()):
 distinct=set()
 for indices in ls:
  g=nx.disjoint_union_all([comps[i][1] for i in indices]) if indices else nx.empty_graph(0)
  assert len(g)==n
  distinct.add(nx.weisfeiler_lehman_graph_hash(g,iterations=20))
 hashcounts[n]=len(distinct)
 print(n,len(ls),len(distinct),flush=True)
expected=[1,1,2,4,9,19,45,106,267,685]
assert [hashcounts[i] for i in range(N+1)]==expected
