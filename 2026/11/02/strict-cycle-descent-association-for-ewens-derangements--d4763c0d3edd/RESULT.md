# Strict cycle–descent association for Ewens derangements

## Finding
Fix an integer \(n\ge4\) and a real parameter \(\theta>0\). Sample a fixed-point-free permutation \(\Pi_n\) of \(\{1,\ldots,n\}\) with probability proportional to \(\theta^{K_n}\), where \(K_n\) is its number of cycles. Let \(D_n\) be its number of ordinary descents and \(C_{2,n}\) its number of two-cycles. For **every strictly increasing real function** \(f\) on the positive integers,

\[
\operatorname{Cov}_{\theta}(f(K_n),D_n)
=\frac{\binom n2\theta Z_{n-2}(\theta)}{nZ_n(\theta)}
\left(\mathbb E_{\theta}f(1+K_{n-2})-\mathbb E_{\theta}f(K_n)\right)>0,
\]

where \(Z_m(\theta)=\sum_{\pi\in\mathcal D_m}\theta^{K(\pi)}\), \(\mathcal D_m\) is the set of derangements of size \(m\), and expectations involving \(K_{n-2}\) are taken under the same positive parameter \(\theta\). The positive bracket follows from a simultaneous stochastic ordering:

\[
K_{n-1}\ \le_{\mathrm{st}}\ K_n\ \le_{\mathrm{st}}\ 1+K_{n-2}
\qquad(n\ge4).
\]

For \(n=2,3\), the covariance is zero because the cycle count is constant. In particular, \(\operatorname{Cov}_{\theta}(K_n,D_n)>0\) for every \(n\ge4\), in marked contrast with the **unconditioned uniform** law on all permutations, where

\[
\operatorname{Cov}(K_n,D_n)=-\frac{1}{2n}\qquad(n\ge2).
\]

The class-conditional expected-descent formula and the Ewens derangement distribution used below are established results. The finding is the all-parameter strict association, its increasing-transform strengthening, and the stochastic sandwich yielding its strict sign.

## Assumptions and scope
A permutation is a bijection of \(\{1,\ldots,n\}\). A fixed point is a position \(i\) for which \(\pi(i)=i\), and a derangement has none. A cycle is a cycle in the disjoint-cycle decomposition, not a descent run. An ordinary descent is a position \(1\le i<n\) such that \(\pi(i)>\pi(i+1)\). All covariance and stochastic-order statements refer to the explicitly specified probability laws; the unconditioned comparison uses the uniform measure on the entire symmetric group.

For the partition function, set \(Z_0(\theta)=1\), \(Z_1(\theta)=0\), \(Z_2(\theta)=\theta\), and \(Z_3(\theta)=2\theta\). All \(Z_n(\theta)\) for \(n\ge2\) are strictly positive when \(\theta>0\). The stochastic order \(X\le_{\mathrm{st}}Y\) means \(\mathbb P(X\ge t)\le\mathbb P(Y\ge t)\) for each real threshold \(t\). The theorem does **not** assert stochastic association of the full joint random pair \((K_n,D_n)\); it asserts the stated covariance inequality for increasing transformations of \(K_n\).

## Proof
**1. Conditional descent mean.** Fix a conjugacy class with \(a_1\) fixed points and \(a_2\) two-cycles, and choose a permutation uniformly in that class. Conjugating the permutation by the adjacent transposition interchanging labels \(i\) and \(i+1\) is a measure-preserving involution. Except when the images at positions \(i,i+1\) are exactly the two values \(i,i+1\), this involution reverses the truth of the descent event at \(i\), because an adjacent transposition preserves the relative order of every other pair of values. In the two exceptional cases, two fixed points contribute no descent, while a two-cycle contributes one. By symmetry among labels their probabilities are respectively \(a_1(a_1-1)/(n(n-1))\) and \(2a_2/(n(n-1))\). Consequently,

\[
\mathbb P(\Pi(i)>\Pi(i+1)\mid\text{cycle type})
=\frac12+\frac{a_2-\binom{a_1}2}{n(n-1)}.
\]

Summing over \(n-1\) positions gives the classical identity

\[
\mathbb E(D_n\mid\text{cycle type})=
\frac{n-1}{2}+\frac{a_2-\binom{a_1}2}{n}.
\]

Under the Ewens derangement law \(a_1=0\), so conditioning further on the cycle count gives

\[
\operatorname{Cov}_{\theta}(f(K_n),D_n)
=\frac1n\operatorname{Cov}_{\theta}(f(K_n),C_{2,n}).
\tag{1}
\]

This expected-descent identity was established by Fulman and appears, in the displayed form above, in Corollary 4.10 of Campion Loth et al. It has been reconstructed here by the adjacent-label involution rather than assumed without explanation.

**2. Marking a two-cycle.** For an unordered pair of labels, the total Ewens weight of derangements in which that pair forms a two-cycle is \(\theta Z_{n-2}(\theta)\). Conditional on this event, the remaining \(n-2\) labels carry an independent Ewens derangement and the total number of cycles is \(1+K_{n-2}\). Counting all unordered pairs yields

\[
\mathbb E_{\theta}[C_{2,n}]=\binom n2\frac{\theta Z_{n-2}(\theta)}{Z_n(\theta)},
\qquad
\mathbb E_{\theta}[C_{2,n}f(K_n)]
=\mathbb E_{\theta}[C_{2,n}]\,\mathbb E_{\theta}f(1+K_{n-2}).
\tag{2}
\]

Combining (1) and (2) gives the asserted exact covariance identity, leaving only positivity of its final bracket.

