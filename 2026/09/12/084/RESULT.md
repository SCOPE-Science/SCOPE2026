# Cartan-group corollary of the compact-branch proper-covering theorem

## Statement
Identify the five-dimensional Cartan group C with R^5 as a topological manifold. Let f:C->C be a proper continuous open discrete map (a proper branched covering) with compact branch set. Then f is a homeomorphism. Consequently its Brouwer degree is ±1 (and +1 in the sense-preserving case), so no such map can have degree >1. In particular there is no proper compactly-branched degree>1 quasiregular self-map once openness/discreteness are part of the map class.

## Why this is a corollary, not a new theorem
Kauranen-Luisto-Tengvall, Proposition 4.3, prove in every dimension n>=3 that a proper branched covering B^n -> image with compact branch set is a homeomorphism whenever the image has torsion-free fundamental group at infinity. R^5 has trivial fundamental group at infinity, and the open ball B^5 is homeomorphic to R^5. Their proposition therefore directly covers the topological content needed here and is stronger than the former record's degree-only conclusion.

The earlier self-contained exterior-sheet argument is consistent with this corollary, but the record's claim that the result was not implied by prior literature was incorrect.

## Cartan parameters
The free step-3 rank-2 Cartan group has layer dimensions (2,1,2), topological dimension 5, and homogeneous dimension Q=2+2+6=10. `artifacts/check_numerology.py` checks these numerical facts. The topological corollary uses dimension 5, not Q=10.

## Scope
This statement concerns proper branched coverings. It does not establish that every analytically defined quasiregular map on the step-3 Cartan group is open and discrete; that analytic theorem is not supplied here. Nonproper maps and maps with noncompact branch set are outside the statement.

## Reference
A. Kauranen, R. Luisto and V. Tengvall, *On proper branched coverings and a question of Vuorinen*, Bull. Lond. Math. Soc. 54 (2022), 145-160, Proposition 4.3, doi:10.1112/blms.12565.
