# A sharp shift threshold for Abelian pattern Sturmian power words

## Finding

**Theorem.** Fix integers \(b\ge2\) and \(d\ge0\). Define \(D_{b,d}=\{b^j+d:j\ge0\}\) and let \(w_{b,d}\) be its infinite binary indicator word indexed from zero. This word is Abelian pattern Sturmian if and only if
\[
0\le d<b(b-2).
\]
In this regime its Abelian maximal pattern complexity, for every positive integer \(k\), is
\[
p_{w_{b,d}}^{*\mathrm{ab}}(k)=f(k):=\left\lceil\frac{1+\sqrt{8k+1}}2\right\rceil.
\]
For every \(d\ge b(b-2)\), the bipartite additive-incidence graph of \(D_{b,d}\) contains a simple cycle of length \(2(b+1)\) involving only the first three elements of \(D_{b,d}\). Consequently,
\[
p_{w_{b,d}}^{*\mathrm{ab}}\!\left(\binom{b+2}{2}\right)\ge b+3>f\!\left(\binom{b+2}{2}\right)=b+2.
\]
For example, none of the nonnegative shifts works in base two; precisely the shifts \(0,1,2\) work in base three; and precisely \(0,\ldots,7\) work in base four.

## Assumptions and scope

All integer quantifiers in the theorem range over \(b\ge2,d\ge0\); the support is infinite. Let \(\mathbb N_0=\{0,1,\ldots\}\). The graph \(\Gamma_D\) has distinct left vertices \(L_r\) and right vertices \(R_s\), for \(r,s\in\mathbb N_0\), and \(L_rR_s\) is an edge exactly when \(r+s\in D\). A forest contains no finite simple cycle.

For a \(k\)-element set \(S\subset\mathbb N_0\), let \(p_w^{\mathrm{ab}}(S)\) count the possible numbers of ones in \(w[n+S]\), as \(n\) ranges through \(\mathbb N_0\), and define \(p_w^{*\mathrm{ab}}(k)=\sup_{|S|=k}p_w^{\mathrm{ab}}(S)\). The term *Abelian pattern Sturmian* means equality with \(f(k)\) for every \(k\ge1\). These definitions and the characterization through \(\Gamma_D\) originate in [1], Theorem E, not in this result.

## Proof

**Step 1: all smaller shifts give forests.** Put \(a_j=b^j+d\). If \(b\ge3\) and \(0\le d<b(b-2)\), then for all \(j\ge2\),
\[
a_j-2a_{j-1}=(b-2)b^{j-1}-d>0.
\]
Assume for contradiction that a cycle in \(\Gamma_{D_{b,d}}\) uses an edge \(L_rR_s\) whose sum \(r+s=a_j\) is maximal among all its edge sums, for some \(j\ge2\). At each vertex, distinct incident cycle edges must have distinct sums: for a fixed sum and fixed endpoint, the opposite endpoint is unique. Thus the other incident edges at \(L_r\) and at \(R_s\) have sums at most \(a_{j-1}<a_j/2\). Nonnegativity then forces \(r<a_j/2\) and \(s<a_j/2\), contradicting \(r+s=a_j\).

It follows that every putative cycle can only use sums \(a_0,a_1\). Each fixed-sum layer is a matching. An alternating walk between its two layers, from one left vertex to the next, changes the left index by the fixed nonzero amount \(\pm(a_1-a_0)\), with signs alternating in a way that preserves the direction along a path. More explicitly, an alternating closed cycle would contain equally many transitions \(a_0\to a_1\) at right vertices, inducing successive left indices shifted by \(a_1-a_0>0\) in one orientation; no finite such orbit returns. Therefore the union of the first two layers has no cycle. Hence \(\Gamma_{D_{b,d}}\) is a forest, and Theorem E of [1] gives the claimed complexity formula. If \(b=2\), there are no integers \(d\ge0\) below the threshold \(b(b-2)=0\), so no sufficiency case is needed.

