import itertools, collections

def mats(a,b):
    for z in range(1<<(a*b)):
        yield [[(z>>(i*b+j))&1 for j in range(b)] for i in range(a)]

def bt(M):
    a,b=len(M),len(M[0]); rows=[tuple(r) for r in M]; cols=[tuple(M[i][j] for i in range(a)) for j in range(b)]
    return all(any(r) for r in rows) and all(any(c) for c in cols) and len(set(rows))==a and len(set(cols))==b

def canon_matrix(M):
    a,b=len(M),len(M[0]); best=None
    for rp in itertools.permutations(range(a)):
        for cp in itertools.permutations(range(b)):
            s=''.join(str(M[i][j]) for i in rp for j in cp)
            best=s if best is None or s<best else best
    return best

def facets(M, side):
    a,b=len(M),len(M[0])
    if side==0: S=[frozenset(i for i in range(a) if M[i][j]) for j in range(b)]; n=a
    else: S=[frozenset(j for j in range(b) if M[i][j]) for i in range(a)]; n=b
    F=[]
    for s in S:
        if s and not any(s<t for t in S) and s not in F: F.append(s)
    return F,n

def canon_complex(F,n):
    best=None
    for p in itertools.permutations(range(n)):
        rep=tuple(sorted(tuple(sorted(p[i] for i in f)) for f in F))
        best=rep if best is None or rep<best else best
    return best

def signature(M):
    F,n=facets(M,0); G,m=facets(M,1)
    return canon_complex(F,n),canon_complex(G,m)

def classify(a,b):
    reps={}
    for M in mats(a,b):
        if bt(M): reps.setdefault(canon_matrix(M),M)
    groups=collections.defaultdict(list)
    for c,M in reps.items(): groups[signature(M)].append(c)
    return reps,groups

for total in range(2,6):
    for a in range(1,total):
        b=total-a
        reps,groups=classify(a,b)
        assert all(len(v)==1 for v in groups.values()), (a,b,groups)
reps,groups=classify(3,3)
assert len(reps)==8
mult=sorted(len(v) for v in groups.values())
assert mult==[1,1,1,1,1,1,2],mult
collision=[v for v in groups.values() if len(v)==2][0]
assert collision==['001011111','011101111'],collision
A=reps[collision[0]]; B=reps[collision[1]]
assert signature(A)==signature(B)
assert canon_matrix(A)!=canon_matrix(B)
assert sorted(map(sum,A))==[1,2,3]
assert sorted(map(sum,B))==[2,2,3]
assert signature(A)==(((0,1,2),),((0,1,2),))
print('VERIFY_OK')
print('3x3_labeled_bi_twin_free=',sum(bt(M) for M in mats(3,3)))
print('3x3_isomorphism_classes=',len(reps))
print('dual_Dowker_signatures=',len(groups))
print('collision=',collision)
