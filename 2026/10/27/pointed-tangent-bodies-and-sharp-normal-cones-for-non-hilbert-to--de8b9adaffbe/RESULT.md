# Pointed tangent bodies and sharp normal cones for non-Hilbert Toeplitz numerical ranges

## Finding
For \(1<p<\infty\), \(p\ne2\), let \(T_p=S_R+S_L\) on the complex sequence space \(\ell_p(\mathbb N_0)\), and let \(W_e(T_p)\) be its essential numerical range. Put \(\delta_p=|1-2/p|\in(0,1)\) and form the intrinsically transversely normalized body
\[
  \mathcal K_p=\bigl\{(\Re z,\Im z/(2\delta_p)):z\in W_e(T_p)\bigr\}\subset\mathbb R^2.
\]
The family has the **exact** conjugate-exponent symmetry \(\mathcal K_p=\mathcal K_q\), where \(q=p/(p-1)\). Each \(\mathcal K_p\) has extreme horizontal endpoints \((\pm2,0)\), and the complete set of supporting normal vectors at \((2,0)\) is the sharp cone
\[
  \bigl\{(a,b):a\ge0,\ |b|\le 2a\sqrt{1-\delta_p^2}\bigr\};
\]
its negative is the corresponding normal cone at \((-2,0)\).

As \(p\to2\) from **either** side, these normalized numerical ranges converge in Euclidean Hausdorff distance to the same compact convex body
\[
  \mathcal K_0=\operatorname{conv}\!\left\{
  \left(\frac{2\cos\theta}{\cosh v},\frac{v\sin\theta}{\cosh v}\right):
  v\ge0,\ \theta\in[0,2\pi]\right\}.
\]
The convergence has **sharp quadratic order**: for all sufficiently small \(\delta_p\),
\[
  c\delta_p^2\le d_H(\mathcal K_p,\mathcal K_0)\le C\delta_p^2
\]
with fixed constants \(0<c<C<\infty\). The limiting support function is exactly
\[
  h_0(a,b)=\max_{v\ge0}\frac{\sqrt{4a^2+b^2v^2}}{\cosh v}.
\]
For nonzero normals with \(|b|\le2|a|\), the maximum is uniquely at \(v=0\) and equals \(2|a|\); for \(|b|>2|a|\) it is uniquely at a positive \(v\) characterized by
\[
  v\coth v-v^2=\frac{4a^2}{b^2}.
\]
The limiting normal cone at \((2,0)\) is therefore \(a\ge0\), \(|b|\le2a\). Its vertical half-width is \(v_*/\cosh v_*\), where \(v_*\tanh v_*=1\), numerically \(0.66274341934918\ldots\).

## Assumptions and scope
All numerical ranges are spatial or essential numerical ranges of bounded complex-linear operators on \(\ell_p\). The essential numerical range uses the standard Banach-space definition. The theorem applies to the symmetric unilateral tridiagonal Toeplitz operator \(S_R+S_L\), not arbitrary unequal off-diagonal Toeplitz coefficients. Hausdorff distance refers to the ordinary Euclidean metric on compact planar sets. A supporting normal at \((2,0)\) is a vector \((a,b)\) satisfying \(ax+by\le2a\) for all \((x,y)\) in the body; the zero normal is included. The limit \(p\to2\) always excludes \(p=2\), where the unnormalized essential range is the segment \([-2,2]\).

## Proof
**1. Exact ellipse parametrization.** Theorem 4.5 of Müller–Tomilov [1] gives the essential numerical range as twice the convex hull of
\[
 \bigl\{r s^{p-1}e^{i\theta}+s r^{p-1}e^{-i\theta}:r,s\ge0,\ r^p+s^p=1,\ \theta\in[0,2\pi]\bigr\}.
\]
Changing the sign of \(\theta\) or exchanging \(r,s\) does not change the resulting convex set. Parameterize positive \(r,s\) by
\[
 r=\frac{e^{v/p}}{(2\cosh v)^{1/p}},\quad
 s=\frac{e^{-v/p}}{(2\cosh v)^{1/p}},\qquad v\in\mathbb R.
\]
Taking \(v\ge0\) suffices by symmetry. After applying the vertical scaling in the definition of \(\mathcal K_p\), each parameter produces the axis-aligned ellipse
\[
 \left(\frac{2\cosh(\delta_p v)}{\cosh v}\cos\theta,
       \frac{\sinh(\delta_p v)}{\delta_p\cosh v}\sin\theta\right).
 \tag{1}
\]
The missing cases \(r=0\) or \(s=0\) contribute the origin, also a limit as \(v\to\infty\). Thus \(\mathcal K_p\) is precisely the closed convex hull of (1). Its formula depends on \(p\) only through \(\delta_p\); since \(\delta_q=\delta_p\), exact conjugate-exponent symmetry follows.

**2. Sharp finite-\(p\) endpoint cones.** For \((a,b)\in\mathbb R^2\), the support value is
\[
 h_p(a,b)=\sup_{v\ge0}\frac{\sqrt{4a^2\cosh^2(\delta_p v)+b^2\sinh^2(\delta_p v)/\delta_p^2}}{\cosh v}.
 \tag{2}
\]
At \(v=0\) this is \(2|a|\). Assume \(a>0\). The condition that every other ellipse contributes at most \(2a\) is equivalent to
\[
 \frac{b^2}{4a^2}\frac{\sinh^2(\delta_p v)}{\delta_p^2}
 \le\sinh^2 v-\sinh^2(\delta_p v),\qquad v>0.
 \tag{3}
\]
Since \(\sinh t/t\) is strictly increasing on \(t>0\),
\(\sinh v>\sinh(\delta_p v)/\delta_p\) for every \(v>0\). Hence (3) holds strictly for all \(v>0\) whenever \(b^2\le4a^2(1-\delta_p^2)\). Conversely, the coefficient of \(v^2\) in the **square of the numerator in (2) minus** \(4a^2\cosh^2v\) is \(b^2-4a^2(1-\delta_p^2)\). If this is positive, sufficiently small positive \(v\) makes (2) strictly greater than \(2a\). At \(a=0\), only the zero normal supports at the right endpoint. This proves the exact normal cone; central symmetry gives the left endpoint.

