# Scientific review

## Correctness
The domain and quantifiers are fixed \(1/2<\beta<1\), \(0<c<2^{\beta}\), and integer tree sizes tending to infinity. The proof reconstructs the exact insertion-depth innovation/variance recurrence, proves \(v_n\sim c n^{1-\beta}/(1-\beta)\), integrates the three variance regimes, and gives the separate martingale/Kronecker argument for almost-sure and \(L^2\) convergence above the threshold. The separate verification script exhaustively checks five small finite tree sizes with rational probabilities; those checks are corroboration only. **Correctness: PASS.**

## Originality
The closest antecedent, Gałązka–Wdowicka (arXiv:2610.00614v1), explicitly proves finite-size path-length identities but its asymptotic linear-limit theorem requires \(p_n=O(1/n)\); the stretched-exponential family here violates that assumption. Its Section 10 asks for relaxations. Sénizergues (arXiv:1904.07115v3) studies the same weighted-tree construction but the inspected profile theorems assume polynomial cumulative-weight growth. Targeted statement/alias/result searches located no directly covering sharp transition. Abstract general martingale coverage remains a priority risk. **Originality: PASS, subject to independent priority assessment.**

## Mathematical value
A concrete, natural superpolynomial-weight family settles a sharp boundary for the motivating paper's open extension direction. The critical \(2/3\) exponent is corroborated by exact powers and constants on both sides, including the logarithmic transition. The result quantifies nonuniform recursive-tree traversal costs and identifies precisely when their linear-scale random correction is square-integrable. **Mathematical value: PASS.**

## Limitations
No weak-limit theorem is asserted below the threshold, and no result is asserted for \(\beta\le 1/2\). Numerical large-size comparisons converge slowly and are not evidence of the infinite theorem. Independent priority and scientific audits remain unperformed.

Self-review: passed. Independent audit: not yet performed.
