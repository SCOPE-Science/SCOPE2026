# A sharp two-partner boundary for prefixwise online proportionality

## Finding

For online assignment of arbitrarily weighted, indivisible items with identical magnitudes for all eligible agents, an eligibility support graph of maximum **distinct-partner degree two** admits an irrevocable deterministic assignment satisfying, **at every prefix for every agent**, both the goods and chores forms of eligibility-aware proportionality up to one item (Prop1). The same assignment works for either interpretation of the items. More precisely, for every agent \(i\) and prefix \(t\),

\[
P_i(t)-b_i^-(t)\ \le\ L_i(t)\ \le\ P_i(t)+b_i^+(t).
\]

Here \(P_i(t)\) is the eligibility-aware proportional share, \(L_i(t)\) is assigned load, \(b_i^+(t)\) is the largest item assigned to \(i\), and \(b_i^-(t)\) is the largest item eligible to \(i\) but assigned elsewhere (each maximum is zero for an empty set). The upper inequality is exact chores-Prop1; the lower is exact goods-Prop1. These are **simultaneous**, not two independently chosen allocations.

This partner-degree hypothesis is sharp for deterministic online chores-Prop1: already a support **tree of maximum degree three** and seven unit items on eight agents can force failure. The latter adversarial obstruction is a contextual established rank-two lower-bound mechanism, not claimed as a new contribution; the new content is the positive simultaneous weighted all-prefix theorem on degree-two support.

## Assumptions and scope

Let \(N\) be any finite nonempty set of agents. At times \(j=1,\ldots,T\), an item with strictly positive real magnitude \(p_j\) and nonempty eligibility set \(E_j\subseteq N\) arrives; \(1\le |E_j|\le 2\), and the item must be assigned immediately and irrevocably to one member of \(E_j\). Both its magnitude and eligibility are revealed on arrival; no future information is supplied. For each two-agent eligibility set, draw the undirected edge joining its endpoints, ignoring repetitions; every vertex in this simple support graph has degree at most two. Singleton eligibility creates no edge. No bound on the number of repeated items on an edge, the magnitudes, or the number of arrivals is imposed.

For each \(t\in\{0,\ldots,T\}\) and \(i\in N\), define

\[
P_i(t)=\sum_{\substack{1\le j\le t\\i\in E_j}}\frac{p_j}{|E_j|},\qquad
L_i(t)=\sum_{\substack{1\le j\le t\\ j\text{ assigned to }i}}p_j.
\]

Define \(b_i^+(t)=\max(\{p_j:j\le t,\ j\text{ assigned to }i\}\cup\{0\})\) and \(b_i^-(t)=\max(\{p_j:j\le t,\ i\in E_j,\ j\text{ assigned elsewhere}\}\cup\{0\})\). Identical magnitude for all eligible agents is essential: this is not a theorem for arbitrary heterogeneous valuations or for eligibility sets of size three.

## Proof

**Online rule.** Maintain two nonnegative cumulative assigned loads separately for each unordered eligible pair \(e=\{u,v\}\). When the next item has eligibility exactly \(e\), give it to the endpoint with smaller *pair-specific* assigned load; break equality ties by any fixed deterministic total order. Singleton-eligible items go to their only eligible agent. Pair-specific loads are never reset. The rule can be implemented without knowing the support graph beforehand.

**Pair discrepancy lemma.** Fix a pair \(e=\{u,v\}\). At prefix \(t\), let \(Q_{u,e}\) and \(Q_{v,e}\) be the total weights of the items on \(e\) assigned to \(u\) and \(v\), respectively. Let \(B_{u,e}\) be the largest weight on \(e\) assigned to \(u\), or zero, and similarly \(B_{v,e}\). Then

\[
-B_{v,e}\le Q_{u,e}-Q_{v,e}\le B_{u,e}.
\]

This holds initially. If a weight \(p>0\) is assigned to \(u\), the rule has \(Q_{u,e}\le Q_{v,e}\) just before assignment. Thus its new difference is at most \(p\le B_{u,e}^{\mathrm{new}}\), and cannot be smaller than its former difference. Assignment to \(v\) is symmetric. Hence both bounds hold by induction after every arrival, including tie cases.

**Global two-sided inequality.** For each pair \(e\) incident to \(i\), denote by \(i_e\) the other endpoint and put \(d_{i,e}=Q_{i,e}-Q_{i_e,e}\). Singleton items contribute equally to \(P_i\) and \(L_i\). A pair item contributes half its magnitude to each endpoint's proportional share. Therefore the exact accounting identity is

