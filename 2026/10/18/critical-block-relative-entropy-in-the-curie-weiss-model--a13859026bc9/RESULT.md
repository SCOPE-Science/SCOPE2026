# Critical-block relative entropy in the Curie–Weiss model

## Finding
Let \(\mu_N\) be the zero-field Curie–Weiss law at inverse temperature one on \(N\) spins, and let \(\mu_N^{(k)}\) be its first-\(k\)-spin marginal. Let \(Q_k\) be the fair independent-spin law and let all relative entropies use natural logarithms. For every integer sequence \(1\leq k_N\leq N\) satisfying
\[
\frac{k_N}{\sqrt N}\longrightarrow\alpha\in(0,\infty),
\]
there is an exact nonzero finite information limit
\[
\lim_{N\to\infty}D(\mu_N^{(k_N)}\Vert Q_{k_N})
=d(\alpha):=\int_{\mathbb R}\phi(z)L_\alpha(z)\log L_\alpha(z)\,dz,
\quad L_\alpha(z)=\mathbb E\exp\!\left(\sqrt\alpha Xz-\frac{\alpha X^2}{2}\right).
\]
Here \(\phi\) is the standard normal density and \(X\) has probability density \(J^{-1}e^{-x^4/12}\) with \(J=12^{1/4}\Gamma(1/4)/2\). Equivalently,
\[
d(\alpha)=D\bigl(\mathcal L(Z+\sqrt\alpha X)\Vert\mathcal L(Z)\bigr)
\]
for an independent standard normal \(Z\). The function \(d\) is continuously differentiable and strictly increasing for positive \(\alpha\), with
\[
d'(\alpha)=\frac12\,\mathbb E\!\left[\left(\mathbb E[X\mid Z+\sqrt\alpha X]\right)^2\right]>0.
\]
Writing \(v=\mathbb E X^2=\sqrt{12}\,\Gamma(3/4)/\Gamma(1/4)\), its endpoint asymptotics are
\[
d(\alpha)=\frac{v^2}{4}\alpha^2+o(\alpha^2)\quad(\alpha\downarrow0),
\qquad
d(\alpha)=\frac v2\alpha-\frac12\log\alpha+h(Z)-h(X)+o(1)\quad(\alpha\to\infty),
\]
where \(h(X)=\log J+1/4\) and \(h(Z)=\tfrac12\log(2\pi e)\) are differential entropies. In particular, the critical window has a positive finite *relative-entropy* profile, which total-variation convergence by itself does not establish.

## Assumptions and scope
The finite-volume Gibbs probability of \(\sigma=(\sigma_1,\ldots,\sigma_N)\in\{-1,+1\}^N\) is
\[
\mu_N(\sigma)=\frac{1}{\mathcal Z_N}\exp\left(\frac{(\sum_{i=1}^N\sigma_i)^2}{2N}\right),\qquad
\mathcal Z_N=\sum_{\sigma\in\{-1,+1\}^N}\exp\left(\frac{(\sum_i\sigma_i)^2}{2N}\right).
\]
There is no external field, \(N\to\infty\) through positive integers, and \(k_N\) is any integer sequence satisfying the displayed critical-window limit. \(D(P\Vert Q)=\sum_xP(x)\log(P(x)/Q(x))\), with \(0\log0=0\). The limiting function and its endpoint expansions concern the same critical-window profile as \(\alpha\) varies *after* the \(N\to\infty\) limit; no uniform two-parameter limit is asserted.

## Proof
**1. Exact latent-field decomposition.** The Hubbard–Stratonovich Gaussian identity gives an exact mixture of independent biased spins:
\[
\mu_N=\int Q_h^{\otimes N}\,\pi_N(dh),\qquad
Q_h(\sigma_i=\pm1)=\frac{e^{\pm h}}{2\cosh h},\qquad
\pi_N(dh)=\frac{e^{-NF(h)}}{\int_{\mathbb R}e^{-NF(u)}du}\,dh,
\]
where \(F(h)=h^2/2-\log\cosh h\). This follows by inserting
\[
 e^{S^2/(2N)}=\sqrt{\frac N{2\pi}}\int_{\mathbb R}e^{-Nh^2/2+hS}\,dh
\]
for every spin sum \(S\), and then summing over the spins. As \(h\to0\),
\(F(h)=h^4/12+O(h^6)\), while \(F(h)>0\) away from zero and there exists \(c>0\) with \(F(h)\geq c\min(h^4,h^2)\) for every real \(h\). Consequently \(X_N=N^{1/4}H_N\), with \(H_N\sim\pi_N\), converges in law and in each fixed polynomial moment to \(X\). More strongly, for each \(A<\infty\),
\[
\sup_{N\geq N_A}\mathbb E e^{AX_N^2}<\infty.
\]
Indeed, after the change of variables \(x=N^{1/4}h\), the exponent satisfies \(NF(N^{-1/4}x)\geq c\min(x^4,\sqrt N x^2)\); the normalized density denominator stays bounded below, and the stated integrable majorant follows for sufficiently large \(N\).

