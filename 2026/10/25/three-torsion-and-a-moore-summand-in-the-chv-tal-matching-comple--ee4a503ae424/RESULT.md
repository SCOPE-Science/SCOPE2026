# Three-torsion and a Moore summand in the Chvátal matching complex

## Finding

Let \(G\) be the twelve-vertex Chvátal graph and let \(\mathcal M(G)\) be its ordinary matching complex: vertices of the simplicial complex are edges of \(G\), and its faces are pairwise vertex-disjoint collections of graph edges. Then
\[
\boxed{\mathcal M(G)\simeq \left(\bigvee^{28} S^3\right)\vee M(\mathbb Z/3\mathbb Z,3),}
\]
where the Moore space \(M(\mathbb Z/3\mathbb Z,3)\) is \(S^3\) with one four-cell attached by a map of degree \(3\). Thus
\[
\widetilde H_i(\mathcal M(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{28}\oplus\mathbb Z/3\mathbb Z,&i=3,\\
0,&i\ne3.
\end{cases}
\]
In particular, the complex is two-connected but is not homotopy equivalent to a wedge of spheres. The assertion is a homotopy classification, not merely an integral homology computation.

## Assumptions and scope

The Chvátal graph is the classical twelve-vertex, twenty-four-edge, four-regular, triangle-free, four-chromatic graph introduced in 1970. To make the assertion independent of any graph library's labeling, take the vertex set \(\{0,1,\ldots,11\}\) and the following complete undirected edge set, listed lexicographically:

```
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

Each nonempty matching is one simplex; the empty matching is the empty face. A face's bitmask has bit \(j\) set exactly when it contains edge \(j\) in the list above, with numbering beginning at zero. All homotopy types refer to geometric realizations, with integral coefficients unless specified otherwise.

## Proof

**1. Exhaustive face construction.** Start from the empty edge set and process the twenty-four edges in the displayed order. An existing face is extended by the new edge if and only if its two endpoints have not yet been used by any edge of the face. This enumerates every matching once: its largest indexed edge is introduced at the unique final step in which that matching can first appear. The resulting nonempty face vector, in dimensions zero through five, is
\[
(24,204,752,1175,628,52),
\]
so the complex has exactly \(2835\) nonempty faces. A matching has at most six edges since the graph has twelve vertices.

**2. An acyclic face-poset matching.** Process the potential matching-complex vertices (that is, graph edges) in this exact order of zero-based edge indices:

```
9 11 10 15 2 13 23 8 14 21 1 0 6 4 3 16 19 17 12 18 5 20 22 7
```

At each stage, among currently unmatched nonempty simplices, pair every face not containing the chosen edge-index with its one-edge extension if both are still unmatched; process candidate lower faces in increasing order of cardinality and then integer bitmask. Such a pair is always a codimension-one face–coface incidence. The recipe yields \(1397\) disjoint pairs and precisely one critical vertex, thirty-four critical three-faces, and six critical four-faces. These counts account for every nonempty simplex.

For acyclicity, orient every matched Hasse incidence upward and every other nonempty face–coface incidence downward. The directed Hasse graph has exactly \(2835\) nodes and \(10816\) arcs. The supplied finite verifier reconstructs every arc and exhaustively removes vertices of indegree zero. It removes all \(2835\) nodes, proving the directed graph acyclic. Forman's discrete Morse theorem therefore provides a CW complex with one zero-cell, thirty-four three-cells, six four-cells, and no other cells, homotopy equivalent to the matching complex.

**3. The signed Morse boundary.** Orient simplices by their increasing edge indices. The simplicial boundary of a face \([e_0<\cdots<e_d]\) is \(\sum_{j=0}^d(-1)^j[e_0<\cdots<\widehat e_j<\cdots<e_d]\). The Morse boundary is obtained by reducing this expression along each gradient pair. More explicitly, if a lower matched face \(a\) is paired with upper face \(b\) and \(\langle a,\partial b\rangle=s\in\{1,-1\}\), replace \(a\) in a chain by \(-s\) times the sum of the other codimension-one faces of \(b\), with their boundary signs, and continue. Faces that are upper members of lower-dimensional pairs project to zero. The acyclicity proved above ensures that these substitutions terminate. The resulting boundary from the six critical four-cells to the thirty-four critical three-cells is an integral \(34\)-by-\(6\) matrix \(B\). All other nonzero-dimensional Morse boundary maps vanish for dimension reasons.

Order the critical three- and four-cells by increasing integer bitmask. Exact integer calculation gives the following finite determinant certificates, with row/column indices starting at zero:

* Rows \(6,10,12,20,24\), columns \(0,1,3,4,5\): determinant \(-1\).
* Rows \(2,8,9,12,16,20\), all six columns: determinant \(3\).
* Reduction of the entire \(B\) modulo \(3\) gives rank \(5\); modulo \(2\) gives rank \(6\).

The first determinant forces the first five Smith invariant factors to equal \(1\). Since the rank modulo \(3\) is five, all maximal minors are divisible by \(3\); the displayed maximal minor of determinant \(3\) shows that their greatest common divisor is precisely \(3\). Hence \(B\) has full rational rank six and Smith normal form
\[
\operatorname{diag}(1,1,1,1,1,3),
\]
with twenty-eight extra zero rows. Every determinant and modular rank is checked from the actual reconstructed Morse boundary in the standalone verifier.

**4. Upgrade from homology to homotopy.** The Morse CW three-skeleton is a wedge of thirty-four three-spheres, because there is only one zero-cell and there are no one- or two-cells. Since this three-skeleton is two-connected, the Hurewicz homomorphism identifies its third homotopy group with \(\mathbb Z^{34}\). Thus each four-cell attaching map is determined by its integer vector of degrees, namely a column of \(B\). Unimodular row and column transformations are realized by homotopy equivalences of the source and target wedges of three-spheres, and preserve the homotopy type of the mapping cone. In Smith form, five four-cells attach by degree one to five distinct three-spheres, giving contractible summands. One remaining four-cell attaches by degree three to one three-sphere, giving \(M(\mathbb Z/3\mathbb Z,3)\), while twenty-eight three-spheres remain unattached. This is the stated homotopy decomposition.

## Verification

Run `python3 verify.py` in a directory containing the supplied standalone file. It needs only the Python standard library. The verifier reconstructs all faces, all matching pairs, and every directed Hasse incidence; checks acyclicity by a complete topological sort; constructs the signed Morse boundary by memoized gradient-path substitutions; and tests the two exact determinants and the modular ranks. Independently of the Morse computation, it constructs the original simplicial boundary matrices and computes their ranks modulo \(2\), \(3\), and \(5\). The complete captured output is embedded as `verify_output.txt`.

The Morse boundary serialized as compact JSON has SHA-256 `5fdbe74f234f882c11c8173e659d998555c001a179fb8514d55dc9305144e0de`. This digest is an identifying convenience, not a substitute for the executable finite proof.

## Relationship to prior work

Chvátal's 1970 note supplies the graph and its coloring context. The accessible bibliographic description does not discuss the matching complex; the original paper was not accessible in full, so no assertion of whole-document noncoverage is made. Jonsson's work on torsion in matching complexes examines \(\mathcal M(K_n)\), the matching complexes of complete graphs, and general techniques for studying torsion; its conclusions do not classify the matching complex of the proper subgraph used here. The outerplanar matching-complex theorem of Bayer, Jelić Milutinović and Vega does not apply: every nonempty outerplanar graph has a vertex of degree at most two, whereas the Chvátal graph is four-regular.

The known matching complex of the eleven-vertex Grötzsch graph, another canonical triangle-free four-chromatic graph, is a wedge of twenty-four three-spheres. By contrast, the Chvátal complex has a nonzero order-three torsion summand. A published indexed result for the icosahedral graph's matching complex contains the same kind of Moore summand but concerns a distinct twelve-vertex graph, with sixty-four free three-sphere factors; it does not imply the present calculation. The independence complex of the Chvátal graph itself is also a different simplicial complex from the independence complex of its line graph, which is \(\mathcal M(G)\).

## Limitations

The theorem concerns this exact labeled graph (equivalently, any isomorphic copy). It does not classify arbitrary four-regular or four-chromatic graphs, and the calculation provides no natural functorial description of the torsion generator. The novelty comparison is based on inspected material and available indexed records; inaccessible or unindexed results could alter the originality assessment. The proof is an exact finite computation supported by a reproducible verifier, not an independently audited formal proof.

## References

1. V. Chvátal, “The smallest triangle-free 4-chromatic 4-regular graph,” *Journal of Combinatorial Theory* **9** (1970), 93–94. DOI: 10.1016/S0021-9800(70)80057-6. Earliest verified public date used: 1970-07-01 (publisher-linked bibliographic listing).
2. J. Jonsson, “More Torsion in the Homology of the Matching Complex,” *Experimental Mathematics* **19** (2010), 363–383; accessible preprint arXiv:1203.5658. The preprint explicitly treats matchings in complete graphs.
3. M. Bayer, M. Jelić Milutinović, J. Vega, “Matching Complexes of Outerplanar Graphs,” arXiv:2411.04601, Theorem 2 and its proof.
4. NetworkX documentation, `chvatal_graph`, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.chvatal_graph.html (graph identification only; not used by the verifier).
5. Indexed comparison records: “The Grötzsch graph matching complex is a wedge of twenty-four three-spheres,” published-finding corpus record `2026/10/11/SCOPE-the-gr-tzsch-graph-matching-complex-is-a-wedge-of-twenty-four-th--514850eb507b`; and “Three-torsion in the icosahedral matching complex,” record `2026/10/11/SCOPE-three-torsion-in-the-icosahedral-matching-complex-a-planar-count--28565ad1ea1a` (index summaries only, not full-text noncoverage certificates).
