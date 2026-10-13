#!/usr/bin/env python3
import itertools, json, math
from pathlib import Path

def rotations(w):
    return [w[i:]+w[:i] for i in range(len(w))]

def min_rotation(w):
    return min(rotations(w))

def alternates(w,x,y):
    s=[z for z in w if z==x or z==y]
    return len(s)==4 and all(s[i]!=s[i+1] for i in range(3))

def represents_kmn(w,m,n):
    N=m+n
    if len(w)!=2*N:
        return False
    if any(w.count(i)!=2 for i in range(N)):
        return False
    for x in range(N):
        for y in range(x+1,N):
            target=(x<m)!=(y<m)
            if alternates(w,x,y)!=target:
                return False
    return True

def multiset_words(N):
    counts=[2]*N
    word=[]
    def rec():
        if len(word)==2*N:
            yield tuple(word)
            return
        for a in range(N):
            if counts[a]:
                counts[a]-=1
                word.append(a)
                yield from rec()
                word.pop()
                counts[a]+=1
    yield from rec()

def classified(m,n):
    N=m+n
    out=set()
    for A in itertools.permutations(range(m)):
        for B in itertools.permutations(range(m,N)):
            core=A+B+A[::-1]+B[::-1]
            out.update(rotations(core))
    return out

def square_free(w):
    L=len(w)
    for i in range(L):
        for d in range(1,(L-i)//2+1):
            if w[i:i+d]==w[i+d:i+2*d]:
                return False
    return True

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
records={}
total_examined=0

for N in range(2,6):
    all_words=list(multiset_words(N))
    total_examined+=len(all_words)
    for m in range(1,N):
        n=N-m
        brute={w for w in all_words if represents_kmn(w,m,n)}
        form=classified(m,n)
        assert brute==form
        expected=N*math.factorial(m)*math.factorial(n)
        assert len(brute)==expected
        cyclic={min_rotation(w) for w in brute}
        if N>=3:
            assert len(cyclic)==math.factorial(m)*math.factorial(n)//2
            assert all(square_free(w) for w in brute)
        else:
            assert len(cyclic)==1
            assert not any(square_free(w) for w in brute)
        records[f"{m},{n}"]={
            "linear":len(brute),
            "cyclic":len(cyclic),
            "square_free":all(square_free(w) for w in brute)
        }

assert records==cert["finite_replay"]["counts"]
print(
    "VERIFY_OK total<=5 exhaustive_multiset_words=%d "
    "pairs=10 classification_engine=ABArBr exhaustive_engine=all_double_occurrence "
    "counts_match=1 cyclic_counts_match=1 squarefree_checks=1" % total_examined
)
