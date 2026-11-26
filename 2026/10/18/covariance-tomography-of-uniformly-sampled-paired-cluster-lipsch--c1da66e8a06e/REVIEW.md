# Independent mathematical audit

## correctness

PASS

The range constraint plus the within-pair differences is exactly the Lipschitz ball for 0<t≤1. Partition by the minimum vertex, disregarding tied minima of measure zero. In minimum-anchored coordinates, the mate of the minimum is uniform on [0,t], and the remaining pairs have independently distributed uniform band vectors in B_t; the changes of anchor are unimodular. Within one ordinary band vector the coordinates need not be independent, despite loose wording in Proof §3; the proof uses their joint band law, which is explicit and correct. For A=2t−t² the band difference has density (1−|d|)/A, and its conditional midpoint has mean 1/2 and variance (1−|d|)²/12. This gives q=t²(4−3t)/(6(2−t)) for squared difference and s=(t²−2t+2)/24 for midpoint variance. The exceptional pair has squared difference mean t²/3, midpoint mean t/4 and variance t²/48. Pair swaps eliminate mixed intra-pair contrast terms and pair-constant cross terms; permutations make the covariance scalar on each summand of H. Mixing over the exceptional pair gives λ_intra=[t²/3+(m−1)q]/(2m) and λ_inter=2(m−1)s/m+2[t²/48+(2−t)²/16]/m, which simplify to the claimed expressions. For x=1−t the gap is x[3+3mx+(1−m)x²]/[6m(1+x)], which gives positivity, the fixed-t limit, and the claimed m²-scaled boundary limit. The bottom projector on H (not on the ambient space, which has a constant zero mode) recovers the matching, and strict increase of λ_intra follows from the t² term and truncation of the band difference density. At t=1 covariance is scalar on H. The supplied exact lattice-enumeration and finite-difference support was inspected, not executed; the general proof does not rely on a finite extrapolation.

## originality

PASS

The distinct claim is the exact interior covariance on the Lipschitz-potential ball of the shortened-pair family, including the gap, matching and distance reconstruction, and boundary scaling. The strongest inspected overlap recovers a matching from covariance for deleted edges of a complete graph, but concerns lengthened pairs at distance 2 rather than shortened pairs and does not cover the claimed regime. No novelty is credited to the ball's volume formula, the symmetry decomposition in isolation, or the general idea of covariance recovery. The inspected citation for equilateral volume does not itself establish the credited paired volume, which is derived directly in this record.

## value

PASS

This is an exact inverse statement from a natural summary of the uniform law on a canonical convex body. Symmetry identifies the possible invariant subspaces but cannot tell whether their eigenvalues coincide, which projector encodes the pairs, or the scale on which that distinction disappears. The explicit formulas solve those questions and identify the common length, with a quantitative transition at the equilateral endpoint. The result is about population covariance, not an unproved sample-recovery guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
