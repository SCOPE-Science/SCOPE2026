# The Chvátal two-independence complex is a three-sphere with a reversed reflection character

## Finding

Let \(G\) be the twelve-vertex Chvátal graph specified below, and let \(K=\operatorname{Ind}_2(G)\) be the simplicial complex of vertex sets whose induced connected components have order at most two. The complex has exactly 424 nonempty faces with \(f\)-vector \((12,66,148,142,52,4)\), so it is nonpure and has simplices of dimension five. Nevertheless,
\[
K\simeq S^3,\qquad \widetilde H_3(K;\mathbb Z)\cong\mathbb Z,
\]
with every other reduced integral homology group zero.

The full graph automorphism group is \(D_4\), with order-four and order-two generators \(r,s\) specified below. Its complete action on the top integral homology is the one-dimensional character
\[
\chi_3(r^a s^b)=(-1)^a\quad (0\le a<4,\ b\in\{0,1\}).
\]
Thus a reflection \(s\) that **reverses** the orientation class of the *ordinary* independence sphere \(\operatorname{Ind}_1(G)\simeq S^2\) **preserves** the new higher-independence three-sphere class. For the same graph generators, the previously determined ordinary character is \(\chi_2(r^a s^b)=(-1)^{a+b}\). The character difference is part of the finding, but it is not an assertion that the two homology groups lie in the same degree or admit a natural comparison map.

## Assumptions and scope

Vertices are the integers `0` to `11`. The graph is undirected with exactly these 24 edges:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

For any nonempty vertex set \(\sigma\), the condition \(\sigma\in K\) is equivalent to every vertex of the induced graph \(G[\sigma]\) having degree at most one. The graph automorphisms are specified by images of vertices `0` to `11`:

```text
r=(1,5,11,6,0,4,7,10,9,2,3,8)
s=(0,4,3,2,1,5,9,8,7,6,11,10)
```

The integers \(a,b\) range precisely over \(0\le a<4\) and \(b\in\{0,1\}\). Homology coefficients are integral unless explicitly stated otherwise. The conclusion is for this particular graph and its indicated vertex action, not for all triangle-free four-chromatic graphs.

## Proof

**A. Enumerating the correct simplices.** Represent each nonempty vertex subset by its 12-bit membership mask. For each chosen vertex compute the number of its four Chvátal neighbors also chosen, rejecting the mask if that number exceeds one. This criterion is equivalent to the required bound on induced component size. Exactly 424 masks survive, with the displayed face vector. The graph is independently verified as four-regular and triangle-free.

**B. An exact acyclic matching.** Begin with all 424 surviving nonempty masks unmatched. Process pivots in the fixed order

```text
4,10,11,9,8,6,5,0,2,1,7,3
```

At a pivot \(i\), visit currently unmatched masks in increasing numerical order and match any mask \(m\) lacking \(i\) with \(m\cup\{i\}\) when the latter is also currently unmatched. Remove both masks from the unmatched set immediately. This deterministic construction produces 211 disjoint face/coface pairs. Precisely the singleton mask `16` and the four-vertex mask `232` remain critical, in dimensions zero and three respectively.

For every codimension-one incidence among nonempty faces, orient it downwards unless it is one of those pairs, in which case orient it upwards. Exhaustive topological sorting of the resulting 424-vertex, 1428-arrow digraph visits **all** 424 vertices; hence the discrete gradient is acyclic. Forman's finite discrete-Morse theorem gives a CW complex homotopy equivalent to \(K\) with one zero-cell, one three-cell, and no other cells. The three-cell attaches to a point, so the CW complex is \(S^3\). This is an integral homotopy equivalence, not an inference from field ranks.

**C. Exact automorphism group.** Adjacency- and nonadjacency-preserving permutation backtracking, with each candidate image checked against all previously mapped vertices, exhaustively finds exactly eight automorphisms. The displayed permutations \(r,s\) preserve all edges and satisfy \(r^4=s^2=1\), \(srs=r^{-1}\). They generate eight distinct automorphisms, so the full group is \(D_4\).

**D. Full orientation character.** For a simplicial automorphism \(g\), the reduced Lefschetz number is computed from every setwise-fixed nonempty simplex \(\sigma\) by
\[
\widetilde L(g)=-1+\sum_{\substack{\sigma\in K,\ \sigma\ne\emptyset\\g\sigma=\sigma}}(-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma).
\]
The sign is the orientation sign of the permutation of the ordered vertices of \(\sigma\). The matching shows that the only reduced homology is the one-dimensional group in degree three. The Hopf trace formula therefore implies \(\chi_3(g)=-\widetilde L(g)\). Complete fixed-face enumeration gives \(\chi_3(r)=-1\) and \(\chi_3(s)=+1\). Since this action is a homomorphism to the units \(\{\pm1\}\) of \(\mathbb Z\), it determines \(\chi_3(r^a s^b)=(-1)^a\) for all eight automorphisms.

## Verification

Run `python3 verify_chvatal_higher.py` from this directory. This standalone script uses only Python's standard library and embeds the full graph, pivots, and two symmetry generators. It checks all 4095 nonempty vertex masks, the 424 accepted faces, all 211 matching pairs, the complete directed Hasse graph and its acyclicity, and all eight graph automorphisms. As an additional *independent chain-level consistency test*, it reconstructs the simplicial boundary matrices without using any matching information and checks the homology ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_{101}\). Those finite-field checks are not substitutes for the integral homotopy proof provided by the verified acyclic matching.

## Relationship to prior work

Ghosh and Selvaraja's 2025 higher-independence paper gives the exact \(r\)-independence definition and establishes general shellability criteria for block graphs, certain bounded-diameter *block graphs and trees*, and graph modifications. None yields this result for the four-regular, triangle-free, nonchordal Chvátal graph. The paper was materially inspected in its freely available 2025 HTML form, including its definitions and Sections 4–5.

Published exact calculations on the same Chvátal graph already establish \(\operatorname{Ind}_1(G)\simeq S^2\), and an equivariant simplicial collapse of that *ordinary* independence complex onto its open-neighborhood complex. They also give the full \(D_4\)-character \(\chi_2(r^a s^b)=(-1)^{a+b}\). Those facts do not identify the larger \(\operatorname{Ind}_2(G)\), its 424 faces, or its degree-three orientation character. The two sets of results should not be conflated: this finding uses the strictly broader allowed induced subgraphs and obtains the opposite sign for \(s\).

## Limitations

This is a reproducible finite-graph classification, not an infinite-family theorem or an equivariant homotopy equivalence to a geometric three-sphere with a specified action. The full character describes only the action on integral homology. Unindexed equivalent calculations cannot be excluded. The source date below is the first public date of the cited contemporary higher-independence investigation and is not presented as a publication date for the calculation here.

## References

1. A. Ghosh and S. Selvaraja, *Shellability of Higher Independence Complexes of Graphs*, arXiv:2505.06614, v1 publicly submitted 2025-05-10; full accessible v3: https://arxiv.org/html/2505.06614v3.
2. *The Chvátal graph independence complex and its vertex-deletion dichotomy*, public RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-chv-tal-graph-independence-complex-and-its-vertex-deletion-d--676b14391238/RESULT.md.
3. *An equivariant collapse connecting the Chvátal independence and neighborhood complexes*, public RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-an-equivariant-collapse-connecting-the-chv-tal-independence-and--3077dabdf181/RESULT.md.
4. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145, https://doi.org/10.1006/aima.1997.1650.
