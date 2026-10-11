# Scientific comparison and same-model review

## Correctness — PASS
Every rectangle is represented by two equal-length diagonals. Central symmetry allows exact recentering. Boundary optimality and a first-variation condition reduce all maximizers to two cases: perpendicular diagonals or two boundary tips. The perpendicular case is controlled by a strictly concave trigonometric denominator and the AM-GM inequality; the boundary case reduces to a quadratic level-set dichotomy. Each branch satisfies the asserted sharp bound, and the two explicit constructions attain it. The equality restrictions show one optimizer in each open phase and exactly two at the threshold. A standalone deterministic sweep verifies representative feasible cases; finite tests are not the universal argument.

## Originality — PASS, with historical limitations
Cabello, Cheong, Knauer, and Schlipf (arXiv:1405.1223, 2014), inspected full-text, give a general exact optimization algorithm but not the closed-form sharp rhombus phase diagram or optimizer classification. Knauer, Schlipf, Schmidt, and Tiwary (2012), inspected full-text, develop approximation algorithms and general contact types, not this formula. Lassak (1993) establishes a universal existence bound but its full text was not inspected. The square case appears within a published regular-even-polygon result; it does not establish the non-square transition. No equivalent indexed result was found in targeted alternate-formulation searches. Earlier elementary treatments cannot be ruled out without independent historical checking.

## Value — PASS
The problem is a natural, well-studied area maximization over freely oriented rectangles. The sharp and complete ratio law \(\max\{1/2,B/A\}\) exposes two qualitatively distinct optimal contact patterns. The exact transition \(B/A=1/2\), its double optimizer, and uniqueness elsewhere classify the entire rhombus family and sharpen the generic half-area guarantee.

## Limits
Only Euclidean rhombi and area optimization; not arbitrary parallelograms or perimeter objectives. Grid tests do not establish the theorem. Publication priority has not been independently checked.

Same-model review: passed. Independent audit: not yet performed.
