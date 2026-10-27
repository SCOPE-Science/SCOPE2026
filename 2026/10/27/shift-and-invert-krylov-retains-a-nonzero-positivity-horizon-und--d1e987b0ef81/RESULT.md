# Shift-and-invert Krylov retains a nonzero positivity horizon under unbounded stiffness

## Finding
For a strictly positive initial vector on a diagonal dissipative system, the two-vector shift-and-invert Krylov exponential approximation has an exact, finite positivity horizon at every positive shift whenever at least three distinct decay rates are present. The horizon is attained first, and simultaneously, at the coordinates with the largest decay rate.

Unlike ordinary two-step polynomial Lanczos, this horizon **need not collapse under arbitrarily large stiffness**. With \(A_L=\operatorname{diag}(1,2,L)\), \(b=(1,1,1)^{\mathsf T}\), and unit shift, its limiting value is
\[
\lim_{L\to\infty}T_{\mathrm{SAI}}(L)=\frac{1}{4\sqrt{79}}\log\left(\frac{179+20\sqrt{79}}{21}\right)=0.07967174251247\ldots,
\]
while the polynomial Lanczos counterpart obeys
\[
T_{\mathrm{poly}}(L)\sim\frac{2\log L}{L}.
\]
Their positivity-horizon ratio grows without bound. Thus shifting and inverting may substantially delay, but cannot eliminate, positivity loss in this reduced projection.

## Assumptions and scope
Let \(n\ge2\), \(A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)\) with all \(\lambda_i>0\), and \(b_i>0\). Fix \(\gamma>0\), put
\[
R=(I+\gamma A)^{-1}=\operatorname{diag}(r_1,\ldots,r_n),\qquad r_i=(1+\gamma\lambda_i)^{-1},
\]
and let the columns of \(V\) form any orthonormal basis of \(\mathcal K_2=\operatorname{span}\{b,Rb\}\). When this space is two-dimensional define
\[
J=V^{\mathsf T}RV,\qquad H=\gamma^{-1}(J^{-1}-I_2),\qquad y_\gamma(t)=V e^{-tH}V^{\mathsf T}b.
\]
This is the two-vector **shift-and-invert projected-resolvent** exponential approximation; it uses the inverse of the *compressed resolvent*. It is not the different rational-Galerkin formula with \(V^{\mathsf T}AV\) in the exponential. The displayed \(H\) is precisely the projected-resolvent mapping used in shift-and-invert Arnoldi (Katrutsa–Botchev–Oseledets, equation (2.3)). All assertions are in exact arithmetic. If the spectral support has only one distinct value, the one-dimensional subspace is used and the approximation is exact. If it has two, the two-dimensional space is invariant and the approximation is exact.

Suppose there are at least three distinct values among the \(\lambda_i\). Let \(\eta_-<\eta_+\) be the eigenvalues of \(J\), and \(r_*=\min_i r_i\). Set
\[
\theta_s=\frac{\eta_+^{-1}-1}{\gamma},\qquad \theta_f=\frac{\eta_-^{-1}-1}{\gamma},\qquad \Delta=\theta_f-\theta_s>0.
\]
Then \(0<\eta_-<\eta_+<1\), \(r_*<\eta_-\), and the **sharp global nonnegativity boundary** is
\[
T_\gamma=\Delta^{-1}\log\left(\frac{\eta_+-r_*}{\eta_--r_*}\right)=\frac{\gamma\eta_+\eta_-}{\eta_+-\eta_-}\log\left(\frac{\eta_+-r_*}{\eta_--r_*}\right).
\]
All coordinates are positive at every \(0\le t<T_\gamma\); at equality exactly the maximal-\(\lambda\) coordinates vanish; afterwards each such coordinate is negative. The other coordinates may develop negative signs later, but the theorem makes no claim that they all do.

