# Scientific review: cyclic spherical-overlap independence

## Correctness — PASS

The final theorem concerns a simple cycle of independently sampled uniform spherical vertices, fixed real dimension at least three, and length at least four. It distinguishes strict-subset exact independence, the whole-vector density, its exact chi-square divergence, and the sharp asymptotic in total variation.

The core equality is a trace of consecutive harmonic projections. Normalized Gegenbauer kernels are the rank-\(D_{d,\ell}\) spherical harmonic projection kernels, so their mixed cycle moments vanish unless every degree matches. Orthogonality gives an \(L^2\)-summable density series when the length is at least four; polynomial measure uniqueness identifies that series with the genuine joint law and establishes nonnegativity without an unsupported positivity assumption. The degree-one term controls the total-variation norm because the higher-harmonic \(L^2\) remainder is exponentially smaller; the required strict rate inequality is proved by two base cases and a gamma-function recurrence. The qubit statement follows by a bijective affine transformation of the Bloch inner products.

The checker actually ran against the bundled script and reported 9,782 successful algebraic/numerical assertions. It tests finite identities, not the infinite-dimensional harmonic argument, which is separately proved. No calculation is interpreted as a proof of the infinite theorem. Mathematical scope and limits are explicit.

## Originality — PASS, with priority risk

Closest primary sources read and compared:

- Zhang, arXiv:2610.25196v1, Sections 6.5–6.9. The paper obtains a single cyclic product's moments, Markov-chain representation, and a logarithmic central limit theorem. The result \(\mathbb E|\Delta_m|^2=2^{-m}+3\,6^{-m}\) agrees with a moment implied by the current density, but a single moment does not determine the joint law or total-variation distance of all separate edge fidelities.
- Huang and Li, arXiv:2610.12765v1, Sections 1.1 and 2.1. They establish independence on forests in a latent spherical edge-indicator model and apply spherical operator traces to cycle-count detection as dimension varies. Their statements concern graph testing with Bernoulli indicators, not the sharp law of all continuous edge inner products as a fixed-dimensional cycle length grows.
- Jones and Potechin, arXiv:2107.00216 / ITCS 2022, Sections 1 and 3. Their spherical polynomial basis and graph-moment results are related harmonic machinery; their inspected results do not state the present full joint cycle density or the exact fixed-dimensional \(L^2\) and sharp \(L^1\) rates.

Statement-level and implication comparisons were made for equivalent parameterizations, general harmonic operators, graph moment frameworks, and direct tables or prior claims. The exact mixed moments and harmonic spectral expansion use classical tools; their mere use is not asserted to be new. Residual risk: a general spectral transfer or polynomial-graph theorem may implicitly imply this specific formula and sharp norm asymptotic. No exhaustive historical priority or independent review is claimed.

## Mathematical value — PASS

A natural random-geometric-graph paradox is that edge overlaps around a cycle can have **all proper marginals independent**, yet the complete set is dependent. The theorem quantifies exactly how quickly this global obstruction disappears when the cycle grows. It provides an \(L^2\) density, an exact chi-square divergence, a sharp total-variation coefficient, and a concrete experimentally interpretable Haar-qubit fidelity corollary. The norm and rate are not consequences of knowing finitely many scalar cumulants or the mean of a cyclic product. The result is structurally motivated rather than an arbitrary special parameter computation.

## Limits

No claim is made for pointwise convergence of the density series, dimension-uniform error, high-dimensional complex states beyond the qubit Bloch representation, or finite closed-form total-variation values. Historical priority relative to very general kernel-operator and spherical polynomial theorems remains a research risk.

Self-review: passed. Independent audit: not yet performed.
