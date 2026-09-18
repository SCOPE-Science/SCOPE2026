# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The lower bound was rederived for rectangular matrices rather than inferred from the square statement in the motivating paper. For a uniform \(d\times e\) matrix \(A\), the statistic \(g(A)=|\ker A|\) has
\[
\operatorname{Var}(g(A))=(q^d-1)(q^e-1)(q-1)/q^{2d}.
\]
Counting ordered pairs of kernel vectors against a fixed rank-\(t\) perturbation gives covariance
\[
(q-1)(q^{d+e-t}-q^d-q^e+1)/q^{2d}.
\]
Averaging over a random rank-at-most-\(r\) mask gives the claimed lower bound. Secret invertible factors do not affect this statistic because they preserve rank and kernel cardinality.

For achievability, the additive channel with uniform input is diagonal in additive characters. On a uniform exact-rank shell, the Fourier coefficient at a rank-\(s\) character is the normalized bilinear-forms eigenvalue \(B_r(s)/C_{d,e}(r)\). Cioabă--Gupta Theorem 4.3 gives strict decrease of \(|B_r(s)|\) with \(s\) for \(q\ge3\); Theorem 4.6 gives the same for \(q=2,e>d\). Thus rank one is the largest nonconstant frequency. Its coefficient was independently evaluated by conditioning on whether a fixed nonzero vector lies in the random kernel, yielding exactly
\[
(q^{d+e-r}-q^d-q^e+1)/((q^d-1)(q^e-1)).
\]
This matches the lower bound.

The square specialization agrees exactly with the converse expression in Cohen--D'Oliveira--Sprintson. Their proof of the kernel-statistic converse was checked: the exact first bound does not intrinsically require \(r\le n-2\); that restriction is used to obtain their further \(q^{-r}/2\) simplification. The rectangular derivation in RESULT.md avoids depending on this observation.

The finite verification artifact evaluates the published bilinear-forms eigenvalue formula with exact integers and rational arithmetic. It checks 532 eligible parameter tuples and separately confirms the known binary-square exception. These computations support, but are not needed for, the proof.

## Originality

The principal recent source, arXiv:2609.18876v1 (submitted 16 September 2026), proves an exact converse expression for square low-rank masking, but its two proposed masking methods are only shown to lie within a factor of two of the optimum. Its maximal-correlation theorem analyzes uniform rank balls and independent low-rank factors, not the uniform exact-rank shell as an exact minimizer.

The association-scheme ingredients are prior results and are not claimed as new. Brouwer--Cioabă--Ihringer--McGinnis give the bilinear-forms eigenvalues and the binary-square exceptional behavior; Cioabă--Gupta prove the absolute-eigenvalue monotonicity used for \(q\ge3\) and for binary nonsquare rectangles.

Searches covered the exact arXiv identifier and combinations of “exact-rank”, “uniform rank-r”, “rank shell”, “maximal correlation”, “matrix masking”, and “bilinear forms graph”. No earlier source was found that connects these spectral results to the rank-constrained maximal-correlation minimax problem or states the rectangular exact optimum above.

The three primary sources listed in RESULT.md were available and their relevant theorem statements were inspected. No inaccessible source surfaced as a concrete likely coverage candidate. Because the motivating preprint is only days old, simultaneous responses, later versions, and not-yet-indexed work remain a material residual originality risk. The originality assessment is therefore only to the best of our knowledge.

## Value

The result closes the finite-parameter achievability/converse gap of the new nonbinary square masking problem exactly, rather than only asymptotically. It also extends the exact converse and optimum to rectangular matrices and shows that secret invertible pre/post transformations cannot beat the shell construction. The optimizer is simple to sample using the same full-rank-factor machinery already used for rank-ball sampling.

The binary square case is intentionally not claimed. The exclusion is substantive: for rank \(d-1\), the bilinear-forms spectrum has a higher-magnitude rank-two coefficient than the rank-one coefficient.

## Review status

Correctness, originality, and value each support acceptance under the Phase II standard. No independent validation is asserted.
