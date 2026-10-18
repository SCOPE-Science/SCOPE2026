# Scientific review

## Correctness — PASS
The hypergeometric absent-species indicator decomposition yields an exact integer expression for rarefied-richness variance. Exhaustive integer-partition enumeration checks every permissible unit-balancing transfer for \(N\le8\), with a separate direct-subset enumeration implementation reproducing the entire lower-bound census and validating the eight-individual example. The unbounded family is verified by symbolic rational-polynomial expansions: all coefficients of the \(m=2,7\) numerator differences are strictly negative and all coefficients for \(m=3\) are strictly positive when expanded in \(t=k-1\ge0\). The expectation increase is a direct binomial-difference identity. The attached standalone checker was executed successfully. Exhaustive finite computation is used only for the finite cutoff, never as an infinite proof.

## Originality — PASS, with residual bibliographic risk
The classical rarefaction literature already provides both mean and variance formulas; the proof does not present those as new. Gotelli and Colwell discuss crossings of *expected* richness under arbitrary community comparisons; the present theorem addresses *variance* after one unit of abundance equalization, including the sharp eight-individual boundary and a sign-stable all-size family. Nipperess and Matsen's broader phylogenetic-moment formulas subsume the variance formula but not, on the inspected material, this transfer-specific sign classification. The full 1975 article by Heck, van Belle and Simberloff could not be inspected, so the possibility of unobserved equivalent comparison results remains a stated risk. No covering result was identified in the examined research-index records and primary texts. Independent bibliographic confirmation is still needed.

## Mathematical value — PASS
The example and its sharp minimality uncover a limitation of using increasing species evenness as a universal predictor of sampling uncertainty. The result is not an arbitrary numerical slice: it resolves an extremal first-occurrence question over all integer abundance partitions, uniquely identifies the first witness, and establishes a parameterized family of arbitrarily large censuses with two strict variance reversals although mean observed richness improves everywhere in the stated range. The contrast between monotone mean and nonmonotone variance has a clear connection to comparing ecological survey precision across sample sizes.

## Scope and risks
The results are mathematical statements about uniformly sampled fixed communities, without inference to ecological population processes or empirical data. The literature search cannot establish absolute uniqueness of an unpublished or differently worded theorem; independently confirm the 1975 source and other combinatorial sampling literature before dissemination.

Self-review: passed. Independent audit: not yet performed.
