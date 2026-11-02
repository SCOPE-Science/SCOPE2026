# Sharp local shape Hessian for hyperbolic Bergman–wavelet concentration

## Finding
Fix \(\alpha>-1\) and \(0<T<1\), and put \(c=\alpha+1>0\). On the probability-normalized analytic weighted Bergman space \(A^2_\alpha(\mathbb D)\), let \(L_\Omega=P_\alpha\mathbf1_\Omega\vert_{A^2_\alpha}\) denote the positive localization operator, and let \(\Lambda(\Omega)=\|L_\Omega\|\). For a real bounded angular profile \(h\) with \(\widehat h_0=0\), define
\[
\Omega_\varepsilon=\left\{re^{i\theta}:\frac{r^2}{1-r^2}<\frac{T}{1-T}+\varepsilon h(\theta)\right\},\qquad
\widehat h_n=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-in\theta}\,d\theta.
\]
For sufficiently small real \(\varepsilon\), this family has the *exactly fixed* hyperbolic area \(\int_{\Omega_\varepsilon}(1-|z|^2)^{-2}\,dA(z)=\pi T/(1-T)\). Define, for each integer \(n\ge1\),
\[
 v_j=\frac{(c)_j}{j!},\quad w_n=\frac{(c+1)_n}{n!},\quad S_n(T)=\sum_{j=1}^n v_jT^j,\quad
 B_n=c(c+1)(1-T)^{c+2}\left(1-\frac{c\,w_nT^n}{(c+1)S_n(T)}\right).
\]
Then the *optimized largest-eigenvalue deficit*, not merely a deficit for a fixed analytic function, has the exact expansion
\[
\boxed{\Lambda(\Omega_0)-\Lambda(\Omega_\varepsilon)
=\varepsilon^2\sum_{n=2}^\infty B_n|\widehat h_n|^2+O_{\alpha,T,h}(|\varepsilon|^3).}
\]
Its Fourier coefficients are strictly ordered:
\[
\boxed{0=B_1<B_2<B_3<\cdots<\lim_{n\to\infty}B_n=c(c+1)(1-T)^{c+2}.}
\]
In particular, the least positive curvature is attained *exactly* by second angular harmonics and has the closed form
\[
\boxed{B_2=c(c+1)(1-T)^{c+2}\frac{2-T}{2+(c+1)T}.}
\]
Consequently, for real mean-zero profiles orthogonal to \(\cos\theta\) and \(\sin\theta\), with \(\|h\|_2^2=(2\pi)^{-1}\int_0^{2\pi}|h|^2\),
\[
\Lambda(\Omega_0)-\Lambda(\Omega_\varepsilon)
\ge\frac{B_2}{2}\varepsilon^2\|h\|_2^2+O_{\alpha,T,h}(|\varepsilon|^3),
\]
with the best possible quadratic coefficient \(B_2/2\), attained asymptotically by \(\cos(2\theta)\) and \(\sin(2\theta)\). The degree-one null directions are precisely the infinitesimal hyperbolic translations among mean-zero directions.

## Assumptions and scope
The normalized Bergman measure is \(d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha dA(z)\). The operator is \(L_\Omega f=P_\alpha(\mathbf1_\Omega f)\); equivalently, \(\langle L_\Omega f,f\rangle=\int_\Omega|f|^2d\mu_\alpha\). The profile \(h\in L^\infty(\mathbb T;\mathbb R)\) is fixed and mean zero. The angular profile need not be smooth: small \(\varepsilon\) keeps all radii uniformly inside the disk and positive. The \(O(|\varepsilon|^3)\) constant may depend on \(\|h\|_\infty\), \(T\), and \(\alpha\), and is *not* uniform over profiles with unbounded amplitudes. The theorem concerns a local expansion of the top localization eigenvalue, not global uniqueness, noisy reconstruction, or the entire concentration spectrum. In the Cauchy-wavelet representation, \(\alpha=2\beta-1\) for wavelet order \(\beta>0\); this is the Bergman realization of the analytic-wavelet problem from Ramos–Tilli.

