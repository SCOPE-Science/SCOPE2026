# The icosahedral dissociation complex: twenty three-spheres and full symmetry

## Finding
Let \(I\) denote the vertex-edge graph of the regular icosahedron, and let \(K\) be its **dissociation complex**: a finite subset \(S\subseteq V(I)\) is a simplex exactly when each vertex of the induced subgraph \(I[S]\) has degree at most one. Equivalently, each induced connected component has at most two vertices, so \(K=\operatorname{Ind}_2(I)\). There is an integral homotopy equivalence
\[
K\simeq\bigvee^{20}S^3.
\]
Under the full automorphism group \(G=\operatorname{Aut}(I)\cong A_5\times C_2\), its only nonzero reduced rational homology representation decomposes as
\[
\widetilde H_3(K;\mathbb Q)
\cong\mathbf1^+\oplus V_4^+\oplus (V_5^+)^{\oplus2}\oplus V_5^-.
\]
Here \(V_4\) and \(V_5\) are the rational irreducible \(A_5\)-modules of dimensions four and five, and superscripts \(+\) and \(-\) indicate how the central antipodal vertex permutation acts. Hence its even and odd eigenspaces have respective dimensions 15 and 5, and its full automorphism-invariant rational homology is one-dimensional.

## Assumptions and scope
All graph subsets are induced vertex subsets, not collections of graph edges. Use twelve graph vertices labelled \(0,\ldots,11\) and the following adjacency lists, which specify the graph independently of a software library:

```text
0:  1 5 7 8 11
1:  0 2 5 6 8
2:  1 3 6 8 9
3:  2 4 6 9 10
4:  3 5 6 10 11
5:  0 1 4 6 11
6:  1 2 3 4 5
7:  0 8 9 10 11
8:  0 1 2 7 9
9:  2 3 7 8 10
10: 3 4 7 9 11
11: 0 4 5 7 10
```

Every vertex has degree five, and its neighbors form a five-cycle. The graph has exactly twenty triangular surface faces and a 120-element automorphism group. Every face of \(K\) has at most four vertices, and all 105 facets have four vertices.

## Proof
**Face predicate.** For each subset \(S\), its connected components have cardinality at most two if and only if every vertex of \(I[S]\) has degree at most one. Indeed, each finite connected graph on at least three vertices contains a length-two path, and the middle vertex has degree at least two. Thus testing this degree condition on each of the \(2^{12}=4096\) masks enumerates *all* faces, not a sample. The resulting face counts in degrees zero through three are \((12,66,140,105)\), with the empty face additionally present. This gives ordinary Euler characteristic \(-19\), in agreement with the homotopy type below.

**A finite perfect discrete-Morse matching.** Starting with the complete face set, successively process the twelve vertex labels in the exact order

```text
2 11 3 10 5 0 7 9 1 4 6 8
```

At pivot \(v\), simultaneously pair every currently unpaired **nonempty** face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) when both remain unpaired. Leave the empty face alone. Because any given pair is determined by its lower face, the deterministic implementation iterates lower masks in increasing numeric order; disjointness is checked at every step. This constructs exactly 151 distinct pairs. Among nonempty faces, the unmatched cells are precisely one vertex and twenty three-simplices, with none in other dimensions.

To certify acyclicity independently of the pivot theorem, construct the entire directed Hasse graph of the face poset: orient a codimension-one incidence from higher face to lower face unless it is a selected matching pair, in which case reverse it. The verifier explicitly processes all 984 such incidences, and a complete topological sort visits all 324 faces (including the empty face). Thus the directed graph is acyclic. By discrete Morse theory the geometric realization of \(K\) has the homotopy type of a CW complex with one zero-cell, twenty three-cells and no other cells. Since every three-cell then attaches to a point, that CW complex is the displayed wedge of twenty three-spheres. This argument is over the integers and rules out hidden torsion and nontrivial attaching maps.

**Complete character.** The two graph automorphisms

```text
r2 = (1,0,11,10,9,8,7,6,5,4,3,2)
r3 = (5,0,7,9,2,1,8,4,11,10,3,6)
```

have respective orders two and three, and their product has order five. They generate a sixty-element subgroup preserving the oriented icosahedral triangulation, which is the rotational \(A_5\). The antipodal involution

