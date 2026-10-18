# Self-review

## Correctness — PASS
The normalization uses \(U_{i+3}=-U_i\) and \(M_{i+3}=M_i\). The original involute's half-sum formulas yield the two ordered triangular interpolations with fractions \(t_i\) and \(r_i\). The product matrix has repeated off-diagonal columns, giving exactly \(T=\rho I+(1-\rho)\mathbf1w^T\) and the weighted stationary point. Its nonconstant eigenvalue is \(\rho\), so iteration contracts by the asserted factor. Elementary arithmetic-geometric-mean inequalities prove the sharp quarter bound and equality case; a one-parameter admissible family realizes every rate below it. Every assumption and indexing convention is stated in RESULT.md. The accompanying exact-rational checker validates the nonlinear-looking half-sum indexing on six examples and five steps each; this is not used as an infinite proof.

## Originality — PASS (best-knowledge self-review)
The 2012 parallel-diagonal transform describes a single precursor but not repeated contraction. Craizer–Martini's 2014 first-public work defines the construction and qualitative convergence. The 2017 discrete-cycloid spectral framework supplies a general operator and regular-polygon instances, but not the exact all-skew-hexagon rate or sharp global bound. A publicly available general finite-solve result already makes the central point computable using a linear inverse; it is specifically acknowledged and is not presented as novel. The new claim is the explicit scalar spectral law with its sharp global extremizer and attainable range and the associated closed barycentric weights. Equivalence-formulation, broader-coverage, exact-table, and prior-implication comparisons appear in AUDIT.json. Residual risk: another general operator treatment may contain an unstated equivalent specialization, and semantic search cannot establish uniqueness.

## Mathematical value — PASS
The six-sided direction case is a complete, natural, first-nontrivial polygonal class for this discrete Minkowski involute. Exact spectral contraction and rigidity quantify a qualitative convergence theorem and replace generic linear solves by a closed barycentric center formula. The equality class and full range are structurally motivated rather than arbitrary calculations.

## Evidence and limitations
Reproduce the exact arithmetic checks using `python3 verify.py`. The proof is symbolic, not experimental; the bounds exclude degenerate boundary norms and do not extend to more than three direction pairs. Checked primary sources: Craizer–Teixeira–da Silva (arXiv:1210.2442); Craizer–Martini (arXiv:1406.3205); Craizer–Teixeira–Balestro (arXiv:1702.00522); the publicly available finite-linear-solve result cited in RESULT.md; and Arnold et al. (arXiv:1510.07742). This is not independent verification.

Self-review: passed. Independent audit: not yet performed.
