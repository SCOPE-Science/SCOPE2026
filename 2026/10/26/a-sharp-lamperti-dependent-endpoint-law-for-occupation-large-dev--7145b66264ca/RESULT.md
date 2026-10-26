# A sharp Lamperti-dependent endpoint law for occupation large deviations under Poisson resetting

## Finding
Fix a sluggishness exponent \(\alpha\geq0\), write \(\mu=1/(\alpha+2)\in(0,1/2]\), and fix a resetting rate \(r>0\). For the continuum sluggish diffusion reset to the origin at independent Poisson times, let \(A_T=\int_0^T\mathbf1_{\{X_t>0\}}\,dt\) and \(Z_T=A_T/T\). The complete sequence \((Z_T)_{T\to\infty}\) obeys a speed-\(T\) large-deviation principle with a good, symmetric rate function \(I_{\mu,r}\) on \([0,1]\).

For every real \(k\), the asymptotic cumulant generating function \(\psi_{\mu,r}(k)=\lim_{T\to\infty}T^{-1}\log\mathbb E[e^{kA_T}]\) is the unique real \(s\) with \(s+r>\max\{k,0\}\) satisfying
\[
(s-k)(s+r-k)^{\mu-1}+s(s+r)^{\mu-1}=0.
\]
Its Legendre transform is \(I_{\mu,r}(x)=\sup_{k\in\mathbb R}\{kx-\psi_{\mu,r}(k)\}\). The rate is strictly convex and real analytic on \((0,1)\), satisfies \(I_{\mu,r}(x)=I_{\mu,r}(1-x)\), and has the unique minimum \(I_{\mu,r}(1/2)=0\). At its endpoints, \(I_{\mu,r}(0)=I_{\mu,r}(1)=r\), with the **sharp cusp**
\[
I_{\mu,r}(1-\delta)=I_{\mu,r}(\delta)
=r-r\,\mu^{-\mu}(1-\mu)^{\mu-1}\delta^{\mu}+o(\delta^{\mu})
\qquad(\delta\downarrow0).
\]
At the center,
\[
I_{\mu,r}(1/2+\varepsilon)=\frac r{1-\mu}\varepsilon^2+O(\varepsilon^4).
\]
In particular, for \(\alpha>0\) the singular endpoint exponent is strictly below the Brownian value \(1/2\), although resetting still yields Gaussian-scale central fluctuations.

For explicit evaluation without an optimization solver, for every \(z>0\) define
\[
s(z)=r\frac{(1-z)z^{\mu-1}}{1+z^\mu},\qquad
k(z)=r\frac{(1-z)(1+z^{\mu-1})}{1+z^\mu}.
\]
As \(z\) ranges over \((0,\infty)\), \(x(z)=s'(z)/k'(z)\) runs continuously from \(1\) to \(0\), and \(I_{\mu,r}(x(z))=k(z)x(z)-s(z)\). The value at \(z=1\) is interpreted continuously: \(x=1/2\), \(I=0\).

## Assumptions and scope
The free process is the symmetric origin-started continuum sluggish diffusion with forward equation \(\partial_t p=\partial_x^2(|x|^{-\alpha}p)\), equivalently backward generator \(\mathcal Lf(x)=|x|^{-\alpha}f''(x)\) away from the origin, endowed with the symmetric origin matching used in the cited free-diffusion theory. Its origin-started positive occupation fraction over any deterministic interval of length \(u>0\) has the exact Lamperti density
\[
f_\mu(y)=\frac{\sin(\pi\mu)}\pi\frac{[y(1-y)]^{\mu-1}}{y^{2\mu}+(1-y)^{2\mu}+2[y(1-y)]^\mu\cos(\pi\mu)},\qquad 0<y<1.
\]
Poisson resets are independent of free paths and reset position to zero; between resets fresh independent copies of the specified diffusion evolve. All assertions concern this continuum process with fixed finite \(r>0\), \(\alpha\ge0\), and observation time \(T\to\infty\). No analogous claim is made for a finite lattice time step or for threshold-triggered resetting.

