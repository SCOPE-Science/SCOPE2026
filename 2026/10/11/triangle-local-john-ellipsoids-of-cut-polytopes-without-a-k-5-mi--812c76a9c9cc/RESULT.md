# Triangle-local John ellipsoids of cut polytopes without a \(K_5\) minor

## Finding

Let \(G=(V,E)\) be any finite simple graph with at least one edge and no \(K_5\) minor. For each vertex subset \(S\subseteq V\), let \(\delta(S)\) denote its edge cut and define the full-dimensional cut polytope
\[
P_G=\operatorname{conv}\{\mathbf1_{\delta(S)}:S\subseteq V\}\subset\mathbb R^E.
\]
Let \(\mathcal T\) be the family of edge sets of triangles of \(G\), and put \(m=|E|\). There is a **unique** vector \(s^*\in(0,\infty)^E\) maximizing
\[
\sum_{e\in E}\log s_e
\quad\text{subject to}\quad
s_e\le\tfrac14\ (e\in E),\qquad
\sum_{e\in T}s_e\le\tfrac14\ (T\in\mathcal T).
\tag{1}
\]
The unique maximum-volume Euclidean ellipsoid contained in \(P_G\) is
\[
\boxed{\mathcal E_G=\left\{\tfrac12\mathbf1_E+\operatorname{diag}(\sqrt{s_e^*})u:\|u\|_2\le1\right\}.}
\tag{2}
\]
Its squared principal semiaxes are the entries of \(s^*\), and its volume is
\[
\boxed{\operatorname{vol}_m(\mathcal E_G)=
\frac{\pi^{m/2}}{\Gamma(m/2+1)}\prod_{e\in E}\sqrt{s_e^*}.}
\tag{3}
\]
In particular, \(s_e^*=1/4\) for an edge belonging to no triangle, while \(0<s_e^*<1/4\) for each edge in at least one triangle. Therefore the **entire ellipsoid shape depends only on edge--triangle incidence**, even though the surrounding cut polytope may have facets from arbitrarily long induced cycles. As a special case, **every triangle-free graph in the stated minor-free class has the radius-\(1/2\) Euclidean ball centered at \(\mathbf1_E/2\) as its John ellipsoid**, regardless of its other cycle structure.

**Complete facet-contact classification.** Each of the two coordinate facets of a nontriangle edge touches \(\mathcal E_G\). Each of the four odd-signed inequalities of a triangle \(T\) touches exactly when \(\sum_{e\in T}s_e^*=1/4\). Each of the eight odd-signed facets of a chordless quadrilateral touches exactly when its four edges belong to no triangle. No facet belonging to a chordless cycle of length at least five touches. These are **all** facet contacts. For any contacting facet \(a^Tx\le b\), its unique ellipsoid contact point is
\[
\boxed{\tfrac12\mathbf1_E+
\frac{\operatorname{diag}(s^*)a}{\sqrt{\sum_{e\in E}a_e^2s_e^*}}.}
\tag{4}
\]

The optimization (1) is an exact variational determination for every graph in the stated class, not a claim of a radical closed form for all such graphs. The unique optimum also satisfies the finite stationarity and complementarity equations stated below. The exceptional case of a graph consisting of a single edge gives the interval \([0,1]\) with its inscribed radius \(1/2\).

**Explicit infinite families.** For the wheel \(W_k=K_1\vee C_k\) with \(k\ge4\), there are \(k\) spokes and \(k\) rim edges and
\[
\boxed{s_{\mathrm{spoke}}^*=\tfrac1{16},\qquad s_{\mathrm{rim}}^*=\tfrac18.}
\]
Every triangle facet touches, while no coordinate or longer-cycle facet does. The volume is \(\kappa_{2k}(8\sqrt2)^{-k}\), where \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\).

For the \(n\)-page triangle book \(B_n=K_2\vee\overline{K_n}\) with \(n\ge1\), its one common spine edge and \(2n\) page edges have
\[
\boxed{s_{\mathrm{spine}}^*=\frac1{4(2n+1)},\qquad
s_{\mathrm{page}}^*=\frac{n}{4(2n+1)}.}
\]
Thus the spine semiaxis tends to zero as the page count grows, whereas the page semiaxes tend to \(1/\sqrt8\). Again every triangle facet touches. For any cactus graph, edges contained in triangles have \(s_e^*=1/12\), and all remaining edges have \(s_e^*=1/4\).

## Assumptions and scope

The graph is finite, undirected, simple, may be disconnected or have isolated vertices, has at least one edge, and excludes a \(K_5\) minor. Each coordinate of \(\mathbb R^E\) is an edge; the Euclidean structure is the usual one in these cut-incidence coordinates. A chordless cycle is a simple cycle without a graph edge joining nonconsecutive cycle vertices. Every chordless cycle and nontriangle-edge inequality mentioned above is a genuine facet by the cited description; the result makes no assertion for graphs with a \(K_5\) minor. A **John ellipsoid** here means the largest-volume *inscribed* ellipsoid, not the smallest-volume circumscribed Löwner ellipsoid. The optimizing covariance parameter \(s_e\) is the squared semiaxis, not the semiaxis itself.

