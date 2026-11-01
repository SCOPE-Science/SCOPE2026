# The Heawood two-particle configuration space has an irreducible six-dimensional homology summand

## Finding
Let \(H\) be the 14-vertex Heawood graph, presented as the point-line incidence graph of the Fano plane, let \(X=\operatorname{UConf}_2(|H|)\) be the collision-free space of two **unordered** points on its geometric realization, and let \(G=\operatorname{Aut}(H)\), of order \(336\). As rational \(G\)-representations,
\[
H_1(X;\mathbb Q)\cong H_1(H;\mathbb Q)=V_8,\qquad
H_2(X;\mathbb Q)\cong V_8\oplus W_6.
\]
Here \(V_8\) and \(W_6\) are nonisomorphic irreducible rational representations of dimensions \(8\) and \(6\), respectively. All other positive-degree rational homology vanishes. The isomorphisms of representations are not asserted to be canonical splittings of spaces.

Moreover, **all** of \(H_2(X;\mathbb Q)\) is spanned by the torus fundamental classes from the \(42\) unordered pairs of vertex-disjoint six-cycles in \(H\). Neither positive-degree rational homology group contains a nonzero class fixed by all \(336\) automorphisms.

The complete characters \(\chi_1,\chi_2\) are determined by the following grouped classes. The two conjugacy classes of order seven (24 elements each) are combined because their character values agree.

| Automorphism kind | Order | Count | \(\chi_1\) | \(\chi_2\) |
|---|---:|---:|---:|---:|
| Point-line preserving | 1 | 1 | 8 | 14 |
| Point-line preserving | 2 | 21 | 0 | -2 |
| Point-line preserving | 3 | 56 | -1 | -1 |
| Point-line preserving | 4 | 42 | 0 | 2 |
| Point-line preserving | 7 | 48 | 1 | 0 |
| Point-line exchanging | 2 | 28 | -2 | -2 |
| Point-line exchanging | 6 | 56 | 1 | 1 |
| Point-line exchanging | 8 | 84 | 0 | 0 |

## Assumptions and scope
The Fano plane is modeled on the seven nonzero vectors of \(\mathbb F_2^3\). Its seven lines are the sets \(\{a,b,a\oplus b\}\), where \(a\ne b\) and \(\oplus\) denotes bitwise vector addition. The graph has seven point vertices and seven line vertices, with one edge for each of the \(21\) incidences. Its full graph automorphism group consists of the \(168\) invertible linear point-line preserving maps and the \(168\) composites with a point-line polarity. These are genuine cellular symmetries of the two-particle space.

The configuration space is the ordinary **unordered, collision-free** space on the topological graph, not an ordered space, a matching complex, or a configuration space allowing particles to meet at vertices. Coefficients are rational in the representation statements. The underlying graph is not planar.

## Proof
**1. A finite cubical model.** For two particles, the graph satisfies the Abrams subdivision criterion: paths between vertices of degree other than two have at least one edge, and simple cycles have at least three edges. Therefore \(X\) deformation retracts onto the unordered cubical complex of cells with disjoint closures. A zero-cell is an unordered pair of distinct graph vertices; a one-cell is a vertex and a nonincident edge; a two-cell is an unordered pair of vertex-disjoint edges. Thus the cubical chain ranks in degrees \(0,1,2\) are \(91,252,168\).

Orient each graph edge from the smaller labeled vertex to the larger. If \(e=[a,b]\), the one-cell \((v,e)\) has boundary \(\{v,b\}-\{v,a\}\). If \(e=[a,b]\), \(f=[c,d]\) are disjoint with \(e<f\) in the prescribed edge order, the two-cell \((e,f)\) has boundary
\[
(b,f)-(a,f)-(d,e)+(c,e).
\]
The executable finite verifier reconstructs all cells and boundaries and checks \(\partial_1\partial_2=0\).

**2. Exact ranks by complementary finite certificates.** The verifier's elementary characteristic-three eliminations give \(\operatorname{rank}_{\mathbb F_3}\partial_1=90\) and \(\operatorname{rank}_{\mathbb F_3}\partial_2=154\). These imply the same lower bounds over \(\mathbb Q\). Since there are \(91\) zero-cells, \(\operatorname{rank}_{\mathbb Q}\partial_1\le90\). The graph has exactly \(28\) simple six-cycles. Exactly \(42\) unordered pairs of them are vertex-disjoint. Taking products of the oriented cycles gives \(42\) explicit, closed two-chains, each supported on \(36\) square cells. The verifier checks that their span has rank \(14\) over \(\mathbb F_3\), hence at least \(14\) over \(\mathbb Q\). Therefore \(\operatorname{rank}_{\mathbb Q}\partial_2\le168-14=154\). Both ranks are exact, and the rational Betti numbers are \((1,8,14)\). The \(42\) product tori necessarily span the entire top rational homology.

