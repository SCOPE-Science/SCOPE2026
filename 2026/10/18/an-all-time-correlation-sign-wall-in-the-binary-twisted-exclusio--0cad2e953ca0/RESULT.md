# An all-time correlation sign wall in the binary twisted exclusion ring

## Finding

Consider the binary twisted symmetric exclusion process defined below on any ring of length \(L\ge3\), with unit rate on every bond, in either fixed parity sector at its uniform stationary distribution. Put \(\sigma_i(t)=(-1)^{\eta_i(t)}\), and let
\[
 C_{ij}(t)=\operatorname{Cov}_{\pi_\pm}(\sigma_i(0),\sigma_j(t)),\qquad d=|i-j|,\quad 1\le i,j\le L.
\]
For **every** \(t>0\), the sign is completely independent of time and of the parity sector:
\[
 \boxed{\operatorname{sgn} C_{ij}(t)=\operatorname{sgn}(L-2d).}
\]
Thus correlations across the shorter arc not traversing the twisted seam are strictly positive; those across the longer arc are strictly negative; and the two antipodal sites of an even ring have identically zero two-time covariance.

The full time dependence and its integrated response are exact:
\[
 C_{ij}(t)=\frac1L\sum_{k=0}^{L-1}
 \exp\!\left[-4t\sin^2\!\left(\frac{(2k+1)\pi}{2L}\right)\right]
 \cos\!\left(\frac{(2k+1)\pi(i-j)}L\right),
 \qquad
 \boxed{\int_0^\infty C_{ij}(t)\,dt=\frac{L-2d}{4}.}
\]
In particular, if \(M(t)=\sum_{i=1}^L\sigma_i(t)\), then
\[
 \operatorname{Var}_{\pi_\pm}(M)=L,\qquad
 \int_0^\infty\operatorname{Cov}_{\pi_\pm}(M(0),M(t))\,dt
 =\frac{L(L^2+2)}{12},\qquad
 \tau_M=\frac{L^2+2}{12}.
\]
Here \(\tau_M\) is the integrated, variance-normalized magnetization correlation time. The slowest rate appearing in the one-site spin-correlation sector is \(4\sin^2(\pi/(2L))\); this is **not** asserted to be the spectral gap of the complete interacting Markov generator.

## Assumptions and scope

Sites are \(1,\ldots,L\), with \(L\ge3\). A configuration is \(\eta\in\{0,1\}^L\). Every adjacent interior pair \((\eta_i,\eta_{i+1})\), \(1\le i<L\), exchanges its entries at rate one. On the seam, the ordered pair \((\eta_L,\eta_1)\) is sent at rate one to \((1-\eta_1,1-\eta_L)\). Thus equal seam bits \(00\) and \(11\) interchange, while unequal seam bits remain unchanged. Inactive clocks cause no transition. This is the two-label instance of the twisted process with twist \(f(0)=1\), \(f(1)=0\), as defined by the cited source.

The quantity \(\prod_i\sigma_i=(-1)^{\sum_i\eta_i}\) is conserved. The two parity classes are irreducible and each has cardinality \(2^{L-1}\). The measures \(\pi_+\) and \(\pi_-\) are uniform on the corresponding classes. Correlations are computed in either of these stationary distributions; the result does not extend by this formula to arbitrary mixtures with additional static correlations or to chains of length two.

## Proof

**1. Sector structure and normalization.** Interior exchanges preserve the number of ones, and the seam changes it by \(\pm2\), so parity is invariant. Exchanges can rearrange any given multiset of bits. When at least two zeros are present, they can be positioned at the two seam endpoints and converted to two ones, increasing the number of ones by two; conversely two ones can be converted to two zeros. Iteration connects every configuration of a fixed parity, including the extreme all-zero or all-one states when permitted. Each move is an involution at rate one, so the generator is symmetric and the uniform distributions \(\pi_\pm\) are stationary.

For \(L\ge3\), the uniform law on a fixed parity class has \(\mathbb E\sigma_i=0\) and \(\mathbb E\sigma_i\sigma_j=\delta_{ij}\): fixing fewer than \(L\) bits leaves the remaining parity-constrained bits equidistributed, and the product of one or two distinct spins therefore has zero mean. In particular the covariance at time zero is the identity matrix.

