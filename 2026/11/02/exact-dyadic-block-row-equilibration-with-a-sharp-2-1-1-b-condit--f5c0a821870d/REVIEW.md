# Review of the dyadic block-row conditioning theorem

## Correctness (C): PASS

The matrix-inverse identity \((DM)^{-1}=M^{-1}D^{-1}\) gives the two exact maximum-row-sum formulas. Normalizing a largest dyadically scaled block and raising all other admissible exponents establishes the finite-candidate minimum with no finite-search assumption. A circular gap of at least \(1/b\) among the fractional binary logarithms supplies the universal bound, and an equally spaced block-diagonal spectrum attains it. The analytic argument handles arbitrary real nonsingular square matrices and all unbounded integer exponents. The standalone checker independently passed 168 rational matrices with 19,558 comparison candidates and nine diagonal sharpness examples. Finite tests are supplementary, not an infinite proof.

## Originality (O): PASS, subject to historical-priority risk

The closest motivating source is Lindquist–Appelhans–Jackson–Derlaga (arXiv:2610.06414v1, Section 2, Corollary 2), which licenses dyadic block-row scaling in a mixed-precision error estimate but does not derive either the global \(b\)-candidate optimizer or its attained sharp gap. Classical one- and two-sided continuous matrix equilibration, particularly Rump (2003), already supplies underlying real-scaling context and is credited. LAPACK's power-of-radix equilibration routine describes a heuristic rather than a global optimizer. Shapiro (1985) concerns block-diagonal Euclidean-norm scaling; only an abstract was accessible for that plausible historical source. Targeted literature and research-record searches and the accessible prior claim ledger revealed no claim with the same quantifier structure: exact discrete block-row optimum over all integer exponents and sharp loss against continuous scaling for each block count. This is a reasoned best-knowledge comparison, not proof of global priority. An unindexed older rounding or matrix-scaling result remains possible.

## Mathematical value (V): PASS

The motivating paper's bound depends on a permitted discrete scaling choice without providing a computable optimal choice for its infinity-condition factor. The theorem replaces an infinite integer optimization with at most \(b\) candidates and identifies the precise unavoidable loss as a function of the number of blocks. The factor is attained, hence not just a coarse rounding estimate. These are naturally motivated numerical design quantities; the claim does not rely on an invented application or asserted whole-solver improvement. A one-sided unbounded-exponent benchmark is valuable even though finite floating-point exponent limits and other mixed-precision error factors must be assessed separately.

## Closest sources and limitations

Primary material examined: arXiv:2610.06414v1, especially the analytical block-scaling Corollary 2 and its proof; Rump's 2003 author-provided full text, especially introduction, norm-scaling formulation and Theorem 3.1; the LAPACK `DGEEQUB` routine documentation. The accessible Shapiro (1985) abstract was considered as a plausible related source but did not permit a full-text exclusion. The exact result assumes a fixed block partition, one-sided positive unbounded radix scaling, an invertible square matrix and exact arithmetic. It minimizes only \(\kappa_\infty(DM)\), not a combined physical or numerical error bound. An independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
