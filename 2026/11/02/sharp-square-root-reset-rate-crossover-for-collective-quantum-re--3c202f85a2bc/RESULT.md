# Sharp square-root reset-rate crossover for collective quantum-reset purity

## Finding

In the simultaneously reset, noninteracting harmonic boson gas of Kulkarni, Majumdar and Sabhapandit [1], the purity of the stationary \(n\)-particle reduced density operator admits an exact modified-Bessel series. It has a nonzero, universal crossover profile if and only if the common resetting rate scales as the square root of the number of particles. These statements quantify collective mixedness and do not assert quantum entanglement.

Specifically, put \(\sigma=\sqrt{\hbar/(m\omega)}\), \(b=4a^2/\sigma^2\), \(\alpha=r/\omega\), and \(z=bn\). For every integer \(n\geq1\) and \(r>0\), the stationary purity \(P_n=\operatorname{Tr}(\rho_n^2)\) satisfies
\[
P_n=e^{-z}\left[I_0(z)+2\sum_{k=1}^{\infty}I_k(z)\frac{\alpha^2}{\alpha^2+k^2}\right]
=\alpha\int_0^\infty e^{-\alpha u-z(1-\cos u)}\,du.
\]
Here \(I_k\) is the modified Bessel function of the first kind. For \(b>0\), \(0<P_n<1\) and the purity increases strictly with the reset rate.

At fixed \(r>0\), as \(n\to\infty\),
\[
P_n=\frac{\sqrt{\pi/2}\,\alpha\coth(\pi\alpha)}{\sqrt{bn}}\,[1+o(1)],\qquad
-\log P_n=\tfrac12\log(bn)-\log\!\left(\sqrt{\pi/2}\,\alpha\coth(\pi\alpha)\right)+o(1).
\]

For a sequence of possibly size-dependent rates \(r_N>0\), let \(\alpha_N=r_N/\omega\), \(z_N=bN\), and suppose \(\alpha_N/\sqrt{z_N}\to c\) in the extended nonnegative real line. Then
\[
\lim_{N\to\infty}P_N(r_N)=F(c),\qquad
F(c)=\begin{cases}
0,&c=0,\\
c\sqrt{\pi/2}\,e^{c^2/2}\operatorname{erfc}(c/\sqrt2),&0<c<\infty,\\
1,&c=\infty.
\end{cases}
\]
The interior profile is strictly increasing from zero to one. Consequently, the sharp scale for nonvanishing, nonunit macroscopic purity is
\[
r_N\asymp \omega\sqrt{bN}=\frac{2a\omega}{\sigma}\sqrt N.
\]
For fixed rate and particle-label bipartitions with \(k_N/N\to x\in(0,1)\), the order-two entropy combination obeys
\[
S_2(k_N)+S_2(N-k_N)-S_2(N)
=\tfrac12\log[bN x(1-x)]-\log\!\left(\sqrt{\pi/2}\,\alpha\coth(\pi\alpha)\right)+o(1),
\]
where \(S_2(n)=-\log P_n\). It is an entropy combination, not an entanglement measure.

## Assumptions and scope

Take integers \(N\ge1\), positive physical constants \(a,m,\omega,\hbar,r\), and \(n\in\{1,\dots,N\}\). Initially prepare \(N\) identical, noninteracting bosons in the product of harmonic-oscillator ground states of a trap centered at \(+a\). Quench the center to \(-a\), evolve under its harmonic Hamiltonian, and simultaneously reset and reprepare all particles in the original product state at homogeneous Poisson rate \(r\). Observe the stationary density operator, not a single trajectory. Equivalently, an independent exponential reset age \(T\) has density \(re^{-rt}\), and
\[
\rho_N=r\int_0^\infty e^{-rt} (|\psi_t\rangle\langle\psi_t|)^{\otimes N}\,dt.
\]
The reduced \(\rho_n=\operatorname{Tr}_{N-n}\rho_N\) refers to particle labels in the symmetric tensor-product representation; no claim about mode bipartitions follows. The Gaussian one-particle wave packet evolves as a coherent state with complex amplitude \(\beta_t=\sqrt2\,a\,e^{-i\omega t}/\sigma\) relative to the post-quench oscillator. Positive \(a\) excludes the trivial unchanged-trap case; the formulas extend continuously to \(a=0\) with purity one. Particle-number asymptotics hold at fixed \(a,m,\omega,\hbar\); rates either fixed or varied exactly as specified.

## Proof

**Stationary mixture and its overlap.** Poisson regeneration gives the stated density operator. Since every conditional state is a product, the same representation applies to \(\rho_n\). For coherent states \(|\beta_t\rangle\), the squared overlap is \(\exp(-|\beta_t-\beta_s|^2)\). With the stated amplitude,
\[
|\langle\psi_s|\psi_t\rangle|^2
=\exp\{-b[1-\cos(\omega(t-s))]\}.
\]
Thus the trace of the square is the expectation of the \(n\)-th power of this overlap for two independent exponential reset ages. Their signed difference has a symmetric Laplace density. The law of its absolute value is exponential with rate \(r\). Scaling time by \(\omega\) gives exactly the integral formula above. The absolutely convergent Fourier identity
\[
e^{z\cos u}=I_0(z)+2\sum_{k=1}^\infty I_k(z)\cos(ku)
\]
and \(\alpha\int_0^\infty e^{-\alpha u}\cos(ku)\,du=\alpha^2/(\alpha^2+k^2)\) yield the Bessel series. Since \(I_k(z)>0\) for each \(k\ge1\), its nonconstant terms increase strictly with \(\alpha\); the integral ensures \(0<P_n<1\).