## Proof
**1. Exact area and diagonal spectrum.** Write \(x=r^2/(1-r^2)\), so \(r^2=x/(1+x)\) and \((1-r^2)^{-2}r\,dr=dx/2\). Thus the hyperbolic area equals \(\tfrac12\int_0^{2\pi}(T/(1-T)+\varepsilon h(\theta))d\theta=\pi T/(1-T)\). The orthonormal analytic monomials are \(e_n(z)=\sqrt{w_n}\,z^n\), where \(w_n=(c+1)_n/n!\). For the unperturbed disk, the eigenvalues satisfy
\[
\lambda_n=cw_n\int_0^Tt^n(1-t)^{c-1}\,dt
=I_T(n+1,c)=1-(1-T)^c\sum_{j=0}^n\frac{(c)_j}{j!}T^j.
\]
This follows from the incomplete-beta recurrence or direct differentiation in \(T\) and equality at \(T=0\). In particular, \(\lambda_0=1-(1-T)^c\), and \(\lambda_0-\lambda_n=(1-T)^cS_n(T)>0\) for every \(n\ge1\): the top eigenvalue is simple and spectrally isolated.

**2. Genuine operator derivatives.** In the orthonormal basis,
\[
\langle e_m,L_{\Omega_\varepsilon}e_n\rangle=
\frac{c\sqrt{w_mw_n}}{2\pi}\int_0^{2\pi}e^{i(n-m)\theta}
\int_0^{X+\varepsilon h(\theta)}
\frac{x^{(m+n)/2}}{(1+x)^{(m+n)/2+c+1}}\,dx\,d\theta,
\quad X=\frac{T}{1-T}.
\]
For sufficiently small complex \(\varepsilon\), the displayed radial primitives extend holomorphically in their upper endpoint near \(X>0\). The resulting matrix has uniform geometric decay in \(m+n\), since all endpoints remain in a compact subset of the disk after the substitution \(t=x/(1+x)\), while \(w_n\) grows at most polynomially. It therefore defines a trace-norm holomorphic family, allowing ordinary simple-eigenvalue perturbation theory. Direct endpoint differentiation gives
\[
\big|\langle e_n,L'_0e_0\rangle\big|^2
=c^2 w_nT^n(1-T)^{2c+2}|\widehat h_n|^2,
\qquad
\langle e_0,L''_0e_0\rangle=-c(c+1)(1-T)^{c+2}\|h\|_2^2.
\]
Because \(\widehat h_0=0\), the first derivative of the leading eigenvalue vanishes. The exact second derivative is
\[
\Lambda''(0)=\langle e_0,L''_0e_0\rangle
+2\sum_{n=1}^\infty\frac{|\langle e_n,L'_0e_0\rangle|^2}{\lambda_0-\lambda_n}.
\]
Using \(\|h\|_2^2=2\sum_{n\ge1}|\widehat h_n|^2\) and the gap from Step 1 yields the asserted coefficient \(B_n\) and cubic remainder.

**3. Strict spectral ordering and optimality.** The elementary binomial identity
\[
 w_n=\sum_{j=0}^n\frac{(c)_j}{j!}=1+S_n(1)
\]
holds for all real \(c>0\). Set \(q_n(T)=S_n(T)/(w_nT^n)\). To prove \(q_{n+1}(T)>q_n(T)\), consider
\[
 P_n(T)=w_nS_{n+1}(T)-Tw_{n+1}S_n(T).
\]
Its coefficient of \(T\) is \(w_n c>0\). For powers \(T^j\) with \(2\le j\le n\), the coefficient is
\[
 w_nv_{j-1}\left(\frac{c-1}{j}-\frac{c}{n+1}\right),
\]
and the coefficient of \(T^{n+1}\) is \(-w_nv_n/(n+1)<0\). The coefficient signs have at most one transition from nonnegative to negative: this is immediate when \(0<c\le1\), and follows from monotonicity of \((c-1)/j\) when \(c>1\). Moreover,
\[
 P_n(1)=w_{n+1}-w_n=v_{n+1}>0.
\]
A polynomial whose coefficients have this one-change sign pattern, with positive value at one, is strictly positive throughout \(0<T\le1\): divide by the power at the change index and compare every term with its value at one. Hence \(q_n(T)\) increases strictly, so \(B_n\) increases strictly. Since \(w_nT^n\to0\) and \(S_n(T)\to(1-T)^{-c}-1\), the stated limiting coefficient follows. For \(n=1\), \(S_1=cT\) and \(w_1=c+1\), giving \(B_1=0\). For \(n=2\), substitution of \(S_2=cT+c(c+1)T^2/2\) gives the boxed formula. Parseval now proves sharp stability on the subspace orthogonal to translations. Taking a pure second angular harmonic attains the stated quadratic constant, and the degree-one modes are the only quadratic null modes.

## Verification
The accompanying `verify.py` is a standalone supplementary checker. It compares incomplete-beta eigenvalues with the negative-binomial identity, tests coefficient ordering for several weights and radii, compares numerical largest-eigenvalue second differences of independent finite Toeplitz matrices with the derived Fourier coefficients, and checks exact hyperbolic area preservation. It uses `numpy` and `scipy` as specified in `requirements.txt` and was run successfully, reporting 212 finite checks. As an explicit normalization test, \(\alpha=0\), \(T=1/2\), \(h(\theta)=\cos(2\theta)\) gives
\[
\Lambda(\Omega_0)-\Lambda(\Omega_\varepsilon)=\frac{\varepsilon^2}{32}+O(|\varepsilon|^3).
\]
Finite checks are not used to infer infinite-dimensional results; the trace-norm analytic expansion and strict coefficient ordering are proved in Steps 1–3.

## Relationship to prior work
Ramos and Tilli (arXiv:2205.07998, initially public on 2022-05-16) establish global Faber–Krahn optimality and uniqueness of hyperbolic disks for analytic Cauchy-wavelet concentration, using the equivalent weighted Bergman formulation. They do not provide the Fourier-resolved second shape derivative of the *largest localization eigenvalue*. Gómez, Kalaj, Melentijević, and Ramos (arXiv:2411.16010) prove a stronger global stability inequality, and their Section 4 computes a second variation when the *analytic signal is perturbed and its best observation level set is readjusted*. That is a different variational functional from the fixed-domain, optimized-eigenvalue shape Hessian here; its existence and the general quadratic stability exponent are prior work. Gómez, Guerra, Ramos, and Tilli (arXiv:2307.09304) treat Fock/STFT stability, not the present hyperbolic Bergman Hessian. Nicola and Riccardi (arXiv:2401.04659) study Hilbert–Schmidt norms, which do not determine the operator norm's shape derivative. A direct earlier calculation or derivation from the functional Hessian of arXiv:2411.16010 remains a historical-priority risk. The present claim is restricted to the explicit Fourier-resolved operator-norm derivative and sharp second-mode constant, not a new global inequality.

## Limitations
The claim concerns only sufficiently small fixed-profile deformations about centered disks. It does not provide a uniform nonlinear stability constant over all measurable shapes, even though such global stability is already known from later literature. The first angular harmonics are quadratically flat because of symmetry, but the exact linear-in-\(\varepsilon\) radial boundary family is not asserted to be a family of shifted disks. The result is not a new formula for the Hilbert–Schmidt purity of localization operators, nor a new finite-spin cap theorem. Historical priority is provisional pending independent full-literature verification. Independent mathematical audit and validation have not been performed.

## References
1. J. P. G. Ramos and P. Tilli, *A Faber–Krahn inequality for wavelet transforms*, arXiv:2205.07998 (first public 2022-05-16); https://arxiv.org/abs/2205.07998 .
2. J. Gómez, D. Kalaj, P. Melentijević, and J. P. G. Ramos, *Uniform stability of concentration inequalities and applications*, arXiv:2411.16010 (first public 2024-11-24); https://arxiv.org/abs/2411.16010 .
3. J. Gómez, A. Guerra, J. P. G. Ramos, and P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304; https://arxiv.org/abs/2307.09304 .
4. F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, arXiv:2401.04659; https://arxiv.org/abs/2401.04659 .
