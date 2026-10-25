# Exact John and Löwner ellipsoids of the trisected-simplex central polytope

## Finding
For each integer \(m\ge3\), put
\[
 H_m=\{x\in\mathbb R^m:\sum_{i=1}^m x_i=1\},\qquad b_m=m^{-1}\mathbf1,\qquad
 P_m=\{x\in H_m:x_i\le 2x_j\ \text{whenever }i\ne j\}.
\]
Equip \(H_m\) with the Euclidean metric inherited from \(\mathbb R^m\). This is the central polytope obtained by trisecting the edges of the regular simplex with vertices \(e_i\). Its unique John (maximum-volume inscribed) ellipsoid and Löwner (minimum-volume enclosing) ellipsoid are both Euclidean balls centered at \(b_m\). Their **squared radii** are
\[
 r_m^2=\frac1{m(5m-1)},\qquad
 R_m^2=\max_{1\le k\le m-1}\frac{k(m-k)}{m(2m-k)^2}.
\]
Writing \(m=3q+s\), with \(s\in\{0,1,2\}\), the outer ball is supported on precisely one cardinality orbit of vertices: the orbit with \(k_m\) lower coordinates, where
\[
 k_m=\begin{cases}2q,&s=0,\\2q+1,&s=1\text{ or }2.\end{cases}
\]
In particular the **only** outer contact vertices are exactly \(\binom m{k_m}\) points. The squared outer radii have the explicit three-residue formulas
\[
 R_{3q}^2=\frac1{24q}\ (q\ge1),\qquad
 R_{3q+1}^2=\frac{q(2q+1)}{(3q+1)(4q+1)^2}\ (q\ge1),\qquad
 R_{3q+2}^2=\frac{(q+1)(2q+1)}{(3q+2)(4q+3)^2}\ (q\ge1).
\]
The John ball touches all \(m(m-1)\) facets. Both contact families admit exact positive isotropic optimality certificates.

## Assumptions and scope
The claim is Euclidean and concerns the **regular** simplex represented by the coordinate vertices \(e_i\); arbitrary affine images preserve the identity of John and Löwner ellipsoids and send these two balls to corresponding affine ellipsoids, but do not generally preserve the numerical Euclidean radii. The intrinsic dimension is \(d=m-1\ge2\). All balls and volumes are computed in the affine hyperplane \(H_m\). The original all-pairs ratio conditions imply \(x_i>0\) for every point in \(P_m\), since if one coordinate were nonpositive, all coordinates would be nonpositive and their sum could not equal one.

## Proof
**1. Exact facets and the inscribed radius.** Put \(E_m=\{u\in\mathbb R^m:\sum_i u_i=0\}\) and let \(\Pi=I-\mathbf1\mathbf1^{\mathsf T}/m\) be its orthogonal projector. In centered coordinates \(x=b_m+u\), the ordered-pair inequality is
\[
 \langle a_{ij},u\rangle\le\frac1m,\qquad
 a_{ij}=e_i-2e_j+\frac1m\mathbf1=\Pi(e_i-2e_j),\qquad
 \|a_{ij}\|^2=5-\frac1m.
\]
Each inequality is a genuine facet: on \(x_i=2x_j\), take the positive coordinates \(x_j=2/(3m)\), \(x_i=4/(3m)\), and \(x_\ell=1/m\) for the other \(m-2\) indices. These sum to one, all other ordered-pair inequalities hold strictly, and the displayed equality alone is active. The ball about \(b_m\) tangent to these facets has radius \(r_m=1/\sqrt{m(5m-1)}\). It lies in \(P_m\) by the half-space inequalities.

For completeness, uniqueness of the largest centered ball follows from the same constraints: if a ball of radius \(r\) centered at \(b_m+u\) is contained in \(P_m\), then
\[
 \langle a_{ij},u\rangle+r\sqrt{5-1/m}\le1/m\quad(i\ne j).
\]
The average of \(\langle a_{ij},u\rangle\) over ordered pairs is zero, forcing \(r\le r_m\). If equality holds, all the pairings must vanish. They span \(E_m\) (as proved by the isotropic identity below), so \(u=0\).

**2. All vertices and their distance shells.** Kazakov [1, Section 4.1] identifies the vertices as the points \(v_L\) indexed by nonempty proper subsets \(L\subset\{1,\ldots,m\}\). If \(|L|=k\), their coordinates are
\[
 (v_L)_i=\begin{cases}(2m-k)^{-1},&i\in L,\\2(2m-k)^{-1},&i\notin L.\end{cases}
\]
There are \(\binom mk\) points of type \(k\). A direct calculation gives their common squared distance to \(b_m\):
\[
 \|v_L-b_m\|^2=\frac{k(m-k)}{m(2m-k)^2}=:F_m(k).
\]
Since the norm is convex, the largest centered distance on \(P_m\) occurs at a vertex, and therefore the centered ball of squared radius \(\max_kF_m(k)\) contains \(P_m\).

