#!/usr/bin/env python3
"""Exact certificates for ternary top-of-menu Boolean choice on seven labels.
Independent computations use only integer masks and permutations, no external modules.
Run: python3 verify_top_choice.py top_choice_depth10_certificate.json
"""
import itertools,json,sys,math
n=7
P=tuple(p for p in itertools.permutations(range(n)) if p.index(0)<p.index(1))
assert len(P)==math.factorial(n)//2
Q=tuple((x,a,b) for x in range(n) for a,b in itertools.combinations([y for y in range(n) if y!=x],2))
M=tuple(sum(1<<i for i,p in enumerate(P) if p[x]>p[a] and p[x]>p[b]) for x,a,b in Q)
N=len(P);F=(1<<N)-1
assert len(Q)==3*math.comb(n,3)==105
assert all(q.bit_count()==math.factorial(n)//6 for q in M)
# There are two rankings for every distinct maximum-on-triples concept.
signatures={}
for p in itertools.permutations(range(n)):
 s=tuple(int(p[x]>p[a] and p[x]>p[b]) for x,a,b in Q)
 signatures[s]=signatures.get(s,0)+1
assert len(signatures)==2520 and set(signatures.values())=={2}
print('DISTINCT_CONCEPTS_PASS',len(signatures),'QUERIES',len(Q),'POSITIVE_BRANCH',M[0].bit_count())

# VC upper: any nonempty shattered support may be relabeled to contain Q[0].
# The recursive trace list records *all* patterns of the selected query support.
# A new query extends a shattered support iff it splits each trace block.
counts=[0]*7
witness6=None

def vc_dfs(index,trace,chosen):
 global witness6
 d=len(chosen)
 counts[d]+=1
 if d==6:
  witness6=tuple(chosen);return
 if index>=len(Q):return
 for j in range(index,len(Q)):
  q=M[j];kids=[]
  for S in trace:
   yes=S&q
   no=S^yes
   if not yes or not no:break
   kids.extend((no,yes))
  else:
   vc_dfs(j+1,kids,chosen+(j,))
vc_dfs(1,(F^M[0],M[0]),(0,))
assert witness6 is None
print('VC_SIX_OBSTRUCTION_PASS nodes',sum(counts),'level_counts',counts)
# The five canonical tests all share two anchor alternatives.
star_queries=[(x,0,1) for x in range(2,n)]
star_masks=[M[Q.index(q)] for q in star_queries]
traces={tuple(int((1<<k)&z!=0) for z in star_masks) for k in range(len(P))}
assert len(traces)==1<<(n-2)
print('VC_FIVE_WITNESS_PASS',len(traces))

# Tree must be complete to depth ten with a *different* actual strict rank
# assignment at each leaf and all branch outcomes verified.
cert=json.load(open(sys.argv[1],encoding='utf8'))
assert cert['schema']==1 and cert['n']==7 and cert['depth']==10
term=[];internal=[]
def verify_node(node,path):
 if 'rank' in node:
  assert len(path)==10 and len(node)==1
  p=tuple(node['rank']); assert sorted(p)==list(range(n))
  for (x,a,b),v in path: assert int(p[x]>p[a] and p[x]>p[b])==v
  term.append(p);return
 assert set(node)=={'query','zero','one'}
 q=tuple(node['query']);assert q in Q
 internal.append(q)
 verify_node(node['zero'],path+((q,0),))
 verify_node(node['one'],path+((q,1),))
verify_node(cert['tree'],())
assert len(internal)==1023 and len(term)==1024 and len(set(term))==1024
print('LITTLESTONE_DEPTH_TEN_TREE_PASS internal',len(internal),'leaves',len(term))
# Every possible first query has exactly n!/6 distinct positive concepts.
# A depth-eleven complete tree would require >=1024 positive concepts.
assert math.factorial(n)//6==840<1024
print('LITTLESTONE_DEPTH_ELEVEN_OBSTRUCTION_PASS',840,1024)
print('TERNARY_CHOICE_ALL_CHECKS_PASS')
