# Conditional Gumbel decoupling from Gaussian root-gap fluctuations in cyclic ballistic deposition

## Finding

In the homogeneous cyclic ballistic-deposition model of length \(K\), the asymptotic waiting time for the **last root** is independent of the entire centered Gaussian profile of **final root-gap counts**. The stronger quantitative statement is a conditional Gumbel approximation given the arrival history observed at an intermediate time.

Let \(T_j\), \(j\in\mathbb Z/K\mathbb Z\), be independent rate-one exponential first-arrival clocks. The final root set is
\[
\mathcal R_K=\{j:T_j<\min(T_{j-1},T_{j+1})\},
\]
and define \(\tau_K=\max_{j\in\mathcal R_K}T_j\) and \(n_K^*\) as the deposition step when the last root is created. For \(K\ge7\), set
\[
s_K=\frac14\log K,\quad t_{K,x}=\frac{\log(K/3)+x}{3},\quad
\mathcal F_{K,s_K}=\sigma\bigl(\mathbf1\{T_j>s_K\},T_j\mathbf1\{T_j\le s_K\}:j\in\mathbb Z/K\mathbb Z\bigr).
\]
Then for every fixed \(x\in\mathbb R\), as \(K\to\infty\),
\[
\boxed{\mathbb E\left|\mathbb P(\tau_K\le t_{K,x}\mid\mathcal F_{K,s_K})-\exp(-e^{-x})\right|=O_x(K^{-1/8}).}
\]

For integer \(i\ge1\), let \(D_{i,K}\) count cyclic gaps of length \(i+1\) between successive sites in \(\mathcal R_K\). Write \(a_i,b_i>0\) for the exact linear mean and variance constants of Matijasevick (2026), and let \(\mathbf V_K\in\mathbb R^{\mathbb N}\) have \(i\)-th coordinate \((D_{i,K}-a_iK)/\sqrt{b_iK}\) for \(K\ge2i+7\), extended by zero elsewhere. With the limiting centered Gaussian process \(\mathbf G\) whose covariance is \(\operatorname{Cov}(G_i,G_j)=c_{ij}/\sqrt{b_ib_j}\) as in that work, the new joint limit is
\[
\boxed{\left(\mathbf V_K,\frac{3n_K^*}{K}-\log(K/3)\right)\ \Longrightarrow\ (\mathbf G,\Lambda),}
\]
in the product space \(\mathbb R^{\mathbb N}\times\mathbb R\), where \(\Lambda\) has standard Gumbel distribution \(\mathbb P(\Lambda\le x)=\exp(-e^{-x})\) and \(\Lambda\) is independent of the **entire process** \(\mathbf G\). In particular the normalized total root count \((|\mathcal R_K|-K/3)/\sqrt{2K/45}\) converges jointly with the last-root time to independent standard normal and Gumbel limits.

## Assumptions and scope

The deposition strip is a cycle of \(K\) sites with uniform independently chosen deposition sites at successive steps, starting from a flat height profile. Independent rate-one Poisson processes at each site couple the discrete process to the exponential first-arrival clocks; their superposition has rate \(K\). The theorem requires only independent continuous exponential first-arrival clocks, fixed \(x\) for the displayed conditional rate, and fixed gap indices when passing to finite-dimensional distributions. The Gaussian-process marginal limit and its covariance constants are the prior results of Matijasevick (2026). Neither a uniform-in-\(x\) conditional rate nor nonuniform site intensities are claimed.

## Proof

**1. Early information and late-root indicators.** Fix \(x\) and take \(K\) large enough that \(t=t_{K,x}>s=s_K\). Put \(q=e^{-s}=K^{-1/4}\), and define the observable triple-survival indicator
\[
A_j=\mathbf1\{T_{j-1}>s,T_j>s,T_{j+1}>s\},\qquad S=\sum_jA_j.
\]
The unresolved site clocks, conditionally on \(\mathcal F_{K,s}\), have independent rate-one exponential residuals by memorylessness. Let
\[
Y_j=\mathbf1\{T_j>t,\ T_j<T_{j-1},\ T_j<T_{j+1}\},\qquad Z_t=\sum_jY_j.
\]
Exactly the roots counted by \(Z_t\) remain unborn at time \(t\), so \(\{\tau_K\le t\}=\{Z_t=0\}\). If \(A_j=0\), then \(Y_j=0\). If \(A_j=1\), all three sites survive past \(s\), and the conditional chance that the middle one is first among its triple and arrives after \(t\) is
\[
\mathbb P(Y_j=1\mid\mathcal F_{K,s})=A_j\int_{t-s}^\infty e^{-3u}\,du
=A_jp_K,\qquad p_K=\frac{e^{-3(t-s)}}3=e^{-x}K^{-1/4}.
\]
Thus the conditional Poisson parameter is \(\mu_K=p_KS\).

