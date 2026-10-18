# Sharp leverage amplification from one outlier in circular affine least squares

## Finding
For each integer \(n\ge 3\), take the \(n\) equally spaced points \(x_j=(\cos(2\pi j/n),\sin(2\pi j/n))\) in the plane, together with one additional point \(x_*=(R\cos\phi,R\sin\phi)\), where \(R\ge0\) and \(\phi\in\mathbb R\). Let \(X\) be the real \((n+1)\)-by-\(3\) matrix with rows \((1,x_{j,1},x_{j,2})\) and \((1,x_{*,1},x_{*,2})\), and let \(H_{n,R,\phi}=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\) be the least-squares fitted-value projector. Write
\[
K_n(\phi)=\sup_{R\ge0}\|H_{n,R,\phi}\|_{\ell^\infty\to\ell^\infty}.
\]
Uniformly over every phase \(\phi\), the sharp amplification and every maximizing radius obey
\[
\boxed{K_n(\phi)=\frac{\sqrt{2n}}{\pi}+\frac12+O(n^{-1/2}),\qquad
R_n=\sqrt{\frac n2}+\frac\pi4+O(n^{-1/2}).}
\]
For all sufficiently large \(n\), the operator-norm maximizing output row is exclusively the added point, not an original unit-circle sample. The outlier-row norm is known **exactly** for every finite \(n,R,\phi\):
\[
\boxed{M_n(R,\phi)=
\frac{1+2R^2+\sum_{j=0}^{n-1}|1+2R\cos(2\pi j/n-\phi)|}{n+1+2R^2}.}
\]
The result describes worst-case bounded perturbations in the *whole vector of observed response values*, not the influence of changing only the outlier response.

## Assumptions and scope
The regression is ordinary unweighted real least squares with an intercept and two linear coordinate predictors. All \(n+1\) observations receive equal weight; the added design point may lie anywhere in the plane, and the original points lie on the unit circle. The design matrix has rank three for every \(n\ge3\), \(R\ge0\), and \(\phi\). The norm is the induced norm on fitted-value vectors, not a coefficient norm or continuous-domain interpolation norm. The constants in both big-O estimates are absolute and independent of \(\phi\), and the second asymptotic holds for **every** global maximizer \(R_n\) for that phase. No uniqueness of finite-\(n\) radii is asserted.

## Proof
**1. Exact row formula.** For the regular \(n\)-gon design \(X_0\), Fourier orthogonality gives
\[
A=X_0^{\mathsf T}X_0=\operatorname{diag}(n,n/2,n/2).
\]
Set \(v=(1,R\cos\phi,R\sin\phi)^{\mathsf T}\), \(c_j=\cos(2\pi j/n-\phi)\), and \(D=n+1+2R^2\). Then \(v^{\mathsf T}A^{-1}v=(1+2R^2)/n\). The Sherman--Morrison rank-one inverse formula for \(A+vv^{\mathsf T}\) gives
\[
H_{*,*}=\frac{1+2R^2}{D},\qquad
H_{*,j}=\frac{1+2Rc_j}{D}.
\]
Taking the absolute row sum proves the exact formula for \(M_n\). Its sharpness is obtained by choosing each input response to be the sign of the corresponding outlier-row entry.

**2. The other rows cannot compete at large size.** The old-only least-squares projector has diagonal entries \(3/n\). The new projector restricted to its original \(n\) rows is the old projector minus a positive semidefinite rank-one matrix, so \(0\le H_{j,j}\le3/n\) for every ordinary row. Since \(H\) is a symmetric orthogonal projection, \(\sum_k H_{j,k}^2=H_{j,j}\). Cauchy--Schwarz therefore yields
\[
\sum_{k=0}^{n}|H_{j,k}|\le\sqrt{(n+1)H_{j,j}}\le\sqrt{\frac{3(n+1)}{n}}.
\]
This bound is uniform in \(R\) and \(\phi\).

**3. Uniform circle quadrature.** Put
\[
S_n(R,\phi)=\sum_{j=0}^{n-1}|1+2R\cos(2\pi j/n-\phi)|,
\quad m(R)=\frac1{2\pi}\int_0^{2\pi}|1+2R\cos t|\,dt.
\]
Direct integration gives \(m(R)=1\) for \(0\le R\le1/2\) and, for \(R>1/2\),
\[
m(R)=\frac2\pi\left(\sqrt{4R^2-1}+\arcsin\frac1{2R}\right),\qquad
m'(R)=\frac4\pi\sqrt{1-\frac1{4R^2}}.
\]
The periodic integrand has total variation at most \(8R\). Comparing an arbitrary shifted uniform grid average with the circular integral cell by cell gives the phase-uniform bounds
\[
|S_n(R,\phi)-nm(R)|\le8R.
\]
For \(R\ge1\) away from the finitely many switching radii, differentiating the sum is valid. The derivative integrand \(2\cos t\,\operatorname{sgn}(1+2R\cos t)\) has bounded total variation uniformly in \(R\ge1\), so the same quadrature argument gives
\[
|\partial_R S_n(R,\phi)-n m'(R)|\le C
\]
with a universal constant \(C\). At a switching radius the one-sided derivative of a term \(|1+2Rc_j|\), necessarily with \(c_j<0\), jumps *upward*. Consequently no switching radius can be a local maximum of \(M_n\).

