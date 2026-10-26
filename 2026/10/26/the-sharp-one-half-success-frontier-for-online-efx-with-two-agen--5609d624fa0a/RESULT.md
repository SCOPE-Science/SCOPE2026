# The sharp one-half success frontier for online EFX with two agents and three goods

## Finding

**Theorem.** Two agents receive exactly three indivisible goods sequentially. Upon each arrival, the allocator observes the singleton value of the arriving good for both agents and irrevocably assigns it to one of them. Each agent's valuation is any nonnegative monotone set function vanishing at the empty set, and both agents' valuations and the arrival order are fixed independently of the allocator's random choices. The allocator knows only that three goods will arrive, not their future values.

Let the success event be that the **final complete allocation** is envy-free up to any good (EFX), using the removal-of-every-good definition, including goods of zero value. Then the exact optimal worst-case success probability of randomized online allocation is

\[
\sup_{\mathcal A}\inf_{I:\,|N|=2,\,|G|=3}
\Pr\bigl[\mathcal A(I)\text{ is EFX}\bigr]
=\frac12.
\]

An explicit online rule attains the lower bound using only comparisons of observed singleton values. The upper bound is witnessed by a pair of strictly positive additive instances with identical information at the first arrival. With at most two goods, assigning each good to a different agent guarantees EFX deterministically, so the third good is the first possible obstacle for two agents.

## Assumptions and scope

Write the arriving goods as \(g_1,g_2,g_3\) and the agents as \(1,2\). Every valuation \(v_i:2^{\{g_1,g_2,g_3\}}\to\mathbb R_{\ge0}\) is normalized at the empty set, \(v_i(\varnothing)=0\), and monotone: \(S\subseteq T\) implies \(v_i(S)\le v_i(T)\). No additivity, submodularity, or positive singleton-value assumption is made for the achievable guarantee. No normalization of the total value \(v_i(G)\) is assumed. The online information at arrival \(t\) consists of \(v_1(\{g_t\})\) and \(v_2(\{g_t\})\), in addition to past observations and decisions. Randomness is private to the allocator and independent of the fixed input.

An allocation \((A_1,A_2)\) is **EFX** if, for both distinct agents \(i,j\) and every \(g\in A_j\),
\[
 v_i(A_i)\ge v_i(A_j\setminus\{g\}).
\]
This is the strong, any-good condition, including zero-value removal goods. The guarantee is assessed at the final third arrival; it does not assert fairness after every prefix. A randomized rule may know the horizon of three arrivals but is given no prediction of future singleton values.

**Elementary completion lemma.** If a final allocation has one agent \(i\) holding one good \(g_s\) and the other agent holding the two remaining goods \(g_a,g_b\), it is EFX if and only if
\[
 v_i(\{g_s\})\ge\max\{v_i(\{g_a\}),v_i(\{g_b\})\}.
\]
Indeed, the singleton holder's two EFX inequalities are exactly these two comparisons. The two-good holder's comparison to the singleton holder leaves the empty set after removal, so it is automatic by nonnegativity. This characterization is valid for all valuations in the stated class and needs no joint-bundle values.

## Proof

**The attaining online rule.** Order singleton goods for each agent by decreasing value, breaking ties in favor of the earlier-arriving good. This produces a strict order without changing any weak value comparison. At the first arrival, give \(g_1\) to a uniformly random agent \(R\). At the second arrival, compare \(g_1\) with \(g_2\) in each agent's refined order. If the agents disagree, give \(g_2\) to the agent preferring \(g_2\). If they agree, give \(g_2\) to an independently and uniformly random agent, regardless of \(R\).

At the third arrival, complete to a one-good/two-good allocation: if the first two goods have the same owner, give \(g_3\) to the other agent; if they have different owners, inspect the two possible third-good recipients and select one making the final allocation EFX whenever one exists. The completion lemma shows that these tests require only the three singleton values already revealed for each agent. When neither completion succeeds, choose either recipient arbitrarily.

