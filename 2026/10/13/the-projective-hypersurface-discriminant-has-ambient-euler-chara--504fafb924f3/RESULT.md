# The projective hypersurface discriminant has ambient Euler characteristic
## Finding
Let
\[
n\ge2,
\qquad
d\ge2,
\]
and let
\[
\mathcal D_{n,d}
\subset
\mathbb P(\operatorname{Sym}^d\mathbb C^{n*})
\]
be the projective discriminant locus of singular degree-\(d\) hypersurfaces in
\[
\mathbb P^{n-1}.
\]
Write
\[
N=\binom{n+d-1}{d},
\]
so the ambient coefficient space is
\[
\mathbb P^{N-1}.
\]
Let
\[
\mathcal U_{n,d}
=
\mathbb P(\operatorname{Sym}^d\mathbb C^{n*})
\setminus
\mathcal D_{n,d}
\]
be the parameter space of smooth degree-\(d\) projective hypersurfaces.

Then, for every pair except binary quadrics,
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal D_{n,d})=N
}
\]
and
\[
\boxed{
\chi_c(\mathcal U_{n,d})=0.
}
\]

The unique exception is
\[
(n,d)=(2,2),
\]
for which
\[
\boxed{
\chi_{\mathrm{top}}(\mathcal D_{2,2})=2,
\qquad
\chi_c(\mathcal U_{2,2})=1.
}
\]

Thus, outside one smallest case, the discriminant of singular hypersurfaces has exactly the same Euler characteristic as the entire coefficient projective space.

## Assumptions and scope
The base field is \(\mathbb C\).

A homogeneous form \(F\) represents a point of the discriminant precisely when the projective hypersurface
\[
V(F)\subset\mathbb P^{n-1}
\]
is singular. Equivalently, for a homogeneous cone, the affine hypersurface has a nonzero singular point.

The discriminant locus is projective, so ordinary and compactly supported Euler characteristic agree on it. The smooth-hypersurface parameter space is quasi-projective, so the complement statement is formulated using compactly supported Euler characteristic.

The theorem concerns the coefficient parameter space itself, not the geometric quotient by projective linear changes of coordinates.

## Proof
Choose coordinates
\[
x_1,\ldots,x_n
\]
and an integer
\[
B>d.
\]
Let
\[
\mathbb C^*
\]
act diagonally by
\[
z\cdot x_i=z^{B^{i-1}}x_i.
\]

For a degree-\(d\) monomial
\[
x^\alpha=x_1^{\alpha_1}\cdots x_n^{\alpha_n},
\qquad
\alpha_i\ge0,
\qquad
\sum_i\alpha_i=d,
\]
the induced weight is
\[
w(\alpha)=\sum_{i=1}^{n}\alpha_i B^{i-1}.
\]
Since
\[
0\le\alpha_i\le d<B,
\]
uniqueness of base-\(B\) expansion shows that distinct degree-\(d\) monomials have distinct weights.

Hence the fixed locus of the induced action on the coefficient projective space consists exactly of the \(N\) monomial coordinate points.

We classify which of these points represent smooth projective hypersurfaces.

If the monomial involves only one variable, then
\[
V(x_i^d)
\]
is nonreduced because
\[
d\ge2,
\]
hence singular.

Suppose the monomial involves at least two distinct variables. If
\[
n\ge3,
\]
its zero locus is a union of at least two coordinate hyperplanes, possibly with multiplicity. Two distinct coordinate hyperplanes intersect in
\[
\mathbb P^{n-3},
\]
and the hypersurface is singular along that intersection.

It remains to consider
\[
n=2.
\]
A binary monomial has the form
\[
x^{d-s}y^s.
\]
It defines a reduced divisor on
\[
\mathbb P^1
\]
only when both positive exponents equal \(1\). This happens only for
\[
d=2,
\qquad
s=1.
\]
Thus the unique smooth monomial hypersurface among all cases under consideration is
\[
xy
\]
for binary quadrics.

Therefore
\[
(\mathcal U_{n,d})^{\mathbb C^*}
=
\varnothing
\]
for every
\[
(n,d)\ne(2,2),
\]
whereas
\[
(\mathcal U_{2,2})^{\mathbb C^*}
=
\{[xy]\}.
\]

For any complex algebraic variety \(Y\) with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(Y)=\chi_c(Y^{\mathbb C^*}).
\]
One proof removes the fixed locus and applies a finite Rosenlicht stratification to the complement. After refinement by stabilizer type, every nonfixed stratum is a Zariski-locally-trivial bundle with fiber a finite quotient of \(\mathbb C^*\), hence with compactly supported Euler characteristic zero. Additivity leaves only the fixed locus.

Applying this to \(\mathcal U_{n,d}\) gives
\[
\chi_c(\mathcal U_{n,d})=0
\]
outside the binary-quadratic case and
\[
\chi_c(\mathcal U_{2,2})=1.
\]

Finally,
\[
\mathbb P^{N-1}
=
\mathcal D_{n,d}\sqcup\mathcal U_{n,d},
\]
so constructible additivity yields
\[
\chi_{\mathrm{top}}(\mathcal D_{n,d})
=
N-\chi_c(\mathcal U_{n,d}).
\]
This is \(N\) outside the exceptional pair and \(3-1=2\) for binary quadrics.

## Verification
The bundled checker enumerates all degree-\(d\) monomials for
\[
2\le n\le8,
\qquad
2\le d\le10.
\]
It verifies pairwise separation of the base-\(B\) weights and classifies smooth monomial divisors by the support and exponent criterion used in the proof.

Across the entire test grid it confirms that the only smooth monomial fixed point is
\[
xy
\]
for
\[
(n,d)=(2,2).
\]

These finite checks are regression evidence only. The theorem for all parameters follows from base-\(B\) uniqueness, the elementary classification of smooth monomial hypersurfaces, and Euler localization.

## Relationship to prior work
The discriminant of homogeneous forms is classical. Alper and Isaev work with the affine open set of forms having nonvanishing discriminant and its projectivization; in their general setup, nonvanishing of the discriminant is the nondegeneracy condition for the corresponding homogeneous hypersurface cone.

The present statement concerns the global Euler characteristic of the projective discriminant and its open complement. Targeted searches for Euler characteristics of homogeneous-form discriminants, parameter spaces of smooth hypersurfaces, Veronese dual discriminants, and torus-fixed monomial descriptions did not locate the all-\((n,d)\) formula above.

Nearby work on discriminants emphasizes invariant theory, dual degree, singularity structure, cohomology, or moduli quotients. Those results do not imply the coefficient-space Euler characteristic without the fixed-point argument.

## Limitations
The theorem does not compute the cohomology or fundamental group of the smooth-hypersurface parameter space. Vanishing of
\[
\chi_c(\mathcal U_{n,d})
\]
is compatible with very rich topology.

The coefficient space is not divided by
\[
\operatorname{PGL}_n.
\]
No claim is made about Euler characteristics of coarse moduli spaces or stacks of smooth hypersurfaces.

The localization argument is short once one notices that every monomial hypersurface is singular except the reduced binary quadric. An older or unindexed observation may therefore exist.

## References
Jarod Alper and Alexander Isaev, *Associated Forms and Hypersurface Singularities: The Binary Case*, arXiv:1407.6838, first submitted 25 July 2014.
