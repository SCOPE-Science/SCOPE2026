# The minimum zero-forcing exchange graph of the Petersen line graph

## Finding

Let \(P=\operatorname{KG}(5,2)\), with its ten vertices the two-subsets of \(\{0,1,2,3,4\}\) and an edge between disjoint two-subsets. Let \(H=L(P)\), so the fifteen vertices of \(H\) are the edges of \(P\). Ordinary zero forcing begins with a black set, and a black vertex may turn its unique white neighbor black.

There are exactly \(2{,}280\) minimum ordinary zero-forcing sets in \(H\). Each has size \(7\), a minimum size independently covered by earlier line-graph forcing theory. Under the natural relabeling action of \(S_5\), the minimum sets form \(21\) orbits: seventeen of size \(120\) and four of size \(60\).

Form the exchange graph \(\mathcal Z(H)\): its vertices are the minimum zero-forcing sets; an edge replaces one selected vertex by one unselected vertex, retaining a minimum zero-forcing set. It is connected with exactly \(28{,}650\) edges, radius \(6\) and diameter \(7\). Its eccentricity classes comprise \(600\) vertices of eccentricity \(6\) and \(1{,}680\) of eccentricity \(7\).

The full degree distribution is:

| Degree | Configurations |
| ---: | ---: |
| 22 | 180 |
| 23 | 480 |
| 24 | 240 |
| 25 | 240 |
| 26 | 660 |
| 27 | 240 |
| 28 | 60 |
| 29 | 180 |

The numbers of unordered distinct configuration pairs at exchange distances \(1,2,3,4,5,6,7\) are respectively \(28{,}650,234{,}120,765{,}570,1{,}004{,}640,483{,}480,78{,}540,3{,}060\). They sum to \(\binom{2280}{2}=2{,}598{,}060\).

**Near-geodesic phenomenon.** For every two minimum sets \(A,B\), write \(h(A,B)=|A\setminus B|\), the unavoidable number of token replacements. Then
\[
 d_{\mathcal Z(H)}(A,B)\in\{h(A,B),h(A,B)+1\}.
\]
Exactly \(18{,}540\) unordered pairs require the additional move, with a complete breakdown:

| Unavoidable moves \(h\) | Actual distance | Unordered pairs |
| ---: | ---: | ---: |
| 2 | 3 | 3,180 |
| 3 | 4 | 11,640 |
| 4 | 5 | 3,720 |

All other unordered pairs admit an exchange geodesic of the minimum Hamming length. Thus the minimum-forcing-set exchange graph is almost, but not quite, isometric in the Johnson graph \(J(15,7)\).

## Assumptions and scope

All sets are **labelled** subsets of the fifteen edges of the fixed Petersen graph; no quotient is taken in the vertex count or distance distribution. The graph \(\mathcal Z(H)\) uses unrestricted one-token replacements, not token slides along an edge of \(H\), and the forcing rule is ordinary zero forcing rather than the positive-semidefinite variant. Distances count legal single exchanges; only minimum-size zero-forcing configurations may appear on a path.

The theorem is **finite and exact**, concerning precisely \(H=L(P)\). No claim about arbitrary line graphs or all generalized Petersen graphs is made.

## Proof

**1. Reproducible finite encoding.** Index the ten two-subsets of \(\{0,1,2,3,4\}\) lexicographically. Index the fifteen pairs of disjoint such subsets lexicographically: these are the fifteen edges of \(P\), hence the vertices of \(H\). Two indices are adjacent in \(H\) precisely when their corresponding Petersen edges have a common endpoint. Encode any set of these fifteen vertices as a fifteen-bit integer \(s\).

For any black mask \(s\), repeatedly add the bit of every white vertex that is the unique white neighbor of some black vertex. Each step strictly increases the mask unless it is stationary, so the process terminates after at most fifteen adding rounds. It agrees with ordinary zero forcing: any force available now either remains available or has its target already black after other forces, so carrying out all simultaneously cannot prevent success. Let \(F(s)\) be the final mask. The initial set is forcing if and only if \(F(s)=2^{15}-1\).

**2. Exhaustive minimum-set classification.** The file `verify_kneser.py` enumerates every one of the \(2^{15}=32{,}768\) masks, tests forcing closure, proves by exhaustive finite evaluation that none of sizes below \(7\) is forcing, and identifies exactly \(2{,}280\) successful masks of size \(7\). This also independently verifies the already-established minimum of \(7\). The arithmetic is exact, with no random choices, floating-point thresholds or unresolved branches. `verify_classical.py` independently enumerates smaller masks and all size-seven masks in a separate outer-cycle/inner-star/spoke model of the Petersen graph and permits every **individual** force in its sequential branching search; it obtains the identical count.

