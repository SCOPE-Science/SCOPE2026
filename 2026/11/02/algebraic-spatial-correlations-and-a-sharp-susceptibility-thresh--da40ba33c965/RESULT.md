# Algebraic spatial correlations and a sharp susceptibility threshold in a globally reset kinetic Ising chain

## Finding

Consider the one-dimensional, zero-temperature Glauber (voter) chain on the full lattice \(\mathbb Z\), globally reset to one initial independent spin configuration at renewal times with a Pareto interarrival distribution. For every tail exponent \(\alpha>1\), initial spin mean \(-1<m<1\), and scale \(\tau_0>0\), the stationary **annealed connected spin covariance** at separation \(n\) is positive and has the sharp asymptotic

\[
C_n:=\mathbb E[\sigma_0\sigma_n]-m^2
\sim K_{\alpha,m,\tau_0}\,n^{-2(\alpha-1)},\qquad
K_{\alpha,m,\tau_0}=\frac{1-m^2}{\alpha}\,(4\tau_0)^{\alpha-1}\frac{\Gamma(\alpha-\tfrac12)}{\sqrt\pi}.
\]

Consequently, its spatial susceptibility \(\chi=\sum_{n\in\mathbb Z}C_{|n|}\) is finite **if and only if** \(\alpha>3/2\). At the threshold the truncated susceptibility grows logarithmically. In the stationary ensemble the variance of a block average of \(L\) spins obeys the complete trichotomy

\[
\operatorname{Var}\!\left(\frac1L\sum_{i=1}^L\sigma_i\right)
\sim
\begin{cases}
\displaystyle\frac{2K_{\alpha,m,\tau_0}}{(3-2\alpha)(4-2\alpha)}L^{-2(\alpha-1)},&1<\alpha<\tfrac32,\\[5pt]
\displaystyle\frac{2K_{3/2,m,\tau_0}\log L}{L},&\alpha=\tfrac32,\\[5pt]
\displaystyle\frac{\chi}{L},&\alpha>\tfrac32.
\end{cases}
\]

A supplementary renewal boundary statement holds when \(0<\alpha\le1\): there is no normalizable equilibrium-age distribution, and the finite-dimensional, annealed law of the spins at large time converges to the mixture of the two spatially uniform spin configurations, with respective probabilities \((1+m)/2\) and \((1-m)/2\). This is a local weak limit, **not** an assertion of convergence of the spatial magnetization in an infinite system.

The result includes an exact Mellin/Gamma identity for the underlying diffusive coalescence time, yielding an explicit controlled asymptotic rather than an exponent-only scaling argument.

## Assumptions and scope

1. Lattice: sites \(i\in\mathbb Z\), spins \(\sigma_i\in\{-1,+1\}\), no external field, strictly zero temperature. Each site updates at rate one and copies its left or right nearest neighbor with probability one-half. This is precisely the one-dimensional zero-temperature heat-bath Glauber rule, including equal-neighbor-energy tie flips. A dual lineage jumps to each neighbor at rate \(1/2\).
2. Initial state: one configuration \(\eta\) drawn from independent spins with \(\mathbb P(\eta_i=+1)=(1+m)/2\), \(-1<m<1\). At each reset **all** spins are simultaneously replaced with this same \(\eta\), rather than with a new sample. The renewal clock, initial spins, and graphical Poisson updates are independent.
3. The inter-reset times \(I\) are independent with density \(\alpha\tau_0^{\alpha}t^{-1-\alpha}\mathbf1_{\{t\ge\tau_0\}}\), with \(\tau_0>0\) and \(\alpha>0\). The process starts at a reset at time zero; the term 'stationary annealed' refers to the time-asymptotic distribution after averaging the initial configuration and all dynamic randomness.
4. The assertions for \(\alpha>1\) apply to each fixed lattice separation followed by the limit of large separation within the resulting stationary annealed law; they do not assume a finite ring or an externally fixed microcanonical magnetization.
5. The random variable \(T_n\), \(n\ge1\), is the first hitting time of zero by the continuous-time simple random walk on \(\{0,1,\ldots\}\), started at \(n\), whose generator on positive integers is \((\Delta f)(j)=f(j-1)-2f(j)+f(j+1)\). Thus each direction has jump rate one, and the total jump rate is two. This is the separation of two independent voter dual lineages before coalescence.

