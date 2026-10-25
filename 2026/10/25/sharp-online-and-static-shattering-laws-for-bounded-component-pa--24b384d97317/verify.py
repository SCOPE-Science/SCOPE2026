"""Exact verification for strict-poset pair-membership shattering. Python 3, standard library."""
import itertools,functools,json,math,pathlib
HERE=pathlib.Path(__file__).resolve().parent

def enumerate_posets(n):
    # Independent ordered-pair Boolean-mask exhaustive census, not ternary choices.
    Q=list(itertools.permutations(range(n),2));P=[]
    for bits in range(1<<len(Q)):
        R={q for j,q in enumerate(Q) if (bits>>j)&1}
        if any((b,a) in R for a,b in R):continue
        if any((a,c) not in R for a,b in R for d,c in R if b==d):continue
        P.append(frozenset(R))
    return P,Q

def littlestone(P,Q):
    ALL=(1<<len(P))-1
    masks=[sum(1<<i for i,R in enumerate(P) if q in R) for q in Q]
    @functools.lru_cache(None)
    def rank(S):
        if S==0:return -1
        if S & (S-1)==0:return 0
        best=0
        for m in masks:
            T=S&m;U=S&(~m&ALL)
            if T and U:best=max(best,1+min(rank(T),rank(U)))
        return best
    answer=rank(ALL)
    return answer,rank.cache_info().currsize

def vc(P,Q):
    for d in range(len(Q),-1,-1):
        for I in itertools.combinations(range(len(Q)),d):
            patterns={sum(((q in R)<<j) for j,q in enumerate([Q[i] for i in I])) for R in P}
            if len(patterns)==(1<<d):return d
    raise AssertionError

nums=[]
for n in range(1,5):
    P,Q=enumerate_posets(n)
    ld,states=littlestone(P,Q)
    v=vc(P,Q)
    nums.append((n,len(P),v,ld))
assert nums==[(1,1,0,0),(2,3,1,1),(3,19,2,3),(4,219,4,6)]
print('FINITE_PROFILE',nums)
P,Q=enumerate_posets(4)
cert=json.loads((HERE/'poset_depth6_certificate.json').read_text())
assert cert['n']==4 and cert['depth']==6
leaves=[];qcount=0

def walk(node,answers):
    global qcount
    if 'query' not in node:
        R=frozenset(map(tuple,node['relations']))
        assert R in P
        assert all((q in R)==v for q,v in answers)
        leaves.append(R)
        return
    q=tuple(node['query'])
    assert q in Q and q not in [p for p,v in answers]
    qcount+=1
    walk(node['yes'],answers+[(q,True)])
    walk(node['no'],answers+[(q,False)])
walk(cert['tree'],[])
assert qcount==63 and len(leaves)==64 and len(set(leaves))==64
print('TREE_CERTIFICATE_INTERNAL',qcount,'LEAVES',len(leaves))
cert3=json.loads((HERE/'poset_depth3_certificate.json').read_text())
P3,Q3=enumerate_posets(3)
ct3=[0,0]
def walk3(node, answers):
    if 'query' not in node:
        R=frozenset(map(tuple,node['relations']))
        assert R in P3
        assert all((q in R)==val for q,val in answers)
        ct3[1]+=1
        return
    q=tuple(node['query'])
    assert q in Q3 and q not in [p for p,v in answers]
    ct3[0]+=1
    walk3(node['yes'],answers+[(q,True)])
    walk3(node['no'],answers+[(q,False)])
walk3(cert3['tree'],[])
assert ct3==[7,8]
print('CRITICAL_N3_CERTIFICATE',ct3)

S=[R for R in P if (0,1) in R]
assert len(S)==66
hist=[]
for q in Q:
    if q==(0,1):continue
    yes=sum(q in R for R in S)
    no=66-yes
    if yes>=32 and no>=32:
        small=[R for R in S if (q in R)==(yes==32)]
        assert len(small)==32
        max_min=max(min(sum(p in R for R in small),len(small)-sum(p in R for R in small)) for p in Q)
        assert max_min<=14
        hist.append((q,yes,no,max_min))
assert len(hist)==4
print('POSITIVE_FIRST_QUERY_TOTAL',len(S))
print('POSSIBLE_DEPTH_SIX_SECOND_QUERY_BRANCHES',hist)
# Recheck bounded-component VC profiles on all 4-point posets.
for b in range(1,5):
    def comp_max(R):
        par=list(range(4))
        def root(x):
            while par[x]!=x:x=par[x]
            return x
        for a,c in R:
            x,y=root(a),root(c)
            if x!=y:par[x]=y
        return max(sum(root(i)==root(j) for j in range(4)) for i in range(4))
    Pb=[R for R in P if comp_max(R)<=b]
    observed=vc(Pb,Q)
    expected=(4//b)*(b*b//4)+(4%b)**2//4
    assert observed==expected,(b,observed,expected)
    print('BOUNDED_COMPONENT_VC',b,len(Pb),observed)
print('ALL_POSET_CHECKS_PASS')
