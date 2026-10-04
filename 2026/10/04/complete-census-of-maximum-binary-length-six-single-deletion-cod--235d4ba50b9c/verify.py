#!/usr/bin/env python3
import itertools, json, os

def descendants(w):
    return {w[:i]+w[i+1:] for i in range(len(w))}

def complement(w):
    return ''.join('1' if c=='0' else '0' for c in w)

def transform(code, reverse, comp):
    out=[]
    for w in code:
        if reverse:
            w=w[::-1]
        if comp:
            w=complement(w)
        out.append(w)
    return tuple(sorted(out))

root=os.path.dirname(os.path.abspath(__file__))
expected=json.load(open(os.path.join(root,'maxima.json'),encoding='utf-8'))
words=[''.join(p) for p in itertools.product('01', repeat=6)]
N=len(words)
adj=[0]*N
for i,a in enumerate(words):
    da=descendants(a)
    for j in range(i+1,N):
        if da.isdisjoint(descendants(words[j])):
            adj[i]|=1<<j
            adj[j]|=1<<i

maximal_count=0
maximum=0
maxima=[]
def bron(R,P,X):
    global maximal_count, maximum, maxima
    if not P and not X:
        maximal_count += 1
        size=R.bit_count()
        if size>maximum:
            maximum=size; maxima=[R]
        elif size==maximum:
            maxima.append(R)
        return
    U=P|X
    if U:
        best_u=None; best=-1; T=U
        while T:
            bit=T & -T; u=bit.bit_length()-1
            score=(adj[u]&P).bit_count()
            if score>best:
                best=score; best_u=u
            T-=bit
        cand=P & ~adj[best_u]
    else:
        cand=P
    while cand:
        bit=cand & -cand; v=bit.bit_length()-1
        bron(R|bit, P&adj[v], X&adj[v])
        P &= ~bit
        X |= bit
        cand &= ~bit
bron(0,(1<<N)-1,0)

codes=sorted(tuple(words[i] for i in range(N) if (m>>i)&1) for m in maxima)
expected_codes=sorted(tuple(x['codewords']) for x in expected['maxima'])
assert maximum==10
assert maximal_count==62707
assert len(codes)==9
assert codes==expected_codes

core=sorted(set.intersection(*(set(c) for c in codes)))
assert core==expected['universal_core']==['000000','001100','110011','111111']
cover=[]
for c in codes:
    balls=[descendants(w) for w in c]
    for i in range(len(balls)):
        for j in range(i+1,len(balls)):
            assert balls[i].isdisjoint(balls[j])
    cover.append(len(set().union(*balls)))
assert sorted(cover)==[26,28,28,28,30,30,30,30,32]
assert {k:cover.count(int(k)) for k in expected['coverage_histogram']}==expected['coverage_histogram']

vt0=tuple(sorted(w for w in words if sum((i+1)*int(w[i]) for i in range(6))%7==0))
assert vt0 in codes
assert cover[codes.index(vt0)]==32
assert sum(v==32 for v in cover)==1

idx={c:i for i,c in enumerate(codes)}
seen=set(); orbit_sizes=[]
for i,c in enumerate(codes):
    if i in seen: continue
    orb={idx[transform(c,r,k)] for r in (False,True) for k in (False,True)}
    seen.update(orb); orbit_sizes.append(len(orb))
assert sorted(orbit_sizes)==[1,1,1,2,2,2]
assert seen==set(range(9))
print('VERIFY_OK vertices=64 maximal_cliques=62707 maximum=10 labeled_maxima=9 core=4 perfect=1 coverage=26x1,28x3,30x4,32x1 orbits=1x3,2x3 group_size=4')
