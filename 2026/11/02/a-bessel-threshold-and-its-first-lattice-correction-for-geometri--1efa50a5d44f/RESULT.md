# A Bessel threshold and its first lattice correction for geometrically regular shifts

## Finding
For \(h>0\), \(\lambda>0\), and \(\lambda h^2<1\), let \(W_{h,\lambda}\) be the positive unilateral weighted shift on complex \(\ell^2(\mathbb N_0)\) with weights
\[
 w_j=\sqrt{1+\lambda h^2e^{-jh}},\qquad j\geq0.
\]
This is the geometrically regular shift with parameters \(b=e^h\), \(N=\lambda h^2\), \(D=0\). Write \(\operatorname{nr}(W)=\sup_{\|u\|_2=1}|\langle Wu,u\rangle|\), and let \(j_{0,1}\) be the smallest positive zero of the ordinary Bessel function \(J_0\). There is a unique threshold \(\lambda_h>0\) (for all sufficiently small \(h\)) such that \(\operatorname{nr}(W_{h,\lambda})=1\) when \(0\leq\lambda\leq\lambda_h\) and \(\operatorname{nr}(W_{h,\lambda})>1\) when \(\lambda>\lambda_h\), within the stated parameter domain. Its **sharp first lattice correction** is
\[
 \boxed{\lambda_h=\frac{j_{0,1}^2}{4}\,e^{-3h/2}+O(h^2)
 =\frac{j_{0,1}^2}{4}\left(1-\frac32h\right)+O(h^2).}
\]
For fixed \(\lambda>j_{0,1}^2/4\), let \(\kappa>0\) be the unique number satisfying \(j_{2\kappa,1}=2\sqrt\lambda\), where \(j_{\nu,1}\) is the first positive zero of \(J_\nu\). Then
\[
 \boxed{\operatorname{nr}(W_{h,\lambda})=1+\frac12\kappa^2h^2+o(h^2).}
\]
For fixed \(0<\lambda<j_{0,1}^2/4\), the radius equals one for all sufficiently small \(h\). In the supercritical regime, the normalized positive eigenvector of \((W+W^*)/2\), piecewise-linearly interpolated at spatial scale \(h\) with zero boundary value, converges strongly in \(L^2(0,\infty)\) to a positive multiple of \(J_{2\kappa}(2\sqrt\lambda e^{-x/2})\).

## Assumptions and scope
Complex Hilbert-space numerical radius is used; parameters are real and positive. For fixed \(h\), the threshold is considered on \(0\le\lambda<h^{-2}\); for small enough \(h\) it lies strictly in this interval. All limits send \(h\downarrow0\) with \(\lambda\) fixed unless otherwise stated. The constant in \(O(h^2)\) in the threshold expansion is absolute locally near \(j_{0,1}^2/4\). There is no assertion about exact critical equality at a fixed \(\lambda=j_{0,1}^2/4\).

## Proof
Put \(J_h=(W_{h,\lambda}+W_{h,\lambda}^*)/2\). Diagonal phase conjugation makes every \(\operatorname{Re}(e^{i\theta}W)\) unitarily equivalent to \(J_h\). The positive Jacobi matrix \(J_h\) has symmetric spectrum and its norm is its spectral supremum, so \(\operatorname{nr}(W)=\sup\sigma(J_h)\). Since \(w_j\to1\), the difference from the free half-line Jacobi matrix is compact and the top essential edge is \(1\).