**3. A unique maximizing cardinality.** On the real interval \(0<x<m\) define \(g_m(x)=x(m-x)/(2m-x)^2\). Its derivative is
\[
 g_m'(x)=\frac{m(2m-3x)}{(2m-x)^3}.
\]
Thus \(g_m\) strictly rises to \(2m/3\) and strictly falls thereafter. If \(m=3q\) its unique integer maximizer is \(2q\). If \(m=3q+1\), the only contenders are \(2q,2q+1\), with
\[
 g_m(2q+1)-g_m(2q)=\frac{q(3q+1)}{2(2q+1)^2(4q+1)^2}>0.
\]
If \(m=3q+2\), the only contenders are \(2q+1,2q+2\), with
\[
 g_m(2q+2)-g_m(2q+1)=-\frac{(q+1)(3q+2)}{2(2q+1)^2(4q+3)^2}<0.
\]
This proves the unique integer maximizer and all stated formulas. In particular, every vertex outside the stated orbit lies strictly inside the outer ball.

**4. From two concentric balls to the unique extremal ellipsoids.** The permutation group \(S_m\) acts orthogonally on \(E_m\). Its standard real representation on \(E_m\) is irreducible, and a permutation-invariant symmetric operator on this space is scalar. Uniqueness of the John ellipsoid and Löwner ellipsoid implies that both are permutation-invariant, hence spherical about the sole fixed point \(b_m\). Their radii are exactly those from Steps 1 and 2. One can also avoid the symmetry-uniqueness argument by using the following explicit contact certificates, which independently verify optimality.

The unit outward facet normals are \(u_{ij}=a_{ij}/\sqrt{5-1/m}\). Their sums and second moments satisfy
\[
 \sum_{i\ne j}u_{ij}=0,\qquad
 \sum_{i\ne j}u_{ij}u_{ij}^{\mathsf T}=m\Pi.
\]
Assigning the positive weight \(1/m\) to each contact normal yields \(\sum w_{ij}u_{ij}=0\) and \(\sum w_{ij}u_{ij}u_{ij}^{\mathsf T}=\Pi\), the dimension-\(m-1\) John contact criterion.

For the outer sphere, let \(\mathcal O\) denote the orbit \(\{v_L:|L|=k_m\}\), put \(N=\binom m{k_m}\), and normalize each contact point by \(z_L=(v_L-b_m)/R_m\). The orbit has zero first moment and isotropic second moment:
\[
 \sum_{v_L\in\mathcal O}z_L=0,\qquad
 \sum_{v_L\in\mathcal O}z_Lz_L^{\mathsf T}=\frac{N}{m-1}\Pi.
\]
The positive weights \((m-1)/N\) give the Löwner enclosing-ellipsoid contact criterion. Alternatively, for any possible ball center \(c\in H_m\), averaging the squared distances from \(c\) to the contact orbit yields \(R_m^2+\|c-b_m\|^2\), proving the outer Euclidean ball center is unique. Standard ellipsoid uniqueness then proves both extremal ellipsoids are unique.

## Verification
Run the standalone, standard-library Python program `check.py`. It constructs every vertex and every facet normal with exact rational coordinates for \(3\le m\le10\), verifies all stated radii, all strict contact-orbit inequalities, and both isotropic moment identities. It separately checks the maximizing-index formula through \(m=25\). These **finite tests are not a proof in all dimensions**; the symbolic arguments in Steps 1–4 provide the general result. For \(m=4\), they yield \(r_4^2=1/76\), \(R_4^2=3/100\), and exactly four outer contact vertices among fourteen vertices. The radius ratio obeys \(R_m/r_m\sim\sqrt{5m/8}\) as \(m\to\infty\), directly from the closed formulas.

## Relationship to prior work
Kazakov [1] introduced the all-dimensional barycentric ratio polytope, proved its volume and vertex count, described its facets, and calculated a three-dimensional regular tetrahedron's face-plane distance in Appendix B. Those combinatorial coordinates and the three-dimensional face-distance calculation are **prior results**, not claimed as discoveries here. The contribution here is the exact intrinsic John and Löwner ellipsoids in every dimension, the complete residue-dependent list of contacts of the outer ellipsoid, and explicit positive moment certificates. John's classical ellipsoid criterion [2] supplies the standard characterization but does not evaluate these parameters for this polytope. Other known symmetric polytopes with exact ellipsoids need not have these defining inequalities; their formulas do not imply this result without an explicit affine identification.

## Limitations
No general ellipsoid-radius formula for arbitrary nonregular simplices in the original Euclidean metric is claimed; their relevant affine ellipsoids are instead the images of those here. The source's vertex descriptions and its tetrahedral facet distance already give some ingredients of the result. The contact classification concerns the Euclidean regular-simplex model, with the exact normalization specified above. Prior-literature searching cannot establish absolute publication priority; equivalent unindexed results remain a residual possibility. There has been no independent scientific audit.

## References
[1] Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087v1, 1 June 2026. https://arxiv.org/html/2606.02087v1

[2] Peter M. Gruber and Franz E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (classical contact characterization). https://arxiv.org/abs/1207.7246
