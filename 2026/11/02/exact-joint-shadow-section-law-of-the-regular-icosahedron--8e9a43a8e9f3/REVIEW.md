# Review of the cooriented icosahedral shadow–section law

## Correctness — PASS

The coordinate model has 12 vertices, 20 triangular facets, 30 original edges and 30 dual edges. The section count is the cut size on original-vertex signs, and the shadow count is the cut size on adjacent-facet-normal signs. Each arrangement is in general position (6 or 10 distinct great circles, respectively), so its chambers and all extreme rays can be exhaustively enumerated from pairwise crosses. The exact `verify.py` checker establishes the 32/92 chamber counts, the 20/12 section and 20/60/12 shadow type splits, and, most decisively, all twenty extreme-ray cone-inclusion statements and four exact rational interior witnesses. Girard's spherical area formula and exact angle signatures yield the joint law after subtraction. Independently, the crossing-angle mean identities check normalizations. No random experiment or finite sampling is used to infer a universal statement.

## Originality — PASS, provisional historical priority

The icosahedron section *marginal* is already given in *Exact Haar polygon-type law for central icosahedron sections*, and the shadow marginal is the polar of an earlier exact regular-dodecahedron central-section marginal. Neither is claimed as a contribution. Black–Criado's 2024 paper concerns general random-shadow estimates; Böröczky–Henk and Kabluchko–Seidel treat other regular-polytope families; De Loera–Lopez-Campos–Torres study sections individually. Searches for cooriented shadow–section laws, dual formulations and direct containment implications produced no equivalent. The novel *candidate* is the twenty-cone nesting and complete joint law, which is not a probabilistic consequence of two marginals. Possible older stereological statements not found remain a priority risk.

## Mathematical value — PASS

Shadow complexity and section complexity are two canonical but different observables from a common viewing plane. Their joint distribution detects geometric dependence invisible to either marginal. A sharp deterministic exclusion (no 12-sided central section can coincide with an 8- or 10-sided shadow) comes from a structural nesting certificate for two nonidentical great-circle arrangements. The complete four-point distribution and exact negative covariance serve as a precise geometric benchmark rather than an arbitrary numerical subcase.

## Limitations

The solid must be regular and the two measurements must use the same centered plane. Nongeneric directions are excluded. The exact marginal area laws and their spherical tessellations are prior information; the historical priority of the new coupling remains provisional. No claim of independent external verification is made.

Self-review: passed. Independent audit: not yet performed.
