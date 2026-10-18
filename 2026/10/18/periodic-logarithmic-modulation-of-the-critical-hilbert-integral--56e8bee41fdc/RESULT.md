# Periodic logarithmic modulation of the critical Hilbert integral operator

## Finding
For every fixed \(\omega>0\) and real \(|\varepsilon|<1\), define the Hilbert space \(X_{\varepsilon,\omega}\) of complex measurable functions on \([e,\infty)\), modulo almost-everywhere equality, by
\[
\|f\|_{X_{\varepsilon,\omega}}^2=\int_e^\infty |f(y)|^2(\log y)^2\bigl(1+\varepsilon\cos(\omega\log\log y)\bigr)^2\,\frac{dy}{y}.
\]
Let \(Y=L^2([e,\infty),dx/x)\) and \((H_{\varepsilon,\omega}f)(x)=\int_e^\infty f(y)/(x+y)\,dy\). Put \(L=2\pi/\omega\), \(a_\varepsilon(t)=(1+\varepsilon\cos(\omega t))^{-1}\), and let \(Q_{\varepsilon,\omega}\) be the positive compact operator on \(L^2([0,L],dt)\) whose integral kernel is
\[
Q_{\varepsilon,\omega}(u,v)=a_\varepsilon(u)a_\varepsilon(v)\sum_{m\in\mathbb Z}e^{-|u-v+mL|/2}.
\]
Then \(H_{\varepsilon,\omega}:X_{\varepsilon,\omega}\to Y\) is bounded and
\[
\boxed{\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}=\sqrt{\lambda_{\max}(Q_{\varepsilon,\omega})}.}
\]
In particular, \(\|H_{0,\omega}\|_{\mathrm{ess}}=2\), whereas every nonzero \(\varepsilon\) obeys
\[
\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}\ge\frac{2}{\sqrt{1-\varepsilon^2}}>2.
\]
For each *fixed* \(\omega>0\), the sharp perturbative law is
\[
\boxed{\|H_{\varepsilon,\omega}\|_{\mathrm{ess}}=2+\left(\frac32+\frac{1}{2\omega^2}\right)\varepsilon^2+O_\omega(\varepsilon^4)\quad(\varepsilon\to0).}
\]

## Assumptions and scope
All integrals are Lebesgue integrals, all functions may be complex, and essential norm means distance to the compact operators between the *specified* Hilbert spaces. The full-line periodic model uses the same fixed amplitude and frequency. The asserted perturbative remainder is not uniform as \(\omega\to0\). The theorem concerns a continuous Hilbert integral on \([e,\infty)\), not the discrete Hilbert matrix or analytic Bergman spaces.

## Proof
**Well-posedness and first compact reduction.** Since \(1-|\varepsilon|\le1+\varepsilon\cos(\omega t)\), Cauchy--Schwarz and \(\int_e^\infty dy/[y(\log y)^2]=1\) show absolute convergence of the defining integral at every fixed \(x\ge e\). Write \(u=\log x\), \(v=\log y\), and transfer input and output unitarily to \(L^2([1,\infty),du)\): \(g(v)=v[1+\varepsilon\cos(\omega\log v)]f(e^v)\), while the output is \((Hf)(e^u)\). The resulting kernel is
\[
B(u,v)=\frac{1}{v[1+\varepsilon\cos(\omega\log v)](1+e^{u-v})}.
\]
It differs from the weighted Copson kernel
\[
C(u,v)=\frac{\boldsymbol 1_{v>u}}{v[1+\varepsilon\cos(\omega\log v)]}
\]
by a Hilbert--Schmidt kernel, because \(|(1+e^{u-v})^{-1}-\boldsymbol1_{v>u}|\le e^{-|u-v|}\) and
\[
\|B-C\|_{\mathrm{HS}}^2\le(1-|\varepsilon|)^{-2}\int_1^\infty\frac{dv}{v^2}\int_1^\infty e^{-2|u-v|}\,du<\infty.
\]
Consequently the two operators have the same essential norm; boundedness follows from that of the Copson operator and Hilbert--Schmidt boundedness.

**Logarithmic-scale reduction.** The unitary map \(Wg(t)=e^{t/2}g(e^t)\) takes \(L^2([1,\infty),du)\) to \(L^2([0,\infty),dt)\). It carries \(C\) to
\[
(Kh)(t)=\int_t^\infty e^{-(s-t)/2}a_\varepsilon(s)h(s)\,ds.
\]
The Schur/Young bound gives \(\|K\|\le2/(1-|\varepsilon|)\). Let \(\widetilde K\) denote the same causal formula on \(L^2(\mathbb R)\). Extension of inputs by zero and restriction of outputs show \(\|K\|_{\mathrm{ess}}\le\|\widetilde K\|\). Conversely, select a compactly supported unit vector \(\varphi\) whose full-line image norm is arbitrarily close to \(\|\widetilde K\|\). Translate \(\varphi\) rightward by integer multiples of the period \(L\); the translated vectors lie in the half-line for large shifts and converge weakly to zero. Since \(a_\varepsilon\) is periodic, their half-line image norms tend to \(\|\widetilde K\varphi\|\): only an exponentially vanishing portion of the translated full-line output lies left of zero. Every compact operator maps this weakly null sequence to a norm-null sequence. Hence \(\|K\|_{\mathrm{ess}}=\|\widetilde K\|\).

