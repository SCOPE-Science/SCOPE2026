# A sharp upper-tail law for derangement occupation in the Ewens restaurant process

## Finding
Let \(\theta>0\). In the Ewens Chinese restaurant growth process, let \(F_j\) be the number of fixed points (singleton cycles) after step \(j\), and put
\[
Q_n=\frac1n\sum_{j=1}^n\mathbf1\{F_j=0\}.
\]
The previously established functional convergence of small-cycle counts implies \(Q_n\Rightarrow Y_\theta\), where
\[
Y_\theta=\int_0^\infty e^{-t}\mathbf1\{X_\theta(t)=0\}\,dt
\]
and \(X_\theta\) is a stationary immigration-death chain with immigration rate \(\theta\) and death rate \(k\) in state \(k\). **This weak limit is background, not the new result.**

For each positive integer \(r\), the limiting occupation variable has the explicit complete moment sequence
\[
\mathbb E[Y_\theta^r]
=e^{-\theta}\prod_{k=1}^{r-1}a_k(\theta),\qquad
 a_k(\theta)=k\int_0^1u^{k-1}e^{-\theta(1-u)}\,du,
\]
where the empty product is one. In particular,
\[
\mathbb E Y_\theta=e^{-\theta},\qquad
\operatorname{Var}(Y_\theta)=e^{-2\theta}\frac{e^{\theta}-1-\theta}{\theta}.
\]
The principal result is a **sharp right-endpoint asymptotic**: define the strictly positive, convergent product
\[
C_\theta=e^{-\theta(1+\gamma)}
\prod_{k=1}^{\infty}\left[a_k(\theta)e^{\theta/k}\right],
\]
where \(\gamma\) is Euler's constant. Then
\[
\boxed{\lim_{\varepsilon\downarrow0}
\frac{\Pr\{Y_\theta>1-\varepsilon\}}{\varepsilon^\theta}
=\frac{C_\theta}{\Gamma(1+\theta)}}.
\]
This identifies both the power-law exponent and an exact nonzero prefactor for unusually high derangement occupation.

## Assumptions and scope
The Ewens seating parameter \(\theta\) is fixed in \((0,\infty)\). At step \(j+1\), a singleton cycle is added with probability \(\theta/(j+\theta)\), and an element is inserted into an existing cycle with probabilities proportional to the cycle sizes. A fixed point means a singleton cycle. The law is for the limit variable \(Y_\theta\), not a uniform-in-\(n\) upper-tail approximation for \(Q_n\). The order of limits is first \(n\to\infty\) and then \(\varepsilon\downarrow0\). The queue is irreducible, positive recurrent and reversible with stationary \(\operatorname{Poisson}(\theta)\) law; its generator satisfies \(q_{k,k+1}=\theta\) and \(q_{k,k-1}=k\) for \(k\ge1\). One has \(0<Y_\theta<1\) almost surely.

## Proof
**1. Occupation limit from known process convergence.** Theorem 6 of Gnedin–Stark, or Proposition 4.2 of Galganov–Ilienko, yields Skorokhod convergence of \(F_{\lfloor nt\rfloor}\) to a stationary \(M/M/\infty\) singleton-count process evaluated at \(\log t\), on each compact \(t\)-interval bounded away from zero. Since a finite-rate continuous-time chain has almost surely finitely many jumps on compact intervals, the indicator of state zero is continuous for time integration with respect to Lebesgue measure at almost every limit path. Thus for each fixed \(\delta>0\),
\[
\frac1n\sum_{\delta n\le j\le n}\mathbf1\{F_j=0\}
\Rightarrow\int_\delta^1\mathbf1\{X_\theta(\log t) =0\}\,dt.
\]
The discarded initial interval is bounded by \(\delta+1/n\); letting \(\delta\downarrow0\) gives the full weak limit. The substitution \(t=e^{-s}\) and stationarity plus detailed-balance reversibility identify the integral with the displayed \(Y_\theta\). Because all \(Q_n\in[0,1]\), convergence also holds for every fixed positive integer moment.

**2. Exact multi-time zero probabilities.** Stationary emptiness has probability \(\pi_0=e^{-\theta}\). Starting empty at time zero, surviving immigrants at time \(s\) form a Poisson variable with mean \(\theta(1-e^{-s})\), so
\[
P_{00}(s)=\Pr\{X_\theta(s)=0\mid X_\theta(0)=0\}=e^{-\theta(1-e^{-s})}.
\]
For ordered times \(0\le t_1\le\cdots\le t_r\), the Markov property gives
\[
\Pr\{X_\theta(t_1)=\cdots=X_\theta(t_r)=0\}
=e^{-\theta}\prod_{i=2}^r P_{00}(t_i-t_{i-1}).
\]
All integrands below are nonnegative, so Tonelli justifies rearrangement. The symmetric expansion of the \(r\)th moment of the time integral gives \(r!\) times the ordered simplex integral. With the gaps \(s_1=t_1\) and \(s_i=t_i-t_{i-1}\) for \(i\ge2\), the exponential time weight is
\(\exp[-r s_1-(r-1)s_2-\cdots-s_r]\). Integrating \(s_1\), and setting \(u=e^{-s}\) in each remaining gap integral, yields
\[
\mathbb EY_\theta^r
=r!e^{-\theta}\frac1r\prod_{k=1}^{r-1}
\int_0^\infty e^{-ks}P_{00}(s)\,ds
=e^{-\theta}\prod_{k=1}^{r-1}
\left[k\int_0^1u^{k-1}e^{-\theta(1-u)}du\right].
\]
The \(r=1,2\) formulas immediately give the mean and variance.