Let \(T_i\in\{g_1,g_2,g_3\}\) be agent \(i\)'s unique favorite under the strict tie refinement. If the singleton held by agent \(i\) equals \(T_i\), the completion lemma guarantees EFX. Moreover, any EFX certificate established using the strict refinement is valid under the underlying weak valuations.

**Case 1: the two agents agree on which of the first two goods is better.** Denote their common preferred good by \(t\in\{g_1,g_2\}\). Since both strictly prefer \(t\) to the other of these two goods, each \(T_i\) belongs to \(\{t,g_3\}\). The first and second assignments are independent fair choices, so each of the four prefix recipient pairs \((1,1),(1,2),(2,1),(2,2)\) occurs with probability \(1/4\).

For each of the two **split** prefixes, the agent holding \(t\) is a singleton holder after the third good is assigned to the other agent; that completion succeeds whenever this agent favors \(t\) globally. For each of the two **same-recipient** prefixes, the agent initially holding nothing receives \(g_3\) as a singleton; that completion succeeds whenever this agent favors \(g_3\) globally. If both agents favor \(t\), both split prefixes succeed. If both favor \(g_3\), both same-recipient prefixes succeed. If one favors \(t\) and the other \(g_3\), one split prefix and one same-recipient prefix succeed. Hence at least two of the four equally likely prefixes admit an EFX completion, and success probability is at least \(1/2\).

**Case 2: the agents disagree.** Relabel agents, if necessary, so agent \(1\) strictly prefers \(g_1\) to \(g_2\), while agent \(2\) strictly prefers \(g_2\) to \(g_1\). The rule gives \(g_2\) to agent \(2\). In the first, probability-\(1/2\) branch, \(g_1\) went to agent \(1\), giving a split prefix. If \(T_1=g_1\), give \(g_3\) to agent \(2\), leaving agent \(1\) her favorite singleton; EFX follows. In the second, probability-\(1/2\) branch, \(g_1\) went to agent \(2\), so agent \(1\) receives \(g_3\) as singleton. This is EFX if \(T_1=g_3\). Because agent \(1\) prefers \(g_1\) to \(g_2\), her overall favorite is necessarily either \(g_1\) or \(g_3\); at least one of the two branches succeeds. Again the lower bound is \(1/2\).

**Matching upper bound.** Consider two additive inputs with strictly positive singleton-value matrices (rows are agents, columns are the three arrivals):
\[
 I^{(1)}:
 \begin{pmatrix}
 1/4 & 1/16 & 1/16\\
 1/4 & 1 & 1
 \end{pmatrix},
 \qquad
 I^{(2)}:
 \begin{pmatrix}
 1/4 & 1 & 1\\
 1/4 & 1/16 & 1/16
 \end{pmatrix}.
\]
The first good has identical reported value \(1/4\) to both agents on both inputs, so every randomized online rule uses the same first-allocation distribution on these two fixed inputs. On input \(I^{(1)}\), every EFX allocation **must** assign \(g_1\) to agent \(1\). To prove this, suppose instead that \(g_1\) goes to agent \(2\). If agent \(1\) receives neither later good, she has zero utility, while agent \(2\)'s bundle still contains positive value after removal of any one good, violating EFX. If agent \(1\) gets both later goods, agent \(2\) has singleton \(g_1\) of value \(1/4\) and envies the pair with either good removed, because each later good is worth \(1\) to agent \(2\). If agent \(1\) gets exactly one later good, she values her singleton at \(1/16\) while agent \(2\)'s pair still contains \(g_1\) of value \(1/4\) after deleting its other good. These exhaust the possibilities and contradict EFX in every case.

