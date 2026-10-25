# A sharp online proportionality threshold for forest eligibility graphs

## Finding

Let \(n\ge 1\) agents receive a stream of unit-valued indivisible goods, each eligible for precisely two distinct agents. Every arriving good must immediately and irrevocably be allocated to one of its two eligible agents. Assume the cumulative graph whose vertices are agents and whose edges are the goods is a forest after every arrival. For agent \(v\) at prefix \(s\), let \(d_v(s)\) be the number of goods for which \(v\) was eligible and \(a_v(s)\) the number awarded to \(v\), and define the signed proportionality deficit
\[
B_v(s)=d_v(s)-2a_v(s).
\]
For every integer \(0\le t\le n-1\), the exact deterministic adaptive-adversary minimax deficiency is
\[
\inf_{\mathcal A}\ \sup_{\mathcal S}\ \max_{0\le s\le t}\max_{v\in[n]}B_v(s)
=\left\lfloor\log_2(t+1)\right\rfloor,
\]
where \(\mathcal A\) ranges over online allocation rules and \(\mathcal S\) over adaptive forest-preserving streams of exactly \(t\) arrivals. The upper bound is attained by assigning each new good to the endpoint with the larger current signed deficit, breaking ties arbitrarily. The lower bound is forced against every online rule by a binary merging adversary, irrespective of advance knowledge of \(n\) or \(t\).

In the eligibility-aware goods sense of proportionality up to one good (Prop1), the allocation at a prefix is Prop1 precisely when \(B_v(s)\le 2\) for all agents. Consequently, an irrevocable online rule maintains Prop1 at **every prefix of every forest stream on at most seven agents**, while on **eight agents an adaptive adversary forces a failure after exactly seven goods**, all forming a tree. No forest stream with fewer than seven goods can force such a failure under the stated greedy rule.

## Assumptions and scope

The agent set is fixed and finite; goods are desirable, identical, and of unit value. Every good has an eligibility set of size exactly two; every good is allocated to an eligible endpoint on arrival and cannot subsequently move. The adversary may select later eligible pairs after seeing previous allocations. The union of all observed eligibility edges is simple and acyclic, so an arriving edge always connects different connected components. Isolated agents are allowed. The objective takes the maximum **positive** signed deficit at any prefix; it is not the maximum of the absolute deficit. Ties may be resolved in any way. The stated minimax equation is for deterministic online policies, although the adaptive construction forces its lower bound pathwise against any realized randomized decisions that it observes.

For unit goods, the eligibility-aware proportional share of agent \(v\) is \(d_v(s)/2\). Prop1 means that either \(a_v(s)\ge d_v(s)/2\), or a single eligible good allocated elsewhere would suffice to reach that share if hypothetically added. The latter good exists whenever \(a_v(s)<d_v(s)/2\). Thus Prop1 is equivalent to \(a_v(s)+1\ge d_v(s)/2\), or \(B_v(s)\le 2\). This equivalence concerns **goods**, not chores.

## Proof

**Upper bound.** Initially all signed deficits are zero. An arriving edge \(uv\) increments the signed deficit of its losing endpoint by one and decrements that of its receiving endpoint by one. The greedy rule selects the receiving endpoint with larger (or equal) prearrival deficit.

We prove the invariant: at every prefix, if a vertex \(w\) in a connected component \(C\) has positive deficit \(B_w=r\ge1\), then \(\lvert C\rvert\ge2^r\). It holds initially. When an edge joins distinct prior components, all unchanged vertices retain their deficits while their components can only grow; the receiving vertex's deficit falls. It remains to check the losing vertex \(w\) if its updated deficit becomes a positive integer \(r\). Before insertion it had deficit \(r-1\), while the receiving endpoint \(z\) had deficit at least \(r-1\), by the greedy choice. When \(r=1\), the new component contains both distinct endpoints and thus at least \(2\) vertices. When \(r\ge2\), both prior deficits are positive and the induction hypothesis places \(w\) and \(z\) in disjoint components of at least \(2^{r-1}\) vertices each. Their union therefore has at least \(2^r\) vertices. This establishes the invariant without restricting tie-breaking.

A forest with \(s\) edges has every connected component of size at most \(s+1\): its connected components are trees, each requiring one fewer edge than vertices. Hence positive deficits at prefix \(s\) satisfy \(B_v(s)\le\lfloor\log_2(s+1)\rfloor\), and for all \(s\le t\) the upper bound follows. The argument also covers \(t=0\) and isolated vertices.

