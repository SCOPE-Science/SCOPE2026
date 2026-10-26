# Self-review

## Correctness: PASS

The exact gradient divided difference equals \(\lambda\) on every nonstationary scalar-quadratic step. The cap involution \(C(C(z))=z\), high-to-low necessity, and low-to-high growth inequality lead to a complete one-variable classification. The growth inequality has the unique sharp ratio root of \(r^3-2r/3-1=0\); the specified initialization generates each asserted cycle, and the primal iterate is multiplied by \((1-a)(1-b)\) every two steps. All finite-iteration divided differences remain defined. At interior cycles both cap comparisons are strict, yielding an explicit two-step map and Jacobian spectrum \(\{0,1\}\). The executable's symbolic rational identities and 80-digit checks passed; finite checking is ancillary to proof.

## Originality: PASS (best-knowledge)

The primary paper already derives the active-curvature inverse-square equality in Lemma 5 and proves primal convergence. It does not, in the inspected mathematical results and relevant appendices, give the full sharp two-cycle classification, a genuine initial-stepsize interval, or transverse exact capture. Nearby 2024 proximal research observes cyclic-looking stepsizes but has a nonidentical recurrence. Targeted method-name, quadratic, period-two, and alias searches did not identify a dominating claim. This assessment cannot rule out implicit derivations from the published recurrence or unpublished equivalents.

## Value: PASS

Nonconvergence of adaptively selected steps on an open interval despite geometric primal convergence is a structural algorithmic feature rather than a one-off numerical trajectory. The exact cubic ratio boundary and the neutral/absorbing dynamical geometry answer a natural question prompted by known empirical cycling, and they clarify which state information a stepsize-stability claim can or cannot control. The one-dimensional, exact-arithmetic scope is material.

## Closest literature and limitations

Malitsky and Mishchenko (2023), Algorithm 2 and Lemma 5, supply the method and part of its algebra; Latafat et al. (2024), §4.3, explicitly note empirical cyclic stepsizes for another adaptive proximal update. No global attraction or robustness to rounding, noise, nonscalar curvature, or higher-period states is asserted. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
