# Smallest-blade law for total-variation stability of clique-bouquet heat semigroups

## Finding

Let a clique bouquet have \(m\ge1\) blades of positive integer sizes \(k_1,\ldots,k_m\). Write \(K=\sum_{i=1}^{m}k_i\) and \(k_*=\min_i k_i\). If \(L\) is its ordinary combinatorial Laplacian and \(H_t=e^{-tL}\), then the sharp logarithmic operator norm for graph edge-total-variation is
\[
\mu=K-2k_*-1.
\]
More precisely, the variation-seminorm operator norm \(N(t)\) satisfies
\[
N(t)=1+\mu t+O(t^2)\quad(t\downarrow0),\qquad
N(t)\le e^{\mu t}\quad(t\ge0).
\]
Hence all-time total-variation contraction holds for every real input exactly when
\[
K\le 2k_*+1.
\]
The bound and threshold are sharp, and the indicator of a smallest entire blade supplies an explicit infinitesimal extremizer. If the inequality fails, this indicator exhibits strict amplification for all sufficiently small positive times.

For a single blade the graph is complete and always contracts. For two blades the criterion reduces to \(|k_1-k_2|\le1\). For three blades the unique contractive bouquet, up to graph isomorphism, is the three-leaf star; for four or more blades no such graph contracts.

## Assumptions and scope

The graph is finite, simple and undirected. It has one distinguished hub \(o\), joined to each vertex of \(m\) disjoint cliques \(B_i\) of cardinality \(k_i\ge1\). Every induced subgraph on \(\{o\}\cup B_i\) is complete; there are no edges between different blades. Every edge has conductance one, and every vertex has counting mass one. For all functions \(f:V(G)\to\mathbb R\), define
\[
(Lf)(u)=\sum_{v\sim u}(f(u)-f(v)),\qquad
J(f)=\sum_{\{u,v\}\in E(G)}|f(u)-f(v)|.
\]
Let \(H_t=e^{-tL}\) for \(t\ge0\). Because \(H_t\) preserves constants, its finite induced operator norm \(N(t)=\sup_{J(f)>0}J(H_tf)/J(f)\) is well-defined on functions modulo constants. The assertion includes all real-valued signals, all positive integer blade sizes, and all times \(t\ge0\).

## Proof

**1. Directional variation derivative for a cut.** For \(f\in\mathbb R^{V(G)}\), let \(D(f)\) be the right derivative at zero of \(J(e^{-tL}f)\). For each undirected edge and \(g=-Lf\), its contribution to \(D(f)\) is \(\operatorname{sgn}(f(u)-f(v))(g(u)-g(v))\) when the edge difference is nonzero, and \(|g(u)-g(v)|\) when it vanishes.

Since a cut and its complement have identical variation derivatives, consider an indicator of a set excluding the hub. Suppose the set has \(x_i\) selected vertices in blade \(B_i\), where \(0\le x_i\le k_i\) and \(x_i\) is an integer. Write \(X=\sum_i x_i\). The values of \(L\mathbf1_S\) at the hub, selected vertices of blade \(i\), and unselected vertices of blade \(i\) are, respectively,
\[
-X,\qquad k_i+1-x_i,\qquad -x_i.
\]
Counting the hub-to-selected, hub-to-unselected, and within-blade selected-to-unselected edges gives the exact formulas
\[
J(\mathbf1_S)=\sum_i x_i(k_i+1-x_i),
\]
\[
D(\mathbf1_S)
=X(K-2X)-\sum_i\bigl[(k_i^2+3k_i+1)x_i-(k_i+3)x_i^2\bigr].
\]
The second formula includes the absolute derivatives along edges that have zero initial difference.

**2. Sharp cut inequality by separate convexity.** Set \(\mu=K-2k_*-1\) and \(F(x_1,\ldots,x_m)=D(\mathbf1_S)-\mu J(\mathbf1_S)\), using the preceding polynomial expressions extended to the real box \(\prod_i[0,k_i]\). For fixed coordinates other than \(x_i\), the coefficient of \(x_i^2\) is
\[
k_i+1+\mu=k_i+K-2k_*\ge0.
\]
Thus \(F\) is convex separately in every coordinate, so its maximum on the box occurs at a corner with all \(x_i\in\{0,k_i\}\). At a corner \(X=\sum_{i\in I}k_i\), each chosen blade is entirely selected, and
\[
J=X,\qquad D=X(K-2X-1),\qquad F=2X(k_*-X)\le0,
\]
because either \(X=0\) or \(X\ge k_*\). Hence \(D(\mathbf1_S)\le\mu J(\mathbf1_S)\) for every cut. Selecting exactly one smallest blade gives \(X=k_*\) and equality:
\[
D(\mathbf1_{B_*})=\mu J(\mathbf1_{B_*})=\mu k_*.
\]

