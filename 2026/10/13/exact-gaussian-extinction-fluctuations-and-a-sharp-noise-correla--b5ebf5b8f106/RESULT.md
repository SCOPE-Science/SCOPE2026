# Exact Gaussian extinction fluctuations and a sharp noise-correlation floor in a stochastic SIRS model
## Finding
For the stochastic SIRS epidemic system specified below, strict subcriticality gives more than a negative upper bound on the infected logarithmic growth rate. There is an exact almost-sure exponent and an explicit normal limit for fluctuations of \(\log I_t\). Brownian correlation changes the second-order extinction uncertainty even though it does not change the first-order epidemic threshold.

Set \(f_0=f(0)\), \(c=\beta/f_0\), \(\alpha=\mu+\gamma+\eta\), and \(\lambda=c\Lambda/\mu-\alpha-b^2/2\). If \(\lambda<0\), then
\[
\lim_{t\to\infty}\frac{\log I_t}{t}=\lambda\quad\text{almost surely},\qquad
\frac{\log I_t-\lambda t}{\sqrt t}\Longrightarrow\mathcal N(0,v_\rho),
\]
where, with \(m=\Lambda/\mu\), \(q=2\Lambda^2/[\mu(2\mu-a^2)]\), and \(k=ca/\mu\),
\[
v_\rho=k^2q+b^2+2kb\rho_{12}m.
\]
The variance obeys the sharp correlation-floor identity
\[
\min_{-1\le\rho_{12}\le1}v_\rho=k^2(q-m^2)+(b-km)^2.
\]
If \(a>0\), then \(q-m^2=\Lambda^2 a^2/[\mu^2(2\mu-a^2)]>0\), so no admissible correlation can eliminate logarithmic extinction fluctuations.

## Assumptions and scope
Let \(\Lambda,\mu,\beta,\gamma,\delta,\eta\) be strictly positive, and let \(f:[0,\infty)\to(0,\infty)\) be nondecreasing and locally Lipschitz, with \(f_0>0\). The source's stronger monotonicity and unimodal-per-capita-incidence assumptions are permitted. Let \(B_1,B_2,B_3\) be correlated standard Brownian motions with constant positive-semidefinite correlation matrix \((\rho_{ij})_{1\le i,j\le3}\), diagonal entries one. Choose \(a,b,d\ge0\) such that \(Q=\max(a^2,b^2,d^2)<2\mu\). For any deterministic \((S_0,I_0,R_0)\in(0,\infty)^3\), consider the unique positive Itô solution
\[
\begin{aligned}
dS_t&=\bigl(\Lambda-\mu S_t-\beta S_t I_t/f(I_t)+\delta R_t\bigr)\,dt-aS_t\,dB_{1t},\\
dI_t&=\bigl(\beta S_t I_t/f(I_t)-\alpha I_t\bigr)\,dt-bI_t\,dB_{2t},\\
dR_t&=\bigl(\gamma I_t-(\mu+\delta)R_t\bigr)\,dt-d\,R_t\,dB_{3t}.
\end{aligned}
\]
The noise amplitudes correspond to the source's common environmental scale multiplied by its class-specific sensitivities; \(\eta\) denotes the infection-related mortality rate and \(d\) the recovered-noise magnitude. This theorem assumes **strict** \(\lambda<0\), equivalently the source's stochastic reproduction threshold below one; it makes no statement at the critical equality.

## Proof
**1. Global bounds and an independent extinction estimate.** Put \(N_t=S_t+I_t+R_t\). Its drift is \(\Lambda-\mu N_t-\eta I_t\). Correlation positivity and \(S,I,R\ge0\) imply that the quadratic variation density of its martingale part is at most \((aS_t+bI_t+dR_t)^2\le QN_t^2\). Thus Itô's formula, \(2\Lambda N\le(2\mu-Q)N^2/2+C\), and Grönwall give \(\sup_{t\ge0}\mathbb E N_t^2<\infty\). Positivity follows from the multiplicative infection diffusion and inward susceptible/recovered boundary drifts; these bounds preclude explosion. Standard one-unit-interval Burkholder–Davis–Gundy estimates now give \(\sup_{n\ge0}\mathbb E\sup_{n\le t\le n+1}N_t^2<\infty\), and Borel–Cantelli yields \(N_t/t\to0\) almost surely. For each component stochastic integral, the uniform second-moment bound and dyadic martingale maximal inequality yield its ratio to \(t\) tending to zero almost surely.

