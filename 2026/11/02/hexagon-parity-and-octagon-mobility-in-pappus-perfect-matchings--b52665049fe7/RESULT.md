# Hexagon parity and octagon mobility in Pappus perfect matchings

## Finding

Let \(P\) be the eighteen-vertex Pappus graph, and let \(\mathcal M(P)\) denote its perfect matchings (one-factors). For an even integer \(\ell\), let \(F_\ell\) be the graph on \(\mathcal M(P)\) in which two perfect matchings are adjacent precisely when their symmetric difference is the edge set of **one simple alternating cycle** of length \(\ell\). Let \(F_{\le L}\) contain all such edges with length at most \(L\).

There are exactly \(42\) perfect matchings. The hexagon-flip graph \(F_6\) consists of **two isomorphic connected components of order \(21\)**, distinguished exactly by the parity of the perfect-matching permutation. Each component is the same explicitly defined graph \(H\): take three hubs and, for each pair of hubs, add a disjoint six-cycle whose six vertices are joined by spokes alternately to the two hubs. Thus each component has three vertices of degree six, eighteen of degree three, thirty-six edges and diameter four.

The octagon-only graph \(F_8\) has six isolated vertices and one connected component on thirty-six vertices, regular of degree six. The combined graph \(F_{\le8}=F_6\cup F_8\) is connected, has \(42\) vertices and \(180\) edges, and has both radius and diameter \(3\). It has six vertices of degree \(6\), each with distance-sphere profile \((1,6,24,11)\), and thirty-six vertices of degree \(9\), each with profile \((1,9,24,8)\). The numbers of unordered matching pairs at distances \(1,2,3\) are \((180,504,177)\). In particular **eight is the least permitted alternating-cycle length that connects all perfect matchings**.

The invariant parity separation for three-cycle permutations is elementary; the novel proposed statement is the **converse connectivity and explicit three-hub/six-cycle structure**, together with the sharp octagon threshold and complete metric, not the parity observation alone or the bare number of perfect matchings.

## Assumptions and scope

All graph vertices and edges are labelled only for computation; the resulting graph statements are invariant under relabelling. Work in \(\mathbb F_3\). The nine points are \((x,y)\in\mathbb F_3^2\); the nine retained lines have labels \((d,c)\in\{0,1,2\}\times\mathbb F_3\). Define incidence by \(x=c\) if \(d=0\), by \(y=c\) if \(d=1\), and by \(x+y=c\) if \(d=2\). The resulting bipartite incidence graph is \(P\), obtained from \(\operatorname{AG}(2,3)\) by deleting its fourth parallel class. This specifies the graph without relying on a picture or external data.

A perfect matching consists of nine point-to-line incidences covering each point and each line once. A flip replaces the alternating half of exactly one even simple cycle by its complementary half; it does **not** simultaneously flip several disjoint cycles. The cutoff statement concerns all even cycle lengths at most \(L\), not only exactly \(L\). The result does not assert an infinite-family generalization, mixing-time theorem, or independent verification by another researcher.

## Proof

**1. Complete state enumeration.** Order points and lines lexicographically. Form the \(9\times9\) binary incidence matrix \(A\), with \(A_{ij}=1\) exactly for an incident point and line. A perfect matching is exactly a permutation \(\sigma\) with \(A_{i,\sigma(i)}=1\) for every \(i\in\{0,\ldots,8\}\). For a subset \(S\) of line labels, let \(f_i(S)\) be the number of injective assignments of the first \(i\) points onto precisely \(S\). Initialize \(f_0(\varnothing)=1\), and, for every allowed \(j\notin S\), update \(f_{i+1}(S\cup\{j\})\mathrel{+}=f_i(S)\). This recurrence is exhaustive and disjoint: the final assigned line is uniquely determined in each matching. The successive totals of all partial assignments are
\[
1,3,8,20,44,73,95,145,114,42,
\]
with \(f_9(\{0,\ldots,8\})=42\). The first standalone verifier implements this recurrence by depth-first traversal; the second uses an independently constructed Hamiltonian LCF model.

**2. Exact characterization of flips.** For perfect-matching permutations \(\sigma,\tau\), form \(\rho=\tau^{-1}\circ\sigma\) on the nine point indices. Every nontrivial \(k\)-cycle of \(\rho\) corresponds bijectively to a connected alternating \(2k\)-cycle of the symmetric difference of the matchings. Therefore a single hexagon flip is equivalent to \(\rho\) having exactly one nontrivial cycle of length three; a single octagon flip is equivalent to exactly one nontrivial cycle of length four. This equivalence verifies that the edge tests never confuse one alternating cycle with a union of cycles. The parity of \(\sigma\) is invariant under a three-cycle and reversed by a four-cycle.

