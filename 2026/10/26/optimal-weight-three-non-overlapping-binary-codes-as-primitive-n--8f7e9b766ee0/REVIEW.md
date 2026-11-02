# Independent mathematical audit

## correctness

PASS

Any non-overlapping codeword must be primitive and two codewords cannot occupy the same cyclic rotation orbit, giving |C|<=floor(binomial(n,3)/n)=floor((n-1)(n-2)/6). The construction chooses words with ones at (i,j,n-1), i>=h-1, j>=n-h, h=ceil(n/3), i<j<n-1. Every proper matching prefix must end at one of the internal 1 positions: at i+1 it would require i_u+j_v<=n-2, contradicted by i_u+j_v>=n-1; at j+1 the suffix contains all three ones but the prefix only two. The j-sum gives (h-1)(2n-3h)/2, equal to the floor bound in all three residues n mod 3. If 3|n exactly n/3 words have period n/3; otherwise every weight-three word is primitive. Rotation packing therefore covers all primitive necklaces. Independent brute overlap, word count and rotation-union checks for every n=4..18 confirm finite cases.

## originality

PASS

Best-of-knowledge PASS for the all-n fixed-weight-three optimum and primitive-necklace transversal; the cyclic-orbit upper bound is classical, not novel. Chee et al. (arXiv:1209.0236) give long-zero-run constructions and near-optimal cardinalities for unrestricted compositions; Blackburn (arXiv:1303.1026) gives general q,n constructions and short-n exact values; Stanovnik–Moškon–Mraz (2024) optimize unrestricted codes. None of their inspected relevant theorems imposes exactly three ones for every n or proves a full primitive-weight-three necklace transversal. Some isolated n values follow from unrestricted tables; an unindexed specialized construction remains possible.

## value

PASS

Fixing weight exactly three is a natural low-energy/constant-composition synchronization constraint independent of unconstrained non-overlap optimization. The all-blocklength optimum saturates the cyclic bound and the construction supplies one codeword per primitive necklace, including the nonprimitive n divisible by 3 boundary. This is a genuine infinite classification with an explicit constructive code, not a routine consequence of known upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
