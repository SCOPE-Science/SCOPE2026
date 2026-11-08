# A loop-controlled sign transition for mutual-dyad and directed-triangle covariance

## Finding
Let \(n\geq3\) and let \(G\) be a random directed graph in which each of the \(n\) labeled vertices independently chooses exactly \(k\) *different* outgoing neighbors, uniformly among the allowed targets. Consider either convention: (i) self-loops are forbidden, so \(0\leq k\leq n-1\); or (ii) self-loops are allowed, so \(0\leq k\leq n\). There are no parallel arcs. Define \(R\) as the number of unordered distinct-vertex pairs with both directed arcs present. Define \(T\) as the number of oriented directed three-cycles on *three distinct vertices*. Both clockwise and counterclockwise cycles are counted when both occur, but cyclic rotations of a cycle are counted once. Self-loops, when allowed, contribute to neither statistic.

Set \(s=n-1\) for convention (i) and \(s=n\) for convention (ii), and put \(p=k/s\). Then
\[
\mathbb ER=\binom n2p^2,\qquad
\mathbb ET=\frac{n(n-1)(n-2)}3p^3.
\]
The exact finite-size covariance is
\[
\boxed{\operatorname{Cov}(R,T)=
\begin{cases}
-n(n-1)p^3(1-p)^2,&\text{self-loops forbidden},\\
n(n-2)p^3(1-p)(2p-1),&\text{self-loops allowed}.
\end{cases}}
\]
For every nondegenerate \(1\leq k\leq n-2\), the loopless covariance is strictly negative. In the loop-allowed model, for \(1\leq k\leq n-1\), it is negative when \(2k<n\), zero when \(2k=n\), and positive when \(2k>n\). The degenerate cases \(k=0\) and \(k=s\) have covariance zero. Thus merely permitting self-loops in the row-wise sampling space changes the sign pattern of two natural, distinct-vertex network motif counts, with a sharp threshold at half the targets.

For any fixed nonnegative integer \(k\), as \(n\to\infty\), both conventions satisfy \(n\operatorname{Cov}(R,T)\to-k^3\). If instead \(k/n\to\alpha\in(0,1)\), then the covariance divided by \(n^2\) tends to \(-\alpha^3(1-\alpha)^2\) without loops and \(\alpha^3(1-\alpha)(2\alpha-1)\) with loops.

## Assumptions and scope
An ordered arc indicator \(A_{uv}\) equals one when vertex \(u\) selects target \(v\). Selections at *different source vertices* are independent. Selections at the same source vertex are negatively associated because exactly \(k\) distinct targets must be chosen. Let
\[
R=\sum_{u<v}A_{uv}A_{vu},\qquad
T=\frac13\sum_{\substack{u,v,w\in[n]\\\text{pairwise distinct}}}
A_{uv}A_{vw}A_{wu}.
\]
The factor \(1/3\) removes the three possible rotations of an oriented cycle. This is a row-regular directed graph null model; the *indegrees are not fixed*. The theorem does not apply to fixed-indegree-and-outdegree configuration ensembles, to multigraph sampling with replacement, or to induced triad counts.

## Proof
The probability of any particular allowed outgoing arc is \(p=k/s\). For two *distinct* specified outgoing arcs from one vertex, their joint probability is
\[
r=\frac{k(k-1)}{s(s-1)},\qquad
r-p^2=-\frac{p(1-p)}{s-1}.
\]
Since a reciprocal pair requires arcs from two different source vertices and a simple directed triangle has exactly one arc from each of three source vertices, independence of the source rows gives the displayed expectations.

Expand \(\operatorname{Cov}(R,T)\) into covariances between indicators of reciprocal pairs and indicators of oriented triangles. If the two motifs have disjoint vertex sets, their indicators are independent. Every overlapping motif pair belongs to exactly one of the following classes.

**Two shared vertices.** Both endpoints of the reciprocal pair occur on the triangle, and the triangle necessarily uses one of the reciprocal arcs. There are \(n(n-1)(n-2)\) such ordered pairs of motif occurrences: for each oriented triangle there are three reciprocal-pair choices. Their joint expectation is \(p^2r\), because the extra reverse arc and one triangle arc leave exactly one source vertex required to choose two distinct targets. The product of marginal expectations is \(p^5\), so their contribution per occurrence is \(p^2(r-p^3)\).

