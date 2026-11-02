# Strict balancing of multiplicative near-envy under common Gamma-valued goods

## Finding

**Theorem (all-tolerance optimum and sharp near-equality law).** Fix integers \(n\ge 2\) and \(m\ge n\), shape \(\alpha>0\), rate \(\lambda>0\), and a finite multiplicative tolerance \(R>1\). Each of \(m\) indivisible goods has an independent realized positive value \(X_g\sim\operatorname{Gamma}(\alpha,\lambda)\), **identical for all agents**. A deterministic complete allocation is fixed **before** those values are drawn; an agent values any bundle by the sum of its realized good values. Writing \(Y_i\) for the total in agent \(i\)'s bundle, define its probability of multiplicative near-envy-freeness by

\[
P_R=\Pr\!\left\{\max_{1\le i\le n}Y_i\le R\min_{1\le i\le n}Y_i\right\}.
\]

An allocation maximizes \(P_R\) **if and only if** its bundle sizes differ by at most one. In particular, if \(m=qn+s\), where \(q\ge1\) and \(0\le s<n\), the maximizing size multiset consists of \(n-s\) copies of \(q\) and \(s\) copies of \(q+1\). The optimal count multiset is independent of \(\alpha\), \(\lambda\), and \(R\) (for every finite \(R>1\)).

More generally, for independent positive Gamma random variables with a common rate and arbitrary positive shape vector \(\boldsymbol\theta=(\theta_1,\ldots,\theta_n)\), the same probability is **strictly Schur-concave** in \(\boldsymbol\theta\) when the sum of the shapes is fixed: if \(\boldsymbol\theta\) majorizes \(\boldsymbol\eta\) and the vectors are not permutations, then \(P_R(\boldsymbol\theta)<P_R(\boldsymbol\eta)\).

The exact leading probability for tolerance \(R=1+\varepsilon\) is

\[
P_{1+\varepsilon}(\boldsymbol\theta)
=\frac{\Gamma(T)}{n^{T-1}\prod_{i=1}^n\Gamma(\theta_i)}\,\varepsilon^{n-1}
+o(\varepsilon^{n-1}),\qquad T=\sum_i\theta_i,
\]

and therefore the **sharp optimal coefficient** for the allocation model is

\[
C_{n,m,\alpha}=\frac{\Gamma(\alpha m)}{n^{\alpha m-1}\Gamma(\alpha q)^{n-s}\Gamma(\alpha(q+1))^s}.
\]

For exponential goods (\(\alpha=1\)), writing \(m=n+r\) and \(b_i=|A_i|-1\), the coefficient equals

\[
\frac{(n+r-1)!}{n^{n+r-1}\prod_i b_i!}
=\frac{(n+r-1)!}{n^{n-1}r!}\,
\Pr\left\{\operatorname{Multinomial}(r;1/n,\ldots,1/n)=\boldsymbol b\right\},
\]

an exact link between near-envy probability and equal-bin occupancy.

## Assumptions and scope

We use the shape-rate parameterization: a positive \(\operatorname{Gamma}(t,\lambda)\) variable has density \(\lambda^t x^{t-1}e^{-\lambda x}/\Gamma(t)\) for \(x>0\). The item values are independent **across goods** and perfectly correlated **across agents**, because all agents attach the same value to each given good. The allocation is fixed independently of the realization; choices made after seeing values are excluded. Complete allocation means every good is assigned once. If any bundle is empty, the event defining \(P_R\) is impossible because the other bundles have positive total value almost surely. We therefore discuss positive bundle counts, possible when \(m\ge n\).

For the shape-level assertion, \(\boldsymbol\theta\) and \(\boldsymbol\eta\) range over \((0,\infty)^n\), have the same coordinate sum, and majorization is in the usual descending-partial-sums sense. The strict assertion excludes vectors related only by a permutation. The cases \(R=1\), \(R=\infty\), non-Gamma item distributions, unequal item rates, and adaptive allocations are not included.

## Proof

**1. Gamma aggregation and a two-coordinate reduction.** For a fixed nonempty allocation, disjoint sums give independent \(Y_i\sim\operatorname{Gamma}(\theta_i,\lambda)\) with \(\theta_i=\alpha|A_i|\). Fix indices \(i\ne j\) and keep \(t=\theta_i+\theta_j\) and all other shapes unchanged. Let \(S=Y_i+Y_j\) and \(U=Y_i/S\). Beta-Gamma factorization gives \(S\sim\operatorname{Gamma}(t,\lambda)\), independent \(U\sim\operatorname{Beta}(\theta_i,\theta_j)\), and \(S\), \(U\), and all other \(Y_k\) independent. The law of \((S,(Y_k)_{k\ne i,j})\) is unchanged when shapes are balanced within this pair.

