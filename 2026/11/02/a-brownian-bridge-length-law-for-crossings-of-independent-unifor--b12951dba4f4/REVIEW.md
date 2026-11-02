# Scientific review: minor-arc length and crossing fluctuations

## Correctness (C): PASS

Conditional on one uniform geometric chord, another chord crosses it with probability \(p(w)=w-w^2/2\), where the doubled short-arc fraction \(w\) is uniform on \([0,1]\). The centered one-chord kernel has exact variance \(1/45\); the degenerate two-chord remainder has variance \(8/45\) per unordered pair. The orthogonal Hoeffding decomposition proves every finite-size variance, projection, and covariance identity. The empirical-process central limit theorem and the deterministic integral identity give the joint Brownian-bridge limit, with remainder vanishing in normalized \(L^2\). The calculus derivation of the unique optimal short-arc cutoff is exact. The packaged checker independently reproduces finite matching enumerations and geometric tests, but does not certify infinitely many sizes.

## Originality (O): PASS with priority risk

Flajolet–Noy (2000), Theorem 3, already gives the precise crossing mean, variance and marginal Gaussian limit, and so those are **not** presented as original. Paguyo (arXiv:2104.01134) gives normal-approximation rates and simple-chord limits; Acan (arXiv:1501.01489) examines the uniform matching and chord position. Their inspected texts do not state the joint limit involving the *physical minor-arc empirical process*, the exact additive projection, or the universally optimal cutoff. General Hoeffding/Donsker results supply the abstract mechanism but do not supply these geometric constants without calculation. Existing published results could nonetheless contain a different derivation of the same formulas; absence of search hits is not proof of priority. In particular, the position of a chord in an unlabeled matching should not be conflated with continuous angular minor-arc length.

## Value (V): PASS

This is a motivated refinement of the classical crossing-count central limit theorem: it identifies which readily measurable geometric statistic generates the leading fluctuations, quantifies the exact finite-size residual variance, and solves a natural optimal observable-design question. The covariance formula gives a nontrivial dependence profile for every threshold and the optimizer is universal in \(n\). These are structural conclusions not furnished by the marginal normal limit alone.

## Limits and residual risks

The result is specific to iid endpoint-uniform chords and the dimensionless short-arc length. The projection is additive, not necessarily the full conditional expectation given all lengths. An independent originality and correctness review is still needed before a publication-priority claim.

Self-review: passed. Independent audit: not yet performed.
