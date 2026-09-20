# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The variance identity for arbitrary positive integer cluster counts follows directly from independence within and across clusters. Subtracting it from the uniform-with-replacement variance and applying the ANOVA decomposition gives the stated exact criterion. The displayed two-cluster instance was checked with exact rational arithmetic: the rounded counts are unambiguous, the normalized scalar gradients form the two cosine clusters claimed, and the rounded clustered variance exceeds the uniform variance by 10437/5000. Replacing the budget by one that permits exact proportional counts restores the source theorem exactly.

The source paper's full HTML was inspected through its theorem, practical rounding rule, assumptions, convergence proposition, discussion, and experimental parameter section. The record deliberately distinguishes the valid exact-proportional theorem from the unsupported extension to the rounded practical allocation.

## Originality

The literature search covered the source title/arXiv identifier together with terms including clustered meta-gradient sampling, rounding, variance, proportional allocation, stratified sampling, Neyman allocation, and exact integer allocation. No public comment or correction to arXiv:2609.16370v1 was located.

The underlying statistical facts that variance depends on stratum allocation, that Neyman allocation minimizes variance in the continuous problem, and that naive rounding need not be integer-optimal are classical and are **not** claimed as new. Wright's work explicitly treats exact integer allocation and the limitations of rounded Neyman allocations. The originality claim is limited to applying the exact arbitrary-count formula to the newly proposed gradient-clustered sampler, deriving the sharp paper-specific variance comparison criterion, and giving an explicit cosine-compatible instance where the source's stated practical rounding rule reverses the claimed variance advantage.

No inaccessible paper was identified as especially likely to contain this specific September 2026 source correction. The original 1934 Neyman article was not needed for the novelty claim; accessible modern and authoritative sources were sufficient to establish that optimal stratified allocation itself is classical.

## Value

The gap affects the bridge between the paper's implementable sampler and its main variance/convergence guarantee. The counterexample is not a numerical edge case: it uses exact rational gradients, two clean angular clusters, distinct cluster means, and an unambiguous nearest-integer allocation, yet increases the selection variance by about 24.5%. The corrected identity provides a direct diagnostic and a simple fallback or variance-aware repair.

## Scope and limitations

The result does not refute the exact-proportional theorem, the ANOVA decomposition, or the empirical results. It does not infer the unreported realized cluster sizes in the experiments. It addresses independent with-replacement sampling, matching the theoretical model in the source paper, and leaves without-replacement variants outside scope.
