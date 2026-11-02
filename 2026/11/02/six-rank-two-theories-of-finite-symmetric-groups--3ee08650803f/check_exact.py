"""Exact rank-two type census for symmetric groups in relational multiplication.

For each conjugacy type x, enumerate every y, collect every atomic two-point
signature and then its extension profile.  Uses only the Python standard library.
Run: python check_exact.py
"""
from itertools import permutations
from collections import defaultdict

def partitions(n, cap=None):
    if not n:
        yield ()
        return
    if cap is None:
        cap=n
    for k in range(min(n,cap),0,-1):
        for rest in partitions(n-k,k):
            yield (k,)+rest

def canonical(p):
    v=list(range(sum(p)));start=0
    for k in p:
        for j in range(k):v[start+j]=start+(j+1)%k
        start+=k
    return tuple(v)

def square(v): return tuple(v[j] for j in v)

def inverse(v):
    w=[None]*len(v)
    for i,j in enumerate(v): w[j]=i
    return tuple(w)

def atomic_signature(x,y,e,x2,y2,xi):
    # These eight comparisons generate every equality and product atom
    # R(u,v,w) over u,v,w in {e,x,y}; multiplication is a group law.
    vals=(x==e,y==e,x==y,x2==e,y2==e,x2==y,y2==x,xi==y)
    return sum((1<<i) for i,flag in enumerate(vals) if flag)

def all_profiles(n):
    e=tuple(range(n))
    universe=[(y,square(y)) for y in permutations(range(n))]
    profiles={}
    for p in partitions(n):
        x=canonical(p); x2=square(x); xi=inverse(x)
        profiles[p]=frozenset(atomic_signature(x,y,e,x2,y2,xi)
                              for y,y2 in universe)
    return profiles

def run():
    # Expected lists enumerate the exact possible first-element extension
    # profiles, expressed as bit masks of the eight primitive comparisons.
    expected={
      1:[(255,)],
      2:[(58,156),(89,255)],
      3:[(4,16,18,224),(8,24,58,156),(9,89,255)],
      4:[(0,4,16,18,48,128),(0,4,16,18,224),
         (8,24,58,72,156),(8,24,58,156),(9,89,255)],
      5:[(0,4,16,18,32,64,128),(0,4,16,18,32,128),
         (0,4,16,18,48,128),(0,4,16,18,64,224),
         (8,24,58,72,156),(8,24,58,156),(9,89,255)],
      8:[(0,4,16,18,32,64,128),(0,4,16,18,32,128),
         (0,4,16,18,48,64,128),(0,4,16,18,48,128),
         (0,4,16,18,64,224),(8,24,58,72,156),
         (8,24,58,156),(9,89,255)]
    }
    signatures={}
    for n in range(1,10):
        mp=all_profiles(n)
        sig=frozenset(mp.values())
        signatures[n]=sig
        if n in expected:
            assert sig==frozenset(map(frozenset,expected[n])), (n,sig)
        print(f'n={n} conjugacy_types={len(mp)} first_profiles={len(sig)}')
    for n in (6,7):assert signatures[n]==signatures[5]
    assert signatures[9]==signatures[8]
    assert len(set(signatures.values()))==6
    print('EXACT_PAIR_EXTENSION_PROFILE_CHECK_PASS')
    print('CLASSIFICATION: [1], [2], [3], [4], [5,6,7], [8,9]')

if __name__=='__main__': run()
