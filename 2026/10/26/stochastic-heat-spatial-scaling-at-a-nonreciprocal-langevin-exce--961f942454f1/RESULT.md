# Stochastic-heat spatial scaling at a nonreciprocal Langevin exceptional point

## Finding

A stable directed Ornstein–Uhlenbeck chain has a critical bulk spatial field that converges, after fourth-root amplitude and square-root spatial rescaling, to an Edwards–Wilkinson (stochastic-heat) field observed at a finite effective time. The limit survives a precisely calibrated inverse-chain-length change in damping, and yields an explicit nontrivial crossover covariance.

**Theorem.** Fix \(D>0\), \(0<s<1\), and \(\zeta\in\mathbb R\). For every integer \(N\ge2\) satisfying \(k_N=1+\zeta/N>0\), take independent standard Brownian motions \(B_1,\ldots,B_N\) and the directed Langevin chain
\[
\begin{aligned}
 dX_i(t)&=(-k_NX_i(t)+X_{i+1}(t))\,dt+\sqrt{2D}\,dB_i(t), &&1\le i<N,\\
 dX_N(t)&=-k_NX_N(t)\,dt+\sqrt{2D}\,dB_N(t).
\end{aligned}
\]
Its unique stationary law is centered and Gaussian. For \(u\in\mathbb R\), define \(i_N(u)=\lfloor sN+u\sqrt N\rfloor\) and, whenever \(1\le i_N(u)\le N\), let \(Z_N(u)=N^{-1/4}X_{i_N(u)}\) under the stationary law. Then, for every fixed \(m\ge1\) and \(u_1,\ldots,u_m\in\mathbb R\),
\[
 (Z_N(u_1),\ldots,Z_N(u_m))\ \Longrightarrow\ (U_L(u_1),\ldots,U_L(u_m)),\qquad L=1-s,
\]
where \(U_t\) is the zero-initial-condition mild solution on the whole real line of
\[
 \partial_t U_t=\tfrac12\partial_{uu}U_t-\zeta U_t+\sqrt{2D}\,\xi,
\]
with space-time Gaussian white noise \(\xi\). In particular, the limit is a stationary-in-space centered Gaussian field with covariance
\[
 K_{L,\zeta}(h)=\frac D{\sqrt\pi}\int_0^L t^{-1/2}\exp\!\left(-\frac{h^2}{4t}-2\zeta t\right)\,dt,\qquad h=u-v.
\]
Its spatial spectral density, under the convention \(K(h)=(2\pi)^{-1}\int_{\mathbb R}e^{i\omega h}\widehat K(\omega)\,d\omega\), is
\[
 \widehat K_{L,\zeta}(\omega)=2D\frac{1-\exp[-L(\omega^2+2\zeta)]}{\omega^2+2\zeta},
\]
with the continuous value \(2DL\) where the denominator vanishes. This spectral density is strictly positive for all real \(\omega\). At \(\zeta=0\),
\[
 K_{L,0}(h)=\frac{2D\sqrt L}{\sqrt\pi}e^{-h^2/(4L)}-D|h|\operatorname{erfc}\!\left(\frac{|h|}{2\sqrt L}\right).
\]
Furthermore, for all fixed \(L>0\) and \(\zeta\in\mathbb R\), the limiting field has local spatial increments with
\[
 \lim_{h\to0}\frac{\mathbb E[(U_L(u+h)-U_L(u))^2]}{|h|}=2D.
\]

## Assumptions and scope

The drive is independent additive Gaussian white noise at every lattice site. The chain has open boundaries and completely directed unit nearest-neighbor coupling. Its positive damping \(k_N\) may approach the coupling strength from either side at rate \(N^{-1}\); \(\zeta\) and the macroscopic observation fraction \(s\) are fixed as \(N\to\infty\). The stationary Gaussian law is taken first for each finite \(N\). Convergence is asserted for **finite-dimensional spatial distributions** only; convergence in a continuous-function topology is not claimed. For fixed \(u\), the site index is admissible for all sufficiently large \(N\).

## Proof

