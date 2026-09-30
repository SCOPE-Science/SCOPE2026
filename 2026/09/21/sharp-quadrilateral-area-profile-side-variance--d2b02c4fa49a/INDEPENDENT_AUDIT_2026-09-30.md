# Independent audit — 2026-09-30

**Record:** `2026/09/21/sharp-quadrilateral-area-profile-side-variance--d2b02c4fa49a`  
**Repository:** `SCOPE-Science/SCOPE2026` at `253a0fe5d0217455660a277f9adb940030e567ad`  
**Audited tree:** `71e428e25fcda9327bc5a466f3b6bdb934a2d790`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The Brahmagupta substitution y_i=(P/2-a_i)/(P/4) gives sum y_i=4, sum(y_i-1)^2=q and K^2=(P/4)^4 product y_i. For q<4/3 the constraint sphere stays inside (0,2)^4; Lagrange multipliers force at most two coordinate values, and the 1+3 and 2+2 products compare by exact factorizations. Independent symbolic algebra reproduced both product differences and the factorization yielding P^2-16K<=12V. For q>=4/3 the displayed boundary family has a zero coordinate and the prescribed moment, so the infimum is zero. Equality/sharpness and the q=4/3 transition are consistent.

## Originality

**PASS (literature-bounded).** Giugiuc--Oai--Altintas (2018) gives the adjacent maximum-product/area inequality and the opposite deficit estimate, not the fixed-variance minimum-product profile or the reverse constant 12. Targeted searches for the exact equivalent formulas and side-variance phrasing did not locate an earlier statement. The contribution therefore survives as literature-bounded originality, with residual risk from older geometric-inequality or symmetric-polynomial formulations.

## Scientific value

**PASS.** The record completes the opposite side of a natural fixed-perimeter/fixed-side-variance cyclic-quadrilateral problem, identifies the unique pre-threshold extremizer and degeneracy threshold, and yields a sharp global reverse stability inequality that pairs with the known opposite bound.

## Literature and evidence

- Giugiuc, Oai, Altintas, An inequality related to the lengths and area of a convex quadrilateral: https://www.researchgate.net/publication/344429273_AN_INEQUALITY_RELATED_TO_THE_LENGTHS_AND_AREA_OF_A_CONVEX_QUADRILATERAL
- Indrei and Nurbekyan, On the stability of the polygonal isoperimetric inequality: https://doi.org/10.1016/j.aim.2015.02.013
- Indrei, A sharp lower bound on the polygonal isoperimetric deficit: https://doi.org/10.1090/proc/12947

## Limitations

- Only nondegenerate convex cyclic Euclidean quadrilaterals are covered.
- For q>=4/3 the minimum is only a degenerate-boundary infimum.
- Equivalent older inequality formulations remain a residual priority risk.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
