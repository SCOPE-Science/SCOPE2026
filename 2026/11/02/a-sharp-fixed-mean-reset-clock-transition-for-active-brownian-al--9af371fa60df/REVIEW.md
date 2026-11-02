# Scientific review of the renewal-clock alignment theorem

## Correctness

**PASS.** The stochastic dynamics and reset independence give the unreset mean response \(F(t)\) exactly. The renewal-reward identity for positive finite-mean clocks is applicable because the cycle's absolute reward has finite expectation. The response has one turning point, implying a unique tangency and a pointwise concave majorant of its integrated reward. Jensen's inequality and the explicit approximating two-atom law prove the complete sharp optimization including equality and nonattainment. The Poisson formula and resonant limit follow by direct integration. The standalone script independently checks 2,390 finite/symbolic consequences. Those diagnostics do not substitute for the universal proof.

## Originality

**PASS, with residual priority risk.** Shee (2024, arXiv:2409.06920v1) gives the Poisson active Brownian mean and its rate optimum, but not the fixed-mean optimization over all renewal clocks. Eule and Metzger (2016) give a general renewal-resetting theory and restricted-family constrained search comparisons, not this explicit full-position/heading-reset alignment frontier. Guéneau, Majumdar and Schehr (2023) reset the *driving noise* rather than the particle's full state and compare periodic and Poisson noise protocols, not this optimization. Accessible mathematical research records on fixed-mean quantum detection and renewal first passage have distinct reward objectives and hypotheses. The concave-envelope method itself is standard, and an unindexed general optimal-renewal-control theorem could subsume some or all of the phase classification; independently established publication priority is not claimed.

## Mathematical value

**PASS.** The source model explicitly studies maximizing mean displacement by Poisson rate selection. Under the natural constraint of fixed mean reset expenditure, the answer is a complete, analytically sharp protocol classification, including a nonattained low-mean plateau, a deterministic high-mean optimizer, and a strict universal improvement over optimized Poisson resetting. The matched-timescale benchmark quantifies a nontrivial \(19.37\%\) performance gap. This is a motivated control question rather than a chosen arbitrary invariant.

## Scientific limitations

Only long-run signed alignment is optimized. Renewal clocks are exogenous, independent, i.i.d., and have positive finite mean; position and heading are reset together at zero duration and zero overhead. Phase-resolved deterministic cycling is not claimed to converge to a time-independent distribution. General heuristic optimal-control methods and inaccessible or unindexed specialized work remain priority risks. Numerical diagnostics are finite and cannot prove uniqueness or global optimality by themselves.

Self-review: passed. Independent audit: not yet performed.