**2. Likelihood-ratio convergence.** Write \(S_k=\sum_{i=1}^k\sigma_i\). Relative to \(Q_k\), the marginal likelihood ratio depends only on \(S_k\) and equals
\[
 L_{N,k}(S_k)=\mathbb E_{H_N}\exp\bigl(H_NS_k-k\log\cosh H_N\bigr).
\]
Let \(\alpha_N=k_N/\sqrt N\). At \(S_{k_N}=\sqrt{k_N}z\), this is
\[
 \mathbb E\exp\left(\sqrt{\alpha_N}X_Nz-k_N\log\cosh(N^{-1/4}X_N)\right).
\]
For bounded \(z\), a Taylor expansion on bounded \(X_N\), the exponential-moment bound from Step 1, and \(k_N\log\cosh(N^{-1/4}x)\to\alpha x^2/2\) give locally uniform convergence to \(L_\alpha(z)\). Under \(Q_{k_N}\), the classical central limit theorem gives \(S_{k_N}/\sqrt{k_N}\Rightarrow Z\), so the random likelihood ratios converge in distribution to \(L_\alpha(Z)\).

**3. Uniform integrability upgrades this to relative entropy.** Introduce independent latent fields \(H_N,H_N'\). The Rademacher moment generating identity yields
\[
\begin{aligned}
\mathbb E_{Q_k}[L_{N,k}^2]
&=\mathbb E\left[(1+\tanh H_N\tanh H_N')^k\right]\\
&\leq \mathbb E e^{k|H_NH_N'|}
\leq\left(\mathbb E e^{\frac{k}{2\sqrt N}X_N^2}\right)^2.
\end{aligned}
\]
The last quantity is uniformly bounded along \(\alpha_N\to\alpha\). Since \(u\log u\) is bounded below and grows strictly slower than \(u^2\), \(L_{N,k_N}\log L_{N,k_N}\) is uniformly integrable. Thus expectations converge and give the first displayed limit. Integrating out a Gaussian shows that the density of \(Z+\sqrt\alpha X\), relative to the density \(\phi\) of \(Z\), is exactly \(L_\alpha\); this proves the second expression. The limit is finite by the same moment bounds and positive because the convolved law has variance \(1+\alpha v\), different from the standard normal variance.

**4. Monotonicity and endpoint expansions.** The Gaussian-channel identity
\[
 d(\alpha)=\frac{\alpha v}{2}-I(X;Z+\sqrt\alpha X)
\]
follows by comparing the differential entropy and second moment of the Gaussian mixture. The established information–MMSE identity for additive Gaussian channels then yields
\[
 d'(\alpha)=\frac12\{v-\mathbb E\operatorname{Var}(X\mid Z+\sqrt\alpha X)\}
=\frac12\mathbb E[\mathbb E(X\mid Z+\sqrt\alpha X)^2].
\]
It is strictly positive: the observation has nonzero covariance \(\sqrt\alpha v\) with \(X\), so the conditional mean cannot vanish almost surely. Symmetry and exponential integrability provide the small-parameter expansion in \(L^3(\phi)\):
\[
 L_\alpha(z)=1+\frac{\alpha v}{2}(z^2-1)+O_{L^3(\phi)}(\alpha^2).
\]
Taylor expansion of \(u\log u\) around one and \(\mathbb E(Z^2-1)^2=2\) give \(d(\alpha)=v^2\alpha^2/4+o(\alpha^2)\). Finally,
\[
 h(Z+\sqrt\alpha X)=\tfrac12\log\alpha+h(X+\alpha^{-1/2}Z)
=\tfrac12\log\alpha+h(X)+o(1),
\]
because Gaussian convolution tends to a smooth positive quartic density in entropy (dominated density bounds and finite logarithmic moments give a direct proof). Substitution in the Gaussian-channel identity gives the large-\(\alpha\) expansion. The quartic moment integral yields \(v=\sqrt{12}\Gamma(3/4)/\Gamma(1/4)\), \(\mathbb EX^4=3\), and \(h(X)=\log J+1/4\), as stated.

## Verification
The supplied `verify.py` implements two numerically independent finite-volume evaluations: brute-force enumeration of all spin configurations for \(2\leq N\leq10\), and a binomial-convolution formula for block likelihood ratios. It also computes the limiting quartic–Gaussian mixture by Gaussian and Legendre quadrature, checking normalization, the exact second moment, six positive information values, monotonicity on the tested grid, and comparisons for \(N\in\{256,1024,4096\}\) and three critical-window ratios. The checker completed **87 passing finite identity/quadrature/asymptotic-consistency assertions**; these checks do not establish the infinite-volume limit or its entire parameter range. To reproduce: install the packages in `requirements.txt`, then run `python verify.py`.

The exact finite expression checked is
\[
 L_{N,k}(s)=\frac{2^k}{\mathcal Z_N}\sum_{j=0}^{N-k}\binom{N-k}{j}
\exp\!\left(\frac{(s+2j-(N-k))^2}{2N}\right),\quad
\mathcal Z_N=\sum_{j=0}^N\binom Nj\exp\!\left(\frac{(2j-N)^2}{2N}\right).
\]
For instance, numerical quadrature gives \(d(1)\approx0.1993891554\) and \(d(2)\approx0.5726993115\).

## Relationship to prior work
Gantert, Löwe and Schnappinger (2026) prove the critical-window breakdown of total-variation propagation of chaos and supply an explicit limiting total-variation profile. This finding is about **relative entropy, not total variation**: convergence of total variation alone does not imply convergence of Kullback–Leibler divergence. The proof's uniform second-moment estimate is the needed additional step, and the information-profile derivative and endpoints go beyond a mere reformulation of total variation.

Ben Arous and Zeitouni (1999, Corollary 1, critical Case II) prove relative-entropy convergence to zero for strictly subcritical windows \(k_N=o(\sqrt N)\), not the positive finite critical-window limit. Their discussion also credits Papangelou (1989) with a non-Gaussian/Gaussian decomposition of critical spin-block fluctuations; weak convergence of those observables does not by itself establish the claimed relative-entropy limit. Jalowy, Kabluchko, Löwe and Marynych (2023) study increasing-block propagation of chaos and total variation. Galicza and Pete (2025, Proposition 7.4) provide global critical Curie–Weiss entropy bounds, not the critical-block finite information curve. Guo, Shamai and Verdú (2005) provide the information–MMSE identity invoked in Step 4; that identity is not claimed as new. A general information-convergence result not located in the surveyed literature could still subsume this theorem.

## Limitations
The theorem is limited to the classical zero-field critical Curie–Weiss Gibbs law, a fixed positive critical-window ratio after taking the infinite-volume limit, and natural-logarithm relative entropy. The derivative and small-/large-ratio laws characterize the limiting profile; they do not establish rates of finite-volume convergence, a uniform joint regime when \(\alpha\) varies with \(N\), or a result for inhomogeneous couplings. Papangelou's 1989 full primary text was not accessible for direct full-document comparison; only its bibliographic description and its precise use in the inspected Ben Arous–Zeitouni paper were available. Priority and possible implication from that earlier fluctuation theorem remain residual originality risks. Independent validation has not been performed.

## References
1. N. Gantert, M. Löwe, K. Schnappinger, *When does propagation of chaos in the critical Curie–Weiss model stop?* (2026), arXiv:2609.02464, first submitted 2026-09-02, https://arxiv.org/abs/2609.02464.
2. G. Ben Arous and O. Zeitouni, *Increasing propagation of chaos for mean field models*, Ann. Inst. Henri Poincaré Probab. Stat. **35** (1999), 85–102, https://www.numdam.org/item/AIHPB_1999__35_1_85_0/.
3. P. Jalowy, Z. Kabluchko, M. Löwe, A. Marynych, *When does the chaos in the Curie-Weiss model stop to propagate?* (2023), arXiv:2307.05335, https://arxiv.org/abs/2307.05335.
4. F. Papangelou, *On the Gaussian fluctuations of the critical Curie-Weiss model in statistical mechanics*, Probab. Theory Relat. Fields **83** (1989), 265–278, DOI:10.1007/BF00333150.
5. B. Galicza and G. Pete, *Sparse reconstruction in spin systems II: Ising and other factor of IID measures* (2025), Proposition 7.4, DOI:10.1007/s00440-025-01395-4.
6. D. Guo, S. Shamai, S. Verdú, *Mutual information and minimum mean-square error in Gaussian channels*, IEEE Trans. Inform. Theory **51** (2005), 1261–1282, DOI:10.1109/TIT.2005.844072.
