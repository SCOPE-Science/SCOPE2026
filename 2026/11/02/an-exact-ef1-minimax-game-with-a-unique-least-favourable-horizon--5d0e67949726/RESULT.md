# An exact EF1 minimax game with a unique least-favourable horizon distribution

## Finding

Fix an integer \(n\ge 2\) and a real \(K>1\). Consider a family \(\mathcal I_{n,K}\) of \(2n\) finite input sequences for irrevocable, online allocation among \(n\) agents. The sequences have a common prefix of \(n-1\) unit-valued goods. A hidden target \(a\in[n]\) determines the valuation vector of the next good: \(K\) for \(a\) and \(K^{-1}\) for all other agents. The input either stops there (short) or has one final good worth \(K\) to \(a\) and one to all other agents (long). The horizon is not disclosed. The full input is fixed in advance, independently of any random choices by the allocating algorithm.

Let \(\rho_{\mathrm{EF1}}\in[0,1]\) denote the usual multiplicative envy-freeness-up-to-one-good score defined precisely below. For a required factor \(\alpha\in[0,1]\), the maximin probability, over all randomized online allocation mechanisms and all inputs in this fixed family, of obtaining \(\rho_{\mathrm{EF1}}\ge\alpha\) is exactly

\[
V_{n,K}(\alpha)=
\begin{cases}
1,&0\le\alpha\le K^{-1},\\
\dfrac{n+1}{2n},&K^{-1}<\alpha\le1.
\end{cases}
\]

For \(\alpha>K^{-1}\), the only least-favourable probability distribution on the \(2n\) inputs is the uniform distribution. More strongly, for *every* input distribution with masses \(q_{a,S},q_{a,L}\ge0\) and total mass one, the maximum expected success probability of a deterministic online algorithm is precisely

\[
F(q)=\max_{b\in[n]}\left(q_{b,S}+q_{b,L}+
\sum_{a\ne b}\max\{q_{a,S},q_{a,L}\}\right).
\]

Thus the least-favourable distribution is uniquely determined, and a randomized mechanism can equalize the success probability on *each* of the \(2n\) inputs. A deterministic algorithm has maximin success probability zero in the high-threshold regime.

## Assumptions and scope

All goods are indivisible, valuations are strictly positive and additive, and each good must be assigned immediately to exactly one agent. The number of agents \(n\) is known, but the horizon and hidden target are not known before their relevant goods arrive. The target is revealed by the distinct value \(K>1\) of the penultimate/last common-prefix-breaking good. The mechanism need only perform well on the explicitly defined finite family; this restriction is central.

For an allocation \(A=(A_1,\ldots,A_n)\) and ordered distinct agents \(i,j\), define

\[
D_{ij}(A)=v_i(A_j)-\max_{g\in A_j}v_i(g),
\]

using \(D_{ij}=0\) for an empty \(A_j\). The multiplicative EF1 score is

\[
\rho_{\mathrm{EF1}}(A)=\min_{i\ne j}
\begin{cases}
1,&D_{ij}(A)\le0,\\
\min\{1,v_i(A_i)/D_{ij}(A)\},&D_{ij}(A)>0.
\end{cases}
\]

The score is one exactly when the allocation is EF1. Its zero-value and nonzero-denominator boundary conventions are explicit. All probabilities are over internal allocation randomness, not over an adaptively selected input.

## Proof

**1. The low-threshold construction.** Choose any designated agent \(b\), allocate the initial \(n-1\) unit goods injectively to all agents other than \(b\), give the next good to \(b\), and, if a last good arrives, give it to an arbitrary previously occupied agent \(c\ne b\). Every short allocation consists of singletons and is EF1.

For a long allocation, every non-target agent other than \(b\) holds at least one unit-valued prefix good, so after deletion of the most valued good from any other bundle that agent never faces residual value greater than one. The non-target \(b\) holds the special good worth \(K^{-1}\) and sees at most one unit of residual value in the sole doubleton \(A_c\). A target agent holding a prefix good sees residual value at most one in that doubleton, even when the last good has value \(K\). If the target is \(b\), its own special good is worth \(K\) and likewise covers all residual values. Thus every directed comparison has score at least \(K^{-1}\), proving \(V_{n,K}(\alpha)=1\) when \(\alpha\le K^{-1}\).

**2. A target-specific short/long conflict.** Now fix \(\alpha>K^{-1}\). Consider a deterministic algorithm. If its first \(n-1\) prefix goods are not assigned to distinct agents, two agents are still empty. The next good can fill at most one of those empty bundles, leaving an empty agent who values two goods in a different agent's bundle at one each. That agent has zero EF1 score on every short input. The algorithm's total success probability against distribution \(q\) is then at most \(\sum_a q_{a,L}\).

Otherwise the prefix goods have distinct recipients, with a unique initially empty agent \(b\). If the target \(a=b\), at most the two corresponding inputs can succeed. Fix \(a\ne b\). If the next special good is not given to \(b\), \(b\) remains empty and some other bundle contains at least two positive goods; hence the short input has score zero. If the special good is given to \(b\), the short input is EF1, but on the long input no placement of the last good achieves score above \(K^{-1}\). Indeed, giving it to \(b\) leaves target \(a\) with a unit good against a doubleton of two goods worth \(K\) each; giving it to any \(j\ne b\) leaves \(b\) with own utility \(K^{-1}\) facing a doubleton worth two units to \(b\). This proves at most one success among the two horizons for each \(a\ne b\).