**Periodic fiber and maximal quasi-momentum.** Direct integration gives
\[
(\widetilde K^*\widetilde K h)(s)=a_\varepsilon(s)\int_\mathbb R e^{-|s-r|/2}a_\varepsilon(r)h(r)\,dr.
\]
Decompose \(\mathbb R\) into cells of length \(L\), and Fourier transform the cell index. This unitary Bloch transform represents the positive full-line operator as a direct integral over quasi-momenta \(\theta\in[0,2\pi)\) of integral operators on \([0,L]\) with kernels
\[
a_\varepsilon(u)a_\varepsilon(v)\sum_{m\in\mathbb Z}e^{-|u-v+mL|/2}e^{im\theta}.
\]
The sum converges absolutely and uniformly. Taking absolute values of the quadratic form of an arbitrary fiber, then applying the positive \(\theta=0\) kernel to the modulus of the input, bounds every fiber norm above by \(\|Q_{\varepsilon,\omega}\|\); the zero fiber achieves this bound. Continuity in \(\theta\) ensures equality with the direct-integral essential supremum. The kernel of \(Q\) is continuous and positive; as a Gram-periodization it defines a positive compact operator. Thus the squared essential norm of \(H\) equals \(\lambda_{\max}(Q)\).

**The strict bound.** Write \(G_L\) for periodic convolution with \(\sum_m e^{-|t+mL|/2}\). With \(M_a\) as multiplication by \(a_\varepsilon\), one has \(Q=M_aG_LM_a\). Fourier modes \(e_k(t)=L^{-1/2}e^{ik\omega t}\) satisfy \(G_Le_k=d_ke_k\) with \(d_k=(1/4+k^2\omega^2)^{-1}\). In particular, \(d_0=4\). Testing with \(e_0\) yields
\[
\lambda_{\max}(Q)\ge\langle a_\varepsilon,G_La_\varepsilon\rangle/L\ge4\left|\frac1L\int_0^L a_\varepsilon(t)dt\right|^2=\frac4{1-\varepsilon^2}.
\]
At \(\varepsilon=0\), \(\|Q\|=4\).

**Sharp small-amplitude curvature.** Set \(c(t)=\cos(\omega t)\). For fixed \(\omega>0\), \(a_\varepsilon=1-\varepsilon c+\varepsilon^2c^2+O(\varepsilon^3)\) in operator norm, so
\[
Q=G_L+\varepsilon Q_1+\varepsilon^2Q_2+O(\varepsilon^3),\quad Q_1=-M_cG_L-G_LM_c,\quad Q_2=M_{c^2}G_L+G_LM_{c^2}+M_cG_LM_c.
\]
The eigenvalue \(4\) of \(G_L\) is simple and isolated for fixed \(\omega>0\). Put \(d=(1/4+\omega^2)^{-1}\). Then \(Q_1e_0=-(4+d)(e_1+e_{-1})/2\), \(\langle e_0,Q_1e_0\rangle=0\), and \(\langle e_0,Q_2e_0\rangle=4+d/2\). The second-order simple-eigenvalue perturbation formula therefore yields
\[
\lambda_{\max}(Q)=4+b\varepsilon^2+O_\omega(\varepsilon^3),\qquad b=4+\frac d2+\frac{(4+d)^2}{2(4-d)}=\frac{2(12+d)}{4-d}.
\]
Changing \(\varepsilon\) to \(-\varepsilon\) translates \(a_\varepsilon\) by \(L/2\), making the two operators unitarily equivalent. Analyticity of this isolated leading eigenvalue therefore removes every odd Taylor coefficient, upgrading the remainder to \(O_\omega(\varepsilon^4)\). Taking square roots gives the coefficient \(b/4=3/2+1/(2\omega^2)\), as asserted.

## Verification
The included `check.py` constructs Fourier finite sections of \(Q\) using the exact period-convolution Fourier multipliers and numerically verifies the strict bound, amplitude symmetry and second-order law at multiple frequencies. These finite checks do not replace the Hilbert--Schmidt, essential-norm, fiber-dominance, and analytic-perturbation arguments above.

## Relationship to prior work
Norrbo's 2026 analysis proves boundedness of the unmodulated critical logarithmic Hilbert integral operator and the associated Hilbert matrix/Bergman endpoint. Previously reported exact essential-norm results give the unmodulated value \(2\), and a related Copson/Fredholm spectral circle. The present assertion does *not* claim that base value, the Copson reduction, positive Green kernels, or Floquet techniques to be new. Its contribution is the explicitly log-log-periodically weighted endpoint, its global essential-norm representation by a compact circle kernel, strict amplification, and its specific sharp frequency-dependent quadratic law. Published analogues for generalized Hilbert matrices with slowly oscillating coefficients and log-log Fock Toeplitz symbols address different operators and weights; their statements do not directly imply these formulas.

## Limitations
The essential-norm identity uses an infinite-dimensional compact circle operator, not a claimed elementary closed form at arbitrary nonzero amplitude. No result is asserted for complex or sign-changing input weights, discrete Hilbert matrices, other \(L^p\) exponents, analytic Bergman spaces, or a uniform small-frequency limit. The novelty assessment has residual risk from older weighted-Hardy/Copson and periodic convolution literature; this is not an independent audit or a claim of publication priority.

## References
1. D. Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1, publicly submitted 2026-09-23; Sections 2–3, especially Proposition 3.3 and Theorem 3.5, https://arxiv.org/html/2610.00252v1.
2. G. H. Hardy, J. E. Littlewood, and G. Pólya, *Inequalities*, Cambridge University Press (1934), classical Hardy/Copson bounds.
3. Classical Floquet decomposition of periodic integral operators and analytic perturbation theory for isolated eigenvalues; used as established tools rather than as novelty claims.
