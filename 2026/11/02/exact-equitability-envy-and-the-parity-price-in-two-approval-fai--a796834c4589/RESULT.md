# Exact equitability, envy, and the parity price in two-approval fair division

## Finding

**Theorem (sparse-approval exact-equitability frontier).** Let \(n\ge3\) agents have additive binary valuations over finitely many distinct goods. Assume that each agent approves exactly \(d\ge0\) goods, and each good is approved by at most two agents (goods approved by nobody are allowed). Define \(\Gamma(S)\) to be all goods approved by at least one agent in \(S\), and define
\[
\kappa=\min_{\varnothing\ne S\subseteq N}\left\lfloor\frac{|\Gamma(S)|}{|S|}\right\rfloor.
\]
Then \(\kappa\ge\lfloor d/2\rfloor\). There exists a **complete** allocation that is simultaneously exactly equitable (EQ), envy-free up to one good (EF1), and maximizes the common realized utility among all complete EQ allocations: every agent realizes exactly \(\kappa\). When \(d\) is even, this allocation is in fact fully envy-free (EF), without requiring every good to have two approvers. It can be constructed in polynomial time by bipartite matching and assignment of surplus goods to nonapprovers.

**Exact-two-approval corollary.** If every good has *exactly* two distinct approvers (equivalently, goods are edges of a loopless \(d\)-regular multigraph of agents), then \(\kappa=\lfloor d/2\rfloor\). The utilitarian optimum is \(nd/2\). The best exactly equitable allocation therefore has utilitarian welfare \(n\lfloor d/2\rfloor\), a sharp loss of zero if \(d\) is even and \(n/2\) if \(d\) is odd. When \(d\) is even, there is a complete allocation satisfying **EQ, full envy-freeness (EF), and Pareto optimality (PO)**. When \(d\) is odd, there is a complete **EQ1+EF1+PO** allocation with individual utilities in \(\{\lfloor d/2\rfloor,\lceil d/2\rceil\}\), although exact EQ cannot be PO. This covers arbitrary numbers of agents, parallel goods, and nonlaminar approval sets.

## Assumptions and scope

An allocation \(A=(A_1,\ldots,A_n)\) is complete when the disjoint bundles partition all goods. A binary additive valuation is \(v_i(T)=|\{g\in T:v_i(g)=1\}|\), with \(v_i(g)\in\{0,1\}\). EQ means all \(v_i(A_i)\) coincide. EF means \(v_i(A_i)\ge v_i(A_j)\) for all agents \(i,j\). EF1 means that whenever \(i\ne j\) and \(v_i(A_j)>v_i(A_i)\), there is some good \(g\in A_j\) satisfying \(v_i(A_i)\ge v_i(A_j\setminus\{g\})\). EQ1 means the realized utilities differ by at most one in the binary PO allocations used below. PO forbids another allocation weakly improving every realized utility and strictly improving at least one.

No graphical connectivity restriction is imposed on bundles; edges describe only which agents approve a good. The bound on approvers, normalization, and \(n\ge3\) concern the first assertion. In the exact-two case every good has exactly two approvers. Goods can be repeated as distinct items with identical approval sets. If \(d=0\), all realized utilities are zero and the assertions are immediate. An approval graph such as a long simple cycle is generally nonlaminar: adjacent agents' approval sets overlap without containment.

## Proof

**Step 1: Matching capacity is the optimum common utility.** A complete EQ allocation in which each agent realizes an integer \(t\) uses \(t|S|\) distinct goods approved by \(S\), for every nonempty \(S\subseteq N\); hence \(t|S|\le |\Gamma(S)|\), giving \(t\le\kappa\). Conversely, replace each agent by \(\kappa\) distinguishable slots, each adjacent to the goods approved by that agent. For any subset of slots involving agents \(S\), the number of slots is at most \(\kappa|S|\), while their neighborhood is \(\Gamma(S)\), containing at least \(\kappa|S|\) goods by definition. Hall's theorem gives a matching filling every slot. This assigns exactly \(\kappa\) approved goods to each agent in a partial allocation.

