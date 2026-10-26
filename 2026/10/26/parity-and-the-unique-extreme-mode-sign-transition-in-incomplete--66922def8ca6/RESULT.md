# Parity and the unique extreme-mode sign transition in incomplete Lanczos exponentials

## Finding
Let \(A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\) have strictly positive diagonal entries, let \(b_i>0\), and let \(s\) be the number of distinct eigenvalues in the spectral support. For each integer \(1\le m<s\), let \(T_m\) be the exact symmetric Lanczos tridiagonal obtained from \(b\), with ordered Ritz values \(\theta_1<\cdots<\theta_m\), and let
\[
y_m(t)=\|b\|_2V_m e^{-tT_m}e_1,\qquad t\ge0.\]
The greatest active eigenvalue \(L=\max_i\lambda_i\) strictly exceeds \(\theta_m\). For every physical coordinate with \(\lambda_i=L\), the following *complete* sign dichotomy holds:

* If \(m\) is odd, then \(y_{m,i}(t)>0\) for every \(t\ge0\).
* If \(m\) is even, there is a unique finite \(t_m(L)>0\) such that \(y_{m,i}(t)>0\) for \(0\le t<t_m(L)\), equals zero at \(t_m(L)\), and is negative for every \(t>t_m(L)\).

For each fixed ordered Ritz list and every extrapolation point \(x>\theta_m\), define \(P_m(x)=\prod_{j=1}^m(x-\theta_j)\), the unit simplex
\[\Delta_m=\{(u_1,\dots,u_m):u_j\ge0,\ \sum_{j=1}^m u_j\le1\},\]
and \(u_{m+1}=1-\sum_{j=1}^m u_j\). The exact interpolation identity is
\[
\frac{p_{m-1,t}(x)}{e^{-tx}}=1-(-1)^m H_m(t,x),\qquad
H_m(t,x)=t^m P_m(x)\int_{\Delta_m}\exp\!\left(t\sum_{j=1}^m u_j(x-\theta_j)\right)du,
\]
where \(p_{m-1,t}\) interpolates \(z\mapsto e^{-tz}\) at the Ritz values. For even \(m\), the unique sign-transition time is characterized without root ambiguity by \(H_m(t_m(x),x)=1\). It is strictly decreasing in \(x>\theta_m\), so the largest-eigenvalue coordinates are the *first among the modes above the largest Ritz value* to change sign. No assertion of first sign loss among all physical coordinates is made.

For every \(m<s\), irrespective of parity, the top-mode relative approximation multiplier has exponential growth:
\[
\frac{y_{m,i}(t)}{b_i e^{-Lt}}\sim \ell_1(L)e^{(L-\theta_1)t}\quad(t\to\infty),\qquad
\ell_1(L)=\prod_{j=2}^m\frac{L-\theta_j}{\theta_1-\theta_j}\ne0.
\]
Thus odd-dimensional top-mode sign preservation does not imply relative accuracy. The special case \(m=2\) is already established in the prior two-step positivity-horizon result; the contribution here is the all-depth alternating-parity theorem, including odd depths and every even depth at least four.

## Assumptions and scope
Everything is in exact arithmetic. The starting vector has positive entries in the coordinate basis in which \(A\) is diagonal; the exact semigroup \(e^{-tA}b\) is consequently strictly positive for finite \(t\ge0\). The spectral support has at least \(m+1\) distinct points, preventing Lanczos termination at step \(m\). The statement concerns only coordinates with the *largest* active eigenvalue, and, in its monotonicity refinement, only spectral coordinates strictly above the largest Ritz value. In particular, an odd Lanczos depth does **not** guarantee positivity in every physical coordinate. Full-depth Lanczos, at \(m=s\), is exact and positive; it is excluded.

The parameter \(t_m(x)\) compares evaluation points \(x\) while holding the Ritz nodes fixed; it is not claimed to be monotone when altering the matrix, starting vector, or Ritz nodes themselves. Numerical finite-precision effects, non-diagonal semigroups, rational Krylov projections, and restarting are outside the claim.

## Proof
1. **Polynomial representation.** Lanczos Krylov exactness states that, for every polynomial \(p\) of degree less than \(m\), \(p(A)b=\|b\|_2V_mp(T_m)e_1\). Since \(T_m\) is irreducible symmetric tridiagonal prior to termination, its Ritz values are simple. The unique polynomial \(p_{m-1,t}\) interpolating the exponential at those values satisfies \(p_{m-1,t}(T_m)=e^{-tT_m}\). Hence \(y_m(t)=p_{m-1,t}(A)b\), coordinatewise.

2. **Strict Ritz location.** Rayleigh–Ritz places \(\theta_m\le L\). Equality would force the Krylov space \(\operatorname{span}\{b,Ab,\ldots,A^{m-1}b\}\) to contain a nonzero \(L\)-eigenvector. This would require a nonzero polynomial of degree below \(m\) to vanish at the other at least \(m\) distinct active eigenvalues, impossible. Thus \(\theta_m<L\).

