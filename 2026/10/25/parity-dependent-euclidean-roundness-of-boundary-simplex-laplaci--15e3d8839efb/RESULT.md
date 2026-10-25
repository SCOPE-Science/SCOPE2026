# Parity-dependent Euclidean roundness of boundary-simplex Laplacian polytopes

## Finding

Let \(n\ge3\), and let \(P_n\) be the highest-dimensional Laplacian polytope of the boundary of the \((n-1)\)-simplex, in the canonical ambient Euclidean metric of its Laplacian columns. Write \(r_n\) for its **intrinsic Euclidean inradius**, and \(R_n\) for its minimum-enclosing Euclidean-ball radius, with all balls understood inside the affine hull of \(P_n\). Then:

* If \(n=2m\ge4\),
  \[
  r_n=\frac{n}{\sqrt{2m(m-1)}}=\sqrt{\frac{2n}{n-2}},
  \qquad R_n=\sqrt{n(n-2)},
  \qquad\frac{R_n}{r_n}=\frac{n-2}{\sqrt2}.
  \]
  The unique incenter and minimum-enclosing-ball center are both \(\mathbf1\). Every one of the \(m^2\) facets touches the inball and every one of the \(n\) vertices touches the enclosing ball.

* If \(n=2m+1\ge3\), set \(p=m+1\) and \(q=m\). Choose the alternating sign vector \(s\in\{-1,1\}^n\) with \(p\) positive and \(q\) negative entries. Let \(\mathbf1_+\) and \(\mathbf1_-\) be the indicators of the two sign classes. Then
  \[
  r_n=\frac{n}{p\sqrt{n-1}+q\sqrt{n+3}},
  \qquad R_n=n\sqrt{\frac{p-1}{p}}.
  \]
  Both centers are unique. The incenter is
  \[
  c_n^{\mathrm{in}}=\frac{\sqrt{n-1}+\sqrt{n+3}}{p\sqrt{n-1}+q\sqrt{n+3}}
  (q\mathbf1_++p\mathbf1_-),
  \]
  while the minimum-enclosing center is \(c_n^{\mathrm{out}}=(q/p)\mathbf1_++\mathbf1_-\). All \(n\) facets touch the inball. Exactly the \(p\) positive-class vertices touch the minimum enclosing ball; all \(q\) negative-class vertices are strictly inside, with squared-distance deficit \(2n/p\).

Consequently, along the even integers \(r_n\to\sqrt2\) and \(R_n/r_n\sim n/\sqrt2\), but along the odd integers \(\sqrt n\,r_n\to1\) and \(R_n/r_n\sim n^{3/2}\). This sharp parity separation occurs despite all edge lengths lying between \(\sqrt{2n(n-2)}\) and \(n\sqrt2\), whose ratio tends to one. In particular, the odd-dimensional simplices are asymptotically nearly equilateral in their **pairwise edge lengths**, yet much thinner than an equal-edge regular simplex of comparable diameter.

## Assumptions and scope

For \(n\ge3\), take the boundary complex \(\Delta_n=\partial(\sigma_{n-1})\), with \(n\) facets carrying the canonical increasing-vertex orientations and ordered by omitted vertex. Its top-dimensional down-Laplacian is \(L_n=\partial_{n-2}^{\mathsf T}\partial_{n-2}\), and \(P_n=\operatorname{conv}\{L_ne_i:1\le i\le n\}\subset\mathbb R^n\). Reversing compatible orientation or reversing the facet order conjugates the construction by an orthogonal signed/permutation matrix, hence leaves the radii unchanged. We select a labeling in which \(L_n=nI-ss^{\mathsf T}\) with alternating \(s_i=(-1)^{i-1}\). All distances are ordinary Euclidean distances in the *original column realization*, **not** in a generally non-isometric unimodular projection of it.

The inradius maximizes the radius of a closed ball contained in \(P_n\) in its own affine space. The enclosing radius minimizes the radius of a ball in that same space covering \(P_n\). No dimension-independent Euclidean normalization of the Laplacian columns is applied.

## Proof

