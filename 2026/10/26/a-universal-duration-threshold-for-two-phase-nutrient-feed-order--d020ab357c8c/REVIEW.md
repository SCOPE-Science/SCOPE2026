# Scientific review

## Correctness — PASS

The exact linear reservoir solution yields a substrate-order difference with exactly one temporal sign change. The Monod rate-difference factorizes into that sign-changing difference times a positive initial-state-dependent weight. The ratio of weights for two increasing initial nutrient levels is strictly time-increasing; a single-crossing comparison then proves that the integrated difference can have at most one zero, crossing from positive to negative. Direct paired-time algebra establishes strict positivity at zero initial nutrient. The large-initial-substrate moment is computed exactly as \(\Delta(E-1)^2(1+2E-E^2)/(2D)\), where \(E=e^{D\tau}\); the same weight-ratio argument covers the equality boundary. The embedded program independently checks the explicit integrals and illustrative root. Scope includes all \(D,K,m,\tau>0\), \(0\le\ell<h\), \(s\ge0\), and finite endpoints; it does not claim biomass-feedback dynamics.

## Originality — PASS with residual risk

Hsu (1980) directly provides periodic nutrient and saturating chemostat kinetics but studies coexistence/competitive exclusion under sinusoidal input, not this finite two-order comparison. Butler–Hsu–Waltman (1985) treats time-varying dilution and periodic coexistence. The accessible Stephanopoulos–Frederickson–Aris (1979) abstract concerns Floquet stability under periodic forcing including variable input; its uninspected full text could contain an equivalent comparison. Smith (1981) also concerns coexistence in oscillating environments. Exact equations and implications—not merely titles—were compared. No inspected source derives the universal threshold \(\log(1+\sqrt2)\) or a unique initial-nutrient sign reversal for equal-duration two-block Monod feed ordering. A more general variation-diminishing or rearrangement theorem may imply it; this is recorded as a risk, not excluded by keyword searches. Related published mathematical results concern different reactor thresholds and long-run averages. Independent literature validation remains undone.

## Mathematical value — PASS

The direction of finite-time rare-invasion amplification is a motivated experimental question when the same feed doses are scheduled in opposite orders. The exact, dimensionless transition is surprisingly independent of feed concentrations, Monod saturation and maximum growth, and the theorem identifies the complete positive-initial-substrate ranking including the otherwise delicate equality boundary. The high-initial-substrate reversal is not visible from comparing endpoint nutrient stocks, which always favor late feeding; hence this is a structural finite-horizon classification, not a routine evaluation of one integral.

## Closest literature and limits

Hsu (1980), doi:10.1007/BF00275917; Butler–Hsu–Waltman (1985), doi:10.1137/0145025; Stephanopoulos–Frederickson–Aris (1979), doi:10.1002/aic.690250515; Smith (1981), doi:10.1137/0140042. Full texts inspected for the first two; latter two inspected at abstract level only. The nonlinear system, unequal-duration switching, arbitrary control orderings and asymptotic coexistence are unproved. The exact public-release day for the 1980 motivating article is not independently established beyond a bibliographic database field.

Self-review: passed. Independent audit: not yet performed.
