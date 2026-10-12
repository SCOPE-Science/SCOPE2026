from itertools import combinations, product
from functools import lru_cache


def integer_partitions(n, cap=None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for a in range(cap, 0, -1):
        for tail in integer_partitions(n-a, a):
            yield (a,) + tail


def graph(profile):
    parts=[]; part_of={}; v=0
    for i,m in enumerate(profile):
        P=[]
        for _ in range(m):
            P.append(v); part_of[v]=i; v+=1
        parts.append(P)
    N=v
    adj=[set() for _ in range(N)]
    for u in range(N):
        for w in range(u+1,N):
            if part_of[u] != part_of[w]:
                adj[u].add(w); adj[w].add(u)
    return N,parts,part_of,adj


def geodesic_triples(profile, d):
    N,parts,part_of,adj=graph(profile)
    E=set()
    if d < 2:
        return E
    for u in range(N):
        for v in range(u+1,N):
            if v in adj[u]:
                continue
            common=adj[u] & adj[v]
            for w in common:
                E.add(frozenset((u,w,v)))
    return E


def omega3(N,E):
    best=0
    for mask in range(1<<N):
        s=mask.bit_count()
        if s<=best: continue
        V=[v for v in range(N) if mask>>v&1]
        if all(frozenset(T) in E for T in combinations(V,3)):
            best=s
    return best


def chi3(N,E):
    inc=[[] for _ in range(N)]
    for e in E:
        t=tuple(e)
        for v in t: inc[v].append(t)
    order=sorted(range(N), key=lambda v:-len(inc[v]))
    for q in range(1,N+1):
        col=[-1]*N
        def bt(j):
            if j==N: return True
            v=order[j]
            for c in range(q):
                col[v]=c
                bad=False
                for e in inc[v]:
                    if all(col[x]==c for x in e):
                        bad=True; break
                if not bad and bt(j+1): return True
                col[v]=-1
            return False
        if bt(0): return q
    raise AssertionError


def subprofiles(profile):
    seen=set()
    for x in product(*[range(m+1) for m in profile]):
        q=tuple(sorted((a for a in x if a), reverse=True))
        if q and q not in seen:
            seen.add(q); yield q

@lru_cache(None)
def direct_pair(profile,d):
    N=sum(profile)
    if len(profile)==1:
        return 1, min(2,N)
    E=geodesic_triples(profile,d)
    return chi3(N,E), omega3(N,E)


def direct_perfect(profile,d):
    for q in subprofiles(profile):
        chi,om=direct_pair(q,d)
        if chi != (om+1)//2:
            return False,q,chi,om
    return True,None,None,None


def predicted(profile):
    r=len(profile)
    M=max(profile)
    p=sum(m>=2 for m in profile)
    return r<=2 or p<=1 or M<=2

profiles=0
induced_profiles=0
for n in range(2,9):
    for profile in integer_partitions(n):
        if len(profile)<2:
            continue
        profiles += 1
        expected=predicted(profile)
        for d in (2,3,4):
            got,witness,chi,om=direct_perfect(profile,d)
            assert got==expected, (profile,d,got,expected,witness,chi,om)
        induced_profiles += len(list(subprofiles(profile)))

# Check the asserted unique minimal obstruction explicitly.
assert not direct_perfect((3,2,1),2)[0]
for q in ((2,2,1),(3,1,1),(3,2)):
    assert direct_perfect(q,2)[0], q

print(f"ALL CHECKS PASSED; profiles={profiles}; induced_profile_checks={induced_profiles*3}; d_values=2,3,4; unique_obstruction=K_3,2,1; orders=2..8")
