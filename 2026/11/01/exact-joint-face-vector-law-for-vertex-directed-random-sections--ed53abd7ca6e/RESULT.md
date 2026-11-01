# Exact joint face-vector law for vertex-directed random sections of regular crosspolytopes

## Finding

Fix an integer \(d\ge3\). For the regular crosspolytope \(C_d=\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\subset\mathbb R^d\), choose a Haar-uniform normal \(U\) and the hyperplane through \(te_d\), where \(0\le t<1\). Its section \(Q_{d,t}\) has an **exact joint law for every face count**, rather than merely formulas for the expected counts.

Let \(G_1,\ldots,G_d\) be independent standard normal random variables and put
\[
M_t=1+\#\{i\in\{1,\ldots,d-1\}:|G_i|>t|G_d|\}.
\]
For \(1\le m\le d\), define the polynomial
\[
H_{d,m}(z)=(1+2z)^d-(1+z)^m\bigl[1+(1+2z)^{d-m}\bigr]+1.
\]
Then, almost surely and simultaneously for all \(0\le k\le d-2\),
\[
f_k(Q_{d,t})=[z^{k+2}]H_{d,M_t}(z).
\]
For \(0<t<1\), every \(m\in\{1,\ldots,d\}\) has strictly positive probability given by
\[
\Pr(M_t=m)=\binom{d-1}{m-1}\sqrt{\frac2\pi}\int_0^\infty e^{-r^2/2}
\operatorname{erfc}\left(\frac{tr}{\sqrt2}\right)^{m-1}
\operatorname{erf}\left(\frac{tr}{\sqrt2}\right)^{d-m}\,dr.
\]
At \(t=0\), \(M_0=d\) almost surely. At the one-sided vertex limit \(t\uparrow1\), the distribution of \(M_t\) becomes uniform on \(\{1,\ldots,d\}\). Since \(H_{d,d-1}=H_{d,d}\) and all earlier face-vector profiles are distinct, the distinct limiting face vectors have respective masses \(1/d\) (for \(m=1,\ldots,d-2\)) and \(2/d\) (the maximal vector).

The vertex count is \(V_t=M_t(2d-1-M_t)\). In the same limit,
\[
\mathbb E V_t\longrightarrow \frac{2(d^2-1)}3,
\qquad
\operatorname{Var}(V_t)\longrightarrow \frac{(d-2)(d-1)(d+1)(4d-7)}{45}.
\]
For the regular octahedron \(d=3\), the entire polygon-type law reduces to
\[
\Pr(Q_{3,t}\text{ is a quadrilateral})=\frac2\pi\arctan\left(\frac{t^2}{\sqrt{1+2t^2}}\right),
\]
and the complementary probability produces a hexagon. All face counts can be coupled to be nonincreasing in \(t\).

## Assumptions and scope

The normal is distributed according to normalized Haar measure on \(S^{d-1}\); the section is the **affine hyperplane** section through the interior point \(te_d\), not a projection. The parameters satisfy \(d\in\mathbb Z\), \(d\ge3\), and \(0\le t<1\). Degenerate normals causing the section plane to pass through a vertex have measure zero. An equality at \(t=1\) is **not** asserted: the limit approaches a vertex from the interior, and the slice at the actual vertex has different degeneracies.

Here \(f_k\) denotes the number of \(k\)-faces of the \((d-1)\)-dimensional section; \([z^j]\) denotes polynomial coefficient extraction. \(\operatorname{erf}\) and \(\operatorname{erfc}\) are the error function and its complement.

## Proof

**Face correspondence.** A generic hyperplane through the interior of a polytope intersects a \((k+1)\)-face transversely in a \(k\)-face precisely when its vertices lie on both sides. Every \(k\)-face of the section arises in exactly this way. A \(j\)-vertex face of \(C_d\) is specified by choosing \(j\) distinct coordinate axes and one sign on each axis; hence the generating polynomial for all faces of the original crosspolytope by vertex count is \((1+2z)^d\).

