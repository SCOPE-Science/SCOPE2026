"""Exact finite certificate for the square two-chain interleaving concept class.

Run `python verify.py` (Python >=3.9, standard library only).  Every
comparison assignment is evaluated on all 70 interleavings, not sampled.
"""
from functools import lru_cache
from itertools import combinations
from math import comb


def data(m,n):
    words=[]
    for subset in combinations(range(m+n),m):
        word=''.join('A' if p in subset else 'B' for p in range(m+n))
        words.append(word)
    queries={}
    for i in range(1,m+1):
        for j in range(1,n+1):
            mask=0
            for k,w in enumerate(words):
                a=[v for v,t in enumerate(w) if t=='A']
                b=[v for v,t in enumerate(w) if t=='B']
                if a[i-1]<b[j-1]:mask|=1<<k
            queries[(i,j)]=mask
    assert len(words)==comb(m+n,m)
    return words,queries


def dim(m,n):
    words,queries=data(m,n)
    full=(1<<len(words))-1
    @lru_cache(None)
    def d(mask):
        if mask.bit_count()<=1: return 0
        return max([0]+[1+min(d(mask & yes),d(mask & (full^yes)))
          for yes in queries.values() if mask & yes and mask & (full^yes)])
    return d(full),d.cache_info().currsize


def certificate():
    words,q=data(4,4)
    full=(1<<70)-1
    split=lambda state, x: (state & q[x], state & (full ^ q[x]))
    balanced=lambda state,threshold: [(x, a.bit_count(),b.bit_count())
       for x in q for a,b in [split(state,x)] if min(a.bit_count(),b.bit_count())>=threshold]
    # A depth-six tree needs two subfamilies of size at least 2**5 at the root.
    assert {x for x,_,_ in balanced(full,32)}=={(1,1),(2,2),(3,3),(4,4)}
    # Extremal first or last comparisons leave a (3,4) family;
    # no (3,4) family can support a depth-five root.
    _,r=data(3,4); all35=(1<<35)-1
    assert max(min((all35 & t).bit_count(),(all35 & (all35^t)).bit_count()) for t in r.values())==15
    # The middle-root obstruction is two rounds deeper.
    p,_=split(full,(2,2))
    assert p.bit_count()==35
    assert balanced(p,16)==[((3,2),17,18)]
    _17, s=split(p,(3,2))
    assert s.bit_count()==18
    assert balanced(s,8)==[((3,3),9,9),((4,4),9,9)]
    for x,_,_ in balanced(s,8):
        for leaf in split(s,x):
            assert leaf.bit_count()==9
            assert balanced(leaf,4)==[]
    # Reversal of both chains interchanges the first two middle-root cases.
    # An independent full minimax recurrence also checks the result.
    checks={}
    for k in range(1,5):
        checks[k]=dim(k,k)[0]
    assert checks=={1:1,2:2,3:4,4:5}
    assert dim(3,4)[0]==4
    assert dim(2,3)[0]==3
    print('FOUR_BY_FOUR_INTERLEAVING_CERTIFICATE_PASS')
    print('hypotheses=70; first_balanced_roots=4; second_split=17+18; third_split=9+9; critical_fourth_splits=0')
    print('square_depths=',checks, '; 4x4_info_bound=',70 .bit_length()-1)

if __name__=='__main__':certificate()
