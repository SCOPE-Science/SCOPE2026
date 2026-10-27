# Mathematical review: rank-conditioned idempotent laws

## Correctness — PASS
The coefficient-matrix idempotent equation is exactly the Frobenius-semilinear fixed-point problem \(x=A^{\mathsf T}x^{[2]}\). Every \(\mathbb F_2\)-independent fixed tuple is \(\mathbb F_q\)-independent, by the minimal relation and Frobenius argument. For uniform matrices of rank \(s\), kernel-subspace avoidance gives \(\alpha_{n,s,r}(q)\); uniformity of ordered output frames gives the exact fixed-frame moments. Gaussian binomial inversion yields every probability. Asymptotic leading terms give the \(\operatorname{GL}_s(\mathbb F_2)\) limiting law. Every finite-field configuration listed in `RESULT.md` was exhaustively verified by `verify.py`; the checks corroborate but do not establish the infinite claim.

## Originality — PASS with residual historical uncertainty
The survey arXiv:2610.22248v1 states the idempotent equation and reports the invertible-case mean, not the nonperfect rank-conditioned distribution. The already-known full-rank characteristic-two law is acknowledged and is not the contribution. The all-rank formula with \(q\)-dependent singular strata, the exact conditional mean, and the limiting rank-\(s\) law are not implied by that full-rank statement. The relevant finite-field rank-distribution article does not study Frobenius-fixed vectors. Targeted comparisons of equivalent formulations and potentially stronger results found no known statement that covers every singular rank. Remaining risk: classical or unindexed semilinear counting literature might give an equivalent theorem.

## Value — PASS
The rank of the structure matrix measures the dimension of \(E^2\), a basic invariant separating perfect and nonperfect evolution algebras. The result solves the complete idempotent-count distribution across **all** rank strata, rather than an arbitrary small example. The exact finite-field dependence and the rank-dependent large-field universality give structural quantitative information about random nonperfect algebras, in the broader setting of the survey's random-algebra questions. No general theory for odd characteristic or unlabelled isomorphism classes is claimed.

## Limits and closest literature
Kaygorodov–Martín González–Viruel (2026), arXiv:2610.22248v1, Sections 1.1 and 2.2.3 and Remark 23; previously established invertible-case fixed-space law; Wei–Zou (2023), arXiv:2310.12368, on the distinct meaning of idempotent algebras; Fulman–Goldstein (2012), arXiv:1211.0504, on ordinary rank statistics. Survey full HTML was inspected, while latter two were evaluated from their abstracts. Absolute literature priority remains open to a domain expert's search.

Self-review: passed. Independent audit: not yet performed.