**3. Extension to arbitrary real signals.** List the distinct levels of \(f\) as \(a_1<\cdots<a_q\). The finite coarea decomposition is
\[
f=a_1\mathbf1+\sum_{j=2}^{q}(a_j-a_{j-1})\mathbf1_{\{f\ge a_j\}},\qquad
J(f)=\sum_{j=2}^{q}(a_j-a_{j-1})J(\mathbf1_{\{f\ge a_j\}}).
\]
On any edge with nonzero initial \(f\)-difference, the contributing cuts all carry the same sign; on a zero-difference edge the ordinary triangle inequality bounds the absolute directional derivative of their sum. Since \(-L\) is linear, summing over edges yields
\[
D(f)\le\sum_{j=2}^{q}(a_j-a_{j-1})D(\mathbf1_{\{f\ge a_j\}})\le\mu J(f).
\]
This also covers constant signals, for which both sides vanish.

**4. All-time bound, optimality and classification.** Apply the preceding inequality to \(H_t f\). The nonnegative function \(t\mapsto J(H_t f)\) is locally Lipschitz and obeys the right-derivative inequality \(D^+J(H_t f)\le\mu J(H_t f)\). Gronwall's inequality gives \(J(H_t f)\le e^{\mu t}J(f)\). Therefore \(N(t)\le e^{\mu t}\). For the indicator of a smallest blade, its exact initial derivative is \(\mu J\), whence \(N(t)\ge1+\mu t+O(t^2)\) as \(t\downarrow0\); the matching upper bound from the exponential yields \(N(t)=1+\mu t+O(t^2)\). If \(\mu>0\), this indicator increases variation strictly for small positive time. If \(\mu\le0\), the exponential bound proves contraction for all time.

Finally, \(K\le2k_*+1\) always holds for \(m=1\); for \(m=2\) it is equivalent to \(|k_1-k_2|\le1\). For \(m=3\), because \(K\ge3k_*\), it forces \(k_*=1\) and then \(K=3\), namely all three blades are singleton. For \(m\ge4\), \(K\ge4k_*>2k_*+1\), so contraction is impossible. This completes the proof.

## Verification

Execute `python3 verify.py` with Python 3 and its standard library; no external data or software packages are required. The code independently constructs bouquet edge sets and Laplacians and checks the symbolic cut derivative against direct absolute-value directional differentiation, the sharp inequality and smallest-blade witnesses. It also tests the coarea argument on randomly selected integer signals and samples first-order finite-time numerical comparisons. In the recorded execution it passed 230 size profiles, 15,006 cut-profile comparisons, 230 sharp witnesses, 9,600 random integer coarea/generator comparisons, and 3,595 first-order numerical diagnostics. These finite checks do not prove the theorem for arbitrary dimensions; the complete analytical argument above supplies that proof.

## Relationship to prior work

Ollivier's transport curvature controls Wasserstein contraction of random walks, and graph curvature-gradient work by Bauer and collaborators treats pointwise or squared-gradient inequalities. These are different observables from the *sum* of absolute edge differences under the linear heat semigroup. The graph total-variation work of Kirisits, Scherzer and Setterqvist concerns denoising minimizers, and the metric-random-walk analysis of Mazón, Solera and Toledo distinguishes linear heat evolution from nonlinear total-variation flows. These comparisons do not establish the present sharp clique-bouquet threshold.

The contractive three-leaf-star and complete-graph subcases are not asserted to be previously unknown in isolation. The contribution assessed here is the global exact smallest-blade parameter, sharp infinitesimal rate, and complete all-time classification across **all clique bouquets**, including blades of size greater than one. Earlier general semigroup estimates might imply the conclusion once a nontrivial graph-specific optimization has been carried out; no directly covering classification was found in the inspected sources. Unindexed equivalent earlier analyses remain a residual possibility.

## Limitations

Only finite clique bouquets, counting vertex masses, unit edge conductances, unweighted edge variation and ordinary linear heat flow are covered. The exponential bound need not equal the exact norm at positive time, and no exact positive-time norm formula is claimed. The statement does not cover arbitrary block graphs, unequal diffusion rates, nonlinear variation flows or infinite graphs. The originality comparison is literature- and record-based, not a guarantee of uniqueness.

## References

1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (first public submission 2007-01-30); https://arxiv.org/abs/math/0701886.
2. Frank Bauer et al., *Li-Yau inequality on graphs*, arXiv:1306.2561 (first public submission 2013-06-11); https://arxiv.org/abs/1306.2561.
3. Clemens Kirisits, Otmar Scherzer and Eric Setterqvist, *Invariant \(\varphi\)-minimal sets and total variation denoising on graphs*, arXiv:1807.10514; https://arxiv.org/abs/1807.10514.
4. José M. Mazón, Marcos Solera and Julián Toledo, *Gradient flows in metric random walk spaces*, DOI:10.1007/s40324-021-00272-z; https://doi.org/10.1007/s40324-021-00272-z.
