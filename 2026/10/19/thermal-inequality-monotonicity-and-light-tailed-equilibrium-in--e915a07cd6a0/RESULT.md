# Thermal inequality monotonicity and light-tailed equilibrium in a bounded trap-diffusion wealth model

## Finding

Consider a connected cycle of \(L\ge3\) wealth-holding sites, containing a fixed total of \(M\ge2\) distinguishable-for-tracking but economically identical money units. A unit at site \(i\) proposes either neighboring site with probability \(1/2\) and accepts a proposed move to \(j\) with probability
\[
a_{ij}(T)=\min\{1,\exp[(\phi_j-\phi_i)/T]\},\qquad T>0.
\]
Here the site depths \(\phi_i\in[0,1]\) are fixed, and different units move independently. This is the unit-hopping rule of the cited temperature-controlled trap-diffusion model; the theorem concerns its genuine infinite-time equilibrium, not the output after a fixed number of attempted moves.

**Finite-system theorem.** Conditional on the depths, the unique equilibrium wealth-count vector \(X=(X_1,\ldots,X_L)\), with \(\sum_i X_i=M\), has law
\[
X\sim\operatorname{Multinomial}(M;p_1(T),\ldots,p_L(T)),\qquad
p_i(T)=\frac{e^{\phi_i/T}}{\sum_{j=1}^L e^{\phi_j/T}}.
\]
Define the empirical Gini coefficient and vacant-site fraction by
\[
G(X)=\frac1{LM}\sum_{1\le i<j\le L}|X_i-X_j|,
\qquad V(X)=\frac1L\sum_{i=1}^L\mathbf1_{\{X_i=0\}}.
\]
If the depths are not all equal, then **both** \(\mathbb E_T G(X)\) and \(\mathbb E_T V(X)\) are strictly decreasing in \(T\in(0,\infty)\). The conclusion remains valid after averaging over any temperature-independent distribution of nonconstant quenched depths. In particular neither stationary expected observable can possess an interior maximum as a function of temperature. For a unique deepest site, both expectations approach \((L-1)/L\) as \(T\downarrow0\). Their large-temperature limits are the respective expectations for a uniform multinomial distribution and are generally nonzero for finite \(M\).

