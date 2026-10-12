# Review of sharp alignment decay in rank-one tangent-polar refinement

## Correctness — PASS

The point \(W=e_1e_1^{\mathsf T}\) has tangent projector deleting precisely the bottom-right entry. The chosen symmetric \(g\) has opposite-sign eigenvalues and is invertible because \(b>0\). The explicit orthogonal polar factor is obtained by a two-eigenvalue calculation; repeated projection doubles the off-diagonal-to-diagonal ratio at every step, which establishes the closed-form \(X_t\). Its pairing with \(g\) and the exact nuclear norm produce \(R_t\), whose continuous-parameter derivative proves strict decrease. The full derivative of the squared ratio in \(y=b^2/a^2\) has a unique change from negative to positive at \(1/(2^{t+1})\), proving the global sharp envelope and attaining examples, including the \(t=1\) boundary. Exact-rational, symbolic, and direct polar-SVD checks in `verify.py` corroborate, but are not substitutes for, the complete proof.

## Originality — PASS, subject to stated retrieval risk

The complete arXiv:2609.02734v1 preprint describes this same alternating operation and gives a conditional alignment premise plus an existing best-inner-iterate safeguard, but its relevant methods, theorem discussion, and appendices do not supply the exact multi-step rank-one formula or sharp worst-case envelope. The complete arXiv:2507.12142v2 preprint discusses repeated tangent orthogonalization and one-step approximation, but the inspected relevant sections do not imply a quantitative strict monotone loss and exact \(t\)-dependent extremal ratio. Separate mathematical-result searches of similarly worded, equivalent, and dominating forms identify no published record that states or implies this precise classification; this is evidence, not proof of unique discovery. A rephrasing hidden in older projected-polar and alternating-projection literature remains a residual originality risk.

## Value — PASS

The motivating algorithm uses multiple inner iterations to flatten singular values, but its convergence hypothesis requires a separate descent-alignment lower bound. The explicit worst-case ratio is \(4/5\) after three steps and \(8/17\) after five, and tends to zero as the number of raw inner steps grows. Thus the quantified trade-off is not a generic counterexample to a conditional theorem: it gives a sharp, naturally parameterized limitation for choosing refinement depth, while explaining why the previously proposed alignment safeguard can matter. It is a complete boundary within the smallest nontrivial fixed-rank tangent geometry; no downstream theorem or claim about large networks is required for this limited finding.

## Closest literature and limitations

Andriianov et al. (arXiv:2609.02734v1) supply the exact recurrence and explicitly propose the safeguard. Bogachev et al. (arXiv:2507.12142v2) precede them in discussing projected orthogonalization. The novelty claim is restricted to the formula, strict monotonicity, and sharp finite-horizon minimum on the specified family. The result does not show universal degradation, failure of a safeguarded choice, or lack of convergence of the full optimization algorithm.

Self-review: passed. Independent audit: not yet performed.
