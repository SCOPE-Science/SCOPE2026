# A square-root resolution law and noncommuting memory limits for noisy rotational diffusion

## Finding

For the stationary planar rotational Ornstein–Uhlenbeck diffusion defined below, independently noisy measurements taken at spacing \(h\) have an **exact full-history time-reversal relative-entropy rate**. Unlike a two-sample statistic, its physical-time rate recovers the complete underlying entropy production as \(h\downarrow0\), but with a nonanalytic square-root finite-resolution loss. At every fixed observation-block length, by contrast, the corresponding physical-time irreversibility vanishes in that limit.

Precisely, put \(q=e^{-2\alpha h}\), \(c=1-q\), \(\vartheta=\omega h\), and for \(\tau>0\) define
\[
K=\sqrt{c\bigl[4\tau+c(1-\tau)^2\bigr]},\qquad
u=\frac{2\tau q}{c+\tau(1+q)+K}.
\]
Then \(0<\nu<1\), and the limit \(\mathcal E_\tau(h)\) of reverse-path Kullback–Leibler divergence **per observed transition** exists and is
\[
\boxed{\mathcal E_\tau(h)
=\frac{4c\nu(1+\nu)\sin^2\vartheta}
{\tau K(1-\nu)\bigl[(1-\nu)^2+4\nu\sin^2\vartheta\bigr]}.}
\]
For noiseless samples \(\tau=0\), the corresponding formula is
\[
\boxed{\mathcal E_0(h)=\frac{4q\sin^2\vartheta}{c}.}
\]
At fixed \(\tau>0\), as \(h\downarrow0\),
\[
\boxed{\frac{\mathcal E_\tau(h)}h
=\frac{2\omega^2}{\alpha}
\left[1-\frac32\sqrt{2\alpha\tau}\,h^{1/2}+O(h)\right].}
\]
For \(\tau=0\), instead, \(\mathcal E_0(h)/h=(2\omega^2/\alpha)[1-\alpha h+O(h^2)]\). Thus the strictly positive localization-noise variance changes the **order** of the finite-resolution correction from linear to square root.

For every fixed integer \(m\ge2\) and every \(\tau>0\), its \(m\)-sample reversal divergence satisfies \(\mathcal D_m(h,\tau)=O_m(h^2)\), so
\[
\lim_{h\downarrow0}\lim_{m\to\infty}\frac{\mathcal D_m(h,\tau)}{(m-1)h}
=\frac{2\omega^2}{\alpha},\qquad
\lim_{m\to\infty}\lim_{h\downarrow0}\frac{\mathcal D_m(h,\tau)}{(m-1)h}=0.
\]
The limits do not commute. In particular, a fixed finite-memory time-reversal statistic loses the arrow of time at arbitrarily fine sampling, although the full-history statistic recovers it.

## Assumptions and scope

Let \(\alpha>0\), \(\omega\in\mathbb R\setminus\{0\}\), \(h>0\), and \(\tau\ge0\). Let \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\) and let the stationary \(\mathbb R^2\)-valued Itô diffusion satisfy
\[
dZ_t=(-\alpha I_2+\omega J)Z_t\,dt+\sqrt{2\alpha}\,dW_t,
\qquad Z_t\sim\mathcal N(0,I_2).
\]
At each integer \(k\), observe \(Y_k=Z_{kh}+\epsilon_k\), with independent \(\epsilon_k\sim\mathcal N(0,\tau I_2)\), independent also of the diffusion. At \(\tau=0\), errors are identically zero.

For integer \(m\ge2\), denote by \(P_m\) the probability law of \((Y_0,\ldots,Y_{m-1})\), and by \(P_m^{\leftarrow}\) its pushforward under reversal of the **order of the two-dimensional observations**, without changing either coordinate's parity. Set
\[
\mathcal D_m(h,\tau)=D_{\mathrm{KL}}(P_m\|P_m^{\leftarrow}),\qquad
\mathcal E_\tau(h)=\lim_{m\to\infty}\frac{\mathcal D_m(h,\tau)}{m-1}.
\]
The path reversal here compares forward and reversed **stationary observed path laws**; it does not compare parameters with a separately sign-flipped driving protocol. All phase-dependent claims apply for each fixed \(h>0\). The asymptotic claims hold with \(\alpha,\omega,\tau\) fixed and \(h\downarrow0\).

For \(\tau\ge0\), \(\mathcal E_\tau(h)=0\) if and only if \(\omega h\in\pi\mathbb Z\). Otherwise \(\mathcal E_\tau(h)>0\); whenever \(\tau>0\) in this nonresonant regime, \(\mathcal E_\tau(h)<\mathcal E_0(h)\). The continuum diffusion has housekeeping entropy production \(2\omega^2/\alpha\) per unit physical time.

## Proof