## Proof

**1. Two-point coalescence identity.** Fix an age \(t\) since the most recent global reset. Trace the spins at sites \(0\) and \(n\) backward via the voter graphical construction. Each is copied from an ancestral initial spin at time zero. The two dual lineages coalesce exactly when their separation walk hits zero by time \(t\). Before coalescence the sampled initial spins are distinct independent \(\eta\)-variables, with product expectation \(m^2\); after coalescence they are the same \(\eta\)-variable, with product expectation one. Therefore, if \(F_n(t)=\mathbb P(T_n\le t)\),

\[
\mathbb E[\sigma_0(t)\sigma_n(t)\mid A=t]
=m^2+(1-m^2)F_n(t),\qquad
\mathbb E[\sigma_i(t)\mid A=t]=m.
\]

The clock age \(A\) is independent of the graphical dynamics within the current renewal interval. Reusing the same initial configuration across distinct intervals does not affect this single-time annealed formula.

**2. Stationary renewal age and its exact survival law.** Suppose \(\alpha>1\). The mean interval length is \(\mu=\alpha\tau_0/(\alpha-1)\). The equilibrium age has density \(a\mapsto\mathbb P(I>a)/\mu\), hence survival function

\[
H(a):=\mathbb P(A\ge a)=
\begin{cases}
1-a/\mu,&0\le a<\tau_0,\\
\displaystyle\frac{\tau_0^{\alpha-1}}{\alpha}a^{1-\alpha},&a\ge\tau_0.
\end{cases}
\]

Integrating the coalescence indicator over the independent equilibrium age and then interchanging expectation gives the exact identity

\[
C_n=(1-m^2)\mathbb E[H(T_n)],\qquad n\ge1,
\]

with \(C_0=1-m^2\). In particular every finite-distance covariance is positive. Notice that this is a **survival** average \(\mathbb E[H(T_n)]\), not an average of the age density.

**3. Exact walk Laplace transform and Mellin identity.** The unique bounded solution of \((s-\Delta)u=0\) on the positive half-line satisfying \(u(0)=1\) is \(u(n)=q(s)^n\), where

\[
q(s)=1+\frac s2-\sqrt{s+\frac{s^2}{4}}
=\exp\!\left[-\operatorname{arcosh}\!\left(1+\frac s2\right)\right].
\]

Consequently \(\mathbb E[e^{-sT_n}]=q(s)^n\). For any fixed \(b>0\) and integer \(n>b\), Mellin inversion followed by the substitution \(q=q(s)\), equivalently \(s=(1-q)^2/q\), yields

\[
\begin{aligned}
\mathbb E[T_n^{-b}]
&=\frac{1}{\Gamma(b)}\int_0^\infty s^{b-1}q(s)^n\,ds\\
&=\frac{1}{\Gamma(b)}\int_0^1q^{n-b-1}(1-q)^{2b-1}(1+q)\,dq\\
&=\frac{B(n-b,2b)+B(n-b+1,2b)}{\Gamma(b)}\\
&=\boxed{\frac{2n\,\Gamma(2b)\Gamma(n-b)}{(n+b)\Gamma(b)\Gamma(n+b)}}.
\end{aligned}
\]

The integral and formula require \(n>b\). In particular, by the Gamma-ratio asymptotic,

\[
\mathbb E[T_n^{-b}]
=\frac{2\Gamma(2b)}{\Gamma(b)}n^{-2b}(1+O(n^{-1}))
=\frac{4^b\Gamma(b+\tfrac12)}{\sqrt\pi}n^{-2b}(1+O(n^{-1})).
\]

This identity exactly fixes the microscopic diffusion normalization; a separation walk with rate one **per direction**, not rate one total, is essential for the coefficient above.