**Step 2: Normalized low-overlap families have enough capacity.** For each nonempty \(S\), count agent–good approvals involving \(S\): there are \(d|S|\). A good contributes at most two, so \(d|S|\le2|\Gamma(S)|\). Therefore \(|\Gamma(S)|/|S|\ge d/2\) and \(\kappa\ge\lfloor d/2\rfloor\). This uses no laminarity assumption.

**Step 3: Complete the allocation without changing utilities.** Every surplus good has at most two approvers, so with \(n\ge3\) it has a nonapproving recipient. Assign every unmatched good to any such recipient. All realized utilities remain exactly \(\kappa\), including when \(\kappa=0\). For any agents \(i\ne j\), the number of goods in \(A_j\) approved by \(i\) is at most all the goods approved by \(i\) but absent from her own approved bundle, namely \(d-\kappa\). Because \(\kappa\ge\lfloor d/2\rfloor\), integer arithmetic gives \(d-\kappa\le\kappa+1\). Hence \(v_i(A_j)\le v_i(A_i)+1\). If an EF1 comparison is strict, its binary-valued excess is precisely one, and removing a good in \(A_j\) that \(i\) approves eliminates envy. Therefore the complete allocation is EQ+EF1. When \(d\) is even, \(\kappa\ge d/2\), so the stronger bound \(d-\kappa\le\kappa\) gives full EF. Step 1 establishes maximal common utility, rather than just feasibility. One can find \(\kappa\) by testing matching feasibility for integer targets and binary searching from zero to \(d\), then complete the allocation; this is polynomial in the explicit incidence input size.

**Step 4: The exact-two welfare frontier.** If every good has exactly two approvers, the incidence graph is a loopless \(d\)-regular multigraph with \(m=nd/2\) edges. Any exactly equitable allocation of common utility \(t\) has welfare \(nt\le m\), so \(t\le\lfloor d/2\rfloor\). Step 2 and the construction show \(\kappa=\lfloor d/2\rfloor\) and attain welfare \(n\lfloor d/2\rfloor\). Giving each good to an approver achieves the utilitarian upper bound \(m\), so the exact EQ welfare loss is \(m-n\lfloor d/2\rfloor\), equal to zero for even \(d\) and \(n/2\) for odd \(d\). This is an exact optimum, not just an example.

**Step 5: Balanced orientation restores efficiency.** Orient each edge toward its recipient. If \(d\) is even, each connected component has an Euler tour; orient each Euler tour cyclically. Every vertex has indegree \(d/2\), and so receives value \(d/2\). For every \(i\ne j\), the total number of edges approved by \(i\) but assigned to *all other* agents is \(d-d/2=d/2\), so \(v_i(A_j)\le v_i(A_i)\). Thus this allocation is EQ+EF; assigning every edge to an endpoint also maximizes utilitarian welfare and ensures PO.

If \(d\) is odd, the handshake lemma makes \(n\) even. Pair the odd-degree vertices arbitrarily and add one auxiliary edge per pair. The augmented multigraph has even vertex degrees; orient each of its components along Euler tours, then discard the auxiliary edges. Every original vertex now has indegree either \(\lfloor d/2\rfloor\) or \(\lceil d/2\rceil\), so the resulting allocation is EQ1. Each agent \(i\) receives \(u_i\ge\lfloor d/2\rfloor\) approved goods and approves at most \(d-u_i\le\lceil d/2\rceil\le u_i+1\) goods assigned elsewhere in total. The same binary one-good deletion argument gives EF1. All original edges still go to approvers, yielding welfare \(m\) and PO. For odd \(d\), no exactly EQ allocation can reach \(m\), as Step 4 already shows.

## Verification

The included standard-library program `verify_sparse_fair.py` exhausts all normalized finite **approval-type multisets** (each good approved by one or two agents, allowing repeated types) for three agents and degrees \(0\) through \(4\), and for four agents and degrees \(0\) through \(3\). It checks Hall capacity, an explicit complete EQ+EF1 allocation, and, in every exact-two instance, orientation and the parity welfare formula. It also directly enumerates all complete allocations for 18 deliberately small instances to verify the maximum equal utility; tests the complete-graph example on four agents; and checks the failure of the nonapprover completion argument for two agents with one shared good. Actual run:

