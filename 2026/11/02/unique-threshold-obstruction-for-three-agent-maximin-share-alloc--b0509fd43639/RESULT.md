# Unique threshold obstruction for three-agent maximin-share allocations with five goods

## Finding

**Theorem (exact five-good threshold rigidity).** Let \(G\) contain five labeled indivisible goods, and let three agents have arbitrary valuations \(v_i:2^G\to\mathbb R_{\ge0}\) satisfying \(v_i(\varnothing)=0\) and \(v_i(S)\le v_i(T)\) whenever \(S\subseteq T\). Define the maximin share of each agent by
\[
\mu_i=\max_{G=P_1\sqcup P_2\sqcup P_3}\min_{j=1,2,3}v_i(P_j),
\]
where empty parts are allowed in the maximum. An allocation is MMS-fair if its disjoint bundles cover \(G\) and each agent receives utility at least \(\mu_i\).

An MMS-fair allocation **does not exist if and only if** there are a distinguished good \(s\in G\), the four remaining goods \(R=G\setminus\{s\}\), and the three pairwise distinct perfect matchings \(M_1,M_2,M_3\) of the complete graph on \(R\) such that, for every agent \(i\) and every \(S\subseteq G\),
\[
\boxed{v_i(S)\ge\mu_i\quad\Longleftrightarrow\quad
   s\in S\ \text{or}\ (\exists e\in M_i)\ e\subseteq S.}
\]
In this case each agent has a **unique** MMS-maximizing partition: the singleton \(\{s\}\) and the two edges of \(M_i\). There are exactly \(5\cdot3!=30\) such threshold patterns when goods and agents are labeled, and all thirty are equivalent under relabeling. The same pattern can be realized by normalized monotone binary-valued functions, so failure is real, not merely hypothetical.

Moreover, all three-agent instances on at most four goods admit MMS-fair allocations. Thus five goods form the first failure size for general monotone valuations.

## Assumptions and scope

The valuations are arbitrary **monotone** set functions, not assumed additive, subadditive or submodular. The theorem classifies the agents' utility-threshold acceptance sets \(\{S:v_i(S)\ge\mu_i\}\), not their utility values below or above the MMS thresholds. Goods and agents are labeled for the count \(30\). There are exactly three agents; no further restriction on the magnitude of utility or on the goods' marginal contributions is imposed.

A perfect matching on a four-element set consists of two disjoint unordered pairs covering that set. Exactly three such matchings exist. An MMS partition has three parts; two partitions differing only in part order are treated as identical.

## Proof

**1. Positive shares in an impossible instance.** Suppose there is no MMS-fair allocation. If \(\mu_i=0\) for some agent \(i\), give that agent nothing. For each of the other two agents whose share is positive, choose an MMS-maximizing partition into three nonempty parts. At least one part of the first such partition is a singleton (five goods in three nonempty parts). Give that singleton to its owner, then give a part of the other partition avoiding that singleton to its owner; the latter exists because three disjoint parts cannot all contain the same good. Distribute leftovers arbitrarily. This is an MMS-fair allocation, a contradiction. If the other agents' shares are zero, the assignment is even easier. Therefore all three shares are positive, and every part of any MMS-maximizing partition is nonempty.

**2. No disjoint rainbow transversal.** Choose any MMS-maximizing partition \(\mathcal P_i\) for each agent. If one can choose mutually disjoint parts \(B_i\in\mathcal P_i\), assigning those parts to their corresponding agents and distributing leftovers arbitrarily is MMS-fair by monotonicity. Therefore the three chosen partitions have no such transversal.

Each three-part partition of five goods has a singleton. If two different agents possess singleton parts \(\{a\}\) and \(\{b\}\) with \(a\ne b\), assign these parts to those agents. The third agent has a part disjoint from \(\{a,b\}\), since at most two of its three disjoint parts can intersect the two specified goods. This is a forbidden transversal. Consequently all singleton parts across all three partitions consist of the **same** single good \(s\). No partition has a second singleton. Every chosen partition therefore has part sizes \(1,2,2\) and is uniquely represented by its singleton \(\{s\}\) and a perfect matching \(M_i\) on \(R=G\setminus\{s\}\).

If \(M_i=M_j\) for two agents, give the two different edges of that common matching to those two agents and the singleton \(\{s\}\) to the third. This is a transversal. Therefore the three matchings are all different. Because there are exactly three perfect matchings of four vertices, all three occur. In particular, any choice of MMS partitions has this configuration.

**3. Rigidity of *every* acceptable bundle.** Fix agent \(i\). All bundles containing \(s\) or an edge of \(M_i\) have utility at least \(\mu_i\), by monotonicity and the selected MMS partition. Suppose another bundle \(S\) also had utility at least \(\mu_i\). It cannot contain \(s\) or an edge of \(M_i\). Since a three-element subset of four vertices necessarily contains an edge of any perfect matching, \(S\subseteq R\) and \(1\le|S|\le2\).

If \(S=\{x\}\), give \(S\) to agent \(i\), give \(\{s\}\) to another agent \(j\), and give the third agent an edge of its matching avoiding \(x\); such an edge exists because its two matching edges partition \(R\). If \(|S|=2\), the pair \(S\) is not an edge of \(M_i\). The three perfect matchings partition the six edges of the complete graph on \(R\), so its complementary pair \(R\setminus S\) is an edge of precisely one of the *other* agents' matchings. Give that pair to its corresponding agent and \(\{s\}\) to the remaining agent. Each construction is an MMS-fair allocation (leftovers, if any, may be assigned arbitrarily), contradiction. Hence the displayed equivalence of acceptable bundles holds for every \(i\).