**4. Removing the short-age cutoff rigorously.** Set \(b=\alpha-1>0\), \(c=\tau_0^b/\alpha\). For \(a\ge\tau_0\), \(H(a)=ca^{-b}\). For \(a<\tau_0\), the tangent-line inequality \(x^{-b}\ge1+b(1-x)\) for \(0<x\le1\) implies \(H(a)\le ca^{-b}\). Thus for \(n>b\), \(\mathbb E[H(T_n)]\le c\mathbb E[T_n^{-b}]\), and the difference is nonnegative. Its size is at most

\[
0\le c\mathbb E[T_n^{-b}]-\mathbb E[H(T_n)]
\le c\mathbb E[T_n^{-b}\mathbf1_{\{T_n<\tau_0\}}].
\]

For \(n>2b\), Cauchy–Schwarz bounds the right side by \(c(\mathbb E[T_n^{-2b}])^{1/2}\mathbb P(T_n<\tau_0)^{1/2}\). Reaching zero from \(n\) requires at least \(n\) jumps of a rate-two Poisson process. Therefore, for \(n>2e\tau_0\),

\[
\mathbb P(T_n<\tau_0)\le\mathbb P(\operatorname{Poisson}(2\tau_0)\ge n)
\le\left(\frac{2e\tau_0}{n}\right)^n.
\]

The exact Mellin identity with exponent \(2b\) shows \(\mathbb E[T_n^{-2b}]=O(n^{-4b})\). The cutoff discrepancy is consequently smaller than every inverse power of \(n\). Combining with the preceding Gamma asymptotic proves

\[
C_n\sim(1-m^2)\frac{\tau_0^b}{\alpha}\frac{4^b\Gamma(b+\tfrac12)}{\sqrt\pi}\,n^{-2b},
\]

which is precisely the stated positive constant.

**5. Susceptibility and block fluctuations.** The stationary annealed covariance is translation invariant, even in the presence of resets to a shared random initial environment. Write \(p=2b=2(\alpha-1)\). Then \(C_n\sim K n^{-p}\) with \(K>0\). A direct comparison with \(\sum n^{-p}\) gives \(\chi<\infty\) exactly when \(p>1\), i.e. \(\alpha>3/2\). For the truncated symmetric sum \(\chi_L=C_0+2\sum_{n=1}^LC_n\), the divergent cases have sharp laws

\[
\chi_L\sim\begin{cases}
\displaystyle\frac{2K}{3-2\alpha}L^{3-2\alpha},&1<\alpha<\tfrac32,\\[3pt]
2K\log L,&\alpha=\tfrac32.
\end{cases}
\]

For \(M_L=L^{-1}\sum_{i=1}^L\sigma_i\), summing covariance pairs gives the exact identity

\[
\operatorname{Var}(M_L)=\frac{C_0}{L}+\frac{2}{L^2}\sum_{n=1}^{L-1}(L-n)C_n.
\]

For \(0<p<1\), the weighted power sum is asymptotic to \(L^{2-p}/[(1-p)(2-p)]\). For \(p=1\), it is \(L\log L(1+o(1))\). For \(p>1\), dominated convergence of \(L\operatorname{Var}(M_L)\) gives \(\chi\). This proves the three regimes and their sharp coefficients.

**6. Infinite-mean renewal boundary.** If \(0<\alpha\le1\), the renewal mean is infinite, so the preceding stationary age construction is unavailable. For any fixed \(a>0\), the standard nonlattice renewal theorem for infinite-mean continuous interarrivals gives \(\mathbb P(A_t\le a)\to0\). In the unreset zero-temperature one-dimensional voter chain, any fixed finite family of backward dual lineages coalesces almost surely by a finite random time because one-dimensional symmetric walks recurrently meet. Hence their spins converge jointly as the age tends to infinity to one shared initial \(\eta\)-spin. Since that ancestral \(\eta\)-spin has probabilities \((1\pm m)/2\), mixing over \(A_t\to\infty\) establishes the stated finite-dimensional mixture. No assertion of convergence in a stronger infinite-volume topology follows from this argument.

