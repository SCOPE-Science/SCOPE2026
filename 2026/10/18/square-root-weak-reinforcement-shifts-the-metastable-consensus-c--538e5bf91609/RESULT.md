# Square-root weak reinforcement shifts the metastable consensus clock

## Finding
Fix any real \(c\ge0\). For the power-weighted conclave process on \(n\) initially singleton candidates, set \(\alpha_n=c/\sqrt n\). With \(T_n\) denoting the first unanimous round, the following exact asymptotics hold as integers \(n\to\infty\):

\[
\frac{T_n}{2^{n-1}e^{-c^2/2}}\ \Longrightarrow\ \operatorname{Exp}(1),
\qquad
\frac{\mathbb E T_n}{2^{n-1}e^{-c^2/2}}\longrightarrow1.
\]

Let \(S_t\) be the number of positive tallies in round \(t\), and \(\tau_2=\inf\{t:S_t\le2\}\). Then \(\mathbb E\tau_2\le n(3/2)^n\), and \(\Pr(S_{\tau_2}=2)\to1\). Thus the exponential waiting occurs overwhelmingly on the last two-candidate face. The correction \(e^{-c^2/2}\) is nonconstant already in the critical weak-reinforcement window.

## Assumptions and scope
There are exactly \(n\ge3\) voters and initially \(n\) labels each receiving one vote. At each integer round, conditional on tallies \((x_1,\ldots,x_n)\) with sum \(n\), all voters draw independently among positive-tally labels, assigning probability \(x_i^{\alpha_n}/\sum_{j:x_j>0}x_j^{\alpha_n}\) to label \(i\). A zero tally remains zero forever. The stated case \(c=0\) uses weights equal to one for positive tallies and zero for zero tallies; for \(c>0\) it is the paper's ordinary power rule. Parameter \(c\) is fixed, not growing with \(n\); time counts complete voting rounds. All asymptotics are with respect to voting randomness at each \(n\).

## Proof
**1. Rapid contraction to two surviving labels.** If \(S_t=j\ge3\), some surviving label has probability at most \(1/j\) on the next ballot, because its tally is minimal and the weight is nondecreasing. Its extinction probability in the next round is therefore at least \((1-1/j)^n\ge(2/3)^n\). Since the surviving-label count never increases, sum the upper expected holding times over the at most \(n-2\) levels to obtain \(\mathbb E\tau_2\le n(3/2)^n\). Every nonzero weight lies between \(1\) and \(n^{\alpha_n}\), so from any state with at least three positive tallies the chance of directly producing a unanimous next round is at most \(n(n^{\alpha_n}/3)^n\). Summing this upper bound over the expected number of pre-\(\tau_2\) steps gives

\[
\Pr(S_{\tau_2}=1)\le n^2(3/2)^n(n^{\alpha_n}/3)^n
=\exp\{-n\log2+O_c(\sqrt n\log n)\}=o(1).
\]

**2. Exact two-candidate killing law.** Label the surviving tallies \(a\) and \(n-a\), with \(1\le a\le n-1\). Define

\[
p_n(a)=\frac{a^{\alpha_n}}{a^{\alpha_n}+(n-a)^{\alpha_n}},\quad
\theta_n(a)=\alpha_n\log\frac a{n-a},\quad
r_n=2^{1-n}.
\]

The next tally of the first survivor is \(B\sim\operatorname{Bin}(n,p_n(a))\). Absorption occurs for \(B\in\{0,n\}\), with exact probability

\[
h_n(a)=p_n(a)^n+(1-p_n(a))^n,
\qquad
\frac{h_n(a)}{r_n}
=\frac{\cosh(n\theta_n(a)/2)}{\cosh(\theta_n(a)/2)^n}.
\]

The elementary bounds \(\lvert\theta_n(a)\rvert\le c\log(n-1)/\sqrt n\) and \(\cosh u\le e^{\lvert u\rvert}\) yield \(r_n\le h_n(a)\le\varepsilon_n\), where \(\varepsilon_n=r_n\exp\{c\sqrt n\log n/2\}=\exp\{-n\log2+o(n)\}\). In particular, \(\varepsilon_n^2=o(r_n)\).

