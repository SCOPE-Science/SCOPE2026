# A graph-matching criterion for stable polarization under strong homophily

## Finding

For the static-network opinion system of Pérez-Martínez, Bauzá Mingueza, Soriano-Paños, Gómez-Gardeñes and Floría, fix a finite connected simple graph \(G\) with at least two vertices, social strength \(K>1\), and weight offset \(\delta>0\). A prescribed binary opinion sign pattern \(\sigma\in\{-1,+1\}^{V(G)}\) is realized by a locally exponentially attracting equilibrium for every sufficiently large finite homophily exponent \(\beta\) **if and only if** each vertex has at least one adjacent vertex with the same sign. The necessity direction holds for any \(\beta\geq0\) and every equilibrium with no zero coordinates, independent of stability.

Writing \(r>0\) for the unique solution of \(r=K\tanh r\), the attracting equilibrium associated with each admissible \(\sigma\) satisfies
\[
\left\|x^{(\beta)}-r\sigma\right\|_\infty
\leq C(G,K,\delta)\left(\frac{\delta}{2r+\delta}\right)^\beta
\]
for all sufficiently large \(\beta\).

A connected graph admits at least one strictly mixed-sign attracting equilibrium for all sufficiently large \(\beta\) precisely when it contains **two vertex-disjoint edges**, equivalently when its matching number is at least two. In particular, the four-vertex path is a smallest connected example, whereas every connected graph on at most three vertices is excluded. For \(K\leq1\), the zero opinion state is the only equilibrium for any \(\beta\geq0\).

## Assumptions and scope

The network is a finite, connected, loopless, undirected, unweighted simple graph with vertices \(V\) and neighbor sets \(N(i)\). Parameters are \(K>0\), \(\delta>0\), and real \(\beta\geq0\). Each opinion is real. For an edge \(\{i,j\}\), define
\[
a_{ij}(x)=(\delta+|x_i-x_j|)^{-\beta},\qquad
p_{ij}(x)=\frac{a_{ij}(x)}{\sum_{k\in N(i)}a_{ik}(x)}.
\]
The dynamics are
\[
\dot x_i=-x_i+F_{\beta,i}(x),\qquad
F_{\beta,i}(x)=K\sum_{j\in N(i)}p_{ij}(x)\tanh x_j.
\]
All contact weights are strictly positive at every finite \(\beta\). A binary sign pattern is **supported** when \(N(i)\) contains some \(j\) with \(\sigma_j=\sigma_i\) for every vertex \(i\). A **strictly polarized** equilibrium means every coordinate is nonzero and both signs occur; it does not require exactly symmetric group sizes or zero mean. Local exponential attraction refers to the full continuous-time system in the sup norm, not just a reduced symmetric subspace.

## Proof

**1. Saturation and the scalar root.** If \(0<K\leq1\), any fixed point satisfies \(M\leq K\tanh M\), where \(M=\max_i|x_i|\), since \(p_{ij}\) form nonnegative rows summing to one. Because \(\tanh M<M\) for \(M>0\), necessarily \(M=0\). For \(K>1\), the function \(K\tanh r-r\) has exactly one strictly positive root \(r\), as it starts with positive derivative and is strictly concave for \(r>0\); moreover \(K\operatorname{sech}^2 r<1\).

**2. Necessity of same-sign support.** At an equilibrium \(x\) with every coordinate nonzero, if all neighbors of a vertex \(i\) have signs opposite to \(x_i\), then every summand \(p_{ij}(x)\tanh x_j\) has sign opposite to \(x_i\), contradicting \(x_i=F_{\beta,i}(x)\). This holds for all finite \(\beta\geq0\) and does not depend on stability or the magnitude of \(K\).

