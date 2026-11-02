# Sharp equilibrium-count spectrum for self-essential anti-coordination on \(K_{a,b}\)

## Finding

**Theorem (exact fixed points and sharp multiplicity spectrum).** Let \(a,b\ge1\) be integers and let \(G=K_{a,b}\) have labeled parts \(A,B\) of respective sizes \(a,b\). Assign each vertex an arbitrary nonnegative integer threshold \(\tau_v\). Under the self-essential inverted-threshold rule, a vertex updates to action \(1\) exactly when at least \(\tau_v\) vertices in its **closed** neighborhood (including itself) currently have action \(0\). An equilibrium means a configuration unchanged by this rule at every vertex.

For \(0\le i\le a\), \(0\le j\le b\), put
\[
F_A(j)=\#\{u\in A:\tau_u\ge j+2\},\qquad
F_B(i)=\#\{v\in B:\tau_v\ge i+2\}.
\]
There is exactly one equilibrium with \(i\) zero-action vertices in \(A\) and \(j\) in \(B\) precisely if
\[
 i=F_A(j),\quad j=F_B(i),\quad
 \tau_u\ne j+1\ (u\in A),\quad
 \tau_v\ne i+1\ (v\in B).
\tag{1}
\]
Otherwise no equilibrium has those two zero counts. Hence its exact equilibrium count is the number of integer pairs satisfying (1), computable with a linear-size threshold histogram and a linear scan.

Among **all** nonnegative integer threshold assignments on \(K_{a,b}\), the attainable equilibrium counts are exactly
\[
\boxed{\{0,1,\ldots,\lfloor\min(a,b)/2\rfloor+1\}.}
\tag{2}
\]
In particular the sharp maximum is \(\lfloor\min(a,b)/2\rfloor+1\). For every even balanced graph \(K_{2r,2r}\), the maximum \(r+1\) is attainable using only nonconstant vertex rules with thresholds \(2,2,4,4,\ldots,2r,2r\) on each side.

## Assumptions and scope

The graph is finite, undirected, simple and complete bipartite; the two vertex parts are nonempty. A configuration is \(x\in\{0,1\}^{A\cup B}\). The synchronous local map is
\[
 T_v(x)=\mathbf 1\left\{\sum_{w\in N[v]}(1-x_w)\ge\tau_v\right\}.
\]
Here \(N[v]=N(v)\cup\{v\}\) and \(\tau_v\in\mathbb Z_{\ge0}\) is vertex-specific. Rules with \(\tau_v=0\) are permitted (they always output \(1\)); the statement also permits thresholds above the closed-neighborhood size. A fixed point of the simultaneous map is likewise unchanged by any sequential sweep that updates each vertex once: no vertex can change in a sweep that returns to its starting configuration, since it is visited only once. No statement is made about non-fixed periodic orbits or their attraction basins.

## Proof

**Local compatibility.** Fix an equilibrium with \(i\) zeros in \(A\) and \(j\) in \(B\). For each \(u\in A\), exactly \(j\) of its open neighbors have action zero. If \(x_u=1\), its own action contributes no zero, so fixedness requires \(j\ge\tau_u\). If \(x_u=0\), it contributes one zero, and fixedness requires \(j+1<\tau_u\), equivalently \(\tau_u\ge j+2\). At \(\tau_u=j+1\), neither action is self-consistent. Consequently a fixed state exists on \(A\) for this \(j\) if and only if no threshold equals \(j+1\), and then the actions are uniquely forced and there are exactly \(F_A(j)\) zeros. The same argument with the parts exchanged proves (1), including both directions and uniqueness of each labeled configuration.

