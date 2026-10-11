# Review of the regular-polygon centroid perimeter splitting law

## Correctness — PASS
For odd \(n\), a central line's two intersections are located on known edges in a fundamental angular sector. Their edge-coordinate parameters are computed exactly, yielding the shorter boundary fraction \(1/2-\tan\alpha\tan(\pi/n-\alpha)/(2n)\). A strict trigonometric maximization gives the minimizing directions; for even \(n\), central symmetry gives equal boundary arcs. The general proof covers every integer \(n\geq3\), including endpoint directions; `verify.py` separately checks boundary intersections for degrees 3 to 37 and exact-rational sample identities. Those finite tests are corroborative, not infinite proofs.

## Originality — PASS, with documented risk
The initiating full-text primary source, Berele–Catoiu, arXiv:2603.23653 (24 March 2026), already determines the equilateral triangle's sharp coefficient \(4/9\), and that case is not claimed new. It does not give the directional profile or equality classification for all odd regular polygons. The primary source's conjecture about arbitrary convex bodies gives no exact regular-polygon coefficient. Published mathematical-record checks of same-object polygon symmetry, central overlap, Fraenkel asymmetry, and diameter bisection found only different quantities; coincident trigonometric factors do not constitute logical coverage. Bibliographic and full-text access limitations leave a residual possibility of overlooked historical work; see `AUDIT.json` for exact queries, source reading, closest IDs, and implication comparisons.

## Value — PASS
The theorem settles a canonically motivated spectral-free family of the perimeter Winternitz partition problem. It classifies every odd and even regular polygon, every cutting direction and every equality line, and the sharp \(n^{-3}\) parity decay. The exact geometric splitting function is a nontrivial structural reference point for the proposed all-convex-body inequality. The classical triangle and trivial centrally symmetric cases are explicit baselines, not separate novelty assertions.

## Limits
The geometry concerns the shorter part of the **original polygonal boundary**, not the full perimeter of a cut piece including its chord; it does not solve the all-convex-body conjecture. Published-record searches cannot prove independence from unindexed or inaccessible sources. Numerical samples are not a proof for arbitrary degrees.

Same-model review: passed. Independent audit: not yet performed.
