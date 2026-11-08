# A mixed-dimensional sphere wedge for the cuboctahedral five-cut complex

## Finding
Let \(C=L(Q_3)\) be the twelve-vertex cuboctahedral graph, obtained as the line graph of the ordinary three-dimensional cube. Its **ordinary five-cut complex** satisfies the complete integral homotopy equivalence
\[
\boxed{\Delta_5(C)\simeq \bigvee^{12}S^5\vee\bigvee^{118}S^6.}
\]
Thus the reduced integral homology is \(\mathbb Z^{12}\) in dimension five, \(\mathbb Z^{118}\) in dimension six and zero in all other dimensions; in particular it is torsion-free. The complex is pure six-dimensional but **not shellable** because it has nonzero degree-five reduced homology.

## Assumptions and scope
All graphs are finite, simple and undirected. Represent the eight cube vertices by binary integers \(0,\ldots,7\), joining distinct vertices when their binary representations differ in one position. Order the twelve cube edges \((u,v)\), with \(u<v\), lexicographically. These edges become vertices \(0,\ldots,11\) of the cuboctahedral graph \(C\); two are joined exactly when the underlying cube edges share an endpoint. This gives a four-regular graph with twelve vertices and twenty-four edges.

For each \(T\subseteq V(C)\) of cardinality five, call \(T\) *disconnected* when the induced graph \(C[T]\) has at least two connected components. The facets of the **ordinary** five-cut complex \(\Delta_5(C)\) are precisely the seven-vertex sets \(V(C)\setminus T\) for disconnected \(T\), together with all their subsets. This differs from the total five-cut complex, which instead requires independent sets \(T\). The empty set is included as a face, but excluded from nonempty face-poset matchings.

## Proof
**Facets and faces.** There are \(\binom{12}{5}=792\) five-element vertex subsets. Exact component enumeration gives 516 disconnected five-subsets and 276 connected ones. Therefore \(\Delta_5(C)\) has 516 facets of cardinality seven. Exhausting all subsets of these facets gives exactly 2,974 faces including the empty face and the nonempty face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6)
=(12,66,220,495,792,872,516).
\]
The independent full-mask membership test in the supplied verifier checks every one of the \(2^{12}\) subsets against these facets and agrees with the complete face enumeration. The complex is pure of dimension six; it misses 52 of the 924 possible six-vertex faces, and its reduced Euler characteristic is \(118-12=106\).

**Two exhaustive acyclic matchings.** Process the twelve vertices in increasing order. At each stage, among faces not previously paired, match a face \(\sigma\) not containing the current vertex \(v\) with \(\sigma\cup\{v\}\) whenever both are currently available, removing the two faces. This yields 1,418 disjoint pairs and critical cells: one vertex, fifteen five-cells and 121 six-cells. Orient every unmatched Hasse cover from the larger face to the smaller face and every matched cover oppositely. An exhaustive topological sort succeeds on all 2,973 nonempty faces and visits every one of the 15,576 Hasse incidences, proving acyclicity.

Repeating with the reverse vertex order gives **a different acyclic matching** of 1,420 pairs, whose critical cells are one vertex, thirteen five-cells and 119 six-cells. All 15,576 incidence orientations again pass exhaustive acyclicity verification. Both matchings provide CW models with no cells in degrees one through four.

**Exact integral attaching data.** Orient simplices by ascending vertex order. For each acyclic matching, eliminate matched lower faces using the signed simplicial boundary of their paired upper faces. Recursive substitution (over the integers) computes the discrete-Morse cellular differential from the critical six-cells to the critical five-cells. In the forward matching its \(15\times121\) integer matrix has rational rank three and a \(3\times3\) minor of determinant \(+1\), using zero-indexed rows and columns \((0,1,6)\). In the reverse matching its \(13\times119\) matrix has rank one and a \(1\times1\) minor of determinant \(+1\), using row \(4\), column \(18\). All entries in both matrices belong to \(\{-1,0,1\}\).

A unit maximal-rank determinant forces every nonzero Smith invariant factor to be one. The integral Morse homology groups therefore have ranks \(15-3=13-1=12\) in dimension five and \(121-3=119-1=118\) in dimension six, with no torsion. More strongly, the five-skeleta of these CW models are wedges of five-spheres. Their six-cell attaching maps are determined completely by integral degree vectors because \(\pi_5(\bigvee^mS^5)\cong\mathbb Z^m\) for \(m\ge1\). Integral basis transformations reduce a full-rank primitive degree matrix to identity and zero blocks. Canceling the unit-degree cell pairs therefore leaves exactly twelve five-spheres and 118 six-spheres. This establishes the **integral homotopy equivalence**, not merely homology ranks. As a pure shellable six-complex can have reduced homology only in degree six, the nonzero fifth homology proves non-shellability.

## Verification
The package's `verification/check_cuboctahedral_fivecut.py` uses only Python 3 standard-library functions. From cube bit arithmetic it independently constructs the twelve line-graph vertices, all connectedness predicates, 516 facets and 2,974 simplicial faces. It explicitly computes both disjoint matchings, checks all 15,576 Hasse covers and both directed acyclicity conditions, builds the signed Morse boundary matrices and certifies the ranks and unit minors using exact rational and integer operations.

The separate simplicial boundary computation over \(\mathbb F_2\) obtains ranks 462 and 398 for the boundary maps from simplicial chain degree five to four and from six to five. Therefore its fifth and sixth mod-two Betti numbers are \(872-462-398=12\) and \(516-398=118\), independently corroborating the integral Morse calculation. Run from the package directory:

```text
python3 verification/check_cuboctahedral_fivecut.py
```

Its exact reproducible output is recorded in `verification/check_output.txt`.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue [1] introduce ordinary cut complexes and study exact topology for several families, including trees, cycles, multipartite graphs and prisms over cliques. Their high-skeleton theorem (Theorem 6.1) does not cover this graph's five-cut complex: here 52 six-vertex faces are absent, so the next-to-top skeleton is not complete. The subsequent work [2] analyzes disjoint unions, squared paths and rectangular grid graphs, none of which equals the line graph of the cube.

The previously published exact classification of the **three-cut** complex of the same cuboctahedral graph gives \(\Delta_3(C)\simeq S^7\vee\bigvee^6S^8\). The three-cut and five-cut complexes have different generating facets and dimensions, so that result does not imply the present type. Existing matching-complex, independence-complex and metric Čech classifications for the same graph likewise concern different simplices. A literature and recorded-result comparison using the graph's cuboctahedral and line-graph descriptions found no implication covering this exact five-cut homotopy type.

## Limitations
The assertion concerns only the ordinary five-cut complex of the specified cuboctahedral graph; it does not establish a classification across all line graphs or higher-dimensional cubes, a natural equivariant sphere-wedge decomposition, or inclusion-induced persistence maps for different cut parameters. The proof uses finite exhaustive enumeration and exact integer certificate checks; no inference from a truncated experiment is needed. Coverage checks cannot exclude an unindexed or inaccessible equivalent work, and independent external review has not been performed.

## References
[1] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Rowan Rowlands, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, first publicly posted 2023-04-26.

[2] Margaret Bayer, Mark Denker, Marija Jelić Milutinović, Sheila Sundaram, and Lei Xue, *Topology of Cut Complexes II*, arXiv:2407.08158v1, first publicly posted 2024-07-11.

[3] *The cuboctahedral three-cut complex is a mixed-dimensional sphere wedge*, published mathematical-result record (2026). Distinct cut parameter and homotopy degrees.
