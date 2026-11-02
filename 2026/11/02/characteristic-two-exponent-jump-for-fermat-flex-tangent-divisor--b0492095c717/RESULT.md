# Characteristic-two exponent jump for Fermat flex-tangent divisors

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(d\ge 3\) be any odd integer. Consider the plane divisor \(C_d\subset\mathbb P^2_k\) with equation
\[
F_d=xyz(x^d+y^d)(y^d+z^d)(x^d+z^d)(x^d+y^d+z^d)=0.
\]
It is geometrically reduced, has degree \(4d+3\), and is a **free divisor with logarithmic syzygy exponents exactly \((d+1,3d+1)\)**. The total length of its projective Jacobian singular scheme is
\[
\tau(C_d)=13d^2+12d+3.
\]
The entire geometric singularity basket is: \(d^2\) ordinary triple points off the coordinate axes, three ordinary \((d+2)\)-fold points at the coordinate vertices, and \(3d\) three-branch contacts with local equation \(s t(t+s^d)=0\). Their respective Tjurina numbers are \(4\), \((d+1)^2\), and \(2d+2\).

For comparison, the original characteristic-zero theorem gives **the same defining polynomial** the balanced exponents \((2d+1,2d+1)\) and total Tjurina number \(12d^2+12d+3\). Thus the characteristic-two specialization has a nontrivial splitting-type jump and an excess Jacobian length of \(d^2\), despite being reduced and free on both sides.

## Assumptions and scope

The statements concern the displayed polynomial, over every algebraically closed field of characteristic \(2\), for all odd integers \(d\ge3\). The coordinate axes and the \(3d\) roots of the three binary Fermat forms are distinct lines because \(d\) is odd. The last factor is a smooth Fermat curve, and no line component divides it, so the whole divisor is reduced. The scheme length refers to the projective singular scheme cut out by the homogeneous Jacobian ideal \((\partial_xF_d,\partial_yF_d,\partial_zF_d)\), equivalently the sheafified Tjurina scheme; since \(4d+3\) is odd, Euler's equation puts \(F_d\) in that ideal.

## Proof

Set \(U=x^d\), \(V=y^d\), \(W=z^d\), and let \(\mathcal L\) be the seven linear forms
\[
U,\ V,\ W,\ U+V,\ V+W,\ U+W,\ U+V+W
\]
over \(\mathbb F_2\). Their elementary identities are
\[
\sum_{\ell\in\mathcal L}\ell=0,
\qquad
\sum_{\ell\in\mathcal L}\ell^3=0.
\]
For example, each pure cube occurs four times, and each mixed cubic monomial occurs twice. Consider the three homogeneous derivations
\[
E=x\partial_x+y\partial_y+z\partial_z,
\]
\[
D_1=x^{d+1}\partial_x+y^{d+1}\partial_y+z^{d+1}\partial_z,
\qquad
D_2=x^{3d+1}\partial_x+y^{3d+1}\partial_y+z^{3d+1}\partial_z.
\]
As \(d\) is odd, \(D_1(U)=U^2\) and \(D_2(U)=U^4\), and likewise for \(V,W\). These derivations act on any \(\ell\in\mathcal L\) by \(D_1(\ell)=\ell^2\) and \(D_2(\ell)=\ell^4\). The three coordinate factors of \(F_d\) contribute logarithmic derivatives \(U,U^3\), etc., so the displayed seven-form identities give
\[
D_1(F_d)/F_d=\sum_{\ell\in\mathcal L}\ell=0,
\qquad
D_2(F_d)/F_d=\sum_{\ell\in\mathcal L}\ell^3=0.
\]
These are polynomial identities, not merely rational equalities. Also Euler's identity gives \(E(F_d)=(4d+3)F_d=F_d\) in characteristic \(2\).

The coefficient determinant is the Moore/Vandermonde identity
\[
\begin{aligned}
\det\!\begin{pmatrix}
x&y&z\\
x^{d+1}&y^{d+1}&z^{d+1}\\
x^{3d+1}&y^{3d+1}&z^{3d+1}
\end{pmatrix}
&=xyz\det\!\begin{pmatrix}1&1&1\\U&V&W\\U^3&V^3&W^3\end{pmatrix}\\
&=xyz(U+V)(V+W)(U+W)(U+V+W)=F_d.
\end{aligned}
\]
Indeed, the degree-four determinant vanishes on the four indicated binary hyperplanes, and evaluating a single monomial coefficient shows that the scalar is one. In characteristic \(2\), the polynomial \(F_d\) is reduced. The determinant criterion for logarithmic derivations therefore makes \(E,D_1,D_2\) a free basis of \(\operatorname{Der}(-\log F_d)\). This criterion remains valid here without a characteristic-zero assumption: each irreducible factor of \(F_d\) is generically separable, and the displayed determinant has valuation one at each factor, so the three derivations form a basis at every codimension-one localization; reflexivity/intersection of such localizations gives the global basis.