**2. Exact closed first-moment evolution.** Write \(\mathcal L\) for the generator on functions and use antiperiodic conventions \(\sigma_0=-\sigma_L\), \(\sigma_{L+1}=-\sigma_1\). Directly evaluating the interior exchanges and the seam gives, for all configurations,
\[
 \mathcal L\sigma_i=\sigma_{i-1}+\sigma_{i+1}-2\sigma_i.
\]
At the seam the identity is valid in both cases: when \(\eta_1=\eta_L\), the seam flips both spins and contributes \(-2\sigma_1\) to \(\mathcal L\sigma_1\); otherwise the seam contributes zero. Both equal \(-\sigma_L-\sigma_1\). The analogous calculation holds at site \(L\). Let \(\Delta_{\mathrm a}\) be the real symmetric \(L\)-by-\(L\) operator just displayed. Markov semigroup evolution preserves the span of the coordinate spins, hence the stationary covariance is exactly
\[
 C_{ij}(t)=(e^{t\Delta_{\mathrm a}})_{ij}.
\]
Antiperiodic Fourier modes \(e^{\mathrm i(2k+1)\pi j/L}\), \(k=0,\ldots,L-1\), diagonalize \(\Delta_{\mathrm a}\) with eigenvalues \(-4\sin^2((2k+1)\pi/(2L))<0\). Taking the real part yields the announced finite Fourier sum and proves exponential integrability. All Fourier eigenvalues and their normalizations are explicit; no approximation enters.

**3. Strict all-time sign.** Let \(p_t(n)=\mathbb P(S_t=n\mid S_0=0)\) for the continuous-time simple random walk on \(\mathbb Z\) whose two jump rates are each one, and define its antiperiodic image sum
\[
 K_d(t)=\sum_{q\in\mathbb Z}(-1)^q p_t(d+qL).
\]
The series converges absolutely and is the fundamental solution of the antiperiodic lattice heat equation, so \(C_{ij}(t)=K_{|i-j|}(t)\). Symmetry of the walk implies \(K_{-d}=K_d\), and antiperiodicity implies \(K_{d+L}=-K_d\); therefore \(K_{L-d}=-K_d\). If \(L=2m\), then \(K_m=0\). On \(d=0,\ldots,m-1\), the closed heat equations have \(K_{-1}=K_1\) and \(K_m=0\). Their coefficient matrix is Metzler and irreducible: all off-diagonal entries are nonnegative, and every nearest-neighbor link in this half interval is positive. Because \(K_0(0)=1\) and all other entries start at zero, \(K_d(t)>0\) for every \(0\le d<m\) and every \(t>0\).

If \(L=2m+1\), then \(K_{m+1}=-K_m\). On \(d=0,\ldots,m\), the same cooperative, irreducible system holds, with last equation \(\dot K_m=K_{m-1}-3K_m\) and first reflection \(K_{-1}=K_1\). This again gives \(K_d(t)>0\) for every \(0\le d\le m\) and \(t>0\). Irreducible Metzler positivity follows directly by adding a sufficiently large scalar multiple of the identity, expanding the exponential in nonnegative matrix powers, and observing a positive path from the initial coordinate to every other coordinate. Finally \(K_{L-d}=-K_d\) proves the strict negative and exactly zero cases.

**4. Exact integrated response.** Since \(\Delta_{\mathrm a}\) has no zero eigenvalue,
\[
 \int_0^\infty e^{t\Delta_{\mathrm a}}dt=(-\Delta_{\mathrm a})^{-1}.
\]
The function \(g_d=L/4-d/2\) for \(d=0,\ldots,L-1\) satisfies \(-\Delta_{\mathrm a}g=e_0\), as direct finite differences show: the second difference vanishes away from the origin, while at the origin \(-[g_1-g_{L-1}-2g_0]=1\), with the seam sign already included. Translation with antiperiodic extension therefore gives \(( -\Delta_{\mathrm a})^{-1}_{ij}=L/4-|i-j|/2\), the stated integral. Summing all its entries gives
\[
 \sum_{i,j=1}^L\left(\frac L4-\frac{|i-j|}2\right)
 =\frac{L^3}{4}-\frac{L(L^2-1)}6=\frac{L(L^2+2)}{12}.
\]
Division by the verified stationary variance \(L\) proves the correlation-time formula.