**Exactly one shared vertex.** There are \(n(n-1)(n-2)(n-3)\) ordered pairs of motif occurrences. The common source vertex has two distinct specified outgoing arcs; every other involved source needs one. Their joint expectation is \(p^3r\), while their marginal-expectation product is again \(p^5\). The contribution per occurrence is \(p^3(r-p^2)\). The count vanishes automatically for \(n=3\).

Summing the only nonzero terms yields the exact general identity
\[
\operatorname{Cov}(R,T)
=n(n-1)(n-2)\left[p^2(r-p^3)+(n-3)p^3(r-p^2)\right].
\]
Substitute \(r-p^2=-p(1-p)/(s-1)\), and use \(r-p^3=(r-p^2)+p^2(1-p)\), to obtain
\[
\operatorname{Cov}(R,T)
=n(n-1)(n-2)\frac{p^3(1-p)}{s-1}
\left[p(s-n+2)-1\right].
\]
For \(s=n-1\) the bracket is \(p-1\), producing \(-n(n-1)p^3(1-p)^2\). For \(s=n\) it is \(2p-1\), producing \(n(n-2)p^3(1-p)(2p-1)\). All identities hold at the extremal allowed values of \(k\) as well, since \(s\geq2\). The sign classification follows directly. In the fixed-\(k\) regime, \(p=k/(n+O(1))\), and in the dense regime \(p\to\alpha\); substituting and dividing by the asserted powers of \(n\) proves the limits.

## Verification
Run \(\texttt{python verify_covariance.py}\) with the Python 3 standard library. The standalone checker verifies equality of the motif-overlap expression and the two closed forms at 952 parameter settings, and independently exhausts 218,118 labeled directed graphs across 27 small parameter settings for \(n=3,4,5\). In the exhaustive cases it checks \(\mathbb ER\), \(\mathbb ET\), and \(\operatorname{Cov}(R,T)\) using exact rational arithmetic. The finite checks detect normalization and small-size errors; the proof above establishes the unbounded claim.

## Relationship to prior work
Directed reciprocity and oriented triangles are established network motifs. Seshadhri, Pinar, Durak and Kolda [1] analyze directed closure rates, reciprocal and cyclic triad patterns, and approximate expectations in degree-aware configuration models. Their Section III.5 compares cyclic motifs with reciprocation in empirical networks; Section IV estimates closure rates under a different null model. Neither section states the exact \(\operatorname{Cov}(R,T)\) for independent uniform fixed-cardinality outgoing rows nor the all-\(k\) sign threshold. Durak, Kolda, Pinar and Seshadhri [2] construct a directed Chung–Lu-style null model matching prescribed in-, out- and reciprocal-degree distributions; its edge-generation mechanism is not independent uniform fixed-cardinality source rows. Roberts and Coolen [3] randomize directed binary networks while preserving full in- and out-degree sequences, another distinct model with different dependence constraints. The result here concerns the non-induced three-cycle count and exact covariance, not their directed closure ratios, empirical correlations, or fixed-double-degree randomization.

The sharp contrast between the two row-wise sampling conventions is a finite-sample null-model diagnostic: an observed correlation between reciprocity and cyclic feedback cannot be attributed to the same baseline mechanism without specifying the loop convention. Related formulas for reciprocity versus indegree-frequency counts do not imply this result, because \(T\) is not determined by the indegree distribution.

## Limitations
This is an exact covariance identity for the stated finite homogeneous row-regular ensemble. It does not give a joint distribution, concentration theorem, causal account of observed network closure, or universality for other graph models. Small-size enumeration is not a proof beyond its checked cases. Searches and primary-source inspection do not establish historical uniqueness: an older general motif-covariance or multivariate subgraph enumerator could implicitly imply the formulas. That priority risk remains open for independent historical review.

## References
[1] C. Seshadhri, A. Pinar, N. Durak, and T. G. Kolda, *Directed closure measures for networks with reciprocity*, first publicly submitted February 25, 2013, arXiv:1302.6220. https://arxiv.org/abs/1302.6220 ; full text https://arxiv.org/html/1302.6220v3 .

[2] N. Durak, T. G. Kolda, A. Pinar, and C. Seshadhri, *A Scalable Null Model for Directed Graphs Matching All Degree Distributions: In, Out, and Reciprocal*, first publicly submitted October 19, 2012, arXiv:1210.5288. https://arxiv.org/abs/1210.5288 ; full text https://arxiv.org/html/1210.5288v4 .

[3] E. S. Roberts and A. C. C. Coolen, *Unbiased degree-preserving randomisation of directed binary networks*, first publicly submitted December 20, 2011, arXiv:1112.4677. https://arxiv.org/abs/1112.4677 .
