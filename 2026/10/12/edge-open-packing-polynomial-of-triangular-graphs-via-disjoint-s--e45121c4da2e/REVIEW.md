# Self-review: triangular-graph edge-open-packing polynomial

## Correctness — PASS

For each integer \(n\geq0\), the proposed bijection identifies an edge-open packing of \(T_n=L(K_n)\) with disjoint chosen \(P_3\)- and \(P_4\)-edge-paths on the original labels. Its proof first derives the induced-star-forest characterization from the literal third-edge obstruction and proves its converse. The neighborhood of a line-graph vertex splits into two cliques; hence every component has at most two leaves. Distinct components share no original labels. Counting exactly three undirected \(P_3\) paths and twelve undirected \(P_4\) paths per designated label set gives \(\exp(u+u^3z/2+u^4z^2/2)\) and its full coefficient formula. The modular maximum and exact multiplicities follow by a minimum-label argument at fixed packing size. All small boundaries, including \(n=0,1,2,3\), are explicitly considered. An independently formulated edge-conflict oracle checked 21,517 valid packings exhaustively through \(n=8\); exact arithmetic checked the coefficient sum, recurrence and extremal statements through \(n=60\). These computations are not substituted for the general proof.

## Originality — PASS, qualified

Chelladurai–Kalimuthu–Soundararajan (doi:10.1051/ro/2022171, first online 2022-11-01) give the edge-open-packing definition and the general induced-star viewpoint. Brešar–Samadi (arXiv:2403.00750v1) treat complexity, bounds and trees. Brešar–Dravec–Hedžet–Samadi (arXiv:2406.04020v2) compare induced matchings with edge-open packings on trees and graph products; their use of “triangular graphs” refers to a broader condition, not this particular line graph. Pandey–Santra (arXiv:2508.01935v1) give subsequent characterizations. The targeted full-text reading and searches for line graphs, induced-star forests, injective edge coloring and equivalent P3/P4 counting did not identify a theorem giving this complete enumerator, mod-four bound and extremal coefficient. The standard induced-star reduction and labeled exponential principle are explicitly treated as prior ingredients. Remaining risk: an older unlabeled or labeled path-block enumeration under other terminology might express the same sequence. Lack of a search hit is not absolute proof of priority.

## Value — PASS

The result determines every coefficient of a natural graph polynomial on an unrestricted classical graph family and yields an explicit recurrence and a geometric interpretation in terms of disjoint chosen paths. It also proves a residue-class obstruction to a larger packing exactly when \(n\equiv2\pmod4\), with two different structural types realizing the optimum for \(n\geq6\) in that residue. These are mathematically motivated structural enumerations rather than arbitrary slices.

## Limitations and integrity

The result concerns only \(T_n=L(K_n)\), not all line graphs or all graphs satisfying a triangle condition. Complete-source inspection was targeted at highly relevant primary theorem sections; synonymous unindexed literature remains a priority risk. The finite computations alone establish only the tested cases. No independent scientific validation or publication-priority determination is claimed.

Self-review: passed. Independent audit: not yet performed.
