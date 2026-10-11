# Exact radial second moments of regular nested permutohedra
## Finding
Let
\[
d\ge2,
\]
and let
\[
M,N>0
\]
be an appropriate parameter pair in the sense of Castillo--Liu for the regular nested permutohedron
\[
\Pi_d^2(M,N).
\]
The source realization has
\[
d!(d+1)!
\]
vertices
\[
v_{\pi,\tau},
\qquad
(\pi,\tau)\in\mathfrak S_{d+1}\times\mathfrak S_d.
\]

Put
\[
c=\frac{M(d+2)}2\mathbf1.
\tag{1}
\]
For
\[
\tau=(\tau_1,\ldots,\tau_d)\in\mathfrak S_d,
\]
define its endpoint-zero quadratic roughness
\[
\mathcal E(\tau)
=
\tau_1^2
+
\sum_{i=1}^{d-1}
(\tau_i-\tau_{i+1})^2
+
\tau_d^2.
\tag{2}
\]
Then
\[
\boxed{
\|v_{\pi,\tau}-c\|^2
=
\frac{M^2d(d+1)(d+2)}{12}
+
MN\,d(d+1)
+
N^2\mathcal E(\tau).
}
\tag{3}
\]

Thus the outer coordinate permutation \(\pi\) is completely invisible to centered Euclidean radius. All radial nonuniformity is carried by the inner permutation \(\tau\).

If the vertices are sampled uniformly, their mean squared radius is
\[
\boxed{
\overline{R^2}
=
\frac{M^2d(d+1)(d+2)}{12}
+
MN\,d(d+1)
+
\frac{N^2(d+1)^2(d+2)}6.
}
\tag{4}
\]
Their squared-radius variance is
\[
\boxed{
\operatorname{Var}(R^2)
=
N^4
\frac{
(d-2)(d+1)^2(d+2)(5d+11)
}{180}.
}
\tag{5}
\]

The centered vertex covariance matrix is exactly
\[
\boxed{
\frac1{d!(d+1)!}
\sum_{\pi,\tau}
(v_{\pi,\tau}-c)(v_{\pi,\tau}-c)^{\mathsf T}
=
\frac{\overline{R^2}}{d}
\left(
I-\frac1{d+1}J
\right).
}
\tag{6}
\]
Hence the centered vertex multiset is a tight frame for
\[
\mathbf1^\perp.
\]

There is a sharp low-dimensional transition. For
\[
d=2,
\]
equation (5) vanishes, so all twelve vertices are cospherical about \(c\). For every
\[
d\ge3,
\]
equation (5) is strictly positive, so the regular nested permutohedron is not vertex-cospherical for any appropriate
\[
M,N>0.
\tag{7}
\]

Moreover, subtracting (4) from (3) gives
\[
\|v_{\pi,\tau}-c\|^2-\overline{R^2}
=
N^2
\left(
\mathcal E(\tau)
-
\frac{(d+1)^2(d+2)}6
\right).
\tag{8}
\]
Thus \(M\) changes the common radial baseline but not the radial fluctuation pattern, while \(N\) scales every squared-radius fluctuation by \(N^2\).

## Assumptions and scope
The polytope is the regular nested permutohedron of Castillo--Liu with
\[
\alpha=(1,2,\ldots,d+1),
\qquad
\beta=(1,2,\ldots,d),
\]
and an **appropriate** positive parameter pair \((M,N)\), so that all displayed indexed points are vertices and the nested braid fan is the normal fan.

The metric is the ordinary Euclidean metric inherited from the ambient coordinate space. The polytope lies in the affine hyperplane
\[
\sum_i x_i
=
M\sum_{i=1}^{d+1} i.
\]

The theorem is a statement about the complete vertex multiset and its Euclidean second moments. It does not claim the circumradius, inradius, or John ellipsoid.

## Proof
The source gives the regular nested-permutohedron vertices in the rearranged form
\[
v_{\pi,\tau}
=
\sum_{i=1}^{d+1}
\left(
Mi
+
N(\tau_{i-1}-\tau_i)
\right)
e_{\pi^{-1}(i)},
\tag{9}
\]
where
\[
\tau_0=\tau_{d+1}=0.
\]
The \(N\)-term telescopes, so every vertex has coordinate sum
\[
M\frac{(d+1)(d+2)}2.
\]
The full coordinate-permutation symmetry therefore has the unique fixed point in the affine hull
\[
c=\frac{M(d+2)}2\mathbf1,
\]
which is also the vertex centroid.

Set
\[
a_i=i-\frac{d+2}{2},
\qquad
b_i=\tau_{i-1}-\tau_i.
\]
Since \(\pi\) only permutes coordinates,
\[
\|v_{\pi,\tau}-c\|^2
=
\sum_{i=1}^{d+1}
(Ma_i+Nb_i)^2.
\tag{10}
\]
The three sums in (10) are
\[
\sum_{i=1}^{d+1}a_i^2
=
\frac{d(d+1)(d+2)}{12},
\tag{11}
\]
\[
\sum_{i=1}^{d+1}b_i^2
=
\mathcal E(\tau),
\tag{12}
\]
and, by summation by parts,
\[
\sum_{i=1}^{d+1}a_i b_i
=
\sum_{j=1}^{d}\tau_j
=
\frac{d(d+1)}2.
\tag{13}
\]
Substitution into (10) proves (3).

It remains to compute the first two moments of \(\mathcal E\) for a uniformly random permutation
\[
(X_1,\ldots,X_d)
\]
of \(\{1,\ldots,d\}\). Put
\[
S_r=\sum_{j=1}^{d}j^r
\]
and
\[
P=\sum_{i=1}^{d-1}X_iX_{i+1}.
\]
Because the multiset of the \(X_i\) is fixed,
\[
\mathcal E
=
2S_2-2P.
\tag{14}
\]