**1. Covariance and spectral reduction.** Stationarity and the explicit OU transition kernel give
\[
\operatorname{Cov}(Y_{j+k},Y_j)=e^{-\alpha h|k|}\,e^{\omega hkJ}+\tau I_2\mathbf1_{\{k=0\}}.
\]
Write \(r=e^{-\alpha h}\), \(c=1-r^2\), and define the Poisson kernel
\[
g(\phi)=\frac{c}{1-2r\cos\phi+r^2}.
\]
Simultaneously diagonalizing the planar rotations in a complex circular-polarization basis shows that the positive-definite matrix spectral density has eigenvalues
\[
f_+(\phi)=\tau+g(\phi-\vartheta),\qquad
f_-(\phi)=\tau+g(\phi+\vartheta).
\]
Time reversal interchanges these eigenvalues. Their common eigenbasis is independent of frequency.

For each fixed \(h>0\), the covariance sequence is absolutely summable, with geometric decay, and the spectral densities are uniformly positive definite, including when \(\tau=0\). The zero-mean Gaussian divergence formula gives
\[
\mathcal D_m=\frac12\{\operatorname{tr}(\Sigma_{m,\leftarrow}^{-1}\Sigma_m)-2m\},
\]
since the block-reversal permutation preserves the determinant. To pass to the infinite-block limit, replace the covariance block-Toeplitz matrices with periodized block-circulant matrices. Their difference has uniformly bounded trace norm: the wraparound error across each corner has geometrically summable ranks and amplitudes, and the remaining periodization tail is exponentially small. Uniform lower spectral bounds control both inverses, so the trace difference is \(O(1)\). The circulant trace is a Riemann sum of the spectral ratio. Consequently
\[
\mathcal E_\tau(h)=\frac1{4\pi}\int_{-\pi}^{\pi}
\left(\frac{f_+(\phi)}{f_-(\phi)}+
\frac{f_-(\phi)}{f_+(\phi)}-2\right)\,d\phi
=\frac1{4\pi}\int_{-\pi}^{\pi}
\frac{\bigl[g(\phi-\vartheta)-g(\phi+\vartheta)\bigr]^2}
{\bigl[\tau+g(\phi-\vartheta)\bigr]\bigl[\tau+g(\phi+\vartheta)\bigr]}
\,d\phi.
\]
The integrand proves strict positivity away from phase resonance and strictly decreases as \(\tau\) increases whenever it is nonzero. In the noise-free case, a direct Poisson-kernel average gives \(\mathcal E_0(h)=4r^2\sin^2\vartheta/(1-r^2)\).

**2. Evaluation of the noisy spectral integral.** Suppose \(\tau>0\). Define \(A=c+\tau(1+r^2)\) and \(K=\sqrt{A^2-4\tau^2r^2}\); elementary expansion gives \(K^2=c[4\tau+c(1-\tau)^2]\). Define \(\nu=2\tau r^2/(A+K)\). The quadratic-root relation yields \(0<\nu<r^2<1\). The reciprocal noisy denominator has the normalized Poisson representation
\[
\frac1{c+\tau(1-2r\cos\phi+r^2)}
=\frac1K P_{\nu/r}(\phi),\qquad
P_s(\phi)=\frac{1-s^2}{1-2s\cos\phi+s^2}.
\]
For \(0<s,t<1\), the Fourier series \(P_s(\phi)=\sum_{k\in\mathbb Z}s^{|k|}e^{ik\phi}\) gives the exact convolution identity
\[
\frac1{2\pi}\int_{-\pi}^\pi P_s(\phi-a)P_t(\phi-b)\,d\phi
=P_{st}(a-b).
\]
Expanding \(f_+/f_-\) using \(g=c/D\), \(D(\phi)=1-2r\cos\phi+r^2\), and averaging this identity gives
\[
\frac1{2\pi}\int_{-\pi}^\pi \frac{f_+(\phi)}{f_-(\phi)}d\phi-1
=\frac{c}{\tau K}\bigl[P_\nu(0)-P_\nu(2\vartheta)\bigr].
\]
The average of \(f_-/f_+\) equals the same expression by reflection, hence the spectral formula equals that average minus one. Finally,
\[
P_\nu(0)-P_\nu(2\vartheta)
=\frac{4\nu(1+\nu)\sin^2\vartheta}
{(1-\nu)[(1-\nu)^2+4\nu\sin^2\vartheta]}.
\]
This proves the stated closed form and all fixed-spacing sign and monotonicity claims.

**3. Square-root resolution law.** With \(c\downarrow0\) at fixed \(\tau>0\),
\[
K=2\sqrt{\tau c}\,[1+O(c)],\quad
\nu=1-\sqrt{c/\tau}+\frac{1-\tau}{2\tau}c+O(c^{3/2}),\quad
\vartheta=\frac\omega{2\alpha}c+O(c^2).
\]
For the coefficient of the next correction, retain these expansions through order \(c\) in the explicit rational formula; direct multiplication gives the sharper Puiseux expansion
\[
\mathcal E_\tau(h)=\frac{\omega^2}{\alpha^2}c
\left[1-\frac32\sqrt{\tau c}+O(c)\right].
\]
(The \(O(c)\) remainder is uniform when \(\alpha,\omega,\tau\) range over a fixed compact subset of their indicated open parameter domain.) Since \(c=2\alpha h+O(h^2)\), dividing by \(h\) produces the claimed physical-time law. The noiseless formula has instead the ordinary Taylor expansion stated in the finding.