## Verification

The standalone script `verification.py` (Python with SciPy) independently compares (i) the exact Gamma/Mellin negative-moment identity against its defining Laplace integral, (ii) the stationary covariance computed using the Bessel first-hitting-time density against the predicted asymptotic constant at several exponents and separations, (iii) the exact equilibrium-age continuity/normalization, and (iv) the exact stationary covariance bounds. It prints the number of completed checks and exits nonzero if any check fails. The finite numerical tests validate coefficient normalization and implementation consistency; they cannot prove a spatial limit or a publication-priority claim. Running from the extracted package directory: `python verification.py` (requirements in `requirements.txt`).

## Relationship to prior work

Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting* (first public arXiv submission February 17, 2026), establish a Pareto global-reset Ising framework and study spatially averaged magnetization and its distribution, including a one-dimensional dynamical relaxation formula. The present work studies **strictly zero temperature, microscopic equal-time two-point correlations**, deriving the full spatial exponent, prefactor, a summability boundary, and exact block variance laws; these are not statements of their magnetization distribution.

Pascal Grange, *Voter model under stochastic resetting* (arXiv:2207.08590), derives spatial two-point information for a distinctly different prescription: **independent Poisson resetting at each lattice site**. Neither the same-clock renewal-age mixture nor the Pareto exponent threshold follows from that local reset construction. Magoni, Majumdar and Schehr, *Ising model with stochastic resetting* (arXiv:2002.04867), study the global **Poisson** protocol and magnetization phases rather than the claimed Pareto pair-covariance law. Classical coalescing-walk duality for one-dimensional voter dynamics is used, not claimed as new.

A general renewal-mixture theorem combined with a coalescence first-passage kernel could potentially imply individual steps, so an unlocated broader formulation remains an originality risk; the complete model-specific spatial susceptibility and block fluctuation crossover is the claim assessed here.

## Limitations

- Results are for the annealed infinite-line, zero-temperature, biased independent initial spin ensemble, with a shared global renewal clock. They do not claim positive-temperature persistence, quenched-initial-configuration asymptotics, or finite-ring thermodynamic uniformity.
- The susceptibility is an equal-time connected **spatial sum**, not a thermodynamic field-response function. Its divergence is a spatial-correlation statement, not a claim of a finite-temperature phase transition.
- At \(0<\alpha\le1\), the limiting uniform-mixture conclusion is only local weak convergence; there is no normalizable stationary renewal age. The stationary spatial asymptotic and block formulas require \(\alpha>1\).
- Numerical calculations are finite checks. The infinite-distance and infinite-time statements depend on the above analytical argument.
- The comparison against known work is based on accessible primary materials and semantic research searches; it does not constitute a proof that no broader, as-yet-unlocated theorem covers the result. Independent audit has not been performed.

## References

1. Anagha V K and Apoorva Nagar, *Ising Model with Power Law Resetting*, arXiv:2602.15495v1 (first publicly submitted 2026-02-17), https://arxiv.org/html/2602.15495v1 . Relevant primary material: Sections II and III, renewal-age and one-dimensional magnetization formulas.
2. Pascal Grange, *Voter model under stochastic resetting*, arXiv:2207.08590v6 (2023 version), https://arxiv.org/html/2207.08590v6 . Relevant primary material: Introduction, Section 2.1 and Section 2.3 (local Poisson resetting and two-point functions).
3. Matteo Magoni, Satya N. Majumdar and Grégory Schehr, *Ising model with stochastic resetting*, arXiv:2002.04867 (2020), https://arxiv.org/abs/2002.04867 . Global memoryless-reset background.
4. T. M. Liggett, *Interacting Particle Systems*, Springer (1985), classical voter-model graphical duality and coalescing random walks.
5. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II, Wiley, renewal theorems for nonarithmetic interarrivals; the infinite-mean renewal-age boundary is used only in the supplementary statement.
