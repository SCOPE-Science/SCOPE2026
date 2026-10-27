# Scientific review — Exact critical relaxation and logarithmic signatures in a payoff-reversal evolutionary game

## Correctness — PASS

The payoff-matrix reconstruction, all three equilibrium derivatives, and the two scalar substitutions were checked directly. On their strictly specified one-sided attracting basins, monotonicity and exact reciprocal-coordinate integrals prove the claimed all-time implicit formulas and the sharp infinite-time expansions. In particular, the endpoint reciprocal state has a nonzero \( -3\log(ct) \) contribution, whereas the interior reciprocal state has no logarithmic term. The frozen state and repelling/other basins are not incorrectly assigned a critical relaxation law. `check_critical.py` reported 12,859 checks. The proof, rather than the finite checks, establishes the universal conclusions.

## Originality — PASS, with limitations

Chen, Zhang, and Li, arXiv:2610.21575 (2026), derive the same vector field, its equilibria, and bifurcation thresholds, and discuss the degenerate \(S=P\) case. Their full accessible mathematical text was compared with the proposed exact quadratures and logarithmic dichotomy: those sharper time laws are not stated there. Ito and Yamamichi (2024, DOI:10.1093/pnasnexus/pgae455) analyze a different feedback game with an independent environmental state. Targeted exact-equation, alias, and broad critical-relaxation searches did not identify stronger equivalent coverage in inspected sources. This is not a proof of publication priority. An unindexed scalar-ODE normal-form study remains a risk.

## Mathematical value — PASS

The payoff thresholds are natural boundaries at which eigenvalue-based convergence estimates fail. The derived complete explicit time laws give the leading coefficient, the initial-condition-dependent phase, and—only at the endpoint—the sharp nonzero logarithmic drift. This distinguishes otherwise similar critical cooperation thresholds, provides testable transient predictions, and treats the source's special degenerate endpoint line. Standard one-variable integration underlies the proof; novelty and value are specifically the exhaustive model-level critical signature, not a new general existence method.

## Scope and residual risk

All parameters are real constants and all claimed attracting rates require the sign and open initial interval specified in RESULT.md. Nothing is established here for spatial, random, discrete, or delayed versions of the game. As in any literature-priority assessment, relevant nonindexed work may have been missed.

Self-review: passed. Independent audit: not yet performed.
