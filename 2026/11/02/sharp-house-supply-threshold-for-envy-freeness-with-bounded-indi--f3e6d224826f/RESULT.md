# Sharp house-supply threshold for envy-freeness with bounded indifference tiers

## Finding

Let \(n\ge2\) and \(k\ge1\) be integers. If each of \(n\) agents has a complete transitive weak preference order with at most \(k\) nonempty indifference tiers over a common set of \(m\) houses, then
\[
m\ge k(n-1)+1
\]
guarantees an envy-free assignment of one distinct house per agent. Other houses may remain unassigned. The bound is sharp: at \(m=k(n-1)\) there is a counterexample even when all agents have identical preferences. A qualifying assignment can be found in polynomial time by eliminating neighborhoods of inclusion-minimal Hall-deficient sets. In particular, \(2n-1\) houses suffice for dichotomous preferences and \(2n-2\) may fail. No transfers are required.

## Assumptions and scope

Agent \(i\)'s weak order on the finite house set has \(k_i\le k\) nonempty tiers. An allocation is an injection \(\pi\) from agents to houses, and is envy-free if \(\pi(i)\succeq_i\pi(j)\) for all \(i,j\). No comparison with an unassigned house is required. No common ordering, utility normalization, cardinal information, or random input model is assumed. Sharpness refers to the worst instance at a given supply, not to failure of every smaller instance.

## Proof

**Hall elimination.** Start with the full house set. At an active set \(Q\) with \(|Q|\ge n\), build the bipartite graph of top choices: the neighbors \(T_i(Q)\) of agent \(i\) are precisely her most preferred active houses. An agent-covering matching is envy-free because all assigned houses are active. If there is no such matching, choose an inclusion-minimal Hall-deficient agent set \(Z\), and delete its neighborhood \(T(Z,Q)=\bigcup_{i\in Z}T_i(Q)\). With \(z=|Z|\), its neighborhood has size \(z-1\): it has size at most \(z-1\) by deficiency and at least \(z-1\) because any \(z-1\) members form a nondeficient set. Each agent has a nonempty top set, so \(z\ge2\) and each unsuccessful round deletes at least one house.

**Polynomial computation of a minimal set.** With the top-choice graph fixed during this computation, start with the full agent set \(A\) that the failed matching could not cover. Delete an agent \(i\) from \(A\) whenever a new maximum-matching test shows that even the restricted set \(A\setminus\{i\}\) cannot be saturated. Keep the entire active house side fixed for these tests. Stop when every single deletion would leave a saturable set. At that point every proper subset of \(A\) is saturable: it is contained in a single-deletion set and can use the restriction of that set's matching. But \(A\) itself remains unsaturable. By Hall's theorem it must itself be deficient and it is inclusion-minimal. Testing only the total neighborhood size of a candidate single-deletion set would not certify this: that set can have enough neighbors in total but still contain a deficient proper subset. Repeated matching tests use at most \(n^2\) matching computations per elimination round, and there are at most \(m\) elimination rounds.

**Tier budget.** As long as \(|Q|\ge n\), a deficient set cannot contain an agent with top set all of \(Q\): its neighborhood would have cardinality \(|Q|\ge n\ge |Z|\). Each time an agent is in a deficient set, deletion of its neighborhood exhausts her entire current best tier, and she cannot participate when only one of her tiers remains. Thus she participates in at most \(k_i-1\le k-1\) rounds. For any prefix of elimination rounds begun with at least \(n\) houses, the total number \(D\) of houses deleted satisfies
\[
D=\sum_t (|Z_t|-1)
 \le \frac{n-1}{n}\sum_t |Z_t|
 \le (n-1)(k-1).
\]
The first inequality uses \(|Z_t|\le n\) and the second counts the total incidences of agents in the deficient sets. At the claimed initial supply, after any such prefix there are at least \(m-D\ge n\) houses. Inductively the algorithm cannot exit by having too few houses. Since each elimination removes at least one house, it must reach an agent-covering top-choice matching. For \(k=1\) the top-choice graph is already complete.

**Sharpness.** With exactly \(k(n-1)\) houses, give all agents one common weak order with \(k\) successive tiers each of size \(n-1\). Any allocation of \(n\) houses must span at least two tiers, and an agent assigned in a lower tier strictly envies an agent assigned in a higher tier. If \(k=1\), there are only \(n-1\) houses, so no injection exists in the first place.

## Reproducibility and limitations

The accompanying standard-library `verify.py` compares direct allocation enumeration with Hall elimination on small exact-rank domains and tests further finite examples. In these small tests, the script searches Hall violators by increasing cardinality rather than running the matching-based minimal-set procedure above. Its finite checks corroborate the threshold but do not certify either the asymptotic running time or the universal theorem; the matching and tier-budget arguments prove those claims.

This statement is for one house per agent, optional unassigned houses, and ordinary envy-freeness without transfers. It does not assert a threshold for assignments of bundles or a characterization at every supply below the universal bound.

## Relationship to prior work

The top-choice Hall-violator elimination algorithm is due to Gan, Suksompong and Voudouris (2019). Their Lemma 2.1 gives a polynomial way to find a minimal Hall violator by alternating paths; their Theorem 2.2 treats algorithmic existence and construction for weak-order house allocation. The quantitative claim here is the tier-budget guarantee and the matching obstruction, not the general top-choice elimination method. The envy-free matchings of Aigner-Horev and Segal-Halevi (2022) use a single bipartite acceptability graph and different saturation conventions. The model here compares preference tiers among the houses actually allocated.

## References

- J. Gan, W. Suksompong, and A. A. Voudouris, *Envy-Freeness in House Allocation Problems*, 2019, [arXiv:1905.00468](https://arxiv.org/abs/1905.00468).
- E. Aigner-Horev and E. Segal-Halevi, *Envy-free Matchings in Bipartite Graphs and their Applications to Fair Division*, 2022, [arXiv:1901.09527](https://arxiv.org/abs/1901.09527).