**3. Precise large-moment constant.** If \(U_k\sim\operatorname{Beta}(k,1)\), then \(a_k(\theta)=\mathbb E[e^{-\theta(1-U_k)}]\). Since
\(\mathbb E(1-U_k)=1/(k+1)\) and
\(\mathbb E(1-U_k)^2=2/((k+1)(k+2))\), Taylor's inequality for the exponential proves
\[
a_k(\theta)=1-\frac\theta{k+1}+O_\theta(k^{-2}),\qquad
\log a_k(\theta)+\frac\theta k=O_\theta(k^{-2}).
\]
All factors are positive and the renormalized infinite product converges to a positive finite number. Writing \(H_m=\sum_{k=1}^m1/k\),
\[
r^\theta\mathbb E[Y_\theta^r]
=e^{-\theta}e^{-\theta(H_{r-1}-\log r)}
\prod_{k=1}^{r-1}[a_k(\theta)e^{\theta/k}]
\longrightarrow C_\theta.
\]

**4. Endpoint Tauberian step.** Irreducibility and recurrence ensure that \(Y_\theta>0\) a.s.; stationarity and infinitely many excursions away from zero ensure \(Y_\theta<1\) a.s. Put \(Z_\theta=-\log Y_\theta\ge0\). The last display states that the Laplace–Stieltjes transform obeys
\[
\mathbb E[e^{-rZ_\theta}]\sim C_\theta r^{-\theta}
\qquad(r\to\infty).
\]
The standard one-sided Karamata Tauberian theorem (valid for this nonnegative measure and \(\theta>0\)) therefore gives
\[
\Pr\{Z_\theta\le z\}\sim
\frac{C_\theta}{\Gamma(1+\theta)}z^\theta
\qquad(z\downarrow0).
\]
Substitute \(z=-\log(1-\varepsilon)\sim\varepsilon\). Strict versus weak inequalities at the threshold have the same asymptotic: regular variation of the distribution function implies atoms are negligible relative to \(z^\theta\). This proves the claim.

## Verification
The standalone standard-library Python program `verify.py` was executed on the packaged algorithm and passed 126 assertions. It compares two independently coded exact rational recursions for \(Q_n\) moments through nine steps for three parameters; tests means and variances at increasing finite sizes; independently simulates the stationary immigration-death integral for 14,000 seeded paths per parameter; compares first three moments with the formula; and checks renormalized moment-product stability at truncations 5,000 and 10,000. These experiments are corroborative, not a proof of either convergence or the Tauberian assertion. All infinite-dimensional steps are handled analytically above.

## Relationship to prior work
Gnedin and Stark (2022 preprint, 2023 journal publication) established the Ewens restaurant model, the irregular almost-sure behavior of discrete-time occupation fractions, and the stationary queue process limit. Galganov and Ilienko (2025 preprint, 2026 journal publication) established stronger Poisson-point-measure and functional limits for the singleton process. Those results imply the weak occupation limit and are treated as known. Prior computations of fixed-state occupation covariances also fall within the background. The present statement concerns the **fully evaluated all-order moment product and the sharp near-one endpoint probability with its explicit constant**; it does not relabel the known process limit as new. Standard Karamata theory supplies the Laplace-to-endpoint conversion. No equivalently explicit endpoint formula was located in the inspected primary works, but absence from inspected works is not proof of absolute historical priority.

## Limitations
Only fixed \(\theta>0\) and the zero-fixed-point indicator are treated. No quantitative convergence rate for the finite-size \(Q_n\) law, nor a simultaneous finite-size and endpoint double limit, is proved. The limit distribution's behavior near zero is not determined. The theorem derives a consequence of previously established functional convergence, and prior queueing occupation theory may contain equivalent formulations; historical priority has not been established independently.

## References
1. A. Gnedin and D. Stark, *Random Permutations and Queues*, arXiv:2209.12781v1, first submitted September 26, 2022; *Advances in Applied Mathematics* **149** (2023), 102549, doi:10.1016/j.aam.2023.102549.
2. O. Galganov and A. Ilienko, *Scaling limit for small blocks in the Chinese restaurant process*, arXiv:2502.05578v2; *Stochastic Processes and their Applications* **192** (2026), 104793, doi:10.1016/j.spa.2025.104793.
3. N. H. Bingham, C. M. Goldie and J. L. Teugels, *Regular Variation*, Cambridge University Press, 1987, chapter on Karamata's Tauberian theorem.
