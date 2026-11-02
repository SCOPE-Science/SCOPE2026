# A sharp Bernoulli threshold for ex-ante fairness versus ex-post envy-freeness probability

## Finding

For every integer \(r\ge1\), two agents divide \(r+1\) indivisible lottery goods before their values are realized. One distinguished good has value \(2r\) with probability \(1/2\) and zero otherwise; each of the \(r\) other goods has value \(2\) with probability \(1/2\) and zero otherwise, independently for every agent and every good. Agents have additive utilities. A fixed deterministic allocation is *ex-ante envy-free* (EF) if each agent's expected value of their own bundle is at least their expected value of the other's. It is *ex-post EF* if both agents prefer their own realized bundles. The objective is the probability of ex-post EF, over the lottery valuations.

Every ex-ante EF fixed allocation assigns the distinguished good to one agent and all \(r\) ordinary goods to the other (up to interchanging the agents). Let \(t\in\{0,\ldots,r\}\) be the number of ordinary goods accompanying the distinguished good. Set \(T=2^{r+1}\) and \(S_t=\sum_{j=t}^r\binom rj\), with \(S_{r+1}=0\). The **exact ex-post EF probability** is

\[
P_r(0)=\frac{(2^r+1)^2}{T^2},\qquad
P_r(t)=\frac{S_t(T-S_{t+1})}{T^2}\quad(1\le t\le r).
\]

The ex-ante EF allocation maximizes this probability for \(r=1,2\), but **fails to maximize it for every \(r\ge3\)**. For the latter range, the maximizing \(t\) is given exactly by the first \(t\ge1\) for which

\[
\frac{S_{t+1}}{T}\le\frac{t+1}{r+1}.
\]

If this inequality is strict, that \(t\) is the unique maximizing count; if equality holds, that \(t\) and \(t+1\) are the only maximizing counts. If \(t_r\) is the smallest maximizing count, then \(t_r/r\to1/2\) as \(r\to\infty\). At \(r=3\), ex-ante EF attains \(81/256\), while allocating one ordinary good with the distinguished good attains \(21/64=84/256\).

## Assumptions and scope

The goods are labeled, but ordinary goods have identical distributions, so only \(t\) matters. All \(2(r+1)\) value indicators are mutually independent fair bits; each agent has the same marginal distribution for each named good, but the distinguished good differs in scale from ordinary goods. Utility additivity is assumed. Allocation is fixed **before** the value indicators are sampled and is not permitted to depend on reports, observations, or random draws. Envy comparisons use weak inequalities; ties count as envy-free. The probabilities here are with respect to values, not over a lottery of allocation rules. The result does not address mechanism truthfulness or arbitrary uncertain-item distributions.

## Proof

**Expected-value characterization.** Every ordinary good contributes expected utility \(1\) to either agent, and the distinguished good contributes \(r\). The bundle containing it has expected value \(r+t\), while the other has expected value \(r-t\). Identical per-item marginal distributions imply ex-ante EF precisely when those expectations agree, which means \(t=0\).

**One-agent comparison distribution.** For a fixed \(t\), the difference between an agent's value for the distinguished-good bundle and the other bundle, divided by \(2\), has law

\[
Q_t=t+\frac{Z}{2},\qquad Z=r\varepsilon_0+\sum_{j=1}^{r}\varepsilon_j,
\]

where the \(\varepsilon_j\) are independent uniform signs. Signs for ordinary goods allocated to the other bundle are negated without affecting their distribution. For the agent receiving the distinguished-good bundle, no envy is the event \(Q_t\ge0\); for the other agent, no envy is \(Q_t\le0\), and these two comparisons are independent because the agents' values are independent.

Writing \(K\sim\operatorname{Bin}(r,1/2)\), the conditional laws of \(Z\), given \(\varepsilon_0=1\) or \(\varepsilon_0=-1\), respectively, are \(2K\) and \(2(K-r)\). Hence, for each \(t\ge1\),

\[
\Pr(Q_t\le0)=S_t/T,\qquad
\Pr(Q_t\ge0)=1-S_{t+1}/T.
\]

For \(t=0\), symmetry and the equality event \(\Pr(Z=0)=2/T\) give both tail probabilities \((T+2)/(2T)\). Multiplying the independent agents' non-envy probabilities proves the displayed formulas.

**Exact optimization.** For \(1\le t<r\), put \(a_t=\binom rt\). Since \(S_t=S_{t+1}+a_t\) and \(S_{t+1}=S_{t+2}+a_{t+1}\), direct subtraction yields

\[
T^2(P_r(t+1)-P_r(t))
 =(a_t+a_{t+1})S_{t+1}-a_tT.
\]

