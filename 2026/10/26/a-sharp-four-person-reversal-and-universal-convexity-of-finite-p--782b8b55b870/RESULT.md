# A sharp four-person reversal and universal convexity of finite-population nonlinear public-goods selection

## Finding

For the finite-population sampling model below, with any mixture of group sizes and a separate positive geometric synergy or discounting factor for every group size, the **expected payoff advantage of cooperation is a discretely convex sequence in the population's number of cooperators**. Its strict signs therefore change at most twice as the number of cooperators increases. If two changes occur, they have the order positive–negative–positive, never negative–positive–negative. The two-change upper bound is sharp at the smallest possible population size, four.

More precisely, let \(N\ge4\), and let \(j\in\{1,\ldots,N-1\}\) count cooperators. Let \(w_\ell\ge0\), \(\sum_{\ell=2}^N w_\ell=1\), \(\delta_\ell>0\), \(b>0\), and \(c>0\). If \(\Delta(j)\) is the expected cooperator payoff minus the expected defector payoff in this population, then

\[
\Delta(j)=-c+b\sum_{\ell=2}^{N-1}\frac{w_\ell(N-\ell)}{\ell(N-1)}\,H_{N-2,j-1,\ell-1}(\delta_\ell),
\]

where the hypergeometric generating function is

\[
H_{M,K,s}(d)=\frac{1}{\binom Ms}\sum_{q=\max(0,s-M+K)}^{\min(K,s)}\binom Kq\binom{M-K}{s-q}d^q.
\]

For every \(1\le j\le N-3\), the **exact nonnegative curvature identity** is

\[
\begin{aligned}
&\Delta(j+2)-2\Delta(j+1)+\Delta(j)\\
&=b\sum_{\ell=3}^{N-1}\frac{w_\ell(N-\ell)}{\ell(N-1)}
\frac{(\ell-1)(\ell-2)}{(N-2)(N-3)}
(\delta_\ell-1)^2\,H_{N-4,j-1,\ell-3}(\delta_\ell)\ \ge0.
\end{aligned}
\]

The inequality is strict for every such \(j\) if at least one size \(\ell\in\{3,\ldots,N-1\}\) has \(w_\ell>0\) and \(\delta_\ell\ne1\). Groups containing the entire population contribute no marginal public benefit to the cooperator-versus-defector comparison.

For a sharp instance, use \(N=4\), size weights \(w_2=3/4\), \(w_3=1/4\), \(w_4=0\), factors \(\delta_2=1/10\), \(\delta_3=3\), and \(b/c=4\). Then

\[
\left(\frac{\Delta(1)}c,\frac{\Delta(2)}c,\frac{\Delta(3)}c\right)
=\left(\frac19,-\frac7{60},\frac1{10}\right).
\]

Thus the selection direction changes twice, already with four players. At most two transient states exist when \(N\le3\), so four is the minimal population size for two strict changes.

## Assumptions and scope

There are exactly \(N\) exchangeable individuals, each currently playing cooperate or defect. The population has \(j\) cooperators, with \(1\le j\le N-1\). A focal individual receives a random group-size draw \(\ell\) with fixed probability \(w_\ell\), independent of strategy and population state. The focal individual's \(\ell-1\) co-players are drawn **uniformly without replacement** from the other \(N-1\) individuals.

For a group of size \(\ell\) containing \(k\) cooperators, each group member receives common public benefit

\[
B_\ell(k)=\frac b\ell\sum_{t=0}^{k-1}\delta_\ell^t,
\]

with the empty sum equal to zero. A cooperator additionally pays \(c\); a defector pays no contribution cost. The same \(b,c\) apply to all groups, and the nonlinear multiplier \(\delta_\ell\) is allowed to depend on group size. Payoffs are averaged over the group-size draw and co-player sample. This is a one-shot **expected-payoff comparison**, not a claim about a payoff realized in a particular sampled game.

The sign statements also apply to the expected direction of the standard finite-population pairwise-comparison Fermi process **when its imitation probabilities are calculated from these expected payoffs** and its selection intensity is positive. They do not automatically extend to models which apply the nonlinear imitation probability to individually realized random payoffs *before* averaging, or to spatial assortment and strategy-dependent group selection.

## Proof

