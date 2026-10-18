# Cycle-space incenter loci and sharp radius phases of biregular bipartite matching polytopes

## Finding

Let \(G=(L\sqcup R,E)\) be a **connected simple biregular bipartite graph** with \(p=|L|\), \(q=|R|\), \(2\le p<q\), \(m=|E|\), common left degree \(a=m/p\), and common right degree \(b=m/q\). For integer \(1\le k\le p\), let \(P_k(G)\subset\mathbb R^E\) be the convex hull of the incidence vectors of matchings of size \(k\), equipped with the standard Euclidean edge-coordinate metric. Every such graph has a matching saturating \(L\).

**Nonsaturating regime, \(1\le k<p\).** The intrinsic Euclidean inradius is
\[
r_k(G)=\min\left\{\frac{k}{\sqrt{m(m-1)}},\frac{p-k}{\sqrt{m(p-1)}}\right\}.
\]
Define
\[
K_{p,m}=\frac{p\sqrt{m-1}}{\sqrt{m-1}+\sqrt{p-1}}.
\]
If \(k\le K_{p,m}\), the uniform vector \(U=(k/m)\mathbf1_E\) is the unique incenter. If \(k>K_{p,m}\), the complete set of incenters is
\[
\left\{x:\sum_{e\ni u}x_e=k/p\ (u\in L),\quad x_e\ge r_k\sqrt{1-1/m},\quad \sum_{e\ni v}x_e\le1-r_k\sqrt{b(1-b/m)}\ (v\in R)\right\},
\]
whose affine dimension is **exactly \(m-p\)**. At \(U\), the shifted coordinate supporting inequalities touch when \(k<K_{p,m}\), the \(p\) shifted left-degree supporting inequalities touch when \(k>K_{p,m}\), and both families touch at equality; no shifted right-degree inequality touches.

**Saturating regime, \(k=p\).** The affine hull consists of edge weights summing to one at every left vertex. With \(a=m/p\),
\[
r_p(G)=\min\left\{\frac1{\sqrt{a(a-1)}},\frac{q-p}{\sqrt{pq(a-1)}}\right\}.
\]
If \((q-p)^2a\ge pq\), the uniform vector \(U=\mathbf1_E/a\) is the **unique** incenter. If \((q-p)^2a<pq\), put
\[
\lambda=\frac{q-p}{\sqrt{pqa}},\qquad \tau=1-a\lambda>0
\]
and define the strictly feasible graph-supported transportation polytope
\[
\mathcal T_G=\left\{y\in\mathbb R_{\ge0}^E:\sum_{e\ni u}y_e=1\ (u\in L),\quad \sum_{e\ni v}y_e=p/q\ (v\in R)\right\}.
\]
Then **every** maximum-ball center, and no other point, belongs to
\[
\mathcal I_p(G)=\lambda\mathbf1_E+\tau\mathcal T_G,
\qquad \dim\operatorname{aff}\mathcal I_p(G)=m-p-q+1.
\]
Thus the dimension of the incenter locus is exactly the **cycle rank** of the connected graph \(G\), a topological invariant. In the strict column-dominated regime, all \(q\) right-degree supporting hyperplanes touch the uniform optimal ball; in the strict coordinate-dominated regime all \(m\) nonnegativity hyperplanes touch it. At equality both sets touch, but the incenter is unique. A supporting hyperplane is not automatically asserted to be a facet for arbitrary sparse \(G\).

**A sparse-graph sharp transition.** Let \(G_n\), \(n\ge4\), be the vertex-edge incidence bipartite graph of the ordinary complete graph \(K_n\): its left vertices are the \(n\) original vertices, its right vertices are the \(\binom n2\) original edges, and incidences are its \(n(n-1)\) edges. For maximum matchings of \(G_n\), the ratio of the right-degree and coordinate inball bounds is \((n-3)/\sqrt2\). Therefore \(G_4\) has an entire **three-dimensional** incenter polytope, while for every \(n\ge5\) the incenter is **unique**, despite the growth of the underlying cycle spaces. The values are
\[
r_n=\begin{cases}1/\sqrt{12},&n=4,\\1/\sqrt{(n-1)(n-2)},&n\ge5.\end{cases}
\]
In fact, the two successive incidence examples have the **same** inradius \(1/\sqrt{12}\), yet the center dimension falls from three to zero. The formulas apply to all connected biregular support graphs, not merely complete bipartite graphs.

## Assumptions and scope

Distances are measured in the affine hull of \(P_k(G)\), using the unscaled standard Euclidean norm on \(\mathbb R^E\). The degree relation is \(pa=qb=m\), and \(p<q\) implies \(a>b\ge2\) because a connected graph with \(p\ge2\) cannot have all right degrees equal to one. Hall's theorem guarantees a matching saturating \(L\): for any \(S\subseteq L\), count \(a|S|\) outgoing incidences to a right neighborhood with capacity \(b\) each, giving \(|N(S)|\ge a|S|/b=(q/p)|S|\ge|S|\).

