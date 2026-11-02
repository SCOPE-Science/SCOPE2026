# The exact eligibility-rank frontier for online chore proportionality up to one item

## Finding

**Theorem (sharp fixed-rank online threshold).** Fix an integer \(r\ge 1\). Consider any finite sequence of irrevocably allocated chores, each with positive size \(p_j\) and a nonempty eligibility set \(S_j\) of agents with \(1\le |S_j|\le r\). Eligible agents have the same cost for each chore. For an allocation \(\sigma\), write

\[
L_i=\sum_{j:\sigma(j)=i}p_j,\qquad
P_i=\sum_{j:i\in S_j}\frac{p_j}{|S_j|},\qquad
b_i=\max\bigl(\{p_j:\sigma(j)=i\}\cup\{0\}\bigr).
\]

For every deterministic irrevocable online algorithm, and every \(\alpha<r\) with \(\alpha\ge1\), some finite adaptive instance has an agent with \(L_i-b_i>\alpha P_i\), provided \(r\ge2\). Conversely, **every** feasible allocation of every instance satisfies \(L_i-b_i\le rP_i\) for all agents, even at every arrival prefix. Therefore the least uniform deterministic online approximation factor for eligibility-aware chore \(\mathrm{Prop1}\), over arbitrarily many agents and arrivals but fixed maximum eligibility cardinality \(r\), is **exactly \(r\)**. For \(r=1\), the factor is \(1\).

The lower bound for each \(r\ge2\) holds with **unit-size chores, eligibility sets of size exactly \(r\), and a simple Berge-acyclic connected eligibility hypergraph**. For \(r=2\), the resulting eligibility graph is a tree.

## Assumptions and scope

The algorithm initially knows the rank bound \(r\), and may know the number of agents and total number of future chores, but not future eligibility sets. Each revealed chore must immediately and permanently be given to an eligible agent. An adaptive adversary chooses subsequent eligibility sets after observing past allocations. No restriction is imposed on the number of agents; the guarantee is uniform in that number. A ratio is interpreted through the inequality \(L_i-b_i\le\alpha P_i\), which avoids division by zero. An agent with \(P_i=0\) is never assigned a chore and satisfies the inequality automatically. Approximation factors are by convention at least \(1\).

Here a hypergraph is Berge-acyclic if its bipartite incidence graph has no cycle. This is stronger than merely forbidding repeated eligibility sets. Our construction gives a connected incidence tree, hence a Berge tree.

## Proof

**Universal upper bound.** For every assigned chore \(j\) with \(\sigma(j)=i\), the cardinality bound gives

\[
p_j\le r\frac{p_j}{|S_j|}.
\]

Sum only over chores assigned to \(i\), then use positivity to include all other chores for which \(i\in S_j\). Thus \(L_i\le rP_i\). Since \(b_i\ge0\), also \(L_i-b_i\le rP_i\). The argument works separately on each prefix, for every allocation rule. For \(r=1\), eligibility forces a unique recipient for every chore and \(L_i=P_i\), so the conventional optimal factor is \(1\).

**Adversary at height \(h\).** Fix \(r\ge2\) and integer \(h\ge2\). Start with \(r^h\) distinct agents, all designated level-zero champions. At level \(\ell\) (initially \(\ell=0\)), partition the current champions into disjoint groups of exactly \(r\). For each group release one unit-size chore whose eligibility set is precisely its \(r\) champions. Whatever eligible recipient the algorithm selects becomes that group's champion for the next level. Continue for \(h\) levels until only one champion \(w\) remains. The total number of chores, \((r^h-1)/(r-1)\), is fixed in advance and independent of the algorithm's choices.

Inductively, every level-\(\ell\) champion has received exactly \(\ell\) chores, has belonged to exactly \(\ell\) released eligibility sets, and is the only champion of its component of the already revealed eligibility hypergraph. At a new group, its \(r\) champions belong to distinct components. The new chore joins those components, and its recipient has one additional chore and one additional eligibility incidence. This proves the induction, including the disjointness needed at the next level.

