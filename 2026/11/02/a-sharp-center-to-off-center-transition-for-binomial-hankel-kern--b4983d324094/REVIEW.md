# Scientific review: binomial Hardy Hankel kernel tests

## Correctness — PASS

The exact operator and kernel norms use the standard Hardy-space normalization. The Poisson-variance identity reduces every kernel vector to the explicit radial function in RESULT.md. For the center-optimality transition, the relevant quadratic in the coefficient has roots parameterized by \(x=r^{2n}\), and the unique maximum of the upper root yields the stated threshold; the borderline case \(m=3n\) is an exactly soluble cubic radial profile. At the positive threshold with \(m>3n\), the nonzero contact radius is unique, and comparison near the origin prevents positive optimizing radii from collapsing to zero from below. The small-coefficient scale is obtained by a compactness-controlled polynomial maximum, not by numerical extrapolation. The full Hankel norm is controlled by a finite path-adjacency spectral decomposition. These independent steps support all stated quantifiers and both asymptotic coefficients. The 8,284 finite exact/arithmetic tests in `check_binomial.py` passed, but are not used as infinite proofs.

## Originality — PASS, best-knowledge assessment

The relevant September 2026 source explicitly sets up the Garsia/kernel-testing norm and states the qualitative polynomial monomial-only SRKT classification. A published polynomial classification and a stronger finite-rank shifted-Blaschke result were inspected in full. Neither gives the sharp binomial center-optimality threshold, its continuous-versus-jumping maximizing-radius distinction, the fractional-power law at the monomial limit, or the two-term full-norm/test-norm deficit. Dyakonov's earlier Garsia-norm paper develops general extremality and norm-attainment theory but does not supply these specific expressions. Targeted equivalence, broader-coverage, and exact-parameter searches found no covering theorem. These are best-knowledge, not priority-certified, findings. A historic special-function or two-frequency Poisson-variance optimization might have computed the same threshold outside the titles searched; that risk remains.

## Mathematical value — PASS

The kernel-testing norm is the concrete quantitative invariant underlying the strong reproducing kernel thesis. Although the qualitative equality classification is known, it does not identify which kernels optimize the test or how quickly testing loses accuracy near an extremal symbol. The sharp exponent boundary \(m=3n\) separates two distinct geometric transitions: no center phase, a continuous center transition, and a discontinuous finite-radius transition. The fractional-power sensitivity versus linear Hankel-norm response determines a nontrivial near-equality scale with exact constants for the complete natural family of two-monomial perturbations. It is not a renaming of the known monomial-rigidity statement.

## Relationship to closest literature and limitations

The claim concerns fixed integer exponents and a two-frequency polynomial only. It does not settle the unrestricted BMOA or general compact Hankel strong-thesis question. Residual publication-priority uncertainty remains about older explicit binomial Garsia calculations; no such dominating source was identified in the accessible inspected material. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