Integrate the equations for \(S+I\) and \(R\), divide by \(t\), and eliminate the time average of \(R\). Writing \(\langle Y\rangle_t=t^{-1}\int_0^tY_s\,ds\), the above boundary and martingale estimates give
\[
\langle S\rangle_t=\frac\Lambda\mu-\left(1+\frac\eta\mu+\frac\gamma{\mu+\delta}\right)\langle I\rangle_t+o(1)\le\frac\Lambda\mu+o(1)
\]
almost surely. Since \(f(I)\ge f_0\), Itô's identity
\[
\log I_t=\log I_0+\int_0^t\left(\frac{\beta S_s}{f(I_s)}-\alpha-\frac{b^2}{2}\right)ds-bB_{2t}
\]
shows \(\limsup_{t\to\infty}t^{-1}\log I_t\le\lambda<0\). Hence for every sufficiently small \(\kappa>0\), eventually \(0<I_t\le e^{-\kappa t}\) almost surely.

**2. Exponential coupling to the disease-free susceptible diffusion.** The recovered component has the exact positive variation-of-constants representation
\[
R_t=e^{-(\mu+\delta+d^2/2)t-d\,B_{3t}}
\left(R_0+\gamma\int_0^te^{(\mu+\delta+d^2/2)s+d\,B_{3s}}I_s\,ds\right).
\]
As \(B_{3t}/t\to0\) almost surely and \(I_t\) decays exponentially, \(R_t\) does too, possibly with a smaller decay exponent.

On the same Brownian path \(B_1\), let \(X_0=S_0\) and
\[
dX_t=(\Lambda-\mu X_t)dt-aX_t\,dB_{1t}.
\]
Then \(D_t=S_t-X_t\) solves \(dD_t=(-\mu D_t+F_t)dt-aD_t\,dB_{1t}\), where \(F_t=\delta R_t-\beta S_tI_t/f(I_t)\) and \(D_0=0\). Since \(S_t\le N_t=o(t)\) almost surely and \(R,I\) decay exponentially, \(F_t\) decays exponentially. The explicit linear stochastic variation-of-constants formula, together with \(B_{1t}=o(t)\), implies \(D_t\) decays exponentially. Local Lipschitz continuity at zero gives \(|f(I_t)^{-1}-f_0^{-1}|\le C I_t\) eventually. Therefore the full nonlinear incidence error is integrable:
\[
\int_0^\infty\left|\frac{\beta S_t}{f(I_t)}-cX_t\right|dt<\infty\quad\text{almost surely}.
\]

**3. Disease-free moments.** If \(a>0\), the one-dimensional diffusion \(X\) has the classical inverse-gamma invariant density with shape \(1+2\mu/a^2\) and scale \(2\Lambda/a^2\). The inequality \(a^2<2\mu\) ensures a finite second moment. Its ergodic theorem, or the moment relations obtained from the diffusion generator, yields
\[
\frac1t\int_0^t X_s\,ds\to m=\frac\Lambda\mu,\qquad
\frac1t\int_0^t X_s^2\,ds\to q=\frac{2\Lambda^2}{\mu(2\mu-a^2)}
\]
almost surely. If \(a=0\), \(X_t\) is a deterministic exponentially relaxing affine flow and the same expressions hold with \(q=m^2\). The elementary second-moment estimate also gives \(X_t/\sqrt t\to0\) in probability.

**4. Exact fluctuation decomposition and martingale limit.** Integrating the affine equation for \(X\) gives
\[
c\int_0^tX_s\,ds=\frac{c\Lambda}{\mu}t-\frac c\mu(X_t-X_0)-k\int_0^tX_s\,dB_{1s},\qquad k=\frac{ca}{\mu}.
\]
Substitution into the logarithmic infection identity yields the **exact** decomposition
\[
\begin{split}
\log I_t-\lambda t={}&\log I_0-\frac c\mu(X_t-X_0)-k\int_0^tX_s\,dB_{1s}-bB_{2t}\\
&+\int_0^t\left(\frac{\beta S_s}{f(I_s)}-cX_s\right)ds.
\end{split}
\]
The last term converges almost surely to a finite limit. For the continuous martingale \(M_t=-k\int_0^tX_s\,dB_{1s}-bB_{2t}\), the exact quadratic variation is
\[
\langle M\rangle_t=k^2\int_0^tX_s^2ds+b^2t+2kb\rho_{12}\int_0^tX_sds,
\]
and its ratio to \(t\) converges almost surely to \(v_\rho\). The continuous-martingale central limit theorem (or Brownian time change) gives \(M_t/\sqrt t\Longrightarrow\mathcal N(0,v_\rho)\), including the degenerate zero-variance case. The other terms vanish on this scale, proving the asserted CLT. Dividing by \(t\) instead proves the exact almost-sure exponent (the martingale strong law follows from the moment estimate and its quadratic variation).

