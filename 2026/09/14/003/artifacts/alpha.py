import numpy as np, itertools
C=np.zeros((8,8),dtype=int)
covers_list=[[1,3,4,6,7],[1,2,4,6,7],[1,2,4,5,7],[0,2,4,5,7],[0,2,3,5,7],[0,2,3,5,6],[0,1,3,5,6],[0,1,3,4,6]]
for i,c in enumerate(covers_list):
    for v in c: C[i,v]=1
# alpha(I^(m)) = min sum a with Ca>=m, via enumeration degree by degree
# brute force over compositions: for m=1..6 search increasing degree d
from itertools import combinations_with_replacement
def alpha_sym(m, dmax=20):
    # search all vectors of sum d? Use recursion generating compositions of d into 8 parts
    for d in range(0, dmax+1):
        # generate weak compositions via stars and bars recursion
        found=False
        # iterate via integer partitions using odometer over first 7 coords
        # for d up to ~12 and 8 vars, C(d+7,7) manageable for small d
        # use recursion
        def rec(i, rem, cur):
            nonlocal found
            if found: return True
            if i==7:
                cur.append(rem)
                a=np.array(cur)
                if np.all(C@a>=m):
                    found=True
                    print(f"m={m}: alpha<={d} e.g. {a.tolist()}")
                    cur.pop(); return True
                cur.pop(); return False
            for t in range(rem+1):
                cur.append(t)
                if rec(i+1, rem-t, cur): return True
                cur.pop()
            return False
        if rec(0,d,[]):
            return d
    return None
for m in [1,2,3,4,5]:
    print("m=",m,"alpha=",alpha_sym(m))
