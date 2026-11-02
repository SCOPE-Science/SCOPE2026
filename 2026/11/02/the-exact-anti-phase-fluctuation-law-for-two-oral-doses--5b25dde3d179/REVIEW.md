# Review of the exact anti-phase fluctuation law for two oral doses

## Correctness — PASS

The domain is the full set of strictly positive absorption and elimination rates, strictly positive fixed dose weights, and positive periods, with phase considered modulo the period. The proof first normalizes the Bateman response and its periodization, then computes the continuous autocorrelation by integrating products of decaying exponentials. A geometric-series identity periodizes the autocorrelation and yields an exact expression for the phase-dependent integrated squared deviation. The positive strict derivative ordering of the ratio of hyperbolic sines proves the unique anti-phase minimizer and monotone phase penalty for all distinct rates. The coincident-rate formula is the exact smooth limit, not a numerically extrapolated assertion. Taylor expansion gives the strictly positive phase-error coefficient. The standalone checker passed 247 direct-quadrature, symmetry, sign, and scaling assertions; numerical checks support but do not replace the proof.

## Originality — PASS within inspected evidence, with limitations

The earliest fully verified day-specific public model source used is Sahin and Benet (2008-11-18), which discusses linear oral absorption and multiple dosing. Plusquellec, De Biasi and Souhait (1999, PMID 10382117) analyze nonuniform repeated dosing in an overlapping two-compartment framework, but their accessible abstract provides only steady-state concentration calculations, not an explicit mean-square phase optimum. The 2008 Sahin–Benet primary full text and 2011 Grover–Benet primary full text address exposure, operational dosing half-life, and peak/trough fluctuation, without giving the claimed integrated-squared two-dose phase penalty. Evans's 2011 accepted manuscript formulates inverse AUC and selected-time-profile dose design through contraction mapping rather than a fixed-positive-dose phase optimum. Searches for exact aliases, Bateman autocorrelation, nonuniform-dose fluctuation variance, and stronger general optimization statements did not produce a statement implying the full theorem. A published general rearrangement or an uninspected portion of the 1999 article might still cover it; priority is not independently certified. The precise assessed claim is the all-positive-parameter strict phase order and explicit exact penalty, including unequal amounts and coincident rates, not the established intuition that more regular dosing reduces fluctuation.

## Value — PASS

Squared steady-state plasma-concentration fluctuation is a natural, dose-normalized pharmacokinetic exposure-variability functional. With the total dose and period held fixed, average exposure cannot distinguish schedules, so a sharp fluctuation criterion answers a motivated remaining question. The exact global penalty and local quadratic sensitivity quantify the cost of deviating from the half-period placement, even when absorption and elimination have disparate or coinciding time scales and the two fixed doses differ. This is a nontrivial complete continuous-parameter scheduling law, rather than an isolated numeric calculation or a generic peak/trough observation. The result is specific to the linear two-stage response and to an integrated square loss; it makes no clinical or nonlinear optimality claim.

## Closest prior sources and residual limitations

- Plusquellec, De Biasi and Souhait (1999), DOI 10.1016/S0939-6411(99)00017-X: highly relevant nonuniform-dose concentration analysis; full text not accessed, so hidden optimization results remain a genuine risk.
- Sahin and Benet (2008), DOI 10.1007/s11095-008-9787-9: full text inspected for the linear repeated-dose model, absorption-sensitive accumulation, peak and trough metrics.
- Evans (2011), DOI 10.1016/j.bspc.2010.06.006: the open accepted manuscript treats inverse AUC and prescribed series targets, not this phase objective.
- Grover and Benet (2011), DOI 10.1007/s10928-011-9198-0: full text treats operational half-life and fluctuation modelling, not an integrated-square global two-dose phase theorem.

Self-review: passed. Independent audit: not yet performed.
