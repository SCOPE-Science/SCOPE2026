# John ellipsoids of complete split-graph Lipschitz balls and a sharp clique-edge screening law

## Finding
For integers \(p\ge3\) and \(q\ge2\), let \(G_{p,q}=K_p\vee\overline K_q\) be the complete split graph: the \(p\) vertices of a clique \(A\) are adjacent to one another and to all \(q\) independent vertices in \(B\), and no pair in \(B\) is adjacent. Give each edge length one and use the shortest-path metric. Set \(N=p+q\), \(d=N-1\), and \(H=\{x\in\mathbb R^N:\sum_i x_i=0\}\) with its inherited Euclidean metric. The real Lipschitz-dual unit ball is
\[
Q_{p,q}=\{x\in H:|x_i-x_j|\le1\text{ for every edge }ij\in E(G_{p,q})\}.
\]
Let \(P_A\) be orthogonal projection onto zero-sum vectors supported on \(A\) (dimension \(p-1\)), let \(P_B\) be the analogous projection onto \(B\) (dimension \(q-1\)), and put \(P_C=I_H-P_A-P_B\) (dimension one). Define \(S=aP_A+bP_B+cP_C\), where
\[
(a,b,c)=
\begin{cases}
\left(\frac{p}{d},\frac{q}{d},\frac{pq}{Nd}\right),&q\ge p+1,\\[2pt]
\left(\frac12,\frac{p+1}{2p},\frac{p+1}{2N}\right),&2\le q\le p.
\end{cases}
\]
**The unique maximum-volume inscribed (John) ellipsoid** of \(Q_{p,q}\) is
\[
\boxed{E_{p,q}=\{x\in H:\langle x,S^{-1}x\rangle\le1\}.}
\]
Its intrinsic Euclidean volume is exactly
\[
\boxed{\operatorname{vol}_d(E_{p,q})=\frac{\pi^{d/2}}{\Gamma(1+d/2)}\sqrt{a^{p-1}b^{q-1}c}.}
\]
Every one of the \(2pq\) oriented cross-edge facets is tangent to this ellipsoid. All \(p(p-1)\) oriented clique-edge facets are also tangent if and only if \(q\le p+1\). At \(q=p+1\), clique facets are tangent although no positive clique-edge weight is needed in the optimal certificate. When \(q\ge p+2\), every clique facet is strictly separated from the ellipsoid.

**Sharp invisible-edge law.** Let \(Q^{\mathrm{bi}}_{p,q}\) be the Lipschitz-dual ball of the complete bipartite graph \(K_{p,q}\), with the same zero-sum Euclidean realization. Then \(Q_{p,q}\subsetneq Q^{\mathrm{bi}}_{p,q}\), yet their unique John ellipsoids coincide **if and only if** \(q\ge p+1\). Equivalently, the Löwner ellipsoids of the corresponding symmetric edge polytopes coincide in precisely that parameter range. Thus adding all \(\binom p2\) clique edges becomes ellipsoid-invisible at the sharp boundary \(q=p+1\).

## Assumptions and scope
All statements concern the inherited Euclidean metric on the \((N-1)\)-dimensional hyperplane \(H\), not anchored-coordinate Lebesgue volume or a metric-free Banach–Mazur invariant. All edges have length one and the graph is simple and connected. The inequalities on edges characterize the unit Lipschitz ball because nonedge distances are shortest-path distances. The result is proved for every integer \(p\ge3\), \(q\ge2\); the already-investigated two-hub book-graph case \(p=2\) is expressly excluded from the new claim. All positive-definite matrices and determinants below act on \(H\).

