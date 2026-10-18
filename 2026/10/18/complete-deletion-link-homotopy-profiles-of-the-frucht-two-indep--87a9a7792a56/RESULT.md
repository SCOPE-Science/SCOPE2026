# Complete deletion–link homotopy profiles of the Frucht two-independence complex

## Finding
Let \(F\) be the twelve-vertex cubic Frucht graph with the explicit edge set below and let \(K=\operatorname{Ind}_2(F)\) be the simplicial complex of vertex subsets whose induced connected components have at most two vertices. Then
\[
K\simeq S^3.
\]
The following table **completely classifies the homotopy types of all twelve vertex deletions and links**, with \(K-v=\operatorname{Ind}_2(F-v)\). The symbol \(\mathrm{pt}\) means a contractible realization.

| Vertex | Deletion | Link |
|:---:|:---|:---|
| 0 | \(\bigvee^{2}S^{3}\) | \(S^{2}\vee\bigvee^{2}S^{3}\) |
| 1 | \(\bigvee^{2}S^{3}\) | \(S^{3}\) |
| 2 | \(\bigvee^{2}S^{3}\) | \(S^{3}\) |
| 3 | \(S^{3}\) | \(\mathrm{pt}\) |
| 4 | \(\bigvee^{2}S^{3}\) | \(S^{3}\) |
| 5 | \(\bigvee^{2}S^{3}\) | \(S^{3}\) |
| 6 | \(S^{3}\) | \(S^{2}\vee S^{3}\) |
| 7 | \(\bigvee^{3}S^{3}\) | \(\bigvee^{2}S^{3}\) |
| 8 | \(S^{3}\) | \(S^{2}\vee S^{3}\) |
| 9 | \(\bigvee^{2}S^{3}\) | \(S^{2}\vee\bigvee^{2}S^{3}\) |
| 10 | \(\bigvee^{2}S^{3}\) | \(S^{3}\) |
| 11 | \(\bigvee^{4}S^{3}\) | \(\bigvee^{3}S^{3}\) |

The natural inclusion \(K-v\hookrightarrow K\) is a homotopy equivalence for \(v=3\). For \(v=6\) and \(v=8\), both source and target are homotopy equivalent to \(S^3\), but the induced homomorphism on integral third homology is **zero**. At the other nine vertices, the deletion has third Betti rank different from that of \(K\), so the inclusion cannot be a homotopy equivalence.

## Assumptions and scope
All graphs are finite, undirected and simple. The vertex set of \(F\) is \(\{0,1,\ldots,11\}\), with edges specified by this complete Python literal:

```python
EDGES=((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
       (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
```

This graph is isomorphic to the standard Frucht graph with LCF increments `[-5,-2,-4,2,5,-2,2,5,-2,-5,4,2]`. The independent verifier supplies and checks an explicit isomorphism. For a simplicial complex \(K\), the deletion contains the faces omitting vertex \(v\), and the link contains faces \(\sigma\) disjoint from \(v\) such that \(\sigma\cup\{v\}\) is a face. The 2-independence condition is equivalently the absence of a connected induced three-vertex subgraph, i.e. the usual 3-path-free condition (the word path here means a possibly non-induced three-vertex path). All asserted equivalences are of geometric realizations and are integral, not merely mod-two homology statements.

## Proof
**Exact enumeration.** For every one of the \(2^{12}-1\) nonempty vertex subsets, a breadth-first traversal checks that each induced connected component has size at most two. Exactly **824** subsets pass, with \(f\)-vector \( (12,66,190,293,209,53,1)\) in dimensions zero through six. The second verifier independently obtains precisely the same face set by excluding all connected induced three-vertex subsets. The two algorithms use different representations of the condition.

**Acyclic matchings.** On each of the 25 nonempty face posets (the whole complex, twelve deletions and twelve links), run staged toggling in vertex order \(0,1,\ldots,11\). At the stage for vertex \(v\), pair each still-unmatched face \(\sigma\) omitting \(v\) with \(\sigma\cup\{v\}\) whenever both faces remain unmatched. Each pair is a codimension-one incidence, and no simplex is used twice. Reverse these incidences in the directed Hasse diagram (with unmatched incidences directed downward) and topologically sort the entire graph. All **25** complete sorts terminate, so these are bona fide acyclic discrete-Morse matchings. Every matching and every directed cover is constructed from the stated edge list in `verify_frucht_ind2_morse.py`.

