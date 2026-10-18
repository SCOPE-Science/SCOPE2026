# Self-review

## Correctness — PASS

The proof follows all characteristic cohorts for one full maturation interval. Logistic comparison gives the deterministic uniform prey ceiling \(L\); the original predator fecundity satisfies \(B(x,z)\le Kx\); the starvation term provides mortality lower bound \(m\); global boundedness of age-specific mortality gives upper bound \(M\). The integrating characteristic then gives \(y_2(t)\ge e^{-(M+KL)T}P(t)\). With \(q=bc/(2K)\), differentiation of \(x+qP\) cancels half the mixed term and gives \(V'\le(C+m)L-mV\). All constants are positive on the stated parameter domain and the initial transient is controlled by Gronwall. This proves global existence and an eventual initial-data-independent \(L^1\) bound. Verified the algebra using the embedded finite-rational and parameter-grid checker. The finite checks are not used as infinite proof.

## Originality — PASS, with risks

The motivating source's Sections 2 and 7 concern the same age-dependent rates. They discuss numerical runaway and propose two simultaneous saturations. The new theorem assumes only the prey-benefit saturation and retains linearly prey-dependent adult fecundity, so the result is neither a direct application of both proposed modifications nor a logical special case of the two-sided capped theorem. The accessible related literature on delayed age-structured predator–prey systems has different population regulation and does not explicitly imply this one-sided-cap result. Prior published records and original research titles/claims were compared for adult-cohort coercivity and equivalent saturation thresholds; none identified an implication. General nonlinear semigroup/renewal dissipativity results might subsume portions; that remains a residual risk.

## Value — PASS

The mathematical question is motivated by the original model's mutually reinforcing growth mechanism and its proposed need to regulate both species' reproductive responses. Showing that exactly one regulatory saturation is sufficient for the full age-structured PDE–ODE system, with no restrictions on benefit/predation ratios, removes a biologically significant modeling intervention and gives a global quantitative guarantee in a setting with delayed maturation. The new survival-to-adulthood estimate is the crucial structural mechanism, not a finite-parameter numerical observation.

## Closest literature and limitations

Suarez et al., arXiv:2502.19748v1 and DOI:10.1007/s00285-026-02402-5, Sections 2–3, 7, appendix: exact original renewal rates, local theory, numerical blowup cases, and proposed dual saturation. Cai et al., DOI:10.1155/2007/54861, population estimates for a different age-structured prey/delayed predator model. An age-stage Gurtin–MacCamy reduction record concerns a bistable scalar renewal population rather than reciprocal role-reversal interactions. Earlier original research records on this same Suarez model concern invasion frontiers around predator-free equilibria, not ultimate boundedness.

The guarantee requires uniformly bounded age-based background mortality. It does not resolve the model with an unbounded age-mortality profile and does not assert that arbitrary initial data approach equilibrium. Unindexed stronger general theorems remain a literature risk.

Self-review: passed. Independent audit: not yet performed.