## Verification

`verify.py` independently constructs the **complete** parity-restricted Markov generator in configuration space, directly applies matrix exponentials to compute spin correlations at time \(t=0.73\), and compares them with the distinct \(L\)-dimensional antiperiodic heat operator. It also checks \(Q S=S\Delta_{\mathrm a}\), the integrated covariance via spectral inversion of the full generator, the explicit signed Green kernel, the sign wall, and the total integrated magnetization law for both parity sectors of every ring \(3\le L\le8\). All tests passed with reported tolerances. Run using `python verify.py` with NumPy and SciPy available.

The finite tests verify the implementation and examples; the proof above, not the tested range, proves every integer \(L\ge3\) and every real time \(t>0\).

## Relationship to prior work

Dabrowski, Poulain d'Andecy and Ragoucy introduce the twisted exclusion generator, identify its invariant sectors, and prove uniform stationarity in arXiv:2602.18204 (Sections 3–4). These ingredients are **prior results**. They study asymptotically long-time sector structure and suggest the finite-time effects of twist changes as further work (Section 7); they do not give the present two-time covariance semigroup, all-time sign classification, or closed integrated Green response.

Their later reactive-species exclusion study arXiv:2607.18959 constructs different *bulk* pair-reaction rules and develops sector structure and stationary quantities; its Section 5 concerns equal-time densities, currents and reaction rates, rather than the single-seam two-time covariance. The earlier twisted XXZ quantum-chain calculations of Qiao et al., arXiv:1901.09604, provide determinant representations for spin-chain form factors and spatial quantum correlations (Section 7). They do not state the classical stationary time-dependent sign wall and exact linear response found here. These are substantive object/observable and statement distinctions, not merely different numerical parameters.

Crampé, Ragoucy, Rittenberg and Vanicat, arXiv:1603.06796, also analyze pair creation and annihilation in an exclusion process, but their rules act throughout the bulk of an open chain with reservoirs, and Section 3 reports stationary equal-time multipoint functions and currents. That construction does not specialize to a periodic ring with a single twisted seam or imply its time-dependent sign wall.

The underlying one-particle antiperiodic lattice Laplacian and its Fourier diagonalization are elementary established tools; the contribution is the exact stochastic-observable identification and the ensuing sharp, all-size and all-time sign/response theorem for the twisted exclusion process, rather than a claim of a new heat equation.

## Limitations

The result concerns stationary two-time **spin** covariances in the exactly specified two-label model and assumes unit bond rates. It says nothing about higher-order correlation functions, arbitrary multi-species twists, general nonequilibrium initial laws, arbitrary edge rates, or the full interacting Markov spectral gap. Literature coverage cannot exclude every implicit or unindexed prior derivation; the source-defined model is explicit and the mathematical claim is independently established here.

## References

1. M. Dabrowski, L. Poulain d'Andecy and E. Ragoucy, *Twisted symmetric exclusion processes and set-theoretical \(R\)-matrices*, arXiv:2602.18204 (first submitted 2026-02-20), Sections 3, 4 and 7; https://arxiv.org/html/2602.18204v2 .
2. M. Dabrowski, L. Poulain d'Andecy and E. Ragoucy, *Integrable multi-species SSEP with reactive particle species*, arXiv:2607.18959 (2026), Sections 2 and 5, Appendix A; https://arxiv.org/pdf/2607.18959 .
3. Y. Qiao et al., *Correlation functions of the XXZ spin chain with the twisted boundary condition*, arXiv:1901.09604 (2019), Sections 2 and 7; https://arxiv.org/html/1901.09604v1 .
4. N. Crampé, E. Ragoucy, V. Rittenberg and M. Vanicat, *Integrable dissipative exclusion process: Correlation functions and physical properties*, arXiv:1603.06796 (2016), Sections 1 and 3; https://arxiv.org/html/1603.06796v2 .
