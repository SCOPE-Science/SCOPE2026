# Exact surjectivity margin for two-tail weighted shifts with an arbitrary interface

## Finding
Let \(H=\ell^2(\mathbb Z;\mathbb C)\). Fix real parameters \(0<\alpha<\beta\) and any nonzero complex number \(\kappa\). Define the invertible forward bilateral weighted shift \(T\) on the standard orthonormal basis by
\[
T e_n=w_n e_{n+1},\qquad
w_n=\begin{cases}\beta&n\le-1,\\\kappa&n=0,\\\alpha&n\ge1.\end{cases}
\]
For every \(\lambda\in\mathbb C\) with \(\alpha<|\lambda|<\beta\), set \(B_\lambda=T-\lambda I\) and \(\delta_\lambda=\min\{\beta-|\lambda|,|\lambda|-\alpha\}>0\). Then:

1. \(B_\lambda\) is surjective and has a one-dimensional kernel.
2. Its **exact adjoint minimum modulus** is
\[
\inf_{\|y\|=1}\|B_\lambda^*y\|=\delta_\lambda.
\]
The infimum is never attained by a nonzero vector.
3. Its Moore--Penrose right inverse satisfies \(\|B_\lambda^\dagger\|=1/\delta_\lambda\), and this operator does not attain its norm.
4. Its **exact distance to non-surjectivity** in operator norm is
\[
\inf\{\|E\|:E\in\mathcal B(H),\ B_\lambda+E\text{ is not onto}\}=\delta_\lambda.
\]
The distance is realized by a perturbation that modifies just one *infinite constant-weight tail*. These formulas are independent of the magnitude and phase of the nonzero interface weight \(\kappa\).

## Assumptions and scope
The Hilbert space is complex, \(0<\alpha<\beta\) are arbitrary, \(\kappa\in\mathbb C\setminus\{0\}\), and \(\lambda\) ranges over the **open** annulus \(\alpha<|\lambda|<\beta\). The operator has the forward-shift convention \(T e_n=w_n e_{n+1}\). Neither a statement at either radial endpoint nor a formula for arbitrary nonconstant tails is asserted. The perturbation in the distance formula may have infinite rank, and the distance is measured over all bounded operators.

## Proof
Write \(\lambda=r e^{i\theta}\) with \(r\in(\alpha,\beta)\). The diagonal unitary \(Ue_n=e^{-in\theta}e_n\) obeys \(U^*TU=e^{i\theta}T\), whence \(U^*B_\lambda U=e^{i\theta}(T-rI)\). Thus all norm, kernel, and surjectivity calculations reduce to real positive \(r\), without changing the interface weight.

Write \(B=T-rI\). For a finitely supported vector \(y=(y_n)\), its adjoint is given coordinatewise by \((B^*y)_n=\overline{w_n}y_{n+1}-r y_n\). Direct expansion and index shifts give the following **exact two-tail identities**:
\[
\begin{aligned}
\sum_{n\le-1}|\beta y_{n+1}-r y_n|^2
&=(\beta-r)^2\sum_{n\le-1}|y_n|^2
+\beta(\beta-r)|y_0|^2
+r\beta\sum_{n\le-1}|y_{n+1}-y_n|^2,\\
\sum_{n\ge1}|\alpha y_{n+1}-r y_n|^2
&=(r-\alpha)^2\sum_{n\ge2}|y_n|^2
+r(r-\alpha)|y_1|^2
+r\alpha\sum_{n\ge1}|y_{n+1}-y_n|^2.
\end{aligned}
\]
The one missing summand is the nonnegative interface expression \(|\overline\kappa y_1-r y_0|^2\). Since
\[
\beta(\beta-r)>(\beta-r)^2\ge\delta_r^2,
\qquad r(r-\alpha)>(r-\alpha)^2\ge\delta_r^2,
\]
adding the three expressions gives \(\|B^*y\|^2\ge\delta_r^2\|y\|^2\). The identity and bound extend by density to all \(\ell^2\) vectors. Equality would force the two discrete gradients to vanish, hence both tails to be constant and therefore zero in \(\ell^2\); equality occurs only at \(y=0\).

For the reverse inequality, place a normalized constant vector on a run of \(L\) coordinates entirely within either constant-weight tail, far from the interface. Its squared adjoint norm is exactly
\[
(\beta-r)^2+\frac{2r\beta}{L}\quad\text{on the left},\qquad
(r-\alpha)^2+\frac{2r\alpha}{L}\quad\text{on the right}.
\]
Letting \(L\to\infty\) proves that the best lower bound is \(\delta_r\), and that it is not attained by a unit vector.

