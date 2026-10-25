# Scientific review

## Correctness — PASS

The exact moment matrix follows from the state equation and disturbance independence. Its scalar off-diagonal moment must satisfy Cauchy--Schwarz; for the inverse-trace objective, any nonzero off-diagonal strictly worsens the criterion at fixed diagonal entries. Independent inputs attain every diagonal moment pair, proving no relaxation gap in the causal reduction. The budget is active, the resulting single-variable objective is strictly convex, and its constrained minimizer gives the sharp three regimes. The fixed-input criterion is fractional-linear in second-stage energy, and its full-budget denominator is a strictly convex quadratic in first-stage energy, proving the pure-stage-only deterministic optimum. Unique covariance and the positive cross-moment of every nonzero fixed pair give strict separation. The asymptotic ratio follows from exact endpoint formulas. Exact rational verification passes on the packaged `check.py`; finite checks are not treated as proof.

## Originality — PASS (provisional, with identified literature risk)

The closest complete primary source [1] establishes the general nonlinear covariance optimization framework, but inspected Section 2 (problem definition), Sections 3--4 (Frank--Wolfe and linear oracle), and Appendix 8.1 (moment feasibility) do not give the exact scalar nonlinear optimum or the deterministic-versus-randomized timing gap. The separate earlier explicit scalar **linear oracle** classification does not cover a nonlinear inverse criterion or prove a fixed-input pure-stage optimum. Classical A-optimal information balancing is acknowledged, not represented as new. The Manchester [2] time-domain input-design paper includes a different deterministic design comparison in its abstract; its full text was not reviewed, and equivalent earlier special cases remain a bibliographic risk. Research-record searches for aliases and implications did not return a covering result; search silence is not a novelty proof.

## Mathematical value — PASS

The sharp budget thresholds determine whether it is optimal to excite at the beginning, at the end, or both. In the same elementary dynamical problem, predetermined inputs undergo an entirely different bang-bang switching law. The fully causal advantage is exact, occurs on a mathematically characterized parameter region, and admits unbounded worst-case multiplicative degradation at large input gain. This matters for choosing between fixed experimental signals and randomized/adaptive designs when information accumulation and energy both include the state. It is stronger than merely restating a water-filling calculation and requires genuinely comparing realizable dynamic covariance classes.

## Scientific limitations and closest work

Only two scalar observations, isotropic regularizer and weights, an expected state-plus-input budget, and exact arithmetic are covered. The optimal stochastic design can be achieved by independent random inputs; no superiority over arbitrary deterministic state-feedback is claimed. The general paper's covariance feasibility and A-optimal balancing are prior knowledge; the new contribution is the full specialized dynamical comparison and its sharp consequences. Prior literature on time-domain A-optimal signal design may still contain equivalent special results.

Self-review: passed. Independent audit: not yet performed.
