# Exact Fourier shape Hessian and angular-frequency transition for Gaussian concentration

## Finding
Fix \(R>0\). In the Bargmann–Fock space \(\mathcal F^2(\mathbb C)\), let \(\Lambda(\Omega)\) be the largest eigenvalue of localization to a planar set \(\Omega\). For every real \(h\in C^2(\mathbb T)\) of mean zero, consider the *exactly area-preserving* family
\[
\Omega_{\varepsilon,h}=\{r e^{i\theta}:0\le r^2<R+\varepsilon h(\theta)\},
\qquad |\Omega_{\varepsilon,h}|=\pi R.
\]
Let \(\widehat h_m=(2\pi)^{-1}\int_0^{2\pi}h(\theta)e^{-im\theta}\,d\theta\), and define
\[
S_m(R)=\sum_{j=1}^{m}\frac{R^j}{j!},\qquad
\Phi_1(R)=0,\qquad \Phi_m(R)=\frac{S_{m-1}(R)}{S_m(R)}\ (m\ge2).
\]
Then the first concentration-eigenvalue deficit has the **exact full angular Fourier Hessian**
\[
\boxed{\lim_{\varepsilon\to0}
\frac{1-e^{-R}-\Lambda(\Omega_{\varepsilon,h})}{\varepsilon^2}
=e^{-R}\sum_{m=2}^{\infty}\Phi_m(R)|\widehat h_m|^2.}
\tag{1}
\]
Its multipliers satisfy \(0<\Phi_2(R)<\Phi_3(R)<\cdots<1\) and \(\Phi_m(R)\uparrow1\) for each fixed \(R\). Consequently, with \(\Pi_1h\) the orthogonal projection onto \(\operatorname{span}\{\cos\theta,\sin\theta\}\),
\[
\boxed{\lim_{\varepsilon\to0}
\frac{1-e^{-R}-\Lambda(\Omega_{\varepsilon,h})}{\varepsilon^2}
\ge\frac{e^{-R}}{R+2}\,\|h-\Pi_1h\|_{L^2(d\theta/2\pi)}^2.}
\tag{2}
\]
The constant is best possible and equality in the *second-order coefficient* holds exactly when \(h\) contains no angular harmonics beyond degrees one and two. Pure quadratic harmonics attain the sharp nontranslational coefficient; the first harmonics are the translational null directions.

For any integer sequence \(m(R)\ge2\) with \(R\to\infty\) and \(m(R)/R\to\alpha\in[0,\infty]\), the Hessian multiplier exhibits the sharp angular-band transition
\[
\boxed{\Phi_{m(R)}(R)\longrightarrow \min\{\alpha,1\},}
\tag{3}
\]
with the right-hand side interpreted as \(1\) when \(\alpha=\infty\). Thus the boundary Fourier mode at scale \(m\asymp R\) marks the transition from soft to saturated local concentration curvature.

## Assumptions and scope
The Fock Hilbert space has norm \(\|F\|^2=\pi^{-1}\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z)\). The spectral concentration functional is
\[
\Lambda(\Omega)=\sup_{\|F\|=1}\frac1\pi\int_\Omega|F(z)|^2e^{-|z|^2}\,dA(z).
\]
Here \(R>0\) is fixed for the shape expansion, \(h\) is real and twice continuously differentiable with \(\widehat h_0=0\), and \(|\varepsilon|\|h\|_\infty<R\). Polar coordinates give \(|\Omega_{\varepsilon,h}|=\frac12\int_0^{2\pi}(R+\varepsilon h(\theta))\,d\theta=\pi R\) without an order-two area correction. Fourier coefficients and norms are normalized with measure \(d\theta/(2\pi)\). Formula (1) concerns one *fixed* \(h\) as \(\varepsilon\to0\); it does not state uniform control over arbitrarily varying rough boundaries. The subsequent asymptotic (3) concerns only the explicitly determined multipliers.

## Proof
**1. Circular spectral gap.** In the orthonormal Fock monomial basis \(e_k(z)=z^k/\sqrt{k!}\) for integers \(k\ge0\), the disk \(\Omega_{0,h}=\{|z|^2<R\}\) has diagonal localization spectrum
\[
\lambda_k(R)=\frac1{k!}\int_0^Re^{-t}t^k\,dt
=1-e^{-R}\sum_{j=0}^k\frac{R^j}{j!}.
\]
The top eigenvalue \(\lambda_0=1-e^{-R}\) is simple and isolated, with \(\lambda_0-\lambda_k=e^{-R}S_k(R)>0\) for all \(k\ge1\). Its eigenvector is the constant function \(e_0\).

**2. Trace-class shape differentiability.** The localization operator can be written as an integral of rank-one normalized Fock coherent projectors. On the compact annulus traced by the moving boundary, these projectors depend smoothly on radius and angle in trace norm. Differentiating their radial integrals therefore gives a \(C^2\) family of compact self-adjoint operators in trace norm, and the ordinary isolated-eigenvalue perturbation formula applies. More explicitly, its monomial matrix elements are
\[
T_{jk}(\varepsilon)=\frac1{2\pi\sqrt{j!k!}}\int_0^{2\pi}
 e^{i(k-j)\theta}
 \left(\int_0^{R+\varepsilon h(\theta)}
 e^{-t}t^{(j+k)/2}\,dt\right)d\theta.
\]
Their first derivatives satisfy
\[
T'_{j0}(0)=\frac{e^{-R}R^{j/2}}{\sqrt{j!}}\widehat h_j,
\qquad T'_{00}(0)=e^{-R}\widehat h_0=0,
\]
where the conjugate alternative for the Fourier coefficient gives identical absolute squares. The second derivative at the leading eigenvector is \(T''_{00}(0)=-e^{-R}(2\pi)^{-1}\int h(\theta)^2\,d\theta\).

