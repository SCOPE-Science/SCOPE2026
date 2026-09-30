# Independent Audit — 2026-09-29

**Record:** `2026/09/18/unique-path-expected-range-maximizers--cf269fe0bc22`  
**Title:** Unique BHM maximizers and a quantitative standard-to-lazy gap transfer  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `2b09a1e60a0b3cebec0ba2bfe5a9a672e52841af`  
**Disposition:** **REPAIRED**

## Independent checks

- Reconstructed the single-class equality condition from the auxiliary-tree Bernoulli parameters.
- Checked the maximum-degree argument and exclusions of C_{2m} for m≥3 and of C4.
- Re-derived the standard-to-lazy gap transfer from the zero-edge contraction identity.
- Rechecked the 2016 tree equality attribution through search-indexed theorem text for Corollaries 2.6 and 2.12 and narrowed the novelty claim accordingly.

## Three-axis assessment

- **Correctness — PASS**: The equality conditions extracted from Zhu’s proof are correct: a cyclic auxiliary graph is strict; for an auxiliary tree, independent edge increments have nonzero probabilities 2/(2^{t_e}+2)≤1/2, and strict increase of the path expected-range sequence forces t_e=1 at equality. Applying this in both bipartition classes forces Δ(G)≤2 and excludes every even cycle, including C4 by codegree two. The gap-transfer inequality correctly follows from zero-edge contraction and the positive-probability no-zero event.
- **Originality — PASS_AFTER_REPAIR**: The prior record materially understated Wu--Xu--Zhu (2016): search-indexed full-text theorem text shows Corollary 2.6 gives unique-path equality for lazy height on trees and Corollary 2.12 gives the corresponding standard/bipartite equality. Those tree equality cases are prior. The repaired record narrows originality to the complete equality classification for Zhu’s 2026 all-connected-bipartite BHM theorem and the general quantitative standard-to-lazy gap transfer; targeted comparison did not find those results.
- **Scientific Value — PASS**: After removing the overstated novelty, the retained result still upgrades the newly proved BHM inequality from maximization to a complete equality classification over all connected bipartite graphs and supplies a quantitative transfer inequality valid on every connected bipartite graph. Both are substantive refinements.

## Findings

- The assigned tree exactly matches the current tree at the checked commit.
- Zhu’s current arXiv page still lists only v1, submitted 17 September 2026.
- The 2016 Wu--Xu--Zhu manuscript is search-indexed with exact theorem text: Corollary 2.6 states h(G)≤h(P_n) for trees with equality iff G=P_n; Corollary 2.12 states the analogous equality iff path for the standard/bipartite height.
- The prior record’s statement that a tree-only equality observation was merely a residual possibility is therefore false and requires research-file repair.
- The all-connected-bipartite BHM equality proof and the quantitative gap transfer remain mathematically sound and were not located in the compared prior sources.

## Sources compared

- Zhu, Paths maximize the expected range of graph-indexed random walks: https://arxiv.org/abs/2609.19728 — Current v1 proves the all-connected-bipartite BHM inequality and the LNR consequence; no complete all-connected-bipartite equality classification is stated.
- Wu, Xu, Zhu, Average Range of Lipschitz Functions on Trees: https://zhuyinfeng.org/Data/Preprints/MJCNT16.pdf — Search-indexed full-text theorem text shows Corollaries 2.6 and 2.12 already classify equality among trees for both lazy and standard/bipartite expected range. Direct PDF opening timed out, so only the indexed theorem text is claimed inspected.
- Bok and Nešetřil, Graph-indexed random walks on pseudotrees: https://doi.org/10.1016/j.endm.2018.06.045 — Extends the two inequalities to unicyclic graphs; no compared text supplied the all-connected-bipartite equality criterion or the quantitative gap transfer.

## Limitations

- The repaired originality claim excludes both tree equality classifications, which are explicit prior work.
- Direct opening of the 2016 author-hosted PDF timed out; attribution rests on search-indexed theorem text that exposed the exact Corollaries 2.6 and 2.12 statements.
- The stronger stochastic-domination version of BHM is not addressed.
- The factor p_G can be exponentially small; no sharp universal stability gap is claimed.
- Because the 2026 BHM proof is very recent, contemporaneous unindexed parallel work remains a residual originality risk.

This audit is independent of the repository’s pre-existing same-model review. No GitHub writes were performed during the audit.
