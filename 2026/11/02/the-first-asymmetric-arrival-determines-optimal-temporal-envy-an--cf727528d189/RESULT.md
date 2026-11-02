# The first asymmetric arrival determines optimal temporal envy and the sharp cost of foresight

## Finding

**Theorem (exact prefixwise optimum and sharp two-input information gap).** Fix any integer \(m\geq 1\), two agents with additive binary valuations \(v_i(g_t)\in\{0,1\}\), and a fixed order \(g_1,\ldots,g_m\) of indivisible goods, each to be allocated irrevocably upon arrival. Write \(B_i^t\) for the goods held by agent \(i\) after round \(t\), and define the maximum pairwise envy
\[
E_t=\max\{0,\,v_1(B_2^t)-v_1(B_1^t),\,v_2(B_1^t)-v_2(B_2^t)\}.
\]
Call a good *common* if both agents value it at one, *private* if precisely one agent values it at one, and *neutral* if both value it at zero. Set
\[
T=\min\{t\in\{1,\ldots,m\}:g_t\text{ is private}\},
\]
with \(T=m+1\) when no private good exists, and let \(C_t\) be the number of common goods among the first \(t\) arrivals. There exists a **single irrevocable fully informed allocation** attaining the individual minimum of \(E_t\) for every prefix \(t\) simultaneously, with the exact profile
\[
\boxed{\min E_t=\mathbf 1\{t<T\}\,\mathbf 1\{C_t\text{ is odd}\}},\qquad 1\leq t\leq m.
\]
Consequently the minimum cumulative maximum envy, for the above fixed arrival order, is
\[
\boxed{\mathrm{OPT}=\sum_{t=1}^{T-1}\mathbf 1\{C_t\text{ is odd}\}.}
\]
The same allocation minimizes every weighted objective \(\sum_{t=1}^{m}\lambda_tE_t\) with nonnegative weights \(\lambda_t\). A scan of the input and an allocation pass take \(O(m)\) time.

In contrast, suppose an online algorithm must commit to each arriving good after seeing its two values, **without knowing future values**, although the horizon \(m\) may be known. For every \(m\geq2\), consider the two possible input sequences
\[
I_1=((1,1),(1,0),\ldots,(1,0)),\quad
I_2=((1,1),(0,1),\ldots,(0,1)),
\]
where each has exactly \(m\) goods. Both inputs have \(\mathrm{OPT}=1\) and every good has positive value to at least one agent. The exact worst-case competitive ratio **restricted to this two-input family** is \(m\) for deterministic online algorithms and \((m+1)/2\) for randomized online algorithms against an oblivious adversary, where randomization is evaluated in expectation. In particular, neither deterministic nor randomized online allocation admits an absolute constant competitive ratio over all binary two-agent inputs against such an adversary.

## Assumptions and scope

The agents' binary values need not agree: all four valuation vectors \((0,0),(1,0),(0,1),(1,1)\) are permitted. Goods are indivisible and must be given wholly to exactly one of the two agents; previously assigned goods cannot be moved. The first result has complete knowledge of the ordered value sequence before the first allocation; the online statement explicitly removes that knowledge, but permits the algorithm to know the horizon. The maximum envy \(E_t\) measures both directions using each agent's own valuation of each bundle. Nonnegative valuation is essential for the simple allocation rule; nothing here covers nonbinary utilities, more than two agents, or reallocations.

The expression \(\min E_t\) is the best value achievable for prefix \(t\) considered by itself. Simultaneous attainment means the displayed profile is achieved by one allocation of the entire ordered sequence, not a different hypothetical allocation at each prefix. When \(\mathrm{OPT}=0\), a multiplicative ratio is undefined, so the online lower bound uses inputs with \(\mathrm{OPT}=1\).

## Proof

**1. A prefix lower bound.** Before the first private good, all positively valued goods are common. Their current allocations give the same bundle value to both agents. If \(C_t\) is odd, the two integer-valued common-good counts differ by at least one, forcing \(E_t\geq1\). If \(C_t\) is even, the trivial bound \(E_t\geq0\) suffices. These bounds apply to every allocation and every prefix \(t<T\).

**2. An allocation attaining every lower bound.** Give every private good to its unique agent who values it positively; neutral goods may go arbitrarily. If there is a first private good and it benefits agent 1, allocate successive common goods alternately to agent 2 and agent 1, starting with agent 2. If the first private good benefits agent 2, reverse the order, starting with agent 1. If there is no private good, use either alternating order. The alternation counts common goods across the entire stream, even across intervening private or neutral goods.

Let \(A_t\) and \(B_t\) be the respective numbers of private goods for agents 1 and 2 already assigned to their valuers. Let \(X_t\) be the number of common goods given to agent 1 minus those given to agent 2. Directly from the definitions,
\[
E_t=\max\{0,\,-A_t-X_t,\,X_t-B_t\}.
\]
When the first private good is for agent 1, the chosen alternation gives \(X_t=0\) for even \(C_t\) and \(X_t=-1\) for odd \(C_t\). For every \(t\geq T\) we have \(A_t\geq1\), \(B_t\geq0\), and \(-1\leq X_t\leq0\), so both potential envy terms are nonpositive and \(E_t=0\). When the first private good is for agent 2, \(B_t\geq1\), \(A_t\geq0\), and \(0\leq X_t\leq1\), giving the same conclusion. Before \(T\), both private counts vanish and \(E_t=|X_t|\), which equals \(1\) exactly when \(C_t\) is odd. With no private good the same parity statement holds at all prefixes. This proves the exact pointwise formula, and hence the cumulative and nonnegative-weighted objectives. The first private good can be located in a linear scan; the explicit allocation also uses a linear pass.

