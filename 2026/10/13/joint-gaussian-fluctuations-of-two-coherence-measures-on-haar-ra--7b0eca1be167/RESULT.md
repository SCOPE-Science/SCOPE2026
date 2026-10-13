# Joint Gaussian fluctuations of two coherence measures on Haar-random pure states

## Finding
For a Haar-uniform unit vector \(\psi\in\mathbb C^d\) with \(d\ge2\), fix the computational basis and put \(p_j=|\langle j|\psi\rangle|^2\). Consider the \(\ell_1\) coherence \(L_d=\sum_{i\ne j}\sqrt{p_i p_j}\), and the relative-entropy coherence \(H_d^{\mathrm{coh}}=-\sum_jp_j\log p_j\), in natural logarithmic units. Write \(h_d=\sum_{j=1}^d 1/j\) and let \(\psi_1\) denote the trigamma function.

Their exact finite-dimensional means, variances and covariance are
\[
\begin{aligned}
\mathbb EL_d&=\frac\pi4(d-1),&\mathbb EH_d^{\mathrm{coh}}&=h_d-1,\\
\operatorname{Var}(L_d)&=\frac{(d-1)\{d(16\pi-5\pi^2)+7\pi^2+32-32\pi\}}{16(d+1)},\\
\operatorname{Var}(H_d^{\mathrm{coh}})&=\frac{\pi^2/3-2}{d+1}-\psi_1(d+2)-\frac1{(d+1)^2},\\
\operatorname{Cov}(L_d,H_d^{\mathrm{coh}})&=\frac{\pi(d-1)}{2(d+1)}(3\log2-2).
\end{aligned}
\]
The means are known; the covariance and variances are supplied to normalize and check the joint fluctuation law, not claimed as mathematically independent of the classical Dirichlet moment formula.

For \(d\to\infty\), define
\[
X_d=\frac{L_d-\pi(d-1)/4}{\sqrt d},\qquad
Y_d=\sqrt d\,[H_d^{\mathrm{coh}}-(h_d-1)].
\]
Then the pair converges jointly in distribution to a **nondegenerate centered Gaussian** with covariance
\[
\boxed{\Sigma=\begin{pmatrix}
\pi-5\pi^2/16 & \frac\pi2(3\log 2-2)\\
\frac\pi2(3\log 2-2) & \pi^2/3-3
\end{pmatrix}.}
\]
The limiting correlation is approximately \(0.967907\), strictly smaller than one. Thus, even after optimal linear calibration of one standardized coherence measure from the other, a strictly positive residual fluctuation remains. The asymptotic residual variance of \(Y_d\) given the best linear prediction from \(X_d\) is \(\Sigma_{22}-\Sigma_{12}^2/\Sigma_{11}\approx0.018307\).

## Assumptions and scope
The state is distributed with Haar measure on the unit sphere of \(\mathbb C^d\). The reference basis is fixed; entries are complex (not real Haar-sphere coordinates). Logs are natural; \(d\) ranges through integers at least two. At finite \(d\), \(p_j\ge0\) and \(\sum_jp_j=1\); as usual define \(0\log0=0\). The limiting assertion concerns weak convergence of the displayed two-dimensional random vector and does not assert Gaussian tails at finite \(d\).

## Proof
**1. Exact distribution and moment identities.** Let \(E_j\) be independent mean-one exponential variables and \(T=\sum_jE_j\). The vector \((E_j/T)_j\) has the Dirichlet distribution with all parameters one, exactly the squared moduli of a Haar-uniform complex unit vector. Hence
\[
L_d=\Big(\sum_j\sqrt{p_j}\Big)^2-1,\qquad
H_d^{\mathrm{coh}}=-\sum_j p_j\log p_j.
\]
For arbitrary real \(s_j>-1\), the joint moment identity is
\[
\mathbb E\prod_jp_j^{s_j}=\frac{\Gamma(d)}{\Gamma(d+\sum_js_j)}\prod_j\Gamma(1+s_j).
\]
The mean coherence is \(d(d-1)\mathbb E\sqrt{p_1p_2}=\pi(d-1)/4\). Differentiating the moment formula in an exponent gives \(\mathbb EH_d^{\mathrm{coh}}=h_d-1\).