## Proof
**1. A free-cycle transform.** Let \(Y\) have density \(f_\mu\). The exact scaling of free occupation time implies \(\int_0^u\mathbf1_{\{X_t>0\}}dt\overset d=uY\) for every \(u>0\). The established Lamperti Stieltjes transform, for \(q>\max\{k,0\}\), is
\[
G_\mu(q,k)=\mathbb E\frac1{q-kY}
=\frac{(q-k)^{\mu-1}+q^{\mu-1}}{(q-k)^\mu+q^\mu}.
\]
This identity follows independently by replacing the Laplace variable for occupation by \(-k\) in the free double-Laplace transform; its integral representation guarantees positivity and the correct real branch.

**2. Renewal growth and uniqueness.** Let \(M_k(T)=\mathbb E[e^{kA_T}]\), \(H_k(u)=e^{-ru}\mathbb E[e^{kuY}]\). Conditioning on the first reset gives the exact renewal equation
\[
M_k(T)=H_k(T)+r\int_0^T H_k(u)M_k(T-u)\,du.
\]
For fixed real \(k\), the function \(s\mapsto rG_\mu(s+r,k)\) strictly decreases from \(+\infty\) to \(0\) on \(s+r>\max\{k,0\}\): the divergence at the lower boundary follows from the strictly positive Lamperti density behaving as a positive multiple of \(y^{\mu-1}\) or \((1-y)^{\mu-1}\), while \(\mu<1\). It therefore has exactly one root \(s=\psi(k)\) of \(rG_\mu(s+r,k)=1\). The displayed polynomial-in-fractional-powers equation is simply the denominator-cleared form of this root identity.

Set \(h_k(u)=r e^{-(r+\psi(k))u}\mathbb E[e^{kuY}]\). It is a continuous strictly positive probability density with finite positive mean, since \(r+\psi(k)>\max\{k,0\}\). The exponentially tilted renewal equation for \(e^{-\psi(k)T}M_k(T)\) has directly Riemann-integrable forcing \(e^{-\psi(k)T}H_k(T)\). The nonarithmetic key renewal theorem gives convergence to a finite positive constant. Consequently \(T^{-1}\log M_k(T)\to\psi(k)\), with no reliance on a guessed pole or unproved interchange of limits.

