# Sharp finite-horizon EFX factor for three one-spike agents

## Finding

For every integer \(m\ge6\) and real \(H>(m-2)(m-3)\), the optimal worst-case ex-post approximate envy-freeness-up-to-any-good (EFX) factor for three agents in the online one-spike frequency-prediction model is

\[
\alpha^*(m,H)=\frac1{m-3}.
\]

A deterministic irrevocable allocation algorithm attains the factor. The upper bound applies even when the algorithm is randomized but must guarantee the factor in **every** realization. The result is a sharp, horizon-dependent quantitative counterpart to the known absence of an EFX factor uniform in the number of goods.

## Assumptions and scope

There are exactly three agents, indexed by \(i\in\{1,2,3\}\), and exactly \(m\ge6\) distinct indivisible goods, arriving in known-length chronological order. Agent \(i\)'s valuation is additive and has exactly one high-value occurrence \(H\) and \(m-1\) occurrences of value \(1\), for common \(H>(m-2)(m-3)\). High occurrences can coincide on the same good for different agents. The common frequency multiset \(\{H,1^{m-1}\}\) is known before any goods arrive, but the cross-agent alignment and order are not. An adaptive adversary may select each currently unspent value vector after observing earlier allocations; each agent's high value is used exactly once. Upon each arrival, the current vector is observed and the complete good is irrevocably assigned.

For final bundles \((A_1,A_2,A_3)\), \(\alpha\)-EFX means that for **every** ordered pair of distinct agents \(i,j\) and **every** good \(g\in A_j\),

\[
v_i(A_i)\ge\alpha\,v_i(A_j\setminus\{g\}).
\]

All goods have strictly positive value, so no zero-value deletion convention arises. Guarantees are ex-post, including after adversarial adaptation. The factor is capped at \(1\).

## Proof

**1. An online lower-bound rule.** Maintain each bundle's size, the number of goods still to arrive (including the current one), and whether a good valued \(H\) by at least two agents has arrived. Call a recipient **frozen** after the first such shared-high good is assigned to her. Because each agent has exactly one high-value occurrence, there is at most one shared-high good in any continuation after that event.

On an arrival, write \(R\) for the number of goods not yet assigned, **including** the arriving good, and \(E\) for the number of empty bundles. If \(R=E\), give the current good to an empty agent. This rule remains in force on every subsequent arrival, filling all empties with singleton bundles.

If \(R>E\) and no shared-high good has yet occurred, allocate a uniquely high good to its unique high-valuing agent. Allocate an all-low good to an already nonempty agent if one exists, and otherwise to any agent. If the current good is high for at least two agents, allocate it to an **empty** agent among its high-valuing agents, freeze that recipient, and never add another good to her bundle.

If \(R>E\) after that first shared-high event, then any newly arriving high good is high for at most one remaining agent: allocate it to that agent. Allocate an all-low good to an occupied, nonfrozen agent if possible, and otherwise to an empty, nonfrozen agent. Apply fixed index-order tie breaking throughout.

**2. Recipient and cardinality invariants.** Before the first shared-high good, all low goods are concentrated on a single recipient, while uniquely high goods are always given to their own high-valuing agents. Thus at most one agent who has not yet received her high-value occurrence has a nonempty bundle. A shared-high good is high for at least two agents whose high occurrence is still unseen, so at least one of them must be empty. The prescribed frozen recipient therefore exists. After freezing, no subsequent high good can be high for that recipient, and no second shared-high good can occur (three one-time high occurrences in total). Subsequent uniquely high goods are given to their own high-valuing agents, and all-low goods are never assigned to the frozen recipient. In the forced-fill phase \(R=E\), remaining goods are each assigned to a previously empty recipient, and such recipients stay singletons.

