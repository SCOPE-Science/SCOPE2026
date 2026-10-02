# Independent audit — 2026-10-01

**Record:** Curvature-distortion numbers of spider trees  
**Disposition:** passed

## Correctness — PASS

The tree fixed-point equation forces pendant weights to one. Along each spider arm, every internal zero-curvature equation makes consecutive weights geometric. Writing the center weighted degree as s reduces the entire system to one strictly monotone scalar equation; this reconstructs the canonical fixed point and the distortion. Monotonicity of the arm ratio gives the sharp fixed-(d,L) minimum and maximum, with uniform subdivision attaining \((d-1)^{L-1}\) and the one-long-arm spider attaining \((d-1)^{(L-1)/L}\). The supplied 660-case computation is consistent with, but not a substitute for, this proof.

## Originality — PASS

Neither implies the exact formulas for arbitrary arm lengths and mixed spiders.

Equivalent-formulation search: The all-spider scalar reduction and fixed-(d,L) extremal classification were not found in the source or archive.

Broader-coverage search: A general implicit fixed-point theorem does not mechanically state the explicit scalar solution or the sharp extremal range; the audited derivation is a nontrivial specialization and classification.

Exact-database/table check: The theorem is infinite-family structural mathematics, not a finite census.

## Scientific value — PASS

Spiders are a canonical branching family for a new tree invariant. The result gives an exact solvable model and quantifies sharply how uniform subdivision amplifies the distortion, providing a natural benchmark for the general fixed-point theory.

## Source inspections

- https://arxiv.org/abs/2609.12125: Complete primary paper inspected through the fixed-point theorem and examples. It proves the tree fixed-point characterization and gives double-star and three-center examples; it does not state the all-spider scalar equation, geometric arm profile, or sharp fixed-(d,L) extremal range.

## Residual risks

- The result concerns spider trees only.
- The invariant itself is very recent, so contemporaneous overlap remains possible.
