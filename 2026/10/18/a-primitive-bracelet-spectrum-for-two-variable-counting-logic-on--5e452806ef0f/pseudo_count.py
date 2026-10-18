import networkx as nx
from collections import Counter,defaultdict
from functools import lru_cache
N=9
@lru_cache(None)
def rooted_form_recur(neighbors,root,par):
    return '('+''.join(sorted(rooted_form_recur(neighbors,u,root) for u in neighbors[root] if u!=par))+')'

tree_forms=[];rooted_types={}
for n in range(1,N+1):
    trees=[nx.empty_graph(1)] if n==1 else list(nx.nonisomorphic_trees(n))
    for t in trees:
        nei=tuple(tuple(t.neighbors(v)) for v in range(n))
        f=rooted_form_recur(nei,0,-1)
        tree_forms.append((n,f))
        for v in t:
            rf=rooted_form_recur(nei,v,-1)
            rooted_types[(n,rf)]=(n,rf)
print('tree counts',dict(Counter(n for n,_ in tree_forms)),flush=True)
print('rooted counts',dict(Counter(n for n,_ in rooted_types)),flush=True)
alphabet=sorted(rooted_types)
wt=[t[0] for t in alphabet]; form=[t[1] for t in alphabet]
# generate circular bracelets, primitive only, weight<=N
bracelets={}
def canonical(seq):
    n=len(seq)
    return min(tuple(seq[i:]+seq[:i]) for i in range(n)) if False else min([tuple(seq[i:]+seq[:i]) for i in range(n)]+[tuple((seq[::-1])[i:]+(seq[::-1])[:i]) for i in range(n)])
def primitive(seq):
 p=len(seq)
 return not any(p%d==0 and seq==seq[:d]*(p//d) for d in range(1,p))
def enum(seq,lo,remaining):
 if seq:
  p=len(seq)
  s=N-remaining
  if primitive(seq) and (p>=3 or (p==2 and 2*s<=N) or (p==1 and 3*s<=N)):
   bracelets[canonical(seq)]=(p,s)
 if remaining==0 or len(seq)>=N: return
 for i in range(lo,len(alphabet)):
  w=wt[i]
  if w>remaining:break
  # min index zero due dihedral rather than multiset
  enum(seq+[i],0,remaining-w)
# more efficient: use min-first index to avoid shifted duplicates
for i,w in enumerate(wt):
 if w>N: break
 enum([i],i,N-w)
print('primitive bracelets available',len(bracelets),flush=True)
cats=defaultdict(int)
for p,s in bracelets.values(): cats[p,s]+=1
print('by p and weight',sorted(cats.items()),flush=True)
coeff=[1]+[0]*N
for n,_ in tree_forms:
 for j in range(n,N+1):coeff[j]+=coeff[j-n]
for (p,s),q in sorted(cats.items()):
 min_k=3 if p==1 else 2 if p==2 else 1
 for _ in range(q):
  # factor 1 + z^(kmin*s)+z^((kmin+1)*s)+ ... ; use old copy to avoid reusing same factor
  old=coeff[:]
  for k in range(min_k,N//s+1):
   for j in range(k*s,N+1): coeff[j]+=old[j-k*s]
print('spectrum counts',coeff,flush=True)
# compare full unlabelled graph atlas
atlas=nx.graph_atlas_g()
D=defaultdict(set);graphcounts=Counter()
for g in atlas:
 n=len(g)
 if n>N:continue
 if all(c.number_of_edges()<=len(c) for c in (g.subgraph(c).copy() for c in nx.connected_components(g))):
  graphcounts[n]+=1
  h=nx.weisfeiler_lehman_graph_hash(g,iterations=2*N+2)
  D[n].add(h)
print('atlas pseudoforest classes',dict((n,len(D[n])) for n in range(8)),flush=True)
print('atlas iso counts',dict(graphcounts),flush=True)
assert all(len(D[n])==coeff[n] for n in range(8)),[(n,len(D[n]),coeff[n]) for n in range(8)]
