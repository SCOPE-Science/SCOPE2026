# The survivor-selected stable clock and spatial-moment reversal in a fluctuating-rate random walk

## Finding
Fix an integer starting height \(h\geq1\), a refresh interval \(\tau>0\), and a tail index \(0<\alpha<1\). Consider the continuous-time simple symmetric nearest-neighbor random walk on \(\{0,1,2,\ldots\}\), absorbed at zero. Its total jump rate is a positive random variable resampled independently after every physical-time interval of duration \(\tau\); each sampled rate \(\lambda\) has Laplace transform \(\mathbb E[e^{-s\lambda}]=(1+s^\alpha)^{-1}\) for \(s\geq0\). The jump directions and Poisson noise are independent of the rate environment. Start at height \(h\) and write \(T\) for the absorption time. The source of this model proves the survival exponent \(1/(2\alpha)\) and the consequent transition between finite and infinite mean absorption time.

The complementary surviving population has the following **joint spatial and operational-clock limit**. Put \(t_n=n\tau\), \(b_n=\tau n^{1/\alpha}\), and \(Z_n=b_n^{-1}\int_0^{t_n}\lambda_s\,ds\). Let \(S_\alpha\) be the positive stable random variable characterized by \(\mathbb E e^{-sS_\alpha}=e^{-s^\alpha}\), and define
\[
 A_\alpha=\mathbb E[S_\alpha^{-1/2}]
 =\frac{\Gamma(1/(2\alpha))}{\alpha\sqrt\pi}.
\]
For every bounded continuous test function \(g:[0,\infty)^2\to\mathbb R\),
\[
\lim_{n\to\infty}\mathbb E\!\left[g\!\left(\frac{X_{t_n}}{\sqrt{b_n}},Z_n\right)\Bigm|T>t_n\right]
 =\frac{1}{A_\alpha}\mathbb E\!\left[S_\alpha^{-1/2}\int_0^\infty g(y,S_\alpha)\,\frac{y}{S_\alpha}e^{-y^2/(2S_\alpha)}\,dy\right].
\]
Here \(X_t\) is the position before absorption, with zero thereafter. In particular, **survival size-biases the stable clock by its inverse square root**, and conditional on that clock the scaled terminal position is Rayleigh with scale equal to the square root of the clock.

The limiting conditional position density is
\[
 f_\alpha(y)=\frac{y}{A_\alpha}\,
 \mathbb E\!\left[S_\alpha^{-3/2}e^{-y^2/(2S_\alpha)}\right],\qquad y>0.
\]
For each \(0<q<1+2\alpha\), the limiting conditional \(q\)-moment exists and the **actual finite-time conditional moments converge after normalization**:
\[
\lim_{n\to\infty}\mathbb E\!\left[\left(\frac{X_{t_n}}{\sqrt{b_n}}\right)^q\Bigm|T>t_n\right]
 =\frac{2^{q/2}\Gamma(1+q/2)}{A_\alpha}
 \frac{\Gamma\!\left(1-\frac{q-1}{2\alpha}\right)}
 {\Gamma\!\left(\frac{3-q}{2}\right)}.
\]
The threshold is exact **at every positive physical time**, not only asymptotically:
\[
\mathbb E[X_t^q\mid T>t]<\infty\quad\Longleftrightarrow\quad q<1+2\alpha,
\qquad (t>0,\ q>0).
\]
In particular, at \(\alpha\leq1/2\), the surviving particle's conditional squared displacement is infinite for every \(t>0\), **even though the mean absorption time is finite when \(\alpha<1/2\)**. At \(\alpha>1/2\) the conditional squared displacement is finite, but the mean absorption time is infinite. At all \(t\geq0\), the exact first-moment identity \(\mathbb E[X_t;T>t]=h\) holds.

## Assumptions and scope
The absorbing lattice is the positive integers and the origin. At each jump the direction is chosen with probability \(1/2\) independently. The total rate remains fixed during \([j\tau,(j+1)\tau)\) and the rates are independently sampled with the stated Laplace transform. The clock \(\Lambda_t=\int_0^t\lambda_s ds\) is almost surely finite for each finite \(t\), although it has infinite mean for \(0<\alpha<1\). The law includes no additional drift, force, boundary reflection, site-dependent jumping or post-absorption trajectory. The joint weak limit is asserted at refresh epochs \(t_n=n\tau\), and the finite-time moment dichotomy applies at **every** \(t>0\). The scale \(b_n\) carries units of expected jump count, with dimensionless rates chosen by the Laplace-transform convention.

