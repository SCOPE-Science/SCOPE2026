# Independent mathematical audit

## correctness

PASS

D_n counts boundaries between consecutive *labels* assigned to different cycles, not adjacent elements in a cycle ordering. Unique maximal runs in the label-ordered cycle partition have compositions ell_1+...+ell_r=n (r=d+1), with nonconsecutive equal-block partition of runs; number of permutations with those cycle memberships is exactly product_B(sum_{j in B}ell_j-1)!. Fix r: an individual largest cycle size m<=n/2 has exponentially small normalized weight; if m>n/2, s=n-m small, t runs of that large cycle are nonadjacent (t<=ceil(r/2)), so contribution O_r(n^(t-s-2)). The only order n^-1 configurations when r=2k+1 have one large cycle occupying alternating k+1 runs and k exceptional singleton labels, giving k! C(n-k-1,k)(n-k-1)!/n!~1/n. For r=2k+2, two alternations with k+1 singleton exceptions contribute 2(k+1)! C(n-k-2,k)(n-k-2)!/n!~(2k+2)/n²; all others lower-order. Independently enumerated every permutation n<=7 and independently summed the weighted composition formula for all eight d values at n=8, matching vector (5040,1812,6042,5539,7744,7134,5102,1907). Additional exact composition probabilities for fixed d=0..3 and n=12,20,30 corroborate the two scaled limits. Finite tests supplement asymptotic dominance proof.

## originality

PASS

Best-of-knowledge PASS for the Ewens-weighted cycle-partition boundary tail and its even/odd order change. Munagi counts unweighted set partitions with consecutive labels in same block; Mansour–Shattuck counts consecutive elements actually adjacent *within the cyclic order*, which is not the same condition. Brualdi–Deutsch count entire cycles of consecutive labels. No statement-level implication to the factorially weighted fixed-d tail appears in full relevant primary texts.

## value

PASS

Natural full-size permutation statistic D_n has an exact finite distribution formula plus a pronounced parity-dependent rare-event asymptotic with explicit coefficients. Different decay powers for neighboring fixed boundaries are nontrivial and could be used as benchmarks for Ewens-weighted partition runs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
