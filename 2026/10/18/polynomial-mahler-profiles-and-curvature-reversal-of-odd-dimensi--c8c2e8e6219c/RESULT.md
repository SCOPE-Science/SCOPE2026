# Polynomial Mahler profiles and curvature reversal of odd-dimensional capsules

## Finding
For every integer \(m\ge1\), the Mahler product of the origin-symmetric Euclidean capsule \(C_a=B_2^{2m+1}+[-a,a]e_1\), with \(a\ge0\), is an explicitly computable polynomial in the natural relative segment fraction \(b=a/(1+a)\). Write \(d=2m+1\), \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), and
\[
\beta_m=\frac{2\kappa_{2m}}{\kappa_{2m+1}}=\frac{(2m+1)\binom{2m}{m}}{4^m}.
\]
Then the normalized Mahler product \(R_m(b)=\operatorname{Vol}_d(C_a)\operatorname{Vol}_d(C_a^\circ)/\kappa_d^2\) is the **degree-\(m+1\) polynomial**
\[
R_m(b)=\beta_m\bigl(1+(\beta_m-1)b\bigr)
\sum_{j=0}^{m}\binom mj\frac{j!m!}{(m+j+1)!}(1-2b)^j,\quad 0\le b<1.
\]
Its polynomial continuation to \(b=1\) represents the long-capsule limit. Its curvature obeys the exact endpoint identities
\[
R_m''(0)=-2\bigl(\beta_m^2-(m+1)\bigr)<0,
\qquad
R_m''(1)=\frac{2\beta_m}{2m+1}\left(1-\frac{\beta_m}{2m-1}\right).
\]
Thus \(R_1(b)=1-b^2/4\) is strictly concave, while for **every odd dimension \(d\ge5\)** the profile is strictly concave near \(b=0\), strictly convex near \(b=1\), and has **at least one** interior inflection point. No uniqueness of the inflection is asserted. Its endpoint value is \(R_m(1)=\beta_m^2/(2m+1)\) and endpoint derivative is \(R_m'(1)=-\beta_m/(2m+1)\).

## Assumptions and scope
The Euclidean unit ball is \(B_2^d=\{x\in\mathbb R^d:\|x\|_2\le1\}\). The centrally symmetric capsule \(C_a\) is its Minkowski sum with a segment of half-length \(a\) parallel to the first coordinate axis. The polar is taken about the origin, which is its Santaló point by symmetry. The natural bounded geometric parameter \(b=a/(1+a)\) measures the segment half-length as a fraction of the body's axial half-length. The formulas cover all integers \(m\ge1\) and all \(a\ge0\), and limits as \(b\uparrow1\). The statement about curvature is for derivatives with respect to this explicitly fixed \(b\), not arbitrary reparametrizations.

## Proof
The axial sections of the capsule consist of a cylinder of length \(2a\) with two hemispherical caps, so \(\operatorname{Vol}_d(C_a)=\kappa_d+2a\kappa_{d-1}\). Its support function is \(h_{C_a}(u)=\|u\|_2+a|u_1|\). Therefore its polar is \(\{x:\|x\|_2+a|x_1|\le1\}\). On the positive axial half, the section at \(x_1=z\) is a \((d-1)\)-ball of squared radius \((1-az)^2-z^2\); here \(0\le z\le1/(1+a)\). Because \(d-1=2m\), its volume is a polynomial in that squared radius. Hence
\[
\operatorname{Vol}_d(C_a^\circ)=2\kappa_{2m}\int_0^{1/(1+a)}\bigl((1-az)^2-z^2\bigr)^m\,dz.
\]
Putting \(b=a/(1+a)\), \(z=(1-b)s\), the integrand becomes \(\bigl((1-s)(1+(1-2b)s)\bigr)^m\). Multiplication by \(\kappa_d+2a\kappa_{2m}\) yields
\[
R_m(b)=\beta_m\bigl(1+(\beta_m-1)b\bigr)J_m(b),\quad
J_m(b)=\int_0^1(1-s)^m(1+(1-2b)s)^m\,ds.
\]
The beta-integral \(\int_0^1s^j(1-s)^m\,ds=j!m!/(j+m+1)!\) gives the claimed finite sum. At \(b=0\), the duplication formula for \(\Gamma\) shows \(J_m(0)=1/\beta_m\). Differentiation under this polynomial integral and elementary beta integrals give
\[
J_m'(0)=J_m(0)-1,\quad R_m'(0)=0,\quad
R_m''(0)=-2\bigl(\beta_m^2-m-1\bigr).
\]
At \(b=1\), \(J_m(1)=1/(2m+1)\), \(J_m'(1)=-1/(2m+1)\), and
\[
J_m''(1)=\frac{4(m-1)}{(2m-1)(2m+1)},
\]
where the displayed identity also holds when \(m=1\). Substituting in the product formula yields the stated endpoint value, slope, and second derivative.

For strict signs, put \(\beta_1=3/2\) and note
\[
\frac{\beta_{m+1}}{\beta_m}=\frac{2m+3}{2m+2},\qquad
\left(\frac{2m+3}{2m+2}\right)^2>\frac{m+2}{m+1}.
\]
Induction from \(\beta_1^2=9/4>2\) proves \(\beta_m^2>m+1\) for all \(m\ge1\). Also \(\beta_2=15/8<3\) and \((2m+3)/(2m+2)<(2m+1)/(2m-1)\) for \(m\ge2\), so induction gives \(\beta_m<2m-1\) for every \(m\ge2\). Thus \(R_m''(0)<0<R_m''(1)\) when \(m\ge2\). Since \(R_m''\) is a continuous polynomial, it has an interior zero at which the concavity changes somewhere between the endpoint neighborhoods. For \(m=1\), substitution gives the exact quadratic \(1-b^2/4\), whose second derivative is negative everywhere.

## Verification
The standalone `verify.py` constructs \(R_m\) from rational factorial/beta coefficients, checks the endpoint identities, and independently evaluates the original polar-section integral for rational \(a\). It checks \(m=1,\dots,10\) and several values of \(a\). Those computations validate examples but are **not** substitutes for the preceding proof for all \(m\).

## Relationship to prior work
Campi and Gronchi (2006) proved that reciprocal polar volume is convex along origin-symmetric shadow systems; Meyer and Reisner (2006) extended the result. Their theory already covers the shadow-system framework containing capsule elongations and provides broad qualitative inequalities. **No new monotonicity theorem for the capsule Mahler product is claimed.** The contribution assessed here is the explicit complete odd-dimensional polynomial profile and the dimension-dependent sign reversal of its curvature in the geometrically normalized parameter \(b\); neither follows as a stated formula or curvature assertion from the inspected general convexity theorems. The classical Blaschke–Santaló inequality covers the fact that the ball maximizes the volume product, not the curvature transition.

## Limitations
The result is restricted to **odd** dimensions; it does not classify inflection-point counts or positions beyond existence, nor assert a novel capsule monotonicity result. Curvature depends on parametrization and is asserted only for \(b\). Unindexed prior exact evaluations or alternative descriptions of this natural profile may exist; the literature comparison does not establish absolute historical priority. Independent external scientific audit has not been performed.

## References
- S. Campi and P. Gronchi, *On volume product inequalities for convex sets*, Proceedings of the American Mathematical Society, 2006, DOI: 10.1090/S0002-9939-06-08241-4. Full-text author copy: https://www3.diism.unisi.it/~campi/files/lavori/Volumeproduct.pdf .
- M. Meyer and S. Reisner, *Shadow systems and volumes of polar convex bodies*, Mathematika 53 (2006), arXiv:math/0606305, first public preprint 2006-06-13: https://arxiv.org/html/math/0606305v2 .
