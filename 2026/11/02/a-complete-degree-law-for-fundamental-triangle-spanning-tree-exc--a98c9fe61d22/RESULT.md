# A complete degree law for fundamental-triangle spanning-tree exchanges on wheels

## Finding
For each integer \(r\ge3\), let \(W_{r+1}\) have rim \(v_0v_1\cdots v_{r-1}v_0\) and hub \(h\). Construct \(X_r\) on all spanning trees of \(W_{r+1}\). A move deletes one selected edge and inserts one nonselected edge whose **fundamental cycle is exactly a hub-incident triangle** \(\{hv_i,hv_{i+1},v_iv_{i+1}\}\); multiple descriptions of the same unordered pair count only once. At \(r=3\), the all-rim triangle is deliberately **not** an allowed move support.

Write \(F_0=0,F_1=1\) and \(L_0=2,L_1=1\) for Fibonacci and Lucas numbers, respectively, and \(A_r(z)=\sum_Tz^{\deg_{X_r}(T)/2}\). Then
\[
 A_r(z)=-r[x^r]\log\!\left(1-zx-\frac{2zx^2}{1-x}-\frac{z^2x^3}{(1-x)^2}\right).
\]
This determines **every degree multiplicity for every wheel**. Moreover \(X_r\) is connected, its order is \(L_{2r}-2\), and its edge count is \(3rF_{2r-2}\). All its degrees are even; its unique maximum-degree vertex has degree \(2r\) and is the all-spoke tree, and precisely \(2r\) vertices have minimum degree \(2\).

## Assumptions and scope
Spanning trees are edge sets containing all \(r+1\) labelled vertices, with \(r\) edges and no cycle. Degrees are in the simple, unweighted exchange graph \(X_r\); there are no loops or parallel reconfiguration edges. The generating variable \(z\) records **half** of the exchange degree, while \(x\) marks rim length. Coefficient extraction and logarithms are formal, so no analytic convergence is needed. We distinguish wheel notation \(W_{r+1}\) from the convention naming the same graph \(W_r\).

## Proof
**1. Encoding all spanning trees.** A spanning tree contains at least one hub spoke: otherwise the hub is isolated. Let its selected spokes terminate at a nonempty cyclic subset of rim vertices \(S\), of size \(m\). Let \(g_1,\ldots,g_m\) be the strictly positive cyclic rim distances between consecutive selected spokes, with \(\sum_jg_j=r\). The selected rim edges form a forest, and each of its components must contain exactly one selected spoke. Indeed a spoke-free component would be disconnected from the hub, and a component with two selected spokes would create a cycle through the hub. Consequently, in each gap of length \(g_j\), exactly one rim edge is deleted, and every such independent choice produces a spanning tree. This correspondence is bijective, including \(m=1\).

**2. Exchange degree is a local statistic.** Each hub triangle contains at most two selected tree edges (three would form a cycle). A triangle supporting exactly two selected edges permits **two** distinct legal swaps, one for each selected edge, replacing it by the third edge: removing either edge of its fundamental cycle gives a tree. A triangle containing fewer than two selected edges allows no move whose fundamental cycle is that triangle; a different insertion can create a longer fundamental cycle, which is outside the stated move definition. A given swap has a unique supporting hub triangle because the union of its exchanged edges is contained in only one such triangle; thus \(\deg_{X_r}(T)=2c(T)\), where \(c(T)\) is the number of hub triangles with two selected edges.

**3. Factorization over gaps.** For an inter-spoke gap of length \(g=1\), its single triangle has both adjacent spokes and no selected rim edge, contributing \(1\) to \(c\), with one possible deletion. For \(g=2\), either endpoint rim edge may be deleted, and exactly one of the two endpoint triangles supports swaps; the weight polynomial is \(2z\). For \(g\ge3\), deletion of either endpoint rim edge (two choices) produces one active triangle, whereas deletion of any of the \(g-2\) interior rim edges produces two active triangles. The gap weight is therefore \(2z+(g-2)z^2\). Denote the ordinary generating function of gap weights by
\[
 P(x,z)=zx+\frac{2zx^2}{1-x}+\frac{z^2x^3}{(1-x)^2}.
\]
For fixed \(m\), counting all labelled cyclic spoke sets together with their deletion choices is \(\frac r m[x^r]P(x,z)^m\): mark any one of the \(m\) selected spoke vertices as the initial spoke and choose its rim label in \(r\) ways, then divide by \(m\). Summing over \(m\ge1\) gives \(A_r(z)=r[x^r]\sum_{m\ge1}P(x,z)^m/m=-r[x^r]\log(1-P(x,z))\).

