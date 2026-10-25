# Scientific review: exact transient blocking in antagonistic adsorption

## Correctness — PASS

The claim concerns the infinite one-dimensional, equal-rate, repeated-Poisson-attempt model. The cavity survival function is the unique solution of a scalar Volterra equation; the integral relation gives \(g(t)=\exp[-t/2-(1-e^{-t})/2]\). Opposite independent cavity colours and the exact conditional no-arrival probability \(e^{-(T_-+T_+)/2}\) yield \(B(t)=\tfrac12(1-e^{-t})^2e^{-(1-e^{-t})}\). The argument specifies the causal graphical construction, independence, infinite-time vacancy identification, and limiting asymptotic. Direct executable checks support the algebra and finite-time predictions without claiming that finite tests prove the infinite-volume statement.

## Originality — PASS, with priority qualification

The closest paper, Martins–Dickman–Ziff (arXiv:2211.04622, Section V), studies precisely the repeated-attempt process but reports a three-site approximation, simulation, and a conjectural finite-ring saturation expression, not the exact full-time blocked-site formula or a cavity proof. Do Amaral–dos Santos (arXiv:2306.09786) treats a materially different one-attempt rule. General graph deposition references do not directly establish the two-colour exact formula. The numerical saturation value was anticipated and is *not* claimed as a new constant. A differently expressed older renewal solution remains an external scholarly priority risk; failure to find one does not prove uniqueness.

## Scientific value — PASS

The exact time-dependent frozen-vacancy density resolves an observable specifically motivated by prior unsuccessful low-order closure and determines rigorous saturation and approach-to-saturation from the microscopic repeated-attempt process. The one-sided cavity representation explains why a short-cluster approximation is not necessary, supplies an analytic benchmark throughout time, and distinguishes repeated proposals from single-attempt dynamics. This is not a renamed single-site calculation or a mere finite numerical enumeration.

## Limits and reproducibility

Equal A/B rates, the infinite one-dimensional lattice, and nearest-neighbour incompatibility are essential to the evaluated formula. Neither unequal rates nor exact finite-cycle expressions are established. Independent priority or external scientific auditing has not occurred. `check.py` and `check_results.txt` document the actual algebraic checks, exact small-cycle tests, and independent stochastic simulations; sample checks do not replace proof.

Self-review: passed. Independent audit: not yet performed.