**3. A uniform contraction near every supported sign pattern.** Fix \(K>1\), supported \(\sigma\), and let \(v=r\sigma\). Write \(d=\max_i|N(i)|\) and \(q_0=\delta/(2r+\delta)<1\). At the center \(v\), a vertex has at least one same-sign neighbor of weight \(\delta^{-\beta}\); each opposite-sign neighbor contributes \((2r+\delta)^{-\beta}\). Consequently
\[
\|F_\beta(v)-v\|_\infty\leq 2rdq_0^\beta.
\]
Choose any \(q\) with \(q_0<q<1\), put \(\epsilon_\beta=q^\beta\), and consider the closed sup-norm ball \(B_\beta=\{x:\|x-v\|_\infty\leq\epsilon_\beta\}\). For all sufficiently large \(\beta\), \(\epsilon_\beta<r\). Its total opposite-sign weight at vertex \(i\), \(\alpha_i(x)=\sum_{j:\sigma_j\ne\sigma_i}p_{ij}(x)\), obeys
\[
\alpha_i(x)\leq d\left(\frac{\delta+2\epsilon_\beta}{\delta+2r-2\epsilon_\beta}\right)^\beta
\leq d(q')^\beta
\]
for a fixed \(q'\) chosen strictly between \(q_0\) and \(q\), after increasing \(\beta\) if necessary.

Put \(m_\beta=\operatorname{sech}^2(r-\epsilon_\beta)\). Along a straight segment in \(B_\beta\), normalized weights are Lipschitz. In any unit sup-norm direction, the logarithmic derivative of each unnormalized weight has absolute value at most \(2\beta/\delta\); hence the total variation of normalized weights is at most \(4\beta/\delta\). More precisely, the total variation restricted to opposite-sign neighbors is at most \((4\beta/\delta)\alpha_i(x)\). Subtracting \(\sigma_i\tanh r\) in the weight-variation term and bounding the same-sign discrepancy by \(m_\beta\epsilon_\beta\) gives the global Lipschitz estimate on the ball
\[
\operatorname{Lip}_\infty(F_\beta|_{B_\beta})\leq
L_\beta:=Km_\beta+\frac{4K\beta}{\delta}
\left(m_\beta\epsilon_\beta+2d(q')^\beta\right).
\]
The absolute-value kinks at equal opinions cause no problem: derivatives hold almost everywhere along segments, and the same integrated Lipschitz bounds follow. Since \(Km_\beta\to K\operatorname{sech}^2 r<1\) and \(\beta q^\beta,\beta(q')^\beta\to0\), we have \(L_\beta<1\) for all sufficiently large \(\beta\). Also \(2rdq_0^\beta+L_\beta\epsilon_\beta<\epsilon_\beta\), so \(F_\beta(B_\beta)\subseteq B_\beta\).

By the contraction theorem, there is a unique fixed point \(x^{(\beta)}\) in this ball. It has sign \(\sigma\), and
\[
\|x^{(\beta)}-v\|_\infty
\leq\frac{2rd}{1-L_\beta}q_0^\beta.
\]
For any solution initially in the ball, the upper Dini derivative satisfies
\[
D^+\|x(t)-x^{(\beta)}\|_\infty
\leq-(1-L_\beta)\|x(t)-x^{(\beta)}\|_\infty,
\]
which gives local forward invariance and exponential attraction. The estimate is uniform for each fixed graph and supported sign pattern; with finitely many such patterns, a common sufficiently large \(\beta\) can be chosen.

**4. Exact topology and minimal network.** If both signs occur in a supported pattern, each sign class contains an edge. These two monochromatic edges are vertex-disjoint. Conversely, suppose \(G\) has disjoint edges \(ab\) and \(cd\). Assign \(a,b\) sign \(+1\) and \(c,d\) sign \(-1\). Expand this partially colored set along a spanning forest rooted at these four vertices; color each new vertex with the sign of its previously colored parent. Every original endpoint has its monochromatic partner, and every new vertex has its monochromatic parent. The completed pattern is supported and mixed. Thus the sharp criterion is \(\nu(G)\geq2\). Four vertices are necessary, and the four-vertex path has two disjoint edges, completing the proof.

## Verification

The independent-of-library standalone script `verify.py` recomputes the graph/matching equivalence on **every connected labeled simple graph on two through six vertices**. Counts of connected graphs and mixed supported patterns are respectively \((1,0)\), \((4,0)\), \((38,34)\), \((728,723)\), and \((26704,26698)\) by increasing order. The graph census is a finite cross-check; the proof above establishes the theorem for all finite sizes.

The same script evaluates the four-vertex path with \(K=2\), \(\delta=1/250\), and \(\beta=4\). It finds the scalar root \(r\approx1.91500804815454\), an attracting mixed-sign fixed point near \((r,r,-r,-r)\), a fixed-point residual below \(10^{-12}\), and a conservative computed Lipschitz upper bound below \(0.25\) on a sup-norm ball of radius \(10^{-4}\). These are reproducibility checks using floating-point arithmetic, not formally certified interval bounds; the general assertions are proved analytically.

Run with `python3 verify.py`. No third-party dependency is needed.

## Relationship to prior work

Pérez-Martínez and coauthors introduced these exact homophily-weighted static-network equations, found the scalar saturation root, analyzed two-opinion arrangements on complete networks, and numerically studied polarization and network structure. The present theorem does **not** claim to introduce their model or to establish the general possibility of polarization for the first time. It adds a graph-independent sufficient-and-necessary support criterion for every binary sign pattern at strong homophily, a quantitative rate of approach to saturated opinions, and an exact matching-number obstruction for any strictly polarized equilibrium.

Brooks, Chodrow and Porter studied a distinct continuous-time sigmoidal bounded-confidence system, including results about polarized states and graph structure. Their dynamics interpolate between averaging and Hegselmann–Krause influence, using prescribed zealots in the main settings, rather than the saturated \(K\tanh\) response and power-law normalized influence here. Their general limiting-state results do not directly imply the graph-matching criterion for the present system. Generic singular-limit intuition suggests the construction but is not a substitute for a finite-parameter stability proof. An independently performed comprehensive novelty certification is not asserted.

## Limitations

The theorem gives existence and local exponential attraction for sufficiently large but not universally specified finite \(\beta\), and the absence of any strictly polarized equilibrium on graphs without two disjoint edges. It does not classify sign-changing equilibria with one or more zero opinion coordinates, multilevel/unequal-magnitude steady states outside the constructed neighborhoods, finite-\(\beta\) bifurcation thresholds, sizes of attraction basins, stochastic dynamics, or global convergence. The same-sign support condition does not imply that every initial state with a given sign pattern converges to its associated equilibrium. The graph size is arbitrary but finite, and \(\delta\) is fixed strictly positive. A possible independently derived equivalent graph characterization in uninspected literature remains a bibliographic risk.

## References

1. H. Pérez-Martínez, F. Bauzá Mingueza, D. Soriano-Paños, J. Gómez-Gardeñes and L. M. Floría, *Polarized opinion states in static networks driven by limited information horizons*, first arXiv version March 3, 2023, arXiv:2303.02113. https://arxiv.org/abs/2303.02113 ; full accessible text https://arxiv.org/html/2303.02113v2 .
2. H. Z. Brooks, P. S. Chodrow and M. A. Porter, *Emergence of polarization in a sigmoidal bounded-confidence model of opinion dynamics*, arXiv:2209.07004 (2022). https://arxiv.org/abs/2209.07004 .