**3. Exact deterministic information gap.** Fix \(m\geq2\). In both sequences \(I_1,I_2\), the first good is common. Thus a deterministic algorithm makes the same first-round choice on both inputs. If it gives the first good to agent 1, choose \(I_1\); agent 2 values only the first good, which is in agent 1's bundle, so agent 2 envies agent 1 by \(1\) at every one of the \(m\) prefixes, regardless of how the remaining goods are allocated. The same argument with agents exchanged applies if the first good is given to agent 2 and the input is \(I_2\). Every online policy therefore incurs a worst-case cost of at least \(m\) on this pair. Allocating the first good arbitrarily and all later privately valued goods to their unique valuer yields maximum envy at most \(1\) at each prefix, so its cost is at most \(m\) on the pair. By the first part, each sequence has offline optimum \(1\); hence the minimax ratio is exactly \(m\).

**4. Exact randomized information gap.** Let \(p\) denote the probability that a randomized online algorithm assigns the indistinguishable first common good to agent 1. Conditional on this event, input \(I_1\) incurs cost at least \(m\); otherwise, its cost is at least its offline optimum \(1\). Thus
\[
\mathbb E[\mathrm{cost}(I_1)]\geq1+(m-1)p.
\]
Symmetrically, \(\mathbb E[\mathrm{cost}(I_2)]\geq1+(m-1)(1-p)\). One of these two fixed inputs therefore yields expected cost at least \((m+1)/2\). This is an **oblivious** adversary because the worse sequence can be chosen from the algorithm's announced distribution without observing its random coin. Giving the initial good to each agent with probability \(1/2\), and then assigning each subsequent private good to its valuer, realizes costs \(m\) and \(1\) with probabilities \(1/2\) and \(1/2\) for either input. Its expected cost is exactly \((m+1)/2\) on both. Dividing by offline optimum \(1\) gives the claimed sharp randomized family ratio. Sending \(m\) to infinity rules out any constant global competitive factor.

## Verification

`verify_binary.py` implements exact dynamic programming on the two signed own-versus-other utility differences, not the construction described in the proof. It compares the dynamic-programming optimum, the closed formula, and the cost of the explicit common-good alternation for **all** sequences over the four value vectors of lengths \(0\) through \(8\) (a total of \(87{,}381\) ordered instances, including the empty-sequence boundary). It also checks both sharp adversarial sequences at horizons \(2\) through \(30\) and evaluates the rational expected-cost bound. Run `python3 verify_binary.py`; expected final line:

`VERIFY_OK exhaustive_binary_profiles=87381 horizon_family=2..30 worst_deterministic_ratio=m worst_randomized_minimax=(m+1)/2`

This is finite computational corroboration of the supplied general analytical proof, not a computational proof for arbitrary horizons or a claim of independent verification.

## Relationship to prior work

Goldberg, Robinson, and Teh [1] introduce cumulative maximum envy for fully informed temporal allocation. Their Proposition 1 and Appendix 0.B.1 attain every prefix's minimum under **identical** binary valuations; their Theorem 4.1 provides a general dynamic program for fixed agent count, while their Theorem 3.2 addresses variable-agent binary hardness. The result above treats **heterogeneous** binary values for two agents and gives a closed formula, a common allocation attaining all pointwise lower bounds, and an exact fully-informed versus online separation not implied by those statements.

Elkind, Lam, Latifian, Neoh, and Teh [2], especially Theorem 3.7 and Appendix B.2, provide temporal EF1 allocations for generalized binary valuations, a more general utility domain but a weaker, qualitative fairness requirement. Their EF1 bound does not force the exact zero-envy prefixes after the first private arrival or determine cumulative optimum. Wang and Wei [3] study online binary fair allocation under EF1 and MMS combined with utilitarian efficiency, rather than this exact temporal cumulative objective. Cookson, Ebadian, and Shah [4] study daily and cumulative EF1-type constraints rather than these quantitative exact costs. No claim is made that these fairness models are equivalent. Prior online vector balancing and final-round envy results, surveyed in [1], have distinct objectives and adversary guarantees.

## Limitations

The closed formula and uniform prefixwise optimality rely on exactly two agents and binary additive valuations. The online sharp ratios hold **for the specified pair of sequences** and serve as lower bounds for unrestricted online input classes; they do not characterize the global horizon-dependent online minimax ratio. Randomized lower bounds are for expected cumulative envy against an oblivious adversary, not for almost-sure performance. The proof does not resolve weighted individual cumulative envy, nonbinary values, strategyproof reporting, or proportionality constraints. Publication priority is not independently certified, and differently formulated or unindexed earlier results may exist.

## References

[1] Paul W. Goldberg, Isaac Robinson, and Nicholas Teh. *Minimizing Cumulative Envy in Allocating a Sequence of Items*. arXiv:2610.09843v1, October 7, 2026. https://arxiv.org/html/2610.09843v1

[2] Edith Elkind, Alexander Lam, Mohamad Latifian, Tzeh Yuan Neoh, and Nicholas Teh. *Temporal Fair Division of Indivisible Items*. arXiv:2410.14593v1, October 18, 2024, particularly Theorem 3.7 and Appendix B.2. https://arxiv.org/pdf/2410.14593

[3] Yuanyuan Wang and Tianze Wei. *Online Fair Allocations with Binary Valuations and Beyond*. Proceedings of AAAI 2026, DOI:10.1609/aaai.v40i20.38778. https://ojs.aaai.org/index.php/AAAI/article/view/38778

[4] Benjamin Cookson, Soroush Ebadian, and Nisarg Shah. *Temporal Fair Division*. Proceedings of AAAI 2025, DOI:10.1609/aaai.v39i13.33500. https://ojs.aaai.org/index.php/AAAI/article/view/33500
