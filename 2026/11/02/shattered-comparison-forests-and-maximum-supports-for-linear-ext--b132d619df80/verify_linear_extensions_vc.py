"""Finite enumeration test of pair-comparison shattering in linear extensions.

Usage: python verify_linear_extensions_vc.py [max_order]
Tests every labelled strict poset through the selected order (default: five).
"""
import itertools
import sys


def support_data(n, pairs):
    k = len(pairs)
    out = []
    for mask in range(1 << k):
        parent = list(range(n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        forest = True
        for j,(a,b) in enumerate(pairs):
            if mask >> j & 1:
                ra, rb = root(a), root(b)
                if ra == rb:
                    forest = False
                    break
                parent[ra] = rb
        if not forest:
            out.append(None)
            continue
        groups = {}
        comp = []
        for v in range(n):
            r = root(v)
            if r not in groups: groups[r] = len(groups)
            comp.append(groups[r])
        out.append(tuple(comp))
    return out


def cycle_after_contract(n, signed_relations, comp):
    m = max(comp)+1
    nexts = [set() for _ in range(m)]
    for u,v in signed_relations:
        a,b=comp[u],comp[v]
        if a==b:return True
        nexts[a].add(b)
    indeg=[0]*m
    for ns in nexts:
        for x in ns:indeg[x]+=1
    todo=[a for a in range(m) if indeg[a]==0]
    done=0
    while todo:
        x=todo.pop()
        done+=1
        for y in nexts[x]:
            indeg[y]-=1
            if indeg[y]==0:todo.append(y)
    return done!=m


def height(n, rel):
    dp=[1]*n
    for _ in range(n):
        nxt=dp[:]
        for u,v in rel:nxt[v]=max(nxt[v],dp[u]+1)
        if nxt==dp:break
        dp=nxt
    return max(dp)


def extremizer_formula(n, h, relations, ordered_parts):
    count=0
    for f, block_sizes, weights in ordered_parts[h]:
        if all(f[u]<f[v] for u,v in relations):
            count += weights
    return count


def ordered_surjective_rank_maps(n):
    out={h: [] for h in range(1,n+1)}
    for h in range(1,n+1):
        for f in itertools.product(range(h),repeat=n):
            if len(set(f)) != h: continue
            sizes=[f.count(i) for i in range(h)]
            weights=1
            for t in sizes:
                weights *= t**(t-2) if t>=2 else 1
            out[h].append((f,sizes,weights))
    return out


def check(n):
    pairs=list(itertools.combinations(range(n),2))
    pair_index={p:i for i,p in enumerate(pairs)}
    supports=support_data(n,pairs)
    permmasks=[]
    for perm in itertools.permutations(range(n)):
        loc=[0]*n
        for i,u in enumerate(perm):loc[u]=i
        permmasks.append(sum(1<<j for j,(a,b) in enumerate(pairs) if loc[a]<loc[b]))
    nposets=nchecks=0
    rank_maps=ordered_surjective_rank_maps(n)
    # In each 3-ary digit: 0 incomparable, 1 a<b, 2 b<a.
    for digits in itertools.product((0,1,2), repeat=len(pairs)):
        rel=[]; plus=minus=0
        for j,code in enumerate(digits):
            a,b=pairs[j]
            if code==1:
                rel.append((a,b));plus|=1<<j
            elif code==2:
                rel.append((b,a));minus|=1<<j
        adjacency=[[False]*n for _ in range(n)]
        for a,b in rel:adjacency[a][b]=True
        if any(adjacency[a][b] and adjacency[b][c] and not adjacency[a][c]
               for a in range(n) for b in range(n) for c in range(n)):
            continue
        nposets+=1
        ext=[x for x in permmasks if x&plus == plus and x&minus == 0]
        H=height(n,rel)
        mx=-1
        extremal=0
        for mask, comp in enumerate(supports):
            predicted=comp is not None and not cycle_after_contract(n,rel,comp)
            if 1<<mask.bit_count()>len(ext):
                actual=False
            else:
                actual=len({order&mask for order in ext}) == 1<<mask.bit_count()
            if predicted!=actual:
                raise AssertionError(f'n={n}; relations={rel}; support={mask}; predicted={predicted}; actual={actual}')
            if actual:
                q=mask.bit_count()
                if q>mx: mx=q;extremal=1
                elif q==mx:extremal+=1
            nchecks+=1
        if mx!=n-H:
            raise AssertionError(f'n={n}; relations={rel}; VC={mx}; height={H}')
        expected_extremal=extremizer_formula(n,H,rel,rank_maps)
        if extremal!=expected_extremal:
            raise AssertionError(f'n={n}; relations={rel}; extremal={extremal}; formula={expected_extremal}')
    return nposets,nchecks

if __name__=='__main__':
    maximal=int(sys.argv[1]) if len(sys.argv)>1 else 5
    for n in range(1,maximal+1):
        posets,checks=check(n)
        print(f'n={n} posets={posets} support_tests={checks}',flush=True)
    print('ALL_LINEAR_EXTENSION_SHATTERING_CHECKS_PASS',flush=True)
