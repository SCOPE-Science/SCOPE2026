# One-surplus temporal EF1 for personalized positive two-tier goods

## Finding

**Theorem (one-surplus temporal EF1).** For every integer \(n\ge2\), let \(m\) indivisible goods arrive individually and irrevocably, where \(0\le m\le n+1\). Every agent \(i\) has an additive value function and known tier constants satisfying
\[
0<\ell_i<h_i,\qquad v_i(g)\in\{\ell_i,h_i\}\quad\text{for every arriving good }g.
\]
There is a deterministic online allocation rule, with no knowledge of future goods, their order, or per-agent frequencies, such that **every allocation prefix is envy-free up to one good (EF1)**. The rule uses only the current good's values and previous assignments.

The structural mechanism is a *universally unenvied low-tier anchor*: after distributing the first \(n\) goods one per agent by the high-tier-first rule below, the earliest low-tier recipient, if one exists, holds a singleton \(g_j\) satisfying
\[
v_i(g_i)\ge v_i(g_j)\qquad\text{for every agent }i\ne j,
\]
where \(g_i\) denotes the first-phase good given to agent \(i\). This certifies where to put the sole surplus good.

## Assumptions and scope

All agents and their distinct positive tier constants \((\ell_i,h_i)\) are known before the first allocation. The rule observes the vector of values of the good currently arriving, but not any future goods or their order. Tiers can differ arbitrarily between agents and there may be arbitrarily many different patterns of high-valuing agents among the goods. Every good must be assigned immediately; no reallocation, waiting buffer, or discarded goods are permitted. If only one of an agent's two tier values actually occurs, the rule still applies.

An allocation \((A_i)_{i=1}^n\) is EF1 precisely when, for every ordered pair \((i,j)\) with \(A_j\ne\varnothing\), there exists \(g\in A_j\) for which \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\). We impose this condition at every prefix, not only after the last arrival.

**Online rule.** For the first \(n\) arrivals, each arriving good is assigned to a previously unassigned agent who values it at their high tier if one exists; otherwise, assign it to any previously unassigned agent. Fix deterministic tie-breaking. Record the first recipient whose assigned good has their low-tier value. If a good \(g_{n+1}\) arrives, give it to this recorded recipient; if there is none, give it to any agent. In a shorter stream simply stop after the last good.

## Proof

**First-phase prefix property.** At every prefix of length at most \(n\), no agent receives more than one good. For any pair \((i,j)\), removing the unique good from \(A_j\), if there is one, leaves the empty set. Since singleton values are positive, EF1 holds for every such prefix.

**Unenvied-anchor lemma.** Assume the first \(n\) goods have arrived; write \(g_i\) for the distinct singleton received by agent \(i\). If every agent received a high-tier good, then \(v_i(g_i)=h_i\ge v_i(g_j)\) for all \(i,j\), so any \(j\) is a universally unenvied anchor.

Otherwise let \(j\) be the **earliest** agent assigned a low-tier good \(g_j\). Consider any other agent \(i\). If \(v_i(g_i)=h_i\), then the tier upper bound gives \(v_i(g_i)\ge v_i(g_j)\). If instead \(v_i(g_i)=\ell_i\), then \(i\) received a low-tier good strictly *after* \(j\) because \(j\) was earliest. Thus \(i\) was still unassigned when \(g_j\) arrived. If \(i\) had valued \(g_j\) at \(h_i\), the high-tier-first rule would have assigned \(g_j\) to some unassigned high-tier agent, rather than to the low-tier recipient \(j\). Hence \(v_i(g_j)=\ell_i=v_i(g_i)\). In both cases,
\[
v_i(g_i)\ge v_i(g_j)\quad(i\ne j).
\]
This proof uses no comparison between distinct agents' numerical tier constants.

**The surplus step.** Give \(g_{n+1}\) to the anchor \(j\), so the only two-good bundle is \(A_j=\{g_j,g_{n+1}\}\) and all other bundles are \(A_i=\{g_i\}\). For every \(i\ne j\), deleting the *new* good from \(A_j\) leaves \(\{g_j\}\), whose value to \(i\) is no greater than \(v_i(g_i)\) by the lemma. Thus every other agent is EF1 toward the only non-singleton bundle. To eliminate the envy of \(j\) toward a different agent, remove that agent's single good; the comparison is with value zero. Envy between two other singleton recipients is similarly eliminated by removing the envied good. This proves EF1 at the final prefix and completes the theorem.