Finally \(|\rho_{12}|\le1\) and \(k,b,m\ge0\) imply the variance is minimized at \(\rho_{12}=-1\); then \(k^2q+b^2-2kb m=k^2(q-m^2)+(b-km)^2\). This is sharp because the two Brownian motions may be exact negatives of one another; \(B_3\) can be taken independent of both. When \(a>0\), \(q-m^2>0\) and \(k>0\), giving a strictly positive lower floor.

## Verification
The included `verify.py` checks the exact moment and variance identities symbolically, positivity of the algebraic variance floor under the theorem's assumptions, and a rational example. For \(\Lambda=\mu=\beta=2\), \(\gamma=\delta=\eta=1\), \(f(I)=1+I^2\), and \((a,b,d)=(1,1/2,1/2)\), the parameters satisfy \(Q=1<4=2\mu\), \(\lambda=-17/8\), and
\[
v_\rho=\frac{19}{12}+\rho_{12},\quad v_{-1}=\frac7{12},\quad v_0=\frac{19}{12},\quad v_{1}=\frac{31}{12}.
\]
The example's incidence function has increasing values and a single maximum of the ratio \(I/f(I)\), satisfying the paper's original incidence shape assumptions. The computational checks support the explicit algebra; they do not replace the infinite-time stochastic arguments above.

## Relationship to prior work
Huang, Du, and Liang (2026) establish a stochastic extinction threshold and an upper bound on the long-time rate \(\log I_t/t\); their Gaussian approximation describes stationary fluctuations near a *positive endemic equilibrium*. Their Remark 3.2 notes threshold invariance under Brownian correlation. Neither statement supplies a Gaussian limit for the *extinct trajectory's logarithmic infection* or the correlation-dependent variance above. Here the exact rate equality, asymptotic distribution, and sharp correlation floor are asserted for that distinct regime. Classical inverse-gamma diffusion moments and the continuous-martingale CLT are tools, not novelty claims.

Zhao, Jiang, Mao, and Gray (2015) treat a different stochastic SIRS varying-population model, giving disease threshold, extinction of infected proportion, and persistence criteria rather than this trajectory-level logarithmic fluctuation law. Zotsa-Ngoufack (2023) derives **large-population** epidemic functional CLTs with varying infectivity; their limit sends population size to infinity rather than time to infinity in a fixed environmental-noise SDE. Chen, Liu, and Jing (2026) study quasi-stationary extinction *times* in a network continuous-time Markov chain, not Gaussian fluctuations of a positive real-valued infected SDE tending to zero. The comparison does not assert that no unindexed or subsequently posted work could contain an equivalent theorem.

## Limitations
Strict extinction \(\lambda<0\) and \(\max(a^2,b^2,d^2)<2\mu\) are essential to the given proof. Critical parameters, infinite-variance susceptible stationary laws, finite-population absorption, and first-passage-time limit laws are not established. The limit is convergence in distribution of the normalized logarithmic infection at deterministic large times, not a sample-path Gaussian approximation or a finite-time confidence interval. The variance only depends on the correlation of the susceptible and infected Brownian drivers; the recovered driver affects transient terms. Published-literature indexing is incomplete, so originality remains subject to later independent audit.

## References
1. J. Huang, J. Du, H. Liang, “Dynamics and stochastic sensitivity technique of a stochastic SIRS epidemic model,” *AIMS Mathematics* **11** (2026), 6720–6743, DOI: 10.3934/math.2026278. First publicly dated 16 March 2026. https://www.aimspress.com/aimspress-data/math/2026/3/PDF/math-11-03-278.pdf
2. Y. Zhao, D. Jiang, X. Mao, A. Gray, “The threshold of a stochastic SIRS epidemic model in a population with varying size,” *Discrete and Continuous Dynamical Systems B* **20** (2015), 1277–1295, DOI: 10.3934/dcdsb.2015.20.1277. https://strathprints.strath.ac.uk/50878/
3. P. Zotsa-Ngoufack, “Functional Central Limit Theorems for Epidemic Models with Varying Infectivity and Waning Immunity,” arXiv:2311.02260 (2023). https://arxiv.org/abs/2311.02260
4. T. Chen, G. Liu, X. Jing, “Quasi-stationary distribution and time to extinction for stochastic SIRS models on networks,” *Advances in Continuous and Discrete Models* **2026**, 33 (2026), DOI: 10.1186/s13662-026-04076-1. https://link.springer.com/article/10.1186/s13662-026-04076-1
