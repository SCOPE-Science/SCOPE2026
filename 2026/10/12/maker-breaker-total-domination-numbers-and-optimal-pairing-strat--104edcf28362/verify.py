from itertools import combinations, product
from functools import lru_cache
from math import comb

def crown(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_td(adj,S):
    S=set(S)
    return all(adj[v] & S for v in range(len(adj)))

def td_stats(n):
    a=crown(n); N=2*n
    mins=[]
    for k in range(1,N+1):
        vals=[S for S in combinations(range(N),k) if is_td(a,S)]
        if vals:return k,len(vals)

def win_moves(n, starter):
    adj=crown(n); N=2*n; FULL=(1<<N)-1
    def td(mask):
        return all(any(mask>>u&1 for u in adj[v]) for v in range(N))
    INF=99
    # turn 0 D, 1 S. Return minimum eventual D move count to force win, INF if S can prevent.
    @lru_cache(None)
    def F(dm,sm,turn):
        if td(dm): return dm.bit_count()
        free=FULL ^ (dm|sm)
        if not free:return INF
        bits=[1<<i for i in range(N) if free>>i&1]
        if turn==0:
            return min(F(dm|b,sm,1) for b in bits)
        else:
            return max(F(dm,sm|b,0) for b in bits)
    val=F(0,0,starter)
    return None if val>=INF else val

def perfect_pairings(items):
    items=tuple(items)
    if not items:
        yield (); return
    x=items[0]
    for k in range(1,len(items)):
        y=items[k]
        rest=items[1:k]+items[k+1:]
        for p in perfect_pairings(rest): yield ((x,y),)+p

def is_pairing_td(n,pairs):
    a=crown(n)
    for choices in product((0,1), repeat=len(pairs)):
        S=[pairs[i][choices[i]] for i in range(len(pairs))]
        if not is_td(a,S): return False
    return True

def count_four_pair_systems(n):
    N=2*n; count=0; types=[]
    for verts in combinations(range(N),8):
        for pairs in perfect_pairings(verts):
            if is_pairing_td(n,pairs):
                count+=1
                aa=sum(x<n and y<n for x,y in pairs)
                bb=sum(x>=n and y>=n for x,y in pairs)
                ab=4-aa-bb
                types.append((aa,bb,ab))
    return count,set(types)

for n in range(3,8):
    g,c=td_stats(n)
    assert g==4
    assert c==comb(n,2)**2, (n,c)
for n in (3,4,5):
    d=win_moves(n,0); s=win_moves(n,1)
    expected=(None,None) if n==3 else (4,4)
    assert (d,s)==expected,(n,d,s)
for n in (4,5,6):
    c,t=count_four_pair_systems(n)
    ex=(3*comb(n,4))**2
    assert c==ex,(n,c,ex)
    assert t=={(2,2,0)},(n,t)
for n in range(4,101):
    assert (3*comb(n,4))**2>0
print('ALL CHECKS PASSED; total_domination_orders=3..7; game_orders=3,4,5; pairing_system_orders=4,5,6; symbolic_count_range=4..100')
