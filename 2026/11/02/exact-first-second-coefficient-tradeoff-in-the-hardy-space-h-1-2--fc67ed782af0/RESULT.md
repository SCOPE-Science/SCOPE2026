# Exact first--second coefficient tradeoff in the Hardy space \(H^{1/2}\)

## Finding

Write \(f(z)=\sum_{j\geq0}a_j(f)z^j\), and define, for every real \(\lambda>0\),
\[
 C(\lambda)=\sup\left\{\left|a_1(f)+\lambda a_2(f)\right|:\ f\in H^{1/2}(\mathbb D),\ \|f\|_{H^{1/2}}\leq1\right\}.
\]
Here \(H^{1/2}\) is equipped with the conventional quasi-norm
\[\|f\|_{H^{1/2}}=\left(\int_0^{2\pi}|f(e^{it})|^{1/2}\frac{dt}{2\pi}\right)^2.\]
For each \(\lambda>0\), let \(u_\lambda\) be the **unique positive root** of
\[
9\lambda^2u^4+12\lambda u^3+(3-6\lambda^2)u^2-6\lambda u-1=0
\tag{1}
\]
and set
\[
 v_\lambda=\frac{\lambda u_\lambda}{1+3\lambda u_\lambda},\qquad
 d_\lambda=\sqrt{1+u_\lambda^2+v_\lambda^2}.
\]
Then
\[
\boxed{C(\lambda)=\frac{4u_\lambda+4\lambda v_\lambda+6\lambda u_\lambda^2}
 {(1+u_\lambda^2+v_\lambda^2)^2}.}\tag{2}
\]
All equality cases are the functions
\[
\boxed{f(z)=e^{i\phi}\left(\frac{1+u_\lambda z+v_\lambda z^2}{d_\lambda}\right)^4,\quad \phi\in\mathbb R.}\tag{3}
\]
In particular, the maximizing function is unique up to multiplication by a unimodular constant, and its polynomial fourth root has no zeros in the closed unit disk.

The positive root satisfies \(1/\sqrt3<u_\lambda<\sqrt{2/3}\) and \(0<v_\lambda<1/3\). The sharp support curve is real analytic and strictly convex on \((0,\infty)\), with
\[
\lim_{\lambda\downarrow0}C(\lambda)=\frac{3\sqrt3}{4},\quad
\lim_{\lambda\downarrow0}C'(\lambda)=\frac98,\quad
\lim_{\lambda\to\infty}\frac{C(\lambda)}\lambda=\frac{27}{16}.
\]
Writing \(D=1+u_\lambda^2+v_\lambda^2\), its exposed coefficient pair is
\[
\big(a_1(f_\lambda),a_2(f_\lambda)\big)
=\left(\frac{4u_\lambda}{D^2},\frac{4v_\lambda+6u_\lambda^2}{D^2}\right),
\quad C'(\lambda)=a_2(f_\lambda).
\]
Thus the theorem gives the complete family of positively supported simultaneous first--second coefficient extremals, not just the separate sharp bounds for each coefficient.

## Assumptions and scope

The parameter \(\lambda\) is any fixed positive real number. Every competing function belongs to the classical complex analytic Hardy space on the unit disk. The assertion does not concern mixed coefficient functionals of orders greater than two, other Hardy exponents, or negative/complex values of \(\lambda\).

## Proof

**Existence and outer reduction.** Each coefficient functional is bounded on \(H^{1/2}\). A maximizing sequence in the unit ball has a locally uniformly convergent subsequence by Hardy-space coefficient bounds and normal-family compactness. Fatou's lemma puts its limit in the unit ball; the limit attains the norm and has unit quasi-norm by homogeneity. The outer-extremal theorem of Brevig--Søvik [1, Theorem 1] implies that every extremizer for this nonzero bounded linear functional is outer. Thus it has a single-valued analytic fourth root \(g\in H^2\), with \(f=g^4\) and \(\|g\|_2=1\).

**Exact finite-dimensional reduction.** Let \(g(z)=b_0+b_1z+b_2z^2+\cdots\). Direct coefficient multiplication gives
\[
 a_1=4b_0^3b_1,\qquad a_2=4b_0^3b_2+6b_0^2b_1^2.
\]
Set \(x=|b_0|\), \(y=|b_1|\), \(z=|b_2|\); Parseval gives \(x^2+y^2+z^2\leq1\). Hence
\[
 |a_1+\lambda a_2|\leq4x^3y+4\lambda x^3z+6\lambda x^2y^2.
\tag{4}
\]
The right side is homogeneous of degree four. Its positive maximum occurs on the first-octant unit sphere. The maximum cannot have \(x=0\) (where the objective vanishes), \(y=0\) (a small positive \(y\) increases it to first order), or \(z=0\) (a small positive \(z\) increases it to first order). Thus \(x,y,z>0\), and higher coefficients of \(g\) necessarily vanish at equality.

