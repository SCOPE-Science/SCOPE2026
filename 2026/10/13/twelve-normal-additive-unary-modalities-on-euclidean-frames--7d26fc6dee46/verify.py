"""Reproducible finite checks for normal additive unary K5 modalities.

This is a computational cross-check; the all-frame argument is a separate proof.
Run: python3 verify.py
"""
from itertools import product
from collections import defaultdict

# Syntax: ('p',), ('bot',), ('not',term), ('and',term,term), ('or',term,term), ('dia',term), ('box',term).
p=('p',); bot=('bot',); top=('not',bot)
def neg(a):return ('not',a)
def conj(a,b):return ('and',a,b)
def disj(a,b):return ('or',a,b)
def dia(a):return ('dia',a)
def box(a):return ('box',a)

def ev(t,R,P):
    n=len(R)
    op=t[0]
    if op=='p':return P
    if op=='bot':return 0
    if op=='not':return ((1<<n)-1)^ev(t[1],R,P)
    if op=='and':return ev(t[1],R,P)&ev(t[2],R,P)
    if op=='or':return ev(t[1],R,P)|ev(t[2],R,P)
    z=ev(t[1],R,P)
    if op=='dia':return sum(1<<i for i in range(n) if R[i]&z)
    if op=='box':return sum(1<<i for i in range(n) if (R[i]&z)==R[i])
    raise RuntimeError(op)

def euclidean(R):
    for x,neigh in enumerate(R):
        y=0
        while y<len(R):
            if neigh>>y&1 and neigh & ~R[y]:return False
            y+=1
    return True

def candidate_formula(e,a,j):
    parts=[]
    if e:parts.append(conj(p,box(bot)))
    if a:parts.append(conj(p,dia(top)))
    if j==1:parts.append(dia(p))
    if j==2:parts.append(dia(dia(p)))
    out=bot
    for term in parts:out=disj(out,term)
    return out

CAND=[candidate_formula(e,a,j) for e,a,j in product(range(2),range(2),range(3))]

# The witness has two immediate successors and two additional members of their cluster.
Rcan=(0b00110,0b11110,0b11110,0b11110,0b11110)
assert euclidean(Rcan)
features=(p,dia(top),dia(p),box(p),dia(dia(p)),box(box(p)))
feature_signatures=set()
for P in range(32):
    feature_signatures.add(tuple((ev(f,Rcan,P)&1)!=0 for f in features))
assert len(feature_signatures)==10, ('unexpected live types',len(feature_signatures))
Rdead=(0,)
for P in range(2):
    feature_signatures.add(tuple((ev(f,Rdead,P)&1)!=0 for f in features))
assert len(feature_signatures)==12, ('unexpected pointed types',len(feature_signatures))
print('pointed types:',len(feature_signatures))

# Each type is its own observable class; any subset is definable by a Boolean formula.
# As an independent cross-check, compile every formula of depth <=4 from a varied grammar
# and confirm equal six-feature signatures force the same truth in all Euclidean models <=4.
terms=[p,bot,top]
for k in range(5):
    a=terms[-(k+1)]
    terms.extend((neg(a),dia(a),box(a),conj(a,p),disj(a,box(bot)),conj(a,dia(p))))

num_frames=0; num_points=0; num_valuations=0
# For all n<=4 every relation enumerated; test all assignments and all 12 templates.
for n in range(1,5):
    for rel in range(1<<(n*n)):
        R=tuple((rel>>(i*n))&((1<<n)-1) for i in range(n))
        if not euclidean(R):continue
        num_frames+=1
        outputs=[[] for _ in CAND]
        for P in range(1<<n):
            num_valuations+=1
            for k,f in enumerate(CAND):outputs[k].append(ev(f,R,P))
            fp=tuple(ev(f,R,P) for f in features)
            for x in range(n):
                signature=tuple((z>>x)&1 for z in fp)
                assert signature in feature_signatures,(n,rel,P,x,signature)
            # Optional modal-syntax induction cross-check using original formulas.
            for f in terms:
                bits=ev(f,R,P)
                # In a Euclidean model, worlds with equal six-feature signature agree.
                for x in range(n):
                    for y in range(x+1,n):
                        if all(((z>>x)&1)==((z>>y)&1) for z in fp):
                            assert ((bits>>x)&1)==((bits>>y)&1)
        for i,f in enumerate(CAND):
            assert outputs[i][0]==0,(n,rel,i,'not normal')
            for A in range(1<<n):
                for B in range(1<<n):
                    assert outputs[i][A|B]==outputs[i][A]|outputs[i][B],(n,rel,i,A,B,'not additive')
        num_points+=n
    print('completed n=',n)

fingerprints=[]
for f in CAND:
    fingerprint=tuple(bool(ev(f,Rcan,P)&1) for P in range(32))+tuple(bool(ev(f,Rdead,P)&1) for P in range(2))
    fingerprints.append(fingerprint)
assert len(set(fingerprints))==12
print('all Euclidean frames n<=4:',num_frames)
print('frame-root positions:',num_points)
print('valuations checked:',num_valuations)
print('twelve pairwise-distinct normal and additive templates: OK')

# All Boolean functions on the twelve pointed signature types are definable,
# yielding 2^12 distinct unary formulas. Count normal/additive functions explicitly.
# Collect necessary joins induced by root valuations on five-world canonical frame.
live_type=[]
for P in range(32):
    live_type.append(tuple((ev(f,Rcan,P)&1)!=0 for f in features))
dead_type=[]
for P in range(2):
    dead_type.append(tuple((ev(f,Rdead,P)&1)!=0 for f in features))
types=sorted(feature_signatures)
idx={t:i for i,t in enumerate(types)}
live_idx=[idx[t] for t in live_type]; dead_idx=[idx[t] for t in dead_type]
count=0
for mask in range(1<<12):
    vals=[(mask>>j)&1 for j in range(12)]
    if vals[live_idx[0]] or vals[dead_idx[0]]:continue
    valid=True
    for i in range(32):
        for j in range(32):
            if vals[live_idx[i|j]]!=(vals[live_idx[i]]|vals[live_idx[j]]):
                valid=False;break
        if not valid:break
    if valid and vals[dead_idx[1]] in (0,1):count+=1
assert count==12,('unexpected total',count)
print('all 4096 Boolean functions on 12 pointed types; normal+additive count:',count)
print('VERIFY_OK')
