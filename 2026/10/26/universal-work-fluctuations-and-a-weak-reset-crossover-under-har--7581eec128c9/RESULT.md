# Universal work fluctuations and a weak-reset crossover under harmonic partial resetting

## Finding
Fix positive diffusivity \(D\) and harmonic resetting stiffness \(\kappa\). A particle diffuses freely for independent positive exploration times \(T_j\), then its endpoint \(Y_j\) is contracted to \(aY_j\), with \(0\le a<1\), before the next free exploration. Assume \(m=\mathbb ET_j\in(0,\infty)\) and \(v=\operatorname{Var}(T_j)<\infty\). In the stationary event-indexed process, define the accumulated harmonic resetting work after \(n\ge1\) completed contractions as
\[
 W_n=\frac{\kappa(1-a^2)}2\sum_{j=1}^nY_j^2.
\]
With \(q=a^2\), its mean and its **exact finite-count variance** are
\[
 \boxed{\mathbb EW_n=n\kappa Dm},
\]
\[
 \boxed{\operatorname{Var}(W_n)=\kappa^2D^2\left(2m^2+3v\frac{1-q}{1+q}\right)
 \left[n\frac{1+q}{1-q}-\frac{2q(1-q^n)}{(1-q)^2}\right].}
\]
Consequently, for each fixed \(0\le a<1\), the central limit theorem holds:
\[
 \frac{W_n-n\kappa Dm}{\sqrt n}\ \Longrightarrow\
 \mathcal N\!\left(0,\ \kappa^2D^2\left[2m^2\frac{1+a^2}{1-a^2}+3v\right]\right).
\]
In particular, the mean work per completed reset does not depend on resetting strength, whereas the asymptotic variance per reset diverges as \(4\kappa^2D^2m^2/(1-a^2)\) as \(a\uparrow1\). The contribution \(3\kappa^2D^2v\) from randomness in exploration durations is exactly independent of \(a\).

There is a **universal non-Gaussian critical window**: as \(\varepsilon=1-a^2\downarrow0\), take a number of resets \(n=n(\varepsilon)\) with \(n\varepsilon\to\ell\in(0,\infty)\). Then
\[
 \boxed{\frac{W_n}{n\kappa Dm}\Longrightarrow
 \frac1\ell\int_0^\ell Z_t^2\,dt,}
\]
where \(Z\) is the *stationary* Ornstein--Uhlenbeck diffusion \(dZ_t=-Z_t\,dt/2+dB_t\), with \(Z_0\sim\mathcal N(0,1)\) independent of future Brownian noise. The limiting random variable is non-Gaussian, positive, has mean one, and variance
\[
 \boxed{\frac{4(\ell-1+e^{-\ell})}{\ell^2}.}
\]
This limit is independent of the detailed exploration-time distribution subject to the stated moment conditions. It interpolates between a \(\chi^2_1\) work ratio as \(\ell\downarrow0\) and a self-averaging ratio with variance asymptotic to \(4/\ell\) as \(\ell\to\infty\).

## Assumptions and scope
Take mutually independent exploration times \((T_j)_{j\in\mathbb Z}\) and standard Brownian increments on each exploration interval; the Brownian motion driving distinct intervals is independent. The durations \(T_j>0\) are identically distributed with \(\mathbb ET_j=m\in(0,\infty)\) and \(\mathbb ET_j^2<\infty\). The endpoint recursion is \(Y_j=aY_{j-1}+\xi_j\), with \(\xi_j\mid T_j\sim\mathcal N(0,2DT_j)\). Prepare the endpoint chain in its unique stationary distribution. Contractions are exactly proportional, \(Y_j\mapsto aY_j\), and the work definition is the decrease of \(\Phi(y)=\kappa y^2/2\) between the two endpoints, under free exploration potential zero. This is a **completed-reset-count ensemble**: no assertion is made for work measured after a fixed elapsed physical time, and the internal duration/dynamics of the contraction phase is not prescribed beyond its endpoint and work rule. The case \(a=1\) is excluded (its work is identically zero and it has no stationary unconfined positional law).

