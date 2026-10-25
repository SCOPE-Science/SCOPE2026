# Shortest hexagon-pair torus basis and full symmetry character of the Heawood configuration space

## Finding
Let \(H\) be the Heawood graph, realized as the bipartite incidence graph of points and lines of the Fano plane, and put \(X=\operatorname{UConf}_2(|H|)\). The complete integral homology is
\[
H_0(X;\mathbb Z)\cong\mathbb Z,\qquad
H_1(X;\mathbb Z)\cong\mathbb Z^8\oplus\mathbb Z/2,\qquad
H_2(X;\mathbb Z)\cong\mathbb Z^{14}.
\]
There is no homology in degrees above two.

The graph has 28 simple hexagons and 42 unordered vertex-disjoint pairs of hexagons. Each pair gives an embedded product torus in \(X\). Fourteen explicitly indexed such classes form a **basis over \(\mathbb Z\)** of the entire second homology; a specified integral minor has determinant \(-1\). The 42 underlying hexagon pairs form a single orbit under the 336 graph automorphisms, as independently established in the graph-theoretic literature.

The full rational character of \(\operatorname{Aut}(H)\cong\operatorname{PGL}_2(7)\) acting on \(H_2(X;\mathbb Q)\) is determined by whether an automorphism preserves the two color classes and by its order:

| Bipartition action | Element order | Number of elements | Trace on \(H_2(X;\mathbb Q)\) |
| --- | ---: | ---: | ---: |
| Preserves | 1 | 1 | 14 |
| Preserves | 2 | 21 | -2 |
| Preserves | 3 | 56 | -1 |
| Preserves | 4 | 42 | 2 |
| Preserves | 7 | 48 | 0 |
| Exchanges | 2 | 28 | -2 |
| Exchanges | 6 | 56 | 1 |
| Exchanges | 8 | 84 | 0 |

The traces sum to zero over all group elements, so \(H_2(X;\mathbb Q)^{\operatorname{Aut}(H)}=0\). Elements of order seven occur in two conjugacy classes, both of trace zero; hence the table determines the character on all 336 elements.

## Assumptions and scope
The graph is a finite one-dimensional CW complex with vertices \(\{0,1,\ldots,13\}\), all rim edges \(\{i,i+1\}\) modulo 14, and the additional chords \(\{i,i+5\}\) for even \(i\), modulo 14. This is the standard LCF presentation \([5,-5]^7\), independently checked against the Fano-plane incidence graph. It has 14 vertices, 21 edges, girth six, and no multiple edges.

We use the **ordinary collision-free unordered configuration space**, not a vertex-sink variant. By the equivariant deleted-product deformation retract described by Barnett–Farber, the space is homotopy equivalent to the finite cubical complex of unordered pairs of graph cells with disjoint closures. The action of graph automorphisms preserves this model.

## Proof
Order vertices and orient every edge from its smaller to its larger endpoint. Let \(E=\{e_0,\ldots,e_{20}\}\) be the lexicographically ordered edge list. The cubical model has 91 zero-cells \(\{u,v\}\), 252 one-cells \((v,e_i)\) with \(v\notin e_i\), and 168 two-cells \((e_i,e_j)\) with \(i<j\) and disjoint endpoints. In these orientations,
\[
\partial_2(e_i,e_j)=(b,e_j)-(a,e_j)-(d,e_i)+(c,e_i),
\]
where \(e_i=[a,b]\), \(e_j=[c,d]\), and the vertices in each edge are increasing. The formula for \(\partial_1(v,e_i)\) is \(\{v,b\}-\{v,a\}\). These expressions give \(\partial_1\partial_2=0\).

Enumerate simple six-cycles as cyclic vertex words, identifying rotations and reversals. For oriented vertex-disjoint cycles \(C,D\), the image of their product fundamental class is represented by the two-chain
\[
T(C,D)=\sum_{\substack{e_i\in C,\ e_j\in D}} s_C(i)s_D(j)\,\operatorname{sgn}(j-i)\,(e_{\min(i,j)},e_{\max(i,j)}),
\]
where each coefficient \(s_C(i)\) or \(s_D(j)\) is \(+1\) or \(-1\) according to the traversal direction relative to the fixed graph-edge orientation. The formula and the cubical boundary show directly that every such chain is a two-cycle.

For reproducibility, enumerate the 42 unordered disjoint hexagon pairs lexicographically (the two hexagon words are themselves canonical and lexicographically ordered); let \(T\) be the integer \(168\times42\) matrix of their signed two-chains. Use these zero-indexed two-cell row positions:

