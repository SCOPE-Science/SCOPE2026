# Scientific review

## Correctness — PASS
The observation of **distinct** factor Parikh vectors equals the pair of minimum/maximum one-count functions because overlapping equal-length windows change by at most one. The minimum length spanning two or three ones fixes the unordered internal gaps. The maximum length spanning at most two ones fixes the unordered outer gaps, yielding at most four possibilities. The maximum span of at most one one separates the two alignments, except exactly when the smaller inner gap is at least the larger outer gap. Direct proof covers equal gaps and zero-length gaps; unique strict inequalities parametrize four-word fibers and give their generating function. The standalone checker independently enumerated all factor observations and verified every predicted fiber for lengths 3 through 24. Finite verification is corroboration, not infinite proof.

## Originality — PASS, with residual priority risk
The defining Parikh-set equivalence and its maximum/minimum window characterization are explicitly prior results (arXiv:1611.09017, Theorem 4), not claimed as new. General prefix-normal-form equivalence in arXiv:1401.6346 and arXiv:1805.12405 uses one extreme and can have larger classes; it does not determine the intersection class sizes at fixed weight three. arXiv:1403.2439 studies a **multiset** of compositions, a strictly richer observation, so its stronger reconstruction result at short lengths is compatible with the present fourfold set-valued ambiguity. Actual database and literature searches did not identify a proof of the exact three-one fiber classification, threshold condition, or four-class generating function. An unindexed equivalent remains possible.

## Value — PASS
The inverse problem is motivated by jumbled-string indexing: the factor Parikh set is precisely the information queried by a binary jumbled-pattern index. The theorem measures the **complete unavoidable source ambiguity** of this natural compressed observation at the first nontrivial sparse level, identifies every ambiguous reconstruction, and enumerates all class sizes with a sharp asymptotic density. This is a coherent, fully quantified structural classification, rather than a restatement of known prefix-normal counts or an arbitrary finite census.

## Limitations
No result is claimed for higher minority weight, multiset reconstruction, or subsequence observations. Publicly accessible full texts and indexed results do not establish absolute historical uniqueness; independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
