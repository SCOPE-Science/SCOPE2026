# Local neighborhood imbalance governs weighted-variation stability of graph gossip

## Finding

**Theorem (sharp weighted-variation law for an edge exchange).** Let \(G=(V,E)\) be a finite connected simple undirected graph with \(|V|\ge3\). Let each edge \(ij\in E\) have a strictly positive weight \(w_{ij}\), and put \(w_{ij}=0\) for nonedges and \(w_{ii}=0\). Fix an edge \(e=uv\) and \(0\le\theta\le1\). Define the linear exchange \(T_{e,\theta}\) by
\[
(T_{e,\theta}f)(u)=(1-\theta)f(u)+\theta f(v),\qquad
(T_{e,\theta}f)(v)=\theta f(u)+(1-\theta)f(v),
\]
with all other coordinates unchanged. Set
\[
J_w(f)=\sum_{ij\in E}w_{ij}|f(i)-f(j)|,\qquad
D_e=\sum_{z\in V\setminus\{u,v\}}|w_{uz}-w_{vz}|,
\qquad m_\theta=\min\{\theta,1-\theta\}.
\]
For every real vertex signal \(f\),
\[
\boxed{J_w(T_{e,\theta}f)-J_w(f)
\le\bigl(\theta D_e-2m_\theta w_{uv}\bigr)|f(u)-f(v)|.}\tag{1}
\]
For every prescribed nonzero endpoint gap, equality is attained by choosing the remaining vertex values from the two endpoint values. Thus (1) is the **sharp local gain bound**, not merely an estimate. For \(\theta>0\), the following are equivalent:
\[
J_w(T_{e,\theta}f)\le J_w(f)\quad\forall f\in\mathbb R^V;
\qquad
\boxed{D_e\le2w_{uv}\quad\text{and}\quad
\theta\le \frac{2w_{uv}}{D_e+2w_{uv}}.}\tag{2}
\]
The case \(\theta=0\) is the identity. In particular, standard equalization \(\theta=1/2\) is variation-nonincreasing exactly when \(D_e\le2w_{uv}\), and the full exchange \(\theta=1\) is variation-nonincreasing exactly when the two endpoints have identical weighted neighbor profiles outside the pair.

The **exact global variation-seminorm operator norm** has a cut formula. Orient every separating cut by taking \(u\in S\), \(v\notin S\), write \(c_w(S)=\sum_{ij\in\partial S}w_{ij}>0\), \(d_z=w_{uz}-w_{vz}\), and \(\sigma_z(S)=1\) for \(z\in S\), \(-1\) otherwise. Then
\[
\boxed{\|T_{e,\theta}\|_{J_w\to J_w}
=\max\left\{1,\max_{\substack{S\subset V:\,u\in S,\ v\notin S}}
\left(1+\frac{\theta\sum_{z\ne u,v}\sigma_z(S)d_z-2m_\theta w_{uv}}{c_w(S)}\right)\right\}.}\tag{3}
\]
The maximum is attained by an indicator signal. For every rational \(k\ge1\), the decision \(\|T_{e,\theta}\|_{J_w\to J_w}\le k\) is equivalent to
\[
\boxed{\min_{\substack{S\subset V:\,u\in S,\ v\notin S}}
\left[(k-1)c_w(S)-\theta\sum_{z\ne u,v}\sigma_z(S)d_z\right]
\ge-2m_\theta w_{uv}.}\tag{4}
\]
The minimand is a positive multiple of a graph cut plus vertex-modular terms, so this threshold question reduces to one ordinary \(u\)-\(v\) minimum-cut computation with additional source/sink arcs (when input weights and parameters are rational). Exact norms are finite maxima of rational cut ratios for rational data.

**Network-wide consequence.** If every edge of a weighted graph satisfies \(D_e\le2w_e\), then every deterministic, adaptive, or randomized sequence of standard pairwise equalizations is pathwise nonincreasing in \(J_w\); conversely, pathwise nonincrease for *every* allowable single-edge exchange forces all these inequalities. For a unit-weight complete multipartite graph \(K_{n_1,\ldots,n_r}\) with \(r\ge2\), all-edge nonincrease holds exactly when the sum of its two largest part sizes is at most four. For a unit-weight tree, it holds exactly for paths and the three-leaf star.

