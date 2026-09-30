# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-shortest-edge-volume-profile-for-simplices--3184b81bbe2a`  
**Audited repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `f7af44f641b81f5179e114c45db2d43d3b006fc5`  
**Disposition:** **PASSED**

## Correctness — PASS

After centering the distinguished edge, the determinant factorization n!Vol=s|det Y| is exact. The endpoint and diameter constraints imply ||y_i||^2<=D^2-s^2/4 and ||y_i-y_j||<=D. The positive weighted frame operator S=YQY^T has the stated trace bound; Q=αI+β(mI-J) has determinant α(α+mβ)^(m-1), and eigenvalue AM–GM gives the displayed determinant/volume bound. Equality forces every transverse norm and pair distance to saturate, hence all nondistinguished edges have length D; conversely G0=αI+βJ is positive definite and realizes equality. Differentiating the normalized profile confirms strict monotonicity, and solving the quadratic in μ^2 gives the inverse law. The n=2 and s=D limits reduce to the isosceles-triangle and regular-simplex formulas.

## Originality — PASS (literature-bounded)

Classical largest-small-polytope sources cover the diameter-constrained regular-simplex setting, and recent frame/simplex work gives aggregate edge-volume inequalities. Targeted searches for a prescribed distinguished edge, shortest-edge/diameter ratio, one-short-edge equality family and the exact inverse profile did not locate this theorem or a stronger statement implying all of it. Because the proof is elementary distance geometry plus a determinant inequality, an older folklore/mesh-quality formulation remains plausible.

## Scientific value — PASS

The result supplies a complete sharp one-parameter refinement of the regular-simplex diameter extremum, including a unique equality family and a best-possible inverse edge-regularity law from volume. That is a useful quantitative shape-control statement rather than merely another upper bound.

## Evidence and literature

- Graham, The Largest Small Hexagon (1975): https://doi.org/10.1016/0097-3165(75)90004-7
- Kind and Kleinschmidt, On the Maximal Volume of Convex Bodies with Few Vertices (1976): https://doi.org/10.1016/0097-3165(76)90056-X
- Fejes Tóth, Finite variations on the isoperimetric problem: https://arxiv.org/abs/2202.09920
- Ledford, Rivera-Ayala, Schroeder, A note concerning frames and geometric inequalities: https://arxiv.org/abs/2509.05611

## Limitations

- The theorem is Euclidean and simplex-specific, and it controls edge lengths rather than stronger shape distances.
- Only one prescribed edge is optimized explicitly; simultaneous multiple-short-edge constraints are not treated.
- Older distance-geometry or mesh-quality folklore is the main residual originality risk.

The independent audit finds the record scientifically complete on all three axes at the audited tree. The literature verdict is bounded by the sources and searches explicitly described above; it is not inferred merely from failure to find a match.