## Proof

**1. Symmetry forces the center and diagonal shape.** An arbitrary ellipsoid can be written \(\mathcal E(c,Q)=\{c+Q^{1/2}u:\|u\|_2\le1\}\) with \(Q\) positive definite. For every \(A\subseteq V\), the cut-switching map
\[
(x_e)_{e\in E}\longmapsto
\bigl(\mathbf1_{e\notin\delta(A)}x_e+
\mathbf1_{e\in\delta(A)}(1-x_e)\bigr)_{e\in E}
\]
permutes cut vertices, because \(\delta(S)\mathbin\triangle\delta(A)=\delta(S\mathbin\triangle A)\). It is an affine Euclidean isometry preserving \(P_G\). By uniqueness of the maximal-volume inscribed ellipsoid, it fixes the ellipsoid. For each edge \(e=uv\), switching at \(\{u\}\) flips that coordinate, forcing \(c_e=1/2\). For distinct edges \(e\ne f\), choose an endpoint of \(e\) not belonging to \(f\); switching at that singleton flips \(e\) and not \(f\), so invariance of \(Q\) forces \(Q_{ef}=0\). Consequently every optimal ellipsoid has \(c=\mathbf1_E/2\) and \(Q=\operatorname{diag}(s_e)\), with \(s_e>0\).

**2. Use the complete published facet description.** Barahona--Mahjoub, Corollary 3.10, says that for a graph without a \(K_5\) minor, the irredundant halfspaces defining \(P_G\) comprise \(0\le x_e\le1\) on each edge not in a triangle, and, for each chordless cycle \(C\) and each odd-cardinality subset \(F\subseteq C\), the signed-cycle inequality
\[
\sum_{e\in F}x_e-\sum_{e\in C\setminus F}x_e\le|F|-1.
\tag{5}
\]
(The harmless upper bound \(x_e\le1\) on *all* edges can be imposed additionally; it is implied by triangles when necessary.) The support of our diagonal ellipsoid on a linear form \(a\) is
\[
\sup_{x\in\mathcal E}a^Tx=a^T(\mathbf1_E/2)+\sqrt{\sum_{e\in E}a_e^2s_e}.
\tag{6}
\]
A coordinate halfspace imposes \(s_e\le1/4\). In (5), if \(|C|=k\), the center's slack is exactly \((k-2)/2\), independently of the chosen odd \(F\), and all nonzero normal coefficients have squared value one. Hence the whole family for the given cycle is satisfied exactly when
\[
\sum_{e\in C}s_e\le\frac{(k-2)^2}{4}.
\tag{7}
\]
For \(k=3\) this is the triangle inequality in (1). For \(k\ge4\), all upper bounds \(s_e\le1/4\) imply \(\sum_{e\in C}s_e\le k/4\le(k-2)^2/4\); the last inequality is an equality only for \(k=4\). Thus no constraint coming from a chordless cycle of length \(\ge4\) restricts a diagonal ellipsoid beyond the simple box constraints. Conversely, an ellipsoid inside \(P_G\) satisfies every triangle constraint, and it satisfies all coordinate bounds: directly for nontriangle edges; for triangle edges because positivity and that edge's triangle inequality give \(s_e<1/4\). This proves the exact feasibility equivalence (1).

**3. Maximize volume and prove uniqueness.** The ellipsoid's volume is \(\kappa_m\sqrt{\prod_e s_e}\), so maximizing volume is equivalent to (1). The feasible set in the nonnegative cube is compact, contains a strictly positive point, and \(\sum_e\log s_e\) tends to \(-\infty\) whenever any coordinate approaches zero. Strict concavity supplies a unique strictly positive maximizer. The argument of Step 1 shows that *every* globally optimal ellipsoid is diagonal, so this unique diagonal solution is globally optimal, not merely symmetric-optimal. An optional computational characterization is given by multipliers \(\mu_e,\lambda_T\ge0\) with
\[
\frac1{s_e^*}=\mu_e+\sum_{T\ni e}\lambda_T,\qquad
\mu_e(s_e^*-\tfrac14)=0,\qquad
\lambda_T(\sum_{e\in T}s_e^*-\tfrac14)=0.
\tag{8}
\]
Slater's condition holds, so these conditions are necessary and sufficient. If an edge is in no triangle, increasing its \(s_e\) to \(1/4\) improves the objective, proving its stated value. If it belongs to a triangle, its value is strictly below \(1/4\), since the other two entries in that triangle are positive.