## Proof
**1. Strict Ritz inclusion.** Every \(r_i\) lies in \((0,1)\). Since \(J\) is a compression of the positive definite \(R\), its two eigenvalues are in \((0,1)\). The Krylov vectors \(b,Rb\) are linearly independent whenever at least two spectral values are active. Compression and Rayleigh–Ritz imply \(r_*\le\eta_-<\eta_+\le r^*=\max_i r_i\). Equality \(\eta_-=r_*\) would force \(\mathcal K_2\) to contain an eigenvector supported only on the \(r_*\)-eigenspace. Each vector in \(\mathcal K_2\) has coordinates \(b_i(a+c r_i)\). A nonzero affine polynomial cannot vanish at two different spectral values above \(r_*\), which exist by the three-level assumption. Thus \(r_*<\eta_-\). Likewise \(\eta_+<r^*\).

**2. Exact projected inverse and interpolation.** Because \(V^{\mathsf T}b\) represents the first Krylov vector, \(Rb\) lies in the subspace and the polynomial exactness identity holds for every affine polynomial \(p\):
\[
Vp(J)V^{\mathsf T}b=p(R)b.
\]
Take \(f_t(r)=\exp[-t(r^{-1}-1)/\gamma]\) and its degree-one interpolant at the distinct Ritz nodes \(\eta_+,\eta_-\). Since \(f_t(J)=e^{-tH}\), the approximate coordinates are **exactly**
\[
\frac{y_{\gamma,i}(t)}{b_i}=\frac{(r_i-\eta_-)e^{-t\theta_s}+(\eta_+-r_i)e^{-t\theta_f}}{\eta_+-\eta_-}.
\]
For every \(t>0\), this affine function is strictly increasing in \(r_i\): its slope is \((e^{-t\theta_s}-e^{-t\theta_f})/(\eta_+-\eta_-)>0\). The smallest coordinate multiplier occurs precisely when \(r_i=r_*\), i.e., on maximal-\(\lambda_i\) coordinates. At \(t=0\) the multiplier is one. At \(r_*\), multiply by the positive denominator and \(e^{t\theta_f}\); the sign is that of
\[
(\eta_+-r_*)-(\eta_--r_*)e^{t\Delta},
\]
which is strictly decreasing from a positive value and vanishes at the stated \(T_\gamma\). This proves the exact sign classification. If at most two distinct rates are present, the subspace contains the entire active invariant eigenspace and exactness follows directly.

**3. Exact stiff limit of the shift-and-invert horizon.** For \(A_L=\operatorname{diag}(1,2,L)\), \(b=(1,1,1)^{\mathsf T}\), \(\gamma=1\), the resolvent eigenvalues are \((1/2,1/3,1/(1+L))\). As \(L\to\infty\), the normalized first and second moments and compressed second Lanczos diagonal entry converge to
\[
\mu=\frac5{18},\qquad s^2=\frac7{162},\qquad \nu=\frac{25}{126}.
\]
The limiting Jacobi matrix \(\begin{psmallmatrix}\mu&s\\s&\nu\end{psmallmatrix}\) has strictly positive eigenvalues \(\eta_\pm=(10\pm\sqrt{79})/42\). Its transformed decay rates are \(\theta_s=19-2\sqrt{79}\) and \(\theta_f=19+2\sqrt{79}\), with gap \(4\sqrt{79}\). Because the smallest resolvent eigenvalue tends to zero, inserting these limits into the exact horizon yields
\[
T_1(L)\longrightarrow \frac1{4\sqrt{79}}\log\left(\frac{\eta_+}{\eta_-}\right)=\frac1{4\sqrt{79}}\log\left(\frac{179+20\sqrt{79}}{21}\right)>0.
\]
All limiting matrix eigenvalues are nondegenerate and the argument uses continuity only; no limit of numerical experiments is invoked.

**4. Comparison with polynomial Lanczos.** In ordinary two-step polynomial Lanczos for the same \(A_L,b\), put \(a=(L+3)/3\), \(v=2(L^2-3L+3)/9\), and \(d=(4L^3-9L^2-3L+18)/[6(L^2-3L+3)]\). The two Ritz values are those of \(\begin{psmallmatrix}a&\sqrt v\\\sqrt v&d\end{psmallmatrix}\), and direct expansion of this explicit \(2\times2\) characteristic polynomial gives
\[
\vartheta_1=\frac32-\frac{1}{2L}+O(L^{-2}),\qquad \vartheta_2=L-\frac{1}{2L}+O(L^{-2}).
\]
The ordinary two-step Lanczos positivity formula is
\[
T_{\rm poly}(L)=\frac{1}{\vartheta_2-\vartheta_1}\log\left(\frac{L-\vartheta_1}{L-\vartheta_2}\right).
\]
Now \(L-\vartheta_2\sim(2L)^{-1}\) and \(L-\vartheta_1\sim L\), so the logarithm is \(2\log L+O(1)\) while the denominator is \(L+O(1)\). Therefore \(T_{\rm poly}(L)\sim2\log L/L\), proving the diverging ratio.

