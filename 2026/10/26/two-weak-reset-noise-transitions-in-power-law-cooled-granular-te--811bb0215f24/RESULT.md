# Two weak-reset noise transitions in power-law-cooled granular temperatures

## Finding

A Poisson-reset macroscopic temperature with a power-law Haff-type cooling profile has an exact, positive two-time covariance, a regenerative central limit theorem for its time integral, and **two distinct weak-reset thresholds**. The one-time temperature fluctuations vanish as resetting becomes rare at every positive cooling exponent, whereas the variance per unit time of its long-time integrated temperature *diverges* exactly when the exponent is below one half. The normalized correlation time diverges for cooling exponents at most one, but tends to a positive finite limit above one.

Fix an arbitrary temperature scale \(T_*>0\), cooling time \(\tau>0\), cooling exponent \(\alpha>0\), and resetting rate \(r>0\). Let \(A_t\) be the stationary backward recurrence time (age) of a two-sided rate-\(r\) Poisson process; write
\[
T_t=f(A_t),\qquad f(a)=T_*(1+a/\tau)^{-\alpha},\qquad \rho=r\tau.
\]
Set \(m_r=\mathbb E T_t\), \(C_r(t)=\operatorname{Cov}(T_0,T_t)\), \(\sigma_r^2=\lim_{H\to\infty} H^{-1}\operatorname{Var}(\int_0^H T_t\,dt)\), and \(\Theta_r=(\int_0^\infty C_r(t)\,dt)/C_r(0)\). Let \(L\sim\operatorname{Exp}(r)\) be a complete inter-reset duration, independent of the stationary age \(A\sim\operatorname{Exp}(r)\), and let \(F(\ell)=\int_0^\ell f(a)\,da\).

For every \(t\geq0\),
\[
C_r(t)=e^{-rt}\operatorname{Cov}(f(A),f(A+t))>0,\qquad
\sigma_r^2=2\int_0^\infty C_r(t)\,dt
=r\,\mathbb E[(F(L)-m_r L)^2]>0.
\]
The strict inequality holds even at \(t=0\). Furthermore,
\[
\frac{\int_0^H (T_t-m_r)\,dt}{\sqrt H}
\ \xrightarrow[H\to\infty]{\mathrm d}\ \mathcal N(0,\sigma_r^2).
\]

Define the positive constants, for \(0<\alpha<1\),
\[
B_\alpha=\frac{\Gamma(3-2\alpha)}{(1-\alpha)^2}-2(1-\alpha)\Gamma(1-\alpha)^2,
\]
and for \(0<\alpha<1/2\), \(V_\alpha=\Gamma(1-2\alpha)-\Gamma(1-\alpha)^2\). As \(\rho\downarrow0\), with \(T_*\), \(\tau\), and \(\alpha\) fixed, the integrated-temperature variance has the three sharp equivalent forms
\[
\frac{\sigma_r^2}{T_*^2\tau}\sim
\begin{cases}
B_\alpha\rho^{2\alpha-1},&0<\alpha<1,\\
\rho\log^2(1/\rho),&\alpha=1,\\
\rho/(\alpha-1)^2,&\alpha>1.
\end{cases}
\]
Its normalized correlation time has five distinct equivalent forms:
\[
\Theta_r\sim
\begin{cases}
B_\alpha/(2V_\alpha r),&0<\alpha<1/2,\\
(4-\pi)/(2r\log(1/\rho)),&\alpha=1/2,\\
\tau(2\alpha-1)B_\alpha\rho^{2\alpha-2}/2,&1/2<\alpha<1,\\
\tau\log^2(1/\rho)/2,&\alpha=1,\\
\tau(2\alpha-1)/(2(\alpha-1)^2),&\alpha>1.
\end{cases}
\]
In particular, at the Haff cooling exponent \(\alpha=2\), \(\Theta_r\to3\tau/2\); at the viscoelastic example \(\alpha=5/3\), \(\Theta_r\to21\tau/8\). At the borderline \(\alpha=1/2\), \(\sigma_r^2\to T_*^2\tau(4-\pi)\). For \(0<\alpha<1/2\), the long-time variance rate diverges as \(r\downarrow0\) even while the stationary temperature variance tends to zero.