## Proof
**1. Symmetry decomposition and exact support conditions.** The three projectors are orthogonal and sum to \(I_H\). A clique-edge root \(r=e_i-e_j\), with both endpoints in \(A\), lies in the range of \(P_A\) and has squared norm \(2\). A cross-edge root has squared projection norms \((p-1)/p\), \((q-1)/q\), and \(N/(pq)\) onto \(P_A\), \(P_B\), and \(P_C\), respectively; these sum to \(2\). For the origin-centered ellipsoid with shape \(S\), the support in the direction \(r\) equals \(\sqrt{\langle r,Sr\rangle}\). Accordingly, containment of \(E_{p,q}\) in \(Q_{p,q}\) is equivalent to the two inequalities
\[
2a\le1,\qquad
\frac{p-1}{p}a+\frac{q-1}{q}b+\frac{N}{pq}c\le1.
\]
In particular, the stated values are positive, cross-edge supports equal one, and clique-edge squared supports equal \(2a\). The latter equal one for \(q\le p+1\) and are strictly smaller for \(q\ge p+2\).

**2. A positive weighted-edge certificate.** Give each undirected cross edge equal weight \(w\) and each undirected clique edge weight \(v\), where
\[
(w,v)=\begin{cases}
(1/(pq),0),&q\ge p+1,\\[2pt]
\left(2/[d(p+1)],\ 2(p+1-q)/[dp(p+1)]\right),&2\le q\le p.
\end{cases}
\]
Both weights are nonnegative and every cross-edge weight is positive. A direct calculation gives
\[
pq\,w+\binom p2v=1.
\]
Let \(L\) be the weighted graph Laplacian,
\[
L=w\sum_{i\in A,j\in B}(e_i-e_j)(e_i-e_j)^\mathsf T
+v\sum_{\{i,j\}\subset A}(e_i-e_j)(e_i-e_j)^\mathsf T.
\]
On the three invariant spaces, its eigenvalues are exactly \(pv+qw\) (multiplicity \(p-1\)), \(pw\) (multiplicity \(q-1\)), and \(Nw\) (multiplicity one). They are all positive. Substitution into the two parameter regimes gives
\[
\boxed{S=(dL|_H)^{-1}.}
\]
Consequently, the ellipsoid from the finding is feasible and is determined by a positive weighted Laplacian of total edge weight one. When \(q=p+1\), \(v=0\) even though clique facets are tangent.

**3. Global maximality including off-center competitors.** Let \(F=y+\{z\in H:\langle z,T^{-1}z\rangle\le1\}\) be any ellipsoid contained in \(Q_{p,q}\), where \(T\succ0\) and \(y\in H\) are arbitrary. For each generating root \(r\), containment in both slabs \(\pm\langle r,x\rangle\le1\) yields
\[
\sqrt{\langle r,Tr\rangle}+|\langle r,y\rangle|\le1,
\qquad\text{hence}\quad\langle r,Tr\rangle\le1.
\]
Average these latter inequalities with the edge weights from step 2, whose sum is one. This gives \(\operatorname{tr}_H(LT)\le1\). The arithmetic–geometric mean inequality applied to the \(d\) positive eigenvalues of \(L^{1/2}TL^{1/2}\) gives
\[
\det_H(L)\det_H(T)\le
\left(\frac{\operatorname{tr}_H(LT)}d\right)^d
\le d^{-d},
\]
with equality only if \(T=(dL)^{-1}=S\). Therefore no inscribed ellipsoid has volume exceeding \(\kappa_d\sqrt{\det_H S}\). The displayed feasible ellipsoid attains this bound. If a competing ellipsoid attains equality, all positively weighted cross-edge slab inequalities in the earlier average are saturated; they then force \(\langle r,y\rangle=0\) for every cross root. Those roots span \(H\), so \(y=0\). This proves global uniqueness with no symmetry assumption on competing ellipsoids. Computing \(\det_H S=a^{p-1}b^{q-1}c\) gives the displayed volume.

**4. Exactly which facets touch.** The edge-root normals are distinct exposed vertices of \(Q_{p,q}^{\circ}\): all have squared Euclidean norm two, and the linear functional \(z\mapsto\langle r,z\rangle\) strictly exposes \(r\) among different roots. Thus every oriented edge inequality is a genuine facet of \(Q_{p,q}\). Its supporting hyperplane contacts \(E_{p,q}\) exactly when \(\langle r,Sr\rangle=1\), in which case the contact point is \(Sr\). Step 1 gives the complete classification, including the equality boundary \(q=p+1\).

