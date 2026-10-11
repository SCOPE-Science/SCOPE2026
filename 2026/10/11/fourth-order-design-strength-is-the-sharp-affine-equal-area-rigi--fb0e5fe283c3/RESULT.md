# Fourth-order design strength is the sharp affine equal-area rigidity threshold

## Finding

Let
\[
X=\{x_1,\ldots,x_N\}\subset S^2
\]
be a spherical \(t\)-design with
\[
t\ge4,
\]
and let \(P_X\subset\mathbb R^3\) be its Minkowski polytope, whose \(N\) facets all have the same area.

For an invertible linear map
\[
A\in GL(3),
\]
the facets of \(AP_X\) all have equal area if and only if
\[
\boxed{
A=\lambda U
}
\]
for some
\[
\lambda>0,
\qquad
U\in O(3).
\]
Thus every affine deformation preserving the equal-facet-area property is necessarily a Euclidean similarity.

The design-strength threshold is sharp. Put
\[
\begin{aligned}
v_1&=\left(\sqrt{\frac23},0,\frac1{\sqrt3}\right),\\
v_2&=\left(-\frac1{\sqrt6},\frac1{\sqrt2},\frac1{\sqrt3}\right),\\
v_3&=\left(-\frac1{\sqrt6},-\frac1{\sqrt2},\frac1{\sqrt3}\right),
\end{aligned}
\]
and
\[
X_0=\{\pm v_1,\pm v_2,\pm v_3\}.
\]
Then \(X_0\) is a spherical \(3\)-design. Nevertheless the nonsimilarity
\[
\boxed{
A_0=
\operatorname{diag}
\left(
\frac2{\sqrt5},
\frac2{\sqrt5},
\sqrt2
\right)
}
\]
maps its Minkowski polytope to another polytope whose six facets still all have equal area.

Hence fourth-order isotropy is exactly sufficient to rule out the anisotropic affine equal-area phenomenon that can persist at strength three.

## Assumptions and scope

The sphere is the Euclidean unit sphere \(S^2\subset\mathbb R^3\).

The Minkowski polytope is the translation class supplied by the equal-area realization of a spherical design. Translation does not affect facet areas, so no normalization of the representative is needed.

The statement asks only whether all corresponding facets of the affine image \(AP_X\) have one common area. It does not require the transformed unit normals themselves to remain a spherical \(t\)-design.

The sharpness example establishes that the hypothesis \(t\ge4\) cannot be weakened to \(t\ge3\). Since every spherical \(3\)-design is also a \(2\)-design, it also excludes a strength-two theorem of the same form.

## Proof

The source proves that every facet of \(P_X\) has area
\[
a=\frac{4\pi}{N},
\]
with outer unit normal \(x_j\), and that under
\[
A\in GL(3)
\]
the corresponding facet of \(AP_X\) has area
\[
a_j^A
=
|\det A|\,
|A^{-T}x_j|\,
a.
\]
Therefore all facets of \(AP_X\) have equal area if and only if there is a constant
\[
c>0
\]
such that
\[
|A^{-T}x_j|^2=c
\]
for every \(j\).

Set
\[
Q=A^{-1}A^{-T}.
\]
Then \(Q\) is positive definite and the equal-area condition becomes
\[
x_j^TQx_j=c
\qquad
(1\le j\le N).
\]
Define the quadratic polynomial
\[
q(u)=u^TQu-c.
\]
It vanishes at every design node:
\[
q(x_j)=0.
\]

Because \(t\ge4\), the spherical design integrates every polynomial of degree at most four exactly. The nonnegative polynomial
\[
q(u)^2
\]
has degree four, so
\[
\int_{S^2}q(u)^2\,d\sigma(u)
=
\frac1N\sum_{j=1}^N q(x_j)^2
=
0.
\]
Hence
\[
q(u)=0
\]
for every \(u\in S^2\). Thus the quadratic form \(u^TQu\) is constant on the unit sphere. By the spectral theorem this is possible only when
\[
Q=cI.
\]
Equivalently,
\[
A^{-1}A^{-T}=cI,
\]
or
\[
AA^T=c^{-1}I.
\]
The polar decomposition therefore gives
\[
A=c^{-1/2}U
\]
with \(U\in O(3)\). This proves the nontrivial implication. The converse is immediate from the facet-area transformation formula, because a similarity multiplies every facet area by the same factor.

