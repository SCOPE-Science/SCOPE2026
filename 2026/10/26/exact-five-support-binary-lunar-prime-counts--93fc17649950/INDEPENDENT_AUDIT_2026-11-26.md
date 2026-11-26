# Independent mathematical audit

## correctness

PASS

Binary lunar convolution gives S=A+B, with zero in each nonunit factor. Increasing paths in the addition grid give |S|≥|A|+|B|−1; in the equality cases, each monotone path exhausts S in order, so swapping two steps forces a_(i+1)−a_i=b_(j+1)−b_j in every cell. The only possible sizes yielding five are (2,3), (2,4), (3,3); the latter two give a progression, which also factors as {0,t}+{0,t,3t}. For (2,3) write S=B∪(B+x); exactly one collision corresponds to x equaling exactly one of the three positive pairwise differences of B. This yields the two families, and each family visibly factors. In F1, y<x gives m=2x and y choices 1,…,x−1; y>x gives m=x+y with x≤floor((m−1)/2) and y=2x excluded. Both branches are injective internally and can duplicate only at the progression: the third sorted element from the lower branch is m/2, so the upper branch must have third 2x=m/2, not y=m/2 (which would give y=x). In F2 the first two positive entries recover the unordered {x,y}; their interchange changes the maximum unless x=y, which is excluded. For intersection with F2 the third positive entry must be the sum of the first two. In F1 this gives y=3x in the upper branch or, in the lower branch, matching the maximum forces x=2y. Thus there is exactly one intersection iff 4 divides m, in addition to the internal duplicate in F1. Inclusion–exclusion gives C_m and choosing the three interior digits gives P_m and the claimed proportion. Fresh enumeration of all eligible factor shapes for 4≤m≤30 reproduced the exact family union, intersection and counts, including the m=4 endpoint.

## originality

PASS

The arithmetic and sumset reduction are established. No inspected comparison supplies the complete two-family classification, their progression overlap and the resulting exact five-one count at fixed degree; existing unrestricted prime totals and higher-level decomposability results do not determine this slice.

## value

PASS

Five positions give a natural structural case beyond the size-four product of two two-point sets: a two-by-three factorization can now lose exactly one of six candidate sums, and representations can overlap both within and across structural families. The exact classification gives membership witnesses and a sparse-weight census inaccessible from unrestricted prime density; the parity slopes and divisibility corrections are useful concrete invariants of the family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
