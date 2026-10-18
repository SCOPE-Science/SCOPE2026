# Scientific review: four-site quenched-trap current classification

## Correctness

**PASS.** The model is a finite irreducible four-state continuous-time chain for every positive rate quadruple and every \(|\varepsilon|<1\). The proof explicitly enumerates all four directed spanning-tree terms for each hole location. Its tree-normalization and current-numerator identities yield the closed formula and establish positivity of the denominator. The resulting parity defect and second-order coefficient are exact consequences of that formula. A separate deterministic script checks the defining polynomial identities symbolically and compares 48 parameter/bias cases against independent numerical solutions of the generator. The numerical checks corroborate, rather than replace, the exact algebra.

## Originality

**PASS, subject to residual literature risk.** Sakai and Akimoto, arXiv:2512.03316, study the same quenched-trap dynamics and present uniform-bond-bias and inversion-correspondence mechanisms, but their analytical treatment and simulations do not supply this fixed-density four-site necessary-and-sufficient condition. The condition \(a+c=b+d\) can hold for genuinely non-reflection-symmetric rate sequences with \(a\ne c\) and \(b\ne d\); it is distinct from the published symmetry mechanisms. The nearest boundary-driven study concerns open reservoirs, whereas older homogeneous-ring solutions do not imply this quenched-site cancellation without additional analysis. Broader exact one-hole random-walk formulas could implicitly encode the result. Database searches cannot establish mathematical uniqueness, and no independent literature audit has occurred.

## Value

**PASS.** This is a complete natural finite interacting-ring classification for every positive trap quadruple and the full bias interval. The exceptional balanced-sublattice family distinguishes exact global current symmetry from spatial reflection symmetry, and the explicit sign and quadratic coefficient characterize rectification direction. This is more informative than an isolated numerical counterexample or a routine small-bias coefficient; it supplies the exact nonlinear cancellation locus and a small-system diagnostic relevant to the source's disorder-induced rectification problem.

## Scope and limitations

Only three particles on four periodic sites are covered; no thermodynamic limit or arbitrary-density criterion is claimed. The manuscript of Sakai and Akimoto was examined in the relevant main text and appendices, but possible implication by older general disordered finite-state transport formulas remains a residual risk. The source date is the earliest verified public preprint submission (2025-12-03), not the later journal date.

Self-review: passed. Independent audit: not yet performed.