**3. Exact best response to every prior on inputs.** With the injective prefix and empty agent \(b\), if \(a=b\) assign the special good to \(b\) and the final good (if any) to any \(c\ne b\); both horizons are EF1. If \(a\ne b\), a short-mode choice assigns the special good to \(b\) and wins on the short input; a long-mode choice assigns the special good to \(a\), then (if present) the final good to \(b\), and wins on the long input. The latter long allocation has a singleton of value one for \(b\), a doubleton of value \(1+K\) for \(a\), and other unit singletons; checking directed pairs shows it is EF1. These decisions can be made when the special good arrives because its value vector reveals \(a\), without revealing which horizon will occur.

Thus an algorithm choosing \(b\) and the more likely horizon for each \(a\ne b\) attains exactly

\[
q_{b,S}+q_{b,L}+\sum_{a\ne b}\max\{q_{a,S},q_{a,L}\}.
\]

The repeated-prefix upper bound is no better, since the displayed expression is at least \(\sum_a q_{a,L}\). Maximizing over \(b\) proves the exact formula for \(F(q)\), for *all* probability distributions, including those with zero masses.

**4. Unique least-favourable distribution.** Put \(r_a=q_{a,S}+q_{a,L}\), \(d_a=|q_{a,S}-q_{a,L}|\), and \(D=\sum_a d_a\). Then

\[
F(q)=\frac{1+D+\max_b(r_b-d_b)}2
\ge\frac{1+D+(1-D)/n}{2}
\ge\frac{n+1}{2n}.
\]

For \(n\ge2\), equality in the last inequality forces \(D=0\), and equality in the averaging bound then forces every \(r_b=1/n\). These conditions uniquely give \(q_{a,S}=q_{a,L}=1/(2n)\). Conversely, the uniform distribution yields \(F(q)=(n+1)/(2n)\). It is therefore the unique least-favourable distribution in the high-threshold regime.

**5. An equalizing randomized algorithm.** Select \(b\) uniformly from the agents and allocate the first \(n-1\) goods injectively to the other agents. When the target \(a\) appears, give the special good to \(b\) if \(a=b\). Otherwise, flip a fair coin between short and long mode as described in Step 3. Conditional on \(a=b\), both horizons succeed; conditional on \(a\ne b\), the chosen mode succeeds on its corresponding horizon and fails on the opposite one at threshold \(\alpha>K^{-1}\). Each input consequently has success probability

\[
\frac1n+\left(1-\frac1n\right)\frac12=\frac{n+1}{2n}.
\]

The uniform input distribution bounds any randomized algorithm above by the same value, by averaging deterministic policies obtained from fixed random tapes. Hence the randomized maximin value is exact. Every deterministic policy has at least one unsuccessful input at this threshold, proving the deterministic maximin value zero.

## Verification

Run `python verify.py` with Python 3.10 or newer. The program uses exact rational arithmetic and independently checks the proposed equalizing mechanism for agent counts \(2\) through \(8\) and several values of \(K\). It also exhaustively enumerates every possible prefix recipient sequence and every feasible later decision for agent counts \(2,3,4\), checking the exact best-response formula for uniform and nonuniform input distributions, above and below the threshold. Expected output begins `VERIFY_OK` and reports 280 equalizer-input checks and 90 exhaustive weighted policy games.

These finite enumerations are **not** a proof for unbounded \(n\) or real \(K\); the proof above uses exact inequalities and online information constraints and is independent of the test ranges.

## Relationship to prior work

Tianqi Chen and Jingxiao Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness* (first available September 20, 2026; arXiv:2609.23577), Theorem 4.3, introduce precisely the \(2n\)-input short/long family and prove an upper bound of \((n+1)/(2n)\) for the success probability of arbitrary randomized online algorithms on unrestricted inputs. Their proof chooses uniform target and horizon and bounds the number of successful inputs of each deterministic rule. The current theorem does **not** claim that their general upper bound is attainable across all online inputs: it solves the finite adversarial-family game, provides a matching equalizing online algorithm, determines the optimal response to an arbitrary distribution, proves uniqueness of the optimal adversarial distribution, and resolves the exact threshold in the EF1 factor.

Tzeh Yuan Neoh and Nicholas Teh, *Closing Gaps in Online Fair Division* (first available September 4, 2026; arXiv:2609.05310), studies broad impossibility results and approximations for online fairness, but does not establish this finite-family minimax or unique-distribution formula. Standard finite zero-sum minimax reasoning is background; no novelty is claimed for the general minimax principle.

## Limitations

The exact game value belongs only to the specific finite short/long family. It does not identify the best possible randomized EF1 success guarantee over all online fair-division instances, which may be strictly lower. It assumes strictly positive valuations, additive utility, no preannouncement of the horizon, and the threshold score given above. The claimed originality is subject to the possibility of unindexed or differently phrased work on the same finite family. Independent external verification has not been performed.

## References

1. T. Chen and J. Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, 2026, arXiv:2609.23577, especially Section 4.2 and Theorem 4.3. https://arxiv.org/abs/2609.23577
2. T. Y. Neoh and N. Teh, *Closing Gaps in Online Fair Division*, 2026, arXiv:2609.05310. https://arxiv.org/abs/2609.05310
