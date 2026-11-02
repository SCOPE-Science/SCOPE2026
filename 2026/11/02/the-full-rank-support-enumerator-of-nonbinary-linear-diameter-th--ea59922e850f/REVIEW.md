# Scientific assessment

## Correctness — PASS

The proof gives a complete four-step classification by support and rank: pivot columns bound the dimension by three; averaging bounds support by four; the hyperplane full-weight count eliminates dimension-three support-four codes; projective-line coverage forces a four-supported dimension-two code to be the ternary tetracode. Exact division by \(|\mathrm{GL}_2(3)|\) yields eight distinct labelled row spaces. All lower-support coefficients follow from elementary finite-field subspace counts. The standalone RREF enumerator checks four distinct fields and all listed small ambient dimensions, including the full support/rank distribution. The infinite theorem relies on the classification, not on the tests.

## Originality — PASS (provisional priority)

Horlemann–Ravi's general polynomial decomposition [1] introduces undetermined full-support coefficients and does not compute this closed polynomial or its rank refinement. Zhang et al.'s antiGriesmer bound [2] already gives strong support obstructions for \(q\ge4\), so that exclusion alone is *not* claimed as new. The ternary tetracode and its projective description are established constructions; the contribution is the exact all-field, all-ambient-size rank-by-support anticode census, including its labelled support-four count. The degree-four ternary exponent also follows from the prior paper’s simplex construction, so only the new exact coefficient and fully refined census are asserted as additional information. Equivalence, stronger-bound, database and direct-implication comparisons did not find a covering polynomial. Residual priority risk remains from coding literature on maximum-weight-three linear codes.

## Mathematical value — PASS

The full rank/support classification computes every unknown coefficient in a natural fixed-diameter case of [1], provides the exact ternary leading coefficient (beyond the already implied degree), and separates a genuine projective-line exception from the generic three-coordinate regime. Exact self-contained counts for an infinite family are useful benchmarks and go beyond merely repeating the fixed-diameter polynomial-existence theorem. It is deliberately scoped to \(q\ge3\), rather than renaming the previously counted binary case.

## Limitations and closest literature

The work does not extend to \(q=2\), to nonlinear anticodes, or to diameter exceeding three. The cited research contains overlapping general bounds and the classical tetracode is not new. The automated RREF checks are finite, and independent scientific audit remains outstanding. References [1] arXiv:2610.31618v1 and [2] arXiv:2511.02519v1 are detailed in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