## Proof
**1. Exact clock law.** Let \(\lambda_1,\ldots,\lambda_n\) be the first \(n\) sampled rates, and let \(G_n\) be Gamma distributed with shape \(n\) and unit scale, independently of \(S_\alpha\). Conditional Laplace transforms show
\[
 \sum_{j=1}^n\lambda_j\ \stackrel d=\ G_n^{1/\alpha}S_\alpha,
 \qquad
 Z_n\ \stackrel d=\ (G_n/n)^{1/\alpha}S_\alpha.
\]
Indeed both sides of the first equality have Laplace transform \((1+s^\alpha)^{-n}\). By the law of large numbers, \(Z_n\Rightarrow S_\alpha\). For \(p>0\) and \(n>p/\alpha\), direct Mellin integration yields the exact negative-moment formula
\[
 \mathbb E[Z_n^{-p}]
 =\frac{n^{p/\alpha}\Gamma(p/\alpha)\Gamma(n-p/\alpha)}
 {\alpha\Gamma(p)\Gamma(n)}.
\]
It follows that \(\sup_{n\geq n_0}\mathbb E[Z_n^{-p}]<\infty\) for each fixed \(p>0\) and sufficiently large \(n_0\), and the limits are \(\mathbb E[S_\alpha^{-p}]=\Gamma(p/\alpha)/(\alpha\Gamma(p))\). For \(0<p<\alpha\), stable-moment integration also gives \(\mathbb E[S_\alpha^p]=\Gamma(1-p/\alpha)/\Gamma(1-p)\), and the Gamma product proves uniform boundedness of the corresponding \(p\)-moments of \(Z_n\).

**2. Absorbed operational-time kernel.** Run an independent rate-one, simple symmetric continuous-time walk \(Y_s\) from \(h\), and denote its first visit to zero by \(\sigma\). Its reflection-principle killed transition kernel is
\[
 q_s(h,j)=\mathbb P_h(Y_s=j,\sigma>s)
 =e^{-s}\bigl[I_{j-h}(s)-I_{j+h}(s)\bigr],\quad j\geq1,
\]
where \(I_k\) is the integer-order modified Bessel function. Conditional on \(\Lambda_t=s\), the physically timed killed walk has this kernel and survives with probability \(S_h(s)=\sum_{j\geq1}q_s(h,j)\). The elementary Gaussian local central limit theorem and the reflected difference give, as \(s\to\infty\),
\[
 S_h(s)\sim h\sqrt{2/\pi}\,s^{-1/2},
\]
and, uniformly for \(z,y\) in compact subintervals of \((0,\infty)\),
\[
 b\,q_{bz}(h,\lfloor y\sqrt b\rfloor)
 \longrightarrow h\sqrt{2/\pi}\,y z^{-3/2}e^{-y^2/(2z)}
 \quad (b\to\infty).
\]
The reflected Gaussian bound also gives \(S_h(s)\le C_h(1+s)^{-1/2}\) for all \(s\ge0\). These estimates follow by taking the difference between the free Gaussian kernels centered at \(h\) and \(-h\); the contribution of the bounded initial height supplies the derivative factor \(2hy/s\).

**3. Conditioning selects the clock.** Combine step 1 with the survival bound. A uniform negative moment of order \(p>1/2\) bounds the contribution of \(Z_n\le\varepsilon\) to \(\sqrt{b_n}\,\mathbb P(T>t_n)\) by \(C\varepsilon^{p-1/2}\); the contribution of \(Z_n\ge R\) is at most \(C R^{-1/2}\). On compact clock intervals step 2 applies uniformly. Thus
\[
 \sqrt{b_n}\,\mathbb P(T>t_n)
 \longrightarrow h\sqrt{2/\pi}\,A_\alpha,
\]
which agrees with the source's survival asymptotic after changing time variables, and for bounded continuous \(g\),
\[
\sqrt{b_n}\,\mathbb E\!\left[g\!\left(X_{t_n}/\sqrt{b_n},Z_n\right);T>t_n\right]
\longrightarrow h\sqrt{2/\pi}\,\mathbb E\!\left[S_\alpha^{-1/2}\int_0^\infty g(y,S_\alpha)\frac y{S_\alpha}e^{-y^2/(2S_\alpha)}dy\right].
\]
The full endpoint range can be handled by the reflected Gaussian upper bound; its integrable Rayleigh tails are uniform when the clock lies in a compact subset of \((0,\infty)\). Division gives the asserted joint limit and density. The mixture integrates to one because \(\int_0^\infty(y/z)e^{-y^2/(2z)}dy=1\).

**4. Sharp moments and conservation.** For every \(q>0\), the same local central limit theorem and Gaussian bounds imply
\[
 M_q(s):=\mathbb E_h[Y_s^q;\sigma>s]
 \sim h\sqrt{2/\pi}\,2^{q/2}\Gamma(1+q/2)\,s^{(q-1)/2}
 \quad(s\to\infty).
\]
For \(q>1\), \(M_q\) is bounded above and below by positive multiples of \((1+s)^{(q-1)/2}\) away from bounded \(s\); for \(0<q\le1\), finiteness follows from \(Y_s^q\le 1+Y_s\) and the exact first moment. The absorbed rate-one walk satisfies \(\mathbb E_h[Y_s;\sigma>s]=h\) by the stopped martingale identity. In physical time, independence of the random clock preserves this identity. Since each rate \(\lambda_j\) has a regularly varying upper tail of index \(-\alpha\) (from \(1-\mathbb E e^{-s\lambda_j}\sim s^\alpha\)), every \(\Lambda_t\) with \(t>0\) has finite positive moments exactly below order \(\alpha\). The asymptotic for \(M_q\) proves the claimed **all-time** moment threshold.