**Why first-phase choice matters.** Let two agents have values \(v_1=(1,2,2)\) and \(v_2=(2,1,2)\) across three arriving goods. If the first good is given to agent \(1\) and the second to agent \(2\), both agents receive a low-tier good. Whichever agent gets the third good, the other still values both goods in the two-good bundle at \(2\) while valuing their own singleton at \(1\), so EF1 fails. The high-tier-first rule instead gives the first good to agent \(2\) and the second to agent \(1\), preventing this dead end.

## Verification

The accompanying standalone source `verify_bivalued_online.cpp` checks the actual allocation rule and the EF1 inequality after **every prefix** with exact integer arithmetic. It enumerates every high/low valuation matrix for \(n=2,3,4\) and \(m=n+1\) under each of three distinct positive tier configurations, then tests \(150{,}000\) deterministic-pseudorandom instances for each \(n=5,\dots,9\), with heterogeneous positive tier values. It also independently tests the unenvied-anchor inequality. Compiling and running the packaged file produced:

```text
VERIFY_OK cases=3908208 prefix_checks=21778368
```

Reproduce by running `g++ -std=c++17 -O3 -Wall -Wextra verify_bivalued_online.cpp -o verify` followed by `./verify`. The finite program checks its stated finite domains only; the proof above, not this enumeration, establishes the theorem for arbitrary \(n\) and arbitrary real tier values.

## Relationship to prior work

Choi and Li, *Temporal Fair Division of Indivisible Goods with Scheduling* (arXiv:2601.12835, first submitted January 19, 2026), explicitly mark the status of exact temporal EF1 for bi-valued goods as an open question in their table of possibilities. Their Theorem 14 gives a multiplicative temporal-EFX bound, not exact temporal EF1. The present theorem establishes exact temporal EF1 in the natural first nontrivial horizon of one more good than agents, without buffering.

Elkind, Lam, Latifian, Neoh, and Teh, *Temporal Fair Division of Indivisible Items* (arXiv:2410.14593), prove existence for at most two **global item types** (Theorem 3.6) and for generalized binary valuations of the form \(v_i(g)\in\{0,p_g\}\) with a common good-specific nonzero value (Theorem 3.7). Neither covers arbitrary positive individualized two-tier matrices with possibly many different item-type vectors.

Wang and Wei, *Online Fair Allocations with Binary Valuations and Beyond* (arXiv:2505.24321), obtain online exact EF1 for a mixture of \(n-1\) identical binary agents and one personalized bi-valued agent (Theorem 6); their all-personalized two-agent results are weaker-factor, non-wasteful guarantees. Neither entails exact temporal EF1 for arbitrarily many personalized positive two-tier agents and one surplus good.

Amanatidis, Giaconi, Markakis, and Protopapas, *Online Fair Division Meets Reordering Buffers* (arXiv:2607.01159), achieve temporal EF1 for personalized multi-valued agents with a nonzero reordering buffer. Their statements use a different resource (deferred assignments), not the zero-buffer first-surplus algorithm here.

## Limitations

Only the horizon of at most \(n+1\) individual arrivals is established. No result is claimed for two or more surplus goods, general three-tier values, changing tier constants, or nonadditive preferences. The algorithm is not asserted to maximize welfare, be Pareto optimal, be EFX, or satisfy non-wasteful efficiency criteria stronger than allocating all arriving goods. Its tiers must be known, though their realized frequencies need not be. The proof is entirely mathematical; finite checking does not establish priority over unindexed literature, and no independent scientific audit is asserted.

## References

- Kui-Wang Choi and Minming Li, *Temporal Fair Division of Indivisible Goods with Scheduling*, arXiv:2601.12835 (first submitted January 19, 2026). https://arxiv.org/abs/2601.12835
- Edith Elkind, Alexander Lam, Mohamad Latifian, Tzeh Yuan Neoh, and Nicholas Teh, *Temporal Fair Division of Indivisible Items*, arXiv:2410.14593 (first submitted October 18, 2024). https://arxiv.org/abs/2410.14593
- Yuanyuan Wang and Tianze Wei, *Online Fair Allocations with Binary Valuations and Beyond*, arXiv:2505.24321 (first submitted May 30, 2025). https://arxiv.org/abs/2505.24321
- Georgios Amanatidis, Giulio Giaconi, Evangelos Markakis, and Nicos Protopapas, *Online Fair Division Meets Reordering Buffers*, arXiv:2607.01159 (first submitted July 1, 2026). https://arxiv.org/abs/2607.01159
