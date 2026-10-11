# Ricci excess exactly measures the quasi-contact metric defect

## Finding

Let
\[
(M^{2n+1},\phi,\xi,\eta,g)
\]
be a quasi-contact metric manifold whose characteristic vector field \(\xi\) is Killing. Use the exterior-derivative convention in which contact metric compatibility is
\[
d\eta=2\Phi,
\qquad
\Phi(X,Y)=g(X,\phi Y).
\]
Then the failure of contact-metric compatibility has the exact pointwise norm
\[
\boxed{
\|d\eta-2\Phi\|^2
=
2\bigl(\operatorname{Ric}(\xi,\xi)-2n\bigr).
}
\]
Equivalently,
\[
\boxed{
\|d\eta\|^2
=
2\operatorname{Ric}(\xi,\xi).
}
\]

There is also an exact angular form of the identity. Let \(\vartheta\in[0,\pi/2)\) be the pointwise angle between the two nonzero two-forms \(d\eta\) and \(2\Phi\). Then
\[
\boxed{
\cos^2\vartheta
=
\frac{2n}{\operatorname{Ric}(\xi,\xi)},
\qquad
\sin^2\vartheta
=
\frac{\operatorname{Ric}(\xi,\xi)-2n}
{\operatorname{Ric}(\xi,\xi)}.
}
\]
Thus the characteristic Ricci excess over the \(K\)-contact value \(2n\) is exactly half the squared contact-metric defect.

For the five-dimensional Sasaki--Einstein deformation family of Cappelletti-Montano and De Nicola, with parameter \(\mu\ge0\),
\[
\operatorname{Ric}(\xi,\xi)=4(1+\mu^2),
\]
so
\[
\boxed{
\|d\eta-2\Phi\|^2=8\mu^2,
\qquad
\|d\eta\|^2=8(1+\mu^2),
\qquad
\vartheta=\arctan\mu.
}
\]
In particular, the deformation parameter \(\mu\) has an intrinsic interpretation as the tangent of the angle between the actual Reeb curvature form \(d\eta\) and the compatible contact-metric form \(2\Phi\).

## Assumptions and scope

The norm is the pointwise norm on two-forms induced by \(g\). The convention
\[
d\eta=2\Phi
\]
is the convention used in the motivating preprint; some older papers use a halved exterior derivative and therefore display different numerical factors.

The Killing hypothesis is essential to the stated identity because it makes
\[
h=\frac12\mathcal L_\xi\phi
\]
skew-adjoint. No claim is made here for arbitrary quasi-contact metric structures with non-Killing characteristic field.

The result is pointwise and requires no compactness, completeness, or curvature sign assumption.

## Proof

Put
\[
h=\frac12\mathcal L_\xi\phi.
\]
For a quasi-contact metric structure, the source proves
\[
d\eta(X,Y)-2\Phi(X,Y)
=
-2g(\phi h_aX,Y),
\]
where
\[
h_a=\frac12(h-h^\ast)
\]
is the skew-adjoint part of \(h\). When \(\xi\) is Killing, the same source proves
\[
h^\ast=-h,
\]
hence
\[
h_a=h.
\]
Therefore, with
\[
B=d\eta-2\Phi,
\]
we have
\[
B(X,Y)=-2g(\phi hX,Y).
\]

If \(K\) is a skew-adjoint endomorphism and
\[
\omega_K(X,Y)=g(KX,Y),
\]
then
\[
\|\omega_K\|^2=\frac12\|K\|_{\mathrm{HS}}^2.
\]
The tensor \(h\) is horizontal, while \(\phi\) is orthogonal on
\[
\mathcal D=\ker\eta.
\]
Consequently
\[
\|\phi h\|_{\mathrm{HS}}=\|h\|_{\mathrm{HS}},
\]
and hence
\[
\|B\|^2
=
4\cdot\frac12\|\phi h\|_{\mathrm{HS}}^2
=
2\|h\|_{\mathrm{HS}}^2.
\]

The curvature identity proved in the source is
\[
\operatorname{Ric}(\xi,\xi)
=
2n+\|h\|_{\mathrm{HS}}^2.
\]
Combining the last two equations gives
\[
\|d\eta-2\Phi\|^2
=
2\bigl(\operatorname{Ric}(\xi,\xi)-2n\bigr).
\]