**2. Concentration of the conditional parameter.** Since distinct three-site masks have overlap in two sites at distance one and in one site at distance two, independence beyond distance two gives, for \(K\ge7\),
\[
\mathbb ES=Kq^3=K^{1/4},\qquad
\operatorname{Var}S=K(q^3-q^6)+2K(q^4-q^6)+2K(q^5-q^6)=O(K^{1/4}).
\]
Consequently \(\mathbb E\mu_K=e^{-x}\) and by Cauchy–Schwarz
\[
\mathbb E|\mu_K-e^{-x}|\le p_K\sqrt{\operatorname{Var}S}=O_x(K^{-1/8}).
\]

**3. Conditional Poisson approximation.** Given \(\mathcal F_{K,s}\), the random indicators \(Y_j\) have a dependency graph consisting of edges at cyclic distances one and two, because disjoint underlying three-site residual-clock sets are independent. Adjacent valleys are mutually exclusive. For distance two, both valleys occur among five independent residual clocks with probability \(16/5!=2/15\), conditional on all five sites surviving \(s\), and both central arrivals must exceed \(t\). In particular, without conditioning,
\[
\mathbb E(Y_jY_{j+2})=\frac{2}{15}e^{-5t}.
\]
The standard dependency-neighborhood Chen–Stein bound for the total-variation error against \(\operatorname{Poisson}(\mu_K)\) is bounded by the sum of the two familiar local terms \(b_1+b_2\) (and a harmless universal constant can be included), where
\[
b_1\le5p_K^2S,\qquad
\mathbb Eb_1\le5e^{-2x}K^{-1/4},\qquad
\mathbb Eb_2\le\frac4{15}Ke^{-5t}=O_x(K^{-2/3}).
\]
It follows from the probability-of-zero event and the Lipschitz property of \(u\mapsto e^{-u}\) on the nonnegative reals that
\[
\begin{aligned}
\mathbb E\left|\mathbb P(Z_t=0\mid\mathcal F_{K,s})-e^{-e^{-x}}\right|
&\le C\mathbb E(b_1+b_2)+\mathbb E|\mu_K-e^{-x}|\\
&=O_x(K^{-1/8}),
\end{aligned}
\]
which proves the quantitative conditional assertion. This estimate is stronger than the unconditional Poisson approximation because it persists after all early clocks have been revealed.

**4. Recovering final gaps from the early history.** A root with \(T_j\le s\) is detectable from \(\mathcal F_{K,s}\): the neighbor comparisons are known even if a neighbor has not yet arrived. Write \(\mathcal R_K^{\rm early}=\{j\in\mathcal R_K:T_j\le s\}\) and let \(L_K=|\mathcal R_K\setminus\mathcal R_K^{\rm early}|\). A direct integral gives
\[
\mathbb EL_K=K\mathbb P(T_0>s,\,T_0<T_{-1},T_1)=\frac K3e^{-3s}=\frac13K^{1/4}.
\]
Thus \(L_K/\sqrt K\to0\) in \(L^1\). Whenever at least one early root exists, inserting each later root splits exactly one cyclic gap into two, so any fixed gap-length count changes by at most two. Write \(D_{i,K}^{\rm early}\) for the count formed using only \(\mathcal R_K^{\rm early}\). Then
\[
|D_{i,K}-D_{i,K}^{\rm early}|\le2L_K
\]
on that event. The first arrived site is always a root, hence the probability of **no** early root is at most \(e^{-Ks}\). Therefore the centered/scaled early gap profile has the same fixed-coordinate Gaussian weak limits as the final profile, and its coordinates are all \(\mathcal F_{K,s}\)-measurable. The same approximation holds for the total root count.