## Assumptions and scope

The graph is finite, connected, simple and undirected, \(|V|\ge3\), with positive symmetric weights on edges. Vertex signals are arbitrary real functions, and the exchange parameter lies in \([0,1]\). The norm is the induced operator norm on vertex functions modulo constants, since connectedness makes \(J_w\) a norm there. Both input data in a two-data stability inequality may be arbitrary, because the exchange is linear. Only the two selected endpoints update; this is not simultaneous averaging over all neighbors. The two-vertex graph is excluded from (3) because no nontrivial cut with the selected endpoints on the same side exists; its norm equals \(|1-2\theta|\).

## Proof

**Local weighted displacement.** Fix distinct endpoint values \(a,b\). Their exchange gives \(a'=(1-\theta)a+\theta b\), \(b'=\theta a+(1-\theta)b\). For any \(z\ne u,v\), put \(\alpha=w_{uz}\), \(\beta=w_{vz}\) and \(c=f(z)\). We claim
\[
\alpha|a'-c|+\beta|b'-c|
-\alpha|a-c|-\beta|b-c|
\le\theta|\alpha-\beta|\,|a-b|.\tag{5}
\]
After translating, scaling, and if necessary interchanging endpoints, take \(a=1\), \(b=0\). The vector \((a',b')=(1-\theta,\theta)\) is a doubly stochastic mixture of \((1,0)\) and \((0,1)\), so by convexity
\[
|a'-c|+|b'-c|\le|1-c|+|c|.
\]
If \(\alpha\ge\beta\), separate \(\beta\) times this last sum and \((\alpha-\beta)|a'-c|\); then use \(|a'-c|\le|1-c|+\theta\). This proves (5). If \(\beta\ge\alpha\), instead use \(|b'-c|\le|c|+\theta\). Equality occurs at \(c=a\) when \(\alpha\ge\beta\), or at \(c=b\) when \(\beta\ge\alpha\).

Sum (5) over all third vertices. Every edge disjoint from \(\{u,v\}\) is unchanged, while the selected edge changes its absolute difference from \(|a-b|\) to \(|1-2\theta||a-b|\). Because \(|1-2\theta|-1=-2m_\theta\), the result is (1). The equality choices can be made independently at all other vertices. For any \(a\ne b\), these choices are simultaneous and achieve (1), proving sharpness and (2). For \(0<\theta\le1/2\), (2) reduces to \(D_e\le2w_e\); for \(1/2<\theta\le1\), it is \(\theta D_e\le2(1-\theta)w_e\). Combining the two intervals gives the displayed closed interval when \(D_e\le2w_e\); otherwise no positive \(\theta\) contracts.

**Indicator reduction.** For every real signal \(f\), a finite discrete layer-cake decomposition writes \(f\), modulo an additive constant, as a positive integral of indicators \(\mathbf 1_{\{f>t\}}\). Since \(T_{e,\theta}\) is linear and preserves constants, convexity and the coarea identity give
\[
J_w(T_{e,\theta}f)
\le\int J_w(T_{e,\theta}\mathbf 1_{\{f>t\}})\,dt,
\quad
J_w(f)=\int c_w(\{f>t\})\,dt.
\]
Therefore the induced norm is exactly the maximum of indicator ratios. An indicator not separating the selected pair is unchanged. Since the connected graph has at least three vertices, there is a nontrivial indicator with both endpoints on the same side, establishing the baseline ratio one. For a separating indicator with \(u\in S\), \(v\notin S\), direct evaluation on each incident edge gives an incremental contribution \(\theta(w_{uz}-w_{vz})\) when \(z\in S\) and its negative otherwise, together with \(-2m_\theta w_e\) from the selected edge. This proves (3), including attainment, and rearrangement yields (4).

**Cut decision.** For \(k\ge1\), the left minimand in (4) is
\[
(k-1)c_w(S)-2\theta\sum_{z\in S\setminus\{u\}}d_z+
\theta\sum_{z\notin\{u,v\}}d_z.
\]
All original undirected edges receive capacity \((k-1)w_{ij}\). A vertex with \(d_z>0\) receives a source-to-vertex arc of capacity \(2\theta d_z\) and a constant offset \(-2\theta d_z\); a vertex with \(d_z<0\) receives a vertex-to-sink arc of capacity \(-2\theta d_z\). The remaining displayed sum is another constant offset. Hence a standard minimum cut evaluates (4) exactly.

**Graph families.** For unit-weight complete multipartite graphs, an edge between parts \(i,j\) has exactly \(D_e=n_i+n_j-2\). The all-edge test is \(n_i+n_j\le4\) for every pair, hence exactly the two-largest-parts condition. On a unit-weight tree, \(D_e=\deg(u)+\deg(v)-2\). Requiring \(D_e\le2\) on all edges allows maximum degree two (a path) or exactly one degree-three vertex adjacent only to leaves (a three-leaf star). The composition statement follows because products of seminorm contractions are contractions; its converse tests a single selected edge.

For a unit-weight star with \(m\ge2\) leaves, the cut formula simplifies to
\[
\|T_{e,\theta}\|_{J\to J}
=\max\{1,\,|1-2\theta|+(m-1)\theta\}
\]
when \(e\) joins its hub to a leaf. The second term is attained by the indicator that is one at the hub and every other leaf, zero at the selected leaf. Every remaining separating cut has a ratio that is a convex combination of this second term and \(1-2\theta\), so it cannot be larger. This shows explicit arbitrarily large one-step variation amplification at \(\theta=1/2\) as the hub degree increases.

## Verification

The accompanying `verify_gossip_variation.py` uses exact rational arithmetic. It independently enumerates all indicator cuts on 600 randomly constructed connected weighted graphs of 3–7 vertices, checking 4,200 cut norms, 4,200 sharp local gains, 4,200 contraction decisions, and 16,800 further signal inequalities. It also checks 91 star examples and independently compares a source/sink minimum-cut construction with exhaustive cut enumeration on 480 weighted instances of 3–8 vertices. The random seeds are fixed in the script. Run with `python verify_gossip_variation.py` after installing the declared dependency. These finite checks are diagnostics, not proofs for arbitrary graph size; the proof above supplies that generality.

## Relationship to prior work

Boyd, Ghosh, Prabhakar and Shah study classical pairwise gossip and its spectral convergence rate. Kováč and Smith study graph-edge total variation as a regression penalty. Ben-Ameur, Bianchi and Jakubowicz study TV-regularized robust consensus, explicitly distinguishing conventional linear gossip from their nonlinear optimization algorithm. None of these materially inspected claims supplies the weighted neighbor-profile iff criterion, the full exchange-parameter interval, or the exact induced norm through cut thresholds. The coarea and minimum-cut machinery are established methods; the specialized identification for an arbitrary weighted single-edge gossip exchange is the claim assessed here. A related exact equivalence hidden in earlier operator-norm or consensus literature is not ruled out.

## Limitations

The theorem concerns an individual symmetric two-vertex exchange on a finite connected undirected weighted graph. It does not characterize the total-variation norm of arbitrary simultaneous multi-vertex mixing matrices, non-symmetric exchanges, nonlinear TV flow, or convergence rates of a random schedule. The minimum-cut decision statement assumes \(k\ge1\) and, for exact rational computation, rational input data. No independent external mathematical validation is claimed.

## References

1. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Analysis and Optimization of Randomized Gossip Algorithms*, IEEE Conference on Decision and Control, December 2004. https://stanford.edu/~boyd/papers/gossip_opt.html
2. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory 52 (2006), 2508–2530. https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf
3. A. Kováč, A. D. A. C. Smith, *Regression on a Graph*, arXiv:0911.1928, first posted 2009-11-10. https://arxiv.org/abs/0911.1928
4. W. Ben-Ameur, P. Bianchi, J. Jakubowicz, *Robust Average Consensus using Total Variation Gossip Algorithm*, VALUETOOLS 2012, DOI:10.4108/valuetools.2012.250316. https://eudl.eu/pdf/10.4108/valuetools.2012.250316
