# Self-review

## Correctness
PASS. The proof reconstructs the \(B\)-coloring condition exactly on \(\operatorname{Cr}_n\). Mapping \(a_i b_j\) to \(i\to j\) shows that same-colored edges must be pairwise composable arcs. Three pairwise compatible arcs are forced to be one directed \(3\)-cycle, and no fourth arc can join the class. This yields the universal lower bound. The Mendelsohn packing theorem supplies matching constructions in every congruence class except order \(6\); at that order, equality in the lower bound would be an excluded Mendelsohn triple system, while an explicit eleven-class partition gives the upper bound. The packaged verifier independently checks the local structural lemma, exact nonexistence of a directed-triangle decomposition at order \(6\), and explicit constructions through order \(8\).

## Originality
PASS. The initiating 2026 paper defines the same \(B\)-coloring parameter and records the complete-biclique value, but full-text inspection found no crown or Mendelsohn treatment. The classical directed-design theorem completely covers the needed triangle packings once a reduction is available; it does not state an edge-coloring result or the crown-graph correspondence. Targeted searches for crown graphs, matching-deleted bicliques, rainbow \(C_4\) edge-coloring, and Mendelsohn formulations located no prior statement of the formula or reduction. A previous exact \(B\)-coloring result for cactus graphs covers the small crown \(\operatorname{Cr}_3\), which is excluded from the new claim and does not apply for \(n\ge4\).

## Value
PASS. Crown graphs are the canonical one-factor deletion of balanced complete bipartite graphs. The theorem exposes a large and nonmonotone sensitivity of a recent coloring invariant: removing only \(n\) edges changes the exact value from \(n^2\) to asymptotically \(n^2/3\). The reduction to Mendelsohn packings also explains the otherwise isolated exceptional order \(6\), giving structural meaning rather than a table of small values.

## Closest literature and limitations
The closest same-invariant sources are Lu–Ying–Song (arXiv:2609.39716v1) and the foundational paper of Gyárfás–Sárközy (DOI:10.1556/012.2023.01539). The design-theory input is Gardner's maximum-packing theorem, originally published in Congressus Numerantium 127 (1997) and reproduced in an accessible design-theory supplement. The original 1997 full text was not retrieved; this is an access limitation, not an unresolved mathematical comparison, because the accessible supplement states the exact theorem used and attributes it to the original paper. An unindexed older edge-coloring reformulation remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