For a finitely supported vector \(u\), set \(u_{-1}=0\) and \(E(u)=\sum_{j=-1}^{\infty}|u_{j+1}-u_j|^2\). Direct expansion gives
\[
 \frac{2}{h^2}\langle u,(I-J_h)u\rangle
 =\frac{E(u)}{h^2}-D_{h,\lambda}(u),\quad
 D_{h,\lambda}(u)=\frac2{h^2}\sum_{j\ge0}(w_j-1)\operatorname{Re}(\bar u_j u_{j+1}).
\]
The same formula extends by density to the form domain. Associate to \(u\) its continuous piecewise-linear interpolant \(f\), with \(f(0)=0\) and \(f((j+1)h)=u_j/\sqrt h\). Then \(E(u)/h^2=\int_0^\infty|f'|^2\). A crucial uniform estimate, for \(\lambda\) in any fixed compact interval of \([0,\infty)\), is
\[
 \left|D_{h,\lambda}(u)-\lambda e^{3h/2}\int_0^\infty e^{-x}|f(x)|^2\,dx\right|
 \le C h^2\int_0^\infty|f'|^2\,dx.\tag{1}
\]
Here is a direct derivation. Expand \(2(w_j-1)/h^2=\lambda e^{-jh}+O(\lambda^2h^2e^{-2jh})\). With \(y_k=f(kh)\) and \(m_k=(k+1/2)h\), the leading sum is exactly \(\lambda e^{3h/2}\sum_{k\ge1}h e^{-m_k}\operatorname{Re}(\bar y_k y_{k+1})\). On each interval \([kh,(k+1)h]\), the integral of the square of a linear interpolant differs from \(h\operatorname{Re}(\bar y_k y_{k+1})\) by \(h|y_{k+1}-y_k|^2/3\). Replacing the exponential by its midpoint value contributes, after summation, at most \(Ch^2(\int e^{-x}|f|^2+\int|f'|^2)\), by Cauchy--Schwarz. The missing first interval \([0,h]\) is at most \(h^2\int_0^h|f'|^2\). The square-root remainder is bounded in the same way by the exponentially weighted discrete Hardy estimate. Finally \(\int e^{-x}|f|^2\le C\int|f'|^2\), obtained from \(|f(x)|^2\le x\int_0^x|f'|^2\). This establishes (1) uniformly in the interpolant, including non-real inputs.

The exact optimal exponential Hardy inequality on the half-line is
\[
 \int_0^\infty|f'|^2\ge\lambda_*\int_0^\infty e^{-x}|f|^2,
 \qquad \lambda_*=j_{0,1}^2/4,\qquad f\in C_c^\infty(0,\infty).\tag{2}
\]
Indeed \(g(x)=J_0(j_{0,1}e^{-x/2})\) is positive for \(x>0\), vanishes at zero, tends to one at infinity and solves \(g''+\lambda_*e^{-x}g=0\). The ground-state transform gives \(\int(|f'|^2-\lambda_*e^{-x}|f|^2)=\int g^2|(f/g)'|^2\ge0\). Cutoffs of \(g\) at increasingly large distances show sharpness. The piecewise-linear subspaces attain the same sharp quotient up to \(O(h^2)\): interpolate the smooth resonance on the mesh, truncate its essentially constant tail over a length much larger than \(h^{-2}\), and use the standard \(H^1\) interpolation error \(O(h)\|g''\|_2\) together with orthogonality of derivative projection (which makes its energy error quadratic). Its exponentially weighted potential error is also \(O(h^2)\). Consequently the variational supremum
\[
 \sup_{u\ne0}\frac{D_{h,\lambda}(u)}{E(u)/h^2}
 =\frac{\lambda e^{3h/2}}{\lambda_*}+O(h^2)\tag{3}
\]
locally uniformly for \(\lambda\) near \(\lambda_*\). The supremum is monotone and continuous in \(\lambda\), and strict increase holds on the positive, nonnegative-vector maximizing branch. The spectral top exceeds one exactly when the ratio in (3) exceeds one. Thus the unique threshold has the asserted first-order expansion.

For the fixed-coupling limit, (1) is a uniform form comparison to the Dirichlet Schrödinger form \(q_\lambda(f)=\int(|f'|^2-\lambda e^{-x}|f|^2)\). Sampling smooth compactly supported test functions gives the upper bound for the minimal rescaled eigenvalue. Conversely, any normalized almost-minimizing discrete vectors with negative rescaled energy have uniformly bounded interpolated derivative energy by the Hardy bound and the bounded potential. The interpolants are locally compact in \(L^2\); the exponentially weighted potential converges because its tail is uniformly small; derivative energy is weakly lower semicontinuous. Moreover their interpolated \(L^2\) norm differs from the discrete \(\ell^2\) norm by at most \(Ch\|f'\|_2\). No loss of mass can lower a negative ground-state Rayleigh quotient. Hence the lowest rescaled spectral value converges to the lowest eigenvalue of \(-d^2/dx^2-\lambda e^{-x}\) with Dirichlet condition at zero; when negative the normalized positive ground states converge strongly in \(L^2\).

For energy \(-\kappa^2<0\), the decaying solution of the differential equation is \(J_{2\kappa}(2\sqrt\lambda e^{-x/2})\). The boundary condition and positivity select the first positive Bessel zero \(j_{2\kappa,1}=2\sqrt\lambda\). Strict increase of that zero with order gives existence and uniqueness exactly for \(\lambda>\lambda_*\). Combining with \(\operatorname{nr}(W)=1-(h^2/2)\inf\sigma(2(I-J_h)/h^2)\) proves the scaling and profile. Below \(\lambda_*\), the threshold estimate already gives equality of the numerical radius to one for small \(h\).

## Verification
The standalone program `check.py` recomputes the resonance thresholds from the Jacobi zero-energy recurrence and compares them to the first-order formula, and compares finite Jacobi eigenvalue coefficients to the Bessel order-root coefficient. This tests finite truncations only; all statements for infinitely many coordinates rely on the form argument above.

## Relationship to prior work
Benhida, Curto and Exner introduce and analyze the same geometrically regular shift family via moment and hyponormality questions (arXiv:2309.05888). Cornean, Garde and Jensen establish general norm-resolvent convergence for finite-difference half-space Laplacians with potentials (arXiv:2211.01974), which motivates but does not state the first-order edge-threshold correction for off-diagonal geometrically decaying weights. Related discrete and continuum Jacobi theory supplies background for the Bessel reduction. The claimed contribution is the specific sharp \(-3/2\) lattice correction together with the numerical-radius edge transition for this off-diagonal family, not the generic convergence theorem or the standard Bessel equation.

## Limitations
The asymptotic threshold requires small \(h\); no exact closed form for finite \(h\) is claimed. The continuum ground-state profile statement is for fixed supercritical \(\lambda\). No uniform double-scaling at \(\lambda-\lambda_*\to0\) is asserted. A literature-equivalent formula under Jacobi bound-state/resonance terminology cannot be ruled out absolutely. Independent verification has not been performed.

## References
1. C. Benhida, R. E. Curto, G. R. Exner, *Geometrically regular weighted shifts*, arXiv:2309.05888, first public 2023-09-12.
2. H. Cornean, H. Garde, A. Jensen, *Discrete approximations to Dirichlet and Neumann Laplacians on a half-space and norm resolvent convergence*, arXiv:2211.01974, first public 2022-11-03.
3. J. T. Lewis and M. E. Muldoon, *Monotonicity and convexity properties of zeros of Bessel functions*, SIAM Journal on Mathematical Analysis 8 (1977), 171–178, DOI:10.1137/0508012.
