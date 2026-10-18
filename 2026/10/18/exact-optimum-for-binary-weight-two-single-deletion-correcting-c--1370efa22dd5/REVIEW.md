# Scientific review

## Correctness: PASS
The weight-one deletion shadow yields \(\ell+2e\le n-1\). A pair of consecutive adjacent-one codewords has a common weight-two descendant after deleting opposite exterior zeroes, bounding the number of adjacent-one words by \(\lceil(n-1)/2\rceil\). Their combination is the claimed upper bound. A matching family of alternating adjacent-one words and regularly spaced separated-one words is directly shown to have disjoint deletion balls. Boundaries \(n=2\) and all admissible parameters are covered in the proof. The independent finite checker verifies n=2..96 and exact small optima through n=8; it does not replace the infinite proof.

## Originality: PASS (examined evidence)
Primary comparisons distinguish the exact fixed-weight-two one-deletion optimization from Sloane's unrestricted single-deletion code constructions and from Gómez Soto et al.'s *adjacent-transposition* fixed-weight-two theorem. The September 2026 En Gad result concerns unrestricted codes correcting at least two deletions, and does not imply the present exact conditional optimum. Source-equivalence, stronger-coverage, database/table, and prior-implication comparisons are given in the structured review. An older potentially pertinent coding thesis could not be inspected fully; an unindexed equivalent result remains a priority risk.

## Value: PASS
The result determines an exact optimum for every blocklength in a natural constant-composition synchronization channel, and provides a uniform construction and sharp obstruction. It explains why the obvious one-deletion shadow bound alone is insufficient: adjacent double-one patterns impose a second local packing constraint. No broader optimality statement for other weights or error models is claimed.

## Limitations
Only exactly two ones and exactly one arbitrary deletion are considered. No claim is made that the maximizing code is unique or that all historical sources have been exhausted. Finite testing is independent corroboration, not an exhaustive mathematical proof. Independent validation is not performed.

Self-review: passed. Independent audit: not yet performed.
