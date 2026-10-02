# Independent mathematical audit — SCOPE-20260918-63a985cd76f4

Final disposition: **PASS**.

## Correctness
**PASS.** The affine recurrence was reconstructed from the zero of the affine operator. Its companion characteristic determinant is \(\det((r^2-r)I+\lambda(2r-1)M)\), so stability reduces to the scalar equation over spectral values of \(M\). Strong monotonicity and the norm bound imply the exact half-disk enclosure \(\operatorname{Re}\zeta\ge q\), \(|\zeta|\le1\). A fresh symbolic elimination of a unit-circle root reproduced \(c(t)=(5t^2-2)/(2(2t^2-1))\), \(\phi(t)=t(3t^2-1)/(2(1-2t^2))\), its strict increase on \([1/\sqrt3,2/3]\), and the cubic \(3t^3+4qt^2-t-2q=0\). The planar rotation-dilation has exactly the boundary spectral value, and the scalar endpoint gives the multiplier \(r=-1\). Finite-dimensional spectral radius below one is sufficient for R-linear convergence even for defective matrices.

## Originality
**PASS.** The motivating 2026 reflected-gradient paper publicly states the sharp merely monotone affine threshold and separately proves strong-monotonicity convergence, while the sharp OGD frequency-domain result assumes strong monotonicity together with cocoercivity. Under only strong monotonicity \(\sigma\) and Lipschitz norm \(L\), that latter theorem yields the weaker sufficient scale obtained from cocoercivity \(\sigma/L^2\), not the audited cubic interpolation. Resultary searches located the assigned result and related later optimization records but no earlier or stronger statement of this exact universal half-disk stability boundary.

### Equivalent formulations
The control/root-locus and optimization formulations were compared at the level of hypotheses and spectral region, not by title.

### Broader coverage
No inspected broader theorem implies the cubic threshold for every affine matrix with symmetric part at least \(\sigma I\) and norm at most \(L\).

### Exact database or table
There is no relevant finite database parameter here; the search was used only to detect an already-published identical theorem, not as proof of novelty.

### Claim versus prior implication
The final theorem is neither a special case nor a mechanical corollary of the inspected stronger-looking results.

## Value
**PASS.** This is a natural sharp stability problem for the affine subclass of reflected gradient/optimistic gradient. The theorem gives an exact universal condition-ratio law, identifies the extremal operator, and interpolates two known endpoint constants. It is a motivated structural boundary rather than a numerical tuning anecdote.

## Source inspections
- **A Parameter-Free Adaptive Reflected Gradient Method for Monotone Variational Inequalities** (https://arxiv.org/abs/2609.18355): primary abstract and indexed theorem context; full-text retrieval was attempted through open and authorized routes but no verified PDF was obtained Assessment: ABSTRACT_LEVEL_COMPARISON_WITH_ACCESS_RISK. Evidence: The accessible primary statement separates the sharp merely monotone affine threshold from the strong-monotonicity convergence result; it does not state the condition-ratio cubic.
- **Frequency-Domain Representation of First-Order Methods: A Simple and Robust Framework of Analysis** (https://arxiv.org/abs/2109.04603): primary indexed abstract/theorem description Assessment: RELATED_STRONGER_HYPOTHESIS_NOT_COVERING. Evidence: Its sharp OGD boundary assumes strong monotonicity and cocoercivity, a smaller operator class than the audited strong-monotone plus norm-bounded affine class.

## Residual risks
- The very recent motivating preprint could not be inspected in verified full text in this run, so hidden overlap remains possible.
- Control-theoretic Schur-stability literature is extensive; an equivalent half-disk extremal calculation under different terminology remains a residual originality risk.