```text
rho = (3,10,11,0,8,9,7,6,4,5,1,2)
```

is central and generates the second factor; the three permutations together generate 120 graph automorphisms. Conversely, the stabilizer of a vertex injects into the dihedral automorphism group of its five-neighbor cycle, giving the bound \(12\cdot10=120\). Hence these are all graph automorphisms.

For an automorphism \(g\), let \(t_j(g)\) be the signed trace of its action on oriented simplicial \(j\)-chains, obtained by summing the induced vertex-permutation sign over setwise fixed \(j\)-faces. The Lefschetz identity, together with the proved homotopy equivalence, gives
\[
\operatorname{tr}(g\mid\widetilde H_3(K;\mathbb Q))
=1-t_0(g)+t_1(g)-t_2(g)+t_3(g).
\]
The complete check over the group gives rotational traces \((20,4,-1,0,0)\) on classes of orders \((1,2,3,5_A,5_B)\), and antipodally twisted traces \((10,2,1,0,0)\). In each tuple, the order-two and order-three classes contain fifteen and twenty elements, and each order-five class contains twelve. The antipodal even and odd character vectors are therefore respectively \((15,3,0,0,0)\) and \((5,1,-1,0,0)\). Using the standard \(A_5\) rational characters
\[
\chi_{\mathbf1}=(1,1,1,1,1),\quad
\chi_{V_4}=(4,0,1,-1,-1),\quad
\chi_{V_5}=(5,1,-1,0,0),
\]
these are \(\chi_{\mathbf1}+\chi_{V_4}+2\chi_{V_5}\) and \(\chi_{V_5}\). Character equality proves the stated rational representation decomposition. Its full-group invariant subspace is the unique \(\mathbf1^+\) summand.

## Verification
Run the self-contained Python 3 program `scripts/verify.py` from the package root. It uses no third-party dependencies and independently checks the degree and connected-component face predicates for all 4,096 vertex subsets, all face counts and facets, every matching pair, every face incidence and full acyclicity; it also computes mod-two simplicial boundary ranks \((11,55,85)\). It builds the complete automorphism group from explicit permutations, checks orientation, and calculates all 120 signed character values. The included `verification_output.txt` is the captured program output, ending with `VERIFY_OK`.

## Relationship to prior work
Orlovich, Dolgui, Finke, Gordon and Werner (2011) study dissociation sets as induced degree-at-most-one vertex subsets, but their enumerative and complexity problem is not a homotopy or full-symmetry classification. Deshpande and Singh (arXiv:2001.05448, 2020; journal 2021) introduce homotopy calculations for higher independence complexes of complete multipartite graphs, whiskered graphs, paths, cycles and perfect trees. The icosahedral graph does not belong to these families. Abdelmalek and collaborators (arXiv:2106.10863, 2021) treat chordal families and trees; the icosahedral graph is not chordal because the neighbors of any vertex induce a five-cycle.

Distinct complexes already considered on this same graph include its ordinary independence complex, its open-neighborhood complex, the ordinary matching complex and various graph-metric nerves. None of those claims implies this vertex dissociation complex's homotopy type or its third-homology character: the underlying face conditions are different. The closest previously classified second independence complexes of other graph families are not identified with the present complex. Searches under the aliases "dissociation complex", "two-independence complex", "induced maximum degree one" and "induced components of size at most two" located no equivalent published formula. These searches do not constitute a proof of global novelty.

## Limitations
The homotopy equivalence is nonequivariant; no equivariant homotopy wedge splitting is asserted. The representation is classified rationally, not as a full integral group lattice. The result treats only the icosahedral graph and does not claim a general formula for higher independence complexes of arbitrary triangulated spheres. Possible unindexed equivalent results remain an originality risk, and independent scientific audit has not been performed.

## References
1. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366. DOI: 10.1016/j.dam.2011.04.023.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448 (first posted 2020-01-15); Journal of the Ramanujan Mathematical Society 36 (2021), 53–71.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863 (2021).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. DOI: 10.1006/aima.1997.1650.
5. D. Kozlov, *Combinatorial Algebraic Topology*, Springer (2008), DOI: 10.1007/978-3-540-71962-5.
