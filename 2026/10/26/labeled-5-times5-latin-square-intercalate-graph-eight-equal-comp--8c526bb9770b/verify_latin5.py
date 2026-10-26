"""Exhaustive verification of the labeled order-five intercalate-switch graph.

Requires Python >=3.9, no third-party packages. All labels are 0,1,2,3,4.
No outside files or downloaded tables are used.
"""
from collections import Counter, deque
from itertools import permutations
from math import factorial

N=5
PERMS=tuple(permutations(range(N)))
PERM_IDS={p:i for i,p in enumerate(PERMS)}
INV={p:tuple(p.index(j) for j in range(N)) for p in PERMS}
Q=((0,1,2,3,4),(1,0,3,4,2),(2,3,4,0,1),(3,4,1,2,0),(4,2,0,1,3))
BASE=bytes(z for row in Q for z in row)
CYCLIC=bytes((r+c)%5 for r in range(N) for c in range(N))

def sign(p):
    return (-1)**sum(p[a]>p[b] for a in range(N) for b in range(a+1,N))

def enumerate_latin():
    """Generate once each square by fixing row zero, then permuting symbols."""
    normalized=[]
    def backtrack(rows,used):
        if len(rows)==N:
            normalized.append(bytes(x for row in rows for x in row))
            return
        for row in PERMS:
            if all(not (used[c] & (1<<row[c])) for c in range(N)):
                backtrack(rows+[row],[used[c] | (1<<row[c]) for c in range(N)])
    backtrack([tuple(range(N))],[1<<j for j in range(N)])
    assert len(normalized)==1344
    squares={bytes(p[x] for x in a) for a in normalized for p in PERMS}
    assert len(squares)==1344*factorial(N)==161280
    return squares

def switches(s):
    """Exactly one neighbor per legal 2x2 two-symbol Latin subsquare."""
    out=[]
    for r in range(N):
        for t in range(r+1,N):
            for c in range(N):
                for d in range(c+1,N):
                    a,b,e,f=r*N+c,r*N+d,t*N+c,t*N+d
                    if s[a]==s[f] and s[b]==s[e]:
                        z=bytearray(s)
                        z[a],z[b],z[e],z[f]=s[b],s[a],s[a],s[b]
                        out.append(((r,t,c,d),bytes(z)))
    assert len({q for _,q in out})==len(out)
    return out

def isotopies(a,b):
    """All triples of row/column/symbol permutations taking a to b."""
    found=[]
    for p in PERMS:
        invp=INV[p]
        for q in PERMS:
            invq=INV[q]
            h=[-1]*N
            for c in range(N): h[a[N*invp[0]+invq[c]]]=b[c]
            if len(set(h))!=N: continue
            if all(b[N*r+c]==h[a[N*invp[r]+invq[c]]]
                   for r in range(N) for c in range(N)):
                found.append((p,q,tuple(h)))
    return found

def component(start):
    dist={start:0}
    queue=deque([start])
    while queue:
        s=queue.popleft()
        for _,t in switches(s):
            if t not in dist:
                dist[t]=dist[s]+1
                queue.append(t)
    return dist

def signature(s):
    def prod(seq):
        o=1
        for p in seq:o*=sign(p)
        return o
    rows=[tuple(s[N*r+c] for c in range(N)) for r in range(N)]
    cols=[tuple(s[N*r+c] for r in range(N)) for c in range(N)]
    syms=[tuple(next(c for c in range(N) if s[N*r+c]==z) for r in range(N)) for z in range(N)]
    return (prod(rows),prod(cols),prod(syms))

def main():
    S=enumerate_latin()
    assert BASE in S and CYCLIC in S
    assert switches(CYCLIC)==[]
    sw=switches(BASE)
    assert len(sw)==4
    h0=isotopies(BASE,BASE)
    hc=isotopies(CYCLIC,CYCLIC)
    assert len(h0)==12 and len(hc)==100
    assert all(sign(p)==sign(q)==sign(t)==1 for p,q,t in h0)
    witnesses=[]
    for coord,s in sw:
        maps=isotopies(BASE,s)
        assert len(maps)==12
        even=[(p,q,t) for p,q,t in maps if sign(p)==sign(q)==sign(t)==1]
        assert len(even)==12
        witnesses.append((coord,even[0]))
    d=component(BASE)
    assert len(d)==(factorial(N)//2)**3//len(h0)==18000
    shells=dict(sorted(Counter(d.values()).items()))
    assert sum(shells.values())==18000
    assert max(shells)==13
    # Exact independent full state-space check: degrees and component sizes.
    deg=Counter(len(switches(s)) for s in S)
    assert deg=={0:17280,4:144000}
    unseen=set(S)
    components=Counter()
    sector_sizes=Counter()
    while unseen:
        seed=unseen.pop()
        queue=[seed]
        for s in queue:
            for _,t in switches(s):
                if t in unseen:
                    unseen.remove(t)
                    queue.append(t)
        components[len(queue)]+=1
        if len(queue)>1:
            tri=signature(seed)
            assert all(signature(t)==tri for t in queue)
            sector_sizes[tri]+=1
    assert components=={1:17280,18000:8}
    assert sorted(sector_sizes.values())==[2,2,2,2]
    # Orbit-stabilizer and exhaustive enumeration prove the two orbits cover S.
    assert factorial(N)**3//len(h0)==144000
    assert factorial(N)**3//len(hc)==17280
    assert 144000+17280==len(S)
    # The ALT(5)^3 orbit of BASE has 18,000 states, contains its four
    # switched neighbors, and is closed under switches by equivariance.
    # Its entire size is reached by BFS. It is a vertex-transitive component.
    print('LATIN_5_COUNT',len(S))
    print('AUTOTOPISM_ORDERS',len(h0),len(hc))
    print('BASE_INTERCALATE_WITNESSES',witnesses)
    print('DEGREES',sorted(deg.items()))
    print('COMPONENTS',sorted(components.items()))
    print('SECTORS',sorted(sector_sizes.items()))
    print('SHELLS',shells)
    print('CONNECTED_COMPONENT_DIAMETER',max(shells))
    print('VERIFY_OK')
if __name__=='__main__':main()
