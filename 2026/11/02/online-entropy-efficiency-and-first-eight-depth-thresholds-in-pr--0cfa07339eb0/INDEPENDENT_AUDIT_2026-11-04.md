# Independent mathematical audit

## correctness

PASS

Reconstructed first-zero equivalence and prefix rule: after first zero position i only k ones may remain. Disjoint slices have (n-i choose <=k) concepts. On a depth-d shattered membership tree, a realized path from slice i is injectively coded by the at most k path depths where a queried coordinate >i returns one; queries <i forced 1 and =i forced 0. Distinctness follows by replaying the deterministic query tree, with no query repeated along a shattered path. Thus 2^d <=1+sum_{j<=k}(n-j)C(d,j); binary search on the n+1 prefix concepts gives floor(log2(n+1)). |P(k,n)|=sum_{j=0}^{k+1}C(n,j), yielding the fixed-k limit. The Boolean first-query recurrence is exhaustive on finite version spaces and nested in n; the source checker evaluates 12 threshold-adjacent cases and depth-nine exclusion at 69. Independently reconstructed version spaces through n=12 AND separately replayed the full 12 threshold-adjacent decisions through n=69 and exclusion of depth nine at n=69; all exact tests passed. No all-(k,n) exact formula asserted.

## originality

PASS

Online Littlestone dimension is distinct from poset local dimension denoted ldim in the original convex-geometry paper; earlier Sauer-maximum size/VC facts are background. A first-zero sparse-tail slice bound gives a new comparison of online depth versus static entropy and a finite exact depth spectrum, beyond the inspected statements of Knauer–Trotter; complete priority is not guaranteed.

## value

PASS

First quantitative separation of an explicitly Sauer-maximum convex-geometry class from its online membership-query tree depth, with fixed-k entropy ratio 1/(k+1); exact n<=69 k=1 thresholds supply meaningful initial structural data where the general fence is not asserted sharp. This is a natural online invariant rather than an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
