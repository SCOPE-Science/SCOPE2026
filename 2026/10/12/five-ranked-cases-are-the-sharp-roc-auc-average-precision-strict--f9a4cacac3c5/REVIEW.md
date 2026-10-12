# Self-review

## Correctness
**PASS.** If positive cases occupy ranks \(r_1<\cdots<r_P\), empirical ROC-AUC is \(1-\sum_j(r_j-j)/(P(N-P))\), while classical average precision is \(P^{-1}\sum_j j/r_j\). These exact formulas reconstruct the two metrics without interpolation or floating-point ambiguity. Exhaustive rational enumeration checks every fixed-prevalence ranking pair through \(N=5\), giving one weak-only split at \(N=4\), no strict reversal through four cases, and exactly two strict reversals at five cases. The packaged verifier returns `VERIFY_OK`.

Risk: score ties and alternative numerical conventions for precision-recall area are outside the theorem.

## Originality
**PASS.** Kishida establishes the discrete average-precision definition and its top-rank sensitivity. Davis–Goadrich establish the ROC/precision-recall correspondence and explicitly note that optimizing ROC area need not optimize precision-recall area. Saito–Rehmsmeier demonstrate the practical difference between ROC and precision-recall evaluation in biological classification. The checked literature therefore owns generic non-equivalence. The searched literature and database records did not state the fixed-prevalence no-tie minimum \(N=5\), the \(N=4\) tie boundary, or the complete two-pair first strict layer.

Risk: a five-item pedagogical example or unit test could be unindexed.

## Value
**PASS.** ROC-AUC and average precision are two standard threshold-free ranking summaries, with AUC weighting all positive-negative pairs uniformly and average precision emphasizing early positives. Fixing prevalence removes the most immediate baseline confounder. The sharp five-case boundary gives the smallest possible exact demonstration that these distinct weighting principles can reverse model selection and identifies every minimal mechanism.

Self-review: passed. Independent audit: not yet performed.
