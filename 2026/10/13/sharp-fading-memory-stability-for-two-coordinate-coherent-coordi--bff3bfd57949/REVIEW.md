# Scientific review: sharp fading-memory CoCD stability

## Correctness — PASS

The exact refresh/decay sequence in Liang et al., equations (5)–(7), produces the explicitly displayed three-variable matrix and cubic. The four strict real-cubic Schur inequalities reduce algebraically to a positive \(p(1)\), a nonnegative perfect-square sum at \(-1\), a determinant constraint, and a single scalar quadratic \(Q\). For interior fading and coupling, \(Q\) has two positive roots and its smaller root precedes the determinant boundary. The remaining endpoint cases are checked separately. Unit-modulus roots preclude convergence at equality; outside, the spectral radius is greater than one. Symbolic identities and 576 sampled spectral comparisons were reproduced using the bundled checker; finite tests are ancillary to the analytic argument.

## Originality — PASS (residual risk retained)

The motivating original paper [1, §4 and §5.3, Appendix C] defines fading CoCD and gives sufficient descent conditions, but the inspected full text does not supply the exact necessary-and-sufficient coupled quadratic step-size surface. The IAG full text [2, §2–§4] analyzes stored gradients of scalar component functions and a different momentum mechanism, not the nonconservative per-coordinate vector fields of this test family. Classical cyclic coordinate descent covers the zero-decay limit, but not the positive-decay enlargement above the standard \(\alpha=2\) threshold. Closest published mathematical comparisons involve randomized delayed Gauss–Seidel and one-step Euclidean transient bounds; their conclusions do not imply the fixed cyclic CoCD Schur classification. Search cannot rule out unindexed equivalent work.

## Value — PASS

The result answers a natural algorithm-design question not resolved by the motivating sufficient bound: exactly which fixed step sizes converge when stale partial derivatives are retained with fading memory? The sharp, condition-dependent frontier and an explicit stable \(\alpha>2\) region demonstrate a qualitative effect of gradient memory that is invisible to the ordinary coordinate-descent step-size ceiling. The result is intentionally restricted to a tractable two-coordinate quadratic and is not an extrapolation to neural-network objectives.

## Sources and limitations

[1] Liang et al., arXiv:2605.14373, especially original update rule, §5.3, and Appendix C. [2] Gürbüzbalaban, Ozdaglar, and Parrilo, arXiv:1506.02081, especially §2 and rate theorems. Classical coordinate methods and related published delay/step-size classifications were used for coverage comparisons. The cubic Schur criterion is standard; only its application and exact parametric boundary are claimed as the contribution. No independent evaluation is represented.

Self-review: passed. Independent audit: not yet performed.
