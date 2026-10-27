# A minimal strict-domination witness for greedy zero-error side-information coarsening

## Finding

Consider the zero-error source-coding problem in which an encoder observes \(X\) and \(g(Y)\), while a decoder observes \(Y\) and must recover \(f(X,Y)\) with zero error. Let \(X\) be uniform on \(\mathcal X=\{0,1,2\}\), let \(Y\) be independent of \(X\), and set
\[
P_Y(a,b,c,d)=\frac1{15}(4,5,5,1).
\]
Define \(f:\mathcal X\times\mathcal Y\to\{0,1,2\}\) by
\[
f(\cdot,a)=(1,0,0),\quad f(\cdot,b)=(0,1,0),\quad
f(\cdot,c)=(0,0,1),\quad f(\cdot,d)=(0,1,2),
\]
where each tuple lists outputs for \(x=0,1,2\), respectively. The joint law has full support.

For a partition \(\mathcal A\) of \(\mathcal Y\), let \(g_{\mathcal A}\) label its blocks. The greedy coarsening rule of Charpenay–Le Treust–Roumy chooses a merge maximizing
\[
\frac{R^*(g_{\mathcal B})-R^*(g_{\mathcal A})}
{H(g_{\mathcal B}(Y))-H(g_{\mathcal A}(Y))}.
\]
Starting from the singleton partition, the unique maximizing first merge is \(\{b,c\}\). The resulting partition
\[
\mathcal P=\{\{a\},\{b,c\},\{d\}\}
\]
is strictly dominated in both entropy and rate by
\[
\mathcal Q=\{\{a,b,d\},\{c\}\}.
\]
The exact gaps are
\[
H(g_{\mathcal P}(Y))-H(g_{\mathcal Q}(Y))
=\frac{5\log_2 5-8}{15}>0
\]
and
\[
R^*(g_{\mathcal P})-R^*(g_{\mathcal Q})=\frac{2}{45}>0.
\]
Thus the greedy path need not consist solely of Pareto-undominated points, even when its first merge is unique.

This failure is dimension-minimal for strict domination in both coordinates: it cannot occur for \(|\mathcal X|\le2\) or for \(|\mathcal Y|\le3\).

## Assumptions and scope

All alphabets are finite. The joint law is \(P_{X,Y}=P_XP_Y\), with \(P_X\) uniform and \(P_Y(a,b,c,d)=(4,5,5,1)/15\), so every pair \((x,y)\) has positive probability. Entropies and rates are measured in bits. The claim concerns the first nontrivial partition returned by the specified slope-maximizing coarsening algorithm, not the optimal value of the full coding problem.

For full-support \(P_{X,Y}\), the single-letter rate formula is
\[
R^*(g)=H(j(X,g(Y))\mid g(Y)),\qquad
j(x,z)=\bigl(f(x,y)\bigr)_{y\in g^{-1}(z)}.
\]
Within each block \(B\), \(X\) is identified by the tuple \((f(X,y))_{y\in B}\). The induced partition of \(\mathcal X\) is the common refinement of the output partitions for the individual \(y\in B\).

Write \(h(p)=-p\log_2p-(1-p)\log_2(1-p)\) and \(L=\log_2 3\). Each singleton block \(a,b,c\) induces output-class entropy \(h(1/3)=L-2/3\); singleton \(d\) induces entropy \(L\). Any block containing at least two distinct symbols of \(\mathcal Y\) induces the discrete partition of \(\mathcal X\), hence entropy \(L\).

## Proof

Let \(h=h(1/3)=L-2/3\). At the singleton partition \(\mathcal I\),
\[
R^*(g_{\mathcal I})=\frac{14h+L}{15}.
\]
Merging two blocks changes the rate by a nonnegative amount and decreases \(H(g(Y))\), so each slope is nonpositive. For a first merge of symbols \(i,j\) with masses \(p_i,p_j\), the entropy decrease is
\[
(p_i+p_j)h\!\left(\frac{p_i}{p_i+p_j}\right).
\]
The rate increase is \((p_i+p_j)(L-h)\) if both symbols are among \(a,b,c\), and \(p_i(L-h)\) if one symbol is \(d\) and the other is among \(a,b,c\). Here \(L-h=2/3\).

The six possible slopes are
\[
s_{bc}=-\frac23;\qquad
s_{ab}=s_{ac}=-\frac{2/3}{h(4/9)};
\]
\[
s_{ad}=-\frac{8}{15h(4/5)};\qquad
s_{bd}=s_{cd}=-\frac{5}{9h(1/6)}.
\]
Since \(h(4/9)<1\), \(h(4/5)<4/5\), and \(h(1/6)<5/6\), every slope other than \(s_{bc}\) is strictly smaller than \(-2/3\). For the latter two inequalities, use
\[
h(4/5)=\log_2 5-\frac85<\frac45
\]
because \(5^5<2^{12}\), and
\[
6h(1/6)=\log_2\!\left(\frac{6^6}{5^5}\right)<5
\]
because \(6^6<32\cdot5^5\). Thus \(b,c\) is the unique maximizing merge.