**Critical equation and unique global maximum.** With \(u=y/x>0\), \(v=z/x>0\), the objective becomes
\[
 F_\lambda(u,v)=\frac{4u+4\lambda v+6\lambda u^2}{(1+u^2+v^2)^2}.
\]
Lagrange multiplier equations (or direct differentiation) imply
\[
 v(1+3\lambda u)=\lambda u.
\tag{5}
\]
Substituting (5) into the remaining equation and clearing positive denominators gives exactly (1). By Descartes' rule, its coefficient sequence in descending degree has exactly one sign change, irrespective of the sign of \(3-6\lambda^2\), so (1) has precisely one positive root counted with multiplicity. Moreover its left side at \(u=1/\sqrt3\) equals \(-\lambda^2-2\lambda/\sqrt3<0\), and at \(u=\sqrt{2/3}\) equals \(1+(2\sqrt6/3)\lambda>0\). Therefore this unique stationary point is the global maximum, and equations (2) and (3) follow from (4).

**Attainment, zero-free factor and equality rigidity.** The polynomial \(P(z)=1+u_\lambda z+v_\lambda z^2\) has no zero in \(|z|\leq1\): indeed \(0<v_\lambda<1\) and \(0<u_\lambda<1\). During the deformation \(P_t(z)=1+t u_\lambda z+v_\lambda z^2\), \(0\leq t\leq1\), a boundary zero would give, after division by \(z=e^{i\theta}\), the equation \(e^{-i\theta}+t u_\lambda+v_\lambda e^{i\theta}=0\). Its imaginary part forces \(\sin\theta=0\), while its real part is nonzero at both \(z=1\) and \(z=-1\) because \(t u_\lambda<1+v_\lambda\). Since \(P_0\) is zero-free in the closed disk, so is \(P_1\). Thus the function (3) is outer and \(\|f\|_{H^{1/2}}=\|P/d_\lambda\|_2^4=1\), proving sharpness. Equality in (4), with all three positive terms, forces the phases of \(b_0^3b_1\), \(b_0^3b_2\) and \(b_0^2b_1^2\) to coincide. Making \(b_0\) real positive forces \(b_1,b_2\) positive; hence only the common unimodular multiplier in (3) remains.

**Dependence on the weight.** The unique positive root in (1) is simple, hence analytically depends on \(\lambda\) by the implicit-function theorem. The envelope identity gives the displayed expression for \(C'(\lambda)\). Convexity follows from \(C(\lambda)=\sup_{\|f\|\leq1,\phi\in\mathbb R}\operatorname{Re}[e^{-i\phi}(a_1(f)+\lambda a_2(f))]\), a supremum of affine functions of \(\lambda\). It is strict: if \(C\) were affine on any nontrivial interval, a maximizing function at an interior weight would attain both endpoint norms. But an extremizer fixes \(u,v\), and (5) determines its weight uniquely, namely \(\lambda=v/(u(1-3v))\); two distinct weights cannot share one extremizer.

As \(\lambda\downarrow0\), equation (1) gives \(u\to1/\sqrt3\) and (5) gives \(v\to0\). The limiting first and second coefficients are \(3\sqrt3/4\) and \(9/8\). Dividing (1) by \(\lambda^2\) as \(\lambda\to\infty\) yields \(u\to\sqrt{2/3}\), and (5) then gives \(v\to1/3\); the second coefficient tends to \(27/16\). All stated limits follow.

## Verification

`CHECK.py` is a standalone supplementary checker. It symbolically verifies the stationarity reduction, exact critical-polynomial identities and endpoint evaluations, and numerically compares several finite-parameter optimizer values against independent constrained optimization. It also checks norm normalization and the endpoint coefficient constants. The numerical tests are illustrative only: positivity, uniqueness, zero-freeness, and strict convexity for every \(\lambda>0\) are proved above, not inferred from sampling.

## Relationship to prior work

Brevig and Søvik [1] prove that every extremizer of a bounded linear functional on \(H^p\), \(0<p<1\), is outer, but do not compute the present mixed functional. Brevig and Saksman [2] compute the individual sharp first and second coefficients, and provide a general finite-degree extremal structure theorem; their exact single-coefficient results do not determine the sharp one-parameter joint support curve or its unique off-endpoint equality cases. Brevig, Grepstad and Instanes [3] study a fixed zeroth coefficient and one later coefficient, rather than the simultaneous free first--second coefficient functional here. General Carathéodory--Fejér-type structural results reduce admissible extremals to finite polynomial factors but do not state the polynomial root and full support profile (1)--(3).

## Limitations

Only real positive weights and the exponent \(1/2\) are covered. The result describes positive supporting directions of the first--second coefficient body, not every point of that body. Its novelty assessment is relative to the cited inspected literature and accessible research records; an earlier equivalent unindexed mixed-coefficient calculation cannot be excluded. Independent mathematical audit has not been performed.

## References

[1] O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, first posted 2026-10-15, arXiv:2610.21788, https://arxiv.org/abs/2610.21788.

[2] O. F. Brevig and E. Saksman, *Coefficient estimates for \(H^p\) spaces with \(0<p<1\)*, first posted 2019-05-23, arXiv:1905.09547, https://arxiv.org/abs/1905.09547.

[3] O. F. Brevig, S. Grepstad and S. M. Instanes, *F. Wiener's Trick and an Extremal Problem for \(H^p\)*, first published 2022-09-12, Computational Methods and Function Theory 23 (2023), 697--722, https://doi.org/10.1007/s40315-022-00469-x.
