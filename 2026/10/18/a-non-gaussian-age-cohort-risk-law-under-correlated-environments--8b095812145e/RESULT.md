# A non-Gaussian age-cohort risk law under correlated environments

## Finding

An age-structured population can have a uniquely determined, environment-correlation-independent long-run growth exponent while its finite-horizon logarithmic abundance has **non-Gaussian** fluctuations, a positive square-root-time mean correction, and a unique interior environmental switching rate minimizing asymptotic risk. The mechanism is the survival of two disconnected parity cohorts, not randomness in the asymptotic growth exponent.

**Theorem (two-stage semelparous fluctuation law).** Fix arbitrary real sensitivity parameters \(a,b\), positive fecundity scale \(F>0\), survival scale \(0<s\le e^{-|b|}\), and environmental switching probability \(0<p<1\). Let \((E_t)_{t\ge1}\) be a stationary symmetric Markov chain on \(\{-1,+1\}\), initially uniform and switching sign with probability \(p\) at each transition. Let \(X_0=(x_1,x_2)^\top\) with \(x_1,x_2>0\), and evolve by

\[
X_t=A_{E_t}X_{t-1},\qquad A_e=\begin{pmatrix}0&F e^{ae}\\s e^{be}&0\end{pmatrix}.
\]

Define total abundance \(M_t=X_{t,1}+X_{t,2}\), logarithmic abundance \(L_t=\log M_t\), and

\[
\lambda=\tfrac12\log(Fs),\qquad c=\tfrac12(a+b),\qquad d=\tfrac12(a-b).
\]

Then \(L_t/t\to\lambda\) almost surely. For **even** \(N\to\infty\), with \(Z_1,Z_2\) independent standard normal variables,

\[
\frac{L_N-N\lambda}{\sqrt N}\ \Longrightarrow\
 c\sqrt{\frac{1-p}{p}}Z_1+|d|\sqrt{\frac{p}{1-p}}|Z_2|.
\]

The first two moments converge as well:

\[
\lim_{N\to\infty\atop N\text{ even}}\frac{\mathbb E L_N-N\lambda}{\sqrt N}
 =|d|\sqrt{\frac{2p}{\pi(1-p)}},
\]

\[
\lim_{N\to\infty\atop N\text{ even}}\frac{\operatorname{Var}(L_N)}N
 =V(p):=c^2\frac{1-p}{p}+\left(1-\frac2\pi\right)d^2\frac p{1-p}.
\]

The limiting law is Gaussian if and only if \(a=b\); otherwise its third centered moment is strictly positive. If \(a+b\ne0\) and \(a-b\ne0\), the variance coefficient has the **unique global minimizer**

\[
p_*=\frac{|a+b|}{|a+b|+\sqrt{1-2/\pi}\,|a-b|},\qquad
V(p_*)=\frac12|a^2-b^2|\sqrt{1-2/\pi}.
\]

If \(a=b\ne0\), the variance coefficient decreases strictly toward zero as \(p\uparrow1\); if \(a=-b\ne0\), it increases strictly from zero as \(p\downarrow0\); if both are zero it vanishes identically. The boundary probabilities \(p=0,1\) are **not** covered by the limit theorem.

## Assumptions and scope

The projection matrix represents complete reproduction of the adult stage into juveniles and maturation of juveniles into adults, with no same-stage retention. The bound \(s e^{|b|}\le1\) keeps both possible survival probabilities physically admissible. Fecundity may exceed one. Both age stages must initially have positive biomass. Environmental randomness is shared by the two stages and is *temporally* correlated. The switching probability \(p\), not its complement, denotes the probability of changing environment; \(p=1/2\) is independent environmental resampling. Every asymptotic distributional assertion concerns even observation years, avoiding a change of the cohort labels at odd times.

No extinction event or demographic integer sampling is present: this is a random-environment linear population projection. Exponential decline of this deterministic-density state occurs when \(Fs<1\) and exponential growth when \(Fs>1\), for fixed \(0<p<1\). Exactly \(Fs=1\) means zero almost-sure exponential growth, not extinction or positive recurrence.