**Two-unit separation.** Suppose two distinct equilibrium count pairs are \((i,j)\) and \((i',j')\), with \(i<i'\). From (1), \(j=F_B(i)\) and \(j'=F_B(i')\); because \(F_B\) is nonincreasing, \(j\ge j'\). Equality would imply \(i=F_A(j)=F_A(j')=i'\), impossible. Thus \(j>j'\). At least one vertex in \(A\) has action \(1\) at the first equilibrium and action \(0\) at the second, since the zero sets are nested as \(j\) decreases. Its threshold therefore satisfies \(\tau_u\le j\) and \(\tau_u\ge j'+2\). Hence \(j-j'\ge2\). Likewise at least one vertex in \(B\) changes from action \(0\) in the first equilibrium to action \(1\) in the second: its threshold satisfies \(\tau_v\ge i+2\) and \(\tau_v\le i'\), so \(i'-i\ge2\).

Sort all equilibrium pairs by increasing \(i\). Adjacent first coordinates differ by at least two, and the corresponding second coordinates decrease by at least two. Since \(i\) ranges from \(0\) through \(a\) and \(j\) from \(0\) through \(b\), there are at most
\[
1+\min\{\lfloor a/2\rfloor,\lfloor b/2\rfloor\}
=1+\lfloor\min(a,b)/2\rfloor
\]
equilibria.

**All intermediate multiplicities.** To realize zero equilibria, assign every vertex threshold \(1\). An action-zero vertex could not be fixed because it sees its own zero and therefore updates to one; the all-ones state also cannot be fixed because its closed-neighborhood zero count is zero, so the equilibrium set is empty.

For a prescribed positive count \(k\le1+\lfloor\min(a,b)/2\rfloor\), write \(r=k-1\). On **each** part choose exactly two vertices of each threshold \(2,4,\ldots,2r\), assigning threshold \(0\) to all remaining vertices. This is possible because \(2r\le\min(a,b)\). Zero-action vertices must lie among the \(2r\) nonconstant-threshold vertices in each part. A candidate equilibrium with \(j\) zeros in \(B\) cannot have an odd \(j\) between \(1\) and \(2r-1\), since some threshold would equal \(j+1\), violating (1). For even \(j=2(r-t)\), \(0\le t\le r\), the forced zero count in \(A\) is precisely \(i=2t\); the forced zero count in \(B\) is then \(2(r-t)\). Thus these \(r+1=k\) pairs satisfy (1). As no vertex with threshold zero can be zero in an equilibrium, no other \(j\) is possible, proving there are exactly \(k\) equilibria. This proves (2). When \(a=b=2r\), the construction has no threshold-zero vertices and all thresholds belong to \(\{2,4,\ldots,2r\}\subseteq\{1,\ldots,2r\}\), establishing the last assertion.

**Counting algorithm.** For each part, clip threshold values above the opposite part size plus two to that upper category, construct frequency counts and suffix counts of its thresholds, and then iterate \(i=0,\ldots,a\). The second equality in (1) forces the unique candidate \(j=F_B(i)\); check the two forbidden equalities and the first equality in (1). This uses \(O(a+b)\) arithmetic operations and memory on integer threshold categories, after reading all thresholds. The algorithm computes the full exact count, not just an upper bound.

## Verification

The accompanying dependency-free program `verify.py` independently enumerates all binary action configurations and performs the closed-neighborhood update, rather than deriving their validity from (1). It compared the resulting zero-count pairs against (1) for all \(19{,}432\) threshold assignments on \(K_{a,b}\), \(1\le a,b\le3\), with each threshold ranging from zero to the corresponding degree plus one. This examined \(1{,}111{,}428\) binary configurations. It also verified all \(1{,}010\) explicit spectrum constructions for \(1\le a,b\le15\) and every permissible target count, and observed the asserted small-size maxima. Run `python verify.py` beside this document. These checks do not establish the unrestricted theorem; the preceding proof does.

## Relationship to prior work

Qiu et al. (arXiv:2301.02889, 2023, v5 2024) define the self-essential inverted-threshold model and prove that equilibrium existence and counting are computationally hard even on general bipartite graphs. Their Lemma 4.4 classifies the two fixed points of one homogeneous-threshold \(K_{3,3}\) example; their complete-graph result is not a complete-bipartite arbitrary-threshold multiplicity theorem. Here, the two-unit threshold separation gives a sharp maximum and **every** attainable equilibrium count for all complete bipartite graphs and all heterogeneous thresholds.

The coordination-oriented threshold protocol game on complete bipartite graphs treated by Fedrigo (2024) has a different update rule and a common adoption parameter. Xia, McAvoy and Su (2025) report equilibrium counts and a complete-bipartite two-community-threshold example, but their update is an open-neighborhood payoff best response with incumbent retention at ties; it is not this closed-neighborhood self-essential map. General Boolean-network fixed-point bounds and general bi-threshold convergence theory likewise do not, in the consulted material, provide the exact spectrum (2). The distinction between the graph families, neighborhood conventions, and threshold quantifiers is essential; a matching graph name alone is not an implication.

## Limitations

The result concerns fixed points, not convergence rates or attraction probabilities. It requires every cross-part edge and unweighted integer-count thresholds. Heterogeneous vertex thresholds and, for the full spectrum at every pair of side sizes, constant-one local rules at threshold zero are allowed. The maximum on balanced even graphs nevertheless needs no constant local rules. Published-priority searches are incomplete, and unseen specialist Boolean-network results may contain equivalent statements. There has been no independent external validation.

## References

1. Z. Qiu, C. Chen, M. V. Marathe, S. S. Ravi, D. J. Rosenkrantz, R. E. Stearns and A. Vullikanti, *Networked Anti-Coordination Games Meet Graphical Dynamical Systems: Equilibria and Convergence*, arXiv:2301.02889 (first public release 2023-01-07), https://arxiv.org/html/2301.02889.
2. A. Fedrigo, *End Behavior of the Threshold Protocol Game on Complete and Bipartite Graphs*, *Games* 15 (2024), 41, https://doi.org/10.3390/g15060041.
3. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974 (2011), https://arxiv.org/abs/1108.2974.
4. J. Aracena, A. Richard and L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, *Journal of Computer and System Sciences* 80 (2014), 1175–1190, https://doi.org/10.1016/j.jcss.2014.04.025.
5. Y. Xia, A. McAvoy and Q. Su, *Behavioral alignment in social networks*, arXiv:2506.00046 (2025), https://arxiv.org/abs/2506.00046.