It remains to prove sharpness. A direct calculation gives
\[
v_i\cdot v_j=\delta_{ij},
\]
so \(v_1,v_2,v_3\) form an orthonormal basis. Consequently
\[
\frac16\sum_{x\in X_0}xx^T
=
\frac13I.
\]
The set \(X_0\) is antipodal, hence all odd moments vanish. Constants are integrated trivially, the displayed identity gives exactness in degree two, and antipodality gives exactness in degrees one and three. Thus \(X_0\) is a spherical \(3\)-design.

Now
\[
Q_0=A_0^{-1}A_0^{-T}
=
\operatorname{diag}
\left(
\frac54,\frac54,\frac12
\right).
\]
Each \(v_i\) satisfies
\[
(v_i)_3^2=\frac13
\]
and therefore
\[
(v_i)_1^2+(v_i)_2^2=\frac23.
\]
Hence
\[
v_i^TQ_0v_i
=
\frac54\frac23+\frac12\frac13
=
1.
\]
The same is true for \(-v_i\). Therefore
\[
|A_0^{-T}x|=1
\]
for every \(x\in X_0\). The affine facet-area formula shows that every facet area is multiplied by the same factor
\[
|\det A_0|.
\]
Thus \(A_0P_{X_0}\) is again equal-facet-area.

Finally, \(A_0\) is not a similarity because its first two singular values are
\[
\frac2{\sqrt5},
\]
while its third singular value is
\[
\sqrt2.
\]
This completes the sharpness proof.

## Verification

The bundled exact symbolic checker verifies that the displayed \(v_i\) form an orthonormal basis, that \(X_0\) has isotropic second moment, that
\[
Q_0=A_0^{-1}A_0^{-T},
\]
and that every node satisfies
\[
x^TQ_0x=1.
\]
It also checks that \(Q_0\) is not scalar.

The infinite rigidity theorem does not depend on finite computation. Its decisive step is exact integration of the degree-four nonnegative polynomial
\[
(u^TQu-c)^2.
\]

## Relationship to prior work

An's recent Minkowski-polytope construction proves that a spherical \(t\)-design gives an equal-facet-area polytope and records the exact affine transformation law
\[
a_j^A
=
|\det A|\,|A^{-T}x_j|\,a_j.
\]
The same paper proves exact fourth surface-moment isotropy when \(t\ge4\). Its affine-covariance section observes that a nonconformal affine map generally introduces unequal facet weights, but it does not state a rigidity theorem characterizing all maps that can preserve equal facet areas for a given high-strength design.

The result here closes that exceptional possibility at precisely fourth order. The proof uses the source's affine Jacobian together with degree-four design exactness to show that a constant transformed facet weight forces the entire positive quadratic form \(A^{-1}A^{-T}\) to be scalar. The explicit spherical \(3\)-design shows that lower-order isotropy genuinely leaves room for anisotropic equal-area affine images.

Targeted searches using spherical-design, finite-frame, affine-equal-norm, equal-facet-area, and fourth-moment formulations did not locate this sharp threshold statement.

## Limitations

The theorem is stated for the three-dimensional Minkowski polytope associated with a design on \(S^2\). The same degree-four argument has a natural higher-dimensional analogue, but that extension is not claimed here.

The sharpness example concerns preservation of equal facet areas, not preservation of strength-three design exactness by the transformed normals.

No quantitative stability estimate is proved: an approximately equal-facet-area affine image is not converted here into an explicit distance of \(A\) from the similarity group.

## References

1. Congpei An, *Minkowski Polytopes of Spherical Designs: High-Order Isotropy and Quantitative Sphericity*, arXiv:2608.11570v1, first submitted 12 August 2026.
2. P. Delsarte, J.-M. Goethals, and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363--388.