For two distinct sampled entries,
\[
\mathbb E[X_1X_2]
=
\frac{S_1^2-S_2}{d(d-1)}.
\]
Therefore
\[
\mathbb E[P]
=
\frac{S_1^2-S_2}{d}
=
\frac{(d-1)(d+1)(3d+2)}{12}.
\tag{15}
\]
Using
\[
S_2=\frac{d(d+1)(2d+1)}6
\]
in (14)--(15) gives
\[
\boxed{
\mathbb E[\mathcal E]
=
\frac{(d+1)^2(d+2)}6.
}
\tag{16}
\]
Equations (3) and (16) give (4).

For the variance, assume first
\[
d\ge3.
\]
In \(P^2\), two path edges are either identical, share one vertex, or are disjoint. Define
\[
A=\mathbb E[X_1^2X_2^2],
\qquad
B=\mathbb E[X_1X_2^2X_3].
\]
For \(d\ge4\), also define
\[
C=\mathbb E[X_1X_2X_3X_4].
\]
Direct sampling without replacement and the standard power sums give
\[
A=
\frac{(d+1)(2d-1)(2d+1)(5d+6)}{180},
\tag{17}
\]
\[
B=
\frac{(d+1)(30d^3+35d^2-11d-12)}{360},
\tag{18}
\]
and
\[
C=
\frac{(d+1)(15d^3+15d^2-10d-8)}{240}.
\tag{19}
\]
The \(C\)-term has coefficient zero when \(d=3\), so (19) is only needed for \(d\ge4\).

There are \(d-1\) diagonal terms, \(d-2\) unordered adjacent pairs of path edges, and
\[
\binom{d-1}{2}-(d-2)
=
\frac{(d-2)(d-3)}2
\]
unordered disjoint pairs. Hence
\[
\mathbb E[P^2]
=
(d-1)A
+
2(d-2)B
+
(d-2)(d-3)C.
\tag{20}
\]
Substituting (15) and (17)--(19) into (20), simplifying, and using (14) yields
\[
\operatorname{Var}(\mathcal E)
=
4\operatorname{Var}(P)
=
\frac{
(d-2)(d+1)^2(d+2)(5d+11)
}{180}.
\tag{21}
\]
For \(d=2\), the two permutations both have
\[
\mathcal E=6,
\]
so the same formula gives zero. Multiplying (21) by \(N^4\) proves (5).

Finally, let
\[
\Sigma
=
\frac1{d!(d+1)!}
\sum_{\pi,\tau}
(v_{\pi,\tau}-c)(v_{\pi,\tau}-c)^{\mathsf T}.
\]
The vertex multiset is invariant under every coordinate permutation, so all diagonal entries of \(\Sigma\) are equal and all off-diagonal entries are equal. Every centered vertex lies in
\[
\mathbf1^\perp,
\]
so
\[
\Sigma\mathbf1=0.
\]
Also
\[
\operatorname{tr}\Sigma=\overline{R^2}.
\]
These three facts uniquely give (6).

Equation (5) now proves the cosphericity statement (7), and subtracting (4) from (3) proves (8).

## Verification
The proof is arbitrary-dimensional and symbolic.

The source-dependent input was checked directly in the full text and on the primary PDF page containing equations (4.1)--(4.3) and Definition 4.4. Those formulas give exactly the two-permutation vertex model used in (9), and Proposition 4.6 confirms that all indexed points are vertices for appropriate parameter pairs.

The accompanying `verify.py` independently enumerates every \(\tau\in\mathfrak S_d\) for
\[
2\le d\le9.
\]
It checks the exact radial identity, the first two moments of \(\mathcal E\), the dimension-two cosphericity transition, and the stated covariance on representative rational parameter choices. These finite checks are corroborative only.

## Relationship to prior work
Castillo and Liu introduce nested braid fans and regular nested permutohedra as a new refinement of the ordinary permutohedral framework. Their main results concern the fan, face correspondence, and deformation cone. The inspected full text contains no occurrence of “Euclidean”, “covariance”, “isotropic”, or “second moment”.

The source's vertex formula is the structural input to the present theorem, but it does not state how Euclidean radii vary across its
\[
d!(d+1)!
\]
vertices. Formula (3) isolates that variation into one permutation statistic, and (5) measures the failure of vertex cosphericity exactly.

Targeted published-result and literature searches used “nested permutohedron”, “nested braid fan”, “vertex covariance”, “second moment”, “isotropic”, “cospherical”, and “Euclidean radius”. No statement was located that gives (3)--(8) or a stronger result implying them.

## Limitations
The result concerns the **regular** nested permutohedron with the arithmetic sequences
\[
\alpha=(1,\ldots,d+1),
\qquad
\beta=(1,\ldots,d).
\]
For a general usual nested permutohedron with arbitrary strictly increasing \(\alpha,\beta\), the cross term in (10) need not collapse to the same constant.

The theorem determines radial second moments, not the extreme radii. In particular, no claim is made here about the circumradius or John--Löwner ellipsoids.

The isotropic covariance itself is forced by the coordinate-permutation symmetry; the substantive metric content is the exact scalar in (4), the full vertexwise identity (3), and the nonzero radial-variance formula (5).

## References
1. Federico Castillo and Fu Liu, *Deformation Cones of Nested Braid Fans*, arXiv:1710.01899, first public version 2017-10-05; International Mathematics Research Notices 2022(3), 1973--2026, DOI 10.1093/imrn/rnaa090.