Because \(E(F_d)=F_d\), subtracting \(\theta(F_d)E/F_d\) from each logarithmic derivation \(\theta\) identifies the kernel of the Jacobian map with the free span of \(D_1,D_2\). The coefficient degrees are exactly \(d+1\) and \(3d+1\), proving the free exponents. The Hilbert--Burch resolution for the homogeneous Jacobian ideal then gives
\[
\operatorname{length}(\operatorname{Sing} C_d)=(4d+2)^2-(d+1)(3d+1)=13d^2+12d+3.
\]

We independently classify the singular points. At a coordinate vertex, all factors except the two local coordinate variables and the opposite binary Fermat factor are units; the germ is a unit times \(st(s^d+t^d)\), an ordinary \((d+2)\)-fold point. Since its degree is odd in characteristic two and its factors are distinct, its Jacobian intersection length is \((d+1)^2\).

On a coordinate axis away from the vertices, there are precisely \(d\) points defined by equality of the other two coordinate \(d\)-th powers. If \(s\) is the vanishing coordinate and \(t\) denotes the difference of those two powers, then the germ is a unit times \(st(t+s^d)\). Its partial derivatives generate \((t^2,s^{d+1})\), giving local Tjurina length \(2(d+1)\). Over the three axes this gives \(3d\) such points.

Off the axes, the Fermat component can meet one of the three families of lines only on an axis, and two distinct line families meet precisely when \(U=V=W\). On the chart \(x=1\) this imposes \(y^d=z^d=1\), giving exactly \(d^2\) points. Their three local branches are transverse, with equation analytically equivalent to \(st(s+t)=0\); the Jacobian ideal is \((s^2,t^2)\), of length four. The preceding cases exhaust all intersections of distinct components and therefore all singularities. Their local lengths sum to
\[
4d^2+3(d+1)^2+3d(2d+2)=13d^2+12d+3,
\]
in agreement with the free-resolution computation.

## Verification

The accompanying standalone script `verify_fano.py` performs exact sparse-polynomial arithmetic over \(\mathbb F_2\). It checks both seven-form identities and the universal degree-four determinant identity, then directly checks Euler's equality, both annihilating syzygies, the full determinant, and both expressions for the Jacobian length for \(d=1,3,5,7,9\). Its output ends with `FANO_FERMAT_CHAR2_GENERAL_IDENTITIES_AND_FIVE_EXACT_INSTANCES_PASS`. **The theorem for all odd \(d\) follows from the symbolic identities and the proofs above, not from testing five degrees.**

## Relationship to prior work

Dimca, Ilardi, Pokora, and Sticlaru, *Construction of free curves by adding lines to a given curve*, Theorem 1.7 (first public version January 3, 2023), introduce precisely this Fermat-plus-flex-tangents-and-axes equation and prove its freeness with balanced exponents over the complex numbers; their proof also determines the complex singularity basket and Tjurina number. Those statements are prior results, not part of the novelty claim. The construction is related to the classical Fermat-type line arrangements collected by Szpond; Toft and Moe subsequently investigate other Fermat osculation arrangements over the complex numbers. The present statement instead gives an explicit characteristic-two logarithmic basis and computes the changed exponents and complete singularities. A mathematical-literature search found no covering published positive-characteristic specialization, although exhaustive historical priority is not established.

## Limitations

The result is specific to characteristic \(2\) and odd \(d\), and does not assert a universal reduction classification in other characteristics or for even degrees. The equality of the divisor polynomials across characteristics does not give a flat relative Jacobian scheme. The statement is a proof and direct computational cross-check, not an independent external validation; an earlier equivalent calculation might exist in unindexed literature.

## References

1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117, first version January 3, 2023, Theorem 1.7 and Section 4 (Results in Mathematics 79, 11, 2024).
2. J. Szpond, *Fermat-type arrangements*, arXiv:1909.04089, Section 1 (2019).
3. N. P. A. Toft and T. K. Moe, *The Fermat curves and arrangements of lines and conics*, arXiv:2412.16993, Sections 1--2 (2024); contextual later work on distinct osculation arrangements.