Torres's bipartite \(k\)-matching theorem identifies \(P_k(G)\) with the entire fractional region
\[
\{x\in\mathbb R^E:x_e\ge0,\ \sum_{e\ni w}x_e\le1\ (w\in L\sqcup R),\ \sum_{e\in E}x_e=k\}.
\]
For \(k<p\), the strictly positive uniform point satisfies every degree inequality strictly, so the affine hull is the sum-equals-\(k\) hyperplane. For \(k=p\), all left degree sums are identically one; uniform weights satisfy the remaining inequalities strictly, so those \(p\) independent equations are the entire affine hull. No extra facial assumptions are made.

## Proof

**1. Exact ball-containment constraints.** Let \(H_k\) be the direction space of the affine hull. A ball of radius \(r\) about a feasible center \(x\) remains in the halfspace \(\langle c,z\rangle\le d\) precisely when \(\langle c,x\rangle+r\|\operatorname{proj}_{H_k}c\|_2\le d\). This elementary support-function identity is applied to *every* inequality in the exact fractional description above.

For \(k<p\), \(H_k=\{z:\sum_E z_e=0\}\). Since all left vertices have degree \(a=m/p\) and all right vertices degree \(b=m/q\), the projected norms of an edge indicator, a left-degree indicator, and a right-degree indicator are respectively
\[
D_0=\sqrt{1-1/m},\quad D_L=\sqrt{a(1-1/p)},\quad D_R=\sqrt{b(1-1/q)}.
\]
Consequently the ball containment system is
\[
x_e\ge rD_0,\quad \sum_{e\ni u}x_e\le1-rD_L\ (u\in L),\quad \sum_{e\ni v}x_e\le1-rD_R\ (v\in R).
\tag{1}
\]