\[
L_i(t)-P_i(t)=\frac12\sum_{e\ni i}d_{i,e}(t).
\]

The discrepancy lemma gives \(-B_{i_e,e}\le d_{i,e}\le B_{i,e}\). As \(i\) has at most two distinct pair neighbors, each \(B_{i,e}\le b_i^+(t)\) and each \(B_{i_e,e}\le b_i^-(t)\). Consequently

\[
-b_i^-(t)\le\frac12\sum_{e\ni i}d_{i,e}(t)\le b_i^+(t).
\]

This proves the claim for arbitrary positive real weights, all finite horizons, and every prefix. No computational experiment is used to establish these universal quantifiers.

**Sharpness of the partner bound.** For the contextual three-partner obstruction, take eight agents. Pair them into four disjoint groups and give a unit-sized item eligible to each pair; retain the four recipients. Pair these four recipients and give a unit item to each new pair; retain the two recipients. Finally give a unit item eligible to the final two recipients. This construction is adaptive to the actual decisions of any deterministic online allocator. The last recipient has received three unit items, and exactly three items are eligible to this agent. Its proportional share is \(3/2\), whereas removing its largest assigned item leaves load \(2\), violating chores-Prop1. The seven eligibility edges connect previously disjoint components into one tree, and all vertices have degree at most three. Thus a degree-three extension is impossible even on a simple tree of unit items. This lower construction is not asserted as a novel independent result.

## Verification

Run `python verify.py` using only the Python standard library. The verifier checks both inequalities at **every prefix** with doubled integer proportional shares, without floating point:

- All \(55{,}987\) item sequences through length six on a three-vertex path, with pair magnitudes drawn from \(\{1,2,5\}\).
- All \(271{,}453\) sequences through length five on a four-vertex cycle, with magnitudes drawn from \(\{1,2,3\}\).
- \(10{,}000\) seeded random sequences on a six-vertex cycle with positive integer weights and occasional singleton eligibility, through length 75.
- All \(128\) recipient-choice histories of the adaptive, seven-item, eight-agent degree-three tournament.

Exact finite tests check the implementation and small instances; the discrepancy induction and accounting identity prove the unbounded statement.

## Relationship to prior work

Biburger, Megow and Shahkarami [1] formulate the eligibility-aware share and prove optimal unrestricted deterministic online approximation orders \(\Theta(\sqrt{m})\) for chores and \(\Theta(\log m)\) for goods. Their general restrictions do not give a degree-two support guarantee in the inspected manuscript (including its sections on online algorithms and appendices). The current result imposes a **bound on distinct eligible partners per agent**, which is substantially more structural than a bound of two agents per item, and gives factor one under arbitrary positive item weights.

Sun, Wang and Li [2] develop offline proportionality for graph orientations; their Prop1 existence/algorithmic statements do not impose irrevocable online arrivals or require every prefix to be fair. Neoh and Teh [3] show online impossibility for heterogeneous valuations even if at most two agents value each good; that result does not imply impossibility under identical eligible-agent weights plus bounded support-graph degree. Li, Sun and Wang [4] study offline graphical variants of proportionality; the accessible abstract does not resolve the online weighted two-partner comparison, and full-text overlap remains a residual risk.

The degree-three tournament is consistent with existing rank-two adaptive online chore lower bounds; the contribution is not a new impossibility proof but the positive theorem and the resulting sharp degree threshold under its exact model.

## Limitations

The result does not cover an agent with three or more distinct eligible partners, eligibility sets of size three, agent-dependent item magnitudes, stronger envy-based criteria, or proportionality stronger than Prop1. The degree-three lower bound concerns deterministic online algorithms against adaptive arrivals, not randomized algorithms against an oblivious input. A literature search does not prove priority; equivalent unindexed results remain possible, and independent mathematical review is not performed.

## References

[1] J. Biburger, N. Megow and G. Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064v1 (first public 2026-10-06), https://arxiv.org/html/2610.08064v1.

[2] A. Sun, R. Wang and B. Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098 (first public 2026-02-20), https://arxiv.org/html/2602.18098v2.

[3] T. Y. Neoh and N. Teh, *Closing Gaps in Online Fair Division*, arXiv:2609.05310 (first public 2026-09-04), https://arxiv.org/abs/2609.05310.

[4] B. Li, A. Sun and R. Wang, *Settling PROPm and PROPavg in Graphical Resource Allocation*, arXiv:2610.10336 (first public 2026-10-07), https://arxiv.org/abs/2610.10336.
