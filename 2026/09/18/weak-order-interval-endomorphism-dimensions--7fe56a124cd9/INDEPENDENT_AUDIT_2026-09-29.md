# Independent audit — Exact interval-endomorphism dimensions for finite weak orders

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/18/weak-order-interval-endomorphism-dimensions--7fe56a124cd9`  
**Audited tree:** `a745444feadfa2bda8f1a434ae4bd3a339c819f4`

## Disposition

**PASSED.** All three required axes pass. Publication may remain in the validated record set.

## Correctness

**PASS.** The closed formula is consistent with Aoki's saturated-pair characterization and survives independent finite reconstruction. In a weak order, any non-singleton interval occupies consecutive levels, with all intermediate levels full and arbitrary nonempty endpoint subsets. The endpoint-max/min argument bounds each saturated-pair weight by its two endpoint sizes. Nonadjacent full endpoint levels attain n_i+n_j. For adjacent levels, exhausting connected relative downsets/upsets gives the stated piecewise F(a,b): 2 at (1,1), a+b-1 when one side is at most 2 (apart from (1,1)), and a+b-2 when both are at least 3; the supplied saturated pairs attain each branch. An independent enumerator reproduced the formula on representative two-, three-, and four-level profiles, including all threshold cases checked.

## Originality

**PASS.** but only for the full weak-order formula and its height-two/uniform-level consequences. An earlier 2026-09-17 SCOPE record globally classifies equality in Aoki's n-1 bound; therefore the assigned record's final equality corollary is not independently novel. That prior record does not give the exact Omega(P) formula for arbitrary weak orders, the adjacent F(a,b) threshold, or the height-independent uniform value 2r. Searches did not locate an earlier source containing those main formulas.

## Scientific Value

**PASS.** The main formula is scientifically useful despite the non-novel equality corollary. It converts a general saturated-pair maximization into a closed expression for a broad classical poset family, distinguishes adjacent and nonadjacent mechanisms, and supplies explicit benchmark families whose interval-resolution complexity stabilizes with height.

## Independent checks

- Reconstructed the interval classification and endpoint upper bound directly from the weak-order relation.
- Implemented an independent saturated-pair enumerator and checked profiles (1,1), (2,3), (3,3), (1,1,4), (2,1,3), (3,2,3), and (1,2,1,2); every value matched the closed formula, including the min=2 threshold.
- Inspected the record's exhaustive-check artifact, which directly implements intervals, relative down/up-sets, extremal boundaries and W(S,C) rather than hard-coding the claimed formula.
- Compared against the earlier global extremal-classification SCOPE record and narrowed the originality claim accordingly.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.15927 — Aoki (2026), general saturated-pair/global-dimension formula and sharp universal bound; foundational prior work.
- https://arxiv.org/abs/2207.03663 — Asashiba, Escolar, Nakashima and Yoshiwaki, interval-resolution framework.
- https://arxiv.org/abs/2308.14979 — Aoki, Escolar and Tada, monotonicity and related interval-resolution results.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/17/extremal-interval-endomorphism-global-dimension--15e3312baa42 — Earlier SCOPE record classifying all equality cases for gldim=n-1; overlaps only the assigned record's equality corollary, not its full weak-order formula.

## Limitations

- The equality-in-the-universal-bound corollary is not a novel contribution because it follows from an earlier SCOPE equality classification.
- The main formula specializes Aoki's very recent general theorem, so equivalent computations under alternate terminology remain a residual literature risk.
- The finite enumeration is supporting evidence; the general proof is combinatorial rather than formally verified.

## Repository identity

The assigned source-tree SHA `a745444feadfa2bda8f1a434ae4bd3a339c819f4` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