## Proof
**1. Stationary endpoint chain and its cumulants.** Write \(\sigma^2=\mathbb E\xi_j^2=2Dm\). Conditioning on \(T_j\) gives \(\mathbb E\xi_j^4=12D^2\mathbb ET_j^2\), hence \(\operatorname{cum}_4(\xi_j)=12D^2v\). The bilateral moving-average representation \(Y_j=\sum_{h\ge0}a^h\xi_{j-h}\) converges in \(L^4\) and gives the unique stationary law. Independence of increments and additivity of cumulants imply
\[
 V_2:=\mathbb EY_j^2=\frac{2Dm}{1-q},\qquad
 \operatorname{cum}_4(Y_j)=\frac{12D^2v}{1-q^2}.
\]
Therefore
\[
 \operatorname{Var}(Y_j^2)=2V_2^2+\frac{12D^2v}{1-q^2}.
\]

**2. Exact covariance and finite-count work.** Since \(Y_{j+h}=a^hY_j+\eta_{j,h}\), with the centered independent innovation block \(\eta_{j,h}\), the conditional quadratic regression is
\[
 \mathbb E[Y_{j+h}^2-V_2\mid Y_j]=q^h(Y_j^2-V_2).
\]
Hence the exact covariance is \(\operatorname{Cov}(Y_j^2,Y_{j+h}^2)=q^h\operatorname{Var}(Y_j^2)\). Multiplying by \(\kappa^2(1-q)^2/4\) yields single-reset work variance \(\kappa^2D^2[2m^2+3v(1-q)/(1+q)]\) and covariance proportional to \(q^h\). Summing pairs, using
\[
 n+2\sum_{h=1}^{n-1}(n-h)q^h=n\frac{1+q}{1-q}-\frac{2q(1-q^n)}{(1-q)^2},
\]
proves the displayed finite-count variance and, after division by \(n\), the long-run variance. The stationary mean follows directly from \(\kappa(1-q)V_2/2=\kappa Dm\). The divergence is the exact leading term of the long-run variance as \(q\uparrow1\).

**3. Central limit theorem.** Set \(U_j=Y_j^2-V_2\), so \(\mathbb E[U_{j+1}\mid\mathcal F_j]=qU_j\). The differences \(M_{j+1}=U_{j+1}-qU_j\) form a stationary, square-integrable martingale-difference sequence. Summing this identity expresses \(\sum_{j=1}^nU_j\) as \((1-q)^{-1}\sum_{j=2}^nM_j\) plus an \(L^2\)-bounded boundary term. The geometrically contractive stationary chain is ergodic; the martingale central limit theorem applies since fourth innovation moments are finite and conditional variances satisfy the ergodic theorem. Because \(\mathbb EM_j^2=(1-q^2)\operatorname{Var}(Y_0^2)\), the CLT variance is \((\kappa(1-q)/2)^2(1+q)\operatorname{Var}(Y_0^2)/(1-q)\), equal to the displayed result.

**4. Universal weak-reset window.** Let \(\varepsilon=1-q\), \(a=\sqrt{1-\varepsilon}\), and define \(Z_j^{(\varepsilon)}=\sqrt{\varepsilon/(2Dm)}\,Y_j\). In stationary preparation, \(Z_0^{(\varepsilon)}\Rightarrow\mathcal N(0,1)\) by the Lindeberg theorem for the independent triangular moving-average weights; its innovation contributions after time zero are independent of that initial value. The recursion
\[
 Z_{j+1}^{(\varepsilon)}-Z_j^{(\varepsilon)}=(\sqrt{1-\varepsilon}-1)Z_j^{(\varepsilon)}+\sqrt{\varepsilon}\,\zeta_{j+1},
\]
with iid \(\zeta_j=\xi_j/\sqrt{2Dm}\) of mean zero and unit variance, converges by the functional invariance principle and stability of linear recursions to the stated stationary OU process under the time interpolation \(t=j\varepsilon\). Since each work increment equals \(\kappa Dm(Z_j^{(\varepsilon)})^2\), the work ratio is the corresponding Riemann average; the continuous mapping theorem gives the integral-square limit. Stationary OU covariance is \(e^{-|t-s|/2}\); Wick's identity yields \(\operatorname{Cov}(Z_t^2,Z_s^2)=2e^{-|t-s|}\), and double integration gives the displayed variance. The integral is nonnegative with strictly positive variance and is thus not Gaussian. All formulas concern fixed \(\ell>0\) before its optional limiting asymptotics.

