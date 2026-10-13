#!/usr/bin/env python3
import itertools
from collections import Counter, deque

N=6
R=2
RANKS=3

def lcs(a,b):
    dp=[0]*(len(b)+1)
    for x in a:
        nd=[0]*(len(b)+1)
        for j,y in enumerate(b,1):
            if x==y:
                nd[j]=dp[j-1]+1
            else:
                nd[j]=max(dp[j],nd[j-1])
        dp=nd
    return dp[-1]

def multipermutations():
    return sorted(set(itertools.permutations([0,0,1,1,2,2])))

WORDS=multipermutations()
INDEX={w:i for i,w in enumerate(WORDS)}

def representatives(w):
    groups=[[i for i,x in enumerate(w) if x==rank] for rank in range(RANKS)]
    return [
        tuple(a+b+c)
        for a in itertools.permutations(groups[0])
        for b in itertools.permutations(groups[1])
        for c in itertools.permutations(groups[2])
    ]

REPS=[representatives(w) for w in WORDS]
assert len(WORDS)==90
assert all(len(x)==8 for x in REPS)

def ordinary_ulam(p,q):
    return N-lcs(p,q)

def quotient_distance(i,j):
    # Farnoud--Milenkovic 2013 definition: minimum ordinary Ulam
    # distance over the two equivalence classes of representatives.
    return min(ordinary_ulam(p,q) for p in REPS[i] for q in REPS[j])

D=[[0]*len(WORDS) for _ in WORDS]
pair_hist=Counter()
for i in range(len(WORDS)):
    for j in range(i+1,len(WORDS)):
        d=quotient_distance(i,j)
        D[i][j]=D[j][i]=d
        pair_hist[d]+=1
assert pair_hist==Counter({1:1080,2:1440,3:1440,4:45})

# Independent ordinary-Ulam implementation via longest increasing
# subsequence of the relative-position sequence.  We recompute every
# quotient distance by minimizing this implementation over the same
# equivalence classes and require exact agreement.
def lis_length(seq):
    tails=[]
    for x in seq:
        lo,hi=0,len(tails)
        while lo<hi:
            mid=(lo+hi)//2
            if tails[mid]<x:
                lo=mid+1
            else:
                hi=mid
        if lo==len(tails):
            tails.append(x)
        else:
            tails[lo]=x
    return len(tails)

def ordinary_ulam_lis(p,q):
    pos={x:i for i,x in enumerate(q)}
    return N-lis_length([pos[x] for x in p])

D2=[[0]*len(WORDS) for _ in WORDS]
for i in range(len(WORDS)):
    for j in range(i+1,len(WORDS)):
        d=min(ordinary_ulam_lis(p,q) for p in REPS[i] for q in REPS[j])
        D2[i][j]=D2[j][i]=d
assert D2==D

# Compatibility graph for minimum r-regular Ulam distance at least 3.
M=len(WORDS)
adj=[0]*M
for i in range(M):
    for j in range(i+1,M):
        if D[i][j]>=3:
            adj[i]|=1<<j
            adj[j]|=1<<i

# Exact Bron--Kerbosch enumeration of all maximal cliques.
best=0
maxima=[]
def bronk(Rset,P,X):
    global best,maxima
    if not P and not X:
        size=Rset.bit_count()
        C=tuple(i for i in range(M) if (Rset>>i)&1)
        if size>best:
            best=size
            maxima=[C]
        elif size==best:
            maxima.append(C)
        return
    if Rset.bit_count()+P.bit_count()<best:
        return
    U=P|X
    if U:
        pivot=max((u for u in range(M) if (U>>u)&1),
                  key=lambda u:(P&adj[u]).bit_count())
        Q=P&~adj[pivot]
    else:
        Q=P
    while Q:
        bit=Q&-Q
        v=bit.bit_length()-1
        bronk(Rset|bit,P&adj[v],X&adj[v])
        P&=~bit
        X|=bit
        Q&=~bit

bronk(0,(1<<M)-1,0)
maxima={tuple(C) for C in maxima}
assert best==5
assert len(maxima)==72

# A separate fixed-size backtracking search certifies that a five-clique
# exists and no six-clique exists, independently of the maximal-clique census.
def exists_k_clique(P,k):
    if k==0:
        return True
    if P.bit_count()<k:
        return False
    while P:
        bit=P&-P
        v=bit.bit_length()-1
        P-=bit
        if exists_k_clique(P&adj[v],k-1):
            return True
        if P.bit_count()<k:
            return False
    return False

