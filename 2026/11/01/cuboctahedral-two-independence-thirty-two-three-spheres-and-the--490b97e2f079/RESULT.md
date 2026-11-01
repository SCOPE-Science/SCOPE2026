# Cuboctahedral two-independence: thirty-two three-spheres and the octahedral homology character

## Finding

Let \(Q_3\) be the graph with vertex set \(\{0,1\}^3\), with two vertices adjacent when they differ in one coordinate, and let \(C=L(Q_3)\) be its line graph. Thus \(C\) is the twelve-vertex cuboctahedral graph. Write \(X=\operatorname{Ind}_2(C)\) for the simplicial complex of subsets \(U\subseteq V(C)\) such that every connected component of \(C[U]\) has at most two vertices.

There is an **integral homotopy equivalence**
\[
X\simeq\bigvee^{32}S^3.
\]
The full cubical automorphism group \(B_3=(\mathbb Z/2)^3\rtimes S_3\cong\operatorname{Aut}(C)\), of order \(48\), acts on the unique nonzero reduced rational homology \(\widetilde H_3(X;\mathbb Q)\). Its full character is the one specified below on all ten signed-cycle conjugacy classes. In particular, this representation has a two-dimensional fixed subspace under \(B_3\). The central antipodal involution has trace \(10\), with \(+1\) and \(-1\) eigenspaces of dimensions \(21\) and \(11\), respectively.

For \(g_{\sigma,b}(x)=b\oplus\sigma(x)\), where \(\sigma\in S_3\) permutes the bit coordinates and \(b\in\{0,1\}^3\), denote each cycle of \(\sigma\) by its length with a \(+\) or \(-\) sign according as the sum modulo two of the entries of \(b\) on that cycle is zero or one. For example, \(1_-2_+\) denotes one negative fixed coordinate and one positive two-cycle. Then:

| Signed cycle type | Class size | \(\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))\) |
|---|---:|---:|
| \(1_+1_+1_+\) | 1 | 32 |
| \(1_+1_+1_-\) | 3 | 2 |
| \(1_+1_-1_-\) | 3 | 8 |
| \(1_-1_-1_-\) | 1 | 10 |
| \(1_+2_+\) | 6 | 2 |
| \(1_+2_-\) | 6 | 0 |
| \(1_-2_+\) | 6 | 4 |
| \(1_-2_-\) | 6 | -2 |
| \(3_+\) | 8 | -1 |
| \(3_-\) | 8 | 1 |

Equivalently, regarding the twelve cube edges as the vertices of \(C\), the faces of \(X\) are precisely the cube-edge selections whose *edge-adjacency graph* has components consisting of either a singleton or a pair. This is not the ordinary matching complex of either the cube or the cuboctahedral graph.

## Assumptions and scope

All graphs are finite and simple, and the cube edges are ordered lexicographically as

```text
(0,1) (0,2) (0,4) (1,3) (1,5) (2,3)
(2,6) (3,7) (4,5) (4,6) (5,7) (6,7)
```

The integers from zero through seven are three-bit vectors; XOR with a coordinate bit determines adjacency. The vertices of the line graph are the twelve listed edges, indexed from zero through eleven. An edge between two vertices of the line graph means the original cube edges share an endpoint. The face condition is *induced maximum degree at most one*, equivalent to connected components having at most two vertices. There is no assertion for arbitrary line graphs, higher-dimensional cubes, or the higher-independence parameter other than two.

## Proof

**1. Explicit finite complex.** For each mask \(m\in\{0,\ldots,2^{12}-1\}\), let \(U_m\) consist of the cube edges whose indices are set in \(m\). Define the adjacency masks \(A_i\) of the cuboctahedron from the cube-edge incidence relation. Then the exact membership predicate is
\[
U_m\in X\quad\Longleftrightarrow\quad
\operatorname{popcount}(A_i\mathbin{\&}m)\le1
\text{ for every }i\in U_m.
\]
Indeed, every connected component of a finite simple graph has size at most two if and only if every vertex has degree at most one. Testing all \(4096\) masks yields \(456\) faces including the empty face, with augmented face vector
\[
(f_{-1},f_0,f_1,f_2,f_3,f_4)=(1,12,66,164,177,36).
\]
The complex is not pure: it has \(45\) tetrahedral facets and \(36\) four-dimensional facets.

**2. Explicit acyclic face matching.** On the *augmented* face poset, use the pivot order
\[
(8,4,9,0,10,7,11,3,5,6,2,1).
\]
At each pivot \(v\), traverse all faces in increasing integer-mask order. Whenever \(m\) and \(m\cup\{v\}\) both remain unmatched and \(v\notin m\), pair the two and delete them from the pool of unmatched faces. This deterministic prescription gives exactly \(212\) disjoint cover pairs and exactly \(32\) unmatched faces; every unmatched face contains four vertices and hence has dimension three. In particular, the empty face is paired with a vertex.