**3. Rapid mixing of a resurrected two-label chain.** Let \(Q_n(a,b)=\Pr(B=b)\) for \(1\le a,b\le n-1\). Define \(\nu_n\) to be \(\operatorname{Bin}(n,1/2)\) conditioned on \(1\le B\le n-1\), and the Markov kernel

\[
P_n(a,b)=Q_n(a,b)+h_n(a)\nu_n(b).
\]

This chain is strictly positive and has a unique invariant law \(\pi_n\). Put \(G_n=\{a:\lvert a-n/2\rvert\le n^{2/3}\}\). Uniformly over all interior \(a\), \(p_n(a)=1/2+O_c(\log n/\sqrt n)\). Hoeffding concentration, including the reset part, gives \(\sup_a P_n(a,G_n^c)\le e^{-\kappa_c n^{1/3}}\), for all sufficiently large \(n\). For \(b\in G_n\), Taylor expansion gives \(p_n(b)=1/2+O_c(n^{-5/6})\). The Kullback--Leibler divergence between the corresponding \(n\)-fold Bernoulli product and fair Bernoulli product is \(O_c(n^{-2/3})\). Data processing and Pinsker's inequality therefore imply

\[
\sup_{b\in G_n}\|P_n(b,\cdot)-\nu_n\|_{\mathrm{TV}}=O_c(n^{-1/3}),
\qquad
\sup_a\|P_n^2(a,\cdot)-\nu_n\|_{\mathrm{TV}}=O_c(n^{-1/3}).
\]

Consequently the Dobrushin contraction coefficient of \(P_n^2\) is \(\delta_n=O_c(n^{-1/3})\), and \(\pi_n(G_n^c)\le e^{-\kappa_c n^{1/3}}\).

**4. Sharp stationary killing rate.** Define \(M_n(b)=h_n(b)/r_n\), \(\lambda_n=\sum_a\pi_n(a)h_n(a)\), and

\[
g_n(a)=\mathbb E\big[M_n(B)\mathbf1_{\{1\le B\le n-1\}}\mid B\sim\operatorname{Bin}(n,p_n(a))\big],
\qquad
\beta_n=\mathbb E_{B\sim\nu_n}M_n(B).
\]

Applying stationarity of \(\pi_n\) to the function \(M_n\) yields the **exact identity**

\[
\frac{\lambda_n}{r_n}\,(1-r_n\beta_n)=\sum_a\pi_n(a)g_n(a).
\]

For \(a\in G_n\), the standardized variable \(Z_n=(B-n/2)/\sqrt n\) converges uniformly in distribution to \(Z\sim N(0,1/4)\), because the shift \(\sqrt n(p_n(a)-1/2)=O_c(n^{-1/3})\). For \(B=n/2+\sqrt n z\) in a fixed central window, the exact expression from step 2 gives \(M_n(B)\to\cosh(2cz)\). Uniform integrability follows by splitting at \(B\in[n/4,3n/4]\), where \(M_n(B)\le e^{C_c\lvert Z_n\rvert}\), and outside, where the binomial tail is \(e^{-\Omega(n)}\) and \(M_n(B)\le e^{O_c(\sqrt n\log n)}\). For all \(a\), the mean of \(Z_n\) is \(O_c(\log n)\), so the same exponential-moment bound gives \(g_n(a)\le n^{K_c}\) for some fixed \(K_c\). Therefore, uniformly on \(G_n\),

\[
g_n(a)\longrightarrow \mathbb E\cosh(2cZ)=e^{c^2/2},
\qquad \beta_n\longrightarrow e^{c^2/2}.
\]

The exponentially small stationary mass of \(G_n^c\), multiplied by the polynomial bound on \(g_n\), is negligible. Since \(r_n\beta_n\to0\), the exact stationarity identity proves

\[
\boxed{\lambda_n/r_n\longrightarrow e^{c^2/2}.}
\]

