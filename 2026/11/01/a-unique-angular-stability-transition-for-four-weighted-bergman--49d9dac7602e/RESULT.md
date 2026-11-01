# A unique angular-stability transition for four weighted Bergman poles

## Finding
For every real \(\alpha>0\), let \(\mathcal E_\alpha\) be the normalized squared weighted Bergman norm of the sum of four unit-residue Cauchy kernels with poles on the unit circle (defined below). At the regular square, let \(\lambda_1(\alpha)\) be its doubly occurring first angular Fourier-mode Hessian eigenvalue and \(\lambda_2(\alpha)\) its alternating-mode eigenvalue. There is exactly one \(\alpha_*\in(2,3)\) such that \(\lambda_1(\alpha_*)=\lambda_2(\alpha_*)\); numerically \(\alpha_*=2.7278417359345863\ldots\). Below this weight the first angular mode is the uniquely softest nonrotational representation; above it the alternating mode is uniquely softest. At the transition, the Hessian is a positive scalar on the full three-dimensional rotation-orthogonal subspace, so the local angular condition number is exactly one. The condition number grows asymptotically as \(\alpha/8\) for large weights.

More explicitly, define positive functions
\[
 u_\alpha=4(\alpha+1)\int_0^1\frac{t(1-t^2)(1-t)^\alpha}{(1+t^2)^3}\,dt,
 \qquad v_\alpha=(\alpha+1)\int_0^1\frac{(1-t)^{\alpha+1}}{(1+t)^3}\,dt.
\]
Then
\[
 \boxed{\lambda_1(\alpha)=4(u_\alpha+v_\alpha)\quad\text{(multiplicity 2)},\qquad
 \lambda_2(\alpha)=8u_\alpha\quad\text{(multiplicity 1)}.}
\]
The crossing is the unique solution of \(u_\alpha=v_\alpha\). The sharp quadratic local stability coefficient, after quotienting common rotation, is
\[
 \boxed{c_\alpha=\tfrac12\min\{4(u_\alpha+v_\alpha),8u_\alpha\}>0.}
\]

## Assumptions and scope
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), take unnormalized planar area \(dA\), and fix \(\alpha>0\). For any four distinct real pole angles \(\boldsymbol\theta=(\theta_0,\theta_1,\theta_2,\theta_3)\), define
\[
 \mathcal E_\alpha(\boldsymbol\theta)
 =\frac{\alpha+1}{\pi}\int_{\mathbb D}
 \left|\sum_{j=0}^3\frac{1}{z-e^{i\theta_j}}\right|^2(1-|z|^2)^\alpha\,dA(z).
\]
The reference square is \(\theta_j^\star=j\pi/2\). Eigenvalues refer to the ordinary real Hessian in radians, not to a gauge-fixed three-coordinate Hessian. One zero eigenvalue is forced by common rotation. A sharp local statement means the optimal leading quadratic coefficient in the full rotation-orthogonal tangent space; no assertion of a global uniform quadratic estimate is made. The primary MSC2020 class is \(30\mathrm H20\) (Bergman spaces).

## Proof
**Bergman moments and interaction.** Expanding each Cauchy kernel in powers of \(z\) gives a norm-convergent series, since \(\alpha>0\). Orthogonality of monomials and radial integration imply
\[
 \mathcal E_\alpha(\boldsymbol\theta)
 =\sum_{p=1}^\infty(\alpha+1)\mathrm B(p,\alpha+1)
 \left|\sum_{j=0}^3e^{-ip\theta_j}\right|^2
 =C_\alpha+2\sum_{0\le j<k\le3}\phi_\alpha(\theta_j-\theta_k),
\]
where \(C_\alpha=4\sum_{p\ge1}(\alpha+1)\mathrm B(p,\alpha+1)\) and
\[
 \phi_\alpha(\vartheta)
 =(\alpha+1)\int_0^1(1-t)^\alpha\operatorname{Re}
 \frac{e^{i\vartheta}}{1-te^{i\vartheta}}\,dt.
\]
For angles separated from collisions, the integral and all its angular derivatives are locally uniformly bounded, so differentiation beneath the integral is legitimate. Twice differentiating gives
\[
 \phi_\alpha''(\vartheta)
 =-(\alpha+1)\int_0^1(1-t)^\alpha
 \operatorname{Re}\frac{e^{i\vartheta}(1+te^{i\vartheta})}{(1-te^{i\vartheta})^3}\,dt.
\]
Substitution yields \(\phi_\alpha''(\pi/2)=u_\alpha>0\), \(\phi_\alpha''(\pi)=v_\alpha>0\), and \(\phi_\alpha''(3\pi/2)=u_\alpha\). These identities hold for **every** \(\alpha>0\), even though the pair interaction need not be convex at other angles for \(\alpha>1\).

