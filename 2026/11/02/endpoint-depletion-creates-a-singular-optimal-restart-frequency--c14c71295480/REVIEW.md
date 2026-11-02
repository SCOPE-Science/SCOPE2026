# Review of endpoint-depleted circular Brownian search

## Correctness — PASS

The independent Brownian exit Laplace boundary-value problem has the unique displayed hyperbolic solution. Integrating that solution against a properly normalized beta law gives the fixed-rate renewal mean. Watson asymptotics from the positive endpoint integral establish the exponent trichotomy; an explicit strict hyperbolic inequality proves the otherwise delicate exponent-one boundary. Exact exit-time moments establish the signed local-rate derivative. Uniform differentiated endpoint asymptotics, bounded-minimizer exclusion, and the interior first-order condition establish the singular scale of **every** global minimizer and the optimized-value expansion. These arguments were checked for normalization, endpoint conditions, quantifiers, and the distinction between infimum and attainment. The standalone program passed 103 independently computed finite assertions; numerical tests are not treated as proof of continuous-parameter claims.

## Originality — PASS, best knowledge and limited

Méndez, Flaquer-Galmés and Campos (arXiv:2401.01125v1) already provide a distributional renewal mean formula and resetting examples. Linn and Lawley (arXiv:2302.05409v1) establish the high-frequency first-passage framework. Thus the fixed-rate mean formula and leading high-rate exponent are explicitly credited, **not** independently claimed. The evaluated increment is the joint beta endpoint-shape/global-rate optimization: finite optimal rates just above the critical exponent, sharp divergence of all minimizers as the exponent descends to one, and the logarithmic optimized-value correction. The source Julián-Salgado et al. (arXiv:2605.08414v1) concerns precisely circular resetting with arbitrary reset density, but only its abstract was accessible; this creates real residual priority risk. Full-text portions of the two earlier open-access sources were inspected. Targeted published research-record and primary-literature searches did not reveal a logically covering statement, but search failure is not a uniqueness proof. An unlocated general optimization theorem could imply the result.

## Value — PASS

For physical first-passage search with random spatial resets, the power with which the reset density vanishes at the absorbing target changes the high-frequency optimum from nonattained to finite. The exact shape-to-clock scaling and its logarithmic optimum cost quantify a singular protocol-design boundary. This addresses a motivated optimization problem, beyond recomputing a known renewal formula or a narrow numerical example.

## Limits and independence

Only an absorbing Brownian circle with independent iid beta resets and cost-free Poisson clocks is treated. The existence claim is for exponents just above one; no global uniqueness or classification above the derived finite-optimum interval is claimed. The relevant 2026 paper could not be reviewed in full, so originality is provisional best-knowledge. No independent review or audit has occurred.

Self-review: passed. Independent audit: not yet performed.
