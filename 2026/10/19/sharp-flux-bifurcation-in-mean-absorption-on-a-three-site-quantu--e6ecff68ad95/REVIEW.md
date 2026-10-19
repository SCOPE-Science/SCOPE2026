# Scientific review: sharp flux bifurcation in a three-site absorbing quantum ring

## Correctness — PASS

The model is fixed by an explicit Hermitian three-site hopping matrix and a trace-decreasing Lindblad sink. The mean time is the integral of remaining probability, not the discrete-detection return time or half-arrival time. The eigenvalue real-part identity identifies all and only the dark fluxes; it also proves exponential integrability away from them. The provided integrated-survival matrix satisfies all nine Lyapunov equations algebraically, giving the exact lifetime for every parameter. A strictly convex quadratic in reciprocal sine proves the complete optimizer classification, including both equality cases and the merge at the sink/hopping threshold. The standalone checker passed 390 symbolic/numerical assertions. Finite checks are corroboration, not an infinite proof.

## Originality — PASS (same-model, with residual risk)

The most directly related primary study is Wang et al., arXiv:2402.15843, whose full accessible text and appendices were read for the chiral three-site hitting-time and dark-state problem; it uses periodic projective monitoring and does not give the claimed continuous-sink integrated-survival formula. Zimborás et al., arXiv:1208.4049, use chiral quantum walks and Lindblad sinks but evaluate half-arrival/transport probabilities on different networks. Bottarelli et al., arXiv:2302.08472, study a coherent six-site chiral router, not the absorbing three-site lifetime. Existing non-Hermitian ring spectral results imply dark-mode behavior but do not state the integrated survival formula or the all-strength flux optimization. Claim-level published-record and literature comparisons did not identify a stronger statement implying both results. The algebra is susceptible to derivation from standard small-matrix Lyapunov methods, and an equivalent unpublished or differently worded treatment remains possible; this is not independent priority certification.

## Scientific value — PASS

A continuously operating sink is a natural transport observable, and the complete mean lifetime is materially different from the earliest time a target reaches half occupancy. At weak absorption the two optimal fluxes do not maximize chirality; they move continuously toward dark configurations as loss weakens and merge at an exact, physically dimensionless threshold. This is an all-parameter classification rather than an arbitrary finite sample, a normalization check, or a cosmetic reparameterization. It provides a concrete calibration rule and a boundary case for broader dissipative chiral networks.

## Scientific limitations and closest literature

The flux orientation is gauge-fixed explicitly, and conclusions change sign under reversal. Scope excludes disorder, dephasing, non-Markovian sinks, multiple loss channels and different preparations. Closest related literature: Wang et al. (2024), Zimborás et al. (2013), and Bottarelli et al. (2023), all listed with stable identifiers in the result. Literature searches and self-review do not substitute for an independent audit.

Self-review: passed. Independent audit: not yet performed.