assert exists_k_clique((1<<M)-1,5)
assert not exists_k_clique((1<<M)-1,6)

# Independent size-five census via nested adjacency intersections.
five=set()
for a in range(M):
    P1=adj[a] & ~((1<<(a+1))-1)
    while P1:
        bb=P1&-P1; b=bb.bit_length()-1; P1-=bb
        P2=adj[a]&adj[b] & ~((1<<(b+1))-1)
        while P2:
            cc=P2&-P2; c=cc.bit_length()-1; P2-=cc
            P3=adj[a]&adj[b]&adj[c] & ~((1<<(c+1))-1)
            while P3:
                dd=P3&-P3; d=dd.bit_length()-1; P3-=dd
                P4=adj[a]&adj[b]&adj[c]&adj[d] & ~((1<<(d+1))-1)
                while P4:
                    ee=P4&-P4; e=ee.bit_length()-1; P4-=ee
                    five.add((a,b,c,d,e))
assert five==maxima

# Every optimum is equidistant at distance three.
for C in maxima:
    assert Counter(D[i][j] for i,j in itertools.combinations(C,2))==Counter({3:10})

# Forgetting rank order gives five perfect matchings of K6.
ALL_EDGES={tuple(sorted(e)) for e in itertools.combinations(range(N),2)}
def underlying_matching(w):
    return frozenset(
        tuple(sorted(i for i,x in enumerate(w) if x==rank))
        for rank in range(RANKS)
    )
for C in maxima:
    matchings=[underlying_matching(WORDS[i]) for i in C]
    assert len(set(matchings))==5
    assert set().union(*matchings)==ALL_EDGES
    assert sum(len(m) for m in matchings)==15

# Independently enumerate every labeled one-factorization of K6.
def perfect_matchings(vertices):
    vertices=tuple(vertices)
    if not vertices:
        yield frozenset()
        return
    a=vertices[0]
    for k in range(1,len(vertices)):
        b=vertices[k]
        rest=vertices[1:k]+vertices[k+1:]
        for m in perfect_matchings(rest):
            yield frozenset({tuple(sorted((a,b)))})|m

PM=sorted(set(perfect_matchings(range(N))), key=lambda m:sorted(m))
assert len(PM)==15
factorizations=set()
for comb in itertools.combinations(PM,5):
    F=frozenset(comb)
    if len(set().union(*F))==15 and sum(len(m) for m in F)==15:
        factorizations.add(F)
assert len(factorizations)==6

support_counts=Counter()
for C in maxima:
    F=frozenset(underlying_matching(WORDS[i]) for i in C)
    assert F in factorizations
    support_counts[F]+=1
assert set(support_counts.values())=={12}
assert len(support_counts)==6

# Coordinate relabeling by S6 is an isometry in the 2013 convention,
# and the 72 maxima form one orbit.
def relabel_word(w,p):
    out=[None]*N
    for old,rank in enumerate(w):
        out[p[old]]=rank
    return tuple(out)

def relabel_code(C,p):
    return tuple(sorted(INDEX[relabel_word(WORDS[i],p)] for i in C))

rep=min(maxima)
orbit={relabel_code(rep,p) for p in itertools.permutations(range(N))}
assert orbit==maxima
assert len(orbit)==72
stabilizer=720//len(orbit)
assert stabilizer==10

def fmt_word(w):
    return ''.join(str(x+1) for x in w)

rep_words=[fmt_word(WORDS[i]) for i in rep]
print("AMBIENT",len(WORDS),"PAIR_DISTANCE_HIST",dict(sorted(pair_hist.items())))
print("METRIC_CHECK representative_min_lcs_equals_representative_min_lis=true")
print("MAXIMUM",best,"LABELED_MAXIMA",len(maxima),"ALL_EQUIDISTANT_D3=true")
print("FACTORIZATIONS",len(factorizations),"OPTIMA_PER_FACTORIZATION",sorted(support_counts.values()))
print("S6_ORBITS 1 ORBIT_SIZE",len(orbit),"STABILIZER",stabilizer)
print("REPRESENTATIVE",','.join(rep_words))
print("VERIFY_OK maximum=5 labeled_maxima=72 equidistant=true factorizations=6 "
      "optima_per_factorization=12 S6_orbits=1 orbit_size=72 stabilizer=10")
