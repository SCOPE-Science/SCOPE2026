# Review of the finite sharpness theorem

## Correctness

**PASS.** Splitting the first joined-history phrase once and every later cross-boundary phrase at most twice gives the universal bound. The recursive construction admits one joined-history phrase per stage, while a unique new adjacent-pair boundary at each stage forces two longest split-source phrases. A self-contained exchange lemma establishes greedy optimality. Finite direct and dynamic-programming checks agree through the stated ranges. The induction, not finite computation, supports the arbitrary-size conclusion.

## Originality

**PASS on the inspected record, with residual priority risk.** Marteau's October 19, 2026 paper proves a factor-two upper bound and expressly leaves sharpness unsettled in Remark IV.11. The present finite additive strengthening and recursively sharp family do not follow from merely knowing that upper bound. Kosolobov–Shur's earlier superficially similar two-to-one parsing comparisons alter overlap/encoding conventions rather than the source boundary. Targeted mathematical-index searches and existing accessible claims yielded no covering statement, but an unindexed equivalent remains possible.

## Value

**PASS.** This resolves a question posed explicitly in a recent source: factor two cannot occur at any finite count, yet is the optimal universal multiplicative constant. The construction reaches the exact upper envelope at each phrase-count value, yielding a full finite extremal law rather than an arbitrary small example or a routine numerical improvement. This clarifies worst-case costs of preventing factors from spanning a reference/target boundary.

## Scientific limitations

The target length and alphabet size both grow with the required phrase count. The work does not establish sharpness over a fixed alphabet, minimize witness lengths, optimize pointer bit lengths, or handle overlapping source copies. External independent audit and exhaustive publication-priority certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
