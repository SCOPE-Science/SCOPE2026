# Scientific assessment

## Correctness — PASS

The proof checks each class of factors separately: factors with at least two ones meet a selected alternate one-position, all-zero factors occur at the terminal zero, and single-one factors may be shifted to the latest eligible one or last boundary. For even exponents, uniquely occurring power-gap factors and the sole longest zero-run enforce the exact cardinality. For odd exponents, two additional uniquely occurring factors at the terminal boundary provide the sharp lower bound. The disjoint intervals and uniqueness are proved for all integers in scope. The checker independently checks every distinct factor and every certificate for stated finite test ranges; numerical checks are supplemental rather than proofs of the infinite case.

## Originality — PASS within inspected evidence

Schaeffer–Shallit, arXiv:2012.06840v6, Section 6, Theorem 8 already supplies an upper bound that specializes to this same dyadic count, and explicitly says that a matching lower bound remains to be established by other means. The lower-bound argument here is the distinguishing claim. Béal–Crochemore–Romana, arXiv:2509.08503v2, Section 5, Table 2, reports a greedy cardinality of \(k\) at dyadic length \(2^k\), rather than optimality. The OA postprint of Mantaci et al., *A Combinatorial View on String Attractors*, was checked for the same powers-of-two object and does not present its dyadic sharp lower bound. Other exact results on period-doubling, Fibonacci, and Thue–Morse families concern different words. Searches of mathematical records, aliases, and related public literature identified no dominating exact theorem. Remaining risk: an equivalent sharp lower-bound argument may occur in unindexed work.

## Mathematical value — PASS

This is an exact natural repetitiveness invariant for every dyadic prefix of a standard 2-automatic sparse sequence, upgrading a known constructive upper bound plus logarithmic-order lower bounds to equality. The odd/even certificate distinction is mathematically necessary to achieve the exact additive term. The result also precisely quantifies an asymptotic factor-two gap between a recent practical attractor-generation algorithm's outputs and optimum, thereby addressing a concrete algorithmic benchmark. It does not imply an exact formula at arbitrary prefix lengths or classify all optimum position sets.

Self-review: passed. Independent audit: not yet performed.