**1. Exact sampling formula.** Fix \(\ell<N\), \(j\), and compare a cooperator focal with a defector focal. For the cooperator focal, the other individuals consist of \(j-1\) cooperators and \(N-j\) defectors. For the defector focal, they consist of \(j\) cooperators and \(N-j-1\) defectors. Couple these two sampling experiments by changing exactly one distinguished other player from defector to cooperator, leaving the \(N-2\) remaining players fixed with \(j-1\) cooperators.

The distinguished player is included in a uniformly sampled group of \(\ell-1\) co-players with probability \((\ell-1)/(N-1)\). If included, the cooperator focal's extra contribution and the other player's changed strategy cancel in the total number of group cooperators; both focal types receive the same public benefit. If excluded, probability \((N-\ell)/(N-1)\), both focal types see the same number \(Q\) of cooperative co-players, and the cooperator focal generates one additional geometric increment \(b\delta_\ell^Q/\ell\). Conditional on exclusion, \(Q\) is hypergeometric with population \(N-2\), successful players \(j-1\), and sample size \(\ell-1\). Subtracting the contribution cost gives

\[
\pi_C^{(\ell)}(j)-\pi_D^{(\ell)}(j)
=-c+\frac{b(N-\ell)}{\ell(N-1)}H_{N-2,j-1,\ell-1}(\delta_\ell).
\]

For \(\ell=N\), every focal group contains the entire population, so the public benefits agree and the difference is \(-c\), consistent with the factor \(N-\ell=0\). Taking the weighted average over sizes gives the stated expression for \(\Delta(j)\).

**2. Hypergeometric second-difference identity.** For \(0\le K\le M-2\), \(2\le s\le M\), and \(d>0\), mark two initially noncooperative individuals among the \(M\) players, with \(K\) cooperative players among the remaining \(M-2\). Let \(I_1,I_2\in\{0,1\}\) indicate whether the two marked individuals belong to a uniformly sampled \(s\)-subset; let \(Q\) count cooperative sampled players among the other \(M-2\). Changing the strategies of both marked players and taking the second finite difference gives exactly

\[
\begin{aligned}
&H_{M,K+2,s}(d)-2H_{M,K+1,s}(d)+H_{M,K,s}(d)\\
&=\mathbb E\big[d^Q(d^{I_1}-1)(d^{I_2}-1)\big]\\
&=(d-1)^2\frac{s(s-1)}{M(M-1)}H_{M-2,K,s-2}(d).
\end{aligned}
\]

Symmetry of the two marked players makes the mixed middle term precisely twice \(H_{M,K+1,s}\). The last equality conditions on both marked players being sampled and counts the remaining \(s-2\) sampled individuals. Every factor on the right is nonnegative, and its hypergeometric factor is strictly positive because \(d>0\). For \(s=1\), the second difference is zero. Substituting \(M=N-2\), \(K=j-1\), and \(s=\ell-1\) into Step 1 proves the displayed curvature identity with its strictness condition.

**3. Sign-pattern bound and minimality.** Every discretely convex real sequence has nondecreasing successive differences. Consequently its strictly negative indices form an integer interval: if \(a<c\) are negative, every \(b\) strictly between them is at most the linear interpolation of their negative endpoint values, hence also negative. The strict sign pattern, after zero entries are ignored, therefore has at most two changes. Two changes must be positive–negative–positive. This conclusion also holds in the affine or identically zero degeneracies (which have no more sign changes).

With fewer than four individuals there are fewer than three interior population states, so two strict changes are impossible. With \(N=4\), the stated rational parameters yield the benefit coefficients before multiplying by \(b\):

\[
\left(\sum_\ell\frac{w_\ell(4-\ell)}{3\ell}
 H_{2,j-1,\ell-1}(\delta_\ell)\right)_{j=1}^{3}
=\left(\frac5{18},\frac{53}{240},\frac{11}{40}\right).
\]

Multiplying by \(b/c=4\) and subtracting \(1\) gives exactly \((1/9,-7/60,1/10)\), so four is sufficient.

**4. Interpretation under expected-payoff imitation.** If an ordered pair of unlike individuals is chosen uniformly with replacement and a defector copies a cooperator with Fermi probability \(1/(1+e^{-\beta\Delta(j)})\), while the reverse probability is \(1/(1+e^{\beta\Delta(j)})\), then the one-step expected change in cooperator count is

