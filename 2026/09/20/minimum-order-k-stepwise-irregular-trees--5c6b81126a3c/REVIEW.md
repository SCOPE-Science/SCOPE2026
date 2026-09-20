# Review — sharp minimum order of k-stepwise irregular trees at fixed maximum degree

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the points where a rooted branching argument could fail. Because every tree has leaves and every edge changes degree by exactly k, all degrees are congruent to 1 modulo k. Thus a maximum degree is necessarily 1+hk, and every degree class from 0 through h occurs on a path from a maximum-degree vertex to a leaf.

For a nonroot class-i vertex, the deletion of its parent edge leaves exactly ik child edges. The branch lower bound F_i is proved by strong induction on branch order, not by induction on the class index. This is important because a child may lie in class i+1. The child branch is nevertheless strictly smaller, so the induction hypothesis applies; strict monotonicity F_{i+1}>F_{i-1} then shows that every child branch contributes at least F_{i-1}. Hence F_i=1+ikF_{i-1} is valid for arbitrary upward and downward class steps.

At the global root, upward steps are impossible because its class h is maximal. Equality therefore requires every root-child branch to be minimal. Recursively, any upward child would contribute at least F_{i+1}>F_{i-1} and make the bound strict. Equality consequently forces every edge away from the root to descend one class and determines the entire rooted tree uniquely. Direct degree counting verifies the converse construction.

The closed form for F_i follows by unrolling the recurrence. For k=1 the resulting expression is exactly the factorial-sum formula recorded for OEIS A392965. For h=1 it gives the star K_{1,k+1}; for h=2 it gives 2k^2+3k+2.

The degree-complexity-three consequence was checked independently by deleting leaves. The remaining core is a tree with bipartition (A,B); summing degrees on B gives |E(H)|=(2k+1)|B|, while |E(H)|=|A|+|B|-1, hence |A|=2k|B|+1. Counting the missing degree at A yields the stated leaf count and order spectrum. The converse core construction realizes every positive value of |B|.

Correctness assessment: PASS.

## Originality

The older starting point was Gutman's 2018 paper introducing SI graphs and considering minimum-order SI trees with prescribed maximum degree. OEIS A392965 now records the general k=1 minimum-order sequence and factorial-sum formula; the present formula specializes exactly to it rather than claiming that case as new.

The full arXiv text of Alizadeh--Klavžar--Langari was inspected. Its tree-specific structural statement is that k-SI trees have even diameter; its principal extremal results bound maximum degree in terms of order and bound graph size, including an equality condition involving degree complexity three. No minimum-order formula for k-SI trees at fixed maximum degree, recursive unique extremizer, or exact order spectrum for three-degree k-SI trees was found there.

The accessible article page and abstract for Das--Mishra--Rai (2023) were inspected; they introduce 2-SI graphs, generalize properties to k-SI graphs, and discuss Albertson-index bounds. The complete theorem text was not inspected. The accessible abstract of Adiyanyam et al. (2026) states upper bounds on maximum degree and size and complete determination of certain 2-SI extremal graphs; its complete theorem text was not inspected. The 2026 Bera--Paul--Subramanian paper concerns ordinary SI graphs and degree-sequence conditions.

Targeted searches used minimum-order, prescribed-maximum-degree, tree, 2-SI, k-SI, degree-complexity-three, and exact-formula variants. No source matching or implying the general theorem was located. The current SCOPE repository was also searched under stepwise-irregular, degree-complexity, tree/minimum-order, and synonymous terms without locating an overlapping record.

Residual originality risk is concentrated in the uninspected theorem text of the 2023 and 2026 k-SI papers and in poorly indexed literature using different terminology. No accessible statement supplied concrete evidence of prior coverage.

Originality assessment: PASS, to the best of our knowledge.

## Value

The theorem gives an exact minimum order for every admissible maximum degree and every step size k, together with a unique extremal tree and its radius/diameter. It turns the known k=1 minimum-order sequence into a uniform structural theorem for all k rather than a parameter-by-parameter construction. The proof also explains the extremizer through a sharp rooted-branch recurrence, and the degree-complexity-three corollary gives a complete order spectrum for the first non-star case.

Value assessment: PASS.

## Scientific limitations

- The full theorem text of Das--Mishra--Rai (2023) was not inspected; its abstract and indexed descriptions were checked.
- The full theorem text of Adiyanyam et al. (2026) was not inspected; its abstract was checked.
- Unindexed or differently phrased equivalent results remain a residual originality risk.
- The result is restricted to trees; it does not give minimum orders for general connected k-SI graphs.