## Proof

**1. Exact parity decomposition.** Write \(N=2k\), \(S_N=\sum_{t=1}^N E_t\) and \(D_N=\sum_{t=1}^N(-1)^tE_t\), with odd positions having a negative sign. Consecutive two-step projection matrices are diagonal. Multiplying their two diagonal entries gives, without approximation,

\[
X_{N,1}=x_1(Fs)^k \exp(cS_N+dD_N),\qquad
X_{N,2}=x_2(Fs)^k \exp(cS_N-dD_N).
\]

Consequently,

\[
L_N=N\lambda+cS_N+\log\bigl(x_1e^{dD_N}+x_2e^{-dD_N}\bigr).
\tag{1}
\]

Positivity of both initial stages gives a deterministic constant \(C<\infty\) (depending only on them) such that

\[
\left|\log\bigl(x_1e^{dD_N}+x_2e^{-dD_N}\bigr)-|dD_N|\right|\le C.
\tag{2}
\]

Indeed its argument lies between \(\min(x_1,x_2)e^{|dD_N|}\) and \((x_1+x_2)e^{|dD_N|}\). The strong law for the irreducible aperiodic two-state chain gives \(S_N/N\to0\) almost surely. Splitting the same chain into successive pairs gives \(D_N/N\to0\) almost surely. Equation (1) establishes \(L_N/N\to\lambda\) along even years. Since each year's total-abundance multiplier lies between the minimum and maximum of the four strictly positive vital rates, \(|L_{N+1}-L_N|\) is bounded, extending the limit to all integer years.

**2. Joint environmental central limit theorem.** Put \(\rho=1-2p\in(-1,1)\) and \(\xi_t=E_t-\rho E_{t-1}\) for \(t\ge2\). The variables \(\xi_t\) are uniformly bounded martingale differences for the natural Markov filtration. Moreover,

\[
\mathbb E(\xi_t^2\mid E_1,\ldots,E_{t-1})=1-\rho^2.
\]

For even \(N\), exact telescoping yields

\[
(1-\rho)S_N=\sum_{t=2}^N\xi_t+E_1-\rho E_N,
\]

\[
(1+\rho)D_N=\sum_{t=2}^N(-1)^t\xi_t-E_1+\rho E_N.
\]

The normalized vector of the two martingale sums has limiting conditional covariance \((1-\rho^2)I_2\): its cross-covariance contains \(N^{-1}\sum_{t=2}^N(-1)^t\to0\). Boundedness verifies the martingale Lindeberg condition. The two-dimensional martingale central limit theorem therefore proves

\[
(S_N,D_N)/\sqrt N\ \Longrightarrow\
\left(\sqrt{\frac{1+\rho}{1-\rho}}Z_1,\sqrt{\frac{1-\rho}{1+\rho}}Z_2\right),
\tag{3}
\]

with independent normal coordinates. The same result follows from the two-component spectral densities of the stationary Markov chain. By (1)--(3), the continuous-mapping theorem gives the asserted normal-plus-folded-normal limit. The folded term has strictly positive third centered moment whenever \(d\ne0\); adding an independent centered normal does not change that moment.

**3. Moment convergence.** Azuma--Hoeffding bounds for each bounded martingale sum in step 2 imply \(\mathbb E S_N^4+\mathbb E D_N^4=O(N^2)\) (bounded endpoint terms do not affect the order). In view of (1)--(2), the fourth moments of \((L_N-N\lambda)/\sqrt N\) are uniformly bounded. Its first and second moments therefore converge to those of the distribution in step 2. Using \(\mathbb E|Z_2|=\sqrt{2/\pi}\) and \(\operatorname{Var}(|Z_2|)=1-2/\pi\) gives the formulas.