**1. Canonical matrix and edge geometry.** Two distinct oriented top facets share one codimension-one face; the orientation signs yield the Gram matrix \(L_n=nI-ss^{\mathsf T}\), with diagonal \(n-1\) and off-diagonal entries \(-s_i s_j\). Thus \(L_n\) has rank \(n-1\), image \(H=s^\perp\), and columns \(v_i=ne_i-s_i s\). Since \(L_n^2=nL_n\), each column has squared norm \(n(n-1)\). For \(i\ne j\),
\[
\|v_i-v_j\|^2=n^2\left(2-\frac{(s_i-s_j)^2}{n}\right)
=\begin{cases}2n^2,&s_i=s_j,\\2n(n-2),&s_i\ne s_j.\end{cases}
\]
This also proves the edge-length assertion for all \(n\ge3\).

**2. Even parity: orthogonal free sum.** Suppose \(n=2m\), so \(s\cdot\mathbf1=0\). The affine hull is \(\mathbf1+E\), where \(E=\{x:x\cdot\mathbf1=x\cdot s=0\}\). Split \(E=E_+\oplus E_-\) orthogonally, with \(E_\pm\) the zero-sum spaces on the corresponding classes, each of dimension \(m-1\). Subtracting \(\mathbf1\) gives the vertices
\[
v_i-\mathbf1=n(e_i-\mathbf1_+/m)\quad(i\in+),\qquad
v_j-\mathbf1=n(e_j-\mathbf1_-/m)\quad(j\in-).
\]
Each class is a centered regular \((m-1)\)-simplex with circumradius \(a=n\sqrt{(m-1)/m}\) and inradius \(\rho=a/(m-1)=n/\sqrt{m(m-1)}\). Their convex hull is the orthogonal free sum \(K=\operatorname{conv}(A\cup B)\). It has \(m^2\) facets, the joins of opposite-vertex facets from \(A\) and \(B\), and polar \(K^\circ=A^\circ\times B^\circ\) in \(E_+\oplus E_-\). The maximum distance of a point of \(K^\circ\) from the origin is \(\sqrt2/\rho\). Hence the largest origin-centered ball in \(K\) has radius \(\rho/\sqrt2\). Averaging any feasible ball center over the orthogonal symmetry group of the two regular simplices and their interchange gives the origin without reducing its radius, so this is the global inradius. All normalized facet normals have sum zero and span \(E\); because all facets are tangent, no nonzero displacement can preserve that inradius, establishing uniqueness.

The vertex barycenter of \(K\) is zero, and all vertices have norm \(a\). For any prospective enclosing center \(c\), averaging squared distances over vertices gives \(a^2+\|c\|^2\), proving both optimality and uniqueness of the origin as enclosing center. Translating back gives the even formulas, contacts and centers.

**3. Odd parity: barycentric facets.** Suppose \(n=2m+1\), choose \(s\) with \(\mathbf1\cdot s=1\), and put \(p=m+1\), \(q=m\). The affine hull is all of \(H=s^\perp\) and the \(n\) columns form a nondegenerate \((n-1)\)-simplex: a linear dependence is a multiple of \(s\), but its coefficients do not sum to zero. For every \(x\in H\), its unique barycentric coordinates are
\[
\lambda_i(x)=\frac{x_i}{n}+s_i\left(1-\frac{\mathbf1\cdot x}{n}\right),\qquad
\sum_i\lambda_i(x)=1,
\]
so \(P_n=\{x\in H:\lambda_i(x)\ge0\ \forall i\}\). The intrinsic gradient is \(\nabla_H\lambda_i=(e_i-s_i\mathbf1)/n\), already orthogonal to \(s\); its norm is \(g_+=\sqrt{n-1}/n\) for \(s_i=+1\) and \(g_-=\sqrt{n+3}/n\) for \(s_i=-1\). A ball of radius \(r\) centered at \(c\) lies in the simplex exactly when \(\lambda_i(c)\ge r g_i\) for each \(i\). Summing gives \(1\ge r(pg_++qg_-)\), with equality attained by the unique barycentric choice \(\lambda_i(c)=g_i/(pg_++qg_-)\). This proves the sharp inradius, uniqueness, all-facet tangency and the displayed incenter after multiplying by \(L_n\).

