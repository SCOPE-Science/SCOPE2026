# Scientific review: largest simplices in the 24-cell

## Correctness — PASS

The body is specified by the \(24\) type-\(D_4\) roots; its \(24\) congruent octahedral facets give four-volume \(8\). The augmented Gram identity and trace bound give the determinant estimate \(|D|\le25\sqrt5/4<14\) for any five roots, while parity of the coordinate-sum lattice forces \(D\) to be even, giving \(|D|\le12\). The displayed witness has determinant \(12\), giving sharp simplex volume \(1/2\). An independent exact finite census of all \(42{,}504\) unordered five-root sets, reproduced by the included checker, finds exactly \(48\) maximizers, all in one signed-permutation orbit, and no maximizing four-root face shared by two distinct maximizers. The latter fact upgrades standard vertex reduction to full rigidity: moving any nonvertex point in an equality simplex to more than one vertex would create two maximum sets sharing four vertices. The algebraic and computational claims therefore have distinct, explicit justifications.

## Originality — PASS, subject to priority uncertainty

Koca, Koca, and Al-Barwani (arXiv:1106.3433) describe the 24-cell's \(D_4\) framework and constructions of the snub 24-cell, not optimization of contained 4-simplices. Horváth and Lángi (arXiv:1402.6496) characterize a regular simplex as the largest among all five points on a prescribed sphere, a larger feasible domain that does not give attainable equality among the 24 roots; adding parity yields only an upper bound, not all 48 witnesses or rigidity. The published 24-cell Voronoi/lattice reducedness result has the same containing polytope but investigates unrelated lattice-width and completeness invariants. The general largest-inscribed-simplex reference supplies algorithmic vertex reduction and complexity, without the present numerical result. Targeted searches for D4 roots, the 24-cell, maximal-volume pentachora, determinant 12, and orbit 48 did not identify an equivalent statement. The possibility that classical regular-polytope literature tabulates these exact configurations remains a genuine historical priority risk; a negative search is not proof of novelty.

## Value — PASS

The 24-cell is a distinguished four-dimensional regular and self-dual convex polytope with no analogue among three-dimensional Platonic solids. The exact extremal ratio \(1/16\), *complete* 48-member orbit classification and absence of arbitrary nonvertex equality configurations give a fully solved geometric optimization problem for this canonical body. The result combines an analytic lattice-parity obstruction with a small exhaustive equality certificate and is not merely a reformulation of the universal regular-simplex ball bound. Its scope is deliberately this natural benchmark, not a general bound on all polytopes.

## Literature and limitations

Most pertinent reviewed material: Koca–Koca–Al-Barwani, arXiv:1106.3433v2, sections 1–4; Horváth–Lángi, arXiv:1402.6496v3, introduction, preliminary simplex corollary, main results and closing questions; the complete publicly available result “The \(D_4\) 24-cell is lattice reduced and complete”; and the AProPo overview of maximum inscribed simplices. The checker exhausts finite root subsets, not all continuous configurations; all continuous points are covered separately by the affine determinant and rigidity arguments. A previously unnoticed classical table or differently formulated determinant theorem could affect the historical originality assessment, and no independent audit has been conducted.

Same-model review: passed. Independent audit: not yet performed.