`[0,2,4,7,10,16,18,20,23,48,50,53,76,82]`

and these zero-indexed torus column positions:

`[0,1,3,4,6,7,9,10,12,13,15,16,18,24]`.

The resulting \(14\times14\) minor has **determinant \(-1\)**. In particular, the chosen fourteen cycles are linearly independent and generate a primitive rank-fourteen subgroup of the full two-chain lattice. A direct elimination modulo \(101\) shows \(\operatorname{rank}\partial_2\ge154\). Because fourteen independent two-cycles exist, \(\operatorname{rank}\partial_2\le168-14=154\). Thus \(\operatorname{rank}\partial_2=154\). The kernel \(\ker\partial_2\) is saturated in its free two-chain lattice; the primitive rank-fourteen torus subgroup equals that kernel. This proves the integral torus basis theorem without inferring integrality from a rational rank.

The one-skeleton of the cubical configuration space is connected, and \(\partial_1\) has rank 90. Euler characteristic is \(91-252+168=7\), giving first Betti number eight. The Smith normal form of \(\partial_2\) has 153 nonzero unit entries and exactly one nonunit entry, equal to two. Since \(\operatorname{im}\partial_1\) is free, the torsion of \(H_1\) equals the torsion of \(\operatorname{coker}\partial_2\). Hence \(H_1\cong\mathbb Z^8\oplus\mathbb Z/2\).

The 28 oriented hexagons have rank eight in the ordinary graph edge-cycle space, equal to the graph cycle rank. Moving one particle around such a hexagon while holding the other particle at any of its eight unused graph vertices shows that the natural sum-of-motions map from \(H_1(X;\mathbb Q)\) onto \(H_1(|H|;\mathbb Q)\) is surjective. Since both have dimension eight, it is an equivariant rational isomorphism; this justifies the independent Lefschetz character cross-check below.

For each of the 336 graph automorphisms, permute graph vertices and apply the signed orientations on all 168 two-cells. Translate all fourteen basis two-cycles; the inverse of the displayed unimodular minor gives their unique **integral** coordinates in the basis. Direct equality of the full transformed two-chains is checked, not merely equality on the fourteen selected coordinates. The traces of these resulting integer matrices give the character table above. As a separate check, the same traces follow from fixed-cell Lefschetz numbers and the natural eight-dimensional graph cycle character on first rational homology.

## Verification
Execute `python verify_heawood.py` in the same directory as the embedded `requirements.txt`. The program constructs the graph in two independent forms, enumerates its cells and simple cycles, verifies \(\partial_1\partial_2=0\), reconstructs all 42 torus cycles, checks the determinant \(-1\) and the rank bound modulo \(101\), computes the exact Smith normal form, and checks the action of all 336 automorphisms. It independently compares homology traces with fixed-cell Lefschetz expressions. The file contains all indexing conventions and the explicit basis certificate.

## Relationship to prior work
Barnett–Farber developed the ordered deleted-product model and intersection methods; their principal explicit generators concern planar graphs. Farber–Hanbury provided broader structural formulas and maturity criteria, not the particular hexagon-orbit integral basis or the 336-element homology character asserted here. Lawrence–Wilson already enumerated the 42 disjoint hexagon pairs and proved transitivity under automorphisms. Those **combinatorial graph facts are prior work**, not the new homological assertion. An–Knudsen characterized planar second-homology generators and identified failures of a naively unrestricted nonplanar analogue; the Heawood graph is nonplanar. An indexed calculation of the **ordered** two-particle Heawood space with mod-two coefficients concerns a different configuration space and coefficient system, and does not entail this unordered integral basis or character.

## Limitations
This is a finite, computer-assisted exact calculation for the Heawood graph. It does not provide a classification for arbitrary cubic graphs or an integral decomposition into irreducible group-ring modules. The character statement is rational, whereas the torus basis and homology groups are integral. Related but unindexed calculations could affect publication priority; the mathematical and computational certificates do not establish uniqueness in the literature.

## References
1. K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, arXiv:0903.2180 (first posted 2009-03-12), Sections 1 and 6–7; DOI 10.2140/agt.2009.9.593.
2. M. Farber and E. Hanbury, *Topology of configuration space of two particles on a graph, II*, arXiv:1005.2300 (first posted 2010-05-13); DOI 10.2140/agt.2010.10.2203.
3. E. D. Lawrence and R. Wilson, *The Structure of the Heawood Graph*, arXiv:1907.11978 (first posted 2019-07-27), Proposition 2 and Theorem 3.
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first posted 2020-08-24), Theorem 1.1 and Example 6.8.
