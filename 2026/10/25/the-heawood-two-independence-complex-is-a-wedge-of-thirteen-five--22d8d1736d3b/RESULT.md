# The Heawood two-independence complex is a wedge of thirteen five-spheres

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, the incidence graph of the Fano plane. Its two-independence complex has the **integral homotopy type**
\[
\operatorname{Ind}_2(H)\simeq\bigvee^{13}S^5.
\]
This is also the three-path-free complex of \(H\). The statement concerns **vertex** subsets with induced components of order at most two; it does not concern edge matching complexes.

## Assumptions and scope

The point vertices are \(0,1,\ldots,6\) and the line vertices are \(7,8,\ldots,13\). The seven incident point triples, in the order defining line vertices, are

```
(0,1,2), (0,3,4), (0,5,6), (1,3,5),
(1,4,6), (2,3,6), (2,4,5)
```

A point vertex is adjacent precisely to its incident line vertices. Every two distinct points occur together in exactly one line and the resulting graph has fourteen vertices and twenty-one edges. Define \(K=\operatorname{Ind}_2(H)\). For any subset \(S\) of its fourteen vertices, \(S\in K\) exactly when every vertex of the induced graph \(H[S]\) has degree at most one: a connected graph has at most two vertices if and only if its maximum degree is at most one, provided it is a disjoint union of isolated edges and vertices; conversely a graph of maximum degree one is such a union. This definition includes the empty face.

## Proof

All faces of \(K\) are determined by the preceding incidence data. Represent a face by its fourteen-bit integer mask. Start with all valid masks \(F\). For each vertex index \(v=0,1,\ldots,13\), in this order, form *every* pair \((S,S\cup\{v\})\) such that both faces still remain unpaired and \(v\notin S\), then remove both faces before advancing to the next vertex. Because the lower face contains no \(v\), these pairs are disjoint at each stage. This is the sequential element matching of Deshpande and Singh, Proposition 2.10; it is acyclic. Moreover, the independent directed-Hasse acyclicity check described below certifies this instance without reliance on the generic matching theorem.

For completeness, the first pair is the augmented empty-face pair \((\varnothing,\{0\})\). Delete that pair from the matching **on nonempty faces**, thereby leaving the single vertex \(\{0\}\) critical. The removed empty face has no place in the nonempty face poset. Every remaining nonempty pair is unchanged. The acyclicity verification explicitly uses this modified, nonempty matching.

The exhaustive face enumeration yields the face counts, indexed by simplicial dimensions \(-1,0,1,\ldots,6\),

```
1, 14, 91, 322, 651, 728, 392, 58.
```

The matching contains exactly \(1,121\) pairs of **nonempty** faces. Its unmatched nonempty faces are exactly one vertex and thirteen faces having six vertices each. The latter face masks are, in increasing order,

```
980, 3300, 5488, 6712, 8064, 9816, 10600,
12160, 12514, 14208, 15232, 15744, 16000.
```

For the complete Hasse diagram on all \(2,256\) nonempty faces, orient every unmatched face-cover relation from the larger face to the smaller face and reverse the \(1,121\) matched relations. The resulting directed graph has \(10,150\) arrows and admits a topological ordering visiting all \(2,256\) vertices, so it is acyclic. These are finite exact checks over every face and covering relation, not a sample or a mod-two approximation.

Discrete Morse theory therefore gives a CW complex homotopy equivalent to \(K\), with exactly one cell in dimension zero, thirteen cells in dimension five, and no other cells. Each five-dimensional attaching map has target the single zero-cell; hence it is constant. The CW complex is a wedge of thirteen five-spheres. This proves the **integral** homotopy equivalence; no assumptions about field coefficients or unknown attaching degrees are needed.

## Verification

Run `python3 verify_heawood.py` beside this file; the expected stdout is recorded verbatim in `verification_output.txt`. The standalone script constructs the graph independently from the seven point triples; enumerates all \(2^{14}=16,384\) candidate masks using two equivalent but separately implemented predicates (induced maximum degree and connected-component breadth-first search); constructs the Morse matching; verifies the complete reversed Hasse directed graph is acyclic; and recomputes all reduced mod-two boundary ranks. The independent homology check returns the complete reduced mod-two Betti vector \((0,0,0,0,0,13,0)\), compatible with—but not used to infer—the integral wedge equivalence.

## Relationship to prior work

Sawant (May 24, 2026) establishes vertex decomposability of higher independence complexes for **trees**, and explicitly identifies two-independence with three-path-free complexes. The Heawood graph contains six-cycles and therefore does not satisfy the tree hypothesis. Deshpande and Singh (2020) establish homotopy types for selected classes, including complete multipartite graphs, whiskered graphs, cycles, and perfect rooted trees, and provide the sequential element-matching principle employed here; their inspected claims do not classify this Fano-incidence example. Abdelmalek and coauthors (2021) address chordal graphs; the Heawood graph is nonchordal.

Nearby public Heawood calculations concern the **ordinary one-independence complex** (which has six three-sphere summands), **two-matching complexes on edge subsets**, or cut complexes. Their underlying simplicial complexes differ from the vertex-subset complex here, so their stated results do not imply this thirteen-sphere conclusion. A record classifying the two-independence complex of the Petersen graph likewise concerns a different graph and does not imply the present value.

## Limitations

This is one exact natural finite graph, not a theorem for all cubic graphs, all incidence graphs, all higher parameters, or arbitrary Fano-plane generalizations. The proof establishes nonequivariant integral homotopy; no automorphism representation is asserted. An exhaustive search is not a mathematical proof of bibliographic priority; further unpublished or unindexed results might exist. The executable verifier and the mathematical matching argument are supplied for reproducibility; independent scientific validation has not yet been performed.

## References

1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, first posted May 24, 2026, https://arxiv.org/html/2605.25150v1 .
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v2, https://arxiv.org/html/2001.05448v2 , especially Proposition 2.10.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, https://arxiv.org/abs/2106.10863 .
4. Public published-finding corpus findings on ordinary Heawood independence and Heawood two-matching complexes (distinct objects): `2026/10/4/SCOPE-the-heawood-independence-complex-is-bigvee-6-s-3--dbd95019d1e2` and `2026/10/11/SCOPE-the-heawood-two-matching-complex-is-a-wedge-of-six-10-spheres--5bc5713358d6`.
