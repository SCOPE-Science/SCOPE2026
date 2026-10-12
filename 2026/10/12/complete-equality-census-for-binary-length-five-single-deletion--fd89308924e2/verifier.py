from itertools import product, combinations
from collections import Counter

N=5
WORDS=[''.join(p) for p in product('01', repeat=N)]
INDEX={w:i for i,w in enumerate(WORDS)}

def deletion_shadow(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def lcs(a,b):
    m=len(a); n=len(b)
    dp=[0]*(n+1)
    for i in range(1,m+1):
        prev=0
        for j in range(1,n+1):
            old=dp[j]
            if a[i-1]==b[j-1]: dp[j]=prev+1
            else: dp[j]=max(dp[j],dp[j-1])
            prev=old
    return dp[n]

D={w:deletion_shadow(w) for w in WORDS}
adj_shadow={w:set() for w in WORDS}
adj_lcs={w:set() for w in WORDS}
for a,b in combinations(WORDS,2):
    if D[a].isdisjoint(D[b]):
        adj_shadow[a].add(b); adj_shadow[b].add(a)
    if lcs(a,b) <= N-2:
        adj_lcs[a].add(b); adj_lcs[b].add(a)
assert adj_shadow==adj_lcs

# Independent exhaustive target-size searches.
def cliques_of_size(k):
    out=[]
    for c in combinations(WORDS,k):
        ok=True
        for a,b in combinations(c,2):
            if b not in adj_shadow[a]:
                ok=False; break
        if ok: out.append(c)
    return out

six=cliques_of_size(6)
seven=cliques_of_size(7)
assert len(six)==6
assert len(seven)==0

# Independent maximal-clique search.
maximal=[]
def bronk(R,P,X):
    if not P and not X:
        maximal.append(tuple(sorted(R)))
        return
    u=max(P|X,key=lambda x: len(P & adj_shadow[x]),default=None)
    candidates=P-(adj_shadow[u] if u is not None else set())
    for v in list(candidates):
        bronk(R|{v}, P & adj_shadow[v], X & adj_shadow[v])
        P.remove(v); X.add(v)
bronk(set(),set(WORDS),set())
mx=max(map(len,maximal))
max_from_bk=sorted(set(c for c in maximal if len(c)==mx))
assert mx==6 and max_from_bk==sorted(six)

comp=lambda w: ''.join('1' if ch=='0' else '0' for ch in w)
rev=lambda w: w[::-1]
TRANS=(lambda w:w, comp, rev, lambda w:comp(rev(w)))

def orbit(code):
    return {tuple(sorted(f(w) for w in code)) for f in TRANS}

seen=set(); orbit_reps=[]
for c in sorted(six):
    if c in seen: continue
    o=orbit(c); seen |= o; orbit_reps.append((c,o))
assert len(orbit_reps)==3
assert Counter(len(o) for _,o in orbit_reps)==Counter({2:3})

# Perfectness and VT-syndrome structure.
def syndrome(w):
    return sum((i+1)*int(ch) for i,ch in enumerate(w)) % 6
vt={a:tuple(w for w in WORDS if syndrome(w)==a) for a in range(6)}
perfect=[]; nonperfect=[]
for c in sorted(six):
    cov=set().union(*(D[w] for w in c))
    if len(cov)==16: perfect.append(c)
    else: nonperfect.append(c)
assert len(perfect)==2 and len(nonperfect)==4
assert set(perfect)=={tuple(sorted(vt[0])),tuple(sorted(vt[3]))}
assert sorted(len(set().union(*(D[w] for w in c))) for c in nonperfect)==[14,14,14,14]

profiles=Counter()
for c in six:
    profiles[(tuple(sorted(len(D[w]) for w in c)),len(set().union(*(D[w] for w in c))))]+=1
assert profiles==Counter({((1,1,2,2,4,4),14):2,((1,1,2,2,3,5),14):2,((1,2,2,3,3,5),16):2})

print('VERIFY_OK vertices=32 compatibility_edges=%d maximum=6 labeled_maxima=6 size7=0 maximal_hist=%s natural_group=4 orbits=3 orbit_sizes=2x3 perfect=2 nonperfect=4 perfect_vt_syndromes=0,3 nonperfect_coverage=14x4 profiles=2x(1,1,2,2,4,4;14),2x(1,1,2,2,3,5;14),2x(1,2,2,3,3,5;16)' % (sum(len(v) for v in adj_shadow.values())//2, ','.join(f'{k}:{v}' for k,v in sorted(Counter(map(len,maximal)).items()))))