## Assumptions and scope

All four parameters \(T_*\), \(\tau\), \(\alpha\), and \(r\) are strictly positive. Every reset deterministically restores the temperature to \(T_*\); between resets cooling follows the stated power law without additional stochastic forcing. The Poisson clock is independent of the deterministic cooling. We consider its unique stationary renewal-age realization and two-sided time covariance. No finite-particle thermal fluctuations, stochastic intercollision times, or velocity distribution evolution are included. For each fixed \(r>0\), first send the observation horizon \(H\to\infty\) to define \(\sigma_r^2\) and its CLT; only afterwards send \(\rho\downarrow0\) to obtain the displayed limits. The theorem does not assert a joint \(H,r\) limit.

## Proof

**Covariance and positivity.** Because the Poisson clock is memoryless, \(A\sim\operatorname{Exp}(r)\) at a stationary observation. If there is no reset in \((0,t]\), an event of probability \(e^{-rt}\) independent of \(A\), the later temperature equals \(f(A+t)\). Otherwise, its age (and hence its temperature) depends only on the resets after time zero and is independent of \(A\). Subtracting the product of means gives the exact formula for \(C_r(t)\). Both \(f(a)\) and \(f(a+t)\) are strictly decreasing in \(a\); for an independent \(A'\), twice the covariance equals \(\mathbb E[(f(A)-f(A'))(f(A+t)-f(A'+t))]>0\), proving strict positivity. Since \(|T_t|\le T_*\), \(|C_r(t)|\le4T_*^2e^{-rt}\), ensuring integrability.

**Time-integrated variance and CLT.** Successive independent exponential inter-reset intervals \(L_j\) define renewal cycles whose total temperature rewards are \(F(L_j)\). The mean reward rate is \(m_r=\mathbb E F(L)/\mathbb E L=r\mathbb E F(L)\). Centered cycle rewards \(Z_j=F(L_j)-m_rL_j\) are iid, centered, and have finite moments of every order because \(|Z_j|\le2T_*L_j\). The renewal-reward central limit theorem (or an iid random-sum CLT with a negligible incomplete cycle) gives \(\sigma_r^2=\mathbb E Z_j^2/\mathbb E L=r\mathbb E Z_j^2\). The stationary covariance bound permits dominated convergence in
\(H^{-1}\operatorname{Var}(\int_0^H T_t\,dt)=2\int_0^H(1-t/H)C_r(t)\,dt\), giving the independent Green–Kubo expression. Strict covariance positivity implies \(\sigma_r^2>0\).

**Weak-reset cumulative-noise asymptotics.** Set \(U=rL\sim\operatorname{Exp}(1)\). Write \(m_r=T_*q_\rho\), where \(q_\rho=\mathbb E[(1+U/\rho)^{-\alpha}]\). Let \(\Phi_\alpha(x)=((1+x)^{1-\alpha}-1)/(1-\alpha)\) for \(\alpha\ne1\), and \(\Phi_1(x)=\log(1+x)\). Direct integration yields
\[
\frac{\sigma_r^2}{T_*^2\tau}
=\rho\,\mathbb E\left[\Phi_\alpha(U/\rho)-q_\rho U/\rho\right]^2.
\]
For \(0<\alpha<1\), dominated convergence in \(L^2\) gives \(\rho^{1-\alpha}\Phi_\alpha(U/\rho)\to U^{1-\alpha}/(1-\alpha)\) and \(\rho^{-\alpha}q_\rho\to\Gamma(1-\alpha)\); taking the second moment yields \(B_\alpha\). In particular, \(B_\alpha\) is the strictly positive variance-type expectation \(\mathbb E[(U^{1-\alpha}/(1-\alpha)-\Gamma(1-\alpha)U)^2]\). At \(\alpha=1\), \(\Phi_1(U/\rho)/\log(1/\rho)\to1\) in \(L^2\) and \(q_\rho/[\rho\log(1/\rho)]\to1\); the normalized bracket converges to \(1-U\), whose second moment equals one. At \(\alpha>1\), \(\Phi_\alpha(U/\rho)\to1/(\alpha-1)\) in \(L^2\) and \(q_\rho/\rho\to1/(\alpha-1)\), so the bracket converges to \((1-U)/(\alpha-1)\), with mean square \(1/(\alpha-1)^2\). Exponential tails of \(U\), boundedness of \(\Phi_\alpha\) for \(\alpha>1\), and elementary polynomial/logarithmic majorants justify the stated dominated-convergence steps.

**Weak-reset point variance and correlation-time transitions.** Elementary changes of variables in the two stationary moments yield
\[
\frac{\operatorname{Var}(f(A))}{T_*^2}\sim
\begin{cases}
V_\alpha\rho^{2\alpha},&0<\alpha<1/2,\\
\rho\log(1/\rho),&\alpha=1/2,\\
\rho/(2\alpha-1),&\alpha>1/2.
\end{cases}
\]
The first line has \(V_\alpha>0\) by strict variance of \(U^{-\alpha}\). The second follows from the logarithmic divergence of the integral of \((1+y)^{-1}\). In the third, \(\mathbb E f(A)^2/T_*^2\sim\rho/(2\alpha-1)\) and \((\mathbb E f(A)/T_*)^2=o(\rho)\). Dividing half the integrated variance rate by these three static-variance regimes proves all five formulas for \(\Theta_r\). Substitution of \(\alpha=1/2,2,5/3\) gives the stated special values.

## Verification

The self-contained `verify.py` independently evaluates \(\mathbb E[(F(L)-m_rL)^2]\) and numerically integrates the separately obtained two-time covariance for seven combinations of cooling exponent and resetting rate. For each, the two evaluations of \(\sigma_r^2\) agree to well within an absolute tolerance of \(2\times10^{-8}\); positive covariance was checked at lag \(0\) and lag \(0.4\). Two additional small-reset calculations check the scale of the asymptotic expressions for exponents \(1/4\) and \(2\). The script also checks \(B_{1/2}=4-\pi\). Run `python verify.py` with Python 3 and SciPy. Numerical tests are finite and do not replace the proofs of the limits or CLT.

## Relationship to prior work

Bodrova, Chechkin, and Dubey (arXiv:2403.18974, originally publicly released 2024-03-27) analyze a granular gas under resetting and derive the stationary temperature distributions and one-time moments for power-law cooling. Those results, including Haff cooling, are prior work; we do not claim them. Evans, Majumdar, and Schehr (arXiv:1910.07993) present broad two-time stochastic-reset identities. Renewal-reward CLTs and Green–Kubo formulas are standard. The proposed contribution is specifically the evaluated temperature two-time covariance and the two distinct reset-rate singularity thresholds, including the five-regime normalized-correlation-time classification and the vanishing point variance/divergent integrated variance contrast. A more general published renewal functional theorem might imply some or all of these specialized consequences; priority has not been independently certified.

## Limitations

The stationary temperature is a deterministic age functional; fluctuations of the actual finite-particle granular temperature and departures from the exact power-law cooling model are not described. The weak-reset results are sequential limits, not a uniform time-and-rate limit. The exact formulas require memoryless resets. No claim is made about experimental noise, age-dependent rates, or the complete power spectrum at nonzero frequency. Novelty is assessed against the inspected sources and searched research records, not proved uniquely against all publications. Independent scientific validation has not been performed.

## References

1. A. Bodrova, A. Chechkin, A. K. Dubey, *Granular gases under resetting*, arXiv:2403.18974 (first public version 2024-03-27), https://arxiv.org/abs/2403.18974.
2. M. R. Evans, S. N. Majumdar, G. Schehr, *Stochastic Resetting and Applications*, arXiv:1910.07993 (review; general two-time reset identities), https://arxiv.org/abs/1910.07993.
3. P. W. Glynn, W. Whitt, *Limit theorems for cumulative processes*, Stochastic Processes and their Applications 47 (1993), 299–314 (regenerative limit theorem).
