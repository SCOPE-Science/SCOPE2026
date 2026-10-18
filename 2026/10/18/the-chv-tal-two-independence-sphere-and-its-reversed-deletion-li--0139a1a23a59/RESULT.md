# The Chvátal two-independence sphere and its reversed deletion–link dichotomy

## Finding

Let \(G\) be the twelve-vertex Chvátal graph specified below, and let \(K=\operatorname{Ind}_{2}(G)\) consist of all vertex subsets whose induced connected components have at most two vertices. Equivalently, a vertex subset belongs to \(K\) if and only if its induced graph has maximum degree at most one. Then

\[
K\simeq S^{3}.
\]

The automorphism group is the eight-element dihedral group \(D_4\). Its orbits on vertices are \(A=\{0,1,4,5\}\) and \(B=\{2,3,6,7,8,9,10,11\}\). Write \(D_v=K\setminus v=\operatorname{Ind}_{2}(G-v)\) for the simplicial deletion and \(L_v=\operatorname{lk}_{K}(v)\) for the simplicial link. For every \(v\in A\),
\[
D_v\simeq S^{3},\qquad L_v\text{ is simplicially collapsible},
\]
and the canonical inclusion \(D_v\hookrightarrow K\) is a homotopy equivalence. For every \(v\in B\),
\[
D_v\text{ is simplicially collapsible},\qquad L_v\simeq S^{2}.
\]
Thus \(K\) is the suspension of \(L_v\) up to homotopy for vertices in \(B\). The two orbits reverse the deletion–link homotopy profile already known for the *ordinary* independence complex of this graph.

Under the explicit generators \(r\) (order four) and \(s\) (order two) given below, the action on \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z\) is the one-dimensional orientation character
\[
\chi(r)=-1,\qquad\chi(s)=+1,\qquad
\chi(r^{a}s^{b})=(-1)^a\quad(0\le a<4,\ b\in\{0,1\}).
\]
In particular the rational fixed subspace of this homology group under the entire automorphism group is zero.

## Assumptions and scope

The graph is finite, simple, and undirected, on vertices numbered `0` through `11`. Its complete unordered edge list is

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

A face is any subset whose induced graph is a disjoint union of edges and isolated vertices; the empty subset is included by the conventional definition. All homotopy equivalences are nonequivariant unless expressly stated. ``Simplicially collapsible'' means that a complete sequence of elementary free-face removals ends in a singleton. The integral character claim concerns homology only, not an equivariant sphere homeomorphism. The primary classification is algebraic topology, MSC2020 `55P15`.

## Proof

**Full complex and homotopy.** The first standalone verifier constructs the twelve-bit masks for every one of the \(2^{12}-1\) nonempty subsets and keeps exactly those masks for which each selected vertex has at most one selected neighbor. It obtains **424** nonempty faces and the dimension-indexed face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,66,148,142,52,4).
\]

The verifier constructs a matching on *all nonempty faces* using the ordered pivot list `9,11,3,4,7,6,8,2,5,10,1,0`. At each pivot, among remaining unmatched masks in increasing numerical order, it pairs a face not containing the pivot with its admissible one-vertex extension, when both remain unmatched. The algorithm constructs all **1,428** face-poset covering incidences, reverses the directions of the **211** matched incidences relative to the others, and performs a complete directed topological sort. The sort visits all 424 faces, certifying that the matching is acyclic. There is exactly one unmatched vertex (dimension zero) and one unmatched dimension-three face, and no other critical faces. Forman's discrete-Morse theorem therefore gives a CW model with just one zero-cell and one three-cell. Its unique attaching map has the point as its target, so the CW model is \(S^3\). This proves the *integral homotopy type* rather than merely homology over a chosen field.

**Deletions and links.** Construct \(D_v\) by retaining all faces not containing \(v\) and \(L_v\) by deleting \(v\) from all faces containing it. For representatives \(v=0\) and \(v=2\), the same exhaustive algorithm (with the individual pivot orders embedded in `verify_morse.py`) produces:

| Complex | Nonempty faces | Matching pairs | Face incidences | Critical dimensions |
| --- | ---: | ---: | ---: | --- |
| \(D_0\) | 302 | 150 | 976 | \(0,3\) |
| \(L_0\) | 121 | 60 | 320 | \(0\) |
| \(D_2\) | 305 | 152 | 990 | \(0\) |
| \(L_2\) | 118 | 58 | 309 | \(0,2\) |

Each respective complete directed Hasse graph passes its topological-sort acyclicity check. The critical-cell counts prove \(D_0\simeq S^3\) and \(L_2\simeq S^2\); in both cases the higher cell attaches to the unique zero-cell. To establish *actual simplicial collapsibility* for the remaining complexes rather than inferring it merely from homology, the verifier separately identifies and deletes a free face and its unique immediate coface until a vertex remains: **60 legal pairs for \(L_0\)** and **152 for \(D_2\)**. The verifier checks every free-face condition against the current full face set before removal.

**Transfer to every vertex and natural inclusions.** A complete adjacency/nonadjacency-preserving backtracking enumeration finds precisely eight graph automorphisms. Their vertex orbits are exactly the stated sets \(A\) and \(B\). Because an automorphism maps deletions to deletions and links to links by simplicial isomorphisms, the representative classifications hold for all twelve vertices. The standard decomposition
\[
K=D_v\cup(v*L_v),\qquad D_v\cap(v*L_v)=L_v
\]
is a homotopy pushout along a simplicial cofibration. If \(v\in A\), then \(L_v\) is contractible, so coning it on makes \(D_v\hookrightarrow K\) a homotopy equivalence. If \(v\in B\), then \(D_v\) is contractible, so \(K\simeq\Sigma L_v\simeq S^3\). These assertions concern the canonical inclusions, not only abstract isomorphism classes.