**1. Stationarity and finite covariance.** Put \(J_{i,i+1}=1\) for \(i<N\), with other entries zero, and \(M_N=-k_NI+J\). Since \(J^N=0\), every eigenvalue of \(M_N\) is \(-k_N<0\), and its propagator is
\[
 (e^{M_Nt})_{i\ell}=\mathbf1_{\{\ell\ge i\}}e^{-k_Nt}\frac{t^{\ell-i}}{(\ell-i)!}.
\]
The stationary covariance is the convergent controllability Gramian \(C_N=2D\int_0^\infty e^{M_Nt}e^{M_N^\top t}\,dt\). By symmetry, write \(i\le j\) and \(d=j-i\). Direct gamma integration gives the exact identity
\[
 \begin{aligned}
 C_N(i,j)&=2D\sum_{\ell=j}^N\frac{(2\ell-i-j)!}{(\ell-i)!(\ell-j)!(2k_N)^{2\ell-i-j+1}}\\
 &=\frac D{k_N}\sum_{r=0}^{N-j}\binom{2r+d}{r}\frac1{(2k_N)^{2r+d}}.
 \end{aligned}
\]
This is also the unique solution of \(M_NC_N+C_NM_N^\top+2DI=0\). It determines the complete stationary Gaussian law without numerical fitting.

