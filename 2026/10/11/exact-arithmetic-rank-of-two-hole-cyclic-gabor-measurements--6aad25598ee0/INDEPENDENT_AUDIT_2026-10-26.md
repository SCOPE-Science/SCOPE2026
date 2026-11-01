# Independent mathematical audit

## correctness

PASS

Goldberger–Kang–Okoudjou Theorem 1 equates the orbit projector-Gram rank with the number of nonzero Weyl ambiguity coefficients. For the complement of {0,a} and N>=5, the character sums at lags 0, +/-a, and all remaining lags reduce to 1+u, 1+u+u^2, and (1+u)(1+v), respectively (with q=2 handled separately). Inclusion–exclusion of u=-1 and v=-1, plus disjoint cubic-root zeros, gives H_N, J_d and 4d*1_(3|q) exactly. The packaged exact-cyclotomic check tests all 589 pairs for 5<=N<=35. The all-N assertion follows from the finite character proof, not interpolation from checks. Exact numerical projector-rank calculations for N=5,6,9,12,15 at 14 spacings matched predicted rank (numerical corroboration only). Direct inspection of all three zero-polynomial geometries and the q=2 collision shows the inclusion–exclusion proof covers N>=5 and all 1<=a<N.

## originality

PASS

The published 2021 Gram-rank theorem and the 2015 Gabor phase-retrieval criteria are credited. The published cyclic boxcar formula covers coprime deleted-site steps by reindexing, but not nonunit steps. A contemporaneous odd-order two-equal-amplitude theorem includes this mask as z=0 and already determines the entire odd-order specialization (loss 4d when 3 divides q). The remaining full nonunit even-order two-hole deficiency formula, including the exceptional order-two lag and overlap J_d, was not found in those compared sources. The combined all-N classification is not claimed as the first odd-order computation. Unknown unindexed equivalent analyses remain possible.

## value

PASS

A full cyclic Gabor tomography orbit built from a constant vector with two dead coordinates is a canonical finite measurement design. Its operator-span rank is natural because it counts recoverable matrix degrees of freedom. The all-N formula distinguishes order-two, order-three and nonunit even-gap effects; for N=12 gaps 1,2,3,4,6 give ranks 116,102,104,108,62, showing essential spacing sensitivity not reducible to a single boxcar length. Exact all-modulus rank counts are useful for deciding whether a proposed physical mask loses directions, without claiming noise stability or a paper-sized contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