**Thermodynamic theorem.** Suppose independently sampled depths are uniform on \([0,1]\), while \(L\to\infty\), \(M=M_L\) and \(M_L/L\to m\in(0,\infty)\). At each fixed \(T>0\), for every integer \(k\ge0\), the equilibrium fraction \(H_{L,k}=L^{-1}\#\{i:X_i=k\}\) converges in probability to
\[
q_T(k)=\int_0^1e^{-\lambda_T(u)}\frac{\lambda_T(u)^k}{k!}\,du,
\quad \lambda_T(u)=\frac{m e^{u/T}}{T(e^{1/T}-1)}.
\]
This mixed-Poisson law has a super-exponentially small upper tail. With
\(\Lambda_T=m e^{1/T}/[T(e^{1/T}-1)]\), for integers \(k>\Lambda_T\),
\[
\sum_{j\ge k}q_T(j)\le\left(\frac{e\Lambda_T}{k}\right)^k.
\]
It therefore has **no asymptotic Pareto power-law tail at any fixed positive temperature**. Apparent power laws or intermediate-temperature maxima in finite-run data are not excluded; they cannot be properties of this model's exact equilibrium in the stated regimes.

## Assumptions and scope

There is no creation, destruction, borrowing, saving-propensity exchange, unit-unit interaction, or dependence of a unit's proposal or acceptance on occupancy. The underlying undirected cycle has symmetric nearest-neighbor proposals, and depths are quenched throughout each run. For unequal depths, arbitrarily many attempted steps per tracked unit converge to the same product law as independent continuous-time clocks. Equal depths still have the stated invariant law, but a non-lazy discrete-time walk on an even cycle is periodic; convergence then requires continuous-time clocks, laziness, or aperiodic sampling. Finite-time results may depend on update protocol and the initial configuration. The monotonicity holds for arbitrary deterministic depth vectors, not only uniformly distributed ones. The thermodynamic statement additionally requires bounded independently sampled depths, fixed positive temperature, and finite positive wealth density; the stated explicit mixture uses the uniform depth law.

The statistic \(G\) is computed from an actual random wealth-count vector and then averaged; it is **not** the Gini index of the vector of mean wealths. We use the standard finite-population normalization with denominator \(LM\). The vacancy fraction is averaged analogously. For \(M=1\), both statistics are independent of temperature, which is why \(M\ge2\) is essential for strictness. Equal depths likewise give a temperature-independent equilibrium.

## Proof

**1. Product equilibrium and conservation.** Write \(r_i=e^{\phi_i/T}\). On each cycle edge the two directed proposal rates are both \(1/2\). Consequently
\[
r_i\frac12\min(1,r_j/r_i)=\frac12\min(r_i,r_j)
=r_j\frac12\min(1,r_i/r_j).
\]
The one-unit walk is irreducible and reversible with stationary masses \(p_i=r_i/\sum_jr_j\). For nonconstant depths, rejected proposals at a deepest site make the attempted-move chain aperiodic; continuous-time clocks are aperiodic for all depth vectors. Each unit has a unique stationary law even in the periodic exceptional case. Their independent joint invariant law is consequently the unique product stationary law, whose occupancy counts are multinomial. For the asynchronous count process, the jump \(x\to x-e_i+e_j\) has rate \(x_i a_{ij}/2\). Its detailed-balance identity follows directly from the multinomial factorials and the displayed one-unit balance. This proves both existence and uniqueness without making any mixing-time claim uniform in temperature.

**2. Thermal majorization.** Set \(b=1/T\) and sort depths so \(\phi_1\ge\cdots\ge\phi_L\). Let \(S_k(b)=\sum_{i\le k}p_i(b)\). Differentiation yields
\[
S_k'(b)=S_k(b)(1-S_k(b))\left(\overline\phi_{\le k,b}-\overline\phi_{>k,b}\right)\ge0,
\]
where both displayed averages are weighted by their conditional Gibbs probabilities. For a nonconstant vector of depths at least one inequality is strict for every \(b>0\). Thus the colder probability vector strictly majorizes the hotter one, while both have total mass one.

**3. Vacancy as a strictly Schur-convex statistic.** The exact equilibrium expectation is
\[
\mathbb E_T V=\frac1L\sum_{i=1}^L(1-p_i(T))^M.
\]
For \(M\ge2\), the function \(s\mapsto(1-s)^M\) is strictly convex on \((0,1)\), so the sum is strictly Schur-convex. Applying step 2 gives strict decrease with temperature.

**4. The sampled Gini is also strictly Schur-convex.** Define \(F_M(p)=\mathbb E_p\sum_{i<j}|X_i-X_j|\). Its symmetry is immediate. To prove strict Schur-convexity rather than merely asserting it, hold all probabilities except \(p_a,p_b\) fixed, and fix their sum \(s\). Write \(p_a=sq\), \(p_b=s(1-q)\). Condition on \(R=X_a+X_b\) and all other counts \((Y_j)_{j\ne a,b}\). Their conditional law is independent of \(q\), and \(X_a\mid R\sim\operatorname{Binomial}(R,q)\). The part of the pairwise absolute-difference sum that depends on \(X_a=t\) is
\[
h(t)=|2t-R|+\sum_{j\ne a,b}\left(|t-Y_j|+|R-t-Y_j|\right).
\]
For integer \(0\le t\le R\), this function is convex, symmetric under \(t\leftrightarrow R-t\), and nonaffine whenever \(R\ge2\). The expectation \(B_R(q)=\mathbb E[h(\operatorname{Binomial}(R,q))]\) is a convex polynomial in \(q\), since
\[
B_R''(q)=R(R-1)\sum_{t=0}^{R-2}\binom{R-2}{t}q^t(1-q)^{R-2-t}\,\Delta^2h(t)\ge0.
\]
Moreover \(B_R(q)=B_R(1-q)\). For \(R\ge2\), its second derivative is strictly positive for \(0<q<1\), because the term \(|2t-R|\) has a positive discrete second difference at the midpoint, and every binomial weight there is positive. Thus \(B_R\) increases strictly with \(|q-1/2|\). The event \(R\ge2\) has positive probability for every positive \(p_a,p_b\) when \(M\ge2\). Hence every nontrivial pairwise balancing of probabilities strictly decreases \(F_M\). By successive pairwise balancing (the majorization characterization), \(F_M\) is strictly Schur-convex on the interior probability simplex. Therefore \(\mathbb E_T G=F_M(p(T))/(LM)\) decreases strictly with temperature by step 2. This argument is about the random sampled Gini itself, not a surrogate inequality statistic.

An exact finite formula, useful for independent checking, is obtained by conditioning on each pair's total occupancy. With \(s_{ij}=p_i+p_j\), \(b_{ij}=p_i/s_{ij}\),
\[
\mathbb E_TG=\frac1{LM}\sum_{i<j}\sum_{r=0}^M\binom Mr s_{ij}^r(1-s_{ij})^{M-r}
\sum_{a=0}^r\binom ra b_{ij}^a(1-b_{ij})^{r-a}|2a-r|.
\]
The ordinary continuous extensions apply when a probability tends to zero; finite positive temperatures give strictly positive probabilities.

**5. The large-system occupancy law.** For independent depths \(\phi_i\sim\operatorname{Unif}[0,1]\), the law of large numbers gives
\(L^{-1}\sum_j e^{\phi_j/T}\to c_T=T(e^{1/T}-1)\) almost surely. Conditional on the depths, \(X_i\sim\operatorname{Binomial}(M_L,p_i)\) with \(p_i\le e^{1/T}/L\), and \(M_Lp_i\) is uniformly close to \(m e^{\phi_i/T}/c_T\). At fixed \(k\), the binomial-to-Poisson approximation error is bounded uniformly by \(2M_Lp_i^2=O(L^{-1})\). Averaging these conditional expectations across sites and using the law of large numbers yields the displayed integral \(q_T(k)\).

Conditional on the depths, the final site labels of the \(M_L\) money units are independent. Changing one label changes at most two indicators in \(H_{L,k}\), each by at most \(1/L\). Efron–Stein therefore gives \(\operatorname{Var}(H_{L,k}\mid\phi)\le2M_L/L^2=O(L^{-1})\). This proves convergence in probability of \(H_{L,k}\) to \(q_T(k)\). Since \(\lambda_T(u)\le\Lambda_T<\infty\), the Poisson Chernoff bound applied uniformly in \(u\) proves the asserted super-exponential tail bound and rules out a true Pareto tail.

**6. Endpoint and averaging statements.** If the deepest site is unique, the Gibbs vector tends to a point mass as temperature tends to zero, and all \(M\) units occupy that site in the limit, yielding the two endpoint values. The strict inequalities in steps 3–4 hold for each fixed nonconstant depth vector, and hence remain strict when averaged over any depth ensemble supported on such vectors and independent of temperature.

## Verification

A standalone standard-library program `verify.py` checks exact reversible count-process balance for cycle weights \((1,2,4)\), with \(M=2,4,6\); it also independently enumerates all finite count vectors and compares the exact expected Gini and vacancy values with their pair-binomial formulas. These integer weights correspond to depths \((0,1/2,1)\) at \(T=1/(2\log2)\).

For the three-site, four-unit example the program verifies exactly
\[
\mathbb E G=\frac{134}{343},\qquad \mathbb E V=\frac{286}{1029};
\]
the uniform-probability values are respectively \(26/81\) and \(16/81\). Additional exact pair-balancing checks, temperature-ordering computations on four unequal depths, and a six-thousand-site multinomial sample versus the limiting Poisson-mixture vacancy are included. All checks completed successfully in the provided execution. None of those finite computations is substituted for steps 2–5 of the proof.

Run using `python verify.py` with a standard Python interpreter. No external packages or datasets are required.

## Relationship to prior work

Aydiner's 2026 trap-diffusion study specifies quenched uniform depths, Metropolis neighbor hops, independently propagated money units, and reports temperature-dependent fitted Pareto exponents together with nonmonotonic finite-run vacancy and Gini curves. These definitions motivate the exact-equilibrium question here. The fitted curves and simulations remain observations of the specified finite-time numerical protocol, not pre-existing proofs of the asserted equilibrium properties. The present result separates an exact infinite-time equilibrium and its fixed-temperature thermodynamic limit from such finite-run behavior.

Gibbs reversibility, majorization, binomial Bernstein convexity, and Poisson approximation are established mathematical tools and are not claimed as new. Their combination here yields a model-specific, finite-sample Gini and vacancy monotonicity theorem and an explicit population-level limiting wealth distribution. Aydiner, Cherstvy, Metzler, and Sokolov (2023) study random saving-propensity transactions, in which wealth transferred depends on both counterparties' wealth, unlike independent-unit Metropolis hopping. Liuh (2025) likewise analyzes a different one-unit-transfer mean-field rule. Neither provides the stated theorem for the fixed-depth thermal hopping model. General stationary random-walk results explain the reversible factor but by themselves do not state the sampled-Gini inequalities or the fixed-density mixed-Poisson wealth law.

## Limitations

The theorem concerns the *specified independently hopping money-unit dynamics*. It does not characterize an economic model with position-dependent saving, interacting units, wealth-weighted exchange, debt, external transactions, or dynamic site depths. It is possible for simulations stopped after a finite number of attempts to display apparent power-law fits or nonmonotonic temperature curves, especially where mixing slows sharply as temperature decreases. Such data are not contradicted as finite-time observations. The super-exponential bound requires temperatures bounded away from zero when taking system size to infinity; it is not uniform for temperature sequences approaching zero. The proof gives no general finite-time mixing bound and makes no assertion about empirical household incomes.

## References

1. E. Aydiner, *A New Model for the Income Distribution*, arXiv:2610.08143v1 (first arXiv posting October 6, 2026), Sections III–V, especially the Metropolis rule and the descriptions of vacancy and Gini curves. https://arxiv.org/abs/2610.08143
2. E. Aydiner, A. G. Cherstvy, R. Metzler, and I. M. Sokolov, *Universal Pareto laws in agent-based exchange models: debt and varying initial-money distributions*, European Physical Journal B **96**, 123 (2023), DOI:10.1140/epjb/s10051-023-00579-y, Sections 2–3.
3. J. Liuh, *How Fixed-Amount Transactions and Liquidity Constraints Amplify Wealth Inequality: A Kinetic Model Deviating from the Maximum Entropy Benchmark*, arXiv:2511.08202v1 (2025), for comparison with a different transfer mechanism.
4. V. M. Yakovenko and J. B. Rosser, *Colloquium: Statistical mechanics of money, wealth, and income*, Reviews of Modern Physics **81**, 1703 (2009), arXiv:0905.1518, for general background on kinetic exchange and the distinction between exponential and Pareto tails.