**3. Equivariance in degree one.** Every six-cycle omits eight graph vertices; holding a second particle at one of them while the first traverses the cycle defines a loop in \(X\). The \(28\) oriented six-cycles span the rank-eight rational graph cycle space, as checked by an independent signed-incidence elimination in the verifier. The natural symmetric-product map induces a \(G\)-equivariant surjection \(H_1(X;\mathbb Q)\to H_1(H;\mathbb Q)\). Since both dimensions are eight it is an isomorphism. The trace of \(g\) on this representation is its signed trace on the graph-edge chain group minus its trace on the graph-vertex chain group plus one.

**4. Equivariant Lefschetz trace and irreducibility.** The finite verifier constructs all \(168\) invertible \(3\)-by-\(3\) binary linear maps and composes them with the standard Fano polarity to enumerate exactly \(336\) graph automorphisms. It checks every element's action on oriented cubical cells. Since only degrees zero through two can have homology,
\[
\chi_2(g)=\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_2)-1+\chi_1(g).
\]
The trace table follows by exact integer summation over the fixed oriented cells. Taking class-function inner products with the group order \(336\), the verified sums give
\[
\langle\chi_1,\chi_1\rangle=1,\quad
\langle\chi_2,\chi_2\rangle=2,\quad
\langle\chi_1,\chi_2\rangle=1.
\]
Consequently \(\chi_1\) is irreducible and occurs once in \(\chi_2\). The difference \(\chi_6=\chi_2-\chi_1\) has degree six and inner-product norm one, so it is the character of a second irreducible constituent. Maschke semisimplicity over \(\mathbb Q\) gives the stated direct-sum decomposition. Summing either positive-degree character over the whole group gives zero, establishing the invariant-space statements.

## Verification
Run `python3 verify.py` from the directory containing the verifier; Python's standard library is sufficient. The checker rebuilds the Fano plane from binary-vector incidence; all \(91+252+168\) cubical cells; both signed boundary operators; \(28\) hexagons and \(42\) disjoint-hexagon tori; modular elimination ranks; all \(336\) automorphisms; the eight-row character table; and all character inner products. It asserts every identity, checks the boundary of each torus, and terminates with `VERIFY_OK`. An actual execution is recorded in `verification_output.txt`. These are finite exact certificates for this fixed graph, not extrapolations.

## Relationship to prior work
Abrams constructed discrete models for graph configuration spaces. Ko and Park obtained general first-homology formulas for graph braid groups, covering the previously known nonequivariant first-homology information here. Farber and Hanbury studied ordered two-point spaces and their intersection and linking forms. An and Knudsen developed toric-class generators for second homology of **planar** graph braid groups and explicitly discussed the nonplanar gap. These results motivate the question but do not specify the full \(336\)-element representation on this Heawood unordered space or prove that its top rational homology is spanned by disjoint hexagon tori.

The previously indexed mod-two Betti calculation for the **ordered** two-point Heawood space concerns a different space and coefficient field. Results for the Heawood **matching complex** concern a different simplicial object. Neither is counted as this result.

## Limitations
This theorem gives rational representations and the rational span of toric cycles. It does not identify an integral direct-sum splitting, nor claim the toric classes are an integral basis; finite characteristic-three ranks alone cannot certify integral saturation. It does not describe the graph braid fundamental group or generalize to other projective planes. A genuinely equivalent result could appear in unindexed or differently formulated literature. The supplied review is not independent mathematical certification.

## References
1. Aaron D. Abrams, *Configuration Spaces and Braid Groups of Graphs*, PhD thesis, University of California, Berkeley (2000). https://math.berkeley.edu/publications/configuration-spaces-and-braid-groups-graphs
2. Ki Hyoung Ko and Hyo Won Park, *Characteristics of Graph Braid Groups*, arXiv:1101.2648 (first posted 2011-01-13). https://arxiv.org/abs/1101.2648
3. Michael Farber and Elizabeth Hanbury, *Topology of Configuration Space of Two Particles on a Graph, II*, arXiv:1005.2300 (first posted 2010-05-13). https://arxiv.org/abs/1005.2300
4. Byung Hee An and Ben Knudsen, *On the Second Homology of Planar Graph Braid Groups*, arXiv:2008.10371 (first posted 2020-08-24). https://arxiv.org/abs/2008.10371