It remains to recover the norm of \(d\eta\) itself. The quasi-contact equations make
\[
B=d\eta-2\Phi
\]
\(\phi\)-anti-invariant on \(\mathcal D\), whereas \(\Phi\) is \(\phi\)-invariant. These two subspaces of horizontal two-forms are orthogonal. Hence
\[
\langle B,\Phi\rangle=0.
\]
In a \(\phi\)-adapted orthonormal frame of the \(2n\)-dimensional horizontal space,
\[
\|\Phi\|^2=n.
\]
Thus
\[
\|d\eta\|^2
=
\|2\Phi+B\|^2
=
4n+\|B\|^2
=
4n+2\|h\|_{\mathrm{HS}}^2
=
2\operatorname{Ric}(\xi,\xi).
\]

The same orthogonal decomposition gives
\[
\langle d\eta,2\Phi\rangle
=
\|2\Phi\|^2
=
4n.
\]
Since
\[
\|d\eta\|^2=2\operatorname{Ric}(\xi,\xi),
\qquad
\|2\Phi\|^2=4n,
\]
the angle \(\vartheta\) satisfies
\[
\cos^2\vartheta
=
\frac{2n}{\operatorname{Ric}(\xi,\xi)}.
\]
Subtracting from one gives the sine formula.

For the source's five-dimensional family,
\[
n=2,
\qquad
h=\mu\phi_2,
\qquad
\|h\|_{\mathrm{HS}}^2=4\mu^2,
\]
so the displayed family formulas follow immediately. Since \(\mu\ge0\),
\[
\cos\vartheta=\frac1{\sqrt{1+\mu^2}},
\]
which is equivalent to
\[
\vartheta=\arctan\mu.
\]

## Verification

The bundled symbolic checker verifies the algebraic conversion
\[
\|d\eta-2\Phi\|^2=2\|h\|_{\mathrm{HS}}^2,
\qquad
\operatorname{Ric}(\xi,\xi)=2n+\|h\|_{\mathrm{HS}}^2
\]
into the two boxed norm identities and the angle law.

It also uses an exact four-dimensional horizontal matrix model for the five-dimensional deformation family. The matrices satisfy the required skew-adjointness and anticommutation identities and reproduce
\[
\|h\|_{\mathrm{HS}}^2=4\mu^2,
\qquad
\|d\eta-2\Phi\|^2=8\mu^2.
\]
The checker is only an algebraic replay. The arbitrary-dimensional theorem is established analytically above and is not inferred from finite-dimensional sampling.

## Relationship to prior work

Cappelletti-Montano and De Nicola construct strict quasi-contact metric structures with Killing characteristic field and prove two ingredients used here: the defect identity
\[
d\eta-2\Phi=-2g(\phi h\,\cdot,\cdot)
\]
under the Killing hypothesis, and the curvature identity
\[
\operatorname{Ric}(\xi,\xi)=2n+\|h\|_{\mathrm{HS}}^2.
\]
They use the latter to characterize the \(K\)-contact case by the equality
\[
\operatorname{Ric}(\xi,\xi)=2n.
\]
Their inspected full preprint does not state the norm identity
\[
\|d\eta-2\Phi\|^2
=
2\bigl(\operatorname{Ric}(\xi,\xi)-2n\bigr),
\]
the formula
\[
\|d\eta\|^2=2\operatorname{Ric}(\xi,\xi),
\]
or the angle law.

Earlier quasi-contact literature establishes contactness of \(\eta\), studies curvature conditions, and develops tensorial characterizations. A 2020 paper asserted that Killing characteristic field forces \(K\)-contactness; the motivating 2026 preprint identifies an error in that assertion and supplies counterexamples while retaining the preliminary identities needed above. A 2024 weak quasi-contact paper gives other curvature criteria but does not state this exact norm--Ricci relation.

Targeted searches for the defect norm, the equivalent Reeb-form norm, the angle formula, and source-specific aliases did not locate a covering statement.

## Limitations

The identity requires the quasi-contact equations and a Killing characteristic field. It is not a formula for arbitrary almost-contact metric structures.

The angle \(\vartheta\) measures compatibility with the prescribed pair \((\phi,g)\). The one-form \(\eta\) itself is already a contact form on every quasi-contact metric manifold.

The result is an exact pointwise structural consequence of the source identities; it does not by itself classify the global topology or moduli of strict quasi-contact structures.

## References

1. Beniamino Cappelletti-Montano and Antonio De Nicola, *Quasi-contact metric structures from Sasaki-Einstein metrics*, arXiv:2610.02073v1, first submitted 1 October 2026.
2. Jihong Bae, Yeongjae Jang, JeongHyeong Park, and Kouei Sekigawa, *Quasi contact metric manifolds with Killing characteristic vector fields*, Bulletin of the Korean Mathematical Society 57 (2020), 1299--1306.
3. Vladimir Rovenski, *Weak Quasi-Contact Metric Manifolds and New Characteristics of K-Contact and Sasakian Manifolds*, Mathematics 12 (2024), 3230.
