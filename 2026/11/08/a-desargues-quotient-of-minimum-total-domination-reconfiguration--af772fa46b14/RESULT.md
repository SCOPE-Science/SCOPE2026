# A Desargues quotient of minimum total-domination reconfiguration on the dodecahedral graph

## Finding
Let \(D=GP(10,2)\) be the dodecahedral graph. Exactly \(190\) minimum total dominating sets exist, each of size \(8\). A *token jump* replaces one selected vertex by any distinct unselected vertex, provided the new set is again a minimum total dominating set. A *token slide* is a token jump constrained to an edge of the original graph. The slide graph consists of \(190\) isolated configurations. The jump graph has \(360\) edges, forty isolated vertices, and one connected component \(X\) with \(150\) vertices, whose radius and diameter both equal \(10\).

The nontrivial component has precisely \(120\) degree-four configurations and \(30\) degree-eight configurations. Its degree-four vertices induce twenty vertex-disjoint hexagons. Each degree-eight configuration neighbors exactly four vertices in each of two distinct hexagons. Form the *hexagon-incidence quotient* \(Q\): one vertex per hexagon, one edge per degree-eight configuration between its two adjacent hexagons. This is a simple cubic graph, and
\[
Q\cong GP(10,3),
\]
the Desargues graph. Thus the twenty hexagons and thirty degree-eight configurations have an exact unexpected incidence geometry distinct from the original dodecahedral graph.

The \(190\) optima form five orbits under \(\operatorname{Aut}(D)\), of sizes \(60,60,30,30,10\); their respective token-jump degrees are \(4,4,8,0,0\). The two isolated orbits account for forty frozen configurations even under jumps.

## Assumptions and scope
Use vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\) and edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+2}\), with indices modulo ten. The code labels \(u_i\) by integer \(i\) and \(v_i\) by \(10+i\), for \(0\le i<10\). These edges define a simple, cubic, 20-vertex graph.

For any subset \(T\) of vertices, define its *open-neighborhood coverage* \(N(T)=\bigcup_{t\in T}N(t)\). Total domination means \(N(T)=V(D)\), including the requirement that every vertex of \(T\) itself has a neighbor in \(T\). All configurations and all allowed transitions in the theorem have minimum cardinality. The quotient \(Q\) is formed by the incidence construction above, not by an ordinary edge contraction that retains parallel edges.

## Proof
**Exact finite-state characterization.** Write each vertex subset \(T\) as its 20-bit mask \(m(T)\). For vertex \(t\), let \(b_t\) be the bitmask of its three open neighbors. Then
\[
T\text{ is total dominating}\quad\Longleftrightarrow\quad\bigvee_{t\in T}b_t=2^{20}-1.
\]
This is an if-and-only-if, so checking the finite list of all subsets of cardinality at most eight is a complete decision procedure for both the minimum and the collection of all minimizers. The first attached program loops through every \(\binom{20}{k}\) subset for each \(0\le k\le8\) and obtains counts \(0,0,0,0,0,0,0,0,190\). Consequently the minimum is eight and all \(190\) minimizers are explicitly represented, with none omitted. Higher-cardinality subsets cannot challenge that minimum.

**Exact transitions.** For each optimal mask \(m\), every ordered selected-unselected pair \((a,b)\) produces the unique proposed replacement \(m'=m\mathbin{\mathrm{xor}}2^a\mathbin{\mathrm{xor}}2^b\). The replacement is legal exactly when \(m'\) lies in the enumerated optimal-mask set; it is a slide exactly when \(a\sim b\) in \(D\). Exhausting these pairs gives no slides and gives \(360\) distinct undirected jump edges. Its jump-degree histogram is \(40\) of degree \(0\), \(120\) of degree \(4\), and \(30\) of degree \(8\). Complete graph traversal yields forty singleton components and one component of size \(150\). Breadth-first search from **each** of its 150 vertices gives eccentricity exactly \(10\), proving both radius and diameter equal ten.

**Hexagon geometry and quotient.** Restrict the jump graph to its degree-four configurations. The code enumerates every component of this induced graph: exactly twenty connected components, each containing six vertices, and each vertex has degree two in that induced graph. Thus each is a simple six-cycle. Every one of the 30 degree-eight configurations has its eight neighbors in precisely two of these cycles, with multiplicities four and four. The thirty resulting two-element cycle incidences are distinct, and each of the twenty cycles is incident to three of them. Therefore the quotient \(Q\) is a simple cubic graph with twenty vertices and thirty edges.

An explicit isomorphism certificate is embedded in `check_gp.py`: index the twenty hexagons lexicographically by the sorted list of their 8-set indices, where the 8-sets are enumerated in lexicographic combinations of \(\{0,\ldots,19\}\). Their images in the ordinary vertex labeling \(0,\ldots,19\) of \(GP(10,3)\) are, in order,

