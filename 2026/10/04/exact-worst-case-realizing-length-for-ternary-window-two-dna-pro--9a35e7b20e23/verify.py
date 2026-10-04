#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

PATTERNS = ('LLLHHH','LLHLHH','LLHHLH','LHLLHH','LHLHLH')
BASES = ('L1','L2','L3','D0','D1','D2')
BIDX = {x:i for i,x in enumerate(BASES)}

def offseq(pat):
    li=hi=0; out=[]
    for c in pat:
        if c=='L':
            li += 1; out.append('L'+str(li))
        else:
            hi += 1; out.append('H'+str(hi))
    return out

def base_and_shift(x):
    if x.startswith('L'): return x,0
    if x.startswith('H'): return 'L'+x[1:],1
    return x,0

def shape_sequence(pat, loop_positions):
    oi=iter(offseq(pat)); di=iter(('D0','D1','D2')); P=set(loop_positions)
    return tuple(next(di) if k in P else next(oi) for k in range(9))

def least_bases(seq,t):
    # Inequality for adjacent ranked entries u<v:
    # base(v) >= base(u)+1+(shift(u)-shift(v))*t.
    edges=[]
    for u,v in zip(seq,seq[1:]):
        bu,su=base_and_shift(u); bv,sv=base_and_shift(v)
        edges.append((BIDX[bu],BIDX[bv],1+(su-sv)*t))
    d=[0]*len(BASES)
    # Longest-path closure for lower-bound difference constraints. A positive
    # cycle means infeasible. With no positive cycle this is the componentwise
    # least nonnegative solution, hence minimizes every positive linear objective.
    for it in range(len(BASES)):
        changed=False
        for u,v,w in edges:
            nv=d[u]+w
            if nv>d[v]:
                d[v]=nv; changed=True
        if not changed: break
    else:
        for u,v,w in edges:
            if d[u]+w>d[v]: return None
    # verify
    if any(d[v] < d[u]+w for u,v,w in edges): raise AssertionError('closure')
    return d

def weights_for(seq,t):
    d=least_bases(seq,t)
    if d is None: return None
    base=dict(zip(BASES,d)); w={}
    for i in (1,2,3):
        w['L'+str(i)]=base['L'+str(i)]
        w['H'+str(i)]=base['L'+str(i)]+t
    for j in (0,1,2): w['D'+str(j)]=base['D'+str(j)]
    vals=[w[x] for x in seq]
    if any(vals[i]>=vals[i+1] for i in range(8)): raise AssertionError('rank')
    total=sum(vals)
    formula=2*(base['L1']+base['L2']+base['L3'])+base['D0']+base['D1']+base['D2']+3*t
    assert total==formula
    return total,w

def exact_shape_min(seq):
    # We first search t<=28 and later verify every shape has a solution <=86.
    # For t>=29, total >=3t>=87, so such t cannot improve any <=86 witness.
    best=None
    for t in range(1,29):
        z=weights_for(seq,t)
        if z is not None and (best is None or z[0]<best[0]): best=(z[0],t,z[1])
    return best

def matrix_from_w(w):
    return [
        [w['D0'],w['H1'],w['L2']],
        [w['L1'],w['D1'],w['H3']],
        [w['H2'],w['L3'],w['D2']],
    ]

def check_matrix(M):
    vals=[M[i][j] for i in range(3) for j in range(3)]
    assert min(vals)>=0 and len(set(vals))==9
    assert [sum(r) for r in M]==[sum(M[i][j] for i in range(3)) for j in range(3)]

def euler_word(M):
    adj=[[] for _ in range(3)]
    for i in range(3):
        for j in range(3): adj[i].extend([j]*M[i][j])
    # graph has all but at most one of nine edges, hence is strongly connected
    stack=[0]; circuit=[]
    while stack:
        v=stack[-1]
        if adj[v]: stack.append(adj[v].pop())
        else: circuit.append(stack.pop())
    circuit=circuit[::-1]
    assert len(circuit)-1==sum(map(sum,M)) and circuit[0]==circuit[-1]
    C=[[0]*3 for _ in range(3)]
    for a,b in zip(circuit,circuit[1:]): C[a][b]+=1
    assert C==M
    return circuit[:-1]

records=[]
for pat in PATTERNS:
    for pos in combinations(range(9),3):
        seq=shape_sequence(pat,pos)
        b=exact_shape_min(seq)
        assert b is not None and b[0] <= 86
        records.append((b[0],pat,pos,seq,b[1],b[2]))
assert len(records)==420
D=Counter(r[0] for r in records)
mx=max(D)
worst=[r for r in records if r[0]==mx]
assert mx==86 and len(worst)==1
assert sum(D.values())==420
# 2 signs * 3! pair orders * 3! loop-label orders =72 rankings per shape.
assert 420*72==30240 and len(worst)*72==72
# Canonical extremizer and exact profile.
r=worst[0]
assert r[1]=='LHLLHH' and r[2]==(5,6,7) and r[4]==5
M=matrix_from_w(r[5]); check_matrix(M)
assert M==[[12,5,6],[0,13,15],[11,10,14]]
word=euler_word(M)
assert len(word)==86
# Direct analytic lower-bound anchors for the canonical order:
# a < a+t < b < c < b+t < D0 < D1 < D2 < c+t.
# Three integers between b+t and c+t force c-b>=4; c<b+t forces t>=5.
# Hence a>=0, b>=a+t+1>=6, c>=b+4>=10, loops>=12,13,14.
assert sum([0,5,6,10,11,12,13,14,15])==86
print('SHAPES',len(records))
print('MAX_MIN_LENGTH',mx)
print('EXTREMAL_SHAPES',len(worst))
print('EXTREMAL_RANKINGS',72)
print('CANONICAL_MATRIX',M)
print('CANONICAL_ASCENDING','p10<p01<p02<p21<p20<p00<p11<p22<p12')
print('DISTRIBUTION_SHAPES',','.join(f'{k}:{D[k]}' for k in sorted(D)))
print('EULER_LENGTH',len(word))
print('VERIFY_OK')