The count inequality \(R\ge E\) is invariant. At each assignment, \(R\) drops by one; if \(R=E\), \(E\) also drops by one. If \(R>E\), assigning to an occupied or empty recipient preserves \(R-1\ge E'\). Hence all three bundles are nonempty upon completion. Crucially, whenever the unique high good of agent \(i\) is assigned to a different agent \(j\), recipient \(j\)'s final bundle is a singleton: this can occur only with the first shared-high good assigned to a frozen recipient, or in the terminal forced-fill phase. (Any uniquely high good outside forced fill goes to its own high valuer.)

**3. EFX guarantee.** Fix distinct \(i,j\). If agent \(i\)'s high good belongs to \(A_j\), then \(A_j\) is a singleton, so every deletion leaves value zero to agent \(i\). Otherwise every good in \(A_j\) has value \(1\) to agent \(i\). Since all three bundles are nonempty, \(\lvert A_j\rvert\le m-2\), whence for every \(g\in A_j\),

\[
v_i(A_j\setminus\{g\})=\lvert A_j\rvert-1\le m-3,
\qquad v_i(A_i)\ge1.
\]

Therefore the rule guarantees \(1/(m-3)\)-EFX for all \(H\ge1\), hence in particular for the stated range.

**4. Matching adaptive upper bound.** Present \(m-2\) goods worth \(1\) to all agents. Let \(P\) be the nonempty set of agents receiving at least one such good. For the penultimate good, set value \(H\) precisely for agents in \(P\) and \(1\) for agents outside \(P\); for the final good reverse those values. Each agent then has exactly one occurrence of \(H\), and the adversary has made only a permitted dependence on the preceding allocations.

An empty final bundle forces EFX factor \(0\), because \(m\ge6\) and some other bundle has at least two positive goods. Assume all three bundles are nonempty.

If the penultimate good goes to \(p\in P\), then \(\lvert P\rvert\ge2\), because only the last good can reach an agent outside \(P\). Choose \(i\in P\setminus\{p\}\). Agent \(i\) never receives her high good, so \(v_i(A_i)\le m-2\). Agent \(p\)'s bundle contains both the penultimate high good and an early unit good; deleting that unit good leaves value at least \(H\) to agent \(i\). Thus the factor is at most \((m-2)/H\).

Otherwise the penultimate good goes to \(c\notin P\). If the last good also goes to \(c\), then choose \(i\in P\): deleting the final good from \(A_c\) leaves a high good of value \(H\) to \(i\), whereas \(v_i(A_i)\le m-2\). If the last good goes to \(p\in P\), then \(A_c\) is a singleton worth \(1\) to \(c\); the bundle of \(p\) contains an early unit good and the final good of value \(H\) to \(c\), giving factor at most \(1/H\). Finally, if the last good goes to a second agent outside \(P\), there must be only one agent in \(P\) (there are three agents altogether). This agent holds all \(m-2\) early unit goods. Agent \(c\)'s singleton has value \(1\) to her, whereas deleting one good from that large early bundle leaves value \(m-3\). Hence the factor is at most \(1/(m-3)\).

The factor in every branch is bounded by

\[
\max\left\{\frac{m-2}{H},\frac1{m-3}\right\}=\frac1{m-3},
\]

where the equality uses \(H>(m-2)(m-3)\). Combined with the policy lower bound this proves the claimed minimax equality. Because every adaptive choice depends only on an observed allocation prefix, the same upper bound applies pathwise to randomized decisions requiring an ex-post sure guarantee.

## Verification

The standalone Python 3 program `verify_one_spike.py` contains a direct implementation of the online rule, an exact-rational EFX evaluator, and an independently structured full adaptive minimax recursion. It exhausts all \(\sum_{m=6}^{15}m^3=14{,}175\) high-occurrence position triples with four heights each, checking the policy's factor and its key singleton and nonempty invariants; the recursive adversarial minimax independently confirms the exact factor for \(m=6,7,8,9,10\) at \(H=(m-2)(m-3)+1\). All checks completed successfully. These are finite regression tests; the universal theorem follows from the preceding quantified proof, not from enumeration.

Reproduction: `python verify_one_spike.py` using Python 3 standard library only. Terminal output must end with `ALL EXACT CHECKS PASSED`.

## Relationship to prior work

Neoh and Teh (2026, arXiv:2610.34625v1), Theorem 4.2 and Appendix C, prove that no fixed positive online EFX approximation exists uniformly over unbounded horizon even for the same one-high/rest-low prediction model. Their adversarial terminal construction is credited and adapted for the upper bound. Their examined theorem and proof give no constructive fixed-horizon matching lower bound or closed-form optimal value for every horizon. Neoh, Peters and Teh (2026, arXiv:2505.24503v3), Theorem 5.5 and its proof, establish the earlier general impossibility without this exact quantitative one-spike frontier. These impossibility results do not imply the asserted attainable fixed-horizon guarantee. Related smaller-horizon calculations do not imply the theorem for arbitrarily many goods.

## Limitations

The exact equality is established only for three agents with one high occurrence each and the given sufficient separation \(H>(m-2)(m-3)\); we do not claim this numerical separation is necessary or determine the full optimum for moderate \(H\). The model requires known horizon, exact frequency multisets, full current value observation and strictly positive additive valuations. The conclusion is about sure ex-post EFX, not expectation or high-probability criteria. Priority of the exact factor remains subject to independent literature review; the review here is not independent verification.

## References

- T. Y. Neoh and N. Teh, *Online Fair Division with Frequency Predictions*, arXiv:2610.34625v1, first publicly posted October 25, 2026, Theorem 4.2 and Appendix C, https://arxiv.org/abs/2610.34625.
- T. Y. Neoh, J. Peters and N. Teh, *Online Fair Division with Additional Information*, arXiv:2505.24503v3, Theorem 5.5 and appendix, https://arxiv.org/abs/2505.24503; ICML 2026, PMLR 306, https://proceedings.mlr.press/v306/neoh26a.html.
