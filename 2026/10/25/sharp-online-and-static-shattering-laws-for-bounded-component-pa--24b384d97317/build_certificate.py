"""Generate an explicit online-shattering certificate for the 4-point strict-poset relation class."""
import itertools,functools,json,pathlib
ROOT=pathlib.Path(__file__).parent
n=4
pairs=list(itertools.combinations(range(n),2))
queries=list(itertools.permutations(range(n),2))
orders=[]
for orient in itertools.product((0,1,2),repeat=len(pairs)):
    E=set()
    for (a,b),s in zip(pairs,orient):
        if s==1:E.add((a,b))
        if s==2:E.add((b,a))
    if all((a,d) in E for a,b in E for c,d in E if b==c):
        orders.append(tuple(sorted(E)))
assert len(orders)==219
masks=[sum(1<<j for j,R in enumerate(orders) if q in R) for q in queries]
ALL=(1<<len(orders))-1
@functools.lru_cache(None)
def dimension(S):
    if S&(S-1)==0:return 0
    out=0
    for m in masks:
        T=S&m;U=S&(~m&ALL)
        if T and U:
            out=max(out,1+min(dimension(T),dimension(U)))
    return out
assert dimension(ALL)==6

def certificate(S,depth):
    if depth==0:
        return {'relations':[list(pair) for pair in orders[(S&-S).bit_length()-1]]}
    for q,m in zip(queries,masks):
        T=S&m;U=S&(~m&ALL)
        if T and U and dimension(T)>=depth-1 and dimension(U)>=depth-1:
            return {'query':list(q),'yes':certificate(T,depth-1),'no':certificate(U,depth-1)}
    raise AssertionError((depth,S.bit_count()))

cert={'description':'Full binary depth-6 strict-poset edge-relation shattering witness','n':4,'depth':6,'tree':certificate(ALL,6)}
(ROOT/'poset_depth6_certificate.json').write_text(json.dumps(cert,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')
print('GENERATED_CERTIFICATE_NODES=63 LEAVES=64')
print('LABELLED_POSETS=219 LITTLES_TONE_DIMENSION=6')
print('STATES_VISITED',dimension.cache_info().currsize)

# Separate three-point certificate for the critical first dimension gap.
n3=3
pairs3=list(itertools.combinations(range(n3),2))
Q3=list(itertools.permutations(range(n3),2))
P3=[]
for orient in itertools.product((0,1,2),repeat=len(pairs3)):
    E=set()
    for (a,b),s in zip(pairs3,orient):
        if s==1:E.add((a,b))
        if s==2:E.add((b,a))
    if all((a,d) in E for a,b in E for c,d in E if b==c):P3.append(tuple(sorted(E)))
assert len(P3)==19
MASK3=[sum(1<<i for i,R in enumerate(P3) if q in R) for q in Q3]
ALL3=(1<<len(P3))-1
@functools.lru_cache(None)
def dim3(S):
    if S&(S-1)==0:return 0
    return max([1+min(dim3(S&m),dim3(S&(~m&ALL3))) for m in MASK3 if (S&m) and (S&(~m&ALL3))] or [0])
assert dim3(ALL3)==3

def build3(S,depth):
    if depth==0:return {'relations':[list(x) for x in P3[(S&-S).bit_length()-1]]}
    for q,m in zip(Q3,MASK3):
        T=S&m;U=S&(~m&ALL3)
        if T and U and dim3(T)>=depth-1 and dim3(U)>=depth-1:
            return {'query':list(q),'yes':build3(T,depth-1),'no':build3(U,depth-1)}
    raise AssertionError('No witness')
(ROOT/'poset_depth3_certificate.json').write_text(json.dumps({'n':3,'depth':3,'tree':build3(ALL3,3)},sort_keys=True,separators=(',',':'))+'\n')
print('GENERATED_N3_CERTIFICATE_NODES=7 LEAVES=8')