Fix \(S=s_0>0\) and all remaining totals \(Y_k=y_k>0\). If the remaining totals do not satisfy their own pairwise \(R\)-ratio inequalities, the near-envy event is impossible for any \(U\). Otherwise the necessary and sufficient constraints on \(U\) are

\[
L\le U\le 1-L,\qquad
L=\max\left\{\frac{1}{1+R},\ \max_{k\ne i,j}\frac{y_k}{Rs_0},\ \max_{k\ne i,j}\left(1-\frac{R y_k}{s_0}\right)\right\}.
\]

When the index set is empty, the last two maxima are omitted. If \(L>1/2\), the event is impossible; otherwise the interval is symmetric about \(1/2\), and is a proper subinterval of \((0,1)\) for all finite \(R>1\). This follows by writing the inequalities \(Y_a\le RY_b\) for each ordered pair and taking their intersection.

**2. Folded Beta ordering is strict.** Write \(d=|\theta_i-\theta_j|\) and \(t=\theta_i+\theta_j\). The density of \(Z=|U-1/2|\) on \(0<z<1/2\), up to its normalizing constant, is

\[
g_d(z)\ \propto\ \left(\frac14-z^2\right)^{(t-2)/2}
\cosh\!\left(d\,\operatorname{artanh}(2z)\right).
\]

To obtain this, add the Beta densities at \(1/2+z\) and \(1/2-z\). If \(d_2>d_1\ge0\), the ratio \(g_{d_2}(z)/g_{d_1}(z)\), before normalizing, strictly increases with \(z\), because its logarithmic derivative with respect to \(h=\operatorname{artanh}(2z)>0\) is

\[
d_2\tanh(d_2h)-d_1\tanh(d_1h)>0.
\]

Indeed \(d\mapsto d\tanh(dh)\) is strictly increasing for positive \(d\). A one-crossing (monotone likelihood-ratio) argument implies that \(Z\) is strictly stochastically larger for the more unequal pair: for every \(0<c<1/2\),

\[
\Pr_{d_2}(Z\le c)<\Pr_{d_1}(Z\le c).
\]

Consequently, every proper nonempty symmetric Beta interval has strictly more probability under a less unequal pair.

**3. Integrating the conditional comparison.** Steps 1 and 2 show nondecrease of \(P_R\) under any shape transfer that decreases \(|\theta_i-\theta_j|\) and preserves their sum. The increase is strict: with positive probability, \(S\) lies in an open interval around some \(s_0>0\) and each other \(Y_k\) lies close to \(s_0/2\). On that positive-probability set, the other pairwise inequalities hold and \(1/(1+R)\le L<1/2\), giving a proper nonempty interval. Gamma densities are strictly positive at all positive arguments, so this set has positive probability. (For \(n=2\) the interval is automatically proper and nonempty.) Since any proper majorization can be decomposed into finitely many such pairwise balancing transfers and permutations, strict Schur-concavity follows. For integer bundle counts, if two counts differ by at least two, transferring one good from the larger bundle to the smaller strictly raises \(P_R\), and iterating reaches precisely the balanced size multiset. Conversely any unbalanced positive size multiset admits such a transfer, so cannot maximize. All balanced size permutations yield the same probability.

**4. Exact small-tolerance coefficient.** Let \(f_i,F_i\) be the Gamma density and distribution function of \(Y_i\). Almost surely the minimum is unique, so for \(\varepsilon>0\),

\[
P_{1+\varepsilon}=\sum_{i=1}^n\int_0^\infty
f_i(x)\prod_{j\ne i}\bigl[F_j((1+\varepsilon)x)-F_j(x)\bigr]dx.
\]

For each \(x>0\), the bracket divided by \(\varepsilon\) converges to \(x f_j(x)\). For \(0<\varepsilon\le1\), the Gamma density ratio on \([x,(1+\varepsilon)x]\) is bounded by \(2^{\max(\theta_j-1,0)}\), so each bracket is at most that constant times \(\varepsilon x f_j(x)\). The resulting dominating function is a constant multiple of \(x^{n-1}\prod_i f_i(x)\), integrable on \((0,\infty)\). Dominated convergence gives