**Full automorphism character.** The permutation images of `0` through `11` are

```text
r=(1,5,11,6,0,4,7,10,9,2,3,8)
s=(0,4,3,2,1,5,9,8,7,6,11,10)
```

The second verifier checks that these preserve all 24 graph edges, generate eight distinct permutations, and satisfy \(r^4=s^2=1\), \(srs=r^{-1}\). For any graph automorphism \(g\), its signed simplicial-chain Lefschetz number is the sum over nonempty setwise fixed faces \(\sigma\) of \((-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)\). Subtract one for reduced chains. Since the only nonzero reduced rational homology of \(K\) is in degree three, the reduced Lefschetz number equals the *negative* of the homology trace. Thus the trace is one minus the signed nonempty-face sum. Exhaustive enumeration gives \(\chi(r)=-1\) and \(\chi(s)=+1\); multiplicativity and the dihedral relations give \(\chi(r^as^b)=(-1)^a\) on all eight elements. The homology group has integral rank one, so these rational traces specify its *integral* group action. Character averaging gives \(\dim_{\mathbb Q}\widetilde H_3(K;\mathbb Q)^{D_4}=0\).

## Verification

The attached `verify_morse.py` uses Python 3's standard library, with the entire graph and all pivot orders specified locally. Execute `python3 verify_morse.py` to enumerate every face, prove complete Morse acyclicity for each of the five complexes, verify two explicit simplicial collapses, and enumerate all automorphisms. Its recorded deterministic output is `verify_morse.out` and ends in `MORSE_CERTIFICATE_OK`.

Independently execute `python3 verify_homology_symmetry.py`. This second standalone program builds faces by combinations from a separately encoded adjacency table, constructs all simplicial boundary matrices over \(\mathbb F_2\), computes reduced Betti numbers for all five complexes, checks the two dihedral generators and all eight character values by exact signed fixed-face enumeration, and verifies multiplicativity. Its recorded output is `verify_homology_symmetry.out` and ends in `INDEPENDENT_CHECKS_OK`. This modular homology computation corroborates but does *not* substitute for the discrete-Morse homotopy proof. The character check uses exact finite integer signs.

## Relationship to prior work

The classical Chvátal graph is distinguished as a twelve-vertex, four-regular, triangle-free, four-chromatic graph. Deshpande and Singh classify higher-independence homotopy types for cycles, complete multipartite graphs, fully whiskered graphs and perfect rooted trees; those graph families do not include this graph. Sawant's May 2026 result proves vertex decomposability of higher-independence complexes for **trees**, and identifies three-path-free with two-independence complexes; this cyclic graph is not a tree. Deshpande, Goyal and Sawant's July 2026 work treats path-free complexes of complete **multipartite** graphs, which also excludes the Chvátal graph.

A publicly available exact Chvátal graph calculation classifies its *ordinary* independence complex as \(S^2\). It establishes the **opposite** deletion/link pattern on these same two orbits: ordinary-deletion contractible and ordinary-link \(S^1\) for \(A\), ordinary-deletion \(S^2\) and ordinary-link contractible for \(B\). A second public calculation gives a relative equivariant collapse from the ordinary independence complex onto the open-neighborhood complex and computes its degree-two orientation character \(\chi(r)=-1,\ \chi(s)=-1\). These are different simplicial complexes and do not determine the present two-independence complex, its reversed deletion/link behavior, or its degree-three character. The canonical inclusion \(\operatorname{Ind}(G)\subsetneq\operatorname{Ind}_2(G)\) alone implies none of the new homotopy conclusions.

## Limitations

This is a classification for one explicitly labeled finite graph, not an infinite family. The homotopy equivalence and orbit-wise deletion/link statements are proved integrally; the finite automorphism calculation determines the induced homology representation but not a model for a strict equivariant sphere action. The independent mod-two homology check is a consistency test rather than an integral torsion certificate on its own. Indexed-record and accessible-literature comparisons reduce, but cannot eliminate, the risk of an equivalent unindexed or unpublished result. May 24, 2026 is the verified first-public date of the motivating source on higher-independence constructions, not a claimed publication date of this finding.

## References

1. Rutuja Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1, first public 2026-05-24, https://arxiv.org/abs/2605.25150.
2. Priyavrat Deshpande, Shuchita Goyal and Rutuja Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358v1, first public 2026-07-06, https://arxiv.org/abs/2607.05358.
3. Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, Journal of the Ramanujan Mathematical Society 36 (2021), 53–71, arXiv:2001.05448, https://arxiv.org/abs/2001.05448.
4. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory 9 (1970), 93–94, DOI:10.1016/S0021-9800(70)80057-6.
5. *The Chvátal graph independence complex and its vertex-deletion dichotomy*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-chv-tal-graph-independence-complex-and-its-vertex-deletion-d--676b14391238.
6. *An equivariant collapse connecting the Chvátal independence and neighborhood complexes*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-equivariant-collapse-connecting-the-chv-tal-independence-and--3077dabdf181.
7. Robin Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
