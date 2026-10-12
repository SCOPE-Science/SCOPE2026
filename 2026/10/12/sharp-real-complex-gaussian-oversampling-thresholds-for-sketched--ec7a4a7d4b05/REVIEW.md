# Scientific review

## Correctness — PASS
The block-triangular reduced matrix follows exactly because the spectator subspace is invariant and the sketched basis has full column rank almost surely. Its non-spectator eigenvalue is a residualized Gaussian least-squares coefficient. Orthogonal Gaussian invariance gives the quotient \(U/\sqrt H\), with denominator degree of freedom \(s-m+1\) and distinct real/complex normalizations. Beta-prime and gamma integrals prove each tail, absolute-moment formula, and divergence at the critical exponent. The packaged finite tests reconstruct the full sketched matrix and corroborate these identities but are not used as infinite proofs. Risk: exact-arithmetic independence depends essentially on Gaussianity and the fixed invariant spectator directions.

## Originality — PASS, with residual risk
The 2026 randomized Rayleigh–Ritz paper establishes high-probability existence guarantees for a square Gaussian pencil. The older Nakatsukasa–Tropp work specifies the oversampled least-squares sketched Rayleigh–Ritz construction and bounds its residual performance. An existing exact complex square-sketch Cauchy law is the \(s=m\) endpoint, but does not determine the oversampled dimension-dependent distributions. The reviewed primary results do not give the complete **real-versus-complex** oversampling moment phase diagram or the sharp mean-square cutoffs. The Gaussian regression calculation itself is classical, so an equivalent result in older statistical or randomized linear algebra literature remains possible. This is a self-review, not an independent novelty certificate.

## Value — PASS
Oversampling is a concrete algorithmic design choice, and changing its size alters moment integrability discontinuously: complex sketches require one additional row and real sketches two to make the identified Ritz value square-integrable. The theorem supplies both complete moment ranges and exact variance constants, rather than a chosen counterexample or a generic concentration estimate. This can inform which moment-based analyses are mathematically permissible for raw sketched eigenvalues. The result does not prove optimal runtime, stability of floating-point QR/SVD, or safety of selecting any reported Ritz root.

## Relationship and limitations
Scientific references: Nian Shao, arXiv:2604.01037v1, §§1 and 4; Nakatsukasa–Tropp, DOI 10.1137/23M1565413, §§6.3–6.6; previously published square-sketch complex Cauchy law for invariant-spectator Ritz pencils. A stronger prior theorem for a different selection/refinement method would need a separate implication comparison. The exact fixed-basis Gaussian hypothesis is essential, and no independent review has been undertaken.

Self-review: passed. Independent audit: not yet performed.