**5. Independent joint limit.** For any bounded measurable function \(f\) of finitely many standardized **early** gap counts, conditional expectation and Step 3 show
\[
\left|\mathbb E[f\,\mathbf1\{\tau_K\le t_{K,x}\}]-e^{-e^{-x}}\mathbb Ef\right|
\le\|f\|_\infty\,O_x(K^{-1/8}).
\]
The early-gap approximation in Step 4 and the previously proved Gaussian marginal limit imply joint convergence, with independence, for each finite set of gap indices and all real \(x\). Tightness in the countable product space follows from the already established Gaussian-process marginal tightness, together with the Gumbel marginal. Consequently the joint process limit is the product of the centered Gaussian-process law and Gumbel law.

**6. Returning to deposition-step time.** The superposed Poisson process \(N\) has rate \(K\) and \(n_K^*=N(\tau_K)\). From a union bound \(\mathbb P(\tau_K>\log K)\le Ke^{-3\log K}/3=1/(3K^2)\). Doob's \(L^2\) inequality gives
\[
\mathbb E\sup_{0\le u\le\log K}|N(u)-Ku|^2\le4K\log K.
\]
Hence \((n_K^*-K\tau_K)/K\to0\) in probability, and Slutsky's theorem transfers the joint limit to discrete deposition steps without changing the independence conclusion.

## Verification

The standalone program `verify_joint_roots.py` uses exact rational arithmetic and exhaustive finite enumeration. It checks that 16 of the 120 five-clock rankings produce the two separated local minima; confirms exact means and variances of root counts for every permutation with \(5\le K\le8\); verifies triple-survival covariance formulas on \(K=7,8\) at two rational survival probabilities; and checks the two-unit change bound for inserting a root on cycles of lengths 5 through 7. Execution: `python verify_joint_roots.py`. Observed result: `VERIFY_OK 3191 checks; 5-clock joint-valley probability 2/15`.

These finite calculations check only arithmetic and local combinatorics. The infinite conditional and joint limit statements rely on the analytic argument above and the stated marginal limit theorems; simulations or enumeration are not used as infinite proofs.

## Relationship to prior work

Matijasevick (2026), Theorems A–B, establishes the exact linear moments and Gaussian-process limit for final root gaps; Proposition 7.3 separately gives the **unconditional** Gumbel limit of last-root completion. The proof of Proposition 7.3 includes an unconditional Chen–Stein bound for late roots. Neither a conditional approximation given an expanding early-history sigma-field nor a joint product limit with the Gaussian gap process is among those assertions. The present result supplies the missing decoupling step, using the surviving-triple parameter and an explicit early-history approximation.

Mansour–Rastegar–Roitershtein (2019) develops the deposition model and root statistics, including a root-count Gaussian limit. Dörr–Heiny (2024) studies joint extreme values of inversion and descent *counts across arrays of independent random permutations*, not the last arrival time of a root in a single cyclic deposition process. General Chen–Stein and local-dependence ideas are classical and not claimed as new. The novelty considered here is the specified quantitative conditional result and its joint dynamical consequence. General joint central/extreme limit theorems could potentially subsume it; no assertion of exhaustive priority certification is made.

## Limitations

The conditional-error rate holds for fixed real thresholds, not uniformly over growing threshold windows; the theorem concerns homogeneous arrival rates. Gaussian covariance constants and marginal limit laws are inherited from the cited 2026 work rather than reproved here. No finite-cycle independence, multivariate rate for the Gaussian coordinates, joint growing-gap Poisson regime, or independent external validation is asserted. Comparisons with the literature cannot exclude every broader abstract limit theorem.

## References

1. Mateo Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, arXiv:2610.21094v1, first public 15 October 2026. https://arxiv.org/html/2610.21094v1
2. T. Mansour, R. Rastegar, A. Roitershtein, *On ballistic deposition process on a strip*, arXiv:1903.12548v2 (2019). https://arxiv.org/html/1903.12548v2
3. P. Dörr and J. Heiny, *Joint extremes of inversions and descents of random permutations*, arXiv:2309.17314v2 (2024). https://arxiv.org/html/2309.17314v2
4. R. Arratia, L. Goldstein, L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability 17 (1989), 9–25.
