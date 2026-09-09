import sys, math, json, itertools
from functools import lru_cache
from fractions import Fraction

N=15

def partitions(n, max_part=None):
    if n==0:
        yield ()
        return
    if max_part is None: max_part=n
    for first in range(min(max_part,n),0,-1):
        for rest in partitions(n-first, first):
            yield (first,)+rest

PARTS = list(partitions(N))
PARTS.sort(reverse=True)  # lex descending
print(f"p({N})={len(PARTS)}", flush=True)
pindex={p:i for i,p in enumerate(PARTS)}

# class sizes: z_mu
from math import factorial
def class_size(mu):
    from collections import Counter
    c=Counter(mu)
    z=1
    for part,m in c.items():
        z*= (part**m)*math.factorial(m)
    return math.factorial(N)//z

CS=[class_size(mu) for mu in PARTS]
assert sum(CS)==math.factorial(N) or True
# sum of class sizes = n!
assert sum(CS)==math.factorial(15), sum(CS)

# ---- Murnaghan-Nakayama ----
# Represent diagram lambda as tuple. Need rim hooks of size k.
# Approach: cell set; rim hook = connected border strip of size k removable leaving valid diagram.
# Standard algorithm: iterate over cells as start, walk rim.
# Simpler: enumerate all subsets? Better: recursive border walk.
# Use classic method: for each row s where we can start removing, try stripping rim hook.
# Alternative well-known recursion via beta-sets? Let's do direct diagram manipulation.

def diagram_cells(lam):
    s=set()
    for i,r in enumerate(lam):
        for j in range(r):
            s.add((i,j))
    return s

def is_partition(lam):
    for i in range(len(lam)-1):
        if lam[i]<lam[i+1]: return False
    return all(x>0 for x in lam)

def rim_hooks(lam, k):
    """Yield (new_lam, height) for each rim hook of size k removable from lam."""
    # Use algorithm: consider the border; a rim hook is determined by start cell (r1,c1) on rim
    # and end cell (r2,c2), strip the border between them.
    # Brute force approach: try all connected subsets of border of size k that are rim hooks.
    # n=15 small; brute force over subsets is too big. Use edge-walk method.
    if sum(lam)<k: return
    if k==0:
        yield (lam,0); return
    cells=diagram_cells(lam)
    # rim cells: those with no cell to right AND below? Actually border strip cells: cell with (i+1,j+1) not in diagram? Let's just compute rim = cells where right neighbor or below neighbor missing... standard rim = cells (i,j) with (i+1,j+1) not in cells? Hmm.
    # Instead use standard recursive MN via "remove border strip containing last cell of first row"? No, must enumerate all.
    # Robust method: A rim hook H of size k with lam\H a diagram iff there exist rows a<=b such that:
    #   we remove alpha_i cells from end of row i for i in a..b, sum alpha_i=k, alpha_i>=1 for a..b,
    #   and lam[i]-alpha_i >= lam[i+1] (for i<b, with lam[i+1] full) and lam[b]-alpha_b >= (lam[b+1] if b+1<len else 0),
    #   and also lam[a-1] > lam[a]-... hmm need connectivity: alpha_{i+1} <= ... plus rim condition: lam[i]-alpha_i <= lam[i+... ]?
    # Let's recall characterization: removing a rim hook from rows a..b means new diagram mu with mu_i=lam_i for i outside [a,b], mu_i = lam_{i+1}... no.
    # Alternative: use beta-set / abacus formulation which is clean and easy to implement correctly.
    # Beta-set: beta_i = lam_i + (r-1-i) for i in 0..r-1, plus extra zeros. Rim hook of size k with height h corresponds to decreasing one beta by k such that result is still distinct nonnegative and height = number of skipped betas.
    # Implement that.
    r=len(lam)
    # use r beta numbers; but hooks that reduce length need care: allow beta to go negative -> row disappears.
    # Standard: take beta with enough trailing zeros: use length r (or r+1?). To allow removal that drops rows, use extended beta of length r+? Actually decreasing a beta may give value already present (invalid) or negative (row removed).
    # Use extended set with extra 0..? Let's use length L = r + k (add k empty rows' beta = L-1-i... ). Simpler: pad lam with zeros to length r+k? Hmm padding changes beta values.
    # Correct approach: choose L = len(lam)+k maybe. Pad lam with zeros to length L: lam_ext[i]=lam[i] if i<r else 0. beta_i = lam_ext[i]+L-1-i.
    L = r + 1  # adding one extra zero row suffices for single hook removal? For height counting need full range. Actually one extra zero suffices since single hook removal drops at most... but k can remove multiple trailing rows? Removing rim hook leaves valid diagram; number of rows can drop by at most... e.g. lam=(1), k=1, r=1, L=2: lam_ext=(1,0), beta=(2,0). Decrease beta_0 by 1 -> (1,0) still beta valid -> mu lam? (1,0)-> rows (1-? ) Let's test.
    # Use L=r+1.
    L=r+1
    lamext=list(lam)+[0]
    beta=[lamext[i]+L-1-i for i in range(L)]
    s=set(beta)
    for i in range(L):
        b=beta[i]
        nb=b-k
        if nb<0: continue
        if nb in s: continue
        # height = number of beta_j in (nb,b) i.e. strictly between
        h=sum(1 for x in beta if nb<x<b)
        # build new beta set, sort desc, convert back to partition
        newbeta=sorted([nb if j==i else beta[j] for j in range(L)], reverse=True)
        newlam=[]
        for j in range(L):
            v=newbeta[j]-(L-1-j)
            newlam.append(v)
        # strip trailing zeros and check nonincreasing (automatic) and nonnegative
        while newlam and newlam[-1]==0: newlam.pop()
        if any(v<0 for v in newlam): continue
        # must be nonincreasing: beta sorted ensures it
        yield (tuple(newlam), h)

# quick self-test of rim hook enumeration: number of rim hooks sizes and MN spot checks at small n
def chi(lam, mu):
    """MN character value chi^lam(mu), mu a partition tuple."""
    # use cache on (lam, mu)
    return _chi(lam, mu)

from functools import lru_cache
@lru_cache(maxsize=None)
def _chi(lam, mu):
    if not mu:
        return 1 if (not lam or sum(lam)==0) else 0
    if not lam or sum(lam)==0:
        return 0
    if sum(lam)!=sum(mu):
        return 0
    k=mu[0]; rest=mu[1:]
    tot=0
    for (nl,h) in rim_hooks(lam,k):
        tot+= ((-1)**h)*_chi(nl, rest)
    return tot

# test at small n
if __name__=="__main__":
    # hook dimension check
    assert _chi((3,2,1),(1,)*6)==16, _chi((3,2,1),(1,)*6)  # dim of (3,2,1) is 16
    assert _chi((5,4,3,2,1),(1,)*15)==292864, _chi((5,4,3,2,1),(1,)*15)  # hook formula? verify below
    print("spot checks pass")
