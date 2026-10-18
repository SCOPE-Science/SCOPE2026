# Parity-split Euclidean balls and canonical ellipsoids of simplex-boundary Laplacian polytopes

## Finding

The canonical highest-dimensional Laplacian polytope of the boundary of a simplex exhibits two distinct Euclidean regimes, determined solely by parity. All distances and ellipsoids below are measured in the **original ambient coordinate Euclidean metric**, rather than in an arbitrary lattice-coordinate identification.

For each integer \(m\ge3\), set \(s_i=(-1)^{i-1}\), let \(s=(s_1,\ldots,s_m)\), and define
\[
L_m=mI_m-ss^{\mathsf T},\qquad P_m=\operatorname{conv}\{L_me_i:1\le i\le m\}\subset\mathbb R^m.
\]
This is the top-Laplacian polytope of the oriented boundary of the \((m-1)\)-simplex, with the standard increasing-order orientation on its \((m-2)\)-faces.

**Even \(m=2k\ge4\).** The polytope has intrinsic dimension \(m-2\), with common unique inball and minimum enclosing sphere centered at \(\mathbf1\):
\[
r_{\mathrm{in}}=\sqrt{\frac{2m}{m-2}},\qquad R_{\mathrm{out}}=\sqrt{m(m-2)}.
\]
There are exactly \(k^2\) facets, and every facet touches the inball; all \(m\) vertices touch the enclosing sphere. The John and Löwner ellipsoids are precisely these two balls. After translation by \(-\mathbf1\), the polytope is the orthogonal free sum of two regular \((k-1)\)-simplices.

**Odd \(m=2k+1\ge3\).** Put \(\epsilon=\sum_i s_i\in\{-1,1\}\), \(A=\{i:s_i=\epsilon\}\), and \(B=\{i:s_i=-\epsilon\}\), with \(|A|=(m+1)/2\) and \(|B|=(m-1)/2\). Here \(P_m\) is an \((m-1)\)-simplex in \(s^\perp\). Its Euclidean inradius and minimum enclosing radius are
\[
r_{\mathrm{in}}=\frac{2m}{(m+1)\sqrt{m-1}+(m-1)\sqrt{m+3}},\qquad
R_{\mathrm{out}}=m\sqrt{\frac{m-1}{m+1}}.
\]
Every facet touches the unique maximum inscribed ball. Write \(v_i=L_me_i\). Its unique center is \(c_{\mathrm{in}}=\sum_i\lambda_i v_i\), with
\[
\lambda_i=\begin{cases}r_{\mathrm{in}}\sqrt{m-1}/m,&i\in A,\\ r_{\mathrm{in}}\sqrt{m+3}/m,&i\in B.\end{cases}
\]
The unique minimum enclosing sphere instead has center \(c_{\mathrm{out}}=\frac2{m+1}\sum_{i\in A}v_i\). **Only the \((m+1)/2\) vertices from \(A\) touch** this sphere; each vertex in \(B\) has exact squared-distance clearance \(4m/(m+1)\). Thus an entire parity class of vertices is strictly screened.

The odd polytope's unique John and Löwner ellipsoids share the distinct common center \(c_J=\mathbf1-(\epsilon/m)s\), with semiaxes along \(\mathbb R c_J\) and its orthogonal complement in \(s^\perp\):

| Ellipsoid | Axis along \(c_J\) (multiplicity one) | Transverse axes (multiplicity \(m-2\)) |
|---|---|---|
| John | \(1/\sqrt{m(m-1)}\) | \(\sqrt{m/(m-1)}\) |
| Löwner | \(\sqrt{(m-1)/m}\) | \(\sqrt{m(m-1)}\) |

These ellipsoid axes have ratio \(m\) for both extremal ellipsoids. In particular, the inball and minimum-enclosing sphere centers are different from the shared John–Löwner center, whereas for even \(m\) all four centers coincide.

## Assumptions and scope

The simplex has vertices numbered \(1,\ldots,m\), its oriented facets are formed by deleting one vertex in the natural order, and the top Laplacian is the Gram matrix of the codimension-one boundary operator. No scaling or change of the original Euclidean coordinate metric is permitted. The minimum-volume enclosing ellipsoid and maximum-volume inscribed ellipsoid are both taken in the affine hull of the polytope. The \(m=3\) case is included; the even case begins at \(m=4\), so both orthogonal simplex factors have positive dimension.

## Proof

