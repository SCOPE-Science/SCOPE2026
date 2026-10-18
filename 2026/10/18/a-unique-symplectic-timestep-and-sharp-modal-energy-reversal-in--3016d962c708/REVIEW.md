# Scientific assessment

## Correctness — PASS

The four stage vectors have exact determinant \(h^6\omega_1^3\omega_2^3(\omega_2^2-\omega_1^2)^2E_1E_2/32\), forcing the projected gradient to equal the full RK4 predictor for two excited modes. The minimum-norm correction is therefore radial, with no singularity because the RK4 imaginary-axis polynomial has positive squared modulus. Exact action ratios follow by cancellation of the common normalization. Their sign changes once at the explicit positive threshold. An action-angle Jacobian strictly below one at equal actions unless the modal attenuation factors match excludes symplecticity away from that threshold. At equality, the map is a fixed orthogonal block rotation, proving the converse. Exact symbolic computation and direct stage comparisons were replayed; no infinite conclusion depends upon finite numerical tests.

## Originality — PASS, with residual uncertainty

The full text of the introducing September 2024 work was inspected through its projection definitions, solvability theorems, oscillator experiments, and discussion. It provides the method and its reduction to orthogonal projection when stages span the state space, not the exact two-frequency threshold or unique symplecticity characterization. The earlier 2020 Jiang–Gong–Wang orthogonal energy projection is a more general predecessor of the *algorithm itself*, fully acknowledged; its conservation/order statements do not imply the reported action-by-action switching threshold and symplecticity iff condition. Relevant mathematical-record searches and earlier scientific claims were compared by mathematical implication: a quasi-orthogonal explicit-midpoint single-oscillator solvability theorem and a different two-stage RK energy-cascade theorem do not imply this RK4 symplectic resonance. Specialized projection-method literature might already express an equivalent crossover under alternate language, so absolute novelty is not certified.

## Value — PASS

The source method explicitly aims to conserve numerical invariants. This exact two-mode benchmark demonstrates a failure not detected by conserving the total quadratic invariant: inexorable transfer of the *entire* conserved energy to one oscillator, even when classical RK4 is linearly stable for both, and an isolated positive step where the same projected RK4 map unexpectedly becomes symplectic and preserves both original actions. This identifies a concrete internal-stability region in which energy conservation does not imply modal fidelity, with exact sharp parameter selection. It is a four-dimensional benchmark rather than a general structural theorem for arbitrary nonlinear systems.

## Closest work and remaining risks

Najafian–Vermeire (2024) already defines quasi-orthogonal gradient-stage projection and the saturated-stage reduction; Jiang–Gong–Wang (2020) already defines radial energy projection. Neither source claims the present exact modal crossover and iff symplecticity criterion in the inspected material. The published oscillator-energy cascade with relaxation-free SSPRK(2,2) is algorithmically different and lacks a globally defined fixed-energy projection or a positive symplectic balancing step. Residual risk: an equivalent exact frequency-selective amplification analysis could exist in earlier orthogonal-projection/postprocessing work not retrieved by the checked searches.

Self-review: passed. Independent audit: not yet performed.
