# Positive connectivity correlation and exact equality on weighted cactus forests

## Finding

Let \(G=(V,E)\) be any finite connected simple cactus graph, so each edge belongs to at most one simple cycle. Give every edge a strictly positive weight \(w_e\). Sample an acyclic edge set \(F\subseteq E\) with probability proportional to \(\prod_{e\in F}w_e\). For arbitrary distinct \(u,v\in V\) and distinct \(x,y\in V\) (the two pairs may intersect),

\[
\operatorname{Cov}\bigl(\mathbf 1_{\{u\leftrightarrow v\}},\mathbf 1_{\{x\leftrightarrow y\}}\bigr)\ge 0.
\]

In fact, the covariance is strictly positive precisely when the two unique block-tree routes share either (i) a bridge, or (ii) a cycle block for which the two partitions into complementary arcs have nonempty opposite intersection cells in one diagonal. Otherwise it is exactly zero. The assertion holds simultaneously for every choice of positive, nonuniform edge weights, with no high-fugacity assumption.

For an explicit cycle block \(C\), let \(A_1,A_2\) be its two edge arcs connecting the entry and exit vertices for the first pair, and \(B_1,B_2\) the analogous arcs for the second pair. Put \(Q_{ij}=A_i\cap B_j\), \(q_e=1/w_e\), and \(t_{ij}=\prod_{e\in Q_{ij}}(1+q_e)\). Then the local covariance equals \((ZH-RS)/Z^2\), where

\[
\begin{aligned}
Z&=t_{11}t_{12}t_{21}t_{22}-1,\\
R&=t_{11}t_{12}+t_{21}t_{22}-2,\\
S&=t_{11}t_{21}+t_{12}t_{22}-2,\\
H&=t_{11}+t_{12}+t_{21}+t_{22}-4.
\end{aligned}
\]

The numerator \(ZH-RS\) has an explicit nonnegative polynomial decomposition proved below. The formula is valid for empty cells, whose product is one.

## Assumptions and scope

A cactus is a finite connected simple graph in which any two simple cycles share at most one vertex; this is equivalent to each edge lying in at most one simple cycle. Its blocks are bridges or simple cycles. Edges have arbitrary finite real \(w_e>0\), with no normalization or uniformity condition. A spanning forest means any acyclic spanning edge subset; isolated vertices are permitted. Distinctness is required within each marked pair, but not across pairs. Connectivity is connectivity using the sampled forest edges, not connectivity in the host graph. An empty set of block demands contributes a probability factor one.

## Proof

**1. Independent block laws.** A selected subset is acyclic if and only if it fails to contain the full edge set of every cycle block. No other cycles exist in a cactus. As the blocks are edge-disjoint, the weighted forest partition function is a product of bridge factors \(1+w_e\) and cycle factors \(\prod_{e\in C}(1+w_e)-\prod_{e\in C}w_e\). Thus the restrictions of the random forest to distinct blocks are independent. A bridge is present with probability \(w_e/(1+w_e)\), strictly between zero and one.

**2. Pair-connection events factor into local block demands.** The block-cut incidence graph is a tree. Fix distinct vertices \(u,v\). The unique route through this tree specifies a sequence of blocks with entry and exit vertices. Any forest path between \(u,v\) must connect those vertices within every visited block. Conversely, all these local connections join to a global forest path. Hence \(\{u\leftrightarrow v\}\) is the intersection of independent block events along that route. The same statement holds for \(x,y\). For blocks outside a route, take the corresponding local event to be certain.

**3. Exact two-event correlation on a cycle.** On a cycle block, write \(M\) for the set of absent edges. The forest condition is \(M\neq\varnothing\); after dividing all weights by the common factor \(\prod_{e\in C}w_e\), a missing set has unnormalized mass \(\prod_{e\in M}q_e\), with \(q_e=w_e^{-1}>0\). The normalizing mass is \(Z=\prod_{e\in C}(1+q_e)-1>0\).

For either local endpoint pair, the two complementary arcs \(A_1,A_2\) partition the cycle edges. That pair is connected in the forest if and only if *all* missing edges lie in one arc: the complementary arc then remains a complete path. The two admissible families of nonempty missing sets are disjoint; hence the corresponding unnormalized event mass is \(R=t_{11}t_{12}+t_{21}t_{22}-2\). For the second pair it is \(S=t_{11}t_{21}+t_{12}t_{22}-2\). Both local connections hold exactly if \(M\) lies in one intersection cell \(Q_{ij}\); again these four nonempty-missing-set families are disjoint. Their total unnormalized mass is \(H=\sum_{i,j}(t_{ij}-1)\). Therefore the covariance is \(H/Z-(R/Z)(S/Z)=(ZH-RS)/Z^2\).