## Verification
Run `python3 verify.py` (Python standard library only). It reconstructs compressed-resolvent parameters and a directly orthogonalized \(2\times2\) matrix projection, tests the affine-interpolation formula and sign horizon on 1,400 seeded diagonal examples, and checks the closed-form stiff limit against a polynomial-Lanczos benchmark. It also verifies exact-rational moments and an exact irrational sign inequality on \(A=\operatorname{diag}(1,2,4)\), \(b=(1,1,1)^{\mathsf T}\), \(\gamma=1\). The completed package replay yielded 65,143 checks. The analytical proof, not the finite tests, establishes the universal statement and the limit.

## Relationship to prior work
Katrutsa, Botchev and Oseledets (arXiv:1909.13059, Sections 1–3, particularly equation (2.3)) specify the shift-and-invert Krylov basis and the compressed-resolvent inverse used here, and study practical shift choices and residual-based accuracy. Bergermann and Stoll (arXiv:2303.09482, Sections 1 and 4) examine rational Krylov spaces in exponential integrators, emphasizing convergence, pole selection, and implementation. Those methods and standard affine Krylov interpolation are established ingredients.

The closest published sign-horizon result, *The exact positivity horizon of the two-step Lanczos exponential* (public research record, October 2026), handles **polynomial** Lanczos with \(\mathcal K_2(A,b)\) and exponentiation of \(V^{\mathsf T}AV\). That earlier conclusion is not new here. The present comparison instead uses \(\mathcal K_2((I+\gamma A)^{-1},b)\) and exponentiates \(\gamma^{-1}[(V^{\mathsf T}(I+\gamma A)^{-1}V)^{-1}-I]\). Its explicit strictly positive stiff-limit horizon and divergence relative to polynomial Lanczos do not follow from the prior published horizon formula without this separate compressed-resolvent calculation. The proof shares the general two-node interpolation mechanism and does not claim that mechanism as new.

## Limitations
The theorem concerns exact arithmetic, diagonal positive definite matrices, positive initial coordinates, **two** Krylov vectors and one fixed positive shift. It does not cover general nonnegative generators, nondiagonal systems, restarted or higher-dimensional Krylov, finite precision, or positivity guarantees under a prescribed error-tolerance stopping rule. The limiting horizon is nonzero but finite, so the shifted method still eventually produces an invalid negative coordinate.

The polynomial comparison is for the specified one-parameter family and is not a universal error superiority theorem. General Lanczos sign-horizon and rational projection literature may contain the stiff-limit separation under another formulation; publication priority is not independently certified.

## References
1. A. Katrutsa, M. Botchev, I. Oseledets, *Practical shift choice in the shift-and-invert Krylov subspace evaluations of the matrix exponential*, arXiv:1909.13059v1 (2019-09-28), Sections 1–3, equation (2.3). https://arxiv.org/abs/1909.13059.
2. K. Bergermann and M. Stoll, *Adaptive rational Krylov methods for exponential Runge–Kutta integrators*, arXiv:2303.09482v1 (2023-03-16), Sections 1 and 4. https://arxiv.org/abs/2303.09482.
3. Q. Ye, *Error Bounds for the Lanczos Methods for Approximating Matrix Exponentials*, SIAM Journal on Numerical Analysis 51 (2013), 68–87, DOI 10.1137/11085935X. Abstract and institutional record inspected, full text not read.
4. *The exact positivity horizon of the two-step Lanczos exponential*, published mathematical research record (October 2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-exact-positivity-horizon-of-the-two-step-lanczos-exponential--fb3579f163d8. Full `RESULT.md` inspected for statement and proof comparison.
