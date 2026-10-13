# All minimum identifying sets of sixteen-point biplanes

## Finding
Let \((X,\mathcal B)\) be any symmetric \(2\!-(16,6,2)\) incidence design. A point subset \(C\subseteq X\) *identifies the blocks* if each trace \(B\cap C\), for \(B\in\mathcal B\), is nonempty and all these traces are distinct.

**Theorem.** The minimum cardinality of such a point subset is \(5\). Moreover, a five-point set is identifying if and only if it equals \(B\setminus\{x\}\) for some block \(B\) and point \(x\in B\), and this representation is unique. Consequently every such biplane has exactly \(96\) identifying subsets of minimum cardinality.

**Graph corollary.** Let \(G\) be the five-regular Clebsch graph (the folded five-cube), with vertices \(\mathbb F_2^4\) and edges between labels differing by one of \(0001,0010,0100,1000,1111\). Then \(\gamma^{\mathrm{ID}}(G)=5\). All \(96\) minimum identifying codes are the \(16\) open neighborhoods \(N(v)\) and the \(80\) punctured closed neighborhoods \(N[v]\setminus\{w\}\) with \(w\in N(v)\). The former induce an edgeless five-vertex subgraph; the latter induce a star with four leaves.

## Assumptions and scope
A symmetric \(2\!-(16,6,2)\) design has sixteen points, sixteen distinct blocks, six points in every block, and exactly two blocks through every pair of distinct points. Standard incidence counting gives six blocks through each point and, by symmetry, exactly two points in the intersection of any two distinct blocks. All points and blocks are labeled for the enumeration; no equivalence by automorphisms is taken. Identification requires both nonempty and distinct traces, as in closed-neighborhood identifying codes of graphs.

The graph is specified explicitly because the name 'Clebsch graph' is occasionally used for its ten-regular complement. All assertions here about identifying codes concern the **five-regular** graph.

## Proof
**Lower bound.** With \(|C|=c\), the \(16\) different nonempty traces are among \(2^c-1\) possible subsets. Since \(2^4-1=15<16\), every identifying set has at least \(5\) points.

**Every punctured block works.** Fix a block \(B\) and a point \(x\in B\); put \(C=B\setminus\{x\}\). Among the other fifteen blocks, the intersections with \(B\) are exactly the fifteen distinct two-element subsets of \(B\). Indeed, two blocks meet in two points, and any two points of \(B\) lie together in precisely one additional block. The fifteen distinct traces on \(C\) are therefore the ten two-element subsets of \(C\) and the five singleton subsets of \(C\). The remaining trace, from \(B\) itself, is all of \(C\). Thus all sixteen traces are distinct and nonempty.

**There are no other minima.** Let \(|C|=5\) and suppose all traces are different and nonempty. Write \(a_j=|\{B\in\mathcal B:|B\cap C|=j\}|\) for \(1\le j\le5\). The design identities give
\[
\sum_{j=1}^{5}a_j=16,\qquad
\sum_{j=1}^{5}j a_j=30,\qquad
\sum_{j=1}^{5}\binom j2 a_j=20.
\]
The trace uniqueness also gives \(a_1\le5\), \(a_2\le10\), and \(a_5\le1\). Subtracting the first two moments from twice the pair moment gives
\[
2a_3+6a_4+12a_5=12.
\]
If \(a_5=0\), then \((a_3,a_4)\) is one of \((6,0),(3,1),(0,2)\). The first two moments then force \((a_1,a_2)\) to be respectively \((8,2),(7,5),(6,8)\), all contradicting \(a_1\le5\). Therefore \(a_5=1\), whence \(a_3=a_4=0\), \(a_1=5\), and \(a_2=10\). Exactly one block contains all five points of \(C\), proving \(C=B\setminus\{x\}\) and uniqueness of \(B\) and \(x\).

There are \(16\cdot6=96\) distinct punctured blocks: if a five-point subset lay in two blocks, those blocks would intersect in at least five points, contrary to their intersection size two.

**Graph specialization.** For \(v\in\mathbb F_2^4\), let \(N[v]=\{v\}\cup\{v+e_1,v+e_2,v+e_3,v+e_4,v+(1,1,1,1)\}\). These sixteen sets each have size six. Distinct sets intersect in two points: adjacent graph vertices have no common open neighbor and contribute the two endpoints, while nonadjacent graph vertices have exactly two common open neighbors. The closed neighborhoods therefore form a symmetric \(2\!-(16,6,2)\) design. Identification of these blocks by \(C\) is precisely the identifying-code condition for \(G\). Deleting the center \(v\) yields an open neighborhood \(N(v)\), and deleting any of its five neighbors yields \(N[v]\setminus\{w\}\). Every such open neighborhood is independent since the graph is triangle-free; the other sets induce a four-leaf star centered at \(v\). The total is \(16+16\cdot5=96\), with no duplication by the theorem.

## Verification
A standalone Python 3 standard-library checker, `verify.py`, builds the sixteen Cayley-graph closed-neighborhood masks, checks all design incidence conditions, enumerates all \(2^{16}=65\,536\) point subsets, and identifies the complete set of minimum codes. It independently compares the result with the punctured-block construction, tests the two graph types, and checks the full code-cardinality spectrum. It prints a single `VERIFY_OK` line on success; it needs no external package or input file. Run `python verify.py`.

The universal biplane theorem relies on the preceding incidence proof, not on these finite graph calculations. There is no claim about larger or asymmetric designs, nor about uniqueness up to design isomorphism.

## Relationship to prior work
Assmus and Salwach (1979) classified the three nonisomorphic biplanes with these parameters, and Bhattacharya and Smith (2008) studied their difference-set constructions. Neither source's investigated algebraic/code-theoretic classifications directly enumerate point subsets producing sixteen distinct nonempty block traces. Gravier, Parreau, Rottey, Storme and Vandomme (2015; public preprint 2014) develop identifying codes in vertex-transitive and strongly regular graphs and investigate generalized quadrangles, but do not provide the punctured-block theorem or this graph's complete minimum-code classification. Bailey's metric-dimension table supplies a different invariant: metric dimension four for the five-regular Clebsch graph; it neither implies the minimum identifying-code value nor the \(96\) solutions.

The proof uses standard symmetric-design incidence identities as input, not as new theorems. Priority under terminology such as block-separating points, distinguishing point tests or identifying families remains a genuine literature-search uncertainty.

## Limitations
The result is an exact theorem for the fixed symmetric design parameters \(2\!-(16,6,2)\) and the specified graph, not an assertion of a general formula for all biplanes. A direct published equivalence under alternative separation terminology may exist despite the searches described in the review. The graph verifier is independent arithmetic corroboration of the finite specialization, not an external audit or a substitute for the universal proof.

## References
- E. F. Assmus Jr. and C. J. Salwach, 'The (16,6,2) designs', *International Journal of Mathematics and Mathematical Sciences* **2** (1979), 261–281. DOI: 10.1155/S0161171279000247.
- C. Bhattacharya and K. W. Smith, 'Factoring (16,6,2) Hadamard Difference Sets', *Electronic Journal of Combinatorics* **15** (2008), #R112, published 2008-08-31. DOI: 10.37236/836.
- S. Gravier, A. Parreau, S. Rottey, L. Storme and E. Vandomme, 'Identifying Codes in Vertex-Transitive Graphs and Strongly Regular Graphs', *Electronic Journal of Combinatorics* **22** (2015), #P4.6, arXiv:1411.5275 (v1 published 2014-11-19).
- R. F. Bailey, 'The metric dimension of small distance-regular and strongly regular graphs', arXiv:1312.4973, Table 1.