By agent symmetry, every EFX allocation on \(I^{(2)}\) must give \(g_1\) to agent \(2\). Let \(p\) be an arbitrary algorithm's probability of giving \(g_1\) to agent \(1\) upon seeing the common first-arrival vector. Its success probabilities on \(I^{(1)}\) and \(I^{(2)}\) are at most \(p\) and \(1-p\), respectively; one is therefore at most \(1/2\). The two instances are selected before the algorithm's randomness, so the argument applies to an oblivious adversary. Together with the attaining rule this proves the theorem.

## Verification

The standalone `verify_efx.py` checks the online rule by exact rational arithmetic, using a direct EFX predicate independent of the proof's singleton characterization. It exhausts all \(4^6=4096\) ordered two-agent triples of additive singleton values in \(\{0,1,2,3\}\) and finds minimum success probability \(1/2\). It also checks all \(6^2=36\) pairs of strict rankings and all \(3^6=729\) pairs of nonadditive maximum-singleton monotone set functions with singleton weights in \(\{0,1,2\}\). Both additive upper-bound witnesses are checked against all \(2^3=8\) final assignments. The script reports `ALL EXACT CHECKS PASSED` when run with standard Python 3.

These finite checks are corroborating tests. Universal correctness for all real singleton values and all normalized monotone set functions follows from the two-case argument and the elementary completion lemma, not from finite enumeration.

## Relationship to prior work

Cohen, Teh and Wooldridge (arXiv:2609.28333, Theorem 5.4 and its proof) establish, for any number \(n\ge2\) of agents and exactly \(n+1\) arriving goods, an upper bound of \(1/n!\) and an algorithm achieving at least \(2/((n+1)n!)\) exact EFX success probability against an oblivious adversary. Their stated results specialize for two agents to the interval \([1/3,1/2]\). The theorem here supplies the missing matching online lower bound \(1/2\) at two agents and three goods; it does not claim the paper's general upper bound as new.

Chen and Long (arXiv:2609.23577) prove arbitrarily small EFX success probability in their unknown/unrestricted-horizon fully online model. Their result does not imply arbitrarily small success for the fixed, known three-good horizon here. Neoh and Teh (arXiv:2504.03951) count **offline** EFX allocations with full advance information, which does not imply the above online randomized probability. Melissourgos and Protopapas (arXiv:2508.04779) study deterministic EFX guarantees with and without predictive advice, rather than this fixed-horizon minimax success probability. These distinctions are about claim implications, not superficial differences of terminology.

## Limitations

The conclusion is for exactly two agents, exactly three goods, full revelation of every arriving good's **singleton** values to the allocator, and a fixed oblivious input. It does not claim EFX at intermediate arrival times, ex-ante envy-freeness, strategic incentive compatibility, Pareto efficiency, a comparable constant for larger markets, or a guarantee against an adaptive adversary that observes random choices. A rule restricted to learning only a single agent's value, or forbidden from using the known horizon, would require new analysis. The matching impossibility construction is additive and strictly positive, whereas the policy's success lower bound extends to all nonnegative monotone set functions. The priority of a mathematical conclusion against unindexed historical literature cannot be absolutely certified by a finite literature search.

## References

1. Saar Cohen, Nicholas Teh, and Michael Wooldridge, *Online Fair Division Against an Oblivious Adversary*, arXiv:2609.28333 (first posted 2026-09-23), especially §5.3, Theorem 5.4 and proof. https://arxiv.org/abs/2609.28333
2. Tianqi Chen and Jingxiao Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, arXiv:2609.23577 (2026), especially the EFX probability result. https://arxiv.org/abs/2609.23577
3. Tzeh Yuan Neoh and Nicholas Teh, *Understanding EFX Allocations: Counting and Variants*, arXiv:2504.03951 (2025), EFX allocation counting. https://arxiv.org/abs/2504.03951
4. Themistoklis Melissourgos and Nicos Protopapas, *Online EFX Allocations with Predictions*, arXiv:2508.04779 (2025). https://arxiv.org/abs/2508.04779