## Verification
Run the included standalone program `python verify.py` with NumPy available. It independently generates each free Brownian displacement as \(\sqrt{2DT_j}\,G_j\), with independent \(G_j\sim\mathcal N(0,1)\), rather than sampling from the analytical work covariance law. Six stationary-ensemble parameter checks use exponentially distributed, Erlang-three, and deterministic residence times and compare work means and variances against the exact finite-count formulas. Three weak-reset finite-variance calculations compare \(n(1-a^2)=2\) to the limiting OU variance. All assertions passed. Finite Monte Carlo does not prove a central limit theorem or the continuum limit; those are established by Steps 3--4.

## Relationship to prior work
Olsen and Gupta (2024, arXiv:2401.11919, equations (9), (36)--(42), Figure 2) introduce the proportional-reset endpoint recursion and obtain the \(a\)-independent **mean** work in a quadratic reset trap. Their stationary one-point moments and numerical histograms are prior work; they do not provide an exact work variance or a path-level weak-reset crossover and explicitly identify work fluctuations as future work. Gupta, Plata and Pal (2019, arXiv:1909.08512) establish work-fluctuation theory for complete resetting, where successive reset blocks are independent, unlike the correlated proportional-reset work increments here. Zamparo (2022, arXiv:2207.07521) develops renewal-reward central limit and large-deviation theory for full regeneration; the proportional-reset chain retains memory and its finite-count covariance is not covered by independent renewal rewards. Olsen and Löwen (2024, arXiv:2406.10039) analyze partial-resetting propagators and refractory-period positional moments rather than cumulative harmonic work. Gupta, Olsen and Krishnamurthy (2025, DOI:10.1038/s42005-025-02277-w) analyze independent fully thermalized erasure cycles with timed stiffness protocols, different from exact proportional endpoint contraction. Classical AR(1) covariance and OU invariance principles are standard methods, not claimed as new; the evaluated work-fluctuation/crossover classification is the assessed contribution. An equivalent specialization in less directly indexed renewal or stochastic-thermodynamic literature cannot be excluded without independent priority review.

## Limitations
Finite second moment of exploration times is required for the stated finite work variance and central limit theorem. The theorem fixes the number of *completed resets*, not a laboratory-time horizon; refractory or return-phase durations therefore do not enter the claims. The stationary starting law differs from the initial-at-origin convention often used in transient resetting results. The result gives second cumulants and weak-reset distributional convergence; it does not determine finite-count full work densities or large-deviation functions. The near-weak-reset OU limit does not justify exchanging \(n\to\infty\) and \(a\uparrow1\). Publication priority requires independent confirmation.

## References
1. K. S. Olsen and D. Gupta, *Thermodynamic work of partial resetting*, arXiv:2401.11919 (first public version 2024-01-22), https://arxiv.org/abs/2401.11919.
2. D. Gupta, C. A. Plata and A. Pal, *Work fluctuations and Jarzynski equality in stochastic resetting*, arXiv:1909.08512 (2019), https://arxiv.org/abs/1909.08512.
3. M. Zamparo, *Statistical fluctuations under resetting: rigorous results*, arXiv:2207.07521 (2022), https://arxiv.org/abs/2207.07521.
4. K. S. Olsen and H. Löwen, *Partial stochastic resetting with refractory periods*, arXiv:2406.10039 (2024), https://arxiv.org/abs/2406.10039.
5. D. Gupta, K. S. Olsen and S. Krishnamurthy, *Thermodynamic cost of recurrent erasure*, Communications Physics 8, 355 (2025), https://doi.org/10.1038/s42005-025-02277-w.
