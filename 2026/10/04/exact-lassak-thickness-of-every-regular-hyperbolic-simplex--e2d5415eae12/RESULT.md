# Exact Lassak thickness of every regular hyperbolic simplex

## Finding

Let \(S^d_\ell\subset\mathbb H^d\), \(d\ge2\), be a regular hyperbolic \(d\)-simplex of edge length \(\ell>0\). Put
\[
q=\cosh\ell,
\qquad
k=\left\lceil\frac d2\right\rceil.
\]
For Lassak's hyperbolic width, the thickness of \(S^d_\ell\) is
\[
\boxed{
\Delta(S^d_\ell)
=
\operatorname{arsinh}
\sqrt{
\frac{(q-1)(dq+1)}{k((d-k)q+1)}
}.
}
\]

The minimizing supports are completely classified. A supporting hyperplane minimizes the width if and only if it contains exactly \(d+1-k\) vertices of the simplex, hence the face they span of dimension
\[
d-k=\left\lfloor\frac d2\right\rfloor,
\]
and the other \(k\) vertices all lie at the same maximal distance from that support. Therefore the number of minimizing supporting hyperplanes is
\[
\binom{d+1}{k}.
\]

For a regular hyperbolic tetrahedron this becomes
\[
\Delta(S^3_\ell)
=
\operatorname{arsinh}
\sqrt{
\frac{(\cosh\ell-1)(3\cosh\ell+1)}{2(\cosh\ell+1)}
},
\]
and the six minimizers are precisely the supporting hyperplanes containing an edge.

## Assumptions and scope

Work in the hyperboloid model with Lorentz bilinear form \(\langle\cdot,\cdot\rangle\) of signature \((- +\cdots+)\):
\[
\mathbb H^d=\{x:\langle x,x\rangle=-1,\ x_0>0\}.
\]
A geodesic hyperplane has the form
\[
H_n=\{x\in\mathbb H^d:\langle x,n\rangle=0\},
\qquad
\langle n,n\rangle=1.
\]
Choose the sign of \(n\) so the simplex lies in
\[
\langle x,n\rangle\ge0.
\]
Then
\[
\sinh d(x,H_n)=\langle x,n\rangle.
\]

Lassak's width determined by a supporting hyperplane is the maximum hyperbolic distance of a point of the body from that hyperplane; his thickness is the minimum of this quantity over all supporting hyperplanes.

Let the vertices be \(v_0,\ldots,v_d\). Regularity with edge length \(\ell\) means
\[
\langle v_i,v_i\rangle=-1,
\qquad
\langle v_i,v_j\rangle=-q
\quad(i\ne j),
\qquad q=\cosh\ell>1.
\]

## Proof

For a supporting hyperplane \(H_n\), define
\[
s_i=\langle v_i,n\rangle\ge0.
\]
At least one \(s_i\) is zero because the hyperplane supports the simplex.

First, the farthest point from \(H_n\) is always a vertex. Indeed, every point of the hyperbolic simplex can be written projectively as
\[
x=\frac{y}{\sqrt{-\langle y,y\rangle}},
\qquad
y=\sum_{i=0}^d\lambda_i v_i,
\qquad\lambda_i\ge0,
\]
with not all \(\lambda_i\) zero. Since
\[
-\langle y,y\rangle
=
\sum_i\lambda_i^2+2q\sum_{i<j}\lambda_i\lambda_j
\ge
\left(\sum_i\lambda_i\right)^2,
\]
we obtain
\[
\langle x,n\rangle
=
\frac{\sum_i\lambda_i s_i}{\sqrt{-\langle y,y\rangle}}
\le
\max_i s_i.
\]
A vertex attaining \(\max_i s_i\) gives equality. Hence if
\[
M=\max_i s_i,
\]
then the width determined by \(H_n\) is
\[
\operatorname{arsinh} M.
\]

The vertex Gram matrix is
\[
G=(q-1)I-qJ,
\]
where \(J\) is the all-ones matrix. Its inverse is
\[
G^{-1}
=
\frac1{q-1}I
-
\frac q{(q-1)(dq+1)}J.
\]
Because the \(v_i\) form a basis of the ambient Lorentz space, write
\[
n=\sum_i\alpha_i v_i.
\]
Then \(s=G\alpha\), and the normalization \(\langle n,n\rangle=1\) gives
\[
1=s^TG^{-1}s
=
\frac1{q-1}
\left(
\sum_i s_i^2
-
\frac q{dq+1}
\left(\sum_i s_i\right)^2
\right).
\]

Put
\[
t_i=\frac{s_i}{M},
\qquad
0\le t_i\le1,
\qquad
\min_i t_i=0,
\]
and set
\[
c=\frac q{dq+1}.
\]
Then
\[
M^2=\frac{q-1}{F(t)},
\qquad
F(t)=\sum_i t_i^2-c\left(\sum_i t_i\right)^2.
\]
Thus minimizing the width is equivalent to maximizing \(F\) on the union of the coordinate faces of the cube \([0,1]^{d+1}\) on which at least one coordinate is zero.

