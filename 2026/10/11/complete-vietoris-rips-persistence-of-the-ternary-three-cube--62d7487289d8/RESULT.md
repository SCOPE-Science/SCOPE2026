# Complete Vietoris–Rips persistence of the ternary three-cube

## Finding

Put \(T=\{0,1,2\}^{3}\) and let \(d(x,y)\) count coordinates in which \(x\) and \(y\) differ. For every real \(r\ge0\), the *inclusive* Vietoris–Rips complex \(R_r=\operatorname{VR}_{\le r}(T)\) is the flag complex whose nonempty faces have pairwise Hamming distance at most \(r\). There are four homotopy regimes:

\[
R_r\simeq
\begin{cases}
\bigsqcup^{27}\{*\},&0\le r<1,\\
\bigvee^{28}S^1,&1\le r<2,\\
\bigvee^{46}S^3,&2\le r<3,\\
\{*\},&r\ge3.
\end{cases}
\]

In particular, the entire *reduced integral persistent homology* is a direct sum of 26 interval modules in degree zero, 28 in degree one and 46 in degree three, with respective half-open intervals \([0,1)\), \([1,2)\), and \([2,3)\); all other reduced intervals are absent. Here each interval module carries a copy of \(\mathbb Z\) at parameters inside its interval and zero elsewhere. The unreduced degree-zero module additionally contains one infinite bar.

At the intermediate threshold,
\[
R_2=\operatorname{Ind}(K_3\times K_3\times K_3)\simeq\bigvee^{46}S^3,
\]
where the product is the categorical graph product. This verifies precisely the equal-three-factor instance of the homotopy-type prediction in Antolín Camarena–Carnero Bravo (2023, Conjecture 26), without claiming their unrestricted conjecture.

## Assumptions and scope

The metric is the discrete three-coordinate Hamming metric, not the Euclidean metric and not the metric on the continuous edges of a graph. The parameter is any real \(r\ge0\). The Rips convention is \(\le r\), so birth and death endpoints are as displayed. Vertex order is lexicographic, \((a,b,c)\leftrightarrow 9a+3b+c\), for \(a,b,c\in\{0,1,2\}\). A simplicial face is nonempty unless explicitly discussing an augmented chain complex. All homotopy types mean geometric realizations.

## Proof

**The regimes below scale two.** At \(0\le r<1\), distinct vertices are not adjacent. For \(1\le r<2\), two vertices are adjacent exactly when they differ in one coordinate; these are the edges of \(K_3\square K_3\square K_3\). Every triangle in the flag complex consists of all three values on a single coordinate line with the other two coordinates fixed. Indeed, if two distinct points differ only in coordinate \(j\), any vertex at distance one from both must agree on all other coordinates. There are exactly \(3\cdot3^2=27\) such coordinate triangles, and their edges are pairwise disjoint. Each triangle has a free edge and can be simplicially collapsed with that edge. The remaining connected graph has 27 vertices and \(81-27=54\) edges, hence first Betti number \(54-27+1=28\). A connected graph of this cycle rank is homotopy equivalent to a wedge of 28 circles.

**The scale-two identification.** A pair of distinct triples has distance at most two if and only if they agree in at least one coordinate. Conversely, edges in the categorical product \(K_3\times K_3\times K_3\) join precisely the pairs differing in all three coordinates. Accordingly, the independence complex of that categorical product is *identically* the scale-two Rips complex, not just homotopy equivalent to it.

**Exact acyclic matching at scale two.** Represent each nonempty face by the 27-bit integer whose bit indexed by \(9a+3b+c\) records the presence of \((a,b,c)\). Enumerate all clique faces by the standard increasing-vertex backtracking rule, intersecting the candidate set with the current vertex's allowed adjacency mask. The precise implementation is the accompanying standard-library-only `verify.py`; it builds from the metric and does not load any stored face list or previously saved computation. It enumerates exactly 5,949 distinct nonempty faces, with dimension-ordered face vector

\[
(f_0,f_1,\ldots,f_8)=(27,243,945,1728,1620,945,351,81,9).
\]

Construct a matching on the *nonempty* face poset as follows. Start with every face unmatched. For \(i=0,1,\ldots,26\), simultaneously pair every still-unmatched face \(\sigma\) not containing vertex \(i\) with \(\sigma\cup\{i\}\) whenever the latter is also still unmatched; immediately remove those two faces from the unmatched set before advancing to the next \(i\). For each fixed \(i\), no face can belong to two of these pairs, and the two faces differ by exactly one vertex. All pairs therefore are valid face-poset cover edges.