For moment convergence when \(1<q<1+2\alpha\), choose \(q'<1+2\alpha\) larger than \(q\); the estimates above and the exact Gamma/stable moment bounds show uniformly bounded conditional \(q'\)-moments of \(X_{t_n}/\sqrt{b_n}\). For \(0<q<1\), the exact conserved first moment yields uniform integrability; \(q=1\) follows directly. Hence moments pass through the joint weak limit. The Rayleigh identity \(\mathbb E[R^q]=2^{q/2}\Gamma(1+q/2)\) and the stable moment formula give the displayed limit. At \(q=2\), the finite/infinite boundary is \(\alpha=1/2\). The source's known first-passage mean criterion has the opposite inequality, proving the stated dispersion reversal.

## Verification
The accompanying executable `VERIFY.py` checks the reflected Bessel kernel against positive-site mass and stopped-walk identities for several heights and clock values. It also checks the Mellin integral for finite Gamma-stable clock sums, source spectral survival integrals at increasing refresh counts, and the algebraic stable-mixture moment identities. Running `python VERIFY.py` with NumPy, SciPy and mpmath produced `PASS 110 deterministic checks`. These numerical checks corroborate the formulas; the uniform limits, quantifiers and infinite-moment conclusion follow from the analytic estimates above, not from finite tests.

## Relationship to prior work
Levit and Reuveni (2026, arXiv:2609.26925v1) define precisely this doubly stochastic walk, derive its killed propagator and survival probability for general jump-rate dynamics, and for Mittag-Leffler rates prove the \(t^{-1/(2\alpha)}\) survival tail and mean-first-passage transition. Those are **prior results**, not discoveries claimed here. The present claim is the joint **survivor-conditioned** clock/endpoint limiting distribution, its size bias and the finite-time conditional-moment boundary. These are not the published mean-time formula or merely the survival exponent, but the source's full propagator provides their starting point; implicit prior coverage remains a material originality risk.

The Brownian meander and its Rayleigh endpoint law are classical (Durrett, Iglehart and Miller, 1977). The work of Iafrate and Orsingher (arXiv:1909.13569v1) concerns conditioned Brownian meanders and occupation functionals without independently refreshed heavy-tailed jump rates. Angstmann, Han, Henry and Huang (arXiv:2511.18256) study related compounded superdiffusive walks and the same first-passage survival exponent in another dynamics; their results are close in scaling, but the inspected material does not give the physical-time, gamma-stable-clock bias or the all-time conditional-moment boundary for the rate-refreshed walk. An ordinary positive-stable time-change of a killed Brownian motion has the same limiting structure; no general classical stable-subordination or conditioned invariance principle is claimed as novel here.

## Limitations
Only the exact finite-time moment threshold and the refresh-epoch conditioned **one-time** joint limit are established. No full conditioned path-space invariance principle, uniform convergence in \(\alpha\), central corrections or non-lattice extension is claimed. The limit requires fixed \(h\) and \(\tau\), and fails to have finite moments beyond the stated threshold. At \(\alpha=1\) the rate law becomes exponential and has all finite moments, so the all-time threshold asserted for \(0<\alpha<1\) must not be extrapolated to that endpoint. Publication-level originality is not independently validated: in particular the source's exact propagator and broader spectral-fractional first-passage results may implicitly determine parts of the conditioned law.

## References
1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925v1, first public 2026-09-22, https://arxiv.org/html/2609.26925.
2. R. T. Durrett, D. L. Iglehart and D. R. Miller, *Weak Convergence to Brownian Meander and Brownian Excursion*, Annals of Probability 5 (1977), https://doi.org/10.1214/aop/1176995895.
3. F. Iafrate and E. Orsingher, *On the sojourn time of a Generalized Brownian meander*, arXiv:1909.13569v1, https://arxiv.org/html/1909.13569v1.
4. C. N. Angstmann, D. S. Han, B. I. Henry and B. Z. Huang, *First-Passage Times for the Space Fractional Fokker-Planck Equation*, arXiv:2511.18256, https://arxiv.org/abs/2511.18256.
5. J. Littin Curinao, *Asymptotic behavior and quasi-limiting distributions on time-fractional birth and death processes*, Journal of Applied Probability 59 (2022), https://doi.org/10.1017/jpr.2022.14.
