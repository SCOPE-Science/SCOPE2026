# A sharp Cesàro-bias criterion for quenched orthogonality of randomly signed bootstrap walks

## Finding
Let \(\xi_1,\xi_2,\ldots\) be independent symmetric signs. Independently, let \(\varepsilon_k\in\{-1,1\}\) be independent, not necessarily identically distributed, with \(m_k=\mathbb E\varepsilon_k\in[-1,1]\). For **each fixed family** of predictable sign maps \(h_k:\{-1,1\}^{k-1}\to\{-1,1\}\), define
\[
 X_n=\sum_{k=1}^n\xi_k,\qquad
 Y_n=\sum_{k=1}^n\varepsilon_k h_k(\xi_1,\ldots,\xi_{k-1})\xi_k.
\]
Then the following assertions are equivalent:

1. \(n^{-1}\sum_{k=1}^n|m_k|\longrightarrow0\).
2. For **every fixed predictable sign family** \((h_k)\), for almost every sign environment \((\varepsilon_k)\), the conditional laws given that environment satisfy
\[
 \bigl(n^{-1/2}X_{\lfloor nt\rfloor},n^{-1/2}Y_{\lfloor nt\rfloor}\bigr)_{0\le t\le1}
 \Longrightarrow (B_t^{(1)},B_t^{(2)})_{0\le t\le1}
\]
in \(D([0,1],\mathbb R^2)\), where the two standard Brownian coordinates are independent.

The quantifiers in assertion 2 are **\(\forall h\;\mathbb P_\varepsilon\text{-a.e.}\)**, not \(\mathbb P_\varepsilon\text{-a.e.}\;\forall h\). In particular, no common full-measure set of environments works for every predictable family.

More quantitatively, write \(a_n=n^{-1}\sum_{k=1}^n|m_k|\) and \(Q_j=\sum_{k=1}^j\varepsilon_k h_k(\xi_1,\ldots,\xi_{k-1})\). For every \(n\ge1\), every \(\delta>0\), and every such family,
\[
 \mathbb P_{\varepsilon,\xi}\left\{\max_{0\le j\le n}|Q_j|>n(a_n+\delta)\right\}
 \le 2\exp(-n\delta^2/2).
\]
The criterion is sharp for the entire class of predictable transformations. It also yields a restricted positive quenched conclusion in the inclusion-induced one-factor construction of Hamza--Tournier (2026): if the independent empty-subset coefficient at every time is a fair bit, the bivariate walk has independent Brownian coordinates almost surely conditionally on the coefficients, regardless of the distributions of the other independent level coefficients.

## Assumptions and scope
The signs \(\varepsilon_k\) are independent of one another and of the entire input walk. Each \(h_k\) is deterministic, takes only values \(\pm1\), and observes the past \(\xi_1,\ldots,\xi_{k-1}\) but not \(\xi_k\). The necessity and sufficiency are uniform **in the choice of fixed family** but do not identify a shared null set over uncountably many families. An auxiliary random family independent of the masking signs and the input walk is also allowed after conditioning on that auxiliary randomness, with an almost-everywhere statement for the joint auxiliary and masking environments.

The first public source motivating the question is arXiv:2610.01658, submitted 2026-10-01; its one-factor construction is explicitly described by independent coefficient blocks indexed by time and subset size. The statement here is for a broader external-mask model, not for all parameter choices in that construction.

## Proof
**Centered-mask strong law.** Fix an input sign path \(\xi\) and one predictable family \(h\). The random variables
\[
 Z_k=(\varepsilon_k-m_k)h_k(\xi_1,\ldots,\xi_{k-1})
\]
are independent, centered, and have variances at most one under the masking-sign law. The Kolmogorov strong law for independent non-identically distributed variables applies because \(\sum_{k\ge1}\operatorname{Var}(Z_k)/k^2\le\sum_{k\ge1}k^{-2}<\infty\). Therefore, for every fixed input path, \(n^{-1}\sum_{k=1}^n Z_k\to0\) with masking probability one. Fubini yields the same convergence almost surely under the joint law, and hence, for almost every fixed environment, almost surely under the input-walk law.

**Uniform brackets.** For any real sequence whose Cesàro averages tend to zero, its maximum absolute prefix sum through \(n\), divided by \(n\), tends to zero. Consequently, under assertion 1,
\[
 \frac1n\max_{j\le n}|Q_j|\le\frac1n\max_{j\le n}\left|\sum_{k=1}^j Z_k\right|+a_n\longrightarrow0
\]
for almost every masking environment and almost every input walk.

**Quenched functional convergence.** Fix one of these environments. Relative to the input-walk filtration, the bivariate walk \((X_j,Y_j)\) is a martingale with increments \((\xi_k,\varepsilon_k h_k(\xi_{<k})\xi_k)\). The conditional variance of each component's step equals one; its conditional cross covariance equals \(\varepsilon_k h_k(\xi_{<k})\). Thus the predictable quadratic variation matrix of the diffusively rescaled martingale converges uniformly on \([0,1]\), in input-walk probability, to \(tI_2\). Each scaled step has Euclidean norm \(\sqrt{2/n}\), giving the Lindeberg condition. The standard vector martingale functional central limit theorem proves assertion 2.

