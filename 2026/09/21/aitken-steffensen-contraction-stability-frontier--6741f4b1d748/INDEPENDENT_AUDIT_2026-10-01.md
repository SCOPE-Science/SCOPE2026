# Independent mathematical audit — Sharp black-box robustness frontier for scalar Aitken-Steffensen acceleration

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** After translating and scaling so the fixed point is zero and the current error is one, let \(a=g(1)\), \(c=g(a)\), and \(t=(c-a)/(a-1)\). The contraction constraints give \(|a|\le q\), \(|c|\le q|a|\), \(|t|\le q\), while the accelerated error is \((a-t)/(1-t)\). Optimizing the feasible positive and negative endpoint branches yields \(W(q)=2q^2/((1-q)(1+2q))\); the stated continuous piecewise-affine contraction attains equality. Imposing monotonicity yields \(W_\uparrow(q)=q^2/(1-q^2)\) with its own sharp witness. Independent endpoint-grid optimization at several values of \(q\) approached both formulas from below, while exact substitution verifies the witnesses and thresholds.

Checked sources: Assigned RESULT.md and artifact source; Johnson--Scholz 1968 complete paper; Păvăloiu 1968 full public text; Independent feasible-region endpoint optimization.

Residual correctness risks: Finite grid checks are corroborative only; sharpness and universality rest on the analytic branch optimization.; The theorem is exact-arithmetic and scalar..

## Originality

**PASS.** The complete Johnson--Scholz paper studies convergence of generalized Steffensen iteration under divided-difference regularity and local/semilocal parameters; its contractive theorem still includes a divided-difference Lipschitz constant and an initial residual condition. It does not state the bare-global-contraction one-cycle minimax factor or thresholds. Other classical sources checked concern convergence speed, monotone enclosure, convexity, or posterior bounds. No exact factor matching the audited theorem was located.

### Equivalent formulations

Searches/sources: Resultary semantic search: Aitken Steffensen scalar global contraction sharp worst-case factor; Johnson--Scholz DOI 10.1137/0705026; classical Steffensen convergence literature.

Evidence: The exact published-result hit was the audited theorem. Johnson--Scholz Theorem 2 assumes divided-difference regularity plus local numerical parameters; it is not a class-wide one-cycle minimax theorem. No searched source states \(2q^2/((1-q)(1+2q))\) or the monotone factor \(q^2/(1-q^2)\).

Classical convergence theorems are not equivalent to the universal black-box fixed-point-error envelope.

### Broader coverage

Searches/sources: Johnson--Scholz 1968 Banach-space theory; Păvăloiu 1968 operator-equation theory; modern fixed-point acceleration surveys.

Evidence: The older theories are broader in dimension or local regularity assumptions but do not dominate the audited assumption/conclusion pair. Modern surveys describe Aitken/Steffensen and Anderson acceleration without the same scalar global minimax classification.

No inspected broader theorem implies both the exact unrestricted and monotone subclass frontiers.

### Exact database or table

Searches/sources: Resultary exact/semantic search for the two factors and thresholds; web search for the numerical threshold \((1+\sqrt{17})/8\) in Steffensen literature.

Evidence: No earlier exact theorem record or formula match was located.

This is a continuous worst-case theorem, not a finite numerical table.

### Claim versus prior implication

Searches/sources: Does Banach contraction plus classical Steffensen convergence theory imply one-cycle nonexpansion?; Compare two Picard evaluations with classical local quadratic convergence.

Evidence: Classical Steffensen theory can guarantee convergence under additional divided-difference hypotheses but does not provide the audited worst-case factor under only a global Lipschitz constant. Local quadratic acceleration does not imply a better black-box minimax one-cycle factor at equal evaluation count.

The endpoint feasibility optimization and sharp piecewise-affine witnesses are essential new steps.

### Source inspections

- **On Steffensen's Method** — RELATED_NOT_COVERING.
  Identifier: https://doi.org/10.1137/0705026
  Trigger: Highly relevant classical paper explicitly treating contractive Steffensen iteration.
  Material read: Complete seven-page paper, including Theorems 1--4 and the contractive Theorem 2.
  Method: lawful full text
  Evidence: Its convergence criteria depend on divided-difference regularity and initial local parameters; it contains no bare-\(q\) minimax one-cycle factor or audited thresholds.
- **On the Steffensen method for solving nonlinear operator equations** — RELATED_NOT_COVERING.
  Identifier: https://ictp.acad.ro/steffensen-method-solving-nonlinear-operator-equations/
  Trigger: Classical operator-equation source with a plausible broader title.
  Material read: Complete accessible theorem text and hypotheses.
  Method: lawful public full text
  Evidence: It proves convergence under structured operator hypotheses rather than the scalar global-Lipschitz worst-case envelope.

Residual originality risks:
- Several older highly relevant papers, especially Schmidt 1966, Hofmann 1975 and Schneider 1981, were not all inspected in complete theorem-level text; historical equivalence under different notation remains the main originality risk.

## Scientific value

**PASS.** The theorem gives an exact robustness frontier for a classical accelerator under the minimal black-box contraction assumption, identifies sharp stability thresholds, quantifies the gap against two ordinary Picard evaluations at equal function-call cost, and separately solves the monotone subclass. These are natural and practically interpretable boundaries rather than a small-instance calculation.

Residual value risks: The result does not address vector-valued acceleration, floating-point cancellation, or long-run behavior above the one-cycle threshold..

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