**1. Boundary Gram matrix and parity.** Let \(B\) be the oriented boundary incidence matrix from \((m-2)\)-faces of the simplex boundary to \((m-3)\)-faces. Each column has \(m-1\) entries of magnitude one; the off-diagonal Gram entries have alternating sign. The resulting matrix is exactly \(B^{\mathsf T}B=mI-ss^{\mathsf T}\), which has rank \(m-1\). Each vertex \(v_i\) satisfies \(s\cdot v_i=0\). The unique linear dependence among the columns is \(\sum_i s_iv_i=0\). If \(m\) is even, \(\sum_i s_i=0\), so this is an affine dependence and the affine dimension is \(m-2\). If \(m\) is odd, \(\sum_i s_i=\epsilon\ne0\), so the columns are affinely independent and the polytope is a simplex of dimension \(m-1\).

**2. Even case: orthogonal simplices and all facets.** Set \(m=2k\) and partition the indices into \(A=\{s_i=1\}\) and \(B=\{s_i=-1\}\), each of size \(k\). Their barycentric centers agree at \(\mathbf1\), since \(\sum_{i\in A}v_i/k=\sum_{j\in B}v_j/k=\mathbf1\). Translation gives
\[
w_i=v_i-\mathbf1=m(e_i-\mathbf1_A/k)\quad(i\in A),\qquad
w_j=m(e_j-\mathbf1_B/k)\quad(j\in B),
\]
where \(\mathbf1_A\) and \(\mathbf1_B\) are block indicator vectors. These form two regular simplices in mutually orthogonal subspaces. Every translated vertex has squared norm \(m(m-2)\). The convex hull of two simplices whose relative interiors contain zero in orthogonal complementary subspaces is their free sum. Its facets are exactly the joins of one facet of each simplex, hence indexed by \((i,j)\in A\times B\). Define
\[
\nu_{ij}=-\frac{k-1}{m(m-2)}(w_i+w_j).
\]
Direct inner products within each regular simplex give \(\langle\nu_{ij},w_t\rangle=1\) for every \(t\notin\{i,j\}\), and \(\langle\nu_{ij},w_t\rangle<1\) for \(t\in\{i,j\}\). Moreover
\[
\|\nu_{ij}\|^2=\frac{m-2}{2m}.
\]
Thus the ball of stated radius centered at zero is contained in every facet halfspace and contacts all facets. Their outward unit normals sum to zero, so summing the ball inequalities shows no larger ball exists. The normals span the affine direction space; equality forces the center to be zero, proving uniqueness. Every vertex lies on the radius-\(\sqrt{m(m-2)}\) sphere, while its center is a convex combination of all vertices with positive coefficients; averaging squared distances proves it is the unique minimum enclosing sphere. The group permuting indices independently inside the two blocks and interchanging blocks preserves the Euclidean polytope. Its action is irreducible on the full affine direction space: independent block permutations force a commuting self-adjoint operator to be scalar on each irreducible standard representation, and block interchange forces the two scalars to coincide. Uniqueness of John and Löwner ellipsoids therefore forces spherical shapes and fixed center zero; their radii are the inradius and enclosing radius already established.

**3. Odd case: barycentric gradients give the exact inball.** Since \(m\) is odd, \(s\cdot\mathbf1=\epsilon\), and the vertex barycenter equals
\[
c_J=\frac1m\sum_i v_i=\mathbf1-\frac\epsilon m s.
\]
On the affine hull \(s^\perp\), the \(i\)-th barycentric coordinate function of any point \(y\) is
\[
\lambda_i(y)=\frac1m+\langle g_i,y-c_J\rangle,\qquad
 g_i=\frac1m(e_i-\epsilon s_i\mathbf1).
\]
To verify this, \(g_i\perp s\), and for each vertex \(v_j\) a direct calculation gives \(1/m+\langle g_i,v_j-c_J\rangle=\delta_{ij}\). Thus the facet opposite \(v_i\) is \(\lambda_i(y)=0\), and the exact Euclidean facet-normal lengths are
\[
\|g_i\|=\begin{cases}\sqrt{m-1}/m,&i\in A,\\\sqrt{m+3}/m,&i\in B.\end{cases}
\]
A closed Euclidean ball \(B(c,r)\) in the affine hull lies in the simplex if and only if \(\lambda_i(c)\ge r\|g_i\|\) for all indices. Summing and using \(\sum_i\lambda_i(c)=1\) gives \(r\le1/\sum_i\|g_i\|\), precisely the claimed radius. At equality every inequality must be tight, uniquely determining the \(\lambda_i(c)\), and every facet is tangent. In particular, \(c_{\mathrm{in}}=\theta c_J\) with \(\theta=(r_{\mathrm{in}}/2)(\sqrt{m-1}+\sqrt{m+3})>1\). This follows by evaluating the constant barycentric weights on the two sign blocks.