**4. Uniqueness of each MMS partition.** In a three-part partition all of whose parts meet agent \(i\)'s MMS threshold, two parts not containing \(s\) require at least two goods each, because acceptance without \(s\) requires a matching edge of \(M_i\). Five goods are available, so the \(s\)-containing part is exactly \(\{s\}\) and the other two parts are exactly the two edges of \(M_i\). This proves uniqueness.

**5. Converse and labeled count.** If the displayed acceptance criterion holds for each agent with the three different matchings, any MMS-fair allocation would need three disjoint acceptable bundles. If no allocated bundle contains \(s\), the three bundles require at least six goods from \(R\), impossible. If one bundle contains \(s\), the other two must contain disjoint edges of two distinct perfect matchings on \(R\). Two disjoint edges of four vertices are complementary, hence belong to the *same* perfect matching, also impossible. Thus the acceptance pattern prevents every MMS-fair allocation.

For a concrete realization, take \(v_i(S)=1\) exactly when \(s\in S\) or \(S\) contains an edge of \(M_i\), and \(v_i(S)=0\) otherwise. Each agent's partition \(\{\{s\},e_i,f_i\}\) has three parts all worth \(1\), and the range is \(\{0,1\}\); therefore \(\mu_i=1\), giving an actual counterexample. The distinguished good has five choices, and the three distinct matchings can be bijectively assigned to the labeled agents in \(3!=6\) ways, giving \(30\) threshold patterns. Permutations of the remaining four goods induce every permutation of the three matchings, showing that all patterns lie in one relabeling orbit.

**6. Sharp smaller-size existence.** With three agents and at most two goods, all MMS shares equal zero, so any allocation works. With three goods, positive MMS implies each part of an MMS partition is a singleton, so distinct goods can be allocated to agents meeting their shares; zero-share agents can receive empty bundles. With four goods, each agent with positive share has a partition with two singleton parts and one two-good part. From two such partitions belonging to different positive-share agents choose two singleton parts with different goods; a third positive-share agent's partition has a part avoiding both goods. These parts are mutually disjoint and yield an MMS-fair allocation after leftovers are distributed. If fewer than three agents have positive share, a singleton part for one can be combined with a disjoint part from the other, while zero-share agents receive empty bundles. Thus no failure occurs with fewer than five goods. \(\square\)

## Verification

A separate standard-library Python 3 program, `verify.py`, enumerates all \(25\) unordered three-part partitions of five labeled goods and all \(25^3=15625\) ordered triples. It directly checks the existence of disjoint part transversals rather than assuming the proof's singleton argument. Exactly \(30\) triples fail, and an independent group-action normalization finds one orbit. It also checks all \(216\) four-good triples, the binary threshold valuations on each of the \(30\) obstructions against all \(3^5=243\) complete allocations, and \(720\) single-extra-acceptable-bundle extensions, all of which restore feasibility. Execute `python3 verify.py`; no external libraries are needed. The universal assertions about arbitrary monotone utility values come from the proof, not merely from finite enumeration.

## Relationship to prior work

Feige (2026) defines the general monotone-MMS threshold problem and its colored-hypergraph/rainbow-matching formulation, and proves asymptotic bounds. Importantly, **Feige's Theorem 6 already supplies a five-good, three-agent nonexistence construction** by specializing its parameter to \(c=2\) and three agents. The existence of such a counterexample, and its underlying three different pairings, are therefore **not** claimed as new here. The present result instead proves **necessity**: every five-good nonexistence instance has *exactly* the specified threshold acceptance pattern, and each agent's MMS partition is unique. It also enumerates the complete first-failure threshold layer. Theorem 6 constructs examples; it does not assert this if-and-only-if rigidity.

Feige, Sapir and Tauber (2021) give the different sharp additive three-agent threshold at nine goods. Hummel (2023) develops additive small-item guarantees. Barman, Rammohan and Sethia (2025) allow duplicated supply to restore MMS fairness, unlike the present disjoint-allocation requirement.

## Limitations

The classification applies to utility-threshold acceptance families, not the numerical utility values themselves. It does not extend unmodified to arbitrary nonmonotone preferences, four or more agents, or fairness notions other than exact MMS. The binary witness is generally complementary rather than additive or submodular, though Feige's earlier construction already provides a submodular numerical realization of this pairing pattern. Novelty is assessed relative to inspected accessible sources; a separately published equivalent classification might exist and would require comparison.

## References

- U. Feige, *On MMS allocations with few items*, arXiv:2610.06125v1 (public October 5, 2026), https://arxiv.org/html/2610.06125v1 . See Introduction, Theorem 6, and Appendix B, Question 22.
- U. Feige, A. Sapir, L. Tauber, *A tight negative example for MMS fair allocations*, arXiv:2104.04977 (2021), https://arxiv.org/abs/2104.04977 .
- H. Hummel, *On lower bounds for maximin share guarantees*, IJCAI 2023, https://arxiv.org/abs/2302.00264 .
- S. Barman, S. Rammohan, A. Sethia, *Exact maximin share fairness via adjusted supply*, arXiv:2502.03789 (2025), https://arxiv.org/abs/2502.03789 .