**Independent number-basis derivation.** The tensor power of \(n\) identical coherent states is unitarily equivalent to one coherent collective oscillator of amplitude \(\sqrt n\,\beta_t\) and \(n-1\) vacuum modes. The collective Fock populations are Poisson with mean \(z/2\). Exponential averaging multiplies the Fock matrix element with index difference \(j-k\) by \(\alpha/(\alpha+i(j-k))\). Its squared modulus gives a second exact expression
\[
P_n=\sum_{j,k\ge0}e^{-z}\frac{(z/2)^{j+k}}{j!\,k!}\frac{\alpha^2}{\alpha^2+(j-k)^2}.
\]
This independently confirms all normalizations, including the factor \(b=4a^2/\sigma^2\).

**Fixed-rate asymptotics.** For every fixed integer \(k\), \(e^{-z}I_k(z)\sim(2\pi z)^{-1/2}\) as \(z\to\infty\). The bound \(I_k(z)\le I_0(z)\) and summability of \(\alpha^2/(\alpha^2+k^2)\) permit dominated convergence in the series after multiplication by \(\sqrt z\). The elementary partial-fraction identity
\[
1+2\sum_{k=1}^\infty\frac{\alpha^2}{\alpha^2+k^2}=\pi\alpha\coth(\pi\alpha)
\]
yields the coefficient. Applying the same asymptotics to three particle numbers proves the stated entropy combination.

**Complete reset-rate crossover.** With \(V\sim\operatorname{Exp}(1)\), the exact integral is
\[
P_N=\mathbb E\,\exp\{-z_N[1-\cos(V/\alpha_N)]\}.
\]
For \(c\in(0,\infty)\), the exponent converges pointwise to \(-V^2/(2c^2)\); bounded convergence gives
\[
F(c)=\int_0^\infty e^{-v-v^2/(2c^2)}\,dv
=c\sqrt{\pi/2}\,e^{c^2/2}\operatorname{erfc}(c/\sqrt2).
\]
This expectation increases strictly with \(c\). If \(\alpha_N/\sqrt{z_N}\to\infty\), using \(1-\cos u\le u^2/2\) gives \(0\le1-P_N\le z_N/\alpha_N^2\to0\). If \(\alpha_N/\sqrt{z_N}\to0\), the Bessel series, \(I_k(z)\le I_0(z)\), and the partial-fraction identity give
\[
P_N\le e^{-z_N}I_0(z_N)\,\pi\alpha_N\coth(\pi\alpha_N)
=O((1+\alpha_N)/\sqrt{z_N})\to0.
\]
The three cases exhaust all limits and prove sharpness of the crossover scale. Finally, the state is a convex mixture of product states across particle labels, so the entropy combination measures correlations without certifying particle-bipartition entanglement.

## Verification

The standalone script `verification.py` evaluates the purity via three distinct methods: the one-period Laplace integral, the modified-Bessel expansion, and the collective-number-basis double sum. It checks multiple positive parameter choices and integer particle numbers, monotonicity with resetting, strict comparison with independent resets, the fixed-rate coefficient, and the universal crossover. Run `python verification.py` with Python 3, NumPy and SciPy. It completed 120 deterministic comparisons and asymptotic tests. These numerical checks corroborate but do not replace the infinite-series and asymptotic arguments above.

## Relationship to prior work

Kulkarni, Majumdar and Sabhapandit [1] introduced the simultaneous-reset harmonic-boson protocol and derived the stationary common-age structure, density and position order/gap/counting statistics; these underlying constructions are prior work. Kulkarni and Majumdar [2] treated quantum resetting and purity in a different, interacting spin example, rather than this bosonic all-\(n\) purity and rate-scaling classification. Magoni and collaborators [3] studied collective resetting correlations in noninteracting quantum systems. Rose and collaborators [4] developed a general spectral stationary-state representation; it can in principle support density-operator computations but does not evaluate this model's macroscopic purity scale and explicit universal profile in the material inspected. This result therefore claims an evaluated model-specific purity theorem and sharp rate crossover, not a new regeneration identity, coherent-overlap identity, or general quantum-resetting framework.

## Limitations

The model assumes instantaneous global reinitialization into the same pure product ground state, no interparticle interactions, harmonic single-particle motion, an exponential reset clock, and exact stationary preparation. The order-two entropy combination is not an entanglement witness. No assertion is made about an interacting condensate, local reset clocks, mode entanglement, non-harmonic traps, higher-order Rényi indices, finite-time relaxation, or sampling error. The numerical checks are finite and do not certify infinite-dimensional mathematical statements; these are addressed by the proof. Novelty relative to unindexed general phase-diffusion identities remains a residual literature risk, and no independent scientific audit has been performed.

## References

[1] M. Kulkarni, S. N. Majumdar and S. Sabhapandit, “Dynamically emergent correlations in bosons via quantum resetting,” arXiv:2407.20342 (first public version 2024-07-29), https://arxiv.org/abs/2407.20342.

[2] M. Kulkarni and S. N. Majumdar, “Generating entanglement by quantum resetting,” arXiv:2307.07485 (2023), https://arxiv.org/abs/2307.07485.

[3] R. Magoni, F. Carollo, G. Perfetto and I. Lesanovsky, “Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting,” arXiv:2202.12655 (2022), https://arxiv.org/abs/2202.12655.

[4] D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, “Spectral properties of simple classical and quantum reset processes,” arXiv:1806.01298 (2018), https://arxiv.org/abs/1806.01298.