3. **Signed divided-difference identity.** For \(x>\theta_m\), Newton interpolation gives the exact remainder
\[
e^{-tx}-p_{m-1,t}(x)=\left(\prod_{j=1}^m(x-\theta_j)\right)f_t[\theta_1,\ldots,\theta_m,x],\]
where \(f_t(z)=e^{-tz}\) and the bracketed expression denotes the order-\(m\) divided difference of \(f_t\), not an exponential of the nodes. The Hermite–Genocchi simplex representation turns this into
\[
e^{-tx}-p_{m-1,t}(x)=(-t)^mP_m(x)\int_{\Delta_m}\exp\!\left[-t\left(\sum_{j=1}^m u_j\theta_j+u_{m+1}x\right)\right]du.\]
Factoring out \(e^{-tx}\) proves the displayed \(H_m\) formula. This integral has its ordinary \(m\)-dimensional Lebesgue simplex measure of total mass \(1/m!\), so there is no omitted factorial.

4. **Unique transition and strict monotonicity.** For fixed \(x>\theta_m\), all gaps \(x-\theta_j\) are positive. Therefore \(H_m(t,x)\) is continuous on \([0,\infty)\), satisfies \(H_m(0,x)=0\), and is strictly increasing for \(t>0\) because both \(t^m\) and its positive exponential integrand increase. Also \(H_m(t,x)\ge t^mP_m(x)/m!\to\infty\). If \(m\) is odd, \(1-(-1)^mH_m=1+H_m>0\). If \(m\) is even, \(1-H_m\) has exactly one zero and changes from positive to negative. For fixed \(t>0\), \(P_m(x)\) and every integrand factor increase strictly with \(x\). Hence \(H_m(t,x)\) increases strictly with \(x>\theta_m\), and the crossing time decreases strictly. Substituting \(x=L\) and \(b_i>0\) proves the asserted coordinate signs.

5. **Relative-error growth.** The Lagrange representation is \(p_{m-1,t}(L)=\sum_{j=1}^m\ell_j(L)e^{-t\theta_j}\), where \(\ell_j(L)=\prod_{k\ne j}(L-\theta_k)/(\theta_j-\theta_k)\). Since \(\theta_1\) is the unique smallest Ritz value and \(\ell_1(L)\ne0\), the first term dominates as \(t\to\infty\). The sign of \(\ell_1(L)\) is \((-1)^{m-1}\), verifying the parity asymptotics independently. Since \(L>\theta_1\), the relative multiplier diverges in magnitude exponentially.

## Verification
The standalone `verify.py` constructs several diagonal positive-definite matrices with distinct spectra and strictly positive initial vectors, computes Lanczos Ritz matrices using a reorthogonalized Krylov basis, and evaluates the Lagrange-extrapolated top coordinate in exponentially scaled form to avoid spurious underflow. It checks odd-depth positive signs, even-depth unique sign crossings numerically, the strict ordering \(\theta_m<L\), and the sign parity of \(\ell_1(L)\). It also checks the elementary \(m=2\) interpolation against its explicit expression. Run `python3 verify.py` with NumPy and SciPy installed.

Finite numerical tests do not prove uniqueness or the theorem for arbitrary \(m\); those conclusions follow from Steps 1–5.

## Relationship to prior work
Chen, Greenbaum, Musco, and Musco (2022, arXiv:2202.11251; published 2023) define the standard Lanczos matrix-function approximation, establish the required Krylov-space representation, and develop an alternative optimal rational-function approximation method. Their source does not establish the all-depth top-mode sign dichotomy. The standard polynomial Lanczos approximation studied here is not the rational optimization method introduced in that paper. The underlying interpolation remainder and Hermite–Genocchi representation are classical, not novel lemmas.

A particularly close prior mathematical finding, *The exact positivity horizon of the two-step Lanczos exponential* (2026), gives a complete formula for the case \(m=2\), including a three-dimensional witness. That case is expressly excluded from the new-contribution claim. Its result does not imply the odd-depth protection, unique crossing at all even depths, or monotonic crossing among modes above the largest Ritz node. Druskin (2008) studies monotonicity of Lanczos exponential norm/error and reduced Jacobi-coordinate positivity rather than the extreme coordinate in the original diagonal basis. Bergermann and Stoll (2023) discuss polynomial and rational Krylov exponential methods without the stated parity law.

## Limitations
This is a precise *one-coordinate-family* sign theorem. Coordinates with eigenvalues between Ritz nodes can have other sign transitions, and no complete original-coordinate positivity classification is claimed. The strict existence result applies to incomplete Krylov spaces; exact termination removes the issue. The novelty assessment is best-knowledge: the proof uses classical extrapolation formulas, and an equivalent all-order parity statement could appear in earlier numerical-interpolation or matrix-function literature under different language.

## References
1. T. Chen, A. Greenbaum, C. Musco, C. Musco, *Low-memory Krylov subspace methods for optimal rational matrix function approximation*, arXiv:2202.11251 (first submitted 2022-02-23), SIAM J. Matrix Anal. Appl. 44 (2023), 670–692, DOI: 10.1137/22M1479853.
2. M. Bergermann and M. Stoll, *Adaptive rational Krylov methods for exponential Runge–Kutta integrators*, arXiv:2303.09482 (first submitted 2023-03-16).
3. V. Druskin, *On Monotonicity of the Lanczos Approximation to the Matrix Exponential*, Linear Algebra Appl. 429 (2008), 1679–1683, DOI: 10.1016/j.laa.2008.04.046.
4. *The exact positivity horizon of the two-step Lanczos exponential*, mathematical result, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-exact-positivity-horizon-of-the-two-step-lanczos-exponential--fb3579f163d8 .
5. K. Atkinson, *An Introduction to Numerical Analysis*, 2nd edition, Wiley (1989), Chapter 3, on divided differences and interpolation; cf. the Hermite–Genocchi formula.
