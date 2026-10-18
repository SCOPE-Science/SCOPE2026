# Exact unconditional constants of spanning-tree molecule bases on weighted cactus graphs

## Finding
Let \(G=(V,E)\) be a finite connected simple cactus graph with \(|V|\ge2\) (every edge belongs to at most one simple cycle), with positive edge lengths \(w_e\), and let \(M\) be its vertex set with the shortest-path metric. For every simple cycle \(C\), assume \(2\max_{e\in C}w_e\le\sum_{e\in C}w_e\), ensuring that every cycle edge realizes the distance between its endpoints. Select one edge \(a_C\) to delete from each cycle; the remaining edges form a spanning tree \(T\). The oriented edge molecules for \(e\in T\) form a basis \(\mathcal B_T\) of the real Lipschitz-free space \(\mathcal F(M)\).

For a cycle \(C\), set
\[
 h_C=w_{a_C},\qquad S_C=\sum_{e\in C\setminus\{a_C\}}w_e,
 \qquad \Delta_C=\min_{\varepsilon_e\in\{-1,1\}}\left|\sum_{e\in C\setminus\{a_C\}}\varepsilon_e w_e\right|.
\]
The optimal unconditional basis constant, with the supremum taken over every sign-change operator on \(\mathcal B_T\), is exactly
\[
 K(\mathcal B_T)=\max\left\{1,\max_{C\text{ cycle of }G}
 \frac{\min\{S_C,\ h_C+S_C-\Delta_C\}}{h_C}\right\}.
\]
For a tree the inner maximum is absent and \(K(\mathcal B_T)=1\). An unweighted cycle with \(r\ge3\) edges has constant exactly \(r-1\), regardless of which edge is omitted.

For integer-weighted cycles with a designated deleted edge, the decision problem whether \(K(\mathcal B_T)=S_C/h_C\) is NP-complete, even under the edge-geodesicity hypothesis above. This decision is equivalent to whether \(\Delta_C\le h_C\).

## Assumptions and scope
All spaces, coefficients and sign changes are real. A cactus is finite, connected, simple and has pairwise edge-disjoint simple cycles; attached tree edges may have any positive lengths. The metric on \(V\) is the shortest-path metric, not the ambient Euclidean distance. An orientation of edges fixes the signs of the basis molecules but does not affect its unconditional constant. The finite-dimensional unconditional constant is
\[
 K(\mathcal B_T)=\sup_{\varepsilon_e\in\{-1,1\}}\left\|D_{\varepsilon}:\mathcal F(M)\longrightarrow\mathcal F(M)\right\|,
 \qquad D_{\varepsilon}m_e=\varepsilon_e m_e\quad(e\in T),
\]
where \(m_e=\delta(v)-\delta(u)\) for the chosen orientation \(u\to v\).

## Proof
**Step 1: Edge-flow quotient.** Fix an orientation of all edges. The edge-difference map on vertex potentials sends a Lipschitz function \(f\) to increments \(y_e=f(v)-f(u)\). Its norm is exactly \(\max_e|y_e|/w_e\), since shortest-path distances are defined by the graph edges. A feasible increment vector has zero oriented sum around each cycle; conversely such a vector integrates to a vertex potential. By finite-dimensional duality, \(\mathcal F(M)\) is isometric to
\[
 Q_G=\ell_1(E,w)/Z_G,\qquad
 \|x\|_{\ell_1(E,w)}=\sum_{e\in E}w_e|x_e|,
\]
where \(Z_G\) is the real cycle-flow space. Its quotient basis vectors correspond to edge molecules.

**Step 2: Cactus decomposition.** Distinct cactus cycles have disjoint edge supports. Consequently, \(Z_G\) is the direct sum of their one-dimensional signed cycle indicators, and
\[
 Q_G\cong
 \left(\bigoplus_{C\text{ cycle}}\ell_1(C,w)/\operatorname{span}\{\mathbf 1_C\}\right)_{\ell_1}
 \oplus_1\ell_1(E_{\mathrm{bridge}},w).
\]
An orientation may reverse coordinate signs without affecting the norm. Deleting one edge per cycle produces exactly the free coordinate basis of each cycle quotient, together with bridge coordinates. Sign-change operators are block-diagonal on this \(\ell_1\)-sum, so their optimal norm is the maximum of the block optima and \(1\).

