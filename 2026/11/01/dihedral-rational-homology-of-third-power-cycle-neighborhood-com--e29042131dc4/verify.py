#!/usr/bin/env python3
"""Exact independent checks for a cyclic neighborhood-complex symmetry theorem.
Requires Python 3 and SymPy. All arithmetic is exact; no external resources.
"""
from itertools import combinations
from collections import defaultdict
from sympy import symbols, Matrix, zeros, factor, expand

t=symbols('t')
# (free face, unique maximal coface), with all vertex offsets read modulo n.
PAIRS=[
 ((0,1,2,4,5),(0,1,2,4,5,6)),
 ((0,1,2,4),(0,1,2,4,6)),
 ((0,1,2,5),(0,1,2,5,6)),
 ((0,1,3,4),(0,1,3,4,5)),
 ((0,1,2,-3),(0,1,2,-4,-3)),
 ((0,1,2,-4),(0,1,2,-4,-2)),
 ((0,1,3),(0,1,3,5)),
 ((0,2,-3),(0,2,-4,-3)),
 ((0,1,4),(0,1,4,5)),
 ((0,2,-4),(0,2,-4,-2)),
]

def faces(n):
    out=set()
    for c in range(n):
        ns=sorted((c+j)%n for j in (-3,-2,-1,1,2,3))
        for k in range(1,7):
            out.update(combinations(ns,k))
    return out

def trans(s,i,n): return tuple(sorted((v+i)%n for v in s))

def norm(s,n):
    # A simplex has a unique lift to a cyclic interval of length <= 6 for n>=13.
    a={tuple(sorted((x-v)%n for x in s)) for v in s}
    a={x for x in a if x[-1]<=6}
    assert len(a)==1, (n,s,a)
    return next(iter(a))

def collapse(n):
    active=faces(n)
    face_count=[sum(len(s)==k for s in active) for k in range(1,7)]
    assert face_count==[n,6*n,14*n,14*n,6*n,n], (n,face_count)
    for a,b in PAIRS:
        A=[trans(a,i,n) for i in range(n)]
        B=[trans(b,i,n) for i in range(n)]
        assert len(set(A))==len(set(B))==n
        assert set(A).isdisjoint(set(B)) and set(A)|set(B)<=active
        # Check all active strict cofaces: precisely the one prescribed facet.
        coface_index=defaultdict(list)
        for s in active:
            for k in range(1,len(s)):
                for u in combinations(s,k):
                    coface_index[u].append(s)
        for x,y in zip(A,B):
            assert coface_index[x]==[y], (n,a,b,x,coface_index[x])
        active-=set(A)|set(B)
    c=[sum(len(s)==k for s in active) for k in range(1,7)]
    assert c==[n,6*n,10*n,5*n,0,0],(n,c)
    groups=defaultdict(set)
    for s in active:groups[len(s)-1].add(norm(s,n))
    reps=[sorted(groups[k]) for k in range(4)]
    assert [len(v) for v in reps]==[1,6,10,5]
    return reps

def matrices(reps):
    D=[]
    for degree in range(1,4):
        rows={s:i for i,s in enumerate(reps[degree-1])}
        M=zeros(len(reps[degree-1]),len(reps[degree]))
        for col,s in enumerate(reps[degree]):
            for j in range(len(s)):
                f=s[:j]+s[j+1:]
                shift=min(f)
                u=tuple(x-shift for x in f)
                M[rows[u],col]+=(-1)**j*t**shift
        D.append(M)
    assert (D[0]*D[1]).applyfunc(expand)==zeros(1,10)
    assert (D[1]*D[2]).applyfunc(expand)==zeros(6,5)
    return D

def original_reps(n):
    groups=defaultdict(set)
    for s in faces(n):groups[len(s)-1].add(norm(s,n))
    return [sorted(groups[k]) for k in range(6)]

def reflection_traces(reps,nparity,jparity):
    # For a symmetric integer template S with min S=0 and max S=m,
    # s_j fixes translation i+S iff 2i=j-m mod n.
    # That congruence has one solution when n is odd, and either two
    # or zero when n is even, according to parity.
    counts=[]
    for d,ss in enumerate(reps):
        total=0
        for s in ss:
            m=s[-1]
            if tuple(m-v for v in s[::-1])!=s:continue
            c=1 if nparity=='odd' else (2 if jparity==m%2 else 0)
            total+=c*((-1)**((d+1)*d//2))
        counts.append(total)
    return counts

def main():
    for n in range(13,26):
        reps=collapse(n)
        if n==13: ref=reps
        else: assert reps==ref,(n,reps,ref)
    assert ref==[
       [(0,)],
       [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)],
       [(0,1,2),(0,1,5),(0,1,6),(0,2,3),(0,2,4),(0,2,5),(0,2,6),(0,3,4),(0,4,5),(0,5,6)],
       [(0,1,2,6),(0,1,5,6),(0,2,3,4),(0,2,4,5),(0,2,5,6)]
    ]
    D1,D2,D3=matrices(ref)
    # Unit 5x5 minor of d2 and d1 ideal (t-1).
    assert factor(D2.extract((1,2,3,4,5),(0,1,2,3,4)).det())==-1
    assert factor(D1[0,0])==t-1
    assert all(factor(z/(t-1)).is_polynomial(t) for z in D1)
    # Unit 4x4 minor, rank drop at -1, and a 5x5 determinant
    # exactly -(t+1) completely determine Smith invariant factors of d3.
    assert factor(D3.extract((0,1,3,5),(0,1,2,3)).det())==-1
    assert D3.subs(t,-1).rank()==4
    assert factor(D3.extract((0,3,5,8,9),tuple(range(5))).det())==-(t+1)
    # Finite symbolic certificate: d2 has five unit invariant factors,
    # d3 has four unit factors and the factor (t+1).
    orig=original_reps(13)
    assert [len(v) for v in orig]==[1,6,14,14,6,1]
    odd=reflection_traces(orig,'odd',0)
    even0=reflection_traces(orig,'even',0)
    even1=reflection_traces(orig,'even',1)
    assert odd==[1,-6,-2,4,0,-1]
    assert even0==[2,-6,-4,6,0,-2]
    assert even1==[0,-6,0,2,0,0]
    assert [sum((-1)**j*z for j,z in enumerate(tr)) for tr in (odd,even0,even1)]==[2,0,4]
    print('COLLAPSE_ALL_N_13_TO_25_OK; LOCALITY_CERTIFIES_N_GE_26')
    print('CORE_ORBITS', [len(v) for v in ref])
    print('SMITH_D1:t-1; D2:1,1,1,1,1,0; D3:1,1,1,1,t+1')
    print('REFLECTION_FIXED_CHAIN_TRACES',odd,even0,even1)
    print('DIHEDRAL_HOMOLOGY_CHARACTER_VERIFY_OK')

if __name__=='__main__':main()
