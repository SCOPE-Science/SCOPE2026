# Scientific review: universal sign-flip Floquet instability of dissipative gradient descent-ascent

## Correctness — PASS

The theorem is quantified over every dimension \(d\ge1\), every invertible real square bilinear coupling, every \(0<\rho<1\), every \(\eta>0\), and every nonzero primary start with synchronized auxiliary variables. The source DGDA update gives exactly \(B_- = B_+^{\mathsf T}\) under alternating payoff signs, so the two-step matrix is the Gram matrix \(B_+^{\mathsf T}B_+\). On singular modes, the exact trace and determinant of the \(2\times2\) Hermitian period block are calculated in RESULT.md. The identity \(\det(I-Q)=-\rho(2-\rho)t^2<0\), together with positive determinant, proves one strictly expanding and one strictly contracting eigenvalue for all allowed parameters.

The nontrivial initialization issue is addressed rather than inferred from an unstable spectral radius alone: synchronized nonzero modal states have period Rayleigh quotient \(1+t^2/2>1\), hence nonzero projection onto the expanding eigenvector. Its primary coordinate is nonzero because the block off-diagonal is nonzero. Orthogonality across singular modes prevents cancellation of the growing primary norm. Exact symbolic identities and a direct numerical assembly of \(240\) real period maps passed the standalone verifier; only the analytic derivation supports the infinite assertion. The stable-frozen example was checked from the exact characteristic roots.

## Originality — PASS (best-knowledge, not independent certification)

The nearest direct methodological source, Zheng et al., arXiv:2403.09090v1, derives the identical augmented DGDA update and shows linear convergence for fixed bilinear matrices. Its proof and appendix treat a single fixed iteration matrix, not a two-period sign-reversing payoff. Feng et al., arXiv:2310.02604, prove divergence for optimistic GDA and negative momentum in a periodic bilinear game, including a rectangular rank-deficient payoff and certain initial conditions. Their results are the closest conceptual precedent and already establish the general *possibility* of periodic-game divergence.

An especially important algebraic overlap is explicit: at \(\rho=1/2\), elimination of the auxiliary variables converts DGDA into optimistic GDA with half the source step. Accordingly, the special case's qualitative failure is not claimed as a separate discovery. The assessed content is the exact *all* \(0<\rho<1\) DGDA stability obstruction, full singular-mode Floquet spectrum, and the theorem that **every nonzero synchronized primary start diverges** for **every invertible square** coupling. Fiez et al., arXiv:2111.03377, analyze continuous-time GDA recurrence, not this discrete dissipative scheme. Exact claim/implication comparisons and remaining risks appear in AUDIT.json.

A possible unindexed reformulation in switched-system or time-varying game literature is a residual originality risk. A search finding no duplicate is not a proof of uniqueness.

## Value — PASS

For a published algorithm designed to dissipate bilinear saddle rotations, the theorem gives a mathematically sharp and counterintuitive limitation: no amount of positive damping in the prescribed interval and no positive stepsize, however small, suppresses two-period sign-reversal instability. It is structural across all dimensions and all invertible couplings, not a tuned single numerical example. Exact modal multipliers give quantitative growth rates. Moreover, a concrete choice has two separately Schur-stable frozen games whose alternating execution diverges, making clear why autonomous convergence analyses cannot simply be transferred to periodic games.

The result does not imply all time-varying DGDA problems fail, all arbitrary augmented initializations diverge, or that the earlier optimistic-gradient phenomenon was previously unknown. The exact simultaneous update, synchronized starts, fixed parameters, and sign-flipped bilinear objectives are essential limitations.

Self-review: passed. Independent audit: not yet performed.