**Step 3: One weighted cycle.** Orient the \(r\) edges cyclically, omit edge \(a\), and let \(h=w_a\), \(S=\sum_{e\ne a}w_e\). The cycle quotient has norm
\[
 q(x)=\min_{t\in\mathbb R}\sum_{e\in C}w_e|x_e+t|.
\]
The quotient unit ball is the convex hull of the signed normalized edge classes \(\pm[e]/w_e\). Thus, for any operator \(D\) on the quotient,
\[
 \|D\|=\max_{e\in C}\frac{q(D[e])}{w_e}.
\]
For a sign change on the retained edges, \(D[e]=\varepsilon_e[e]\) when \(e\ne a\). The geodesicity assumption gives \(q([e])=w_e\), hence these ratios equal \(1\). Since \([a]=-\sum_{e\ne a}[e]\), the only remaining ratio is
\[
 \frac1h\min_{t\in\mathbb R}
 \left(h|t|+\sum_{e\ne a}w_e|\varepsilon_e+t|\right).
\]
This convex piecewise-linear function has a minimizer at one of \(t=-1,0,1\). If \(S_+\) and \(S_-\) are the sums of retained weights with positive and negative signs, its three values are \(h+2S_-\), \(S\), and \(h+2S_+\). The least value is
\[
 \min\{S,\ h+S-|S_+-S_-|\}.
\]
Maximizing over the signs is therefore equivalent to minimizing the discrepancy \(|S_+-S_-|\), and yields
\[
 K_C=\frac{\min\{S,h+S-\Delta\}}{h}.
\]
Because \(h\le S\) and \(\Delta\le S\), this quantity is at least \(1\). This proves the cactus formula. For unit weights, \(\Delta\in\{0,1\}\) and \(h=1\), hence \(K_C=r-1\).

**Step 4: Decision complexity.** The equality \(K_C=S/h\) holds exactly when \(\Delta\le h\). For integer weights, membership in NP follows from a certificate consisting of signs on the retained edges. For NP-hardness reduce the positive-integer PARTITION problem. Instances with odd total, fewer than two entries, or an entry greater than half the total are immediately negative or trivial and can be mapped to fixed eligible yes/no instances. For an instance \(a_1,\ldots,a_m\) with even total \(A\), \(m\ge2\), and \(\max_i a_i\le A/2\), make a simple \((m+1)\)-cycle whose retained edges have lengths \(2a_1,\ldots,2a_m\) and whose deleted edge has length \(h=1\). Every edge is geodesic because \(4a_i\le2A+1\); the distinguished edge is geodesic as well. The discrepancy equals
\[
 \Delta=2\min_{\varepsilon_i\in\{-1,1\}}\left|\sum_i\varepsilon_i a_i\right|.
\]
Since \(A\) is even, either \(\Delta=0\) or \(\Delta\ge4\). Therefore \(K_C=2A\) exactly when the original integers admit an equal-sum partition. The reduction uses polynomially many edges and binary digits. A fixed negative target is the four-cycle with consecutive weights \((2,2,2,1)\) and the last edge omitted; a fixed positive target is the four-cycle with weights \((2,2,2,2)\). Thus the decision problem is NP-complete.

## Verification
The included script `verify_weighted_cycle.py` uses exact rational arithmetic. Independently of the quotient-median expression, it computes the norm of a signed edge combination by maximizing over the vertices of the dual edge-increment polytope
\[
 \left\{y\in\mathbb R^r: \sum_e y_e=0,\quad |y_e|\le w_e\right\}.
\]
Every vertex has all but at most one coordinate at a box endpoint, which the script enumerates. It compares the resulting unconditional constants with the discrepancy formula on \(284\) weighted cycle instances, covering lengths \(3\) through \(7\) and different omitted edges. It also checks the unit-weight formula in lengths \(3\) through \(8\) and several partition instances. Execute with `python3 verify_weighted_cycle.py` in a directory containing this result and the script. These finite checks are not the proof of the all-cactus statement.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (arXiv:1807.03814, initial public version July 10, 2018) give the finite graph edge-flow quotient for unweighted metrics and study complementability and graph families; their quotient identity supplies the geometric starting point but not the sign-unconditional cactus formula. Novotný (arXiv:1905.13188, initial public version May 30, 2019) studies retractional Schauder bases on graph circles and conditionality on nets, with different bases and quantitative invariants. Basso (arXiv:2104.14238, initial public version April 29, 2021) studies linear Lipschitz extension constants and relative projections, not unconditional constants of edge-molecule bases. Related published calculations of numerical indices on graph cycles concern the norm of all operators through numerical radius, not these designated sign-change operators.

The present theorem's central distinction is an exact parameter-sensitive formula for a canonical finite-dimensional basis over every weighted cactus, including a partition-discrepancy threshold and a complexity classification. The literature search does not establish uniqueness; an equivalent formula for weighted \(\ell_1\)-quotient bases may exist under different indexing.

## Limitations
The theorem is restricted to real scalars, finite connected cactus graphs, and metric weights satisfying the stated cycle-edge geodesicity condition. It does not classify arbitrary Banach-space bases, unrestricted graphs with overlapping cycles, or the optimal basis selected among all possible bases. NP-completeness concerns exact decision from binary-encoded integer edge lengths, not approximation hardness. The unit-weight cycle case is a specialization rather than a separate claim.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first posted July 10, 2018), especially Section 1.1 and the cycle-flow quotient.
2. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188 (first posted May 30, 2019), especially Theorem 5 and Section 4.
3. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first posted April 29, 2021), Section 1.
4. Classical NP-completeness of PARTITION (used only for the complexity reduction).