**Signs and polynomial.** Reverse the normal if needed so that \(U_d>0\), without changing the hyperplane. The affine functional at a vertex \(\pm e_i\) is \(\pm U_i-tU_d\). For axis \(d\) these values have opposite signs, because \(t<1\). Among the remaining axes, exactly \(M_t-1\) have two opposite-sign vertex values, while each of the other \(d-M_t\) axes has two negative vertex values. Therefore the generating polynomial for faces with *only positive* vertices is \((1+z)^{M_t}\), and for faces with *only negative* vertices is \((1+z)^{M_t}(1+2z)^{d-M_t}\). Subtracting these from the total and adding back the double-counted empty choice proves \(H_{d,M_t}\), coefficient by coefficient for \(2\le j\le d\).

**Joint law.** A Haar normal has the same direction distribution as \((G_1,\ldots,G_d)/\sqrt{\sum_iG_i^2}\). Conditional on \(|G_d|=r\), the \(d-1\) comparison indicators are independent Bernoulli variables with success probability \(\operatorname{erfc}(tr/\sqrt2)\). Integration against the half-normal density \(\sqrt{2/\pi}e^{-r^2/2}\) yields the asserted one-dimensional integral, with strictly positive mass at every \(m\) when \(0<t<1\). At \(t=0\), every pair is split with probability one.

**Sharp vertex limit and monotonicity.** For each sample having pairwise distinct absolute Gaussian coordinates, \(M_t\) tends as \(t\uparrow1\) to one plus the number of absolute coordinates larger than \(|G_d|\). Its rank is uniform among the \(d\) possibilities by exchangeability, proving the discrete uniform law. Moreover,
\[
H_{d,m+1}(z)-H_{d,m}(z)
=z(1+z)^m\bigl[(1+2z)^{d-m-1}-1\bigr].
\]
For \(m\le d-2\), every coefficient of degrees \(2,\ldots,d\) on the right is strictly positive; at \(m=d-1\) the entire difference vanishes. This proves that the last two ranks yield exactly the same full face vector, all earlier ones are distinct, and every face count is nondecreasing with \(m\). Since the indicators defining \(M_t\) decrease pointwise as \(t\) grows, this is the claimed strong coordinatewise monotone coupling.

**Moments and the octahedral formula.** Taking the coefficient of \(z^2\) in \(H_{d,m}\) gives \(m(2d-1-m)\). The uniform distribution of \(m=1,\ldots,d\) and elementary sums of powers \(m,m^2,m^3,m^4\) yield the stated limiting mean and variance. For \(d=3\), a quadrilateral occurs exactly when \(|G_1|,|G_2|<t|G_3|\). This corresponds on the unit sphere to two congruent rectangular cones with edge generators \((\pm t,\pm t,1)\). Each cone has solid angle \(4\arctan(t^2/\sqrt{1+2t^2})\); dividing their combined area by \(4\pi\) gives the displayed probability. These cones are disjoint when \(t\le1\).

## Verification

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The script independently enumerates signed crosspolytope faces, checks coefficient formulas and Euler identities in dimensions three through eight, checks the strict rank order and final tie, verifies the uniform rank limit by exhaustive permutations, and compares the octahedral closed form with numerical half-normal integration. The analytic proof, not these finite checks, establishes the all-dimensional result.

## Relationship to prior work

Philipp Schange's 2026 study of solid angles and randomly translated sections supplies explicit formulas for **expected** face numbers of regular crosspolytopes and related polytopes. The theorem above concerns the **complete joint distribution** of face counts, a one-dimensional latent rank, its monotone coupling, and a sharp one-sided vertex-limit distribution. Expected values alone do not imply this joint distribution. Related investigations of central regular-simplex sections and central four-cube sections treat different models. The motivating paper's full text could not be inspected, leaving a residual priority risk regarding the possibility of unadvertised equivalent formulas.

## Limitations

The law applies to hyperplanes translated along an axis through a vertex, not to general off-axis translation vectors, random codimension greater than one, or arbitrary crosspolytopes. All statements about \(t=1\) are **limits**, not exact section assertions. Neither independent mathematical validation nor an exhaustive historical-priority determination has been performed.

## References

- Philipp Schange, *Solid-angle formulas for simplicial cones and random shifted sections of polytopes*, arXiv:2610.28084v1 (first submitted 2026-10-20), https://arxiv.org/abs/2610.28084.
- David L. Donoho and Jared Tanner, *Counting the Faces of Randomly-Projected Hypercubes and Orthants, with Applications*, Discrete & Computational Geometry 43 (2010), 522–541, https://doi.org/10.1007/s00454-009-9221-z (a different random-projection model).
