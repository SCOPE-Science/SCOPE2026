# Scientific review

## Correctness — PASS

The exact SSPRK(2,2) stage update is \(u_j^+=(1-br_j)u_j+h\omega_jJu_j\). Orthogonality gives the quadratic \(Vb^2-2Ub+U=0\), whose discriminant makes the one-step feasibility criterion necessary and sufficient. The same equation gives the exact modal gain \(1+b^2r_j(r_j-\mu)\). If any active mode has \(r_*>1\), its energy increases by at least a fixed positive factor on every feasible step, contradicting bounded conserved total energy after finitely many steps. All quantifiers and the repeated-root boundary are covered. Exact rational verification of the two-step witness and further independent numerical consistency tests pass.

## Originality — PASS (best-knowledge, residual risk remains)

Najafian–Vermeire (arXiv:2401.14508v1) already provide the fixed-step RF-RK method, its scalar quadratic and local solvability, and an empirical warning about missing real roots. The assessed claim instead concerns sharp **all-step solvability versus inevitable finite-step breakdown** at an active spectral threshold, the sharp two-mode initial-energy frontier, and an exact one-successful-step obstruction. Ketcheson's arXiv:1905.09847 rescales the full step and changes effective time, rather than using the same zero-sum stage perturbation. The later arXiv:2409.18328 chooses a quasi-orthogonal projection direction, not the fixed one. Exact all-step loss for the specified method was not identified in the relevant primary literature or searches. A differently phrased prior analysis of stage-weight corrections remains possible.

## Value — PASS

The theorem separates a successful conservative step from the existence of an indefinite conservative numerical trajectory. The sharp condition \(h\omega_{\max}\le1\), its dependence only on the **active** spectrum, and the boundary for a small initially present high-frequency component identify when a method can be forced to stop despite exact conservation at every prior step. The numerical consequence is intrinsic to fixed-step scalar correction, not to roundoff or nonlinear stiffness. The result is not a generic criticism of energy conservation or a claim about unrelated projection methods.

## Scientific limitations

This exact theorem applies only to the explicitly stated SSPRK(2,2) RF-RK coefficients, finite collections of independent positive-frequency planar rotations, one shared real correction parameter, and constant positive base step. The conserved invariant is total squared Euclidean norm; the exact flow conserves each modal norm. Mode-dependent corrections, other stage weights, and adaptive step changes are excluded. Originality is best-knowledge rather than an independent literature certification.

Self-review: passed. Independent audit: not yet performed.
