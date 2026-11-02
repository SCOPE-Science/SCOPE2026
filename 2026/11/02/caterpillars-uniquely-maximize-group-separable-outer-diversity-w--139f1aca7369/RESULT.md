# Caterpillars uniquely maximize group-separable outer diversity, with a sharp runner-up gap

## Finding

Let \(m\ge 2\), and let \(T\) range over full rooted binary trees whose \(m\) leaves are labeled by distinct alternatives. Its group-separable domain \(\mathrm{GS}(T)\) consists of all rankings obtained by independently reversing the two child blocks at any internal node. For a uniformly random strict ranking \(V\), let
\[
D(T)=\mathbb E\left[\min_{\pi\in\mathrm{GS}(T)}d_{\mathrm K}(V,\pi)\right],
\qquad
\operatorname{outdiv}(T)=1-\frac{2D(T)}{\binom m2},
\]
where \(d_{\mathrm K}\) is Kendall's adjacent-swap distance. Set
\[
F_m=\frac{(m-1)(m-2)}8+\frac14\sum_{j=1}^{\lfloor(m-1)/2\rfloor}\frac{1}{2j+1}.
\]
**Theorem.** Every such tree satisfies \(D(T)\ge F_m\), with equality exactly for caterpillar trees (every internal vertex has a leaf child). For \(m\ge4\), every noncaterpillar satisfies the sharp stronger bound
\[
D(T)\ge F_m+\frac16.
\]
Equality in this second bound holds exactly for a tree obtained from a four-leaf root split \((2,2)\) by successively adjoining single leaves above its root. Thus caterpillars are the unique maximizers of outer diversity up to alternative relabeling, and the second-largest achievable outer diversity is exactly
\[
1-\frac{2F_m}{\binom m2}-\frac{1}{3\binom m2}.
\]
For \(m=2,3\) all full rooted binary-tree shapes are caterpillars, so the second-largest value is not defined.

## Assumptions and scope

An internal node has exactly two children; child-order reversals are independent, and leaves are distinct. The average is over all \(m!\) strict rankings with equal probability. The theorem compares every such tree shape, not arbitrary preference domains of the same cardinality or distances for correlated multi-voter elections. The unnormalized gap \(1/6\) concerns expected Kendall swaps, not the normalized outer-diversity value.

For a node with child subtrees of sizes \(a,b\ge1\), let \(U_{a,b}\) be the number of pairs in which a leaf from the second child occurs before a leaf from the first in a uniformly random interleaving of the two blocks. Define the local optimum
\[
g(a,b)=\mathbb E\min\{U_{a,b},ab-U_{a,b}\}.
\]
The order within either child is irrelevant to this local count.

## Proof

**1. Exact decomposition.** Every pair of distinct leaves belongs to the two different child subtrees of a unique lowest common ancestor. To transform a ranking into \(\mathrm{GS}(T)\), each node's two child blocks must occur in one of their two orders. This changes only cross-child pairs at that node; relative orders inside each child are optimized separately. The minimum number of swaps is therefore the sum of the separate minimum cross-child inversion counts over all internal nodes. Taking expectations, and using that a uniformly random ranking induces uniform interleavings and uniform restrictions within each subtree, gives
\[
D(T)=\sum_{v\text{ internal}}g(a_v,b_v).
\]
This agrees with, and follows directly from, the exact node-cost decomposition in Faliszewski et al., *Outer Diversity of Condorcet Domains*, Lemmas A.1–A.3 (2026).

**2. Exact caterpillar cost.** When one block has size \(1\) and the other size \(k\), the number \(U_{1,k}\) is uniform on \(\{0,\ldots,k\}\). Summation gives
\[
g(1,k)=\begin{cases}
(k-1)/4,&k\text{ odd},\\
(k-1)/4+1/[4(k+1)],&k\text{ even}.
\end{cases}
\]
A caterpillar is built by repeatedly attaching one new leaf to the preceding tree, so its cost is \(F_m=\sum_{k=1}^{m-1}g(1,k)\). Summing the displayed formulas yields exactly the expression for \(F_m\) in the theorem, with \(F_1=0\).

**3. Universal mixed-block bound.** We prove
\[
g(a,b)\ge \frac{ab}{4}\qquad\text{for all integers }a,b\ge2.
\]
Write \(n=a+b\) and let \(P_1<\cdots<P_a\) be the positions of the first block within a uniformly chosen size-\(a\) subset of \(\{1,\ldots,n\}\). Then \(U_{a,b}=\sum_i(P_i-i)\). The finite-population sampling identities give
\[
\mathbb E U_{a,b}=ab/2,\qquad
\operatorname{Var}(U_{a,b})=ab(a+b+1)/12.
\]
Consequently, by Cauchy–Schwarz,
\[
g(a,b)=ab/2-\mathbb E|U_{a,b}-ab/2|
\ge ab/2-\sqrt{ab(a+b+1)/12}.
\]
The right-hand side is at least \(ab/4\) provided \(3ab\ge4(a+b+1)\). By symmetry assume \(2\le a\le b\). The condition holds except at \((a,b)=(2,2),(2,3),(2,4),(2,5),(3,3)\). Direct exact enumeration of the \(\binom{a+b}{a}\) interleavings yields, in that order,
\[
g(a,b)=1,\quad 8/5,\quad 34/15,\quad 61/21,\quad 13/5.
\]
Each is at least \(ab/4\), establishing the bound for all positive block sizes \(a,b\ge2\). These five checks are finite exact sums, not approximations to the universal claim.

