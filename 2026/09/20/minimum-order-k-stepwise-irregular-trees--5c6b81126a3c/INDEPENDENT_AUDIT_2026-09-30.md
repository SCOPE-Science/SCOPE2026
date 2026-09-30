# Independent audit — Sharp minimum order of k-stepwise irregular trees at fixed maximum degree

## Scope
Independent review of `2026/09/20/minimum-order-k-stepwise-irregular-trees--5c6b81126a3c` for task `d78192f91c71d25955327c261d13fec3`. The assigned source tree `fd2cf1ea53377f6a287ba9b35dffc8dd70ccfcbc` matches the tree on repository `main` at commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`. Audit date: 2026-09-30 UTC.

## Correctness
**PASS.**

- The rooted-branch induction is valid when formulated as strong induction on branch order across all degree classes: a nonroot class-i vertex has exactly ik children, each child is class i-1 or i+1, every child branch is strictly smaller, and monotonicity of F_i forces the bound F_i=1+ikF_{i-1}.
- Equality forces every child to move one class downward and every descendant branch to attain equality; this recursively yields the unique extremal tree. The root then contributes 1+(1+hk)F_{h-1}, and the radius/diameter assertions follow from the forced h-level structure.
- The h=2 core calculation was independently recomputed: the core tree identity gives |A|=2kb+1, the leaf count is (2k^2-1)b+k+1, and hence n=2k(k+1)b+k+2. Small symbolic checks of the recurrence and closed form were consistent.

## Originality
**PASS_NARROW.**

- The accessible full preprint of Alizadeh–Klavžar–Langari (arXiv:2411.15765) advertises maximum-degree/size bounds, diameter constructions, and degree complexity, not this minimum-order tree theorem or its unique extremizer.
- Targeted searches for two-stepwise/k-stepwise irregular trees and minimum order did not locate the displayed general formula or the exact three-degree order spectrum. The 2023 Das–Mishra–Rai paper remains a residual coverage risk: open-access searches did not yield its full text, and an authorized Oxford retrieval attempt ended in a timeout, so it was not treated as read.
- The 2026 Adiyanyam et al. paper is indexed as studying upper bounds on maximum degree and size and extremal 2-SI graphs; no indexed statement matched this fixed-maximum-degree tree minimum.

## Scientific value
**PASS.**

- The theorem extends the known k=1 minimum-order phenomenon to all k with an exact formula and a unique extremizer, and the three-degree corollary gives a complete exact order spectrum in a natural low-complexity subclass.

## Literature checked
- [Extremal results on k-stepwise irregular graphs](https://arxiv.org/abs/2411.15765)
- [On Two-Stepwise Irregular Graphs](https://doi.org/10.24200/sci.2022.57725.5388)
- [On k-stepwise irregular graphs](https://doi.org/10.1016/j.dam.2026.06.027)
- [Stepwise irregular graphs](https://doi.org/10.1016/j.amc.2017.12.045)
- [OEIS A392965](https://oeis.org/A392965)

## Limitations
- Originality is limited to the stated minimum-order/uniqueness theorem and three-degree spectrum; general k-SI properties are prior work.
- Full text of Das–Mishra–Rai (2023) was not accessible through the checked open sources and the authorized institutional retrieval attempt timed out; no claim is made to have read it.

## Conclusion
The record **passes** the independent three-axis audit on the stated, literature-bounded claim. No substantive research-file correction is required. This audit does not convert a targeted literature search into an exhaustive priority guarantee.