`[0,1,3,2,12,11,17,14,13,4,5,18,10,19,9,8,16,15,7,6]`.

The attached checker verifies that this list is a bijection and that its image sends the entire 30-edge quotient edge set to the explicit edges \(u_iu_{i+1}\), \(u_iv_i\), \(v_iv_{i+3}\) (modulo ten). Equality of both 30-edge sets proves the graph isomorphism, without relying on pictures or matching only numerical invariants.

**Symmetry orbits.** Two explicit 20-vertex permutations in `check_gp.py` preserve every edge and generate 120 permutations. Each of the resulting five set orbits has the asserted size and degree. The checker separately enumerates **every** adjacency-preserving permutation of the twenty vertices by exact constraint backtracking and finds exactly 120. This independent full-group test proves that the 120 generated permutations constitute the full automorphism group. This certifies the orbit decomposition.

## Verification
Run `python3 check_gp.py` and `python3 check_lcf.py` in any Python 3 environment; both use only the standard library and assert all critical numerical and structural conclusions before emitting JSON. Expected outputs are supplied in `check_gp.out` and `check_lcf.out`.

The first program uses the explicit \(GP(10,2)\) presentation, enumerates all candidate subsets through size eight, constructs transitions by selected-unselected swaps, tests an explicit 20-vertex quotient-isomorphism certificate, and checks 120 automorphisms. The independent second program constructs the dodecahedron by the 20-vertex LCF presentation `[10,7,4,-4,-7,10,-4,7,-7,4]^2`, scans all 20-bit masks with cardinality at most eight, constructs transitions by **pairs of optimal sets**, and obtains its quotient isomorphism by fresh backtracking rather than the first program's prescribed mapping. It also computes every nontrivial-component eccentricity. Both terminate with the exact values in the theorem. No randomness, inaccessible file, solver, or remote dependency is used.

## Relationship to prior work
Kang's 2012 work defines total domination value and gives counts for complete multipartite graphs, paths and cycles, but not these dodecahedral optimal-state relocation graphs. Godbole, Jamieson and Jamieson (2013) investigate extremal *numbers* of minimum total dominating sets in arbitrary graphs; those theorems do not classify the present 150-state component. Santhanam and Sudha (2014), Section 3 and Example 3.3, explicitly construct a minimum total dominating set on this **same graph** \(P(10,2)\); the minimum cardinality and that one example are not claimed as new. The inspected paper does not enumerate all optimal configurations or define token reconfiguration and the hexagon-incidence quotient. Zhao and collaborators (2020) investigate total-domination invariants on generalized Petersen graphs and must also be acknowledged as related background. General graph databases can supply optimal subsets; availability of those subsets alone does not state the transition geometry or its explicit Desargues quotient.

The added result is the complete relocation and quotient structure, not a renamed minimum domination number, an unmotivated subfamily, or a mere table of counts.

## Limitations
This is a finite exact theorem for the dodecahedral graph only; no analogous classification is established for general \(GP(n,k)\). The two source representations are standard and equivalent, but the standalone checkers prove only the properties they actually assert. Independent scholarly verification and a comprehensive historical-priority determination have not been performed. Source search and comparison reduce but cannot eliminate the risk of unindexed equivalent work, particularly graph-data computations or hard-to-index specialized discussions. The public 2014 article was reviewed in extracted text; attempts to retrieve page-image screenshots were unsuccessful, so image-dependent details were not used to infer noncoverage.

## References
1. Cong X. Kang, *Total Domination Value in Graphs* (submitted April 18, 2012), arXiv:1204.3970, https://arxiv.org/abs/1204.3970.
2. Anant Godbole, Jessie Jamieson and William Jamieson, *Maximum Number of Minimum Dominating and Minimum Total Dominating Sets* (submitted August 14, 2013), arXiv:1308.3178, https://arxiv.org/abs/1308.3178.
3. R. Alphonse Santhanam and S. Sudha, *Total Domination on Generalized Petersen Graphs*, International Journal of Scientific and Innovative Mathematical Research 2(2) (February 2014), pp. 149–155, https://www.arcjournals.org/pdfs/ijsimr/v2-i2/5.pdf.
4. Taiyin Zhao et al., *The Numerical Invariants concerning the Total Domination for Generalized Petersen Graphs*, Journal of Mathematics (2020), doi:10.1155/2020/5473675.
5. Wolfram MathWorld, *Dodecahedral Graph*, https://mathworld.wolfram.com/DodecahedralGraph.html.
6. Wolfram Documentation, *GraphData* property catalogue, https://reference.wolfram.com/language/ref/GraphData.html.