```text
VERIFY_OK counts= {(3, 0): 1, (3, 1): 4, (3, 2): 11, (3, 3): 23, (3, 4): 42, (4, 0): 1, (4, 1): 10, (4, 2): 56, (4, 3): 214} direct_optimum_checks= 18 K4= 6 two_agent_exception=confirmed
```

Run with `python3 verify_sparse_fair.py`. These 362 finite incidence-type cases corroborate the construction; the all-\(n\), all-\(d\) claim is proved in Steps 1–5, not inferred from enumeration. The executable uses only the standard library.

## Relationship to prior work

Hosseini, Pathak, Xia and Zhang (2026, arXiv:2608.26410v1, first public August 26) establish simultaneous **EF1+EQ1** for normalized binary valuations with at most seven agents (Theorem 3) and for laminar approval sets with any number of agents (Theorem 5). Appendix C, Theorem 13 gives a Hall-based argument specifically for three agents. Their 113-agent obstruction to EF1+EQ1 uses high-overlap approval sets, so does not contradict this low-overlap theorem. The present claim is stronger **exact EQ+EF1** for the explicit two-approval family for arbitrary \(n\), and supplies an optimal common utility and an exact Pareto-efficiency parity frontier. No implication of this complete statement from their theorems was identified in the inspected text.

Freeman, Sikdar, Vaish and Xia (2019, arXiv:1905.10656) already study EQ, EF1 and PO, show that binary EQ+PO existence is polynomial-time decidable (Theorem 2), prove that binary EQ+PO implies EF (Proposition 5), and provide a conditional polynomial algorithm for EQ1+EF1+PO (Theorem 4). Their general results are not a guaranteed exact EQ+EF1 allocation in every two-approval normalized instance and do not report this graph-regularity welfare formula. The use of Hall matching and Euler orientation is standard mathematics; the new asserted statement is their combined exact guarantee and sharp efficiency boundary for this natural family.

Christodoulou, Fiat, Koutsoupias and Sgouritsa (2023) study EFX allocations on graphical valuation instances and Hsu (2026) studies EFX orientations of multigraphs; these address envy strength/edge orientations rather than the exact EQ utility target or parity price quantified here. This comparison is limited to their available abstracts and accessible definitions, respectively, and is not a priority guarantee.

## Limitations

The theorem requires binary additive values with the same approval degree \(d\), and at most two approvers per good. For its completion proof, \(n\ge3\) is essential: with two agents and one shared good there is no complete exactly equitable allocation. The proof does not establish EFX under conventions requiring deletion of **every** good, including zero-valued goods. In odd-degree exact-two instances, the exactly equitable solution deliberately assigns \(n/2\) goods to nonapprovers and thus is not Pareto optimal; an efficient solution exists only after relaxing EQ to EQ1. Nothing is claimed for unrestricted normalized valuations, weighted valuations, or unrestricted approval hypergraphs. Finite checks are not a substitute for the analytical Hall/Euler proof. Previously unindexed or unavailable proofs could affect publication priority; independent scientific validation has not been performed.

## References

1. Hadi Hosseini, Shraddha Pathak, Lirong Xia, Chengkai Zhang, *Simultaneous Envy and Equitability Guarantees*, arXiv:2608.26410v1 (public August 26, 2026), https://arxiv.org/abs/2608.26410. Theorems 3, 5; Theorem 13 in Appendix C; the 113-agent counterexample.
2. Rupert Freeman, Sujoy Sikdar, Rohit Vaish, Lirong Xia, *Equitable Allocations of Indivisible Goods*, arXiv:1905.10656 (2019), https://arxiv.org/abs/1905.10656. Theorems 2 and 4, Proposition 5, Section 3 and Appendix 6.7.
3. George Christodoulou, Amos Fiat, Elias Koutsoupias, Alkmini Sgouritsa, *EFX Allocations on Graphs*, ACM EC 2023, https://doi.org/10.1145/3580507.3597764.
4. Chao Hsu, *EFX Orientations of Multigraphs*, 2026, https://doi.org/10.3233/FAIA251259.
5. P. Hall, *On Representatives of Subsets*, J. London Math. Soc. (1935), the classical marriage theorem.