**3. Exact finite connectivity certificate.** There are \(\binom{42}{2}=861\) unordered pairs of distinct states. The first verification program computes the cycle decomposition of \(\tau^{-1}\sigma\) for *all* these pairs, yielding \(72\) hexagon edges and \(108\) octagon edges. It finds \(21\) even and \(21\) odd states. Both parity classes are connected using hexagon flips. Each hexagon component has precisely three degree-six vertices (hubs). Removing them leaves three disjoint six-cycles, and each residual vertex has exactly one neighbour among the hubs. On each residual cycle these hub neighbours alternate between exactly two hubs, and the three cycles use each of the three unordered hub pairs exactly once. These exhaustive local properties give an explicit isomorphism of each parity component with \(H\), not merely agreement of its order or degree sequence. Breadth-first searches from every state establish diameter four in both components.

The octagon graph has six isolated states and a single connected thirty-six-state component. Combining the two edge sets yields a connected graph with \(180\) edges. Exhaustive breadth-first searches from each of its \(42\) states give the two sphere profiles stated above and the unordered distance histogram \((180,504,177)\). Since \(F_6\) is disconnected while \(F_{\le8}\) is connected and \(P\) has girth six, the least even cycle-length allowance ensuring connectivity is exactly eight. This proves the finding.

**4. Independent graph reconstruction.** The second verification program builds an eighteen-cycle with the repeated chord offsets \((5,7,-7,7,-7,-5)^3\). It independently obtains the bipartition, enumerates all perfect matchings by selecting edges on one side, recognizes a flip by the connectivity and degree-two condition of the symmetric difference, and independently computes the same component sizes, degree multiplicities, and shortest-path histogram. It additionally checks an explicit vertex bijection from the affine-incidence model to the LCF construction, proving that the two data models are isomorphic.

## Verification

Run `python3 verify_affine.py` and `python3 verify_lcf.py` with Python 3.9 or newer; the scripts use only the standard library, require no internet access and use no previously computed certificate files. Expected final markers are `AFFINE_PAPPUS_HEXAGON_OCTAGON_EXHAUSTIVE_PASS` and `LCF_PAPPUS_ALTERNATING_CYCLE_INDEPENDENT_PASS`. Both scripts were executed successfully from the delivered scientific contents. The first checker recomputes the matching and adjacency enumerations and performs full breadth-first searches. The combinatorial recurrence and the alternating-cycle permutation bijection explain why the finite search is exhaustive, rather than an extrapolation from a sample.

## Relationship to prior work

The incidence construction and the LCF representation of the Pappus graph are classical. Lei, Yeh and Zhang (2014) study alternating cycles and anti-forcing in perfect matchings; their stated main minimax theorem has a **planar bipartite** hypothesis and does not determine this nonplanar Pappus flip graph. Dyer, Jerrum and Müller (first public in 2015) study switches along four-cycles; the Pappus graph has no four-cycles, so their switch chain has no nontrivial moves here. Bau and Henning (2003) study matching transformation graphs of **cubic bipartite plane graphs**. Ito and coauthors (2019) study unrestricted alternating-cycle reconfiguration and its computational complexity; their general reachability statement does not determine the sharp length-six/eight cutoff or the exact metric for \(P\). None of these prior results implies the specific two parity components, their three-hub model, or the combined-graph distance profile. Related exact reconfiguration results on **other** cubic graphs do not transfer automatically to \(P\); the number and geometry of alternating cycles change with the graph.

## Limitations

This is an exact single-graph theorem, not a statement about all toroidal honeycomb graphs. The parity invariant by itself is standard, and the cardinality \(42\) is supporting context rather than an independently asserted first discovery. Some historical work on toroidal dimers or matching transformation graphs could contain an equivalent formulation not returned by searches. In particular, the complete text of Bau and Henning (2003) was not obtained, although its explicit planarity scope excludes the Pappus graph. The scientific checking here is self-review and executable finite verification; independent scholarly audit has not been performed.

## References

1. A. E. Brouwer, *Pappus graph*, graph notes, https://aeb.win.tue.nl/graphs/Pappus.html (incidence realization and nonplanar cubic geometry).
2. H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1, first public 2014-06-15, https://arxiv.org/abs/1406.3796.
3. M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725v1, first public 2015-01-30, https://arxiv.org/abs/1501.07725.
4. S. Bau and M. A. Henning, *Matching transformation graphs of cubic bipartite plane graphs*, Discrete Mathematics 262 (2003), 27–36, DOI:10.1016/S0012-365X(02)00519-8.
5. T. Ito, N. Kakimura, N. Kamiyama, Y. Kobayashi and Y. Okamoto, *Shortest Reconfiguration of Perfect Matchings via Alternating Cycles*, arXiv:1907.01700v1, first public 2019-07-03, https://arxiv.org/abs/1907.01700.
6. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html (LCF model and graph identification).