**5. Sharp comparison with the complete bipartite subgraph.** Removing the clique edges leaves only the cross constraints. For \(K_{p,q}\), the uniform cross-edge design \(w=1/(pq)\) yields a feasible ellipsoid tangent to every cross facet and the same determinant-trace optimality certificate as in step 3. It is its unique John ellipsoid and has shape eigenvalues \((p/d,q/d,pq/(Nd))\). Hence the two John ellipsoids coincide whenever \(q\ge p+1\). When \(q\le p\), the bipartite ellipsoid violates the clique-edge constraint, since its clique-edge squared support is \(2p/d>1\), and therefore cannot equal the John ellipsoid of the split graph. Finally the inclusion of balls is strict: the clique-edge roots are genuine vertices of the polar symmetric-edge polytope, hence add nonredundant inequalities. This establishes the if-and-only-if law and its strict contact threshold.

## Verification
The standalone standard-library `verify.py` checks all \(342\) pairs with \(3\le p\le20\) and \(2\le q\le20\) using exact rational arithmetic. It checks the two edge-support inequalities, all three stated Laplacian eigenvalues, nonnegative normalized certificate weights, and the exact Karush–Kuhn–Tucker identities including the boundary multiplier. For \(42\) smaller instances it constructs the full rational projectors and weighted Laplacian and checks \(dSL=I_H\) entry by entry. It passed with output `EXACT_CHECKS_PASS`. These tests confirm the displayed finite instances; the all-parameter theorem is established by the proof, not by enumeration. Run `python3 verify.py` alongside this document.

## Relationship to prior work
Aliaga's work on real Lipschitz-free spaces supplies the relevant functional-analytic setting, but concerns extremal Banach-space structure rather than this ellipsoid. D'Alì, Delucchi and Michałek develop symmetric edge polytopes and their graph invariants. Mori, Mori and Ohsugi analyze facets of join-graph symmetric edge polytopes, including graphs of the form used here, but their published theorems are about facet counts, not intrinsic Euclidean ellipsoids. Suliman and Weinstein establish the general relationship between infinite Lewis weights, effective resistance and minimum-volume enclosing ellipsoids; this general D-optimality principle is **not claimed new**.

The publicly recorded book-graph ellipsoid theorem already resolves \(K_2\vee\overline K_q\), including its own sharp edge-invisibility and contact thresholds. That \(p=2\) case is **credited and excluded**, rather than repackaged. Another recorded result treats \(K_{a,a,b}\) for \(a\ge2\), a different graph family with no edges within either of its two \(a\)-vertex parts. Neither theorem by itself states or implies the exact three-eigenspace formula and clique-screening threshold for arbitrary \(p\ge3\) in \(K_p\vee\overline K_q\). The new contribution is this complete evaluation and contact classification, not the general ellipsoid-optimization method.

## Limitations
The result uses the canonical zero-sum Euclidean realization, not an arbitrary lattice-equivalent coordinate system. It makes no assertion about other complete multipartite families, nonunit edge lengths, or arbitrary graph joins. The bound \(p\ge3\) deliberately excludes an existing theorem. The equality \(q=p+1\) is a geometric tangency without positive clique-edge weight; strict geometric noncontact only begins at \(q=p+2\). The standalone finite checks do not certify all infinitely many parameters. An equivalent classification phrased as graph D-optimal design, Lewis weights or effective resistances might exist outside the inspected literature; no independent audit has been performed.

## References
1. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (first posted 2021-02-01; primary MSC 46B20), https://arxiv.org/abs/2102.01219.
2. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), https://arxiv.org/abs/1910.05193.
3. A. Mori, K. Mori and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287 (2023), https://arxiv.org/abs/2312.11287.
4. A. Suliman and O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966 (2023), https://arxiv.org/abs/2302.05966.
5. *A sharp Löwner ellipsoid edge-invisibility threshold for book-graph symmetric edge polytopes*, published open research record `87e035ae5886` (book-graph special case; complete mathematical text examined).
6. *Exact Löwner ellipsoid and sharp screening transition for \(K_{a,a,b}\) symmetric edge polytopes*, published open research record `2ec3472028bb` (different three-part family; complete mathematical text examined).
