"""Independent full-complex mod-2 homology calculation without collapses.

Generates all faces by checking 19 out-neighborhood membership and reduces
full simplicial boundary matrices over the two-element field.
"""
import itertools
from collections import Counter
P=19
r={x*x%P for x in range(1,P)}
blocks=[set((u+k)%P for k in r) for u in range(P)]
F={}
for order in range(1,10):
    F[order]=sorted(sum(1<<x for x in t) for t in itertools.combinations(range(P),order)
                    if any(all(x in block for x in t) for block in blocks))
assert [len(F[k]) for k in range(1,10)]==[19,171,969,2223,2394,1596,684,171,19]
def rank_mod2(lower,higher):
    di={mask:i for i,mask in enumerate(lower)}
    pivots={}
    for s in higher:
        col=0
        for x in range(P):
            if s&(1<<x):
                col ^= 1<<di[s^(1<<x)]
        while col:
            h=col.bit_length()-1
            if h in pivots:col^=pivots[h]
            else:pivots[h]=col;break
    return len(pivots)
ranks={k:rank_mod2(F[k-1],F[k]) for k in range(2,10)}
assert ranks=={2:18,3:153,4:815,5:1330,6:1064,7:532,8:152,9:19},ranks
# H_{k-1}= dim C_{k-1}-rank boundary_{k-1}-rank boundary_k.
# For k=1, connectedness gives rank of augmented boundary 1.
betti={k-1:len(F[k])-ranks.get(k,1 if k==1 else 0)-ranks.get(k+1,0)
       for k in range(1,10)}
assert betti=={0:0,1:0,2:1,3:78,4:0,5:0,6:0,7:0,8:0},betti
print('PASS: full-complex independent GF(2) boundary ranks',ranks,'reduced Betti',betti)
