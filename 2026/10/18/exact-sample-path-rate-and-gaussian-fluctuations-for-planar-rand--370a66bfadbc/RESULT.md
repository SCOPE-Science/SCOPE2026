# Exact sample-path rate and Gaussian fluctuations for planar randomized residual line search

## Finding
Let \(A\) be a real \(2\times2\) symmetric positive-definite matrix with eigenvalues \(0<a\le b\), and write
\[
q=\frac{b-a}{b+a}\in[0,1),\qquad \beta=\frac{2q}{1+q^2}.
\]
For any deterministic nonzero residual \(r_0\), draw independent \(d_k\sim N(0,I_2)\) and perform exact residual line search
\[
\alpha_k=\frac{r_{k-1}^{\mathsf T}Ad_k}{\|Ad_k\|_2^2},\qquad r_k=r_{k-1}-\alpha_kAd_k.
\]
Then almost surely
\[
\lim_{n\to\infty}\frac1n\log\frac{\|r_n\|_2^2}{\|r_0\|_2^2}
=\mu(q):=2\log\frac{1+q^2}{2}<0.
\]
Moreover, with \(\operatorname{Li}_2(z)=\sum_{m\ge1}z^m/m^2\) for \(|z|\le1\),
\[
\frac{\log(\|r_n\|_2^2/\|r_0\|_2^2)-n\mu(q)}{\sqrt n}
\ \Longrightarrow\ N(0,\sigma^2(q)),
\quad \sigma^2(q)=\frac{\pi^2}{3}+2\operatorname{Li}_2(q^4)
+4\operatorname{Li}_2(\beta^2)-8\operatorname{Li}_2(\beta q)>0.
\]
This is an exact almost-sure convergence law and central limit theorem despite the independently generated direction having no information about the linear-system residual. At \(q=0\), the typical one-step squared-residual factor is \(1/4\), versus the mean-square factor \(1/2\).

## Assumptions and scope
The system \(Ax=b_0\) has a unique solution because \(A\) is invertible; \(r_k=b_0-Ax_k\). Gaussian correction directions have independent, isotropic, nondegenerate laws, with exact arithmetic and exact residual-minimizing line searches. The iteration is defined for all \(k\ge1\) almost surely. The theorem includes the isotropic case \(a=b\), excludes singular matrices, and concerns the residual Euclidean norm rather than componentwise errors. No noisy evaluation of the residual or line-search scalar is assumed. The logarithm is finite at every finite iteration almost surely. The probability measure includes all Gaussian direction draws, not the initial residual.

## Proof
**Projection reduction.** Rotate into the eigenbasis of \(A\), permissible by Gaussian rotational invariance. Put \(w_k=Ad_k\). Exact minimization gives \(r_k=(I-w_kw_k^{\mathsf T}/\|w_k\|_2^2)r_{k-1}\). Let \(u_k\) be the unit vector perpendicular to \(w_k\), with angle \(\phi_k\) modulo \(\pi\). The orthogonal projector is \(u_ku_k^{\mathsf T}\); for the angle \(\phi_0\) of \(r_0\),
\[
\frac{\|r_n\|_2^2}{\|r_0\|_2^2}
=\cos^2(\phi_1-\phi_0)\prod_{k=2}^n\cos^2(\phi_k-\phi_{k-1}). \tag{1}
\]
Every cosine is nonzero almost surely. Write \(\theta_k=2\phi_k\pmod{2\pi}\). A change of variable in the Gaussian angle, using the ellipse with semiaxes \(a,b\), gives the Poisson-kernel law
\[
\Pr(\theta_k\in dt)=\frac{1-q^2}{2\pi(1-2q\cos t+q^2)}\,dt,\qquad \mathbb E e^{im\theta_k}=q^{|m|}. \tag{2}
\]
The possible \(\pi/2\) rotation in defining the perpendicular direction is immaterial to angle *differences*: choose the coordinate axes so that its Poisson center is zero. For clarity, (2) follows directly from \(\theta=2\arctan((b/a)\tan\psi)\) after accounting for the perpendicular shift; explicitly the density is a constant times \((a^2\cos^2\phi+b^2\sin^2\phi)^{-1}\), and elementary double-angle algebra identifies \(q=(b-a)/(b+a)\). Under the diagonal-axis convention the sign or a fixed angular rotation changes but never affects the difference laws or their covariance.

**Stationary one-dependent increments.** Set \(g(t)=\log\cos^2(t/2)\), and \(X_k=g(\theta_k-\theta_{k-1})\) for \(k\ge2\). Because each \(X_k\) depends only on the independently drawn pair \((\theta_{k-1},\theta_k)\), this sequence is strictly stationary and one-dependent. Its second moment is finite: the only singularity is logarithmic at \(t=\pi\), and the density in (2) is bounded for every \(q<1\). The first term in (1) is a fixed-in-\(n\), almost surely finite random variable and disappears after dividing by \(n\) or \(\sqrt n\). Standard strong laws for one-dependent integrable sequences and the central limit theorem for one-dependent square-integrable sequences apply.

**Exact logarithmic drift.** The difference \(\theta_k-\theta_{k-1}\) has Fourier coefficients \(q^{2|m|}\), hence is distributed according to the Poisson kernel with parameter \(q^2\). In \(L^2\) one has
\[
g(t)=-2\log 2+2\sum_{m=1}^\infty\frac{(-1)^{m-1}}m\cos(mt).
\]
Poisson averaging (or the harmonic mean-value formula) yields \(\mathbb E X_k=-2\log2+2\log(1+q^2)=\mu(q)\). As \(q<1\), the drift is strictly negative. The one-dependent strong law and (1) prove the almost-sure assertion.