**4. Optimal switching.** Write \(t=p/(1-p)>0\). The variance coefficient becomes \(V=c^2/t+(1-2/\pi)d^2t\). If both \(c\) and \(d\) are nonzero, strict convexity and the arithmetic--geometric-mean inequality give exactly one minimizer \(t_*=|c|/(\sqrt{1-2/\pi}|d|)\), yielding the stated \(p_*\) and \(V(p_*)\). The degenerate cases follow directly from the displayed function.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script compares direct matrix products with (1) for all \(4{,}092\) state sequences across three parameter choices; computes exact rational Markov moments for \(12\) finite cases; tests the unique optimizer numerically; and compares finite-horizon Monte Carlo moments against the analytical limiting values at three switching probabilities. All included tests passed when creating this package. The exact finite tests and simulations independently corroborate algebraic steps, but the infinite limit is proved above by the martingale argument.

A simple numerical example takes \(a=1\), \(b=0\), \(F=2\), \(s=1/2\), and strictly positive initial age stages. Here \(\lambda=0\), and yet the scaled log-population limit is non-Gaussian whenever \(0<p<1\); its asymptotic variance is uniquely minimized at

\[
p_*=(1+\sqrt{1-2/\pi})^{-1}\approx0.6239041611.
\]

At independent environmental resampling \(p=1/2\), this example has \(V(1/2)=(1-1/\pi)/2\approx0.3408450569\), and a strictly positive order-\(\sqrt N\) shift in expected logarithmic population size.

## Relationship to prior work

Sanz (2019) studies stochastic age-structured projection models, bounds for the stochastic growth rate, and a two-stage Leslie family with positive juvenile retention. Sanz and Bravo de la Parra (2020) study growth and *scaled logarithmic variance* and state Gaussian/lognormal limits under eventual positivity of products. The present semelparous matrices have zero diagonal and **no product of any fixed length is strictly positive**: even products remain diagonal and odd products remain off-diagonal. Their primitive-matrix Gaussian theorem therefore does not cover the present setting. The calculation here instead identifies a non-Gaussian distribution, an exact square-root-time log-mean correction, and the interior risk-minimizing environmental correlation.

Unterberger (2021) studies growth-rate variance in continuous-time Markovian phenotype switching with an ergodic population-composition process. His variational and two-state results concern a different, mixing model and do not give this parity-cohort fluctuation law. General Markov martingale central limit theorems are classical proof tools, not original claims. Older theory of semelparous age structure and general random matrix products provides context; possible equivalent formulations in those literatures remain a priority risk.

## Limitations

The law is for a two-stage, zero-retention population projection, a stationary *symmetric* binary environment, fixed \(p\in(0,1)\), and observation at even years. One vanishing initial stage removes the fold mechanism and is excluded. The limits are not uniform as \(p\to0\) or \(p\to1\); those endpoint processes have different spectral structure. The model has no carrying capacity, demographic noise, dispersal, or nonlinear density regulation. The theorem gives asymptotic fluctuation and expectation/variance coefficients, not exact finite-horizon confidence intervals or extinction probabilities. Priority beyond the inspected primary literature is not independently established.

## References

1. L. Sanz, *Conditions for growth and extinction in matrix models with environmental stochasticity*, Ecological Modelling **411** (2019), 108797. DOI: `10.1016/j.ecolmodel.2019.108797`; author's open manuscript: `https://arxiv.org/abs/2402.03827` (2019 article, uploaded there in 2024).
2. L. Sanz and R. Bravo de la Parra, *Stochastic matrix metapopulation models with fast migration: re-scaling survival to the fast scale*, Ecological Modelling **418** (2020), 108829. DOI: `10.1016/j.ecolmodel.2019.108829`; open manuscript: `https://arxiv.org/abs/2402.03888`.
3. J. Unterberger, *Exact computation of growth-rate fluctuations in random environment*, `https://arxiv.org/abs/2111.04167` (2021).
4. S. Tuljapurkar and S. H. Orzack, *Population dynamics in variable environments I: Long-run growth rates and extinction*, Theoretical Population Biology **18** (1980), 314--342.
5. V. Yu. Protasov, *Asymptotics of products of nonnegative random matrices*, Functional Analysis and Its Applications **47** (2013), 138--147; DOI: `10.1007/s10688-013-0018-8`.
