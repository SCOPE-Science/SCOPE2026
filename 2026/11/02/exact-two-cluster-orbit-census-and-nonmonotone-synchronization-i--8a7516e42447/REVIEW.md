# Self-review

## Correctness — PASS

The statement is confined to the explicitly defined parallel, nominal-snapshot, flash-entry rule. The exact half-quorum reduction uses the fact that \(m-1\) of \(2m-1\) same-group neighbors are insufficient for acceleration and that all neighbors flash once the other equal-sized group does. The derived difference events have only two active ranges; their overlap yields exactly the explicitly listed mutually accelerated waves. The coasting states cannot be entered from outside, and the two extra preimages of each accelerated wave have no predecessors. These facts prove the complete cycle and basin census for all admissible integer clock lengths, independent of enumeration. The separately implemented `verification/check_firefly.py` passed exact comparisons for 2,553 parameter pairs through \(C=72\), 6,779,342 phase states, and 81,330 agent-level reductions. Finite testing checks but does not certify the infinite family.

## Originality — PASS, with stated priority limits

The closest primary reference is Aust–Zhang–Reina–Hamann (arXiv:2605.17206v1), whose complete HTML main text, main figures' explanations, model and Algorithm 1 were inspected. It reports multimodal synchrony and locked clusters, but does not establish the present exact two-clock cycle/basin formulas. Crucially, its prose suggests an entry-trigger rule while the printed implementation tests one phase later in a sequential loop: **this theorem fixes the parallel entry-trigger convention and does not purport to cover that printed algorithm**. The inhibitory finite-state oscillator of Lyu (arXiv:1407.1103) and the aggregation model of O’Keeffe–Krapivsky–Strogatz (arXiv:1501.04115) have different update laws. Searches for equivalent subgroup, periodic orbit, phase-width, and exact-basin statements identified no dominating result. Residual risks are specialized unindexed literature and inaccessible supplementary code; no uninspected document is described as fully reviewed.

## Mathematical value — PASS

A two-equal-cluster sector is a distinguished invariant symmetry reduction of an all-to-all pulse network, not an arbitrary numeric slice. Its exact coasting/accelerated boundary, all-parameter synchrony basin, and full zeta function provide an explicit mechanism for nonmonotone performance as flash width increases, a mechanism the motivating study primarily explores through simulation. The result is about exact phase consensus, unlike an amplitude-overlap success score, and neither establishes results for unconditioned random clocks nor claims any robustness under asynchrony or noise.

## Limitations and closest comparisons

Only noiseless simultaneous nominal-snapshot updates, flash-entry triggering, half-quorum, complete graphs, and the equal-two-cluster invariant sector are covered. In particular the 2026 paper's printed sequential, after-entry implementation is distinct. Priority comparisons are best knowledge, not an independent historical certification.

Self-review: passed. Independent audit: not yet performed.