Fix one zero coordinate. On that \(d\)-dimensional face, the Hessian of \(F\) is
\[
2(I-cJ).
\]
Its eigenvalues are \(2\) with multiplicity \(d-1\) and
\[
2(1-dc)=\frac2{dq+1}>0.
\]
Hence \(F\) is strictly convex on every such face. Its maximum is therefore attained at a cube vertex, and strict convexity excludes a nonvertex maximizer.

Suppose exactly \(k\) coordinates of \(t\) equal \(1\), the rest being zero. Then
\[
F_k
=
k-ck^2
=
\frac{k((d-k)q+1)}{dq+1}.
\]
The consecutive difference is
\[
F_{k+1}-F_k
=
\frac{(d-2k-1)q+1}{dq+1}.
\]
Since \(q>1\), these differences change sign exactly at
\[
k=\left\lceil\frac d2\right\rceil.
\]
Thus this \(k\) is the unique maximizing cardinality. Consequently
\[
M^2
=
\frac{(q-1)(dq+1)}{k((d-k)q+1)},
\]
which gives the displayed thickness formula.

The strict-convexity step also gives the equality classification. At a minimizing support, each normalized \(t_i\) is either \(0\) or \(1\), with exactly \(k\) ones. Hence exactly \(d+1-k\) vertices lie on the supporting hyperplane and the remaining \(k\) vertices have the common maximum distance. Conversely, any such zero-one pattern determines through \(G^{-1}\) a unit spacelike normal with nonnegative vertex pairings, so it defines a supporting hyperplane with the stated width. Choosing the \(k\) off-support vertices gives exactly
\[
\binom{d+1}{k}
\]
minimizers.

For \(d=3\), \(k=2\), so the support face is an edge and the formula reduces to the tetrahedral expression stated above.

## Verification

The proof is exact and does not rely on finite enumeration.

The packaged `verify.py` symbolically checks the inverse of the regular-simplex Lorentz Gram matrix, the objective formula, the consecutive-difference identity, and the positive Hessian eigenvalue on every support face for dimensions \(2\) through \(10\). It also performs exact-rational checks of the discrete maximizer for several values of \(q>1\), and symbolically verifies that the three-dimensional formula agrees with the edge-supported tetrahedral width computed by Lassak after substituting \(\ell=2x\).

The replay output is:

`VERIFY_OK regular hyperbolic simplex Lassak thickness`

The finite-dimensional replay is a consistency check only. The all-dimensional theorem is established by the algebraic identities and sign analysis in the proof.

## Relationship to prior work

Lassak introduced the width used here and proved that the width determined by a supporting hyperplane equals the maximum distance of a point of the body from that hyperplane. He defined the thickness as the minimum over supports. For a regular hyperbolic simplex he computed the width determined by a facet-supporting hyperplane. In dimension three he then exhibited a narrower edge-supporting hyperplane and used it to show that every regular hyperbolic tetrahedron is not reduced.

The present result closes the optimization step left implicit there: the displayed edge-supported tetrahedral width is the global thickness, the six edge supports are all minimizers, and the same optimization gives a parity-dependent face dimension and a closed formula in every dimension.

Dekster's earlier equidistant thickness is a different hyperbolic width notion: it encloses a set between two hypersurfaces equidistant from one hyperplane and was used to obtain lower estimates for simplices with edge lengths in a range. It therefore does not imply a statement about Lassak's later support-hyperplane width.

Later work on Pál's isominwidth problem in hyperbolic space uses Lassak width but studies volume minimization and horocyclic convexity; it does not give a regular-simplex thickness formula or minimizing-support classification.

## Limitations

The theorem concerns Lassak's support-hyperplane width. Hyperbolic geometry has several inequivalent notions of width, so the formula must not be transferred to Santaló-type or equidistant-thickness definitions without a separate argument.

The simplex is assumed regular and compact, with finite edge length \(\ell>0\). Ideal or nonregular simplices are not covered.

The literature comparison found no statement of this all-dimensional optimization or its minimizer classification, but differently phrased or poorly indexed prior observations remain a residual originality risk.

## References

M. Lassak, “Width of Convex Bodies in Hyperbolic Space,” arXiv:2306.04412, first submitted 2023-06-07; Results in Mathematics 79 (2024), article 111, DOI 10.1007/s00025-023-02102-2.

B. V. Dekster, “Equidistant Thickness in a Space of Constant Curvature,” JP Journal of Geometry and Topology 1 (2001), 1–36.

B. V. Dekster, “Thickness of a Simplex Whose Edge Lengths Fall Within a Prescribed Range,” Geometriae Dedicata 68 (1997), 49–59.

K. J. Böröczky, A. Freyer, and Á. Sagmeister, “Pál’s Isominwidth Problem in the Hyperbolic Space,” Journal of Geometric Analysis 36 (2026), article 76.