Acyclicity is certified on the **complete** augmented Hasse diagram, not inferred from a sample. For each of its \(1524\) cover relations, orient from the larger face to the smaller face except when the relation is paired, when it is reversed. The supplied standalone checker constructs all these arrows and performs a topological sort of all \(456\) nodes. Every node is removed, proving that this directed graph has no cycle. The complete construction and finite verification are mathematical proof data for this fixed twelve-vertex complex: no unstated infinite-search claim is used.

By the reduced form of Forman's discrete-Morse theorem, the augmented acyclic matching with only \(32\) critical three-faces gives a CW homotopy model with one basepoint and \(32\) three-cells attached to it. Their attaching maps are necessarily constant. Thus \(X\simeq\bigvee^{32}S^3\) integrally, rather than merely having the displayed rational or mod-two Betti numbers.

**3. All cubical symmetries.** Every translation by a three-bit vector, followed by a coordinate permutation, induces a distinct automorphism of \(C\), giving \(48\) automorphisms. Conversely, every triangle of \(C\) comprises exactly the three cube edges incident to one original cube vertex. There are eight such triangles; two share a cuboctahedral vertex exactly when their original cube vertices are adjacent. Therefore, any automorphism of \(C\) induces an automorphism of the reconstructed cube, proving \(\operatorname{Aut}(C)\cong B_3\).

**4. Entire rational character.** Order the vertices of each simplex by its cube-edge index. For an automorphism \(g\), the simplicial chain trace in degree \(j\) is the sum of the signs of the induced permutations of invariant \(j\)-simplices. Since reduced homology is concentrated in degree three, the reduced Lefschetz formula gives
\[
\chi(g):=\operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))
=\sum_{\substack{U\in X\\gU=U}}
(-1)^{|U|}\operatorname{sgn}(g\mid U),
\]
where the empty face contributes \(+1\). The checker enumerates the full \(B_3\) action, evaluates this sum for every one of its \(48\) elements, and verifies that the answers are constant with the tabulated values on precisely the ten signed-cycle conjugacy classes. In particular, the sum of all character values is \(96\), so averaging over the group gives two invariant dimensions. The central antipodal map is \(g_{\mathrm{id},(1,1,1)}\); its trace is \(10\), so its two eigenspace dimensions solve \(a+b=32\) and \(a-b=10\), giving \((a,b)=(21,11)\).

## Verification

The standalone package program is `verification/check_cuboctahedral_ind2.py`; run it from the package root with:

```text
python3 verification/check_cuboctahedral_ind2.py
```

It uses only the Python standard library, reconstructs the cube and line graph independently from the listed bit description, tests all \(4096\) subsets, verifies the complete matching and acyclicity, and evaluates all \(48\) symmetry operations and their character traces. It also independently computes the mod-two boundary ranks \(11,55,109,36\) in chain degrees one through four, giving reduced mod-two Betti numbers \((0,0,0,32,0)\) in degrees zero through four. These rank checks corroborate but are not substitutes for the integral discrete-Morse proof.

The saved expected output is `verification/check_output.txt`. The exact success marker is `CUBOCTAHEDRAL_IND2_EXACT_MORSE_CHARACTER_OK`.

## Relationship to prior work

The definition of higher-independence complexes and homotopy classifications of complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees appear in Deshpande and Singh, *Higher Independence Complexes of graphs and their homotopy types* (arXiv:2001.05448, first submitted January 15, 2020). The cuboctahedron is none of those graph families.

Deshpande, Shukla and Singh, *Distance r-domination number and r-independence complexes of graphs* (arXiv:2001.06775), gives homological connectivity bounds and a sphere-wedge result for **chordal** graphs, not this numerical homotopy type or symmetry character. The cuboctahedral graph is not chordal: its four vertices corresponding to the four cube edges around one square face induce a chordless four-cycle. Abdelmalek et al., *Chordal graphs, higher independence and vertex decomposable complexes* (arXiv:2106.10863), likewise concerns chordal graphs, trees and caterpillars.

Related exact classifications indexed for the same underlying cuboctahedron concern the **ordinary matching complex**, the **ordinary three-cut complex**, and intrinsic metric Čech complexes. Their face conditions, chain complexes, and homological degrees differ from \(\operatorname{Ind}_2(C)\). In particular, connected induced triples are *forbidden* in the present complex, whereas the ordinary three-cut construction uses complements of **disconnected** triples as facets. Those prior classifications do not state the present full homotopy type and \(B_3\) character.

## Limitations

This is an exhaustive, exact finite proof for the cuboctahedral graph, not an infinite-family theorem. A finite-field rank computation alone would not establish the integral homotopy type, which is why a complete acyclic matching is supplied. The symmetry character is rational and does **not** claim a decomposition into integral irreducible lattices. The included manuscript comparisons establish only the absence of a covering statement in the identified and materially inspected sources, not a globally certified uniqueness or novelty result; equivalent unindexed literature may exist.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first version January 15, 2020, https://arxiv.org/abs/2001.05448.
2. P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, first version January 19, 2020, https://arxiv.org/abs/2001.06775.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first version June 21, 2021, https://arxiv.org/abs/2106.10863.