**Integral attaching degrees.** Use the increasing-vertex orientation of simplices and cancel each matched face–coface pair in the integral cellular boundary matrices, using its verified unit coefficient. The verifier performs every integral column update and tests that the final Morse boundary squares to zero. For \(K\), 410 matched pairs leave one critical zero-cell, two critical three-cells and one critical four-cell; the only nonzero Morse boundary is a unit from the four-cell to one of the three-cells. The resulting CW complex is \(S^3\), because \(\pi_3(\bigvee^2 S^3)\cong\mathbb Z^2\) and the primitive attaching vector is equivalent to \((1,0)\). The same argument handles every deletion, whose critical cells consist of one zero-cell, some three-cells and at most one four-cell, with every nonzero four-to-three boundary vector primitive.

For each link the critical cells comprise one zero-cell and possibly two- and three-cells, with no one-cells or cells of dimension at least four. Each nonzero three-to-two Morse boundary has rank one and contains a unit entry; all other Morse boundaries vanish. Since \(\pi_2(\bigvee^q S^2)\cong\mathbb Z^q\), elementary integral basis changes reduce every such map to a unit projection, yielding exactly the link wedges in the table. In particular, vertex 3 has a link with only one critical vertex, hence it is contractible. The full signed sparse Morse matrices and critical-cell labels are printed by the provided verifier; these are not conclusions inferred from mod-two ranks alone.

**Inclusion maps.** The decomposition \(K=(K-v)\cup(v*\operatorname{lk}_K(v))\) is an ordinary homotopy-cofibration diagram. For \(v=3\), the link is contractible, so inclusion of the deletion is a homotopy equivalence. For \(v\in\{6,8\}\), exactness of
\[
\widetilde H_3(\operatorname{lk}_K(v))\longrightarrow
\widetilde H_3(K-v)\longrightarrow
\widetilde H_3(K)\longrightarrow
\widetilde H_2(\operatorname{lk}_K(v))\longrightarrow 0
\]
combines with the proved types \(\widetilde H_3(K-v)\cong\widetilde H_3(K)\cong\widetilde H_2(\operatorname{lk}_K(v))\cong\mathbb Z\). The connecting homomorphism \(\mathbb Z\to\mathbb Z\) must be onto, thus is an isomorphism; exactness forces the deletion inclusion to induce the zero map on \(\widetilde H_3\). All remaining vertex deletions have third Betti rank unequal to one. This proves every assertion.

## Verification
Run `python3 verify_frucht_ind2_morse.py` and `python3 verify_frucht_ind2_homology.py` with Python's standard library. The first completely enumerates 25 complexes, checks all Morse face–coface incidences and global Hasse DAGs, computes exact signed integer Morse boundaries by unit-pivot cancellations, verifies boundary-squared-zero and the complete table. The second independently reconstructs the graph from its LCF description, enumerates faces using forbidden connected triples, computes all mod-two simplicial boundary ranks, and checks the full/deletion/link reduced Betti groups. The recorded standard output files are part of this package.

## Relationship to prior work
Sawant, arXiv:2605.25150v1 (first publicly dated May 24, 2026), proves vertex decomposability for higher-independence complexes of **trees**. The Frucht graph has an induced four-cycle on vertices \(\{2,3,8,9\}\), so it is not a tree; that theorem neither yields its homotopy type nor its deletion maps. The foundational Deshpande–Singh classification treats complete multipartite, fully whiskered, cycle and perfect-ary-tree families, not this graph. Published ordinary-independence calculations for the **same Frucht graph** establish \(\operatorname{Ind}(F)\simeq\bigvee^3 S^2\) and give all its ordinary vertex-deletion profiles, but the allowed vertex subsets are different: \(\operatorname{Ind}(F)\subsetneq\operatorname{Ind}_2(F)\). They therefore do not imply the present 2-independence classification or the null-homology inclusion maps at two vertices. Relevant exact searches are documented in `AUDIT.json`; no equivalent or dominating published result was identified in the inspected sources.

## Limitations
This is an exact computation for one labeled canonical graph, not a theorem for arbitrary asymmetric or cubic graphs. Mod-two boundary ranks alone would not prove the homotopy statements; the proof uses full acyclic matching and integral attaching-degree checks. The literature search cannot rule out inaccessible or unindexed equivalent work. These conclusions have not undergone independent scientific audit.

## References
1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, 24 May 2026, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448v1 (2020); Journal of the Ramanujan Mathematical Society 36 (2021), 53–71.
3. E. W. Weisstein, *Frucht Graph*, MathWorld, https://mathworld.wolfram.com/FruchtGraph.html (LCF data and graph invariants).
4. Public Frucht graph **ordinary** independence complex and vertex-deletion theorem, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-frucht-graph-independence-complex-and-its-complete-vertex-de--8b7d9b2243c2.
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
