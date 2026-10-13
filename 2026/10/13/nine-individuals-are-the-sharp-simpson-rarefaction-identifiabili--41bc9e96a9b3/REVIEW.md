# Self-review

## Correctness
**PASS.** The two-draw identity follows directly because rarefied richness is one on a collision and two otherwise. For three draws, the pointwise identity \(S_3=3-C+I\) gives \(R_3=3-3D_2+T_3\). The finite cutoff is exhaustive: strict positivity bounds richness by \(S\le N\), and every positive abundance multiset through \(N=9\) is generated twice by independent exact enumerators. No fixed-\((N,S)\) Simpson collision exists through \(N=8\), and the unique \(N=9\) collision is \((1,4,4)\) versus \((2,2,5)\). The packaged verifier returns `VERIFY_OK`.

Risk: none within the stated finite domain; changing the domain by allowing varying richness or noninteger weights changes the boundary question.

## Originality
**PASS.** Simpson and Hurlbert own the underlying concentration and rarefaction quantities. Hurlbert also explicitly owns the broader observation that equal values of a conventional diversity index can coexist with different species-richness curves, so generic nonidentification is not claimed. Olszewski later made the rarefaction–PIE link explicit. The inspected literature and targeted searches did not state the fixed-richness sharp boundary \(N=9\), the uniqueness of the first collision, or its exact three-draw separation.

Risk: an unindexed teaching note, worked example, or ecological software test could contain the same nine-individual pair.

## Value
**PASS.** Rarefaction standardizes richness across sample sizes, while Simpson/PIE summarizes pairwise abundance concentration. Fixing both observed richness and total abundance removes obvious scale effects and asks when the pairwise summary first ceases to encode the abundance structure needed for the next rarefaction depth. The answer is a natural complete finite cutoff with a unique first obstruction and an exact information increment at sample size three.

Self-review: passed. Independent audit: not yet performed.
