from itertools import combinations_with_replacement, product
from functools import lru_cache

V = tuple(range(1,8))
T = 5
WITNESS = (1,1,1,2,2,2,2)

def options(q):
    out=[(q,)]
    for u in V:
        for v in V:
            if u < v and (u ^ v) == q:
                out.append((u,v))
    assert len(out)==4
    return tuple(out)
OPTS={q:options(q) for q in V}

def feasible(queries, caps):
    # Backtracking over exact column-type capacities. Each option consumes one copy
    # of every listed type; the options are exactly the minimal recovery sets of
    # size at most two in F_2^3.
    queries=tuple(queries)
    @lru_cache(None)
    def rec(rem, caps):
        if not rem:
            return True
        # choose a query with the fewest currently feasible options
        best_i=None; best_opts=None
        for i,q in enumerate(rem):
            fo=[]
            for opt in OPTS[q]:
                ok=True
                for x in opt:
                    if caps[x-1] <= 0:
                        ok=False; break
                if ok: fo.append(opt)
            if not fo:
                return False
            if best_opts is None or len(fo)<len(best_opts):
                best_i=i; best_opts=fo
        q=rem[best_i]
        rem2=rem[:best_i]+rem[best_i+1:]
        for opt in best_opts:
            nc=list(caps)
            for x in opt: nc[x-1]-=1
            if rec(rem2, tuple(nc)):
                return True
        return False
    return rec(queries, tuple(caps))

def Aq(caps,q):
    s=caps[q-1]
    seen=set()
    for u in V:
        v=u^q
        if v in V and u<v:
            s += min(caps[u-1],caps[v-1])
    return s

def comps(total, parts=7):
    if parts==1:
        yield (total,); return
    for x in range(total+1):
        for tail in comps(total-x, parts-1):
            yield (x,)+tail

assert sum(WITNESS)==11
assert feasible((1,2,3,4,5), WITNESS)
multisets=list(combinations_with_replacement(V,T))
assert len(multisets)==462
bad=[qs for qs in multisets if not feasible(qs,WITNESS)]
assert not bad, bad[:1]

# Exhaustive repeated-query obstruction at total length ten.
cs=list(comps(10))
assert len(cs)==8008
mx_pair=-1; mx_total=-1; repeat_feasible=[]
for c in cs:
    pair=sum(min(c[i],c[j]) for i in range(7) for j in range(i+1,7))
    mx_pair=max(mx_pair,pair)
    vals=[Aq(c,q) for q in V]
    mx_total=max(mx_total,sum(vals))
    if min(vals)>=5:
        repeat_feasible.append(c)
assert mx_pair==24, mx_pair
assert mx_total==34, mx_total
assert not repeat_feasible

# Supplemental exact census at the first feasible length: all repeated-query-
# feasible multiplicity vectors are fully functional for five requests.
c11=[c for c in comps(11) if min(Aq(c,q) for q in V)>=5]
assert len(c11)==77, len(c11)
assert all(feasible(qs,c) for c in c11 for qs in multisets)
patterns={tuple(sorted(c)) for c in c11}
assert patterns=={(0,1,2,2,2,2,2),(1,1,1,2,2,2,2)}, patterns

print('QUERY_MULTISETS', len(multisets))
print('TOTAL10_COMPOSITIONS', len(cs))
print('MAX_PAIR_MIN_SUM_AT_10', mx_pair)
print('MAX_SUM_AQ_AT_10', mx_total)
print('LENGTH11_REPEATED_QUERY_FEASIBLE', len(c11))
print('LENGTH11_PATTERNS', sorted(patterns))
print('VERIFY_OK')
