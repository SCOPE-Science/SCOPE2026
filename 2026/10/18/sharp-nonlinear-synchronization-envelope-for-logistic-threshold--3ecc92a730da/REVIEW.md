# Scientific review of a sharp logistic-network diameter comparison

## Correctness

**PASS.** Row stochasticity and the Dobrushin total-variation coefficient imply the exact range inequality \(\operatorname{diam}(Wx)\le\delta(W)\operatorname{diam}(x)\). The logistic secant is maximized when its two arguments are centered at zero, yielding the nonlinear factor \(\tanh(\beta\delta(W)R/4)\). Almost-everywhere differentiation of active maxima/minima and scalar ODE comparison produce the global diameter bound. The symmetric two-node construction makes each inequality an equality for the entire trajectory. An inverse-square derivative gives the critical limit \(t r(t)^2\to3/2\); strict concavity of the scalar drift gives the unique positive supercritical amplitude. The checker passed 4,000 finite random envelope tests and 1,500 equality checks, plus scalar critical/supercritical diagnostics. Those tests are corroboration only.

## Originality

**PASS on the inspected literature, with residual bibliographic risk.** The motivating full primary text of Boudourides (arXiv:2609.10580v1, Sections 2, 5–7) proves full-state contraction under \(\beta<4\), topology-independent behavior on the homogeneous branch, weakly coupled multistability, and cusp asymptotics. Its Theorem 2.2 does not imply our within-trajectory synchronization criterion \(\beta\delta(W)\le4\) for strong feedback or for arbitrary time-dependent forcing, and it does not establish the sharp nonlinear comparison or critical coefficient. Gaubert–Qu (arXiv:1302.5226, Sections 4 and 6) establishes the classical linear row-diameter coefficient and general nonlinear consensus principles, not the specialized logistic threshold-network envelope or its all-parameter sharpness. Relevant published research records about Thomas rings, confidence systems, and other phase transitions concern different vector fields and do not imply the statement. The classical coefficient and scalar normal form are expressly credited, not claimed new. A broader theorem in older nonlinear consensus literature might subsume parts of the result; independent comprehensive literature evaluation remains outstanding.

## Mathematical value

**PASS.** The result separates agreement of network nodes from uniqueness of the network equilibrium: overlapping stochastic rows force synchrony even in feedback regimes exhibiting scalar bistability. It supplies the optimal state-dependent comparison for every initial diameter, a dimension-independent critical scaling law with exact coefficient, and an explicit obstruction above the same threshold. These statements provide quantitative, verifiable control of synchronization for nonautonomous threshold dynamics rather than merely a restatement of a linear contraction estimate.

## Scope and limitations

The theorem assumes logistic activation, shared external input, nonnegative row stochasticity and time-independent couplings. It does not assert a unique global attractor, robustness to heterogeneous forcing, or full-space stability of the two-node unequal equilibria. Results are supported by an analytical proof and self-review only; no independent mathematical audit has been performed.

## Closest sources

- M. Boudourides, *Collective Hysteresis and Multistability in Threshold Networks*, arXiv:2609.10580v1, https://arxiv.org/abs/2609.10580, first published 2026-09-05.
- S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones, and beyond*, arXiv:1302.5226, https://arxiv.org/abs/1302.5226.

Self-review: passed. Independent audit: not yet performed.
