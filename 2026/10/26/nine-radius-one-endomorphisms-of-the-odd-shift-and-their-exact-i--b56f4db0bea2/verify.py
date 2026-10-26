#!/usr/bin/env python3
"""Independent finite checks for a radius-one map classification on the odd-gap binary shift.
Uses only the Python standard library. Infinite claims use the proof in RESULT.md.
"""
from collections import defaultdict
from itertools import product
from math import isclose, sqrt, log

TRIPLES=(0,1,2,4,5)
REP_BY_COARSE={
    'zero':0, 'rise':2, 'identity':4, 'fall':16,
    'difference':18, 'and':32, 'right_projection':34,
    'left_projection':48, 'or':50,
}


def f(rule,a,b,c):
    return (rule >> (4*a+2*b+c)) & 1


def valid(w):
    pos=[i for i,bit in enumerate(w) if bit]
    return len({p%2 for p in pos})<=1


def image_words(rule,n):
    seen=set()
    for w in product((0,1),repeat=n+2):
        if valid(w):
            seen.add(tuple(f(rule,*w[i:i+3]) for i in range(n)))
    return seen


def coarse_valid(w,typ):
    if not valid(w): return False
    if typ=='zero':return all(a==0 for a in w)
    if typ in ('identity','right_projection','left_projection','difference'):return True
    forbidden={'rise':(1,1),'fall':(1,1),'and':(1,0,1),'or':(0,1,0)}[typ]
    for phase in (0,1):
        if any(w[i]==1 and i%2!=phase for i in range(len(w))):continue
        coarse=w[phase::2]
        if not any(coarse[i:i+len(forbidden)]==forbidden for i in range(len(coarse)-len(forbidden)+1)):
            return True
    return False


def charpoly(M):
    # Exact Faddeev-LeVerrier over integer matrices.
    n=len(M)
    B=[[int(i==j) for j in range(n)] for i in range(n)]
    c=[1]
    for k in range(1,n+1):
        N=[[sum(M[i][h]*B[h][j] for h in range(n)) for j in range(n)] for i in range(n)]
        tr=sum(N[i][i] for i in range(n))
        assert tr%k==0
        ck=-tr//k
        c.append(ck)
        B=[[N[i][j]+(ck if i==j else 0) for j in range(n)] for i in range(n)]
    return c


def main():
    # An admissible 3-word has all its ones on one parity class.
    assert tuple(j for j in range(8) if valid(tuple((j>>k)&1 for k in (2,1,0))))==TRIPLES
    groups=defaultdict(list)
    good=[]
    for r in range(256):
        t=tuple((r>>i)&1 for i in TRIPLES)
        if t[0]==0 and not (t[2] and (t[1] or t[3] or t[4])):
            good.append(r);groups[t].append(r)
    assert len(good)==72 and len(groups)==9
    assert all(len(v)==8 for v in groups.values())
    canonical={name:tuple((r>>i)&1 for i in TRIPLES) for name,r in REP_BY_COARSE.items()}
    assert len(set(canonical.values()))==9 and set(canonical.values())==set(groups)
    onto=('identity','right_projection','left_projection','difference')
    assert sum(len(groups[canonical[k]]) for k in onto)==32
    # Verify all output words, including all-zero word and both possible phases.
    counts={}
    for n in range(1,9):
        for name,rule in REP_BY_COARSE.items():
            observed=image_words(rule,n)
            expected={w for w in product((0,1),repeat=n) if coarse_valid(w,name)}
            assert observed==expected,(name,n,observed^expected)
            counts[(name,n)]=len(observed)
    # Coarse forbidden-word graphs and their integer characteristic polynomials.
    def adjacency(forbid):
        states=list(product((0,1),repeat=len(forbid)-1))
        M=[[0]*len(states) for _ in states]
        for i,w in enumerate(states):
            for b in (0,1):
                trial=w+(b,)
                if trial!=forbid:
                    M[i][states.index(trial[1:])]+=1
        return M
    # '11' prohibition: golden-mean polynomial.
    assert charpoly(adjacency((1,1)))==[1,-1,-1]
    # '101' prohibition: a zero eigenvalue times cubic polynomial.
    assert charpoly(adjacency((1,0,1)))==[1,-2,1,-1,0]
    assert charpoly(adjacency((0,1,0)))==[1,-2,1,-1,0]
    phi=(1+sqrt(5))/2
    lo,hi=1.75,1.76
    p=lambda t:t*t*t-2*t*t+t-1
    assert p(phi)<0 and p(lo)<0 and p(hi)>0
    assert log(phi)/2 < log(lo)/2 < log(2)/2
    # Distinct formal image languages are detected by finite witnesses.
    sigs={name:tuple(counts[(name,n)] for n in range(1,9)) for name in REP_BY_COARSE}
    assert len(set(sigs.values()))==4
    langs={frozenset(image_words(r,8)) for r in REP_BY_COARSE.values()}
    assert len(langs)==5
    # Rule 18 restricted to the odd shift equals Rule 90.
    assert all(f(18,*bits)==f(90,*bits) for bits in product((0,1),repeat=3) if valid(bits))
    # Direct parity-phase derivative checking on finite cyclic coarse words.
    for n in range(1,9):
        derivative={tuple(a[i]^a[(i+1)%n] for i in range(n)) for a in product((0,1),repeat=n)}
        assert all(sum(v)%2==0 for v in derivative)
        assert len(derivative)==2**(n-1)
    print('VERIFY_OK: 256 rules; 72 preserving codes/9 distinct maps; 32 surjective codes/4 maps;')
    print('five distinct image languages; four exact entropy levels;')
    print('all nine image languages checked by direct input enumeration for lengths 1..8;')
    print('exact charpoly golden mean [1,-1,-1], forbidden 101/010 [1,-2,1,-1,0];')
    print('Rule 18 = Rule 90 on the odd shift; finite derivative fibres checked n<=8.')

if __name__=='__main__':main()
