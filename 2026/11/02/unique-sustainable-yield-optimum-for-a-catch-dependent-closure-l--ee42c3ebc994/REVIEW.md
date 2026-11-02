# Review: unique sustainable-yield optimum for catch-dependent closures

## Correctness — PASS

The theorem is stated for the logistic flow with strictly positive growth and capacity, a fixed Schaefer pulse fraction, and the linear closed-season rule with \(0<A=raK<4\). A direct fixed-point calculation yields the exact bijection between persistent effort and dimensionless flight duration \(0<s<W(A)\), as well as the formula for sustainable yield per unit physical time. Strict monotonicity of the one-step biomass map proves existence and global convergence on the persistent range. Its logarithmic yield derivative compares a strictly decreasing rational-exponential expression with the strictly increasing function \(1-e^{-s}\); thus the yield has exactly one global maximum. The positive-root inequality for the optimality equation proves a negative slope derivative of the optimized value, and an independent periodic mass balance proves the strict \(rK/4\) ceiling. Exact symbolic algebra establishes the coefficients of the small-feedback expansion, and rational interval arithmetic brackets a benchmark optimizer. These finite checks are not substitutes for the all-parameter analytic proof.

## Originality — PASS within the inspected evidence

Córdova-Lepe, del Valle and Robledo, arXiv:1110.6413v1 (13 October 2011), Section 5, give exactly the linear closure law and extinction/persistence threshold, while Section 6 expressly identifies optimizing sustainable catch per unit time as an open direction. The present result resolves that optimization in the linear logistic subclass and additionally proves a unique optimum, strict dependence on closure slope, and a sharp quadratic deficit. Bai and Wang (2003) optimize periodic pulse fishing at externally fixed harvest times, rather than feedback-dependent harvest intervals; the previously derived optimal-effort formulas therefore do not imply this theorem. Braverman and Mamdani (2008) prove broad pulse-versus-continuous yield bounds, which agree with the upper bound but do not specify the unique feedback-policy maximizer. Bohner and Streipert (2016) concern a discrete Beverton–Holt model with periodic forcing. Carvalho et al. (2019) address a field-calibrated bioeconomic model for periodically protected areas, with objectives different from the exact feedback clock here. No inspected source proves or implies the full stated result; unseen later work or a more general theorem remains a historical-priority risk.

## Value — PASS

The 2011 founding paper specifically poses the sustainable-yield optimization as an unresolved question. Closing this gap for its explicit, policy-motivated linear closure law is mathematically meaningful because pulse effort changes both the capture and the length of the next closed season. The theorem gives an unambiguous effort decision, proves its global uniqueness rather than a local stationarity condition, and establishes a strict comparative static and the small-feedback price of intermittent harvest. It is not a routine fixed-period substitution or a numerical optimizer; the global proof depends on distinct monotonicity and sign arguments.

## Limitations and closest antecedents

This result covers the autonomous logistic model and the specified harvest-feedback rule only. Convergence is proved in \(0<A<4\), and claims for stronger slope, noise, spatial dynamics, price, and regulatory costs are not made. The original closed-season article's broad nonlinear feedback problem remains open beyond the stated subclass. Literature priority is based on inspected accessible sources, not comprehensive independent certification; the 2016 and 2019 comparisons include abstract/accessible-material limitations.

Self-review: passed. Independent audit: not yet performed.
