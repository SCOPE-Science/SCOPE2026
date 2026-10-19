# Self-review

## Correctness — PASS
The homogeneous polar equations give the exact strict quartic identity \(\dot P=-4a|z|^2P\) and positive coercive bounds for \(0\leq b<\omega\). Every global solution therefore converges to zero. For \(b\leq a\), \(V=|z|^2+P\) is smooth, proper, strict and has Hessian \(2I\). For \(b>a\), averaging the leading Hessian inequality for any hypothetical local \(C^2\) Morse function over the quarter-turn group contradicts the outward cubic drift on the positive real ray. The same group average excludes every strict quadratic at equality. Odd-degree leading polynomials are not positive definite on the entire plane. Both symbolic identities and rational representative cases were recomputed in `check.py`.

## Originality — PASS, with documented risk
Jongeneel (arXiv:2610.05626v1, Proposition 3.5, Corollary 3.9) gives a nilpotent-Jacobian counterexample and a semisimplicity necessary condition, but not a sharp threshold for zero-Jacobian homogeneous cubic fields. Liu–Fitzsimmons (arXiv:2607.16171v1, Theorem II.2 and Section IV.D) treats a twofold cubic family whose relevant members lack polynomial Lyapunov functions, whereas this fourfold family always has a strict quartic. The closest inspected published mathematical record (3937ccf41604) uses flat smooth time changes and proves jet invisibility, not a polynomial-family classification. Actual equivalence, generalization and coefficient searches uncovered no covering implication. A hidden classical equivariant reduction or less-indexed source remains a priority risk; literature absence is not proved.

## Mathematical value — PASS
The fourfold-equivariant cubic monomials are the natural lowest nonlinear covariants under quarter rotation. The theorem finds an exact, nontrivial boundary for positive-Hessian certificates inside a uniformly globally stable region, distinguishes Morse regularity from polynomial existence, and determines the minimal strict polynomial degree. It exposes a limitation of zero-linearization tests that is not visible from spectral information or the existence of some smooth strict Lyapunov function.

## Scope and limitations
The results are restricted to \(a>0\), \(0\leq b<\omega\). No classification of all homogeneous cubic fields, of \(\omega\leq b\), or of arbitrary Lyapunov regularity is claimed. The symbolic verifier checks identities, not bibliographic priority. An independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
