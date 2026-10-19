# Scientific review

## Correctness — PASS

The claim is a sharp minimum and unique length-twelve classification together with an all-length construction. Complete restricted-growth enumeration covers all patterns using at least three symbols through length twelve: it tests 4,211,549 classes at length twelve and two independently implemented run evaluators identify precisely the same unique class. Exact rational run lists for the ternary family and all three projected images establish the strict losses; a uniform-suffix lemma rigorously reduces the infinite part to finitely inspected prefixes. The replayable source files in this package contain both exhaustive engines and the family checker. No finite sample is used to infer an unproved generalization.

## Originality — PASS, with residual risk

Czarkowski, *Improved Bounds on the Sum of Exponents of Runs in a String* (2026), DOI 10.4230/LIPIcs.CPM.2026.23, proves general and binary upper bounds and explores alphabet dependence. Crochemore and collaborators, arXiv:1003.4866 (2010), prove extremal bounds and give binary morphic constructions. Their inspected original texts do not classify words for which **every two-letter identification strictly lowers the sum**, identify a sharp minimum at twelve, or give this all-length resistant family. Database searches using alphabet coalescence, merging, projection, run exponents, and the exact witness found no matching stronger claim. Residual risk: relevant older morphism classifications may be unindexed or formulated differently; this is not an independent priority judgment.

## Value — PASS

The binary and unrestricted run-exponent problems have different established bounding arguments. It is natural to ask whether merging two letters can always avoid loss, thereby simplifying alphabet reduction. The complete, unique first obstruction and its persistent family show why that local simplification cannot be used in general. This is a motivated structural boundary, not merely a numerical example or a claim to improve the known global exponent bounds.

Self-review: passed. Independent audit: not yet performed.
