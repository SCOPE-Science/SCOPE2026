# Sharp cubic Runge–Kutta contraction frontier and an identity-step resonance

## Finding

Consider the explicit three-stage second-order Runge–Kutta family with stability polynomial
\[
R_\beta(z)=1+z+\frac{z^2}{2}+\beta z^3,\qquad 0\le\beta\le\tfrac12.
\]
For all \(a,b>0\), let
\[
L_{a,b}=\begin{pmatrix}0&-a\\a&-b\end{pmatrix},\qquad
D_{\beta,a,b}(h)=R_\beta(hL_{a,b})^{\mathsf T}R_\beta(hL_{a,b})-I.
\]
Every \(L_{a,b}\) is asymptotically stable and semi-dissipative. The following is a sharp **pointwise small-step Euclidean contraction classification** (the small-step threshold may depend on the fixed parameters):

1. For \(\beta<\tfrac14\), \(D_{\beta,a,b}(h)\prec0\) for all sufficiently small \(h>0\), for every \(a,b>0\).
2. For \(\beta>\tfrac14\), \(D_{\beta,a,b}(h)\) is indefinite for all sufficiently small \(h>0\), for every \(a,b>0\).
3. At \(\beta=\tfrac14\), \(D_{\beta,a,b}(h)\prec0\) for all sufficiently small \(h>0\) exactly when \(b\le a\); when \(b>a\) it is indefinite for all sufficiently small \(h>0\).

The borderline has two additional exact phenomena. For \(\beta=\tfrac14\) and \(a=b\), *every* nonzero vector contracts strictly when \(0<ah<2\), the update is **exactly the identity** at \(ah=2\), and *every* nonzero vector expands strictly when \(ah>2\). For \(a=1\), \(b=11/10\), \(\beta=1/4\), all sufficiently small steps admit expanding vectors, yet at \(h=1\) every nonzero vector contracts strictly. All sufficiently large steps expand every nonzero vector. Thus a strictly contractive step interval exists away from both zero and infinity.

## Assumptions and scope