**4. Every genuine branch incurs a uniform surcharge.** Put
\[
S_r=\sum_{j=1}^{\lfloor r/2\rfloor}\frac{1}{2j+1}.
\]
For \(a+b=n\), the formula in Step 2 gives
\[
F_n-F_a-F_b=\frac{ab-1}{4}
+\frac{S_{n-1}-S_{a-1}-S_{b-1}}4.
\]
When \(a,b\ge2\), define \(p=\lfloor(a-1)/2\rfloor\), \(q=\lfloor(b-1)/2\rfloor\), and \(r=\lfloor(a+b-1)/2\rfloor\). As \(r\le p+q+1\) and the summands \(1/(2j+1)\) decrease strictly, the difference \(S_{n-1}-S_{a-1}-S_{b-1}\) is bounded above by \(1/(2q+3)\le1/3\). Equality with \(1/3\) forces \(a=b=2\) (otherwise an initial omitted positive denominator or a larger denominator makes it strict). Hence
\[
F_n-F_a-F_b\le\frac{ab}{4}-\frac16,
\]
with equality only for \((a,b)=(2,2)\). Together with Step 3 this proves
\[
\delta(a,b):=g(a,b)-(F_{a+b}-F_a-F_b)\ge1/6
\quad(a,b\ge2),
\]
with equality only for the split \((2,2)\). If one side is a singleton, Step 2 instead gives \(\delta(1,b)=0\) exactly.

**5. Telescope over the tree.** Summing the last definition over the internal nodes, every nonroot term \(F_{|T_v|}\) cancels against its parent's negative child term, and all leaf terms vanish because \(F_1=0\). Thus
\[
D(T)-F_m=\sum_{v\text{ internal}}\delta(a_v,b_v).
\]
All summands are nonnegative. They all vanish precisely when every internal node has a singleton child, which characterizes a caterpillar. Otherwise at least one internal node has both child sizes at least \(2\), giving a surcharge of at least \(1/6\). Equality requires exactly one nonsingleton split, necessarily \((2,2)\), and all other splits must have singleton children. Such a tree is exactly a four-leaf balanced core with zero or more successive outer singleton attachments. Those trees exist for every \(m\ge4\), so both the minimum and runner-up bound are sharp, including their equality cases.

Finally, \(\operatorname{outdiv}=1-2D/\binom m2\) reverses the ordering of costs and converts the raw gap of \(1/6\) into an outer-diversity gap of \(1/(3\binom m2)\). This completes the proof.

## Verification

The accompanying standalone `verify.py` uses exact integer and rational arithmetic. It independently computes interleaving inversion counts both by dynamic programming and by explicit position-subset enumeration for all \(1\le a,b\le8\), verifies the five exceptional local values, checks the cross-block inequality on 300 pairs with \(2\le a\le b\le25\), enumerates all unlabeled full binary-tree shapes through \(m=14\) (2,179 shapes at the largest size), and confirms the unique optimum and runner-up shape. For every tree shape on at most six leaves it also computes the expected minimum Kendall distance directly over all strict rankings and all rankings in the represented group-separable domain, independently checking the node-cost formula. Run `python verify.py` from the folder containing the file. The analytical argument, not these finite tests, proves the unbounded theorem.

## Relationship to prior work

Faliszewski, Jabrocki, Słuszniak, Sornat, Szufa and Wąs (2026), *Outer Diversity of Condorcet Domains*, arXiv:2610.00720v1, first made public September 30, 2026, developed an exact \(O(m^4)\) algorithm to evaluate outer diversity for an arbitrary binary group-separable tree (Theorem 4.3) and to select an optimum at any specified size (Theorem 4.5). Its Finding 4.4 reports that the caterpillar wins for all tested sizes up to 100; the text does not derive an all-size characterization or a next-best gap. The exact caterpillar cost \(F_m\) also follows from its Theorem 4.6 and is treated here as previously established, not as a new theorem.

Faliszewski, Sornat, Szufa and Wąs (2026), *Outer Diversity of Structured Domains*, arXiv:2602.15708v1, explicitly raised whether caterpillars are the most outer-diverse group-separable domain. Faliszewski et al. (2026), *Nearly Group-Separable Elections*, arXiv:2609.33535v1, studies the different task of changing whole elections into structured profiles and does not provide this expectation extremum. The new mathematical content here is the uniform mixed-block inequality and its sharp telescoping surcharge, converting finite observations into a proof for all sizes and identifying the unique runner-up shape.

## Limitations

The result assumes the complete impartial-culture distribution over individual strict rankings, binary block-reversal trees, and Kendall/adjacent-swap distance. It does not establish maximum outer diversity over all Condorcet domains, all arbitrary preference domains of size \(2^{m-1}\), or any analogous ordering for correlated profiles or alternative distances. Scientific novelty remains subject to possible unindexed equivalent prior results; independent scholarly validation has not been performed.

## References

1. P. Faliszewski, J. Jabrocki, M. Słuszniak, K. Sornat, S. Szufa and T. Wąs, *Outer Diversity of Condorcet Domains*, arXiv:2610.00720v1 (September 30, 2026), https://arxiv.org/html/2610.00720v1 . Relevant material: Sections 2.1–2.2 and 4, Appendix A.3–A.5.
2. P. Faliszewski, K. Sornat, S. Szufa and T. Wąs, *Outer Diversity of Structured Domains*, arXiv:2602.15708v1 (February 17, 2026), https://arxiv.org/html/2602.15708v1 . Relevant material: Sections 3 and 5.2.
3. P. Faliszewski, J. Jabrocki, S. Kaźmierowski, K. Pekárková, Š. Schierreich and I. Schlotter, *Nearly Group-Separable Elections*, arXiv:2609.33535v1 (September 27, 2026), https://arxiv.org/html/2609.33535v1 . Relevant material: introduction and Sections 2–4.
