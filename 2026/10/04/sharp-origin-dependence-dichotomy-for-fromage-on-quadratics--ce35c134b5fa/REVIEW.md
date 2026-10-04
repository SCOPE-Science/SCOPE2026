# Review

## Correctness

PASS. Expanding the exact Fromage update reduces its squared norm ratio to one minus a scalar multiple of the angle cosine \(x^\top Hx/(\|x\|\|Hx\|)\). The sharp lower bound \(2\sqrt{\mu L}/(\mu+L)\) follows from the eigenvalue inequality \(\lambda^2+\mu L\le(\mu+L)\lambda\) and arithmetic-geometric mean, with equality on a two-eigenvalue witness. This proves the exact centered factor, its unconditional contraction for every positive finite learning rate, and the unique optimum at \(\eta=1\). Removing the prefactor gives the exact LARS-type comparison. For the shifted scalar objective, the official update becomes a two-branch multiplicative map; the invariant interval and logarithmic rigid-rotation conjugacy are exact.

Risk: the square-root statement is a sharp repeated one-step guarantee, not a lower bound on every trajectory's asymptotic convergence rate.

## Originality

PASS. The defining Fromage paper explains the norm-ratio update and introduces the \((1+\eta^2)^{-1/2}\) prefactor to correct relative norm growth, but the inspected text does not derive a sharp SPD-quadratic condition-number law. Earlier proportional-update analysis already shows qualitative fixed-rate nonconvergence on shifted one-dimensional objectives, so that phenomenon is treated as prior coverage rather than novelty. The surviving claim is the exact effect of the Fromage prefactor: unconditional centered SPD contraction, the sharp \(1-\Theta(\kappa^{-1/2})\) one-step bound, the exact LARS comparison, and the prefactored log-rotation boundary.

Focused searches over Fromage, LARS, proportional updates, normalized gradients, centered quadratics, condition numbers, and shifted scalar dynamics found no inspected source stating or implying the complete claim.

## Value

PASS. Fromage's defining distinction from LARS is precisely its normalization prefactor. The theorem quantifies that design choice on the canonical SPD quadratic class: it removes the proportional update's finite stability ceiling and improves the best sharp centered one-step condition-number scaling from \(1-\Theta(\kappa^{-1})\) to \(1-\Theta(\kappa^{-1/2})\). The shifted example simultaneously identifies the limitation that makes this possible—the update is relative to the origin rather than translation invariant. This provides both a positive benchmark and a sharp caution for interpreting Fromage as a general quadratic optimizer.

Same-model review: passed. Independent audit: not yet performed.
