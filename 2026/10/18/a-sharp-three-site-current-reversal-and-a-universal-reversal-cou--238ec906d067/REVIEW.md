# Review

## Correctness — PASS

The full claim is proved using the zero-mass row subspace, the inverse of each irreducible reversible generator on that subspace, and the stationary environment-marginal constraint. The decisive nonsingularity proof uses uniqueness of the stationary distribution of the irreducible joint chain. The numerator-degree bound follows from an adjugate of dimension \(n-1\), not numerical root counting. The three-site landscape has exact detailed-balance weights and an independently solved six-state stationary flux \(\kappa(5\kappa-2)/[2(469\kappa^2+1236\kappa+792)]\). The local checker passed 187 exact assertions. The zero-current exceptional case, strict positivity of rates, and \(n\ge3\) boundary are explicit.

## Originality — PASS within inspected literature, with residual risks

The 2003 three-state ratchet uses a single discrete-time landscape and external noise; its null curve does not assert the universal switching-rate root bound for a pair of individually reversible continuous-time landscapes. Zhang's 2010 two-state molecular-motor hopping model gives genuinely broader stationary-current formulas and is acknowledged as such. Its inspected equations do not state or resolve a rate-zero degree bound under individual detailed balance, nor the exact three-site sign-changing witness. Levien–Bressloff's 2015 fast-switching continuum reduction concerns a different approximation regime. Relevant research-record queries found no implication-equivalent theorem; they do not prove uniqueness. A hidden algebraic specialization of older general formulas or differently indexed current-reversal work remains a substantive residual risk.

## Mathematical value — PASS

The root-count theorem gives a cycle-size-dependent algebraic limit on how often switching frequency can reverse transport, under a physically natural detailed-balance assumption that forces each uncoupled environment to carry no current. The exact minimal three-site witness shows a positive switching rate can reverse an emergent nonequilibrium current and that the bound is nonvacuous and sharp at the smallest allowed size. This supplies a meaningful structural constraint beyond merely evaluating a finite-state stationary distribution.

## Closest literature and limitations

Lee et al., *Physical Review Letters* **91**, 220601 (2003); Zhang, arXiv:1007.1745 (2010); Levien and Bressloff, *Physical Review E* **92**, 042129 (2015). No independent audit or exhaustive literature review has been performed. The theorem excludes asymmetric or position-dependent switching, nonreversible individual landscapes, and multi-environment systems; sharpness beyond three sites is not established.

Self-review: passed. Independent audit: not yet performed.