**Exact one-dependent fluctuation variance.** Write \(V=\operatorname{Var}(X_2)\) and \(C=\operatorname{Cov}(X_2,X_3)\). Differentiating the classical Poisson integral of \(|1+e^{it}|^{2s}\) twice at \(s=0\), or expanding the logarithmic Fourier series and summing absolutely after radial regularization, gives
\[
V=\frac{\pi^2}{3}+4\operatorname{Li}_2(-q^2). \tag{3}
\]
Conditional on the common angle \(\theta_2\), the variables \(X_2\) and \(X_3\) are independent, with the same conditional mean
\[
h(\theta)=-2\log2+2\log|1+qe^{i\theta}|.
\]
Thus \(C=\operatorname{Var}(h(\theta_2))\ge0\). The Poisson-law parameterization \(e^{i\theta_2}=(q+\zeta)/(1+q\zeta)\), with \(\zeta\) uniform on the circle, transforms
\[
1+q e^{i\theta_2}=(1+q^2)\frac{1+\beta\zeta}{1+q\zeta}.
\]
For \(u,v\in[0,1)\), Fourier orthogonality gives the exact identity
\[
\operatorname{Cov}_\zeta(\log|1+u\zeta|,\log|1+v\zeta|)
=\tfrac12\operatorname{Li}_2(uv).
\]
Therefore
\[
C=2\bigl[\operatorname{Li}_2(\beta^2)+\operatorname{Li}_2(q^2)-2\operatorname{Li}_2(\beta q)\bigr]. \tag{4}
\]
The variance in the one-dependent central limit theorem is \(V+2C\). Using \(\operatorname{Li}_2(z)+\operatorname{Li}_2(-z)=\tfrac12\operatorname{Li}_2(z^2)\) yields the displayed \(\sigma^2(q)\). It is positive: for any \(q<1\), the stationary increments have nondegenerate conditional variability given \(\theta_2\); also \(\sigma^2=V+2C\ge V>0\), because the difference-angle density is strictly positive and \(g\) is not constant. The central limit theorem follows.

**Strict difference from the expected squared rate.** The earlier fourth-moment transfer for this same planar Gaussian projection model has Perron root
\[
\rho(q)=\frac{3+q^2+\sqrt{1+14q^2+q^4}}8.
\]
The typical factor is \(e^{\mu(q)}=(1+q^2)^2/4\), strictly smaller than \(\rho(q)\) for \(q<1\); for \(q=0\) compare \(1/4<1/2\), and for \(q>0\) put \(s=q^2\), square the two sides where permissible, and use
\[
\bigl(2(1+s)^2-(3+s)\bigr)^2-(1+14s+s^2)=4s(s-1)(s^2+4s+5)<0.
\]
A negative unsquared left-hand side also implies the desired strict inequality. This comparison supplies context, not a separate novelty claim.

## Verification
`verify.py` reproduces the fourth-moment transfer characteristic polynomial symbolically, tests the displayed variance decomposition, evaluates three independent angular integrals (drift, one-increment variance, adjacent-increment covariance) at seven anisotropy values, and checks four sets of direct standard-Gaussian projection simulations. Install packages in `requirements.txt` and run `python verify.py`. The infinite-horizon conclusions rely on the analytic one-dependent strong law and central limit theorem; finite simulations are only consistency checks.

## Relationship to prior work
Wu, Squillante, Kalantzis, and Horesh (2023), *Stable iterative refinement algorithms for solving linear systems*, introduce exact residual line search to avoid divergence for inaccurate linear-system corrections. Their analysis establishes nonincrease in residual norm and convergence under accuracy conditions on the basic correction, but not the exact almost-sure rate or fluctuation distribution under entirely uninformative independent Gaussian corrections. Stich, Müller, and Gärtner (2011), *Optimization of Convex Functions with Random Pursuit*, analyze random-direction exact line search with expected convergence-rate bounds rather than this planar pathwise log-normal fluctuation law. Fridovich-Keil and Recht (2020), *Approximately Exact Line Search*, study approximate line search and general convergence rates. A prior exact *mean-square* planar Gaussian projection calculation determines \(\rho(q)\) but does not imply either the pathwise exponent or the one-dependent asymptotic variance. The present contribution is the explicit sample-path law with its closed dilogarithmic central-limit variance, not the mean-square transfer result or the generic fact of random-projection convergence.

## Limitations
Restricted to two real dimensions, SPD \(A\), isotropic Gaussian correction directions, and exact residual minimization in exact arithmetic. Gaussian components are independent over iterations; correlated, adversarial, heavy-tailed, approximate, or deterministic corrections need separate analysis. The exact logarithmic CLT does not give finite-time Gaussian error bounds. The proof is not an assertion of independent validation or of the absence of all unindexed equivalent literature.

## References
1. C. W. Wu, M. S. Squillante, V. Kalantzis, L. Horesh, *Stable iterative refinement algorithms for solving linear systems*, arXiv:2309.07865, first submitted 2023-09-14. https://arxiv.org/abs/2309.07865
2. S. U. Stich, C. L. Müller, B. Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194, first submitted 2011-11-01. https://arxiv.org/abs/1111.0194
3. D. Fridovich-Keil, B. Recht, *Approximately Exact Line Search*, arXiv:2011.04721, first submitted 2020-11-09. https://arxiv.org/abs/2011.04721
4. Classical strong law and central limit theorem for stationary one-dependent sequences; standard Fourier/Poisson-kernel identities.
