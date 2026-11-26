# Independent mathematical audit

## correctness

PASS

For descending sizes define D=Σ_{i<j}|d_i−d_j|=(k+1)N−2R. Then HTI=N/(kN−D), with positive denominator, so at fixed k,N it increases strictly with D, while HHI increases strictly with Q=Σ d_i². I ran an independent exact enumeration using multiplicities: starting at part size s=N and remainder N, take a=0,…,floor(remainder/s) copies of s and recurse at s−1 with remainder reduced by as; at s=0 keep exactly remainder-zero profiles of length at least two. This visits each admissible multiset exactly once. Bucket by length and compare every unordered pair by integer differences ΔQ,ΔD. There were 762 pairs, with counts for N=2,…,12 equal to 0,0,1,2,7,13,30,56,109,190,354. The tie-split counts were zero through 9, then 1,5,8; reversal counts were zero through 11 and one at 12. At N=10 the unique tie split has profiles (1,4,5), (2,2,6) with (Q,D)=(42,8),(44,8), giving HHI 21/50,11/25 and common HTI 5/11. At N=12 the unique strict reversal is (1,2,4,5),(2,2,2,6), with (Q,D)=(46,14),(48,12), giving HHI 23/72,1/3 and HTI 6/17,1/3. This exhausts the asserted finite domain; N<2 has no admissible profile. The frozen Python verifier, inspected but not executed, uses partition and ordered-composition generators and direct rational HTI. The multiplicity recursion and integer comparisons above give a separate replay without relying on that verifier. These are lattice cutoffs, not invariant market-size thresholds for continuous shares.

## originality

PASS

Hall–Tideman is order-equivalent to Gini on these fixed-(k,N) layers, and known partition-index results control both rankings on comparable majorization pairs. Those results do not determine the first discordant incomparable profiles. A distinct same-day HHI–entropy record uses the same N=10 witness but gives a strict HHI–entropy reversal there, not an HTI tie, and its boundary is for N−k. Credit the exact first HHI–HTI weak disagreement and first strict reversal with uniqueness, not the relationship between indices or discovery of the N=10 profiles.

## value

PASS

A tie split and a strict reversal are substantively different failures for commonly used concentration rankings. Fixing both the number of firms and total, the result gives minimal reproducible examples of each and proves the strict witness unique at the first grid size. This is useful when testing or explaining the rankings without a change in total or firm count. It is not a welfare result or a policy threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