**3. Uniform singular limit and its sharp rate.** For \(\delta=\delta_p\) with \(0<\delta\le1/2\), the generating ellipse coordinates from (1) converge uniformly over \(v\ge0\) and \(\theta\) to those in the claimed limit. Explicitly, using \(\cosh x-1\le x^2 e^x/2\) and \(0\le\sinh x-x\le x^3 e^x/6\),
\[
 \left|\frac{2\cosh(\delta v)}{\cosh v}-\frac2{\cosh v}\right|
 \le\delta^2\frac{v^2 e^{\delta v}}{\cosh v},\qquad
 \left|\frac{\sinh(\delta v)}{\delta\cosh v}-\frac v{\cosh v}\right|
 \le\frac{\delta^2 v^3e^{\delta v}}{6\cosh v}.
\]
The right-hand sides are bounded uniformly by constants times \(\delta^2\), since \(e^{v/2}/\cosh v\) decays exponentially. Hausdorff distance between convex hulls is no greater than the uniform displacement of their generating families, giving the stated upper bound.

For the lower bound let \(v_*>0\) be the unique root of \(v\tanh v=1\), whose uniqueness follows because \(v\mapsto v\tanh v\) increases strictly from zero to infinity. The highest vertical coordinate of \(\mathcal K_0\) is \(v_*/\cosh v_*\). The ellipse in (1) with \(v=v_*\) contains the vertical point whose ordinate is \(\sinh(\delta v_*)/(\delta\cosh v_*)\); its excess above the limiting height is
\[
 \frac{\sinh(\delta v_*)/\delta-v_*}{\cosh v_*}
 =\frac{v_*^3}{6\cosh v_*}\delta^2+O(\delta^4)>0.
\]
The Euclidean distance from this point to \(\mathcal K_0\) is at least its vertical excess. Therefore the quadratic order is sharp.

**4. Limiting support phase transition.** Maximization over the ellipse angle yields the claimed support formula. When \(a=0,b\ne0\), it reduces to maximization of \(v/\cosh v\), whose unique positive optimizer satisfies \(v\tanh v=1\). If \(b=0,a\ne0\), the maximum is uniquely at zero. Otherwise write \(r=2|a|/|b|\). For \(v>0\) the logarithmic derivative of the expression to be maximized has the sign of
\[
 G(v)-r^2,\qquad G(v)=v\coth v-v^2.
\]
Indeed \(G(v)-r^2=\frac{v}{\tanh v}-(v^2+r^2)\). For all positive \(v\), \(G\) is strictly decreasing: its derivative equals
\[
 G'(v)=\frac{\frac12\sinh(2v)-v\cosh(2v)}{\sinh^2v}<0,
\]
because \(\tanh(2v)<2v\). Furthermore \(G(0+)=1\) and \(G(v)\to-\infty\). If \(r\ge1\) the maximum is uniquely at zero; if \(0\le r<1\) there is a unique positive critical point and it is the global maximum. This proves the threshold, uniqueness, and the vertical half-width. The zero normal, excluded from uniqueness claims, has zero support on every point.

## Verification
The accompanying standard-library `verification.py` checks the exact hyperbolic reparameterization against direct \(r,s\) calculations, finite-exponent support-cone thresholds, limiting support maximizers, convergence for exponents on either side of two, and the vertical critical-root value. It reports 203 finite numerical checks passing. These computations are corroborative only; the infinite-dimensional essential-range identity is credited to [1], and all singular-limit, normal-cone, and sharp-rate conclusions above are analytic.

## Relationship to prior work
Müller–Tomilov [1], Theorem 4.5, provides the **complete unnormalized essential numerical range** of the symmetric Toeplitz example, while Corollary 4.6 identifies its horizontal and vertical extremal coordinates. Those are indispensable starting facts, not new contributions here. The new result extracts a conjugate-invariant singularly normalized convex body, classifies its supporting-normal phase transition, and proves both the finite-exponent endpoint cones and the sharp quadratic convergence rate. Their exact formula logically determines these quantities after further analysis; no claim of independent determination of the original numerical range is made. Mandal–Bhanja–Bag–Paul [2] study ordinary numerical ranges and transpose duality on finite-dimensional \(\ell_p^2\), rather than the essential Toeplitz limit geometry. No general result concerning arbitrary asymmetric Toeplitz coefficients is claimed.

## Limitations
The conclusion concerns one symmetric Toeplitz family. Equality of conjugate-exponent normalized sets is special to this family and chosen normalization. The endpoint-cone formula does not assert uniqueness of all non-endpoint maximizing ellipses at fixed \(p\). The rate \(\Theta(\delta_p^2)\) does not identify the global leading coefficient of the Hausdorff distance. Bibliographic priority beyond the inspected and searched literature is not independently certified.

## References
[1] V. Müller and Yu. Tomilov, *Numerical and essential numerical ranges on \(\ell_p\)*, arXiv:2606.22693v1, publicly available 2026-06-21, especially Theorem 4.5 and Corollary 4.6. https://arxiv.org/abs/2606.22693

[2] K. Mandal, A. Bhanja, S. Bag, and K. Paul, *On the numerical range of operators on some special Banach spaces*, arXiv:2005.01288v1, 2020, published in Journal of Convex Analysis 29 (2022), 371–380. https://arxiv.org/abs/2005.01288
