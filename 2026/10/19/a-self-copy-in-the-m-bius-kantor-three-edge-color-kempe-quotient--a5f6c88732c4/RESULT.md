# A self-copy in the Möbius–Kantor three-edge-color Kempe quotient

## Finding
Let \(M=\operatorname{GP}(8,3)\) be the Möbius–Kantor graph. Its vertices are \(u_i,v_i\), \(i\in\mathbb Z/8\mathbb Z\), and its edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). A proper three-edge-coloring partitions its edges into three perfect matchings. Identify colorings that differ by a global permutation of the three color names. Join two distinct resulting partitions when one can be obtained from the other by interchanging two colors around **one connected** alternating two-color cycle, possibly after naming the colors.

The resulting color-unlabeled Kempe-switch graph is
\[
\mathcal K(M)\cong K_{1,3}\sqcup M.
\]
Thus one of its two components is a four-vertex star, while its other component is an exact graph-theoretic copy of the original sixteen-vertex Möbius–Kantor graph. There are precisely \(33\) perfect matchings, \(20\) unordered one-factorizations, and \(27\) quotient edges.

Keeping the three color names, the graph of all \(120\) proper edge-colorings under individual alternating-cycle switches has two components. The smaller has \(24\) vertices, \(54\) edges, radius and diameter \(3\), and degree distribution \(18\) vertices of degree \(4\) and \(6\) of degree \(6\). The larger has \(96\) vertices, \(288\) edges, radius and diameter \(4\), and is \(6\)-regular. These are exact finite assertions.

## Assumptions and scope
Graph edges are undirected and simple; arithmetic on subscripts is modulo \(8\). Each of the twenty-four edges receives exactly one color from \(\{0,1,2\}\), and the three edges meeting a vertex have distinct colors. Because the graph is cubic, each color class is necessarily a perfect matching. A Kempe switch is allowed on one maximal connected two-colored cycle at a time; simultaneous switches on separate cycles do not constitute one move. The unlabeled quotient discards global names of colors, but the latter labeled graph retains them. The named and unnamed graphs are different; their distances should not be conflated.

## Proof
The finite classification admits a complete constructive exhaustive proof supplied in `verify.py`, using a fixed vertex and edge order. All loops have explicit finite ranges, and the checks exhaust the space rather than sample it.

**Exhaustive generation.** Enumerate perfect matchings by taking the least uncovered vertex and recursively pairing it with one of its adjacent uncovered vertices; every perfect matching has exactly one branch at each recursion, so the resulting list is complete and duplicate-free. This produces \(33\) matchings. Every partition into three perfect matchings arises by choosing two disjoint matchings whose edge-complement is a matching; conversely every such triple is a valid partition. Sorting triples gives precisely \(20\) partitions. As an independent check, assign colors to all twenty-four edges by backtracking, excluding colors already incident to either endpoint. Fix colors on the three edges at vertex \(u_0\) in edge-index order to eliminate the global sixfold renaming symmetry. Every partition has exactly one such named representative; this entirely different generator yields the same twenty partitions.

**Exact quotient adjacency.** For each partition and each of its three color pairs, the union of those two matchings is a union of disjoint even cycles, because every vertex has degree two in the union. Interchanging along each connected cycle gives every possible one-step Kempe switch. Sorting the resulting color classes gives the exact quotient neighbors; switches that only rename the three color classes give loops and are omitted. A second, pairwise construction agrees: two distinct partitions are adjacent precisely when they share one matching and, for at least one choice of a remaining matching from each partition, the symmetric difference is a single connected alternating cycle. Both constructions yield \(27\) distinct edges and components of orders \(4\) and \(16\).

To certify the small component, label the twenty partitions \(0,\ldots,19\) by lexicographically sorting triples of their edge bitmasks, with bit \(j\) corresponding to edge \(j\) in the lexicographically ordered twenty-four-edge list. The four-vertex component is \(\{0,1,4,11\}\), with edges \(\{1,0\},\{1,4\},\{1,11\}\), hence it is \(K_{1,3}\). For the other sixteen partitions, the following explicit bijection \(f\) onto the original vertex indices \(0,\ldots,15\) proves the isomorphism:

| Partition index | 2 | 3 | 5 | 6 | 7 | 8 | 9 | 10 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(f\)(index) | 0 | 8 | 7 | 15 | 3 | 11 | 2 | 1 | 9 | 12 | 13 | 5 | 6 | 14 | 10 | 4 |

Here original indices \(0,\ldots,7\) denote \(u_0,\ldots,u_7\), and \(8,\ldots,15\) denote \(v_0,\ldots,v_7\). The checker constructs **all** \(\binom{16}{2}\) potential pairs and verifies that an edge joins two quotient states exactly when their images are adjacent in \(M\): the twenty-four image edges equal the twenty-four original edges. This verifies both directions of the claimed isomorphism, not merely degree sequences.

**Named colorings and distances.** Expand every one-factorization into its six ordered colorings. For each of the resulting \(120\) states, generate all distinct single-cycle Kempe switches and verify undirected reversibility. Exhaustive breadth-first search from every vertex in each component gives component orders \(24,96\), edge counts \(54,288\), and radii/diameters \(3,4\). The ordered-distance distributions, including the diagonal, are respectively \((24,108,360,84)\) for distances \(0,1,2,3\), and \((96,576,2592,4032,1920)\) for distances \(0,1,2,3,4\). These totals equal the squares of the corresponding component orders and independently check completeness of the distance search.

## Verification
Run `python3 verify.py` from the directory containing this report. It uses only Python's standard library. The file `verification_output.txt` contains one successful replay transcript from that exact source. The program asserts equality of independent generators and independent quotient adjacency constructions, the complete explicit isomorphism table, all component and edge counts, and all named-graph distances. These are finite complete verifications; no sampled experiment is used as an infinite proof.

## Relationship to prior work
The edge-Kempe equivalence relation and reconfiguration graphs are established in the primary work of Belcastro and Haas (2012/2014; 2017), and McDonald–Mohar–Scheide prove connectedness with four colors on subcubic graphs (2010/2012). Goedgebeur and Östergård (2021/2022) enumerate the **number** of edge-Kempe classes of all small cubic graphs, including the order-sixteen graphs. Their global classification and the existence of two classes here are prior coverage, not novelty by themselves. The new claim is the exact \(K_{1,3}\sqcup M\) graph-isomorphism type of the *unlabeled one-step* Kempe quotient, including the self-copy, and the exact metric and size structure of both *labeled* components. The inspected passages and sections of these primary works do not provide this particular quotient isomorphism or the labeled metric census. The arbitrary graph names “Möbius ladder” and “Möbius–Kantor graph” designate **different** objects; their results must not be conflated.

## Limitations
This theorem concerns one finite symmetric cubic graph, not an infinite family or all generalized Petersen graphs. The isomorphism is exhibited by an explicit finite index map, not claimed to be canonical, equivariant, or induced by an automorphism of \(M\). Similarities in the ordinary graph parameters of other cubic graphs do not imply the same Kempe graph. The computations have a self-contained verifier but have not undergone independent external validation. Unindexed previous exact computations or supplementary data could affect the novelty assessment.

## References
1. S.-M. Belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730 (public preprint 2012-09-08); Discrete Mathematics 325 (2014), 77–84. https://arxiv.org/abs/1209.1730
2. S.-M. Belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, Australasian Journal of Combinatorics 69(2) (2017), 197–214. https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363 (public preprint 2021-05-04); Discrete Mathematics 345 (2022), 112963. https://arxiv.org/abs/2105.01363
4. J. McDonald, B. Mohar, and D. Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248 (first public preprint 2010-05-13); Journal of Graph Theory 70 (2012), 226–239. https://arxiv.org/abs/1005.2248