**The actual Hessian.** Cyclic symmetry and rotation invariance make the square stationary. For the standard basis \(e_0,\ldots,e_3\), its Hessian is
\[
 H_\alpha=2u_\alpha\sum_{j=0}^3(e_j-e_{j+1}) (e_j-e_{j+1})^{\mathsf T}
 +2v_\alpha\sum_{j=0}^1(e_j-e_{j+2})(e_j-e_{j+2})^{\mathsf T},
\]
with cyclic indices in the first sum. This is a four-cycle Laplacian plus the two opposite chords. Substituting the constant, first Fourier, and alternating vectors gives the exact spectrum
\[
 \{0,\;4(u_\alpha+v_\alpha),\;4(u_\alpha+v_\alpha),\;8u_\alpha\}.
\]
The eigenvalue difference is \(\lambda_2-\lambda_1=4(u_\alpha-v_\alpha)\).

**Exactly one modal crossover.** Since \(v_\alpha>0\), introduce a probability measure \(\nu_\alpha\) on \((0,1)\) with density proportional to \((1-t)^{\alpha+1}(1+t)^{-3}\). Direct division of the integrands yields
\[
 \frac{u_\alpha}{v_\alpha}
 =\int_0^1R(t)\,d\nu_\alpha(t),\qquad
 R(t)=\frac{4t(1+t)^4}{(1+t^2)^3}.
\]
The logarithmic derivative
\[
 \frac{R'(t)}{R(t)}
 =\frac{(1-t)(1+6t+t^2)}{t(1+t)(1+t^2)}>0
 \qquad(0<t<1)
\]
shows that \(R\) is strictly increasing. If \(\beta>\alpha\), the ratio of the two normalized densities is a strictly decreasing multiple of \((1-t)^{\beta-\alpha}\). Equivalently, multiplying the \(\nu_\alpha\) density by a strictly decreasing function reduces the mean of the strictly increasing \(R\), by the strict negative covariance identity obtained from two independent samples. Therefore \(u_\alpha/v_\alpha\) is continuous and strictly **decreasing** for \(\alpha>0\).

At the limit \(\alpha\downarrow0\), elementary rational integration gives \(u_0=1/2\), \(v_0=1/4\), hence the ratio tends to \(2\). As \(\alpha\to\infty\), \(\nu_\alpha\) concentrates at zero, so the ratio tends to \(R(0)=0\). A unique \(\alpha_*\in(0,\infty)\) satisfies \(u_\alpha=v_\alpha\). Exact elementary integrals further give
\[
 u_2-v_2=12+\frac{3\pi}{2}-24\log2>0,\qquad
 u_3-v_3=102-6\pi-120\log2<0.
\]
The signs have exact rational alternating-series certificates in `CHECK.py`; thus \(2<\alpha_*<3\). The quoted decimal is numerical quadrature of the **uniquely defined** root, not an algebraic closed form. This proves the stated modal classification, including strict inequalities outside the crossing.

**Sharp stability and asymptotics.** For fixed \(\alpha>0\), \(\mathcal E_\alpha\) is smooth near the square; writing \(\varepsilon_j^\circ=\varepsilon_j-\frac14\sum_k\varepsilon_k\), stationarity and Taylor's theorem imply
\[
 \mathcal E_\alpha(\boldsymbol\theta^\star+\boldsymbol\varepsilon)-\mathcal E_\alpha(\boldsymbol\theta^\star)
 =\tfrac12\boldsymbol\varepsilon^{\circ\mathsf T}H_\alpha\boldsymbol\varepsilon^\circ
 +O_\alpha(\|\boldsymbol\varepsilon^\circ\|_2^3).
\]
The smallest positive Hessian eigenvalue gives \(c_\alpha\) and the corresponding real Fourier eigenvector makes this coefficient sharp. At \(\alpha=\alpha_*\), all positive eigenvalues coincide, so the Hessian restricts to a positive scalar on the centered subspace.

Finally, beta-moment concentration at \(t=0\) gives
\[
 u_\alpha=\frac{4}{\alpha}+O(\alpha^{-2}),\qquad
 v_\alpha=1+O(\alpha^{-1}).
\]
For example, bound the smooth rational factors in their defining integrands by their Taylor expansions near zero and use \((\alpha+1)\int_0^1t^k(1-t)^\alpha\,dt=(\alpha+1)\mathrm B(k+1,\alpha+1)\). Consequently \(\lambda_1\to4\), \(\lambda_2\sim32/\alpha\), and their ratio, which is the sharp nonrotational angular condition number for large \(\alpha\), obeys \(\kappa_\alpha\sim\alpha/8\).

## Verification
The included standalone `CHECK.py` runs with Python's standard library. It independently evaluates the radial pair-interaction energy and uses symmetric finite differences to verify both distinct Hessian eigenvalues for eight weights; checks the integrals against the displayed \(\pi\)-and-\(\log2\) endpoint formulas; tests the monotone ratio on a finite grid; and, using rational alternating-series bounds for \(\pi\) and \(\log2\), supplies **exact** certificates for the signs at weights two and three. Running `python3 CHECK.py` returns `PASS`. The continuity, uniqueness, strict stochastic-order argument, and all-weight asymptotics are analytical, not established by the finite checks.

## Relationship to prior work
Corbett (2026, arXiv:2609.21121v1, first public 2026-09-17) establishes global equispaced-pole minimization for all positive power weights using universal optimality, and analyzes the Hessian as a positivity device in the concave-weight range \(0<\alpha\le1\). The paper does **not** determine the first-versus-alternating Hessian mode in the four-pole configuration as the weight varies through values greater than one. Abakumov, Borichev, and Fedorovskiy (2020) provide the original weighted Hilbert-space minimization theorem and a general angular interaction/convexity formula; their Lemma 12 explicitly marks the \(\alpha=1\) boundary of global pair convexity, but does not supply the four-pole weight-dependent eigenvalue crossover. The previously deposited result *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles* (2026) diagonalizes the Hessian for the **fixed weight** \(1-|z|^2\) and all polygon sizes. That result is compatible with the present \(\alpha=1\) case, but does not imply or resolve the unique transition in the continuous weight parameter. Globally optimal pole placement alone also cannot determine the ordering of local Hessian eigenvalues. The novelty assessment is relative to these inspected sources and the specified literature/database searches, not a proof that no unindexed equivalent exists.

## Limitations
The classification is for **four** poles, **unit** pole residues, and the normalized quadratic weighted Bergman norm with exponent \(\alpha>0\). It asserts a local angular spectral phase diagram, not a changed global minimizer, and not a condition number for the full infinite-dimensional Bergman operator. At the transition the Hessian is isotropic only to quadratic order; higher-order anisotropy is not excluded. The displayed decimal is approximate. The literature search cannot exclude inaccessible or unindexed identical results. No independent audit has been performed.

## References
1. Georgia Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121v1, first public 2026-09-17, https://arxiv.org/abs/2609.21121 (especially Sections 1, 2.3, and 3).
2. Evgeny Abakumov, Alexander Borichev, Konstantin Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898v1, first public 2020-09-03, https://arxiv.org/html/2009.01898v1 (Theorem 1 and Lemma 12).
3. *Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles*, mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-full-fourier-hessian-spectrum-and-sharp-local-stability-for-equi--9aca32c3cb4f (full `RESULT.md`, fixed exponent only).
