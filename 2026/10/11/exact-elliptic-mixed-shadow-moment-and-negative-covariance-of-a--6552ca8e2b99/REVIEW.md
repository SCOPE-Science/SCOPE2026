# Review of exact elliptic mixed shadow moment

## Correctness — PASS
The face-normal and projected-edge formulas are independently derived for a unit regular tetrahedron. Spherical symmetry reduces the mixed moment to a one-dimensional integral; an explicit change of variables yields the Legendre incomplete elliptic integrals. The first moments follow from independent spherical averaging. The strict negative covariance is proved by a finite Taylor expansion with uniform alternating remainder, rational interval arithmetic, and exact angle identities. The standalone verifier checks the interval certificate and independently compares 400 projected convex hulls; these checks supplement the analytic derivation. The scope is all uniformly random directions, not a sample of directions.

## Originality — PASS, with residual risk
The closest primary source is Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, §2.1: it contains the previously known numerical mixed value and negative correlation, and records a missing closed form for the mixed area–perimeter expectation. The proposed exact incomplete-elliptic formula and rational proof of sign are not stated there. Dirksen's arXiv:1509.06408 treats simplex sections, not the mixed projection invariant. Semantic database searches for mixed moments, elliptic forms, and tetrahedral projections yielded adjacent geometry but no implication of the exact formula. Earlier hidden equivalent evaluations could exist and are an explicit residual risk; lack of a search result alone is not a novelty proof.

## Value — PASS
An exact evaluative gap was expressly identified for a classical random-shadow invariant. The result determines the missing mixed moment using standard special functions and upgrades an observed negative correlation to a rigorous inequality with a reproducible rational certificate. This addresses a geometrically motivated joint statistic rather than an arbitrary isolated numerical constant.

## Limitations
The result does not supply the complete joint law, higher mixed moments, an elementary expression, or a uniform theorem for all simplices. The quoted long decimal is diagnostic only. Scientific review is not independent external validation.

Same-model review: passed. Independent audit: not yet performed.
