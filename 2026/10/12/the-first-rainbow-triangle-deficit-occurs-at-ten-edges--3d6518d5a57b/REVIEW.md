# Scientific assessment: first finite rainbow-triangle deficit

## Correctness — PASS

All graph and coloring quantifiers include arbitrary finite simple graphs, three available edge colors (not necessarily all used), and exactly \(m\) edges. The Kruskal--Katona upper bound provides \(R(m)\le Q(m)\) and the supplied colored edge lists attain it through nine edges. For ten and eleven edges, the triangle-bearing-core reduction handles disconnected graphs and removes triangle-free edges. An eight-or-more-vertex connected core has a degree-two vertex in exactly one triangle, forcing strict subthreshold counts by the ordinary bound. Therefore a high-triangle graph must occur among graphs on at most seven vertices and have ten or eleven edges. The integer-mask verifier exhausts all 709801 such labeled graphs without any isomorphism assumptions and establishes the required implications. The self-contained \(K_5\) coloring argument forces at least three nonrainbow triangles. That obstruction and the witnesses give both sharp upper bounds. Compile/run checks are documented in `verification.log`; these finite results are not presented as infinite proofs absent the mathematical reduction.

## Originality — PASS, with residual risk

Chao--Sankar--Yu, arXiv:2610.02165v1 (1 October 2026), prove an overarching inequality but not the exact budgets ten and eleven; their numerical inequality permits 8 and 9, compared with the exact 7 and 8 here. The earlier Balogh--Hu--Lidický--Pfender--Volec--Young complete-graph theorem and construction for five vertices give a seven-rainbow-triangle example, but do not settle the maximum over every graph with a fixed edge budget. The Balogh--Bradshaw--Garcia--Lidický 2025 exact three-color-class bound \(T^2\le 2RGB\) also permits respectively eight and nine rainbow triangles at these budgets and does not subsume the sharper seven and eight. The ordinary Kruskal--Katona triangle count is an upper bound and is attained through nine but not ten edges. Precise comparisons against other indexed mathematical results did not reveal an exact edge-budget classification. The conclusion must not be interpreted as guaranteed global publication novelty: equivalent unindexed extremal bounds or an unexamined corollary remain possible.

## Value — PASS

The exact first point where the ordinary maximum triangle count ceases to be realizable with three pairwise-distinct colors is a well-defined, motivated finite boundary in the colorful Kruskal--Katona problem. The finite result is not merely a selected graph census: it optimizes over arbitrarily many vertices, with a graph-theoretic reduction and a sharp coloring obstruction. The plateau at ten and renewed increase at eleven provide finer behavior than the asymptotic upper bound. It has mathematical content independent of solving larger budgets and does not require an unsupported downstream theorem.

## Closest literature, methodological limits, and risks

Relevant sources: arXiv:2610.02165v1 (colorful edge-budget inequality); arXiv:2511.21061v3 (exact three-color-class bound); arXiv:1408.5296v1 (rainbow triangles in complete 3-edge-colored graphs); classical Kruskal--Katona. Exact enumeration uses a small standard C++17 executable; possible program implementation error is mitigated by a separate unlabeled-graph atlas census through seven vertices and explicit analytic checks. The classification does not extend past eleven edges and does not establish uniqueness of extremizers. Literature search cannot exclude unindexed equivalent results.

Self-review: passed. Independent audit: not yet performed.
