# Scientific assessment

## Correctness — PASS

The theorem is reconstructed independently from the backward two-piece permeable-interface boundary-value problem. Matching the interface flux and the backward jump condition gives the no-reset transform, which is checked against Kay–Giuggioli (2022), Eq. (11). Global Poisson reset creates an iid-attempt renewal law. A dimensionless exact mean follows by algebra. The entire parameter domain is covered analytically: strict convexity follows from the displayed integral and sum-of-squares formulas for the second derivative; coercivity forces a unique positive optimum; implicit differentiation proves the strict increase–decrease split and unique midpoint maximum. The envelope theorem proves strict decrease of the minimized mean with membrane position. The packaged standard-library numerical checker passed 1,461 deterministic tests, but those are corroboration, not infinite-parameter proof. Parameter boundaries and the screened-reset exception are explicitly excluded.

## Originality — PASS, with stated residual risks

Kay and Giuggioli (2022) derive the membrane first-passage transform without any resetting; their transform is used as a known premise, not claimed. Bressloff's 2022–2023 screened-target resetting article (Secs. 2–5) explicitly prohibits resets inside the interface and reports that its optimal rate shifts toward larger rates as the barrier moves outward; this does not imply the global-reset midpoint maximum. His 2022–2023 membrane-renewal paper (Sec. 3) also explicitly forbids cross-membrane resetting, focusing on nonequilibrium stationary densities and relaxation rather than absorption optimization. The classical scalar renewal formula alone lacks the nontrivial location derivative; it must be combined with the precise transform and strict convexity. Search of directly relevant published literature and mathematical research records did not uncover an equivalent result or a more general theorem supplying this universal location law. There remains a genuine risk of unrecognized coverage by a general stochastic-restart comparison theorem, and a 2025 moving-barrier paper was not fully inspected. Absence of a match is not proof of exhaustive novelty.

## Value — PASS

This is a physically interpretable design rule, not merely an alternative formula for an already-known mean. For every finite membrane resistance, the reset frequency optimal for absorption is highest at an exact parameter-independent spatial midpoint, even though changing the membrane position improves the search time monotonically. The disagreement between optimization of the control and improvement of the objective is non-obvious and can inform protocols that combine environmental permeability with external relocation. The full location-dependent phase diagram follows for all positive parameter values, not for a narrowly tuned example. No claim is made of a downstream experimental demonstration.

## Closest sources and limitations

Kay–Giuggioli, *Phys. Rev. Research* **4** L032039 (2022), Eq. 11; Bressloff, arXiv:2211.12468, Secs. 2–5; Bressloff, arXiv:2209.09176, Sec. 3. The single-interface, perfectly absorbing, spatially uniform diffusion and globally allowed reset assumptions are essential. Universal midpoint location is not asserted for screened, non-Poisson, or partial resetting.

Self-review: passed. Independent audit: not yet performed.
