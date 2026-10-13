# Haar full-bunching has a sharp large-deviation law and an exponential mean–typical gap

## Finding
Fix an integer \(m\ge N\ge1\) and one output mode of a Haar-distributed complex unitary interferometer. With one photon in each of \(N\) distinct input modes and arbitrary normalized pure *product* internal states, define their Gram matrix \(G=(\langle\phi_i,\phi_j\rangle)_{i,j=1}^N\) and the strictly positive scalar \(\kappa=\operatorname{perm}(G)\). The probability \(P\) of detecting **all \(N\) photons in that fixed output mode**, without resolving their internal states, has the exact law
\[
P=\kappa\prod_{j=1}^N W_j,\qquad (W_1,\ldots,W_m)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
Consequently, for every real \(t>-1\),
\[
\mathbb E[(P/\kappa)^t]=\frac{\Gamma(m)\Gamma(1+t)^N}{\Gamma(m+Nt)}.
\tag{1}
\]
In particular,
\[
\mathbb EP=\kappa\frac{\Gamma(m)}{\Gamma(m+N)},\quad
\mathbb E\log(P/\kappa)=N[\psi(1)-\psi(m)],\quad
\operatorname{Var}(\log P)=N\psi_1(1)-N^2\psi_1(m).
\tag{2}
\]
Here \(\psi\) and \(\psi_1\) denote the digamma and trigamma functions.

For every sequence with \(N\to\infty\), \(m=m_N\ge N\), and \(m_N/N\to\alpha\in[1,\infty]\) (the endpoint \(\alpha=\infty\) denotes divergence), define the normalized logarithmic probability \(Z_N=N^{-1}\log(m_N^NP/\kappa)\). It obeys a **full good large-deviation principle**, at speed \(N\), with rate
\[
I_\alpha(z)=\sup_{t>-1}\{tz-F_\alpha(t)\},\qquad
F_\alpha(t)=\begin{cases}
\log\Gamma(1+t)+t-(\alpha+t)\log(1+t/\alpha),&1\le\alpha<\infty,\\
\log\Gamma(1+t),&\alpha=\infty.
\end{cases}
\tag{3}
\]
The rate is uniquely minimized at \(z=-\gamma\), where \(\gamma\) is Euler's constant. For finite \(\alpha\), it is infinite at and above \(z=\log\alpha\). Equivalently, every closed set \(C\) and open set \(O\) in \(\mathbb R\) satisfy
\[
\limsup_{N\to\infty}N^{-1}\log\Pr\{Z_N\in C\}\le-\inf_{z\in C}I_\alpha(z),\qquad
\liminf_{N\to\infty}N^{-1}\log\Pr\{Z_N\in O\}\ge-\inf_{z\in O}I_\alpha(z).
\tag{4}
\]
The centered central-limit refinement is
\[
\frac{\log(P/\kappa)-N[\psi(1)-\psi(m_N)]}{\sqrt N}
\ \Longrightarrow\ \mathcal N\!\left(0,\frac{\pi^2}{6}-\frac1\alpha\right),\qquad 1/\infty:=0.
\tag{5}
\]
Most importantly, *the Haar average is exponentially atypical*: in probability,
\[
\frac1N\log\frac{P}{\mathbb E P}\longrightarrow
-\Delta_\alpha,\qquad
\Delta_\alpha=\gamma-\int_0^1\log(1+u/\alpha)\,du>0,
\quad\Delta_\infty=\gamma.
\tag{6}
\]
For finite \(\alpha\), the integral is \((\alpha+1)\log(1+1/\alpha)-1\). The prefactor \(\kappa\) cancels from all relative-fluctuation and large-deviation conclusions: imperfect mutual indistinguishability changes the absolute full-bunching probability, but not its Haar-distributed normalized fluctuations.

## Assumptions and scope
The optical evolution is a Haar-random element of \(U(m)\), acting identically on each photon's spatial state and trivially on its internal state. There are exactly \(N\) single photons, occupying mutually distinct input modes, with normalized pure internal states in an arbitrary complex Hilbert space and no entanglement across photon preparations. The detector measures the event that all \(N\) photons reach **one preselected output port** and ignores internal degrees of freedom. The theorem does not refer to the union over all output ports. No photon loss, mixed internal preparations, correlations between input preparation and interferometer, or detector inefficiency is included.

## Proof
**1. Internal-state prefactor.** Define \(|\Phi\rangle=|\phi_1\rangle\otimes\cdots\otimes|\phi_N\rangle\). The all-in-one-output amplitude in the internal tensor space is the symmetrized vector \(\big(\prod_i U_{1i}\big)(N!)^{-1/2}\sum_{\sigma\in S_N}T_\sigma|\Phi\rangle\), with \(T_\sigma\) permuting tensor factors. Expanding its squared norm and using permutation invariance yields \(\operatorname{perm}(G)\prod_i|U_{1i}|^2\). Furthermore, the symmetrized tensor is nonzero: there exists an internal vector having nonzero inner product with each of the finitely many nonzero \(\phi_i\), so its tensor power has nonzero overlap with the symmetrized vector. Hence \(\kappa>0\). This step fixes the \(N!\) normalization: for fully identical internal states \(\kappa=N!\), whereas for orthogonal ones \(\kappa=1\).

**2. Haar moments.** A fixed row of a Haar unitary is a normalized vector of independent standard circular complex Gaussians. Its squared moduli therefore have the representation \(W_i=X_i/S_m\) with independent unit-rate exponentials \(X_i\) and \(S_m=\sum_{i=1}^mX_i\). The Dirichlet integral gives
\[
\mathbb E\prod_{i=1}^NW_i^t=
\frac{\Gamma(m)}{\Gamma(m+Nt)}\prod_{i=1}^N\Gamma(1+t),
\qquad t>-1.
\]
Differentiating the logarithm at \(t=0\) yields (2); the first derivative is the log-mean and the second is the log-variance.

**3. Large deviations.** For \(t>-1\), the exact log-moment-generating function of \(NZ_N\) is
\[
\log\mathbb Ee^{NtZ_N}
=Nt\log m+\log\Gamma(m)-\log\Gamma(m+Nt)
+N\log\Gamma(1+t).
\]
For finite \(\alpha\), the Gamma-ratio Stirling formula gives \(N^{-1}\log\mathbb Ee^{NtZ_N}\to F_\alpha(t)\) from (3), because the Riemann sum \(N^{-1}\sum_{j=0}^{N-1}\log(1+j/m)\) has an integral limit. When \(m/N\to\infty\), the ratio contribution after normalization is \(o(1)\), giving \(F_\infty(t)\). For \(t\le-1\), the moment diverges for every \(N\) because each Dirichlet coordinate has a nonintegrable negative power.

For finite \(\alpha\),
\[
F_\alpha'(t)=\psi(1+t)-\log(1+t/\alpha),\qquad
F_\alpha''(t)=\psi_1(1+t)-(\alpha+t)^{-1}>0.
\]
Strict positivity follows from \(\psi_1(x)>1/x\) for \(x>0\) and \(\alpha\ge1\). For \(\alpha=\infty\), the derivatives are \(\psi(1+t)\) and \(\psi_1(1+t)>0\). In all cases \(F_\alpha'(t)\to-\infty\) as \(t\downarrow-1\). Thus the limiting cumulant function is differentiable throughout its open effective domain, lower semicontinuous and steep at its finite boundary. Exponential tightness follows from finiteness of the moment-generating function at one positive and one negative \(t\). The Gärtner–Ellis theorem gives (3)–(4). For finite \(\alpha\), \(F_\alpha'(t)\uparrow\log\alpha\) as \(t\to\infty\), and the Stirling asymptotic shows \(I_\alpha(\log\alpha)=\infty\); the geometric–arithmetic mean inequality also gives the deterministic support bound \(Z_N\le\log(m/N)\). Finally \(F_\alpha'(0)=\psi(1)=-\gamma\), proving the claimed unique minimum.

**4. Gaussian scale.** Using the same exponential representation, write
\[
\log(P/\kappa)=\sum_{i=1}^N\log X_i-N\log S_m.
\]
The bivariate central-limit theorem for \((\log X_i,X_i)\), plus the remaining \(m-N\) exponentials, applies when \(m/N\to\alpha<\infty\). Its single-variable moments are \(\operatorname{Var}(\log X_i)=\pi^2/6\), \(\operatorname{Var}(X_i)=1\), and \(\operatorname{Cov}(\log X_i,X_i)=1\). Linearizing \(\log S_m\) at \(m\), the normalized variance is exactly \(\pi^2/6-1/\alpha\). If \(m/N\to\infty\), the denominator's centered contribution is \(o_{\Pr}(\sqrt N)\), leaving variance \(\pi^2/6\). Replacing the linearized deterministic center by \(N[\psi(1)-\psi(m)]\) changes it by \(O(1)\); thus (5) follows. Formula (2) provides the exact finite-size variance and checks the same limit.

**5. Exponential mean–typical gap.** The weak law for \(\log X_i\) and \(S_m/m\) gives \(Z_N\to-\gamma\) in probability. Independently, (2) and the Gamma-ratio product yield
\[
\frac1N\log\frac{m^N\mathbb EP}{\kappa}
=-\frac1N\sum_{j=0}^{N-1}\log(1+j/m)
\longrightarrow-\int_0^1\log(1+u/\alpha)\,du.
\]
Subtracting proves (6). The integral is at most \(1/(2\alpha)\le1/2\), while \(\gamma>1/2\), establishing strict positivity for all allowed ratios. This finishes the proof.

## Verification
Run the accompanying standalone Python 3 file using `python3 verify.py` (standard library only). It independently evaluates 162 rational integer moments, three direct internal-state symmetrization norms, three seeded Dirichlet sampling checks (each with 100,000 samples), 12 limiting cumulant comparisons, and four representative mean-gap/variance limits. Expected output begins `VERIFY_OK internal_symmetrization=3 exact_integer_Mellin=162`. The exact Gamma/Dirichlet integral and the Gärtner–Ellis hypotheses are verified in the proof; a finite simulation does **not** prove the asymptotic assertions.

## Relationship to prior work
Spagnolo et al. (2013), Eq. (5)–(7), proved the ideal-boson full-bunching amplification and performed experiments with finite random interferometer ensembles. Tichy (2014/2015), Sec. IV.3 Eq. (57), proved the permanent-of-distinguishability-Gram prefactor for pure product input states. These equations are explicit antecedents for the factorization in step 1. Liu et al. (2016) explored boson-sampler certification using Haar-random interferometers, including finite numerical tests; the paper does not formulate the one-port log-probability rate or its mean–typical exponent. Geller and Knill (2025), Appendix I, gave general Haar-*mean* bunching laws, encompassing averages of related events but not the present distributional rate analysis. The logarithmic-spacing central limit theory of Baryshnikov, Penrose and Yukich (2008) concerns a closely related classical Dirichlet mechanism; consequently, no standalone claim of novelty is made for the classical central-limit ingredient. The asserted contribution is the **explicit one-parameter, all-ratio large-deviation law with the strict exponential mean–typical separation for a fixed-port multiphoton bunching event**, including invariance under arbitrary pure product-state distinguishability.

## Limitations
The exact multiplicative factorization concerns one fixed output port and single occupancy of distinct inputs; the probability of all photons bunching at *some* output port is a sum of dependent row products and is not characterized by this theorem. The Haar assumption is essential. The proof does not cover mixed or entangled internal preparations, non-Haar optical ensembles, photon loss, noisy detectors, or experimental feasibility of observing exponentially rare events. The rate formula is an asymptotic probability law, not a finite-size confidence bound. The use of elementary Dirichlet statistics means that analogous purely classical probability statements may already be known; an independent literature-priority audit has not been conducted.

## References
1. N. Spagnolo et al., *General rules for bosonic bunching in multimode interferometers*, arXiv:1305.3188 (first submitted 2013-05-14), Eqs. (5)–(7). https://arxiv.org/abs/1305.3188
2. M. C. Tichy, *Sampling of partially distinguishable bosons and the relation to the multidimensional permanent*, arXiv:1410.7687 (first submitted 2014-10-28), Sec. IV.3 Eq. (57). https://arxiv.org/abs/1410.7687
3. K. Liu et al., *A certification scheme for the boson sampler*, arXiv:1607.03584 (first submitted 2016-07-13), Secs. II–III. https://arxiv.org/abs/1607.03584
4. Y. Baryshnikov, M. D. Penrose and J. E. Yukich, *Gaussian limits for generalized spacings*, arXiv:0804.4123 (2008), introduction and logarithmic-spacing CLT discussion. https://arxiv.org/abs/0804.4123
5. Geller and Knill, *Measuring Multiparticle Indistinguishability with the Generalized Bunching Probability*, arXiv:2509.04550 (2025), Appendix I, especially Lemma I.2. https://arxiv.org/abs/2509.04550