**4. Odd parity: the enclosing ball screens one vertex class.** The barycenter of the \(p\) positive-class vertices is
\[
 c=\frac1p\sum_{s_i=1}v_i=\frac qp\mathbf1_++\mathbf1_-\in H.
\]
These vertices form a regular \((p-1)\)-simplex, and each is at distance \(n\sqrt{(p-1)/p}\) from \(c\). Any enclosing ball for \(P_n\) must cover these \(p\) vertices. Averaging their squared distances proves its radius is at least this value, with equality possible only at \(c\). For every negative-class vertex \(v_j\), use \(c\cdot v_j=nc_j=n\), whereas for a positive-class vertex \(c\cdot v_i=nq/p\), and all columns have the same squared norm. Consequently \(\|v_j-c\|^2=R_n^2-2n/p<R_n^2\). Thus the ball centered at \(c\) covers the whole polytope and is uniquely optimal.

**5. Asymptotic parity gap.** Substitute \(m=n/2\) on even dimensions; on odd dimensions, \(p=(n+1)/2\), \(q=(n-1)/2\). The stated expansions follow immediately from the exact expressions. In the odd family, the ratio of the longest and shortest edge lengths is \((1-2/n)^{-1/2}=1+O(1/n)\), yet its inradius is \(\Theta(n^{-1/2})\), rather than the order-one inradius of a regular \((n-1)\)-simplex with edge length \(n\sqrt2\). This is a dimension-dependent instability of edge-length near-regularity.

## Verification

The accompanying `check_metric.py` independently constructs the oriented simplicial boundary matrix (without entering the formula for its Gram entries), checks \(\partial^{\mathsf T}\partial=nI-ss^{\mathsf T}\), computes the convex hull in an orthonormal affine-hull basis, solves a linear program for its largest inscribed ball, and compares its radius with the exact theorem. It also compares all vertex distances from the proposed enclosing center and all facet distances from the proposed incenter. Tests passed for every \(n=3,\ldots,10\); the checks provide finite-dimensional corroboration and are **not** substitutes for the proof for arbitrary \(n\). Execute with Python, NumPy and SciPy: `python check_metric.py`.

## Relationship to prior work

Juhnke-Kubitzke and Köhne, *Laplacian polytopes of simplicial complexes* (arXiv:2301.11602, first submitted 2023-01-27), give the signed top-Laplacian matrix, parity-dependent combinatorial type, unimodular triangulations, lattice volume and \(h^*\)-properties. Their full-text discussions of the boundary-simplex case do not state the canonical Euclidean in- and enclosing-radius formulas or the opposite contact regimes here. A unimodular coordinate equivalence does not preserve the Euclidean radii. Braun and Meyer, *Laplacian Simplices* (arXiv:1706.07085), study graph-Laplacian simplices and Ehrhart-type properties; a graph Laplacian is a different operator from the top down-Laplacian used here. Indexed geometric results on graph Laplacian simplices and unrelated parity transitions likewise do not imply these explicit formulas for the higher-dimensional simplicial-complex family.

## Limitations

The classification concerns only the canonical top-dimensional down-Laplacian of the boundary of a simplex in its original Euclidean embedding; it does not assert corresponding metric formulas for arbitrary simplicial complexes, all Laplacian levels, other lattice-equivalent embeddings, or general two-distance simplices. The bibliographic comparison is bounded by accessible primary papers and indexed mathematical records; it cannot establish absolute novelty. These are direct analytic formulas with finite numerical checks, not independently validated results.

## References

1. M. Juhnke-Kubitzke and D. Köhne, *Laplacian polytopes of simplicial complexes*, arXiv:2301.11602 (submitted 2023-01-27), Sections 3–7. https://arxiv.org/abs/2301.11602
2. B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085 (submitted 2017-06-21), Sections 1–3. https://arxiv.org/abs/1706.07085