For \(\mathcal P=\{\{a\},\{b,c\},\{d\}\}\),
\[
H(g_{\mathcal P}(Y))=H(4/15,10/15,1/15),\qquad
R^*(g_{\mathcal P})=\frac{4h+11L}{15}.
\]
For \(\mathcal Q=\{\{a,b,d\},\{c\}\}\),
\[
H(g_{\mathcal Q}(Y))=h(1/3)=L-\frac23,\qquad
R^*(g_{\mathcal Q})=\frac{10L+5h}{15}.
\]
Subtracting rates gives
\[
R^*(g_{\mathcal P})-R^*(g_{\mathcal Q})
=\frac{L-h}{15}=\frac{2}{45}>0.
\]
Expanding the block-mass entropies gives
\[
H(4/15,10/15,1/15)-h(1/3)
=\frac{5\log_2 5-8}{15}>0,
\]
where positivity follows from \(5^5>2^8\). Hence \(\mathcal Q\) is strictly better on both coordinates.

It remains to prove dimension-minimality.

Rate is nondecreasing under partition coarsening: merging two blocks replaces their output-class partitions of \(\mathcal X\) by their common refinement, whose entropy is at least that of either partition. Thus the one-block partition cannot strictly dominate a two-block partition by having a smaller rate.

If \(|\mathcal Y|\le3\), every non-endpoint partition on a greedy coarsening path is a two-block partition obtained by one merge from the singleton partition. If another two-block partition had both smaller entropy and smaller rate, it would have a larger entropy decrease and a smaller rate increase from the singleton partition, hence a strictly larger slope. The greedy rule would choose it instead. Therefore strict domination in both coordinates is impossible for \(|\mathcal Y|\le3\).

If \(|\mathcal X|\le2\), each \(y\) either makes \(f(\cdot,y)\) constant or distinguishes the two source symbols. A block containing any distinguishing \(y\) has output-class entropy \(H(X)\); a block containing only constant columns has entropy \(0\). Merging two blocks of the same type leaves the rate unchanged and has slope \(0\); merging a distinguishing block with a constant-only block increases the rate and has negative slope. The greedy rule therefore performs all available same-type merges before the final mixed merge. Every intermediate point has the minimum rate, or is the final one-block endpoint, so no point along the path is strictly dominated in both coordinates. This proves the asserted minimality.

## Verification

The included standard-library script `verify.py` reconstructs the six first-merge slopes from the displayed block-mass formula, confirms that \(b,c\) is the unique maximizer, and numerically checks both gap formulas. The analytic proof above establishes the inequalities and dimension-minimality; floating-point checks are supplementary and are not used as proof.

## Relationship to prior work

Charpenay, Le Treust, and Roumy give the full-support formula \(R^*(g)=H(j(X,g(Y))\mid g(Y))\) and later introduce the greedy coarsening algorithm for side-information design. Their design paper describes the algorithm as returning achievable points and presents an example where its resulting boundary coincides with the Pareto front. It does not claim that every greedy output is Pareto-undominated. The present result adds a fully specified instance with a unique first merge that is strictly dominated in both coordinates, plus a proof that these two-coordinate failures require at least three source symbols and four side-information symbols. It is a limitation witness for the heuristic, not a contradiction of a general optimality claim in the source.

## Limitations

The counterexample concerns the specified full-support instance and the stated slope-maximizing coarsening rule. It does not characterize all greedy trajectories, quantify worst-case approximation loss, or imply that the algorithm fails on every nontrivial instance. The strict gaps are exact for this instance. The literature comparison is not a proof of global novelty; unindexed or unpublished equivalent examples remain a residual priority risk.

## References

1. N. Charpenay, M. le Treust, and A. Roumy, “Optimal Zero-Error Coding for Computing under Pairwise Shared Side Information,” arXiv:2211.03649v1, first submitted 2022-11-07. Theorem IV.8 gives the full-support single-letter rate formula. https://arxiv.org/abs/2211.03649
2. N. Charpenay, M. le Treust, and A. Roumy, “Side Information Design in Zero-Error Coding for Computing,” *Entropy* 26(4), 338 (2024), first published 2024-04-16. Section 4.2, Algorithms 1–2, and equations (30)–(31) define the coarsening and refining rules. https://doi.org/10.3390/e26040338