**4. Odd case: a minority-screening minimum sphere.** There are \(a=(m+1)/2\) majority vertices, and for \(i\in A\) their coordinates are \(v_i=m e_i-s_i s=m e_i-\epsilon s\). Their average is \(c_{\mathrm{out}}=\frac2{m+1}\sum_{i\in A}v_i=\frac m{m+1}c_J\). They form a regular \((a-1)\)-simplex with side length \(m\sqrt2\), whose squared circumradius is \(m^2(a-1)/a=m^2(m-1)/(m+1)\). Its center is the average of these vertices, so that sphere is the unique minimum enclosing sphere for this majority subset: for any other center, the average squared distance increases by the squared displacement. For each minority vertex \(v_j\), direct substitution into the Euclidean distance gives
\[
R_{\mathrm{out}}^2-\|v_j-c_{\mathrm{out}}\|^2=\frac{4m}{m+1}>0.
\]
Thus the same sphere encloses every vertex, proving global optimality and uniqueness, with precisely the stated contact set.

**5. Odd case: canonical ellipsoid axes.** Let \(H=\mathbf1^\perp\), the standard \((m-1)\)-simplex direction space in the source coordinate system. The restriction \(L_m:H\longrightarrow s^\perp\) is a linear isomorphism and maps the standard coordinate simplex to \(P_m\). On \(H\cap s^\perp\) (dimension \(m-2\)), it multiplies vectors by \(m\). On the complementary one-dimensional line spanned by \(s_H=s-(\epsilon/m)\mathbf1\), it sends \(s_H\) to \(-\epsilon c_J\), which has the same norm as \(s_H\). Hence its singular values are \(1\) (one copy) and \(m\) (\(m-2\) copies). The ordinary regular coordinate simplex has the John ball of radius \(1/\sqrt{m(m-1)}\) and Löwner ball of radius \(\sqrt{(m-1)/m}\), both centered at \(\mathbf1/m\). The affine-equivariance and uniqueness of these volume-extremal ellipsoids, combined with the singular values just computed, give the stated axes and common center \(c_J\). This also proves that all claimed axes are principal and exhaust the affine hull.

## Verification

A standalone Python standard-library checker, `checker.py`, independently constructs the oriented top boundary incidence matrix and verifies \(B^{\mathsf T}B=L_m\) with exact rational arithmetic for every \(3\le m\le17\). In even dimensions it checks every predicted facet plane, all vertex contacts, and exact inradius and outer-radius squares. In odd dimensions it checks barycentric gradients, the exact majority circumradius, the strictly positive minority clearance, and the incenter identities. The numerical incenter identities use finite-precision square roots; other checks are rational exact. The checker is finite corroboration, **not** an exhaustive proof for all dimensions; that is supplied above.

To replay from this package, run `python3 checker.py` with Python 3 and no dependencies. The checker reports `PASS` if every test succeeds.

## Relationship to prior work

Juhnke-Kubitzke and Köhne introduced these Laplacian polytopes and determined their defining Laplacian matrix, parity-dependent combinatorial types, facets, triangulations, and Ehrhart structure. Their arXiv preprint was first publicly posted January 27, 2023. The present classification fixes the original Euclidean metric and proves exact inball, enclosing-sphere, complete contact, and John–Löwner data, rather than new combinatorial or Ehrhart results. General results about graph Laplacian simplices do not imply the non-graph top-boundary geometry, and affine combinatorial identification with cyclic polytopes does not preserve Euclidean distances. The odd-case minimum enclosing sphere is also distinct from the Löwner ellipsoid; conflating them would erase the strict vertex-screening effect.

## Limitations

No claim is made about Laplacian polytopes of arbitrary simplicial complexes, nor about metric invariance under lattice-unimodular changes of coordinates. Literature coverage does not rule out a differently phrased earlier metric theorem; a relevant author thesis was not accessible in full during comparison. The exact universal statements are analytical, and the finite checker is auxiliary. Independent validation has not yet been performed.

## References

- Martina Juhnke-Kubitzke and Daniel Köhne, *Laplacian polytopes of simplicial complexes*, arXiv:2301.11602, first publicly posted 2023-01-27; especially the definition of the highest Laplacian polytope and its simplex-boundary structure, Sections 2–5. https://arxiv.org/abs/2301.11602
- Benjamin Braun and Robert Meyer, *Laplacian simplices*, 2017. (Graph Laplacian simplex background; not a source for the claimed simplex-boundary Euclidean classification.)
