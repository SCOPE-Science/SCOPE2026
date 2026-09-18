# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The argument was checked against Aoki's definitions of intervals, relative downsets/upsets, extremal boundaries, the Boolean family \(W(S,C)\), saturation, and \(\bar\omega(S,C)\). The proof reduces every saturated pair to the endpoint levels of \(T=S\cup C\).

The main points checked adversarially were:

- In an ordinal sum of antichains, every non-singleton interval has consecutive occupied levels, all intermediate levels full, and arbitrary nonempty endpoint subsets.
- If \(S\) is a relative downset and \(C\) a relative upset of \(T\), then \(\operatorname{Max}(C\setminus S)\subseteq\operatorname{Max}(T)\) and \(\operatorname{Min}(S\setminus C)\subseteq\operatorname{Min}(T)\). This gives the endpoint-size upper bound without assuming more than saturation supplies.
- For nonadjacent endpoint levels, the proposed full-segment pair is saturated: any lower enlargement violates downward closure of \(S\), and any upper enlargement violates upward closure of \(C\).
- For adjacent levels, connected relative downsets and upsets have only the two stated forms. Exhausting those forms yields the piecewise function \(F(a,b)\), including the exceptional two-point value \(F(1,1)=2\) and the threshold at level size two.
- Each branch of \(F\) has an explicit saturated pair on the full adjacent levels, so the upper bounds are attained.
- The derived corollaries for uniform levels and equality in the \(|P|-1\) universal bound follow directly from the closed formula.

As an independent finite check of the combinatorics, `artifacts/check_small_weak_orders.py` was executed. It directly enumerates intervals and saturated pairs from the definitions and compared the resulting \(\Omega(P)\) with the theorem for all 102 level profiles with \(2\le h\le4\), \(1\le n_i\le3\), and total size at most nine. It reported zero mismatches. This computation supports but does not replace the general proof.

## Originality

The originality assessment is **to the best of our knowledge**.

Aoki's arXiv:2609.15927v1 was inspected in full. It proves the general saturated-pair formula \(\operatorname{gldim}\Lambda_P=\Omega(P)\), the relative formula \(\operatorname{int-res-gldim}_kP=\Omega(P)-2\), the universal \(|P|-1\) upper bound for \(|P|\ge3\), and an explicit rectangular-grid application. Searches inside that paper found no treatment under the terms `weak order`, `ordinal sum`, or `layered`; `bipartite` occurs in an unrelated simplicial-complex argument.

The full arXiv texts of Asashiba--Escolar--Nakashima--Yoshiwaki (arXiv:2207.03663) and Aoki--Escolar--Tada (arXiv:2308.14979) were also inspected for `weak order`, `ordinal sum`, and `complete bipartite`; no matching formulation was found. Their general finiteness/relative-Auslander framework, monotonicity, and zero-dimensional classification are treated as prior work.

External searches combined `interval resolution global dimension` or `interval endomorphism algebra` with `ordinal sum`, `weak order`, `complete bipartite poset`, `complete multipartite order`, and `layered poset`. No exact formula equivalent to the theorem, no height-two threshold, and no uniform-height stabilization result was located.

No specifically identified high-risk primary paper among the three directly relevant interval-resolution sources remained inaccessible. The remaining originality risk is terminological: weak orders are classical objects and the specialization of a very recent general theorem is combinatorial, so an equivalent calculation could exist in older persistence, relative-homological, or poset-representation literature under different language. Aoki's source is also a recent first version, so subsequent revisions may independently add such examples.

## Value

The result converts a general saturated-pair maximization into a closed formula for an infinite, classical family of posets. It exposes two distinct mechanisms for the maximum: an adjacent-level local term with a sharp small-level threshold, and a nonadjacent endpoint-sum term. The uniform-level corollary gives immediate stabilization independent of height, while the equality classification identifies exactly which weak orders attain the general upper bound. These statements provide reusable benchmark families for interval-resolution homological complexity beyond rectangular grids.