**2. Local binomial scaling.** For two fixed spatial offsets \(u,v\), the corresponding ordered lattice indices satisfy \(d_N/\sqrt N\to|u-v|\) and \((N-\max(i_N(u),i_N(v)))/N\to L\). Define the fair-binomial mass
\[
 b_{r,d}=2^{-(2r+d)}\binom{2r+d}{r}=\Pr\{\operatorname{Bin}(2r+d,1/2)=r\}.
\]
For every fixed \(t>0\), the local central limit theorem (or Stirling's formula with remainder), with \(r=\lfloor Nt\rfloor\), yields
\[
 \sqrt N\,b_{r,d_N}\longrightarrow \frac1{\sqrt{\pi t}}\exp\!\left(-\frac{(u-v)^2}{4t}\right).
\]
The damping term has the uniform-on-compact-time limit \(k_N^{-(2r+d_N+1)}\to e^{-2\zeta t}\). Since the binomial point probability is bounded by \(A/\sqrt{r+1}\), uniformly in \(d\ge0\), and \(\sup_{0\le r\le N,\,d_N=O(\sqrt N)}k_N^{-(2r+d_N+1)}\) is bounded, the contribution after dividing covariance by \(\sqrt N\) from \(r<\varepsilon N\) is at most \(A'\sqrt\varepsilon\), uniformly in \(N\). On \([\varepsilon,L]\), the local asymptotic and ordinary Riemann-sum convergence apply; then let \(\varepsilon\downarrow0\). Hence
\[
 N^{-1/2}C_N(i_N(u),i_N(v))\longrightarrow\frac D{\sqrt\pi}\int_0^L t^{-1/2}e^{-(u-v)^2/(4t)-2\zeta t}\,dt.
\]
The transformed vectors are Gaussian with zero means, so entrywise convergence of every finite covariance matrix proves the joint weak convergence claimed. No assumption of statistical independence between nearby spatial observation sites is made.

**3. Stochastic-heat identification.** Let \(G_t(h)=(2\pi t)^{-1/2}\exp[-h^2/(2t)]\). The mild heat-equation field has covariance, by the white-noise isometry and \(G_t*G_t=G_{2t}\),
\[
 2D\int_0^L e^{-2\zeta t}G_{2t}(u-v)\,dt=K_{L,\zeta}(u-v).
\]
The spatial Fourier transform of \(G_{2t}\) is \(e^{-t\omega^2}\), which gives the stated spectral density. At \(\zeta=0\), direct integration by substituting \(z=|h|/(2\sqrt t)\) yields the complementary-error-function expression.

**4. Spatial roughness.** The spectral density obeys \(\widehat K_{L,\zeta}(\omega)=2D\omega^{-2}+O(\omega^{-4})\) as \(|\omega|\to\infty\) (with an exponentially small contribution). Since
\[
 \mathbb E[(U_L(u+h)-U_L(u))^2]=\frac1\pi\int_{\mathbb R}(1-\cos(\omega h))\widehat K_{L,\zeta}(\omega)\,d\omega,
\]
rescaling the integrand and using \(\int_{\mathbb R}(1-\cos z)z^{-2}\,dz=\pi\) gives the stated \(2D|h|\) leading term by dominated convergence after separating a bounded low-frequency interval.

**5. Why damping \(1\) is critical.** For any fixed \(k>0\), the diagonal variance a distance \(M=N-i+1\) from the noise-input boundary has the exact expression
\[
 V_M(k)=\frac Dk\sum_{r=0}^{M-1}\binom{2r}{r}(4k^2)^{-r}.
\]
Elementary central-binomial asymptotics give, as \(M\to\infty\),
\[
 V_M(k)\longrightarrow\frac D{\sqrt{k^2-1}}\quad(k>1),\qquad
 V_M(1)\sim\frac{2D}{\sqrt\pi}\sqrt M,
\]
while for \(0<k<1\),
\[
 V_M(k)\sim\frac{D k^{1-2M}}{(1-k^2)\sqrt{\pi M}}.
\]
For \(k_N=1+\zeta/N\) and \(M\sim LN\), the theorem interpolates these regimes through the explicit finite crossover \(N^{-1/2}V_M(k_N)\to(D/\sqrt\pi)\int_0^L t^{-1/2}e^{-2\zeta t}\,dt\). In particular the stationary amplitude is generically of order \(N^{1/4}\), even though every finite drift matrix is Hurwitz-stable.

## Verification

The accompanying self-contained `VERIFY.py` calculates the finite covariance sum using a stable term recurrence and checks the independent Lyapunov recurrence at sizes \(N=2,3,5,8,12\) and several positive damping values. It compares critical and near-critical covariance entries at \(N=400,1600,6400\) against numerical quadrature of the limiting heat kernel and tests all three fixed-damping regimes. The code uses the Python standard library and reports 805 passing deterministic checks; its maximum absolute near-critical covariance discrepancy over tested cases is approximately \(0.033461\). These finite checks verify calculations and implementation, not the infinite-limit theorem; the latter follows from the preceding binomial local-limit proof.

## Relationship to prior work

Pal and Gupta, *Non-reciprocally interacting Ornstein-Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration* (arXiv:2609.05391v1, September 4, 2026), derive the exceptional-point propagator and fixed-size covariance of this directed chain (their Section IV.3 and equations (83), (85), (92)–(96)). Those exact finite-dimensional inputs are prior work. The claim here is instead a simultaneous chain-size/damping/spatial-mesoscale theorem: its \(N^{1/4}\) field normalization, \(\sqrt N\) correlation scale, full Gaussian covariance kernel, effective stochastic-heat representation, and exact \(N^{-1}\) damping crossover.

Fanelli et al., *Noise driven neuromorphic tuned amplifier* (arXiv:1708.00070), establish noise amplification along a directed excitatory–inhibitory network; neither noise amplification as a general phenomenon nor its nonnormal mechanism is claimed here as new. Nicoletti et al., *Non normal amplification of stochastic quasi-cycles* (arXiv:1806.10566), study amplification in a three-node nonlinear stochastic loop. Arnold and Erb, *Sharp entropy decay for hypocoercive and non-symmetric Fokker-Planck equations with linear drift* (arXiv:1409.5425), study nonsymmetric linear-drift convergence, not this field-level spatial critical scaling. The heat kernel and Gaussian local-limit methods are standard mathematical tools, not new theorems. The assessment of priority is limited by potential implicit coverage through general directed-chain hydrodynamic or Gaussian kernel limits.

## Limitations

The model is exactly linear and Gaussian with independent homogeneous noise, uniform directed unit coupling, and an open chain. Results are fixed-\(s\) finite-dimensional spatial limits; no tightness in a specified function space, simultaneous spatial-boundary limit, nonlinear perturbation robustness, entropy-production statement, or universality for spatially correlated driving is proved. Near-critical damping is of the specific form \(1+\zeta/N\); the general fixed-\(k\) trichotomy does not by itself imply the mesoscopic field. The originality assessment remains subject to independent comparison with broader Gaussian fluctuation-field and nonnormal-chain results.

## References

1. S. K. Pal and S. Gupta, *Non-reciprocally interacting Ornstein-Uhlenbeck processes: Exceptional points, Anomalous relaxation, Pseudo-equilibrium and Boundary refrigeration*, arXiv:2609.05391v1, 2026-09-04, https://arxiv.org/html/2609.05391v1 .
2. D. Fanelli, F. Ginelli, R. Livi, N. Zagli and C. Zankoc, *Noise driven neuromorphic tuned amplifier*, arXiv:1708.00070, 2017, https://arxiv.org/abs/1708.00070 .
3. S. Nicoletti, N. Zagli, D. Fanelli, R. Livi, T. Carletti and G. Innocenti, *Non normal amplification of stochastic quasi-cycles*, arXiv:1806.10566, 2018, https://arxiv.org/abs/1806.10566 .
4. A. Arnold and J. Erb, *Sharp entropy decay for hypocoercive and non-symmetric Fokker-Planck equations with linear drift*, arXiv:1409.5425, 2014, https://arxiv.org/abs/1409.5425 .