All matrices are real \(2\times2\), \(a,b>0\), the Euclidean matrix norm is induced by the standard inner product, and one step acts on the homogeneous autonomous linear equation \(u'=L_{a,b}u\). The three-stage algorithm is
\[
\begin{aligned}
 k_1&=f(u),& k_2&=f(u+hk_1),& k_3&=f(u+hk_2),\\
 u^+&=u+h\left(\tfrac12 k_1+(\tfrac12-\beta)k_2+\beta k_3\right).
\end{aligned}
\]
The weights sum to one and their moment against stage abscissae \((0,1,1)\) equals one half, so this is second order for general sufficiently smooth nonlinear vector fields. Substitution of \(f(u)=Lu\) gives the displayed polynomial. The symmetric part of \(L_{a,b}\) is \(\operatorname{diag}(0,-b)\), while its characteristic polynomial is \(\lambda^2+b\lambda+a^2\). Thus it is semi-dissipative with both eigenvalues in the open left half-plane.

## Proof

**Small-step determinant criterion.** Direct exact polynomial multiplication gives
\[
\operatorname{tr}D_{\beta,a,b}(h)=-2bh+O_{a,b,\beta}(h^2),
\]
and
\[
\begin{aligned}
\det D_{\beta,a,b}(h)
={}&a^2b^2(1-4\beta)h^4\\
&+\frac{a^2b}{2}(8a^2\beta-a^2-b^2)h^5+O_{a,b,\beta}(h^6).
\end{aligned}
\]
For a real symmetric \(2\times2\) matrix, negative determinant means indefinite; positive determinant together with negative trace means negative definite. For \(\beta\ne1/4\), the \(h^4\)-coefficient determines the sign and proves assertions 1–2. At \(\beta=1/4\), the \(h^5\)-coefficient is \(a^2b(a^2-b^2)/2\). This proves assertion 3 when \(a\ne b\); the equality case is included in the full calculation below.

**Exact equal-rate resonance.** Put \(a=b>0\), \(\beta=1/4\), and \(x=ah\). Then the exact update is
\[
R_{1/4}(hL_{a,a})=
\begin{pmatrix}
 (x^3-2x^2+4)/4&x(x-2)/2\\
 -x(x-2)/2&(x^3-4x+4)/4
\end{pmatrix}.
\]
It equals \(I\) at \(x=2\). Its squared-norm defect has the exact invariants
\[
\operatorname{tr}D=
\frac{x(x-2)(x^2-2x+2)(x^2+2x+4)}8,
\]
\[
\det D=
\frac{x^6(x-2)^2(x^4+16)}{256}.
\]
The final two quadratic factors in the trace are positive for every real \(x\). For \(x>0\), the determinant is positive except at \(x=2\). Consequently \(D\prec0\) for \(0<x<2\), \(D=0\) for \(x=2\), and \(D\succ0\) for \(x>2\). This also handles \(a=b\) in assertion 3.

**A genuinely reentrant contraction window.** Put \(a=1\), \(b=11/10\), \(\beta=1/4\), \(h=1\). The exact update is
\[
Q=\begin{pmatrix}31/40&-201/400\\201/400&889/4000\end{pmatrix}.
\]
Here
\[
\operatorname{tr}(Q^{\mathsf T}Q-I)
=-\frac{13519479}{16000000}<0,\qquad
\det(Q^{\mathsf T}Q-I)=\frac{1269}{50000}>0.
\]
Hence every nonzero vector strictly contracts at \(h=1\). But \(b>a\) makes the small-step determinant negative, so the smallest steps admit expanding vectors. Finally, \(L_{a,b}\) is invertible, and the leading \(\beta h^3L_{a,b}^3\) term is invertible for \(\beta=1/4\); therefore the smallest singular value of \(R_{1/4}(hL_{a,b})\) tends to infinity as \(h\to\infty\). Thus all sufficiently large steps expand every nonzero vector. Strict matrix inequalities are open in \(h\), giving a bounded nonempty interval of strict contractions disjoint from neighborhoods of zero and infinity.

## Verification

A standalone reproducible script, `verify.py`, uses exact symbolic arithmetic to check the stability polynomial, the first two nonzero coefficients of the determinant, the trace derivative, both full equal-rate factorizations, the exact identity update, and the rational reentrant matrix and certificate. Execute `python verify.py` with SymPy installed. Its exact polynomial identities check universal expressions; no floating-point experiment supplies an infinite-dimensional or all-parameter proof.

## Relationship to prior work

Achleitner, Arnold, and Jüngel (2023), arXiv:2308.05689v1, give general necessary/sufficient criteria for Runge–Kutta strong stability and hypocoercivity-index-dependent results. Their Theorem 0.2.2(b) gives a strict **non-stability** condition which, for \(R_\beta\) above, reads \(\beta>1/4\). The equality case \(\beta=1/4\) lies on the boundary of that published strict condition; their theorem does not give the exact \(b/a\) split, exact identity resonance, or bounded reentrant contraction window established here. Sun and Shu (2018), arXiv:1811.10680v1, develop the underlying energy method and strong-stability conditions for explicit Runge–Kutta integrators, including an even-order sufficient condition, but not these sharp planar equal-coefficient and unequal-coefficient classifications. The related hypocoercivity survey arXiv:2310.19758v1 concerns broader structural mechanisms and truncated-exponential stability functions.

## Limitations

The claimed sharpness is over this three-stage polynomial family on the specified two-dimensional rank-one damped oscillator matrices, not over every explicit Runge–Kutta method or every semi-dissipative matrix. A bound that holds separately for each fixed \(a,b\) need not have a common uniform step threshold over all parameter values. Strict Euclidean contraction is different from spectral-radius stability and from contractivity in a specially chosen weighted norm. The reentrant certificate proves existence of a contractive interval, not a complete count of all such intervals for arbitrary parameters. There is no independent mathematical audit and publication-priority uncertainty remains for unlocated equivalent special-case calculations.

## References

1. F. Achleitner, A. Arnold, and A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge–Kutta methods*, arXiv:2308.05689v1 (first public version 2023-08-10), https://arxiv.org/html/2308.05689v1.
2. Z. Sun and C.-W. Shu, *Strong stability of explicit Runge–Kutta time discretizations*, arXiv:1811.10680v1 (2018), https://arxiv.org/abs/1811.10680.
3. F. Achleitner, A. Arnold, and A. Jüngel, *Hypocoercivity for Linear ODEs and Strong Stability for Runge–Kutta Methods*, arXiv:2310.19758v1 (2023), https://arxiv.org/abs/2310.19758.
