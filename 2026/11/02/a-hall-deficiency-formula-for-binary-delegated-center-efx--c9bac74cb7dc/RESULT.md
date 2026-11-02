# A Hall-deficiency formula for binary delegated center-EFX

## Finding
Let \(k\ge2\) centers each contain exactly two lower-level agents. Let \(M\) consist of \(2k\) indivisible goods. Each lower agent has a nonnegative, additive, binary valuation, taking value \(0\) or \(1\) on each good. Every lower agent must receive **exactly one** good. For center \(i\), define its approval neighborhood
\[
L_i=\{g\in M:\max(v_{i,1}(g),v_{i,2}(g))=1\},\qquad A=\{i:L_i\ne\varnothing\}.
\]
Let \(\nu\) be the maximum cardinality of a matching in the bipartite graph between centers in \(A\) and goods in \(M\), with incidence \(g\in L_i\). For a one-to-one allocation, a center *fails EFX* if there is some other center and some good belonging to that center whose removal still leaves the first center envious, under the relevant center-valuation convention.

**Theorem.** Under each of the four conventional center valuations (item-based potential, item-based realized, bundle-based potential, bundle-based realized), the minimum number of EFX-failing centers, among all one-to-one allocations, is exactly
\[
\delta=|A|-\nu=\max_{S\subseteq A}\left(|S|-\left|\bigcup_{i\in S}L_i\right|\right).
\]
Moreover, **one allocation simultaneously attains** this minimum for all four center valuations and satisfies inter-EF1 for every pair of lower agents. Consequently, center-EFX together with lower-agent inter-EF1 is possible under one-to-one allocations if and only if Hall's condition \(\left|\bigcup_{i\in S}L_i\right|\ge|S|\) holds for every \(S\subseteq A\). An optimal allocation and its deficiency certificate can be found by bipartite maximum matching.

The restriction to two lower agents per center is sharp for the Hall criterion: with three agents in each of two centers, three goods approved by all six agents, and three goods approved by none, Hall's condition holds but no one-to-one allocation is center-EFX.

## Assumptions and scope
There are \(k\ge2\) distinct labeled centers, two distinct lower agents per center, and \(2k\) distinct goods; all \(2k\) lower-agent bundles are singletons. The valuation of an agent for a set is the sum of its binary singleton values. Center comparison follows the four definitions in Deligkas et al., arXiv:2607.27743: a center assesses another center's goods by the maximum potential welfare obtainable either by redistributing the goods (item-based) or by reassigning its existing lower-agent bundles (bundle-based); its own value is either potential welfare or the realized welfare of the chosen assignment. In particular, potential item-based welfare may put several goods with the same lower agent, whereas potential bundle-based welfare only permutes the bundles. Center EFX requires its own value to be at least its value for the other center's bundling following removal of **each** good. Inter-EF1 uses each lower agent's actual valuation and allows removal of the single good in the envied lower-agent bundle. No Pareto-optimality or positive-value assumption is imposed.

## Proof
**Singleton reduction.** Each center holds two singleton lower-agent bundles. Removing any good from another center leaves precisely one singleton. Either hypothetical-reallocation interpretation of a remaining singleton yields, for center \(i\), exactly \(\ell_i(g)=\max(v_{i,1}(g),v_{i,2}(g))\in\{0,1\}\). Thus every possible comparison after a deletion has value at most \(1\), under all four conventions.

**Lower bound.** Fix any one-to-one allocation. If an active center \(i\in A\) has no good of \(L_i\) in its own center, its own realized and potential values are all zero. Some liked good \(g\in L_i\) instead lies in another center \(j\), which has a second distinct good \(h\). Removing \(h\) leaves \(g\), of hypothetical value \(1\) to center \(i\), so center \(i\) fails EFX under all four conventions. Therefore every EFX-satisfied active center possesses a liked good. Select one such owned good for each satisfied active center. The selected goods are distinct because ownership is disjoint; these center-good pairs form a matching. At most \(\nu\) active centers can be EFX-satisfied. Inactive centers never fail EFX, so at least \(|A|-\nu\) centers fail under any convention.

**Simultaneous construction.** Find a maximum matching of size \(\nu\). Put each matched good in its matched center and give it to an affiliated lower agent who values it at \(1\). Fill every remaining singleton slot with the remaining goods in any order. Each matched center has realized welfare at least \(1\), so its own value is at least \(1\) under every valuation convention. The singleton reduction shows it satisfies EFX toward every other center. Every inactive center also satisfies EFX, because it values all goods at zero. Thus at most \(|A|-\nu\) centers fail simultaneously; the lower bound proves equality. Since each lower agent receives one good, removing that good from any envied agent's bundle leaves the empty set, so inter-EF1 automatically holds. Hall's matching-deficiency theorem gives the displayed maximum-over-subsets identity; hence the exact existence condition and polynomial-time algorithm follow.