**Adaptive lower bound.** For each integer \(r\ge0\), inductively construct a forest stream on exactly \(2^r\) fresh agents with \(2^r-1\) goods and mark an agent whose final signed deficit is exactly \(r\), irrespective of the decisions of the allocation rule. For \(r=0\), take a single isolated agent with deficit zero. Given two disjoint level-\((r-1)\) constructions, both ending with a marked agent of deficit \(r-1\), offer one additional good eligible for exactly the two marked agents. This new edge connects different tree components, so acyclicity is preserved. Whichever marked agent does **not** receive the good acquires deficit \(r\); designate it as the new marked agent. The resulting graph is one tree on \(2^r\) vertices, with exactly \(2^r-1\) edges. All choices of which agent receives any good are permitted and are accounted for. Thus no irrevocable algorithm can prevent a deficit of \(r\) at that prefix.

Set \(r=\lfloor\log_2(t+1)\rfloor\), so \(2^r\le t+1\le n\) and \(2^r-1\le t\). Apply the level-\(r\) adversary, then, if necessary, append arbitrary forest-preserving edges among the remaining disconnected components to reach exactly \(t\) edges. At least \(n-t\ge1\) components remain, and such extensions are possible as long as fewer than \(n-1\) edges have arrived. The witnessed deficit persists in the **prefix maximum**, even if later assignments alter that marked agent's deficit. This proves the lower bound and the minimax identity.

**Sharp fairness cutoff.** Every stream on \(n\le7\) agents has at most \(n-1\) edges, so the greedy upper bound is at most \(\lfloor\log_2 n\rfloor\le2\), precisely Prop1. For \(n=8\), the level-three adversary gives a forest with seven edges and a vertex of deficit three, violating Prop1. Conversely, under the greedy rule any forest prefix with at most six edges has maximum deficit at most \(\lfloor\log_2 7\rfloor=2\); hence fewer than seven goods cannot force a violation against that rule. This completes the sharp threshold proof.

## Verification

The standalone file `checker.py` implements an exact minimax game-state recursion for all horizons \(0\le t<n\) and agent counts \(2\le n\le6\). At every forest state, it lets the adversary choose any bridge and the allocator choose either endpoint, with the payoff equal to the largest signed deficit across all prefixes. The program checks its resulting values against the closed formula. It also constructs the binary adversarial trees at levels one through four under three different response policies, and checks the component-size invariant for the greedy orientation of those trees. These finite checks corroborate, but do not replace, the general inductive proof. Run `python3 checker.py` from this directory; no third-party dependencies are required.

## Relationship to prior work

Biburger, Megow and Shahkarami's 2026 online eligibility-constrained fair-division work defines the same eligibility-aware proportional share, proves logarithmic-factor approximate Prop1 in general goods instances, and describes failure of unscaled deficit-greedy in general instances (Appendix C.1). It does not state the exact forest-prefix minimax value or the seven/eight-agent Prop1 threshold. Its general approximation theorem does not imply exact Prop1 under forest structure.

Bender and collaborators (2021) consider online forest edge orientation. Their no-flip orientation toward a larger tree gives logarithmic maximum **outdegree**; because signed deficit is outdegree minus indegree, this already supplies a related forest upper bound after translation. We do not claim that a logarithmic forest upper bound by itself is new. Their stated goal, however, is outdegree and edge-reorientation tradeoffs; the adaptive lower matching our **signed-deficit** upper bound and the resulting **eligibility-aware Prop1 impossibility threshold** are different assertions. Gupta and collaborators (2021/2022) study graph discrepancy with recourse; their constant forest bound in Section 5.4 allows path reversals and does not provide an irrevocable allocation. Sun, Wang and Li (2026) address existence and computation of fair orientations offline, not the irrevocable prefix game. The fully adaptive forest lower construction also differs from unrestricted multigraph counterexamples, which may reuse eligible pairs.

## Limitations

The theorem does not extend as stated to cycles, repeated eligibility pairs, goods of unequal value, hyperedge eligibility, or chores. The minimax objective is one-sided shortfall, not two-sided absolute graph discrepancy; the latter is not controlled by the same greedy rule. The lower bound assumes the adversary observes assignments, while a lower bound against an oblivious adversary requires separate analysis. The argument does not claim that every greedy execution attains the upper bound or that every forest orientation is fair; it gives one guaranteed online rule and an adversarial obstruction applicable to all online rules. Established forest-orientation doubling arguments are an important antecedent to the upper-bound technique. The scientific claim has not undergone an independent audit.

## References

1. Joes Biburger, Nicole Megow, and Golnoosh Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064, first posted 2026-10-06, https://arxiv.org/abs/2610.08064 .
2. Michael A. Bender et al., *Incremental Edge Orientation in Forests*, arXiv:2107.02318, first posted 2021-07-05, https://arxiv.org/abs/2107.02318 .
3. Anupam Gupta, Vijaykrishna Gurunathan, Ravishankar Krishnaswamy, Amit Kumar, and Sahil Singla, *Online Discrepancy with Recourse for Vectors and Graphs*, arXiv:2111.06308, 2021 preprint; SODA 2022, https://arxiv.org/abs/2111.06308 .
4. Ankang Sun, Ruijie Wang, and Bo Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098, 2026, https://arxiv.org/abs/2602.18098 .
