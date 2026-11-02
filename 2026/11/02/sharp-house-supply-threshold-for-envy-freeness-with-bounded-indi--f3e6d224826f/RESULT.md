# Sharp house-supply threshold for envy-freeness with bounded indifference tiers

## Finding

**Theorem (sharp universal supply threshold).** For integers \(n\ge2\) and \(k\ge1\), consider any \(n\) agents with arbitrary, possibly different, complete transitive weak preferences over a common set of \(m\) distinct houses. Each agent has **at most \(k\) nonempty indifference tiers**. An allocation assigns one distinct house to each agent and may leave other houses unassigned. If

\[
m\ge k(n-1)+1,
\]

then there exists an envy-free allocation, in which no agent strictly prefers the house received by another agent to her own. The uniform threshold is sharp: for every such \(n,k\), an instance with exactly \(k(n-1)\) houses and no envy-free allocation exists, even with identical preferences across agents. The favorable allocation is constructible in polynomial time using minimal Hall-deficiency elimination.

In particular, for dichotomous (two-tier) preferences, \(2n-1\) houses always suffice, while \(2n-2\) may fail. This is a **zero-transfer** statement: no subsidies are necessary in the guaranteed range.

## Assumptions and scope

Let \(N=\{1,\ldots,n\}\) be the agent set and \(H\) be the finite house set. Each weak order partitions \(H\) into \(k_i\) nonempty classes \(C_{i,1},\ldots,C_{i,k_i}\), with \(1\le k_i\le k\), strictly ordered from most to least preferred. An allocation is an injection \(\pi:N\to H\), and envy-freeness means \(\pi(i)\succeq_i\pi(j)\) for every pair \(i,j\in N\). Unallocated houses need not be compared to allocated houses. No interpersonal cardinal-utility comparisons, transfers, common preferences, or randomness are assumed.

The theorem is uniform in all integers \(n\ge2,k\ge1,m\ge k(n-1)+1\). The lower-bound instances establish sharpness of a universal guarantee, not that every instance below the threshold fails.

## Proof

**Step 1 (the existing Hall-elimination framework).** Start with the active house set \(H_0=H\). For an active set \(Q\) with \(|Q|\ge n\), let \(T_i(Q)\subseteq Q\) be the nonempty set of agent \(i\)'s most-preferred houses within \(Q\). Form a bipartite graph whose agent-neighbor sets are \(T_i(Q)\). If it has a matching covering all agents, assign these matched houses. Each assigned house is one of that agent's most-preferred active houses, so the resulting allocation is envy-free.

If no agent-covering matching exists, Hall's theorem gives a subset \(Z\subseteq N\) with \(|T(Z,Q)|<|Z|\), where \(T(Z,Q)=\bigcup_{i\in Z}T_i(Q)\). Choose an **inclusion-minimal** deficient \(Z\). Put \(z=|Z|\). Minimality implies every proper subset is nondeficient, hence (by deleting one member of \(Z\)) \(|T(Z,Q)|\ge z-1\). Deficiency gives the reverse inequality, so \(|T(Z,Q)|=z-1\). Because every top-choice set is nonempty, \(z\ge2\). Remove exactly these \(z-1\) houses and repeat on the surviving active set. This is the standard Hall-violator elimination idea; the quantitative bound below is the assertion at issue. A deficient set can be found by a matching computation and made inclusion-minimal by testing whether individual agents can be deleted while deficiency remains. Thus each round admits polynomial-time implementation, independently of the verifier’s small-case exhaustive search.

**Step 2 (a tier-budget invariant).** As long as \(|Q|\ge n\), an agent whose top-choice set is *all of \(Q\)* cannot belong to a Hall-deficient set \(Z\): if she belonged, its neighborhood would be \(Q\), containing at least \(n\ge|Z|\) houses. For any agent \(i\) in a removed deficient set \(Z\), **all** her currently most-preferred houses are in \(T(Z,Q)\), so that removal exhausts a nonempty entire remaining tier of her weak order. Consequently, during rounds in which at least \(n\) houses remain, each agent can participate in at most \(k_i-1\le k-1\) removal sets; a remaining last tier makes her top set equal to the active set and excludes her from deficient sets.

**Step 3 (optimal removal count).** Let \(T\) denote the number of elimination rounds, and write \(z_t\in\{2,\ldots,n\}\) for the size of the deficient agent set in round \(t\). The total number of removed houses is

\[
R=\sum_{t=1}^{T}(z_t-1).
\]

