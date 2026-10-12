# Scientific review

## Correctness — PASS

Exact depth-first enumeration over the three labeled letters, with a reversible palindrome tree and exact prefix sums, yields 404535 admissible words across lengths 0–105, exactly eight of length 104 and none of length 105. Factoriality of both restrictions proves the global upper bound from the empty depth 105. An independently implemented naive Python routine checked all labeled words of lengths 0–10 and all eight extremal witnesses of length 104, as well as every one-letter extension and the two full symmetry orbits. The finite exhaustive step is essential to this finite theorem; no infinite extrapolation is made.

## Originality — PASS, with priority risk

The closest relevant work is Andrade and Mol, *Avoiding abelian and additive powers in rich words* (arXiv:2408.15390), which determines maximum ternary richness under the weaker abelian-cube exclusion at length 180. Neither that number nor its proof determines the sharp additive-cube-free maximum 104 and its eight extremizers. Comparisons against the closest mathematical claims and public literature did not identify a statement covering this weighted exact classification. Such searches cannot preclude an unindexed independent census.

## Value — PASS

The published work explicitly studies the gap between abelian and additive power avoidance in rich words. Replacing equality of Parikh vectors with equality of sums is a natural, strictly stronger requirement on the same weighted alphabet, and the exact maximum decreases markedly from 180 to 104. Classification of all eight extremizers and two natural symmetry orbits quantifies that boundary, rather than sampling arbitrary parameter values. The result does not answer the question for larger integer alphabets.

Self-review: passed. Independent audit: not yet performed.