**2. Exact variance of \(L_d\).** The fourth power of \(\sum_j\sqrt{p_j}\) partitions into the five index-multiplicity patterns \((4)\), \((3,1)\), \((2,2)\), \((2,1,1)\), \((1,1,1,1)\). Applying the Dirichlet formula to each yields
\[
\mathbb E\Big(\sum_j\sqrt{p_j}\Big)^4=
\frac{3d-1+\frac32\pi(d-1)^2+\frac{\pi^2}{16}(d-1)(d-2)(d-3)}{d+1}.
\]
Subtracting \([1+\pi(d-1)/4]^2\) and factoring gives precisely the stated \(\operatorname{Var}(L_d)\); subtracting the deterministic one in \(L_d\) does not change variance.

**3. Exact covariance and entropy variance.** With \(\psi_0\) and \(\psi_1\) the digamma and trigamma functions, differentiation of the Dirichlet moment identity gives
\[
\begin{aligned}
\mathbb E[p_1^{3/2}p_2^{1/2}\log p_1]&=\frac{3\pi}{8d(d+1)}[\psi_0(5/2)-\psi_0(d+2)],\\
\mathbb E[p_1^{1/2}p_2^{1/2}p_3\log p_3]&=\frac{\pi}{4d(d+1)}[\psi_0(2)-\psi_0(d+2)].
\end{aligned}
\]
Counting whether the logarithm index coincides with one of the two indices in a term of \(L_d\), then subtracting the product of the means, gives \(\operatorname{Cov}(L_d,H_d^{\mathrm{coh}})=\pi(d-1)(3\log2-2)/(2(d+1))\). This uses \(\psi_0(5/2)-\psi_0(2)=5/3-2\log2\) and \(\psi_0(d+2)-\psi_0(d+1)=1/(d+1)\). (For \(d=2\), the terms with three distinct indices have zero multiplicity and require no three-index random variable.)

Similarly, differentiating \(\mathbb Ep_1^s\) twice at \(s=2\) and \(\mathbb Ep_1^sp_2^t\) once in each exponent at \(s=t=1\) supplies the diagonal and off-diagonal terms of \(\mathbb E(H_d^{\mathrm{coh}})^2\). After cancellation against \((h_d-1)^2\), the result is
\[
\operatorname{Var}(H_d^{\mathrm{coh}})=\frac{\pi^2/3-2}{d+1}-\psi_1(d+2)-\frac1{(d+1)^2}.
\]
These identities are exact at every integer \(d\ge2\), not asymptotic extrapolations.

**4. Joint central limit theorem.** Define empirical means \(A_d=d^{-1}\sum_j\sqrt{E_j}\), \(B_d=d^{-1}\sum_jE_j\), \(D_d=d^{-1}\sum_jE_j\log E_j\). Then identically
\[
L_d=dA_d^2/B_d-1,\qquad
H_d^{\mathrm{coh}}=\log d+\log B_d-D_d/B_d.
\]
The i.i.d. vectors \((\sqrt E,E,E\log E)\) have finite moments of every positive order. Their mean is \((\mu,1,1-\gamma)\), where \(\mu=\sqrt\pi/2\) and \(\gamma\) is Euler's constant. The multivariate central limit theorem and the smooth delta method apply to \(f(a,b,c)=a^2/b\) and \(g(a,b,c)=\log b-c/b\). Their gradient rows at the mean are \((2\mu,-\mu^2,0)\) and \((0,2-\gamma,-1)\).