**4. Optimal scale and first two asymptotic terms.** The elementary inequality \(|1+2Rc_j|\le1+2R\) shows
\[
1\le M_n(R,\phi)\le1+\frac{2nR}{n+1+2R^2}.
\]
Thus \(M_n/\sqrt n\to0\) uniformly in either regime \(R/\sqrt n\to0\) or \(R/\sqrt n\to\infty\). On compact subintervals of \(\rho=R/\sqrt n\in(0,\infty)\), the explicit mean and quadrature error yield uniformly in \(\phi\)
\[
M_n(\rho\sqrt n,\phi)=\sqrt n\,F(\rho)+G(\rho)+O(n^{-1/2}),
\quad F(\rho)=\frac{4\rho}{\pi(1+2\rho^2)},\quad G(\rho)=\frac{2\rho^2}{1+2\rho^2}.
\]
The unique maximum of \(F\) on \((0,\infty)\) is at \(\rho_0=1/\sqrt2\), where \(F(\rho_0)=\sqrt2/\pi\). Therefore every maximizing radius lies at \(R_n/\sqrt n\to\rho_0\), uniformly in \(\phi\). This peak diverges as \(\sqrt n\), dominating the bounded ordinary-row norms. Continuity and the endpoint limits \(M_n(0,\phi)=\lim_{R\to\infty}M_n(R,\phi)=1\) ensure an interior radius maximizing \(M_n\) for sufficiently large \(n\).

**5. Optimal additive radius shift.** At a maximizing radius there is no switching cusp by Step 3, so differentiation of \(M=(1+2R^2+S_n)/D\) gives exactly
\[
0=D^2\partial_R M=4Rn+D\partial_R S_n-4RS_n.
\]
Near \(R\sim\sqrt{n/2}\), the two uniform quadrature bounds and the explicit formulas yield
\[
S_n(R,\phi)=\frac{4nR}{\pi}+O(\sqrt n),\qquad
\partial_R S_n(R,\phi)=\frac{4n}{\pi}+O(1).
\]
Substitution reduces the stationary equation to
\[
n-2R^2+\pi R=O(1),
\]
with absolute error uniformly in phase. Its positive solution satisfies \(R=\sqrt{n/2}+\pi/4+O(n^{-1/2})\). Finally insert this into the expansion from Step 4. Because \(F'(\rho_0)=0\), its displacement changes the leading term only by \(O(n^{-1/2})\); \(G(\rho_0)=1/2\). This establishes the stated two-term sharp norm asymptotic and completes the proof.

## Verification
The accompanying standard-library `checker.py` independently builds the full design Gram matrix and inverts it by Gauss--Jordan elimination, compares the resulting projection rows with the closed-form expressions, verifies projection identities and ordinary-row bounds, and checks shifted-grid integral estimates. Additional finite optimizations test the first two asymptotic terms and the universal additive radius shift for several phases. Running `python3 checker.py` produced `PASS: 21642 independent finite assertions`. The checker is a consistency test only; the proof's asymptotic and all-size assertions follow from the analytic steps above.

## Relationship to prior work
Cohen, Davenport and Leviatan study stability of least-squares approximation, including trigonometric spaces and equispaced samples, with accuracy controlled in \(L^2\) rather than the sharp response-vector \(\ell^\infty\) norm for one extreme covariate. McWilliams, Krummenacher, Lucic and Buhmann use leverage and influence to understand corrupt linear-regression design points, but do not give the present exact circular outlier-row sum or optimized critical radius.

The hat-matrix identity is classical (Hoaglin and Welsch). An existing exact endpoint norm for the three-character Fourier projector on a cyclic group gives the *uncontaminated* circle-design baseline; its single trigonometric kernel does not imply the rank-one-contaminated maximization. A known simplex affine projection norm concerns continuous volume measure, a different projection and no isolated point of variable leverage. The proof uses these established ideas without claiming them as new. Historical novelty cannot be certified solely from searched records.

## Limitations
Only one additional covariate, equal observational weights, the affine three-parameter model, real bounded response perturbations, and the large-\(n\) optimum are treated. The formula for the added row holds at every finite \(n\), but there is no asserted complete finite-\(n\) classification of the optimizing radius or phase. The norm measures adversarially correlated errors across all observations, not a stochastic risk or single-point influence score. An older equivalent result under regression leverage, discrete Lebesgue constant, or projector row-sum terminology remains possible.

## References
1. A. Cohen, M. A. Davenport and D. Leviatan, *On the stability and accuracy of least squares approximations*, arXiv:1111.4422v1, first posted 2011-11-18 (full HTML v3 at https://arxiv.org/html/1111.4422v3).
2. B. McWilliams, G. Krummenacher, M. Lucic and J. M. Buhmann, *Fast and Robust Least Squares Estimation in Corrupted Linear Models*, arXiv:1406.3175v1, first posted 2014-06-12 (full HTML v2 at https://arxiv.org/html/1406.3175v2).
3. D. C. Hoaglin and R. E. Welsch, *The Hat Matrix in Regression and ANOVA*, MIT working paper WP 904-77 (1977); available PDF at https://scispace.com/pdf/the-hat-matrix-in-regression-and-anova-4ujfb1ja3a.pdf.
4. *Exact three-frequency Fourier projection norm on every cyclic group*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242/RESULT.md.
5. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34/RESULT.md.
