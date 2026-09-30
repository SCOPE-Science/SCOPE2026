#!/usr/bin/env python3
import itertools, json
from fractions import Fraction

V=tuple(range(6))
TRIPLES=list(itertools.combinations(V,3))
TINDEX={t:i for i,t in enumerate(TRIPLES)}
GEDGES=list(itertools.combinations(range(5),2))

def matmul(A,B):
    n=len(A); m=len(B[0]); q=len(B)
    return [[sum(A[i][k]*B[k][j] for k in range(q)) for j in range(m)] for i in range(n)]

def charpoly(mask):
    A=[[0]*5 for _ in range(5)]
    for b,(i,j) in enumerate(GEDGES):
        if mask>>b&1: A[i][j]=A[j][i]=1
    I=[[int(i==j) for j in range(5)] for i in range(5)]
    B=[row[:] for row in I]
    coeff=[1]
    for k in range(1,6):
        AB=matmul(A,B)
        tr=sum(AB[i][i] for i in range(5))
        c=Fraction(-tr,k)
        assert c.denominator==1
        c=int(c)
        coeff.append(c)
        B=[[AB[i][j]+c*I[i][j] for j in range(5)] for i in range(5)]
    # descending: x^5+c1*x^4+...+c5
    return coeff

def shift_by_two(desc):
    # Return ascending coefficients q(y)=p(y+2).
    n=len(desc)-1
    out=[0]*(n+1)
    import math
    for idx,c in enumerate(desc):
        power=n-idx
        for j in range(power+1):
            out[j]+=c*math.comb(power,j)*(2**(power-j))
    return out

def sign_changes(seq):
    s=[1 if x>0 else -1 for x in seq if x!=0]
    return sum(a!=b for a,b in zip(s,s[1:]))

def graph_relation(mask):
    q=shift_by_two(charpoly(mask))
    mult0=0
    while mult0<len(q) and q[mult0]==0: mult0+=1
    rem=q[mult0:]
    # A is real symmetric, hence p and q are real-rooted. For a real-rooted
    # polynomial, Descartes' sign variation equals the number of positive roots
    # counted with multiplicity (multiply linear factors one at a time).
    pos=sign_changes(rem)
    if pos>0: return 1
    if mult0>0: return 0
    return -1
REL=[graph_relation(m) for m in range(1<<10)]

COMP_PAIRS=[]
for i,t in enumerate(TRIPLES):
    c=tuple(sorted(set(V)-set(t)))
    j=TINDEX[c]
    if i<j: COMP_PAIRS.append((i,j))

LOCAL={}
for ei,t in enumerate(TRIPLES):
    for v in t:
        others=[x for x in V if x!=v]
        pos={x:i for i,x in enumerate(others)}
        a,b=[x for x in t if x!=v]
        e=tuple(sorted((pos[a],pos[b])))
        LOCAL[(ei,v)]=1<<GEDGES.index(e)

def family_link_masks(E):
    lm=[0]*6
    for ei in E:
        for v in TRIPLES[ei]: lm[v]|=LOCAL[(ei,v)]
    return lm

def canon(E):
    emasks=[sum(1<<x for x in TRIPLES[i]) for i in E]
    best=None
    for p in itertools.permutations(V):
        trans=[]
        for m in emasks:
            nm=0
            for i in V:
                if m>>i&1: nm|=1<<p[i]
            trans.append(nm)
        key=tuple(sorted(trans))
        if best is None or key<best: best=key
    return best

valid=0; equality=[]; worst=-2
for hmask in range(1<<20):
    if any((hmask>>a&1) and (hmask>>b&1) for a,b in COMP_PAIRS):
        continue
    valid+=1
    E=[i for i in range(20) if hmask>>i&1]
    s=min(REL[m] for m in family_link_masks(E))
    worst=max(worst,s)
    if s==0: equality.append(tuple(E))
classes={}
for E in equality:
    classes.setdefault(canon(E),0)
    classes[canon(E)]+=1
summary={
    'enumeration':'all 2^20 triple systems filtered by complementary disjoint pairs',
    'intersecting_families_checked':valid,
    'max_sigma_value':2,
    'no_family_has_sigma_gt_2':worst<=0,
    'equality_labeled_count':len(equality),
    'equality_isomorphism_types':len(classes),
    'orbit_sizes':sorted(classes.values()),
}
assert valid==59049
assert worst==0
assert len(equality)==78
assert len(classes)==5
assert sorted(classes.values())==[6,12,20,20,20]
print(json.dumps(summary,sort_keys=True,separators=(',',':')))
