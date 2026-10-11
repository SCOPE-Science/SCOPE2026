#!/usr/bin/env python3
"""Independent finite checks for path-reversal action on strong matching complexes.

The full generators satisfy the parity and direction-string rules of
Knudson--Owens-White. No homotopy or infinite proof is inferred from a test.
"""
from itertools import product
from collections import defaultdict

ALPHABET = ('>', '<', '-')
FLIP = {'>': '<', '<': '>', '-': '-'}

def full_valid(word):
    if any(word[i:i+2] == ('<', '>') for i in range(len(word)-1)):
        return False
    i = 0
    while i < len(word):
        if word[i] != '-':
            i += 1
            continue
        j = i
        while j < len(word) and word[j] == '-':
            j += 1
        if (j-i) % 2:
            return False
        i = j
    return True

def local_valid(word):
    return all(word[i:i+2] != ('<','>') for i in range(len(word)-1)) and all(
        word[i:i+3] != ('<','-','>') for i in range(len(word)-2))

def face(word):
    return tuple(2*i + (0 if a == '>' else 1)
                 for i,a in enumerate(word) if a != '-')

def full_closure(n):
    f = {()}
    for word in product(ALPHABET, repeat=n):
        if not full_valid(word):
            continue
        b = face(word)
        for mask in range(1 << len(b)):
            f.add(tuple(x for j,x in enumerate(b) if (mask >> j) & 1))
    return f

def local_faces(n):
    return {face(w) for w in product(ALPHABET, repeat=n) if local_valid(w)}

def reflection(v,n):
    i,orient = divmod(v,2)
    return 2*(n-1-i) + (1-orient)

def sign_of_permutation(vs):
    inv = 0
    for i in range(len(vs)):
        for j in range(i+1,len(vs)):
            if vs[i] > vs[j]:
                inv += 1
    return -1 if inv%2 else 1

def direct_reduced_lefschetz(n,faces):
    answer = 0
    invariant_nonempty = 0
    for f in faces:
        im = tuple(reflection(x,n) for x in f)
        if sorted(im) != list(f):
            continue
        # Reduced degree of the empty simplex is -1.
        answer += (-1 if len(f)==0 else (-1)**(len(f)-1)) * sign_of_permutation(im)
        if f: invariant_nonempty += 1
    return answer,invariant_nonempty

def symmetric_half_trace(n):
    h = n//2
    s = 0
    for p in product(ALPHABET, repeat=h):
        if not local_valid(p) or (p and p[-1]=='<'):
            continue
        a = sum(x!='-' for x in p)
        s += (-1)**a
    return -s

def recurrence_trace(n):
    A=B=C=0;D=1
    for j in range(n//2):
        S=A+C+D
        A,B,C,D = -(A+D),-(A+B+C+D),B,S
    return -(A+C+D)

def mod2_rank(columns):
    pivots={}
    for x in columns:
        while x:
            top=x.bit_length()-1
            if top not in pivots:
                pivots[top]=x
                break
            x^=pivots[top]
    return len(pivots)

def betti_f2(faces):
    by_dimension=defaultdict(list)
    for f in faces:
        if f:
            by_dimension[len(f)-1].append(f)
    if not by_dimension:
        return {-1:1}
    ranks={}
    for k in sorted(by_dimension):
        if k == 0:
            ranks[k]=1 if by_dimension[k] else 0 # augmented degree-zero boundary
            continue
        target={f:i for i,f in enumerate(by_dimension[k-1])}
        columns=[]
        for f in by_dimension[k]:
            col=0
            for i in range(len(f)):
                col^=1 << target[f[:i]+f[i+1:]]
            columns.append(col)
        ranks[k]=mod2_rank(columns)
    return {k:len(by_dimension[k])-ranks[k]-ranks.get(k+1,0)
            for k in by_dimension}

def run():
    face_cases=0; involution_cases=0;rank_cases=0;half_cases=0
    for n in range(1,12):
        fc=full_closure(n)
        fl=local_faces(n)
        assert fc == fl, ('closure mismatch',n,len(fc),len(fl))
        face_cases+=1
        for f in fc:
            assert tuple(sorted(reflection(x,n) for x in f)) in fc, (n,f)
        lefs,ct=direct_reduced_lefschetz(n,fc)
        assert lefs==recurrence_trace(n)==symmetric_half_trace(n),(n,lefs)
        involution_cases+=1
        if n <= 10:
            b=betti_f2(fc)
            d=((n//4)*2-1) if n%4==0 else ((n//4)*2 if n%4==1 else None)
            expected={} if d is None else {d:1}
            assert {i:v for i,v in b.items() if v}==expected, (n,b,expected)
            rank_cases+=1
    for n in range(1,25):
        assert symmetric_half_trace(n)==recurrence_trace(n),n
        half_cases+=1
    for n in range(1,301):
        expected = (0 if n%4 in (2,3) else ((-1)**((n//4)+1) if n%4==0 else (-1)**(n//4+1)))
        # The two active Lefschetz classes happen to obey the same closed form.
        assert recurrence_trace(n)==expected,(n,recurrence_trace(n),expected)
    print('VERIFY_OK')
    print('FULL_GENERATOR_CLOSURE_CASES',face_cases)
    print('DIRECT_SIMPLICIAL_REFLECTION_CASES',involution_cases)
    print('DIRECT_MOD2_HOMOLOGY_CASES',rank_cases)
    print('INDEPENDENT_HALF_WORD_CASES',half_cases)
    print('RECURRENCE_PARAMETER_CASES',300)

if __name__=='__main__':run()
