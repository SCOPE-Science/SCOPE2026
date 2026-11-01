# Review of the positive-tolerance numerical-information theorem

## Correctness
PASS. The objective is over unit-vector pairs and the hypotheses require only self-adjoint finite-dimensional matrices and two nonnegative expectation tolerances. Reconstructing the mixed-state minimax with the absolute-value support function gives the exact spectral spread. The trace-one constraints and at most two independent active boundary equations force the sum of squared support ranks to be at most four; hence both states are rank one. The primal and finite-dimensional dual optima are attained. The Bloch-sphere calculation independently recovers the exact piecewise saturation profile. The finite script is a diagnostic, not a general proof.

## Originality
PASS on a best-knowledge literature and available-claims comparison. Johnson (arXiv:2610.29826v1, Sections 2 and 4–5) proves exact numerical-information dependence, not an error-aware quantitative formula. Chen and coauthors (arXiv:1212.3503, Section IV and Appendix C) prove an exact qualitative pure/mixed uniqueness implication, not a positive-error spectral-spread formula. A prior exact-zero-tolerance operator-distance theorem was identified and excluded as existing coverage. The present nonzero-tolerance penalty and active-face rank reduction cannot be read off from its statement. Residual publication risk remains from older general semidefinite optimization literature and unrecognized operator-system equivalents.

## Mathematical value
PASS. Expectation data are typically approximate, so the worst-case unmeasured expectation error is a natural invariant. The exact dual formula makes error sensitivity computable without optimizing nonconvex pairs of pure states, and the qubit example has a sharp nonlinear saturation threshold. The two-error-constraint rank-rigidity mechanism explains why pure states suffice even though mixed-state convexification is used in the proof. The theorem is finite dimensional and does not claim an arbitrary-observable count or a full distributional measurement-error model.

Self-review: passed. Independent audit: not yet performed.
