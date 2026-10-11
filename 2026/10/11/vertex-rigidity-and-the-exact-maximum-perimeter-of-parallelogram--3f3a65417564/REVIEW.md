# Same-model mathematical review

## Correctness — PASS
The centralization argument preserves side vectors. Separate convexity of the perimeter in opposite corner vectors reduces the global optimization to vertex pairs. Equality rigidity uses equality in two Euclidean triangle inequalities, which forces the relevant segment to lie on the diameter line; the resulting perimeter cannot attain the strictly larger vertex-pair maximum. The circumdisk parallelogram identity forces any original maximizing center to be the circle center. The sharp angular formula follows from chord lengths. The scan is linear on sorted diameter angles. The included deterministic verifier independently compares linear and exhaustive vertex scans and samples the convexity bound. Finite checks supplement, not replace, this analytical proof.

## Originality — PASS (subject to historical priority risk)
Cabello et al. give a cubic-time maximum-perimeter rectangle algorithm for arbitrary convex polygons but not this vertex rigidity or direct formula. Choi et al. likewise treat general polygonal optimization. The closest published regular-polygon result determines maximum *area*, expressly leaving perimeter untreated, and does not cover irregular centrally symmetric cyclic polygons or parallelogram equality rigidity. Searches by mathematical statement, object, and equivalent formula found no stronger published coverage in the inspected materials. The possibility of an older elementary or rotating-calipers formulation remains a priority risk.

## Value — PASS
The result completely classifies an infinite, nonregular geometric class and all equality cases. Its simultaneous parallelogram/rectangle extremality and linear-time reduction to diametral angular pairs are structurally stronger than simply evaluating a regular-hexagon example or reprinting a known maximization table. The regular-even closed form is a consequence of the broader theorem and highlights its sharp angular obstruction.

## Limits and closest references
The assertion requires central symmetry, concyclicity and exact vertex order. It is not a bound for arbitrary convex bodies; general-purpose cubic algorithms remain necessary outside this class. Relevant primary references are Cabello–Cheong–Knauer–Schlipf, arXiv:1405.1223, and Choi–Lee–Ahn, DOI:10.1016/j.comgeo.2020.101710; the closest published special-case record is *Exact maximum-area rectangles in every regular even polygon*.

Same-model review: passed. Independent audit: not yet performed.