For independent mean-one exponential \(E\), the needed covariance entries are
\[
\begin{aligned}
\operatorname{Var}(\sqrt E)&=1-\pi/4,&\operatorname{Cov}(\sqrt E,E)&=\mu/2,\\
\operatorname{Cov}(\sqrt E,E\log E)&=\mu(3-3\log2-\gamma/2),&\operatorname{Var}(E)&=1,\\
\operatorname{Cov}(E,E\log E)&=2-\gamma,&\operatorname{Var}(E\log E)&=\pi^2/3+1-4\gamma+\gamma^2.
\end{aligned}
\]
They follow by evaluating derivatives of \(\Gamma(s+1)=\mathbb EE^s\). Multiplying this covariance matrix on both sides by the two gradient rows gives exactly \(\Sigma\). The exact finite-dimensional center \(\mathbb EL_d=\pi(d-1)/4\) differs by \(O(1)\) from \(d\mu^2-1\), negligible on the \(\sqrt d\) scale. Also \(h_d=\log d+\gamma+O(d^{-1})\), so centering \(H_d^{\mathrm{coh}}\) at \(h_d-1\) is equivalent at scale \(\sqrt d\). Slutsky's theorem proves the displayed joint convergence.

**5. Strict nondegeneracy.** The two first-order influence functions are nonzero linear combinations of \(\sqrt E\), \(E\) and \(E\log E\). If their covariance were singular, they would be proportional almost surely; because the exponential distribution has positive density on all positive reals, continuity would force a relation between \(\sqrt x\), \(x\) and \(x\log x\) on \((0,\infty)\). Comparing their distinct growth laws proves no such proportionality. Therefore \(\det\Sigma>0\), and the residual variance is strictly positive.

## Verification
The included `verify_joint_coherence.py` uses standard-library arithmetic to compare two independent evaluations of \(\operatorname{Var}(L_d)\) for every dimension \(2\le d\le119\), checks covariance positivity, nondegeneracy, and uses independent exponential simulations at four dimensions to check both means, both variances and cross-covariance. Reproduction: `python3 verify_joint_coherence.py`. It prints `VERIFY_OK exact_second_moments=118 positive_covariance=passed independent_monte_carlo=4_datasets bivariate_limit=passed`. Sampling supports numerical checks only; the infinite-dimensional claim follows from the i.i.d. central limit theorem and delta method.

## Relationship to prior work
Puchała, Pawela and Życzkowski (arXiv:1507.05123, Sec. VIII, Eq. (61)–(62)) supply the underlying Dirichlet mixed-moment identity and the pure-state mean of \(\ell_1\) coherence. Thus neither the Dirichlet law, the general moment identity, nor this mean is claimed as original. Cheng and Hall (arXiv:1508.03240, Sec. IV) study coherence averaged over measurement bases for fixed quantum states, while Singh, Zhang and Pati (arXiv:1509.08939, Secs. III–IV) give typicality and bounds involving relative entropy and \(\ell_1\) coherence. Their inspected results do not state the present explicit **joint Gaussian limit** for the two differently scaled coherence measures, its exact cross-covariance, or the fact that their Gaussian fluctuations remain linearly distinct. General multivariate central limit and delta-method theorems supply standard techniques; the specific covariance calculation is a specialization that could appear elsewhere under joint Shannon–Rényi functional language.

## Limitations
The limit is asymptotic for Haar-complex pure states, not a finite-dimensional Gaussian identity. No convergence rate, large-deviation estimate, distributional tail bound, real-amplitude analogue, or mixed-state analogue is claimed. The two coherence statistics are strongly correlated, but not independent. Equivalent formulations in the broader classical Dirichlet-distribution literature remain a priority risk. Scientific correctness and priority have not been independently reviewed.

## References
1. Z. Puchała, Ł. Pawela and K. Życzkowski, *Distinguishability of generic quantum states*, arXiv:1507.05123 (first public 17 July 2015), especially Section VIII and equations (59)–(62); https://arxiv.org/pdf/1507.05123.
2. S. Cheng and M. J. W. Hall, *Complementarity relations for quantum coherence*, arXiv:1508.03240 (first public 13 August 2015), Sections III–IV; https://arxiv.org/pdf/1508.03240.
3. U. Singh, L. Zhang and A. K. Pati, *Average coherence and its typicality for random pure states*, arXiv:1509.08939 (first public 29 September 2015), Sections III–IV; https://arxiv.org/pdf/1509.08939.