**3. Complete exchange graph.** Two distinct size-seven masks represent adjacent configurations exactly when their bitwise exclusive-or has two set bits. Both programs generate this adjacency exactly; no intermediate nonforcing set is admitted. Summing degrees and dividing by two yields \(28{,}650\) edges and the eight degree multiplicities displayed above.

**4. Symmetry and all distances.** Every permutation of the five underlying labels induces a Petersen-graph automorphism and therefore permutes the fifteen vertices of \(H\), preserving forcing, exchange adjacency and shortest-path distance. Explicitly enumerating these \(120\) permutations partitions the size-seven forcing masks into the stated \(21\) disjoint orbits. The first certificate performs ordinary breadth-first search from each orbit representative and weights its distance histogram by the orbit cardinality; this is equivalent to BFS from every labelled configuration because distances are invariant under relabeling. All representatives reach all \(2{,}280\) states, proving connectivity. The weighted distance histograms establish the asserted pair counts and eccentricities, radius and diameter. The twofold division for unordered distinct pairs is exact because adjacency and shortest-path distance are symmetric.

**5. Sharp Johnson-distance comparison.** Each token replacement changes precisely one selected and one unselected item, so every path from \(A\) to \(B\) has length at least \(|A\setminus B|\). The same exhaustive BFS records this lower bound for each pair and verifies that the difference is never greater than one. The weighted counts of pairs with difference one are precisely \(3{,}180\), \(11{,}640\), and \(3{,}720\), at the three indicated lower bounds. The second certificate verifies the same defect property and all counts by BFS from **every** state in the independent graph model, without using symmetry reduction. These finite exhaustive algorithms jointly provide a proof of the stated exact finite theorem.

## Verification

From a directory containing the two supplied standalone scripts, run `python verify_kneser.py` and `python verify_classical.py` using Python 3 with standard-library support for integer bit counts. On successful completion they print respectively `KNESER_CERTIFICATE_PASS` and `CLASSICAL_CERTIFICATE_PASS`, after evaluating all assertions. Both scripts were executed against the actual supplied source files and passed. No external graph database, solver, arbitrary search cutoff or other file is required.

## Relationship to prior work

Eroh, Kang and Yi's preprint first posted July 25, 2012 studies zero-forcing numbers of line graphs, including wheels and bouquets, and their relationship to other graph parameters. The present work concerns a different graph and the entire configuration-space metric, not only the minimum size. Fallat and Soltani's 2016 paper proves a general minimum-size formula for the line graphs of graphs with Hamiltonian paths; because the Petersen graph has a Hamiltonian path and has fifteen edges and ten vertices, their formula already implies \(Z(L(P))=15-10+2=7\). That value is **not** claimed as new.

Geneson, Haas and Hogben's 2020 work introduces the minimum zero-forcing-set exchange graph and examines its general structure, with exact examples for paths, cycles, complete graphs, forests and other families. Its examined full text contains no Petersen-line-graph exact enumerator or metric. The original 2008 zero-forcing paper provides foundational definitions. The contribution asserted here is the complete 2,280-state census, natural \(S_5\)-orbit decomposition, degree/eccentricity/distance distributions, and precise Johnson-distance defect profile.

## Limitations

The proof is an exact finite, reproducible computational enumeration, not a new all-order structural theorem. Two independently constructed graph models and forcing algorithms reduce implementation risk, but the verification is not an independent scholarly audit. Existing theory already determines the size-seven minimum. The novelty comparison is limited to inspected primary literature, available mathematical research records and targeted discoverable sources; an equivalent historical unpublished or unindexed computation could exist. The theorem does not establish a formula for other line graphs.

## References

1. Linda Eroh, Cong X. Kang and Eunjeong Yi, *Metric Dimension and Zero Forcing Number of Two Families of Line Graphs*, arXiv:1207.6127, first public preprint July 25, 2012; Math. Bohem. 139 (2014), 467–483. https://arxiv.org/abs/1207.6127
2. Shaun M. Fallat and Abolghasem Soltani, *Line graphs: their maximum nullities and zero forcing numbers*, Czechoslovak Mathematical Journal 66 (2016), 743–755. DOI 10.1007/s10587-016-0290-x. https://dml.cz/dmlcz/145869
3. Jesse Geneson, Ruth Haas and Leslie Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first posted September 1, 2020; Discrete Applied Mathematics 329 (2023), 126–139. https://arxiv.org/abs/2009.00220
4. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648. DOI 10.1016/j.laa.2007.10.009.