**3. Analyticity and the full LDP.** Implicit differentiation of \(\mathbb E[e^{kLY-\psi(k)L}]=1\), with independent \(L\sim\operatorname{Exp}(r)\) and \(Y\sim f_\mu\), shows
\[
\psi'(k)=\frac{\mathbb E[LYe^{kLY-\psi(k)L}]}{\mathbb E[Le^{kLY-\psi(k)L}]},\qquad
\psi''(k)=\frac{\mathbb E[L^2(Y-\psi'(k))^2 e^{kLY-\psi(k)L}]}{\mathbb E[Le^{kLY-\psi(k)L}]}>0.
\]
The same exponential integrability gives real analyticity by the implicit-function theorem. Reflection \(Y\overset d=1-Y\) gives \(\psi(k)=k+\psi(-k)\). The root equation gives \(\psi(k)=k-r+o(1)\) as \(k\to+\infty\), and by symmetry \(\psi(k)=-r+o(1)\) as \(k\to-\infty\). Therefore \(\psi'(k)\to1\) and \(0\) at the respective ends. Since \(Z_T\in[0,1]\) has compact support and \(\psi\) is finite differentiable on all of \(\mathbb R\), the differentiable Gärtner–Ellis theorem gives the full speed-\(T\) LDP and the strictly convex analytic interior rate. Convexity and one-sided continuity establish the endpoint values, and the asymptotic cumulant slopes establish \(I(0)=I(1)=r\). Outside \([0,1]\) the rate is \(+\infty\).

**4. Sharp edge.** For \(k\to+\infty\) write \(\psi(k)=k-r+e_k\), with \(0<e_k<r\). The root equation becomes
\[
(r-e_k)e_k^{\mu-1}=(k-r+e_k)(k+e_k)^{\mu-1},
\]
which implies \(e_k\sim r^{1/(1-\mu)}k^{-\mu/(1-\mu)}\). For \(x=1-\delta\), Legendre duality now gives
\[
I(1-\delta)=r-\inf_{k>0}\{k\delta+e_k\}
\]
when \(\delta\) is sufficiently small (the minimizer then tends to \(+\infty\)). Minimizing the regular-varying leading terms yields \(\inf\{k\delta+Ck^{-a}\}\sim (a+1)a^{-a/(a+1)}C^{1/(a+1)}\delta^{a/(a+1)}\), where \(a=\mu/(1-\mu)\) and \(C=r^{1/(1-\mu)}\). This simplifies to the stated coefficient \(r\mu^{-\mu}(1-\mu)^{\mu-1}\). Reflection gives the other endpoint.

**5. Central curvature and parametric form.** At \(k=0\), \(\psi'(0)=\mathbb EY=1/2\). The known Lamperti variance \(\operatorname{Var}Y=(1-\mu)/4\), together with \(\mathbb EL=1/r\) and \(\mathbb EL^2=2/r^2\), gives \(\psi''(0)=(1-\mu)/(2r)\). Legendre duality and reflection then give the displayed quadratic expansion (odd centered terms vanish). Finally, set \(z=(\psi+r-k)/(\psi+r)>0\) in the root equation; solving for \(k\) and \(\psi\) gives the stated parametric formulas. Strict convexity makes \(k'(z)\ne0\) and supplies their monotone interior parametrization.

## Verification
Run `python verify.py` with Python 3 and SciPy installed. It independently evaluates the Lamperti Stieltjes integral by regularized quadrature, solves the real renewal root equation numerically across three sluggishness parameters and three reset rates, checks the reflection identity and the explicit Brownian limit, tests the parametric Legendre rate, and examines the normalized sharp-edge constant. These are finite corroborations, not substitutes for the all-parameter renewal and convex-duality proof.

## Relationship to prior work
Del Vecchio and Majumdar (arXiv:2410.22097v1, October 29, 2024) obtained the exact free-sluggish Lamperti occupation distribution and Stieltjes transform. Frimpong, Bresque and Roldán (arXiv:2610.21962v1, October 15, 2026) derived the resetting occupation double-Laplace transform and its Gaussian central-limit scaling; these are inputs, not claimed novelties. Den Hollander, Majumdar, Meylahn and Touchette (arXiv:1801.09909, 2018) established the exact Brownian Poisson-reset occupation large-deviation function. Zamparo (arXiv:2207.07521, 2022) supplies a general rigorous renewal-reward large-deviation framework. The contribution here is the explicit all-sluggishness scaled cumulant root and parametric full rate together with the sharp \(\mu\)-dependent endpoint cusp, absent from the inspected formulations. The \(\mu=1/2\) case reduces to the already-known Brownian expression \(I_{1/2,r}(x)=r(1-2\sqrt{x(1-x)})\).

## Limitations
The theorem applies to independent exponential resets of the symmetric origin-started continuum sluggish diffusion, not discrete microscopic dynamics, spatially variable reset rates, or non-Poisson intervals. A general renewal-reward theorem already establishes abstract LDP machinery, so no priority is claimed for that general principle or for the Brownian special case. The explicit cusp concerns the fixed-parameter limit \(\delta\downarrow0\) after the long-time limit; it does not provide uniform finite-time error bounds or trajectory-level large deviations. No independent audit or literature-wide priority certification has been performed.

## References
1. G. Del Vecchio and S. N. Majumdar, *Generalized arcsine laws for a sluggish random walker with subdiffusive growth*, arXiv:2410.22097v1 (first publicly posted 2024-10-29), https://arxiv.org/html/2410.22097v1 .
2. T. D. Frimpong, L. Bresque and E. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (first publicly posted 2026-10-15), https://arxiv.org/html/2610.21962v1 .
3. F. den Hollander, S. N. Majumdar, J. M. Meylahn and H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (2018), https://arxiv.org/abs/1801.09909 .
4. M. Zamparo, *Statistical fluctuations under resetting: rigorous results*, arXiv:2207.07521 (2022), https://arxiv.org/abs/2207.07521 .
5. P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, arXiv:2009.01968 (2020), https://arxiv.org/abs/2009.01968 .
