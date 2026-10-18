# Integral homology in four consecutive degrees for the bidirected Petersen multipath complex

## Finding
Let \(P=GP(5,2)\) denote the Petersen graph. Replace each edge by its two opposite arcs, and let \(X=X(\overleftrightarrow P)\) be the simplicial complex whose vertices are those thirty directed arcs and whose simplices are the subdigraphs that are disjoint unions of directed simple paths (including isolated vertices). Then
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{12},&j=4,\\
\mathbb Z,&j=5,\\
\mathbb Z^{44},&j=6,\\
\mathbb Z^{94},&j=7,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, all reduced integral homology is torsion-free. The complex is three-connected, and the Hurewicz homomorphism gives \(\pi_4(X)\cong\mathbb Z^{12}\). This is an integral homology and connectivity result, **not** a claim that \(X\) is a wedge of spheres.

## Assumptions and scope
The ten vertices of \(P\) are \(0,1,\dots,9\). Its fifteen edges are the outer pentagon edges \(\{i,(i+1)\bmod5\}\), the five spokes \(\{i,5+i\}\), and the inner star edges \(\{5+i,5+((i+2)\bmod5)\}\), for \(i=0,\dots,4\). All edges are **bidirected**. The thirty arcs are ordered by increasing undirected edge \((u,v)\) with \(u<v\), followed by the arc \(u\to v\) and then \(v\to u\). A set of arcs is a face exactly when each vertex has in-degree and out-degree at most one and its undirected support is a forest. This last condition removes all directed cycles, including antiparallel two-cycles.

The statement is specific to this ten-vertex digraph. It does not concern the undirected matching complex, its ordinary Morse complex, a one-way orientation of the Petersen graph, or the bidirected complete graph.

## Proof
**1. Exhaustive faces.** Enumerate all face masks by successively appending arcs of strictly increasing index; reject a candidate immediately if an in-degree or out-degree exceeds one or if union-find discovers an undirected cycle. Every valid mask has exactly one increasing list, so this visits **all** faces. The augmented face-count vector, in degrees \(-1\) through \(8\), is
\[
(1,30,360,2240,7860,15912,18280,11160,3120,240).
\]
Thus there are exactly \(59{,}203\) faces, including the empty one. This count admits a second enumeration: scan all \(2^{15}\) undirected edge subsets, retain degree-at-most-two forests, and weight each nonempty path component by its two orientations. The weighted counts agree in every cardinality.

**2. Explicit acyclic reduction.** Starting with all augmented faces unmatched, visit each directed arc in the fixed order. For every still-unmatched face \(F\) not containing that arc, pair \(F\) with its still-unmatched coface obtained by adding the arc. The supplied code implements this deterministic rule and constructs the entire signed Hasse diagram. Directing paired inclusions upward and all other face-cover relations downward, topological sorting visits all \(59{,}203\) nodes and all \(333{,}390\) incidences. Hence the \(29{,}464\) pairs form an acyclic matching, not merely a plausible heuristic. Its only critical augmented cells occur in dimensions \(4,5,6,7\), with counts \(17,59,101,98\), respectively. To get an ordinary CW model, omit the matching involving the empty face; the corresponding vertex is then critical and serves as a basepoint. No other cell of dimension at most three remains, so \(X\) is three-connected.

**3. Integral Morse differential.** Each paired inclusion of a lower face into an upper face has signed incidence \(\pm1\). The standard elementary chain cancellation substitutes \(F=-\varepsilon\sum_{G\neq F}[\partial U:G]G\) whenever \(\partial U=\varepsilon F+\sum_{G\neq F}[\partial U:G]G\), with \(\varepsilon\in\{\pm1\}\); acyclicity makes the recursive substitutions terminate. Applied to the critical chains, this gives integral Morse boundary matrices in degrees \(5,6,7\) of sizes \(17\times59\), \(59\times101\), and \(101\times98\). Direct multiplication verifies that consecutive differentials compose to zero.

**4. Complete integer reduction.** The embedded checker performs exact elementary integral row and column operations, selecting unit pivots and eliminating their rows and columns. It finds respectively \(5\), \(53\), and \(4\) pivots, **all** of absolute value one, with an identically zero remaining matrix each time. These are full Smith reductions, since there is no nonzero residual block. Hence the nonzero integral invariant factors of all differentials are units, leaving no homology torsion. The critical-cell counts and adjacent ranks give
\[
\begin{aligned}
\operatorname{rank}\widetilde H_4&=17-5=12,\\
\operatorname{rank}\widetilde H_5&=59-5-53=1,\\
\operatorname{rank}\widetilde H_6&=101-53-4=44,\\
\operatorname{rank}\widetilde H_7&=98-4=94.
\end{aligned}
\]
All other groups vanish. The reduced Euler characteristic is \(-39\), agreeing independently with the alternating face count. The connectivity assertion and the Hurewicz theorem yield the stated fourth homotopy group.

## Verification
Run `python3 checks/petersen_verify.py` using only the Python 3 standard library. The program enumerates faces, performs the full Hasse-diagram acyclicity test, constructs signed Morse differentials, performs unit-pivot integer reductions, and asserts all ranks and zero remainders. It also checks consecutive differential products, computes **direct** simplicial mod-two boundary ranks without the Morse reduction, and independently counts faces by orienting undirected path forests. Its recorded stdout is included in `checks/verification_output.txt`; the last line is `VERIFIED_BIDIRECTED_PETERSEN_INTEGRAL_HOMOLOGY`.

The finite enumeration is complete for this one finite graph. Neither field-homology agreement nor experimental statistics alone is used to infer the integral result; the exact integer row/column operations provide the torsion conclusion.

## Relationship to prior work
The multipath complex is studied systematically in Caputi–Collari–Di Trani–Smith [1], which computes families including linear graphs, polygons, transitive tournaments, and small grids. Vrećica–Živaljević [2] describe the equivalent cycle-free partial-injection or chessboard construction, with detailed connectivity results for complete directed graphs. The quiver blowup/matching comparison of Caputi–Collari–Ramos [3] assumes **no oriented directed cycles**, an assumption violated by every antiparallel edge pair of \(\overleftrightarrow P\). Caputi–Collari–Smith [4] analyze **bidirectional polygons and paths**, not the Petersen graph, which is cubic and girth five. The resulting homology groups here do not follow from those quoted family classifications.

## Limitations
The result proves the four integral homology groups, torsion-freeness, three-connectivity, and the fourth homotopy group, **not** a complete integral homotopy decomposition or a claim about larger graph families. Originality was checked against relevant direct, alias, and stronger-coverage literature and published mathematical records; logically equivalent work not indexed or identified remains a possible priority risk. The computations and proofs are reproducible, but no independent mathematical audit has yet been performed.

## References
[1] L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 9 August 2022. https://arxiv.org/abs/2208.04656

[2] S. Vrećica, R. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252 (2007). https://arxiv.org/abs/0710.5252

[3] L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248 (2024). https://arxiv.org/abs/2401.01248

[4] L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (2026). https://arxiv.org/abs/2601.05670