**4. Consequences.** At \(z=1\), \(P(x,1)=x/(1-x)^2\). Hence
\[
 A_r(1)=-r[x^r]\log\!\left(\frac{1-3x+x^2}{(1-x)^2}\right)=L_{2r}-2.
\]
Differentiating the formal identity in \(z\) and evaluating at \(z=1\) yields
\[
 A'_r(1)=r[x^r]\frac{x+x^3}{1-3x+x^2}=3rF_{2r-2}.
\]
As \(\deg(T)=2c(T)\), the handshaking lemma gives \(|E(X_r)|=A'_r(1)\). Each gap contributes at least one to \(c(T)\). The coefficient of \(z\) comes only from single-spoke trees with one deleted rim edge incident to that spoke: exactly \(2r\) possibilities (two deletions per spoke). The coefficient of \(z^r\) is one, from the all-spoke tree; for \(m<r\) at least one gap has length at least two, so \(c(T)<r\). Finally, a triangle swap can change an active rim edge into a spoke at an endpoint adjacent to an existing spoke, increasing the spoke count by one. Each rim-forest component is a path containing its unique spoke, so such an edge exists whenever the tree is not the all-spoke tree. Iterating reaches that tree and proves connectedness.

## Verification
A standalone exhaustive checker independently enumerates all labelled spanning trees as edge subsets and builds the legal swap graph, while a second checker enumerates labelled cyclic spoke-gap configurations. The two resulting degree polynomials agree for every \(3\le r\le8\) and coincide with the coefficient formula above. The enumeration checks connectivity and the edge count independently of the generating-function manipulation. The programs and exact tested ranges are included with this result; their finite tests corroborate but do not replace the all-parameter combinatorial proof.

## Relationship to prior work
The classical wheel spanning-tree enumeration \(L_{2r}-2\) is due to earlier authors, including Myers, Hilton and Sedláček; it is reproduced here only as a specialization. Chan, Church and Grochow (2013) study actions on spanning trees of planar graphs, but not the present degree law for exchanges inside hub triangles. Nichols, Pilz, Tóth and Zehmakan (2020) study plane-tree transition operations, rather than this precise degree enumerator. Tamura and Tanaka (2026) give root-set-conditioned wheel-forest counts and Fibonacci/Lucas formulas; their full available article discusses interval decompositions, but does not state a hub-triangle tree-exchange degree distribution. The new assertion concerns the full adjacency-degree profile and connectivity under one restricted exchange operation, not the already known number of wheel spanning trees.

## Limitations
This establishes degree counts, connectivity and the total number of local moves, but not the exact diameter, shortest-path distance distribution, spectral data or mixing time of \(X_r\). The check against accessible literature cannot exclude an equivalent result expressed in a different basis-graph or matroid-polytope formulation. No independent mathematical audit is asserted.

## References
1. R. J. Myers, *Number of spanning trees in a wheel* (1971), as cited by Tamura and Tanaka.
2. A. J. W. Hilton, *Spanning trees and Fibonacci and Lucas numbers* (1974), as cited by Tamura and Tanaka.
3. M. Chan, T. Church, J. A. Grochow, *Rotor-routing and spanning trees on planar graphs* (first preprint 2013-08-12), https://arxiv.org/abs/1308.2677.
4. T. L. Nichols, A. Pilz, C. D. Tóth, A. N. Zehmakan, *Transition operations over plane trees* (2020), https://doi.org/10.1016/j.disc.2020.111929.
5. S. Tamura, Y. Tanaka, *Rooted spanning forests in wheel graphs: Fibonacci–Lucas formulas and extremal root configurations* (first preprint 2026-09-04), https://arxiv.org/abs/2609.29486.
