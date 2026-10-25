# Scientific review

The statement concerns the homogeneous scalar all-order simplicial SIS mean-field equation, with strictly positive coefficients, and not finite-population stationary disease distributions.

## Correctness — PASS

The polynomial controlling positive equilibria has exact degree \(M\), and \(k\) asymptotically stable roots require at least \(2k-1\) distinct positive roots. For sharpness, all \(M\) roots can be prescribed inside \((0,1)\) with total below one. The elementary symmetric functions decrease after degree one, forcing every coefficient of the divided difference \((E(y)-E(1))/(y-1)\) to be positive. Taking those coefficients as transmission intensities proves the exact vector field \(-yE(y)\), the alternating signs of simple endemic roots and robust persistence. A standalone exact-rational program verifies 72 finite constructions, including the six-body example. It is corroboration, not an infinite proof.

## Originality — PASS (same-model, subject to literature-priority risk)

The motivating 2023 primary source gives the general ODE and discusses the possibility of arbitrarily many distinct endemic states, but its explicit bifurcation picture reaches only four-body interactions. The 2024 follow-up analyzes up-to-four-body homogeneous models and coupled two-population models; its three-attractor examples involve the latter and do not imply a one-population arbitrary-order sharp capacity/positive-rate realization theorem. The standard polynomial bound is elementary, but the new contribution is the sharp positive-rate realization with explicit all-order group-size design. No directly dominating result was found in the inspected relevant primary texts and targeted mathematical literature. General prior work on root-placement with constrained polynomial coefficients remains a residual priority risk.

## Value — PASS

This exact all-order classification resolves the naturally posed question of how many coexisting attracting endemic states can be sustained by group-mediated infection, and specifies the minimal maximal group size needed to produce a prescribed number of such states. It is robust to small positive-parameter changes, uses all infection orders rather than suppressing rates, and distinguishes high-order effects from multi-population symmetry breaking.

## Closest work and limitations

The closest primary works are arXiv:2309.12752 and arXiv:2410.15330. The result is restricted to single-population deterministic SIS mean-field equations with positive rates. It does not assert a finite-population stochastic stationary multistability result, a global parameter-space bifurcation classification, or originality certified by an independent reviewer.

Self-review: passed. Independent audit: not yet performed.