Every \(z_t\le n\) gives \(R\le(n-1)T\). The tier budget summed over agents gives \(\sum_tz_t\le n(k-1)\), hence also \(R\le n(k-1)-T\). If \(T\le k-1\), the first bound gives \(R\le(n-1)(k-1)\). If \(T\ge k-1\), the second gives \(R\le n(k-1)-(k-1)=(n-1)(k-1)\). Thus, in either case,

\[
R\le(n-1)(k-1).
\]

For \(m\ge k(n-1)+1\), there are therefore always at least \(m-R\ge n\) active houses. Every unsuccessful round removes at least one house, so the process must terminate; it cannot run below \(n\) houses. It must therefore terminate at an agent-covering top-choice matching, proving the existence and constructibility of an envy-free assignment. The same argument covers \(k=1\), in which no deficient set exists when \(m\ge n\).

**Step 4 (sharpness).** Take exactly \(k(n-1)\) houses, partitioned into \(k\) disjoint classes \(B_1,\ldots,B_k\), each of cardinality \(n-1\). Give every agent the identical weak order \(B_1\succ B_2\succ\cdots\succ B_k\), with indifference inside each class. Every injection of \(n\) agents selects \(n\) distinct houses, which cannot all lie in one class because each class has only \(n-1\) houses. An agent assigned a lower-tier house strictly envies an agent assigned a higher-tier house. Hence no envy-free allocation exists. When \(k=1\), this also records that \(n-1\) houses cannot be injected into \(n\) agents. This completes the sharp universal classification.

## Verification

The accompanying dependency-free `verify.py` independently implements exhaustive assignment search and a Hall-deficiency peeling construction. It exhaustively compares both algorithms on all \(6,561\) labeled two-agent, four-house profiles with three possible ranks per house and all \(32,768\) three-agent, five-house profiles with two possible ranks per house. It also verifies the complete \(4,096\)-profile three-agent, four-house binary boundary domain (\(78\) have no envy-free allocation), tests \(11,000\) reproducible random profiles in larger guaranteed domains, and checks \(25\) sharpness families with direct assignment enumeration for manageable sizes. Execute `python3 verify.py`. All discrete tests are supplementary; the all-parameter guarantee follows from the proof above, not from samples.

## Relationship to prior work

Gan, Suksompong and Voudouris (2019) give a polynomial envy-free house-allocation algorithm employing Hall-deficient elimination. The elimination framework itself is prior work. Aigner-Horev and Segal-Halevi (2022) prove structural and algorithmic theorems for envy-free matchings in a single unweighted bipartite acceptability graph; their saturation and partial-match criteria do not furnish the rank-tier resource threshold here. Aziz and colleagues (2024) study house allocation under uncertain/weak preference descriptions and note the established deterministic algorithm, but do not state this universal sharp bound on the number of houses relative to each agent's number of indifference tiers. Dai and colleagues (2026) and Teh and colleagues (2026) study the role and minimization of subsidies in offline and online house allocation, respectively; their cost and recourse models do not imply this **zero-subsidy, universal bounded-tier supply threshold**. The contribution here is the tight accounting invariant across Hall-deficient rounds, its sharp supply formula, and matching lower-bound instances.

## Limitations

The theorem requires allocating exactly one house per agent, with optional unallocated houses; it does not cover multiple objects per agent, indivisible-bundle fairness, or price/subsidy minimization when too few houses exist. The number \(k\) bounds each agent's *indifference tiers*, not the number of distinct preference orders in the market. The lower-bound examples establish worst-case sharpness, not generic nonexistence below threshold. Priority against all unpublished or unindexed proofs is not established; the counting observation may have been independently derived from the older Hall-elimination algorithm. The precise boundary when preferences have varying individual tier counts below the common upper bound is not classified.

## References

- Aigner-Horev, E., and Segal-Halevi, E. (2022). *Envy-free Matchings in Bipartite Graphs and their Applications to Fair Division*. https://arxiv.org/abs/1901.09527
- Gan, J., Suksompong, W., and Voudouris, A. (2019). *Envy-Freeness in House Allocation Problems*. https://arxiv.org/abs/1905.00468
- Aziz, H., Iliffe, I., Li, B., Ritossa, A., Sun, A., and Suzuki, M. (2024). *Envy-Free House Allocation under Uncertain Preferences*. AAAI 2024. https://ojs.aaai.org/index.php/AAAI/article/download/28802/29534
- Dai et al. (2026). *The Complexity of Minimizing Subsidies in Envy-Free House Allocation*. https://arxiv.org/abs/2608.22216
- Teh et al. (2026). *Online House Allocation with Subsidy*. https://arxiv.org/abs/2609.29691
- Choo et al. (2024). *Envy-Free House Allocation with Minimum Subsidy*. https://arxiv.org/abs/2403.01162