The final champion \(w\) consequently has

\[
L_w=h,\qquad b_w=1,\qquad P_w=\frac{h}{r},\qquad
\frac{L_w-b_w}{P_w}=r\Bigl(1-\frac1h\Bigr).
\]

For any \(\alpha<r\), take an integer \(h>r/(r-\alpha)\). Then \(r(1-1/h)>\alpha\), violating \(\alpha\)-\(\mathrm{Prop1}\). This works against every deterministic algorithm because the adversary reacts only to the actual recipient of each previously revealed chore.

**Acyclicity.** Initially every agent is an isolated component. Every new hyperedge has one vertex in each of \(r\) distinct previous components, so adding its incidence node connects those components without creating an incidence-graph cycle. At termination it has connected all agents. Since each job joins \(r\) previously disconnected components, the constructed hypergraph is simple and Berge-acyclic; for \(r=2\) it is a simple tree. This finishes the proof.

## Verification

The accompanying standalone script `verify_rank.py` uses exact rational arithmetic. It tests the universal upper bound on 1,000 reproducible variable-size random profiles; constructs the recursive adversary for ranks \(2,3,4,5\), including height \(11\) at rank \(2\); checks the incidence-forest invariant by disjoint-set unions; and exhaustively enumerates all recipient choices for selected small tournament instances, including all \(32{,}768\) paths at rank \(2\), height \(4\). These experiments confirm the formulas on tested instances. The arbitrary-size conclusion depends on the induction and inequalities above, not on finite testing.

To reproduce: `python3 verify_rank.py` (Python standard library only).

## Relationship to prior work

Biburger, Megow and Shahkarami (arXiv:2610.08064, Section 3 and Appendix B) formulate the same eligibility-aware share and prove the unrestricted deterministic online bound \(\Theta(\sqrt m)\), where \(m\) is the number of agents. Their lower-bound instance uses eligibility sets of increasing size; their algorithm can process small-eligibility chores trivially. The precise fixed-cardinality frontier \(r\), its matching adaptive tournament lower bound, and the Berge-tree restriction are not part of those results. The direct small-cardinality upper inequality alone would not prove sharpness.

Sun, Wang and Li (arXiv:2602.18098) establish offline fair-orientation existence and complexity results under relevance constraints, including the rank-two graph setting, but not this online minimax factor. Bansal and coauthors (arXiv:2604.04159) study online graph balancing against an offline maximum-load benchmark (especially independent random arrivals), rather than proportional share at each vertex; its competitive statements do not imply this local fairness factor. Classical online load-balancing lower-bound constructions are conceptually related, so source priority beyond the inspected literature remains a limitation.

## Limitations

The lower bound uses an adaptive adversary and establishes an impossibility for deterministic algorithms (also for pathwise randomized guarantees under an adversary that observes choices). It is not a lower bound for expected fairness against oblivious inputs. The result assumes identical positive chore sizes on eligible agents, cardinality-bounded eligibility, and arbitrarily many agents. For a fixed number of agents or additional structural/predictive information, smaller factors may be possible. The prefixwise upper bound is universal; no online algorithm with a uniquely favorable strategy is asserted. This statement is not a claim of priority against unindexed literature. Independent expert validation has not been performed.

## References

1. Joes Biburger, Nicole Megow and Golnoosh Shahkarami, *Online Fair Division under Eligibility Constraints*, arXiv:2610.08064 (first public 2026-10-06). https://arxiv.org/abs/2610.08064
2. Ankang Sun, Ruijie Wang and Bo Li, *Fair Orientations: Proportionality and Equitability*, arXiv:2602.18098 (first public 2026-02-20). https://arxiv.org/abs/2602.18098
3. Nikhil Bansal, Milind Prabhu, Sahil Singla and Siddharth M. Sundaram, *Online Graph Balancing and the Power of Two Choices*, arXiv:2604.04159 (first public 2026-04-05). https://arxiv.org/abs/2604.04159
