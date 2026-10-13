# Scientific review

## Correctness — PASS

For each of the \(2^m-1\) adjacent-pair states, the output is a nonzero \(m\)-bit vector. Distinct outputs exhaust the nonzero cube, so every coordinate occurs in exactly \(2^{m-1}\) outputs; each selected item can account for at most two adjacent-pair outcomes. This proves the per-pool \(2^{m-2}\) lower bound and identifies equality with nonadjacent selected items. The construction's explicit edge-output permutation of \(\{1,\ldots,2^m-1\}\) proves decoder uniqueness, including the cyclic wrap. Coordinate counts prove every pool has exactly \(2^{m-2}\) items. The included verifier checks all formulas for \(2\le m\le13\). Infinite validity relies on the written proof, not finite enumeration.

## Originality — PASS, qualified

The strongest close equivalence is the union vertex-distinguishing coloring of Bousquet et al. For a cycle it is the same OR mechanism after dualizing edge labels to item masks, but their theorem optimizes only the number of colors/tests and assumes nonempty edge labels. The color-count conclusion alone is previously known and is not claimed as a new finding. The **different** objective is the exact sum of pool cardinalities, with its lower bound, equality condition and balanced all-parameter explicit attainment. Their full available primary text, including cycle proofs, contains no theorem implying that incidence optimum. The Müller–Jimbo 2CPD formulation is stronger (it also distinguishes individual columns) and does not imply the minimum-weight claim. The 2025 balanced Gray-code article forces constant item weight and adjacent Hamming distance two, whereas this construction has varied item weight and includes zero columns. The 2026 low-weight Gray-code conference abstract addresses ranking of monotone codes, not this exact cyclic total-incidence bound. Some older full texts and that conference paper were inaccessible; earlier unindexed treatment is a real residual literature risk. A failed search is not proof of priority.

## Value — PASS

Total sample aliquots and maximal pool volume are independently motivated physical resources in nonadaptive group testing. The result resolves the exact optimal cost, not just a feasible count of tests, throughout the naturally saturated family of \(2^m\) distinguishable states. It also characterizes equality and supplies an elementary explicit perfectly balanced construction, with each pool's size at the smallest value forced by the output spectrum. This may inform a resource-limited cyclic-screening design when the restricted defect model is realistic. Its lack of robustness and lack of singleton detection are essential limits.

## Literature and limitations

Closest earlier work: Bousquet et al., arXiv:1605.02588 (cycle union-distinguishing color count); Müller–Jimbo, doi:10.1016/S0012-365X(03)00282-6 (stronger 2CPD matrices); He et al., doi:10.1093/bioinformatics/btaf611 (balanced constant-weight consecutive-positive designs). See the structured review for source materials, negative comparisons and the full-text-access risks. No separate human or external audit has occurred.

Self-review: passed. Independent audit: not yet performed.