The stationary physical probability current is \(j(z)=\omega Jz\,\pi(z)\), where \(\pi\) is the standard Gaussian density and the diffusion coefficient is \(\alpha I_2\). Its quadratic housekeeping rate is therefore
\[
\int \frac{j(z)^T(\alpha I_2)^{-1}j(z)}{\pi(z)}\,dz
=\frac{\omega^2}{\alpha}\mathbb E|Z|^2
=\frac{2\omega^2}{\alpha}.
\]

**4. Fixed-block obstruction and noncommuting limits.** At \(h=0\), for every finite \(m\) the forward and reversed observation covariances are the common positive-definite matrix
\[
\Sigma_m(0)=\mathbf1_m\mathbf1_m^T\otimes I_2+\tau I_{2m}.
\]
For \(\tau>0\), all block covariance entries are right-analytic in \(h\) at zero, and their forward/reversed differences are \(O_m(h)\). Zero-mean Gaussian KL is quadratic in such a perturbation around identical positive-definite covariance matrices (the linear trace and log-determinant terms cancel). Therefore \(\mathcal D_m(h,\tau)=O_m(h^2)\). The exact two-sample identity makes this visible:
\[
\mathcal D_2(h,\tau)=\frac{4e^{-2\alpha h}\sin^2(\omega h)}{(1+\tau)^2-e^{-2\alpha h}}
\sim\frac{4\omega^2h^2}{\tau(2+\tau)}.
\]
Taking the finite-block physical-time limit first gives zero for every finite \(m\), while taking the block length to infinity first gives \(\mathcal E_\tau(h)/h\) and then the positive continuum rate. This proves the noncommutation.

## Verification

The accompanying standalone Python 3 program `verify.py` computes the closed form, independently integrates the frequency-domain Gaussian KL integrand by periodic midpoint quadrature, constructs actual finite Gaussian block covariance matrices and reversals, evaluates their KL divergence by matrix elimination, and tests the exact two-block identity, fixed-block quadratic scaling, phase resonance, strict noise contraction, and the high-frequency asymptotics. It runs with Python's standard library only: `python3 verify.py`. All 36 deterministic checks passed on the supplied parameter sets. Numerical checks corroborate but do not replace the analytic proof above.

## Relationship to prior work

Sagawa's 2026 framework derives general entropy production expressions for autoregressive and Kalman-innovation representations, including linear Gaussian systems. That broad framework provides methods for evaluating observed Gaussian path irreversibility and is not claimed as new here. Gingrich, Igoshin, Kolomeisky and Makarov (2026) established lower bounds and emphasized memory and the competing effects of temporal and spatial resolution in noisy trajectory-based thermodynamic inference; the general non-Markovian observation effect is also prior work. Earlier Gaussian diffusion research establishes stationary OU dissipation formulas. The contribution asserted here is the **explicit noisy rotational OU full-path closed form**, the sharp **square-root small-spacing coefficient**, and its precise **noncommutation with every fixed observation-block length**. General formulas in earlier papers may imply the spectral reduction after specialization; the particular resolution theorem is not asserted to follow automatically from a difference in terminology or presentation.

## Limitations

The theorem is for two-dimensional isotropic stationary OU dynamics, additive independent isotropic Gaussian localization error, and even-parity coordinate reversal. It is not claimed for arbitrary non-Gaussian sensing, anisotropic OU models, nonstationary initializations, finite-exposure camera integration, or general measurement noise correlated across samples. Sensor error remains of fixed variance as the sampling interval shrinks; changing this scaling changes the asymptotic regime. Strict positivity fails at isolated resonance spacings, but this does not affect the small-spacing result for nonzero fixed rotation. Full statistical estimation from a finite dataset is not addressed. A broad Gaussian state-space theorem could potentially subsume portions of the formula; publication-priority comparison is not independent certification.

## References

1. T. Sagawa, *Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective*, arXiv:2604.07867, first submitted 2026-04-09. https://arxiv.org/abs/2604.07867
2. T. R. Gingrich, O. A. Igoshin, A. B. Kolomeisky, and D. E. Makarov, *Thermodynamic inference from noisy single-molecule time series*, arXiv:2606.23619, first submitted 2026-06-22. https://arxiv.org/abs/2606.23619 ; doi:10.1063/5.0354355.
3. D. da Costa and G. A. Pavliotis, *The entropy production of stationary diffusions*, arXiv:2212.05125, https://arxiv.org/abs/2212.05125.
4. C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein–Uhlenbeck processes*, arXiv:1807.00694, https://arxiv.org/abs/1807.00694.