**3. A simultaneous stochastic sandwich.** Removing label \(n\) from a cycle of length at least three produces a derangement on \(n-1\) labels, and there are \(n-1\) possible insertion sites to reverse this deletion. If label \(n\) lies in a two-cycle, removal of that cycle leaves a derangement on \(n-2\) labels, and there are \(n-1\) possible partners. Tracking the cycle weights gives, for all \(n\ge4\),

\[
Z_n(\theta)=(n-1)(Z_{n-1}(\theta)+\theta Z_{n-2}(\theta)).
\]

Moreover, the distribution of \(K_n\) is the mixture of \(K_{n-1}\) with positive weight \(a_n=(n-1)Z_{n-1}/Z_n\) and \(1+K_{n-2}\) with positive weight \(b_n=(n-1)\theta Z_{n-2}/Z_n\), satisfying \(a_n+b_n=1\).

At sizes two and three, both cycle-count variables equal one. Inductively assume \(K_{m-2}\le_{\mathrm{st}}K_{m-1}\le_{\mathrm{st}}1+K_{m-2}\). A mixture of its ordered endpoints lies between them, proving \(K_{m-1}\le_{\mathrm{st}}K_m\le_{\mathrm{st}}1+K_{m-2}\). Since also \(K_{m-2}\le_{\mathrm{st}}K_{m-1}\), the upper bound implies \(K_m\le_{\mathrm{st}}1+K_{m-1}\), closing the induction.

For every \(n\ge4\), \(K_{n-1}\) has positive probability of being one (one long cycle), while \(1+K_{n-2}\ge2\) always. Thus the stochastic comparison \(K_{n-1}\le_{\mathrm{st}}1+K_{n-2}\) is strict, at least at threshold two. Because \(f\) is strictly increasing, \(\mathbb Ef(K_{n-1})<\mathbb Ef(1+K_{n-2})\). The positive-mixture identity then gives \(\mathbb Ef(K_n)<\mathbb Ef(1+K_{n-2})\). The prefactor in the covariance identity is positive. This proves the strict result for all claimed sizes and all positive real \(\theta\).

**4. Unconditioned comparison.** In a uniform permutation, a specified two-cycle and a specified pair of fixed points each have probability \(1/(n(n-1))\). Therefore \(\mathbb E C_2=\mathbb E\binom{C_1}2=1/2\). Marking either kind of pair and deleting it leaves a uniform permutation on \(n-2\) labels; the total cycle count becomes respectively \(1+K_{n-2}\) or \(2+K_{n-2}\). Consequently

\[
\operatorname{Cov}\left(K_n,C_2-\binom{C_1}2\right)
=\frac12\left((1+\mathbb EK_{n-2})-(2+\mathbb EK_{n-2})\right)
=-\frac12.
\]

The same conditional descent identity from step 1, divided by \(n\), proves the negative covariance \(-1/(2n)\). The empty permutation has zero cycles, so this argument includes the boundary \(n=2\).

## Verification
The standalone Python 3 program `verify.py` uses only the standard library and exact rational arithmetic. It independently enumerates all derangements for \(2\le n\le8\) for the parameters \(\theta\in\{1/2,1,2,3\}\); checks the partition function, cycle-count law, class-conditional descent means, and the covariance formula for \(f(k)=k,k^2,k^3\); and checks stochastic tail inequalities by recurrence through \(n=35\). A separate enumeration through size eight verifies the unconditioned sign. The extracted program reports 3,295 exact assertions passed. These finite checks supplement the complete analytic proof and are not claimed to establish its infinite quantifiers.

## Relationship to prior work
Bóna (2006) studies cycle-count generating polynomials for derangements. Fulman (1998) established class-conditional descent moments, and Campion Loth et al. (2023), Corollary 4.10, provide an explicit version of the mean formula. Eriksen, Freij and Wästlund (2008) enumerate derangements with prescribed descent sets and establish dependence of the derangement event and descents under uniform permutations. Da Silva, Jamshidpey and Tavaré (2020) develop the Ewens derangement law and cycle-count distributions. Gessel and Reutenauer (1993) provide a broader joint cycle-structure/descent-set generating function. These works supply substantial antecedents, including the exact mean and marginal cycle law. The point assessed separately is the strict positive covariance for all positive Ewens parameters and every strictly increasing transform of the cycle count, proved through the stochastic sandwich.

## Limitations
The assertion is only for the weighted **derangement** measure and ordinary descents; it is not a general positive-dependence theorem for all cycle-pattern statistics, nor an independence, full stochastic association, or central-limit statement. The displayed formula is a first mixed moment, not an explicit joint distribution. Finite computations alone do not establish generality. Although related full papers and prior formulas have been examined, the possibility that this monotone-transform sign statement is implicit in other specialized enumerations remains a historical-priority risk.

## References
- M. Bóna, *On a Balanced Property of Derangements*, first public arXiv submission 2006-06-12, https://arxiv.org/abs/math/0606277.
- J. Fulman, *The Distribution of Descents in Fixed Conjugacy Classes of the Symmetric Groups*, Journal of Combinatorial Theory Series A (1998), Theorem 2.
- N. Eriksen, R. Freij, J. Wästlund, *Enumeration of Derangements with Descents in Prescribed Positions*, arXiv:0811.1925 (2008), https://arxiv.org/abs/0811.1925.
- P. H. da Silva, A. Jamshidpey, S. Tavaré, *Random Derangements and the Ewens Sampling Formula*, arXiv:2006.04840 (2020), https://arxiv.org/abs/2006.04840.
- J. Campion Loth et al., *Permutation Statistics in Conjugacy Classes of the Symmetric Group*, arXiv:2301.00898 (2023), Corollary 4.10, https://arxiv.org/abs/2301.00898.
- I. M. Gessel, C. Reutenauer, *Counting Permutations with Given Cycle Structure and Descent Set*, Journal of Combinatorial Theory Series A (1993).