**3. The optimized-eigenfunction correction.** Rayleigh–Schrödinger perturbation for the isolated top eigenvalue, with the whole infinite orthogonal complement retained, gives
\[
\Lambda''(0)=\langle e_0,T''(0)e_0\rangle
+2\sum_{k\ge1}\frac{|T'_{k0}(0)|^2}{\lambda_0-\lambda_k}
=-e^{-R}\|h\|_2^2
+2e^{-R}\sum_{k\ge1}\frac{R^k/k!}{S_k(R)}|\widehat h_k|^2.
\]
This series converges absolutely: its spectral denominators are bounded below by the strictly positive first gap, and \(\sum|T'_{k0}|^2<\infty\). Because \(h\) is real and mean zero, Parseval gives \(\|h\|_2^2=2\sum_{k\ge1}|\widehat h_k|^2\). Thus
\[
\Lambda''(0)=-2e^{-R}\sum_{k\ge1}
\left(1-\frac{R^k/k!}{S_k(R)}\right)|\widehat h_k|^2.
\]
The degree-one multiplier vanishes, and the others equal \(\Phi_k(R)\). Taylor expansion yields (1). In particular, for the test profile \(h(\theta)=\cos(2\theta)\), the exact coefficient equals \(e^{-R}/[2(R+2)]\).

**4. Strict multiplier ordering and sharpness.** Set \(a_m=R^m/m!\). Directly,
\[
\frac{S_m}{a_m}=\sum_{r=0}^{m-1}\frac{m(m-1)\cdots(m-r+1)}{R^r}.
\]
Every existing summand strictly increases when \(m\) is incremented (except the first), and a positive new summand appears, so \(S_m/a_m\) strictly increases. Hence \(\Phi_m=1-a_m/S_m\) strictly increases from \(\Phi_1=0\), with \(\Phi_2=2/(R+2)\), toward \(1\). Applying its minimum on degrees at least two and Parseval proves (2), including exact equality and sharpness conditions.

**5. The high-area edge scale.** If \(m/R\to\alpha<1\), the falling-factorial formula is dominated by a summable geometric series with ratio strictly below one, and each fixed summand tends to \(\alpha^r\). Dominated convergence gives \(S_m/a_m\to (1-\alpha)^{-1}\), so \(\Phi_m\to\alpha\). If \(m/R\to\alpha\ge1\), every fixed initial collection of summands has limiting sum \(\sum_{r=0}^K\alpha^r\), which diverges as \(K\to\infty\); hence \(S_m/a_m\to\infty\), giving \(\Phi_m\to1\). The same argument covers \(\alpha=\infty\) by eventual lower bounds. This proves (3) without assuming any simultaneous uniformity in \(m\), \(R\), or \(h\).

## Verification
Independent numerical checks construct the finite monomial localization matrix by direct angular quadrature of the radial incomplete-gamma integrals and compute its top eigenvalue, without feeding the Hessian into the matrix calculation. The standalone `shape_hessian_checker.py` compares twelve single-frequency perturbations, two mixed-frequency perturbations, twelve large-area coefficient tests, and monotonicity at four radii. The tests pass when run with Python, NumPy and SciPy. In the representative case \(R=1\), \(h(\theta)=\cos(2\theta)\), the predicted quadratic coefficient is \(e^{-1}/6=0.061313240195240384\ldots\). Finite truncation and finite \(\varepsilon\) are checks of normalization, not proofs of the infinite-dimensional assertions.

## Relationship to prior work
Nicola–Tilli proved the global Gaussian-STFT Faber–Krahn inequality and sharp disk spectral optimum. Gómez–Guerra–Ramos–Tilli established quantitative shape/function stability and computed second variations of a **different optimized-superlevel functional** (Sect. 5, Eq. (5.20)–(5.21)); those negative coefficients involve \(S_{m-1}(R)\), whereas the present first-*fixed-domain-eigenvalue* Hessian has the essential extra spectral-gap factor \(1/S_m(R)\). Ramos (2026) constructs noncircular localization domains with prescribed near-Gaussian eigenfunctions, shows sharpness of a square-root stability exponent, and proves local maximizers are disks using first shape variations; its inspected main results and pertinent sections do not state (1), (2), or the frequency transition (3). Nicola–Riccardi analyzes the **Hilbert–Schmidt norm** of localization, a different spectral objective. These comparisons distinguish the present claims from prior qualitative rigidity and from different second-variation functionals, but do not certify historical priority against every unindexed work.

## Limitations
The complete shape expansion is local, for smooth polar-graph perturbations of one disk and the *largest* Gaussian localization eigenvalue. It is not a global nonlinear deficit estimate, nor a claim for other windows, multiply connected sets, arbitrary rough boundary perturbations, higher eigenvalues, or simultaneous large-area shape families. The spectral transition is an asymptotic of the exact Hessian coefficients, not an interchange of the shape and large-area limits. Independent verification and full historical-priority certification have not been performed.

## References
1. J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, arXiv:2607.21590 (first public version 2026-07-23). https://arxiv.org/abs/2607.21590
2. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber-Krahn inequality for the short-time Fourier transform*, arXiv:2307.09304 (first public version 2023-07-18); Invent. Math. 236 (2024), 779–836. https://link.springer.com/article/10.1007/s00222-024-01248-2
3. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, arXiv:2106.03423 (2021); Invent. Math. 230 (2022), 1–30. https://link.springer.com/article/10.1007/s00222-022-01119-8
4. F. Nicola and F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, arXiv:2401.04659 (2024); J. Fourier Anal. Appl. 31 (2025). https://link.springer.com/article/10.1007/s00041-025-10145-y