Set \(a=t_{11}-1\), \(b=t_{12}-1\), \(c=t_{21}-1\), \(d=t_{22}-1\), all nonnegative. Write \(X=a+d\), \(Y=b+c\), \(P=ad\) and \(Q=bc\). Direct expansion gives the polynomial identity

\[
ZH-RS=P X(1+Y+Q)+QY(1+X+P)+PY+QX+4PQ\ge0.
\]

Since \(a,b,c,d\ge0\), this expression is strictly positive if and only if \(P>0\) or \(Q>0\). Here \(P>0\) means that the two opposite cells \(Q_{11},Q_{22}\) are both nonempty, and \(Q>0\) means that \(Q_{12},Q_{21}\) are both nonempty, since every \(q_e>0\). Thus the asserted exact cycle-block equality criterion follows. A block encountered by only one marked pair has certain local event for the other, hence local covariance zero.

**4. Product preservation and strictness.** Let \(E_B,D_B\) be the local block demands, with \(E_B\) or \(D_B\) identically true outside the relevant route. The independence in Step 1 gives

\[
\Pr(u\leftrightarrow v,\ x\leftrightarrow y)=\prod_B\Pr(E_B\cap D_B),\qquad
\Pr(u\leftrightarrow v)\Pr(x\leftrightarrow y)=\prod_B\Pr(E_B)\Pr(D_B).
\]

On a bridge demanded by both pairs, \(E_B=D_B=\{\text{bridge present}\}\), with strictly positive covariance \(p_B(1-p_B)\). On a cycle demanded by both, Step 3 proves local nonnegative covariance and the stated strict criterion. All local marginal and joint connection probabilities are strictly positive, since choosing every bridge and all but one edge of each cycle produces a valid local connection configuration of positive weight. Every factor on the left therefore dominates the corresponding factor on the right, strictly precisely if some shared block satisfies its strict criterion. Multiplication proves both the global inequality and the global exact equality characterization. \(\square\)

## Verification

The accompanying dependency-free `verify.py` executes exact-rational exhaustive checks of all ordered pairs of distinct vertex pairs for nine nonuniformly weighted cactus examples, including single cycles, two attached cycles, and a bridge-attached cycle. It checks 2,145 pair-pair covariance inequalities across 701 proper forest edge sets and 256 exact integer evaluations of the stated polynomial decomposition and strictness criterion. These finite computations corroborate the proof but do not replace the all-graphs argument in Steps 1–4. Reproduce using `python3 verify.py` in the extracted package directory.

## Relationship to prior work

Çiçeksiz and Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model*, arXiv:2610.00549v1 (publicly submitted September 30, 2026), formulate positive covariance of arbitrary vertex-pair connectivity indicators as Conjecture 6.2. Their Proposition 6.1 gives a leading large-uniform-fugacity result for a related setup, and their Example 6.4 exhibits a four-vertex polynomial, but neither proves this all-positive-weights cactus theorem or the strictness criterion. They also study a distinct negative-correlation question for individual edge indicators. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs* (arXiv:1008.3660), proves the latter edge-indicator property for a wider graph class; that theorem does not assert positive correlations of connectivity events. Grimmett and Winkler (arXiv:math/0302185) discuss negative association of edge inclusion in forest and connected-subgraph models, likewise distinct from the claimed connectivity assertion.

## Limitations

The theorem covers the unrooted finite weighted forest law on connected cactus graphs, not arbitrary series-parallel graphs, general overlapping-cycle graphs, random-cluster measures at fixed \(q>0\), or an assertion of positive association for all increasing events. This is a theorem about **pairs of vertex-connectivity indicators**, not pairwise positive correlation of edge-inclusion indicators. The exact equality criterion presumes strictly positive weights. Literature comparisons are bounded and do not prove global priority; an equivalent older cactus-specific statement cannot be excluded. Independent scientific validation has not been performed.

## References

1. R. A. Çiçeksiz and M. Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model*, arXiv:2610.00549v1, September 30, 2026, especially Section 6, Proposition 6.1, Conjecture 6.2 and Example 6.4; https://arxiv.org/html/2610.00549v1.
2. A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, arXiv:1008.3660, 2010; https://arxiv.org/abs/1008.3660.
3. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185; https://arxiv.org/abs/math/0302185.