As \(a_t/(a_t+a_{t+1})=(t+1)/(r+1)\), the sign of the difference is precisely the sign of \(S_{t+1}/T-(t+1)/(r+1)\). The first quantity strictly decreases with \(t\), while the second increases. Therefore the positive-indexed probabilities are unimodal, with at most a two-way adjacent tie and the exact threshold specified above.

Next,

\[
T^2(P_r(1)-P_r(0))=2^r(r-2)-r-2.
\]

This is strictly positive for every \(r\ge3\): at \(r=3\) it equals \(3\), and its consecutive differences are positive from there onward. For \(r=1\), the probabilities at \(t=0,1\) are \(9/16,1/4\). For \(r=2\), the values for \(t=0,1,2\) are \(25/64,21/64,1/8\). Thus the sharp global threshold is \(r=3\).

**Asymptotic location.** For any fixed \(0<\delta<1/2\), when \(t\le(1/2-\delta)r\) and \(r\to\infty\), a binomial tail estimate gives \(S_{t+1}/T\to1/2\), while \((t+1)/(r+1)\le1/2-\delta+o(1)\). The differences are eventually positive up to that range. Conversely for \(t\ge(1/2+\delta)r\), the binomial upper tail \(S_{t+1}/T\to0\) while \((t+1)/(r+1)\ge1/2+\delta+o(1)\), so differences are negative. The maximizing count therefore satisfies \(t_r/r\to1/2\).

## Verification

The companion script `verify.py`, using only Python's standard library and exact rational arithmetic, independently enumerates both agents' binary valuations for every \(1\le r\le10\) and \(0\le t\le r\), checks the count formula, then checks the exact unimodal threshold and sharp \(r=3\) boundary for all \(1\le r\le200\). Run `python3 verify.py`. The proof, not these bounded tests, establishes all infinite-parameter statements.

## Relationship to prior work

Aloisio, Bilò, Caruso, Flammini, and Vinci (AAMAS 2024) study the same fundamental precommitment timing under independently random bounded valuations, but minimize **expected maximum envy**, not the chance of exact joint ex-post EF; their bounds and random-allocation schemes do not imply the binomial-tail optimizer in this theorem.

Halpern, Psomas, and Zhang study fairness and welfare with random valuations in *Truthful Fair Division under Stochastic Valuations* (first public February 12, 2026), principally for valuation-responsive truthful mechanisms and high-probability asymptotic guarantees. The present theorem instead fixes allocation **before** valuations become known, uses heterogeneous item distributions, and optimizes the finite ex-post envy-free probability exactly.

Babaioff and Grofman's *On Best-of-Both-Worlds Fairness via Sum-of-Variances Minimization* (first public January 23, 2026) concerns randomness of the **allocation** under known valuations, not independent random values of goods. Chen and Long's *Randomized Online Fair Division* (first public September 20, 2026) similarly studies random allocation rules and online arrivals, rather than a precommitted allocation of intrinsically uncertain goods.

Igarashi and Oh's *Fair Division of Lotteries* (first public October 26, 2026) studies the closest precommitment model. Its convolution-power and non-atomic-symmetry theorems give conditions for optimality of ex-ante EF, while its general symmetry results bound realized fairness probabilities. The present two-point heteroscedastic family is atomic, has a scale-amplified Bernoulli good rather than convolution powers of a common generator, and is not covered by those optimality hypotheses; the exact all-\(r\) phase boundary and optimizer are not stated there. The relationship is an exact discrete boundary beyond those sufficient hypotheses, not a claim of a general extension of their theorems.

## Limitations

The theorem is restricted to two agents, fair independent binary valuation indicators, one distinguished good of scale \(2r\), and \(r\) goods of scale \(2\). It does not say that ex-ante fairness fails to maximize realized fairness for arbitrary valuation models, nor does it establish an algorithm for general input distributions. Scientific priority may be affected by unindexed equivalent binomial-tail or probability-of-fair-allocation results. Computer checks cover only the finite stated ranges. No independent audit is claimed.

## References

- A. Aloisio, V. Bilò, A. M. Caruso, M. Flammini, and C. Vinci, *Approximately Fair Allocation of Indivisible Items with Random Valuations*, AAMAS 2024, May 6–10, 2024. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p2120.pdf
- D. Halpern, A. Psomas, and S. Zhang, *Truthful Fair Division under Stochastic Valuations*, arXiv:2602.12359, v1 publicly released February 12, 2026. https://arxiv.org/abs/2602.12359
- M. Babaioff and Y. Grofman, *On Best-of-Both-Worlds Fairness via Sum-of-Variances Minimization*, arXiv:2601.16579, v1 publicly released January 23, 2026. https://arxiv.org/abs/2601.16579
- T. Chen and J. Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, arXiv:2609.23577, v1 publicly released September 20, 2026. https://arxiv.org/abs/2609.23577
- A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906, v1 publicly released October 26, 2026. https://arxiv.org/abs/2610.34906