**Step 2: every shift at or beyond the boundary gives a cycle.** Let \(d\ge b(b-2)\), set \(\delta=b-1\) and \(t=d-b(b-2)\ge0\). The first three allowed sums are
\[
A=d+1=t+(b-1)\delta,\quad B=d+b=t+b\delta,\quad C=d+b^2=t+2b\delta.
\]
Take the following circular vertex sequence, with \(j=0,\ldots,b\):
\[
L_{t+b\delta},\ R_0,\ L_{t+(b-1)\delta},\ R_\delta,\ L_{t+(b-2)\delta},\ldots,\ L_t,\ R_{b\delta},\ L_{t+b\delta}.
\]
Each pair of successive distinct vertices is joined by an allowed edge: going from a left vertex with index \(t+(b-j)\delta\) to the right vertex with index \(j\delta\) has sum \(B\); from that right vertex (for \(j<b\)) to the next left vertex has sum \(A\); the final closing edge \(R_{b\delta}L_{t+b\delta}\) has sum \(C\). All \(b+1\) left indices and all \(b+1\) right indices are distinct. Thus this is a simple cycle of length \(2b+2\), and \(\Gamma_{D_{b,d}}\) is not a forest.

Theorem E of [1] proves the failure of minimal complexity. More quantitatively, the word contains gaps of zeros of unbounded lengths, so the all-zero infinite word belongs to its orbit closure; hence Theorem 7.4 of [1] applies to the cycle with \(r=b+1\), and yields the stated lower bound at \(k=\binom{b+2}{2}\). This completes both implications and the quantitative consequence.

## Verification

The accompanying standalone \(`verify.py`\) uses union-find to check cycles in finite additive-incidence subgraphs, including all first-three-support graphs for bases 2 through 9 and offsets through three times the squared base, and all first-five-support graphs for the allowed shifts in those bases. Separately it reconstructs all proposed cycles for bases 2 through 39 at three offsets each and checks every edge and the vertex distinctness. Running \(`python3 verify.py`\) gives:

```
FINITE_FOREST_CASES_OK 1056
CYCLE_FORMULAS_OK 114
VERIFY_OK
```

The exhaustive assertions are finite smoke tests. The unbounded theorem is proved by Step 1 and Step 2 together with the explicitly cited published graph–complexity equivalence. The proof does not rely on extrapolating the finite checks.

## Relationship to prior work

Zeng, Xue and Zeng [1] prove the general equivalence between Abelian pattern Sturmian words and acyclic additive-incidence graphs (Theorem E); give the stronger sufficient hypothesis that **every** successive support ratio exceeds two (Proposition 7.12); and record base-three unshifted extremality and base-two unshifted non-extremality (Example 7.13). Those statements and cases are not claimed as new. The new mathematical work here is the **sharp classification of all nonnegative additive shifts across every integer base**, including the critical boundary cycle and an explicit finite-size complexity gap. In particular the existing successive-ratio criterion does not cover the allowed positive shifts when the first ratio is at most two. Related two-dimensional Abelian maximal pattern complexity is discussed in [2] but does not supply this one-dimensional arithmetic classification.

## Limitations

The result only covers integer bases at least two, **nonnegative** integer additive shifts, and binary characteristic words. It does not determine exact nonextremal complexity above the lower-bound witness, nor the minimum possible length of a cycle. Priority remains subject to unindexed equivalent classifications, and no independent mathematical audit has been performed.

## References

1. Q. Zeng, Y. Xue and C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059 (first public 2026-09-23), Sections 1 and 7, Theorem E, Theorem 7.4, Proposition 7.12 and Example 7.13. https://arxiv.org/abs/2609.28059
2. Q. Zeng, Y. Xue and C. Zeng, *Abelian maximal pattern complexity of two-dimensional words*, arXiv:2608.21084 (first public 2026-08-21), related two-dimensional setting. https://arxiv.org/abs/2608.21084