\[
\frac{j(N-j)}{N^2}\tanh\left(\frac{\beta\Delta(j)}2\right).
\]

For \(\beta>0\) its sign is the sign of \(\Delta(j)\), so the same two-change bound applies. This is a **direction-of-selection statement**, not an assertion of distinct stochastic stationary states or guaranteed fixation.

For each fixed supported group size and a sequence with \(j/N\to x\in(0,1)\), the hypergeometric generating function tends to \([1+(\delta_\ell-1)x]^{\ell-1}\) as \(N\to\infty\). The prefactor tends to \(1/\ell\), recovering the established well-mixed nonlinear public-goods selection gradient.

## Verification

The standalone `verify.py` uses exact rational arithmetic to compute conditional payoffs directly by enumerating every distinct co-player subset, independently computes the coupled hypergeometric formula, and checks equality across population sizes \(4\le N\le9\), all permitted group sizes, four multiplier values, and every nontrivial cooperator count. It also independently checks the claimed second-difference identity and the four-person exact witness.

Executing `python verify.py` gives 796 exact direct-versus-formula comparisons, 532 exact second-difference identities, and the rational witness \((1/9,-7/60,1/10)\). The universal proof is the two-marked-player identity, not finite testing.

## Relationship to prior work

Llabrés et al. (2026, arXiv:2604.07228v1), Sections II–III, define the geometric nonlinear benefit function and obtain the infinite well-mixed replicator equation for one group size, then fully analyze mixtures of sizes two and three. The result here concerns **finite sampling without replacement**, arbitrarily many size classes, size-specific nonlinear multipliers, an exact discrete curvature identity, and the minimal four-player two-switch witness.

Peña (2012) analyzes diverse group sizes in an infinite well-mixed population, prominently via Jensen's inequality; that work is not a finite-population hypergeometric second-difference classification with independently chosen nonlinear multipliers. Peña, Lehmann, and Nöldeke (2014) give a general Bernstein-polynomial and gain-sign framework for infinite-population multiplayer games. Their general sign-counting principles are **antecedent theory**, not claimed here as new; the specific finite hypergeometric convexity identity and sharp finite-population specialization are the added steps. Duong, Durbac, and Han (2023), Section 2.1.2, explicitly derive the factor \((N-\ell)/(N-1)\) for a **linear** public-goods game, which is recovered by setting every \(\delta_\ell=1\). The present result is not a rediscovery of that linear factor.

## Limitations

The result assumes the specified one-shot payoff, strategy-independent size weights, a well-mixed finite population, uniformly sampled distinct co-players, and expected payoffs. It says nothing about arbitrary nonlinear benefit functions, arbitrary spatial hypergraphs, group-dependent costs, state-dependent group sampling, realized-payoff Fermi updating, or fixation probabilities. The direction-of-selection sequence need not itself correspond to a deterministic finite-population equilibrium. Established general gain-sign theorems and prior group-size-heterogeneity work significantly overlap in motivation and machinery; although no exact finite hypergeometric mixed-order statement was identified among inspected sources, an older equivalent specialization is still possible. No independent scientific audit has been performed.

## References

1. J. Llabrés, O. Sadekar, F. Malizia, and F. Battiston, *Emergence of cooperation in nonlinear higher-order public goods games*, arXiv:2604.07228v1 (first posted 2026-04-08), especially Eqs. (1)–(2), (7), and (11)–(16). https://arxiv.org/html/2604.07228v1
2. J. Peña, *Group-size diversity in public goods games*, Evolution **66** (2012), 623–636, DOI:10.1111/j.1558-5646.2011.01504.x. https://onlinelibrary.wiley.com/doi/10.1111/j.1558-5646.2011.01504.x
3. J. Peña, L. Lehmann, and G. Nöldeke, *Gains from switching and evolutionary stability in multi-player matrix games*, Journal of Theoretical Biology **346** (2014), 23–33, arXiv:1310.0498. https://arxiv.org/abs/1310.0498
4. M. H. Duong, C. M. Durbac, and T. A. Han, *Cost optimisation of hybrid institutional incentives for promoting cooperation in finite populations*, Journal of Mathematical Biology **87** (2023), article 77, DOI:10.1007/s00285-023-02011-6. https://link.springer.com/article/10.1007/s00285-023-02011-6