**Necessity.** If assertion 1 fails, fix the deterministic rule \(h_k\equiv\operatorname{sgn}(m_k)\), using \(\operatorname{sgn}(0)=1\). The independent centered strong law gives, for almost every environment,
\[
 \frac1n\sum_{k=1}^n\varepsilon_k\operatorname{sgn}(m_k)
 -\frac1n\sum_{k=1}^n|m_k|\longrightarrow0.
\]
For this rule and every fixed environment, the covariance of the terminal pair, normalized by \(n\), is exactly the first displayed sum. Both normalized terminal walks are symmetric simple random walks individually, and their fourth moments are bounded uniformly in \(n\). Hence their normalized products are uniformly integrable. Convergence in law to independent standard Gaussians would force the cross covariance to tend to zero, contradicting a positive subsequential limit of the nonnegative bias averages. Thus assertion 2 fails for this specific fixed rule.

**Finite-horizon bound and quantifier boundary.** Conditional on the input signs, the centered variables \(Z_k\) are independent, lie in intervals of width two, and admit the exponential moment bound \(\mathbb E\exp(\theta Z_k)\le\exp(\theta^2/2)\). The exponential maximal inequality applied to positive and negative partial sums, followed by \(\theta=\delta\), gives the stated \(2e^{-n\delta^2/2}\) bound. Finally, for any particular realized environment, the deterministic family \(h_k\equiv\varepsilon_k\) gives \(Y_n=X_n\); this family is not independent of the mask as a random selection, but proves that the order of quantifiers cannot be interchanged.

**One-factor corollary.** In the inclusion-induced one-factor representation, each predictable multiplier contains the factor \((-1)^{\beta_{k-1,\varnothing}}\), because the empty subset belongs to every relevant power set. When these empty-subset bits are independent fair Bernoulli variables and independent of all other coefficients, they form the \(\varepsilon_k\) masks of this theorem. Conditioning on the remaining coefficients gives admissible predictable maps \(h_k\); the joint-almost-everywhere quenched functional limit follows.

## Verification
The accompanying standalone standard-library program `verify_sign_mask.py` performs exact rational finite-path and finite-mask enumerations for lengths one through five. It verifies the centered-mask mean-zero identity, the exact variance identity \(\mathbb E_\varepsilon(\sum_kZ_k)^2=\sum_k(1-m_k^2)\), the finite cross covariance, and maximization of deterministic signed bias by \(h_k=\operatorname{sgn}(m_k)\). The verified program reports 3,116 exact checks. The infinite strong law and martingale functional limit are proved analytically, not inferred from enumeration.

## Relationship to prior work
Hamza and Tournier, *Are random random walks normal?* (arXiv:2610.01658v1, 2026), establish annealed functional convergence for their time-and-subset-size independent one-factor construction (Corollary 9) and explicitly leave its quenched counterpart unresolved. Their separate Theorem 2 treats a different, subset-indexed independence class, not the time-by-size one-factor regime. The present result supplies an exact **universal external-mask bias criterion** and hence a fair-empty-coefficient quenched subcase; it does not claim the whole open regime.

Collevecchio, Hamza, Shi and Williams, *Limit theorems and ergodicity for general bootstrap random walks* (arXiv:2010.16000; published 2022), supply a general Brownian convergence criterion for deterministic predictable transformations, based on their quadratic covariations (Theorem 6). That abstract criterion motivates the bracket argument but does not state the sharp universal Cesàro absolute-bias characterization for independent temporal masks. Classical independent-variable strong laws, Hoeffding bounds and martingale invariance principles are the ingredients; none is itself claimed as new.

## Limitations
The result does **not** establish quenched normality for all elliptic one-factor parameters of Hamza--Tournier; in particular, fixed nonfair empty-subset bits are outside the sufficient corollary. Independence of temporal masks from the entire predictable family is essential, and the universal characterization does not address dependent masks. The cutoff concerns a *universal all-rules property* and is not necessary for a particular recycling rule. No common almost-sure mask set works simultaneously for every possible rule. An equivalent formulation hidden in general martingale-transform literature is an originality risk, and independent review has not been performed.

## References
1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first submitted 2026-10-01), Sections 1, 2 and 4.2, especially Corollary 9 and the following remark. https://arxiv.org/abs/2610.01658
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electronic Journal of Probability 27 (2022), article 92; arXiv:2010.16000, Theorem 6. https://arxiv.org/abs/2010.16000
3. J. Jacod and A. N. Shiryaev, *Limit Theorems for Stochastic Processes*, Springer, 1987 (classical martingale functional CLT; also cited as reference [4] in Hamza--Tournier).
