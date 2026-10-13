# Review

## Correctness
PASS.  In the one-component smooth quadratic specialization, the variance-reduced estimator collapses exactly to the full gradient at the interpolation point.  The inner loop is therefore an affine linear recurrence with a fixed snapshot.  Summing it gives the stated matrix polynomial.  Spectral decomposition reduces the zero question to one scalar equation; in the algorithmic range the relevant branch is positive and unique.  Reparameterizing by \(u=(1-\theta)^{1/m}\) proves the exact root range, and convexity of \((1-q\theta)^m\) proves the no-zero infimum.  The bundled checker replays, but does not replace, these proofs.

## Originality
PASS.  The 2026 MNMPSVRG paper was inspected at Algorithm 1, its general convergence theorem, parameter-sensitivity experiments, and conclusion.  It does not state the quadratic epoch polynomial, one-notch property, or exact one-epoch termination criterion.  The full Katyusha paper was inspected at its negative-momentum mechanism and gives a structurally different multi-sequence method.  Targeted searches using the exact algorithm name, scalar/isotropic quadratics, snapshot interpolation, epoch polynomials, spectral annihilation, and finite termination found no prior result implying the claim.  The closest NMSVRG predecessor is a genuine residual risk because only its abstract and publisher preview were accessible; those materials state convergence-rate results, not this exact finite-termination law.

## Value
PASS.  The source paper reports strong practical sensitivity to the negative-momentum coefficient and explicitly identifies adaptive parameter tuning as future work.  The finding gives a complete calibration law on the canonical local quadratic model: the coefficient creates exactly one movable spectral notch, can solve a condition-number-one quadratic in one epoch precisely beyond the threshold \(m\eta\lambda>1\), and cannot simultaneously cancel two distinct admissible curvatures.  This is a structural explanation of what the single negative-momentum parameter can and cannot tune, rather than a routine recomputation of a convergence rate.

## Closest literature and limitations
Katyusha establishes the broader negative-momentum principle, and NMSVRG is the direct predecessor of MNMPSVRG, but neither accessible statement covers the transfer polynomial or its exact tuning classification.  The claim is deliberately restricted to deterministic quadratics and does not assert stochastic or nonsmooth finite termination.

Self-review: passed. Independent audit: not yet performed.
