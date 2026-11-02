# Review of the exact transient footrule-noise theorem

## Correctness

**PASS.** The claim specifies the lazy discrete-time random-transposition kernel, ordered start, observable, and all quantifiers. The permutation representation on ordered distinct position pairs contains exactly four central eigenspaces, with eigenvalues \(1\), \(1-2/n\), \((1-2/n)^2\), and \(1-4/n\). Exact uniform, one-step, and two-step moments fix the three transient coefficients, and subtraction of the exact mean square gives the stated variance. The independent exact-enumeration checker passed 59 checks. The asymptotic cancellation between the largest two spectral coefficients is explicitly accounted for, and the limiting maximizer is justified by a one-sign-change derivative. No finite enumeration is used as an infinite proof.

## Originality

**PASS, qualified best-knowledge.** The full accessible arXiv manuscript by He, Hutsalyuk, Mussardo and Stampiggi establishes the discrete random-transposition model, its global mixing scale and associated quantum stochastic walks; its spectral variance is a *Hamiltonian* diagnostic, not a transient Spearman-footrule variance. The full available preprint of Jain and Sawhney establishes total-variation and hitting-time mixing for the same random-transposition dynamics, rather than absolute-displacement moment dynamics. The full accessible paper by Xia, Guan and Xu derives stationary/null-distribution properties of Spearman's footrule, including the equilibrium variance credited here, but not the time-dependent three-mode formula. Published research records with potentially related random-permutation covariance and group-Fourier ideas were searched at the level of their statements. Neither their reported claims nor the inspected papers entail the precise finite-time law or the \(18.488377\ldots\%\) overshoot without the evaluated two-position projections. The residual risk is an unlocated special-case formula in the broader interchange-process or association-scheme literature.

## Value

**PASS.** The earliest nonstationary noise profile of a physically canonical random-walk equilibration observable is not monotone, and the exact formula determines the finite-deck noise at every step. The strict all-size overshoot and the universal, sharp \(t=O(n)\) maximum distinguish observable equilibration from the much later distributional total-variation cutoff. This directly matters when comparing randomization experiments or noisy diagnostics against equilibrium uncertainty; the stationary variance can underestimate observed transient fluctuations by a finite asymptotic fraction.

## Closest literature and limits

The motivating source (arXiv:2609.13387; submitted 2026-09-11) studies permutation-group classical-to-quantum mixing and does not calculate the footrule-noise profile. Jain and Sawhney (arXiv:2410.23944) study sharp global mixing; Xia, Guan and Xu (arXiv:2505.01825) study the uniform-permutation footrule null law. All three were inspected in accessible source text, with model, assumptions and claimed quantities compared explicitly. The result does not extend to quantum-walk dynamics or infer a finite-deck unique variance peak. An independently conducted proof or publication-priority review has not occurred.

Self-review: passed. Independent audit: not yet performed.