The lower bound makes \(B^*\) injective with closed range. By the closed-range theorem, \(\operatorname{ran}B\) is closed; by \(\operatorname{ran}B^\perp=\ker B^*=\{0\}\), it is also dense, hence all of \(H\). Solving \(Bx=0\) gives, with \(x_0=1\),
\[
x_{-m}=(r/\beta)^m\ (m\ge1),\qquad
x_n=(\kappa/r)(\alpha/r)^{n-1}\ (n\ge1).
\]
Both tails lie in \(\ell^2\); every solution is a multiple of this vector. The general complex-\(\lambda\) eigenvector follows by the unitary reduction. This proves surjectivity and one-dimensional kernel.

For a surjective Hilbert-space operator, \(B^\dagger=B^*(BB^*)^{-1}\) and \((B^\dagger)^*B^\dagger=(BB^*)^{-1}\). The proven spectral lower bound and the tail test vectors imply \(\inf\sigma(BB^*)=\delta_r^2\), so \(\|B^\dagger\|=1/\delta_r\). A norm-attaining vector for \(B^\dagger\) would be a top eigenvector of \((BB^*)^{-1}\), hence a bottom eigenvector of \(BB^*\), contradicting strictness of the lower bound. Thus norm attainment fails.

If \(\|E\|<\delta_r\), then \(\|(B+E)^*y\|\ge(\delta_r-\|E\|)\|y\|\), and the same closed-range argument shows that \(B+E\) remains onto. Conversely, if \(\delta_r=\beta-r\), change **all** weights on the left constant tail from \(\beta\) to \(r\); if \(\delta_r=r-\alpha\), change all weights on the right tail from \(\alpha\) to \(r\). The corresponding weighted-shift perturbation has norm exactly \(\delta_r\). Its adjoint admits normalized long, phase-adjusted constant blocks with norm tending to zero (on the modified tail, its constant-weight modulus equals \(|\lambda|\)), so it is not bounded below; hence the perturbed operator is not onto. This proves the exact distance and attainment.

## Verification
The accompanying `verify_gap.py` uses exact rational complex arithmetic to check both telescoping identities and the lower bound on 700 sampled finitely supported vectors, plus 500 independent pairs of exact tail-block Rayleigh quotient identities: **3,100 asserted finite identities and inequalities**. Execute `python verify_gap.py` with a standard Python interpreter. The checker is only a finite consistency check. Density, nonattainment, infinite-tail sharpness, closed range, and perturbation attainment are proved above and are not inferred from the code.

## Relationship to prior work
Messaoudi, Tofanin Neto, Saavedra, and Tsokanos (arXiv:2608.17021) obtain qualitative relationships among generalized hyperbolicity, surjective spectrum, stability, and shadowing. Pituk (arXiv:2511.12272, especially Example 1.8 and Proposition 2.1) gives the qualitative spectral/shadowing characterization and a classical two-constant-tail model associated with Eisenberg and Hedlund. Bayart (arXiv:2101.02989) studies qualitative weighted-shift dynamical properties. The elementary closed-range and Moore--Penrose facts are standard. The present contribution is the explicit **defect-independent exact adjoint lower modulus and operator-norm surjectivity distance**, including their nonattainment/attainment dichotomy and the variable complex interface; no novelty is attributed to qualitative existence of nonhyperbolic shifts with shadowing.

In particular, when \(\alpha<1<\beta\), the entire unit circle consists of eigenvalues of \(T\) although \(T-\lambda I\) is surjective there, with sharp surjectivity margin \(\min\{\beta-1,1-\alpha\}\). This gives a quantitative refinement of the classical qualitative example, not a new shadowing criterion.

## Limitations
The result concerns exactly two constant tails joined by one arbitrary nonzero interface link. It does not determine quantitative shadowing constants (as opposed to surjectivity margins), does not cover multiple uncontrolled interface links, and makes no endpoint claims. The originality comparison is best-knowledge only: an older general Jacobi-operator factorization or Toeplitz/Fredholm result might imply a version of the estimate. Independent verification and a definitive publication-priority determination have not been performed.

## References
1. A. Messaoudi, J. Tofanin Neto, M. Saavedra, and I. Tsokanos, *On Generalized Hyperbolicity, Stability, and Shadowing for Linear Operators*, arXiv:2608.17021 (first version 17 August 2026).
2. M. Pituk, *Spectral characterization of shadowing for linear operators on Hilbert spaces*, arXiv:2511.12272 (first version 15 November 2025), particularly Proposition 2.1 and Example 1.8.
3. F. Bayart, *Two problems on weighted shifts in linear dynamics*, arXiv:2101.02989 (2021).
