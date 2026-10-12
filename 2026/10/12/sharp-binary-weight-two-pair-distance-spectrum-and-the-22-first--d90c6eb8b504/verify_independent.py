"""Independent closed Euler-trail enumeration for length ten (stdlib only)."""
from functools import lru_cache
from itertools import combinations, permutations
V=range(5)
edges=list(combinations(V,2)); assert len(edges)==10
edge_index={e:i for i,e in enumerate(edges)}

@lru_cache(None)
def ntrails(at,unused):
    if unused==0: return int(at==0)
    return sum(ntrails(v,unused^(1<<edge_index[tuple(sorted((at,v)))]))
               for v in V if v!=at and unused&(1<<edge_index[tuple(sorted((at,v)))]))
assert ntrails(0,(1<<10)-1)==528

tours=[]
def generate(at,unused,seq):
    if unused==0:
        if at==seq[0]: tours.append(tuple(seq))
        return
    for v in V:
        if v==at:continue
        mask=1<<edge_index[tuple(sorted((at,v)))]
        if unused&mask: generate(v,unused^mask,seq+[v])

generate(0,(1<<10)-1,[0])
assert len(tours)==528
# A code has one 2-subset support for each color, hence canonically label its
# words by order of their earliest coordinate, removing arbitrary color names.
codes=set()
for tour in tours:
    seq=tour[:-1]
    for perm in permutations(V):
        seq2=tuple(perm[t] for t in seq)
        positions=tuple(tuple(i for i,c in enumerate(seq2) if c==a) for a in V)
        code=tuple(sorted(positions))
        codes.add(code)
assert len(codes)==22
assert len(tours)*5//120==22
for code in codes:
    assert len(code)==5 and all(len(x)==2 for x in code)
    assert len(set(sum((list(x) for x in code),[])))==10
    for x,y in combinations(code,2):
        union=set(x)^set(y)
        d=sum((i in union) or ((i+1)%10 in union) for i in range(10))
        assert d>=7
print('INDEPENDENT_VERIFY_OK K5_tours_start0=528 K5_color_sequences=2640 optimal_unlabeled_sets=22')