**2. Nonsaturating optimality and all centers.** Sum the three types of inequalities in (1), respectively over all \(m\) edges, all \(p\) left vertices, and all \(q\) right vertices. The exact bounds are
\[
r\le\frac{k}{\sqrt{m(m-1)}},\quad
r\le\frac{p-k}{\sqrt{m(p-1)}},\quad
r\le\frac{q-k}{\sqrt{m(q-1)}}.
\]
For \(p<q\) and \(k\ge1\), the function \(f(t)=(t-k)/\sqrt{t-1}\) is strictly increasing for \(t\ge p\), because \(f'(t)=(t+k-2)/(2(t-1)^{3/2})>0\). Hence the right bound is always strictly weaker than the left bound. At \(U=(k/m)\mathbf1_E\), all inequalities within each family have the same slack; its nearest supporting hyperplane therefore attains the minimum of these bounds. Comparison of the first two bounds yields exactly \(k\le K_{p,m}\).

If the coordinate obstruction is minimal, summing \(x_e\ge rD_0\) forces equality for all \(m\) edges, so the sole center is \(U\), even at a tie. If the left-degree obstruction is strictly smaller, summing all left-degree cap conditions forces each left sum to be \(k/p\). The other conditions are precisely the center locus in the Finding. Both other families of inequalities are strict at \(U\); therefore a relatively open neighborhood of \(U\) in the affine space of \(p\) independent left-degree equations is feasible, giving full affine dimension \(m-p\).

**3. Saturation changes the metric.** At \(k=p\), the direction space becomes
\(H_p=\{z:\sum_{e\ni u}z_e=0\ (u\in L)\}\). Left-star supports are pairwise disjoint. Projecting one edge indicator within its \(a\)-element left star gives squared norm \(1-1/a\). Each right vertex is adjacent to \(b\) *different* left stars in the simple graph, and each incident edge contributes a projected vector of squared norm \(1-1/a\), orthogonal to the other stars. Thus
\[
D'_0=\sqrt{1-1/a},\qquad D'_R=\sqrt{b(1-1/a)}.
\]
The affine-hull ball conditions reduce exactly to
\[
x_e\ge rD'_0,\quad\sum_{e\ni v}x_e\le1-rD'_R\ (v\in R),\quad\sum_{e\ni u}x_e=1\ (u\in L).
\tag{2}
\]
Summing the first inequalities over edges and the second over right vertices yields
\[
r\le\frac1{\sqrt{a(a-1)}},\qquad
r\le\frac{q-p}{\sqrt{pq(a-1)}}.
\]
As before, \(U=\mathbf1_E/a\) attains the smaller bound: each left sum is one and each right sum is \(b/a=p/q<1\). The second bound is smaller precisely when \((q-p)^2a<pq\).

If coordinates control, their sum forces \(x=U\). Otherwise, all \(q\) shifted right inequalities must be equalities, yielding \(\sum_{e\ni v}x_e=p/q\). The edge floors are \(rD'_0=\lambda=(q-p)/\sqrt{pqa}\). Since \(\tau=1-a\lambda>0\), the transformation \(x_e=\lambda+\tau y_e\) yields simultaneously \(y_e\ge0\), left sums one, and right sums \(p/q\). It is bijective between the entire center locus and \(\mathcal T_G\). Its strictly positive point \(y_e=1/a\) shows that the affine hull is exactly the solution space of these equations. The incidence matrix of a connected bipartite graph has rank \(p+q-1\) (multiply one vertex class by minus one to obtain the oriented incidence matrix, whose rank is \(|V|-1\)); hence \(\dim\mathcal T_G=m-p-q+1\). If the two obstructions tie, coordinates again force uniqueness. All statements about which support planes touch at \(U\) follow directly from equality versus strictness of the bounds, without requiring every plane to define a facet.

**4. Sparse incidence family.** In \(G_n\), the parameters are \(p=n\), \(q=n(n-1)/2\), \(m=n(n-1)\), \(a=n-1\), and \(b=2\). Thus the ratio between the second and first bounds of step 3 simplifies to \((n-3)/\sqrt2\). At \(n=4\) the second bound wins and the cycle-space dimension is \(12-4-6+1=3\). At every \(n\ge5\) the first bound wins, hence the unique-center formula and displayed radii.

## Verification

The standalone `check_inballs.py` constructs the intrinsic ball-containment linear program directly from the graph's edge incidences, rather than from the closed formulas, and tests 110 complete-bipartite parameter profiles and 22 connected sparse vertex-edge incidence-graph profiles, totaling 132 independent linear programs. It verifies both radius and contact/equality ranks. Run `python -m pip install -r requirements.txt` followed by `python check_inballs.py`. Finite numerical optimization is a cross-check only; the exact all-graph proof is steps 1–4.

## Relationship to prior work

Torres's June 20, 2023 preprint proves the exact fractional H-description for \(k\)-matching polytopes of **arbitrary bipartite graphs**, making it possible to apply the present geometric argument uniformly to sparse support graphs. Gill and Linusson (2009) gave that description previously for **complete bipartite** \(k\)-assignment polytopes, and studied their combinatorial faces and graph diameters; that older special case alone does not cover the present sparse-graph theorem.

A closely related indexed *Birkhoff-polytope family of incenters for partial assignment polytopes* computes the square complete-bipartite family. A prior *Three contact regimes for rectangular assignment-polytope John ellipsoids* result concerns maximum-volume ellipsoids of **complete** rectangular supports, not intrinsic Euclidean largest balls or sparse-graph cycle-space center loci. An indexed inradius theorem for positive-margin transportation polytopes assumes both vertex classes' sums are **equalities** throughout the original polytope; here the right caps are inequalities, and the transportation polytope arises **as the optimal-center locus only in one phase**. Their statements do not imply the sparse biregular classification here. Full text of the indexed square-incenter result was unavailable, and an equivalent graph-supported formulation is a residual bibliographic risk.

## Limitations

The result requires connected simple biregular bipartite graphs with \(2\le p<q\); it does not cover all irregular bipartite graphs, equal part sizes, degenerate rank, or arbitrary rescaled Euclidean edge metrics. Tangent planes are classified at the uniform center, but for sparse graphs they need not all be individual facets. The theorem computes the affine dimension, not the full face vector, of each positive-dimensional incenter polytope. Independent mathematical validation has not been performed; numerical tests cannot establish the universal theorem, and unindexed prior literature may contain equivalent statements.

## References

1. Juan Camilo Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, first publicly submitted **2023-06-20**, arXiv:`2306.11910`, notably Theorem 3.1 (exact fractional H-representation) and Theorem 4.8 (normality).
2. Jonna Gill and Svante Linusson, *The k-assignment polytope*, Discrete Optimization 6 (2009), 148–161, DOI:`10.1016/j.disopt.2008.10.003`. Lawful postprint: `https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf` (complete bipartite special case, Theorem 3 and facet table).
3. *A Birkhoff-polytope family of incenters for partial assignment polytopes*, indexed published finding (square complete-bipartite family, accessible indexed abstract).
4. *Exact intrinsic Euclidean inradius and centers of transportation polytopes*, indexed published finding (positive-margin fixed-row-and-column family, accessible indexed abstract).
5. *Three contact regimes for rectangular assignment-polytope John ellipsoids*, earlier geometric result (complete support and maximum-volume ellipsoids, not Euclidean ball center spaces).
