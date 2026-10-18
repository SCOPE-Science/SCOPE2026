# Self-review

## Correctness — PASS
Parseval reduces the first resonant moment to the unique primitive collision between \((0,B,0)\) and \((B-A,0,A)\). The exact normalized cross term is \(2\binom BA |c_0|^{B-A}|c_1|^B|c_2|^A/S^B\), with no other collisions for powers below \(B\). Strict log-concavity on the power simplex proves the unique optimal allocation. Two phase-offset measurements form exact cosine/sine quadratures, whose inverse local condition number and sharp deterministic angular perturbation bound follow from planar geometry. Stirling's formula establishes the stated balanced-family decay, while a binomial-probability bound proves the global bound. The included exact checker corroborates the collision and radius formulas in 614 finite cases; the proof covers all primitive pairs, not merely those tested.

## Originality — PASS
The closest published full text, *Even phase moments recover the normalized geometry of a three-frequency spectrum* (2026-10-04), proves the **equal-magnitude** phase formula and explicitly does not address non-unimodular coefficient magnitudes. Its collision formula is credited rather than relabeled. The new theorem optimizes arbitrarily weighted first-resonance contrast, classifies all maximizing weights, and derives exact two-probe inversion conditioning and gap asymptotics. Pan et al. (2026, arXiv:2609.09740v1) treat non-even majorant inequalities, and Ling et al. (2026) study Gaussian average norm ratios. Neither statement entails this precise sharp inverse design. Residual risk: equivalent older experimental-design optimization may be unindexed; only Pan's abstract and published statement, not its full arXiv manuscript, were accessible.

## Value — PASS
The primitive resonance order is the first point at which a phase invariant is observable through even Fourier moments. The amplitude allocation theorem answers a natural sharp measurement-design question: how to maximize recoverable phase contrast subject to fixed \(L^2\) power, and hence minimize exact deterministic local inverse amplification. The coefficient-energy ratio differs strictly from equal powers; the exponentially small optimal contrast demonstrates a real obstruction even with optimal design. This is a motivated inverse observable, not a degree substitution or a minor norm-constant increment.

## Restrictions
Requires three nonzero coefficients with known magnitudes, one-dimensional integer frequencies and two controlled coefficient-phase perturbations. Does not solve unrestricted phase retrieval, determine noisy minimax risk, or assert that all possible sensing modalities share this condition number.

Self-review: passed. Independent audit: not yet performed.