\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-(n-1)}P_{1+\varepsilon}
=n\int_0^\infty x^{n-1}\prod_i f_i(x)\,dx
=\frac{\Gamma(T)}{n^{T-1}\prod_i\Gamma(\theta_i)},
\]

as the common rate cancels. The balanced-count expression follows by substituting \(\theta_i=\alpha a_i\). Finally \(\Gamma(k)=(k-1)!\) for positive integers \(k\), yielding the multinomial occupancy identity in the exponential case.

## Verification

The included `verify.py` uses only Python's standard library and exact fractions. For integer Gamma shapes it derives event probabilities by expanding Gamma CDFs in the minimum-conditioned integral, then checks all positive integer count partitions for \(2\le n\le5\), \(n\le m\le10\), and \(R\in\{3/2,2,3\}\), verifying that precisely balanced count multisets maximize. It also independently compares the two-agent formula with exact Beta binomial tails and validates small-tolerance coefficient orderings. Running `python3 verify.py` prints `VERIFY_OK exact_profile_comparisons=306 strict_comparisons=216 beta_reductions=108 small_tolerance_coefficients=checked`. This **finite** computational check is corroboration, not a proof of the all-real-parameter theorem, which is supplied in the preceding section.

## Relationship to prior work

Halpern, Psomas and Zhang (2026), including their discussion and Appendix B on correlated valuations, examine truthful mechanisms and high-probability ordinary envy-freeness for stochastic preferences, not the exact probability of a fixed pre-realization allocation under perfectly shared Gamma goods. Their main bounded-value, independent-agent model does not include the present Gamma setting; their Appendix B requires non-perfect dependence for its two-agent guarantee. Garg, Narayan and Shen (2025) allow correlated values but their positive asymptotic mechanism requires positive normalized cross-agent valuation separation, excluding perfectly identical agents, and does not optimize multiplicative near-envy over bundle counts. Gölz, Igarashi, Manurangsi and Suksompong (2025) derive group-allocation and high-probability asymptotic existence results under independent agent-item values; their results neither state nor imply this all-tolerance Gamma-shape ordering. Corrado's (2011) work on Dirichlet extrema/ranges suggests related computational distribution methods, but the accessible abstracts do not establish its coverage of the **shape-majorization and optimal allocation** theorem here; the full article was not available for a decisive comparison.

These are distinctions between mathematical claims and assumptions, not claims that no relevant unpublished or unindexed result exists. Beta-Gamma factorization, monotone likelihood ratios, and majorization transfers are classical ingredients; novelty is sought in their combination for strict global multiplicative near-envy optimization and its exact coefficient.

## Limitations

The result applies only to iid Gamma-valued goods with a common shared realization across agents, additive utility, and allocation fixed before revelation. It is not a result about ordinary exact envy-freeness at finite continuous samples, which has probability zero for a fixed allocation, nor about choosing a favorable allocation after seeing goods. It does not cover heterogeneous rates, arbitrary item laws, unequal valuation scales, or strategic incentives. The counting formula is asymptotic only as the **tolerance** tends to zero while \(n,m,\alpha\) remain fixed. Complete historical priority cannot be established from the inspected literature; a relevant 2011 Dirichlet range paper was inaccessible in full.

## References

1. Daniel Halpern, Alexandros Psomas and Shirley Zhang. *Truthful Fair Division under Stochastic Valuations*, arXiv:2602.12359v1, first public 2026-02-12. https://arxiv.org/html/2602.12359v1 (especially Sections 1–2, 5 and Appendix B).
2. Jugal Garg, Vishnu V. Narayan and Yuang Eric Shen. *Designing Truthful Mechanisms for Asymptotic Fair Division*, arXiv:2512.10892v1, 2025-12-11. https://arxiv.org/html/2512.10892v1 (Sections 1–3, 6).
3. Paul Gölz, Ayumi Igarashi, Pasin Manurangsi and Warut Suksompong. *Fair Allocation of Indivisible Goods with Variable Groups*, arXiv:2511.06218v1, 2025-11-09. https://arxiv.org/html/2511.06218v1 (Sections 1 and 5).
4. Pasin Manurangsi and Warut Suksompong. *When Do Envy-Free Allocations Exist?*, arXiv:1811.01630, first submitted 2018-11-05. https://arxiv.org/abs/1811.01630.
5. Charles J. Corrado. *The exact distribution of the maximum, minimum and the range of Multinomial/Dirichlet and Multivariate Hypergeometric frequencies*, *Statistics and Computing* **21** (2011), 349–359. https://doi.org/10.1007/s11222-010-9174-3 (full article not inspected).