**4. Exhaust all contacts.** For a facet with center slack \(h=b-a^Tc\), (6) shows tangency if and only if \(\sum a_e^2s_e^*=h^2\). The coordinate, triangle, and quadrilateral assertions follow directly from the equalities in Steps 2--3. For a chordless cycle of length \(k\ge5\), \(\sum_{e\in C}s_e^*\le k/4<(k-2)^2/4\), so none can touch. Since the cited list contains every facet, no other facet contacts exist. The Cauchy--Schwarz equality case gives (4), hence a unique contact point for each touching facet.

**5. Evaluate the families.** In a wheel, each spoke belongs to two triangle constraints and each rim edge to one. Taking \(s_{\mathrm{spoke}}=1/16\) and \(s_{\mathrm{rim}}=1/8\), every triangle has sum \(1/4\). Assign multiplier \(8\) to each triangle and zero box multipliers: (8) holds for both edge types, proving exact global optimality. In a book, each page edge belongs to one triangle and the spine to all \(n\). With the stated \(s\), all \(n\) triangles have sum \(1/4\); assigning multiplier \(4(2n+1)/n\) to each triangle verifies (8). In a cactus, triangles are edge-disjoint, so each triangle independently maximizes the product of its three entries with fixed sum \(1/4\), yielding \(1/12\) each; nontriangle edges attain their coordinate caps. All these graphs are planar and therefore exclude a \(K_5\) minor.

## Verification

The bundled standard-library program `verify.py` uses exact rational arithmetic. It assembles chordless cycles and triangle constraints, checks stationarity/complementarity as sufficient strict-concavity certificates, and checks all relevant signed-cycle halfspaces against every graph cut. It checked 22 instances (wheels, triangle books, paths, chordless cycles, a cactus, and \(K_4\)), 1,522 signed-cycle facet inequalities and 12,840 tested cut assignments. Execution command: `python3 verify.py`. A separate numerical convex-hull stress test on selected small graphs agreed with the predicted covariance, but is not needed for the proof. Finite enumeration is explicitly not an exhaustive verification of the theorem for arbitrary graphs; the proof depends on the exact published facet theorem and the preceding inequalities.

## Relationship to prior work

Barahona and Mahjoub (1986) establish the complete \(K_5\)-minor-free cut-polytope facet system used as a premise. Their facet classification does not state the maximal inscribed ellipsoid, its log-determinant triangle reduction, or facet-contact collapse. Chimani, Juhnke-Kubitzke, Nover and Römer (2019) examine cut-polytope facet and combinatorial structures for minor-free graphs; their paper does not report these metric quantities. Nikolaev (2024) computes graph-of-polytope diameters and clique numbers for cut polytopes; those are one-skeleton invariants, not Euclidean semiaxis or facet-contact claims. Gartsman and Linial (2023) determine inner and outer ellipsoids of the **metric polytope**, a distinct and generally larger object, and explicitly raise the cut-polytope ellipsoid as a question in their discussion. The present result answers that geometric question **only on the stated \(K_5\)-minor-free graph class**. General inscribed-ellipsoid log-determinant optimization is standard; the cut-switching diagonalization plus disappearance of every induced-cycle constraint longer than a triangle, and the complete contact classification, are the specific structural assertions here.

## Limitations

This is a Euclidean-coordinate result and does not claim affine-invariant formulas under arbitrary changes of embedding. For arbitrary eligible graphs, (1) is a uniquely solvable finite concave optimization, not a universal closed-form expression in graph size or degree. A graph with a \(K_5\) minor can possess extra cut facets that invalidate the reduction. The theorem concerns the *inscribed* John ellipsoid, not the circumscribed Löwner ellipsoid; it does not determine the latter, and it does not resolve the cut-polytope question for complete graphs of order at least five. Bibliographic equivalences under different optimization terminology remain possible; no independent priority or proof audit is asserted.

## References

1. F. Barahona and A. R. Mahjoub, “On the cut polytope,” *Mathematical Programming* **36** (1986), 157–173, especially Corollary 3.10, https://www.lamsade.dauphine.fr/~mahjoub/Papers/BM86.pdf ; DOI: 10.1007/BF02592023.
2. A. V. Nikolaev, “On 1-skeleton of the cut polytopes,” arXiv:2402.13591v1, first posted 21 February 2024, https://arxiv.org/html/2402.13591v1 ; primary MSC 52B05.
3. R. Gartsman and N. Linial, “On the Löwner-John Ellipsoids of the Metric Polytope,” arXiv:2305.02113v1, especially Section 4, https://arxiv.org/html/2305.02113v1.
4. M. Chimani, M. Juhnke-Kubitzke, A. Nover and T. Römer, “Cut Polytopes of Minor-free Graphs,” arXiv:1903.01817v1, https://arxiv.org/pdf/1903.01817.