**Sharp capacity boundary.** For two centers with three lower agents apiece, take six goods, exactly three of which give value \(1\) to all six agents; the other three have value \(0\). Every one-to-one center bundle has three goods. One center holds at most one valued good; the other holds at least two. If the latter holds two, it also holds a zero-valued good, whose removal leaves value \(2\), exceeding the former center's own value at most \(1\). If the latter holds all three valued goods, removing any one leaves value \(2\), again exceeding the other's value \(0\). For these identical valuations, the four center-value conventions coincide. Thus center EFX is impossible although the center-good incidence graph satisfies Hall's condition.

## Verification
The accompanying standalone `VERIFY.cpp` computes each center's own value separately under the four original conventions, explicitly evaluates every possible one-good deletion from another center, and independently computes maximum matching cardinality by subset backtracking. It exhausts all \(2^{16}=65{,}536\) binary lower-agent valuation profiles for two centers and four goods, inspecting all \(24\) one-good-per-agent allocations. It also checks \(1{,}024\) deterministic pseudorandom profiles of three centers and six goods against all \(720\) allocations, and verifies all \(720\) permutations of the three-agent-per-center boundary instance. Compile and run with `g++ -O2 -std=c++17 VERIFY.cpp -o verify && ./verify`. The observed output is

`VERIFY_OK exhaustive_two_center_agent_profiles=65536 random_three_center_profiles=1024 valuation_variants=4 capacity_three_boundary=720/720_infeasible`

The unbounded-\(k\) theorem follows from the proof, not from the finite test suite. The finite verifier does not prove literature originality.

## Relationship to prior work
Deligkas, Fasoulakis, Ioannidis, Mancho and Markakis (2026), *Delegated Fair Division*, introduced the four center valuation conventions and contrasted center-EFX with inter-EF1. Their Theorems 9 and 10 give nonexistence and NP-hardness for broader additive valuations; their Discussion proposes one-to-one allocations for further study. Neither is an exact binary two-person-center deficiency characterization. The present result exploits two features that do not hold in those broader instances: each center owns two singleton bundles and each remaining singleton comparison has binary value at most one. Its matching theorem is an application of classical Hall deficiency, which is not claimed as a new matching result.

Cookson, Shah and Verma (2026), *Fair and Efficient Balanced Allocations for Additive Valuations*, establish balanced EF1 and fractional Pareto optimality in an ordinary one-level setting, which does not imply center EFX or the exact minimal number of EFX-failing centers. Kawase and Mahara (2026) obtain balanced EF1 and efficiency under further additive restrictions; this likewise does not imply this stronger two-level counting invariant.

## Limitations
The result requires binary individual approvals, exactly two agents and two assigned goods per center, and one good per lower agent; it is not a general theorem for arbitrary additive weights, larger center capacities, or unbalanced bundles. The explicit three-agent boundary shows that the same Hall condition fails beyond capacity two. The result does not optimize social welfare and does not imply overall EFX in the general delegated setting. Although the special-model reduction and its quantitative optimum are not found in the inspected directly relevant sources, equivalent formulations in unindexed literature remain possible.

## References
1. A. Deligkas, M. Fasoulakis, S. D. Ioannidis, A. Mancho, E. Markakis, *Delegated Fair Division*, arXiv:2607.27743v1 (first public version July 30, 2026), https://arxiv.org/abs/2607.27743 . In particular Definitions 1 and 5, Theorems 9 and 10, and Section 6.
2. B. Cookson, N. Shah, P. Verma, *Fair and Efficient Balanced Allocations for Additive Valuations*, arXiv:2608.06325v1 (August 6, 2026), https://arxiv.org/html/2608.06325v1 . In particular Theorem 1 and Section 1.1.
3. Y. Kawase, R. Mahara, *Fair and Efficient Balanced Allocation for Indivisible Goods*, AAAI 2026, DOI:10.1609/aaai.v40i20.38755, https://ojs.aaai.org/index.php/AAAI/article/view/38755 .
4. P. Hall, *On Representatives of Subsets*, Journal of the London Mathematical Society 10 (1935), 26–30. The matching deficiency formula is classical.