The exact checker obtains 2,951 pairs and precisely 47 unmatched faces: singleton \(\{(0,0,0)\}\) and 46 tetrahedra (three-dimensional simplices). For a complete acyclicity certificate, orient every codimension-one face-poset incidence \(\tau\subset\sigma\) downward \(\sigma\to\tau\), except that every matched incidence is reversed \(\tau\to\sigma\). The program enumerates all 27,189 such directed incidences and runs Kahn's topological sorting algorithm on all 5,949 nonempty faces. It visits every vertex, proving the entire orientation acyclic. This exhaustive finite check establishes a valid discrete-Morse matching, not a sample or statistical test.

By the acyclic-matching theorem of discrete Morse theory, the resulting finite simplicial complex is homotopy equivalent to a CW complex having exactly one 0-cell and exactly 46 3-cells and no cells in other dimensions. Every 3-cell has its attaching map into the sole 0-cell (because there are no 1- or 2-cells), so the CW complex is a wedge of 46 3-spheres. This conclusion holds over \(\mathbb Z\), not only mod two.

**The final threshold and persistence.** All triple distances are at most three, so \(R_r\) is the full 26-simplex for \(r\ge3\). The complexes change only at integer distances 1, 2 and 3. In any given positive homological degree, the nonzero reduced group appears in just one consecutive scale regime; all maps leaving that regime land in zero. In reduced degree zero, 26 generators die at threshold 1; one unreduced generator survives forever. Therefore the exact integral interval-module decomposition is as stated.

## Verification

Run `python3 verify.py` with Python 3 and no third-party libraries. The program reconstructs all stages directly from the Hamming metric, checks the coordinate-triangle collapse input, all face counts, matching construction, every codimension-one Hasse incidence, and full acyclicity. As a logically separate consistency check it computes mod-two ranks of every positive simplicial boundary map in the scale-two complex; the ranks are \((26,217,728,954,666,279,72,9)\), yielding reduced mod-two homology only in degree three, with dimension 46. The mod-two calculation corroborates the result but is **not** used as a substitute for the integral homotopy proof. Successful standalone execution prints `VERIFY_OK`.

## Relationship to prior work

Adams–Frick–Virk (first public June 17, 2022; primary MSC 55N31) place Vietoris–Rips complexes and persistent homotopy information in a general metric-topology framework, but do not calculate the ternary three-cube filtration. Goyal–Shukla–Singh (2019) calculate independence complexes of two-factor categorical complete-graph products and describe face toggles as a discrete-Morse method, not the complete three-factor case. Antolín Camarena–Carnero Bravo (2023) prove their homotopy result when one factor is \(K_2\), then explicitly state the general three-factor formula as Conjecture 26. The present scale-two result handles the case with three \(K_3\) factors, outside their proved factor-two range. The entire integral Rips barcode is an additional metric-topology conclusion.

## Limitations

The statement concerns **exactly** the 27-point ternary three-cube with the specified Hamming distance and inclusive filtration. It does not establish the predicted formula for larger alphabet sizes or for other products of three complete graphs. The finite exhaustive acyclicity certificate proves this one fixed complex, not an infinite-parameter theorem; the checker requires ordinary trust in Python execution and integer arithmetic. Mathematical originality may be limited by an unindexed equivalent theorem or computational record. No independent audit has been performed.

## References

1. H. Adams, F. Frick, and Ž. Virk, “Vietoris thickenings and complexes have isomorphic homotopy groups,” arXiv:2206.08812 (first public June 17, 2022), https://arxiv.org/abs/2206.08812.
2. S. Goyal, S. Shukla, and A. Singh, “Homotopy Type of Independence Complexes of Certain Families of Graphs,” arXiv:1905.06926 (May 16, 2019), especially Section 3, https://arxiv.org/html/1905.06926v1.
3. O. Antolín Camarena and A. Carnero Bravo, “Homotopy type of the independence complex of some categorical products of graphs,” arXiv:2307.12401 (first public July 23, 2023), especially Proposition 25 and Conjecture 26, https://arxiv.org/html/2307.12401v2.
4. R. Forman, “Morse Theory for Cell Complexes,” Advances in Mathematics 134 (1998), 90–145; standard acyclic-matching formulation as cited in Goyal–Shukla–Singh.