**5. Exponential absorption clock and its mean.** For a distribution \(\mu\) on the interior states, the next-state law conditional on surviving a round is \(\Phi_n(\mu)=\mu Q_n/(1-\mu h_n)\). Because \(\mu P_n=(1-\mu h_n)\Phi_n(\mu)+(\mu h_n)\nu_n\), its total-variation distance from \(\Phi_n(\mu)\) is at most \(\varepsilon_n\). Combining this perturbation with the two-step contraction in step 3 yields, from **any** initial interior tally, and at all times after an even burn-in \(L_n=O(n/\log n)\),

\[
\|\mathcal L(A_t\mid\text{survival through }t)-\pi_n\|_{\mathrm{TV}}
\le e^{-2n}+O_c(\varepsilon_n),
\]

where the coefficient in \(L_n\) is chosen large enough; this follows by iteration of the contraction recurrence \(d_{t+2}\le\delta_n d_t+O(\varepsilon_n)\). The probability of extinction before burn-in is at most \(L_n\varepsilon_n=o(1)\). Thereafter, the conditional killing probability per round equals

\[
\lambda_n+O_c\big(\varepsilon_ne^{-2n}+\varepsilon_n^2\big)
=\lambda_n(1+o(1)),
\]

uniformly in the initial tally, since \(\lambda_n\asymp r_n\). Multiplying the survival probabilities for \(\lfloor u/\lambda_n\rfloor\) rounds gives the mean-one exponential limit. Also \(h_n(a)\ge r_n\), so the remaining lifetime is stochastically bounded by a geometric random variable of parameter \(r_n\); the scaled lifetimes are uniformly integrable and their means are asymptotic to \(1/\lambda_n\).

Finally \(\mathbb E\tau_2\le n(3/2)^n=o(1/r_n)\). Combining the strong Markov property at \(\tau_2\), uniformity of the two-label law over the entrance tally, and the negligible chance of skipping the two-label face proves both asserted full-process limits.

## Verification
Run \(\texttt{python verify.py}\) with NumPy and SciPy installed. The checker verifies the exact hyperbolic-cosine killing identity over finite sizes, the uniform-weight exact binary hazard in rational arithmetic, transition-mass normalization, and convergence diagnostics for finite matrix quasi-stationary rates. In checks with \(n=640\), the normalized rates \(2^{n-1}\lambda_n\) were approximately \(1.00000,1.13340,1.65067,7.45930\) for \(c=0,0.5,1,2\), respectively, versus predicted limits \(1,1.13315,1.64872,7.38906\). The program completed 408 finite assertions; the infinite results rest on steps 1--5, not numerical convergence.

## Relationship to prior work
Benjamini, Cai, Chen, Gong and Li define this exact multinomial process and show an exponential lower bound for the absorption time at **fixed** \(0<\alpha<1\), with constants depending on the exponent. Their Theorem 1.5 and its proof do not provide the sharp exponential-clock distribution, leading constant, or the shrinking-exponent window \(\alpha_n=c/\sqrt n\). The Wright--Fisher and coalescent discussion in that paper concerns \(\alpha=1\), not the rapidly mixing binary dynamics in the present result. General rare-event perturbation and binomial Gaussian limit methods are established tools; their use here does not constitute a claim that the tools are new.

## Limitations
The asymptotic coefficient is established for each fixed \(c\ge0\), not uniformly for \(c=c_n\to\infty\) or for arbitrary fixed positive \(\alpha\). The result concerns the first fully unanimous round; real-world two-thirds decision thresholds, correlated ballots, and time-varying populations are outside the proof. No quantitative convergence rate in the exponential limit is asserted. Earlier unindexed treatments of the same weak-exponent window could affect priority; no independent priority audit has been carried out.

## References
Benjamini, I., Cai, Z., Chen, G., Gong, S., and Li, Z., *The Conclave Process*, arXiv:2607.22324 (first submitted July 24, 2026), https://arxiv.org/abs/2607.22324. Classical ingredients: binomial central limit theorem, Hoeffding concentration, Pinsker inequality, and the Dobrushin contraction estimate for finite Markov kernels.
