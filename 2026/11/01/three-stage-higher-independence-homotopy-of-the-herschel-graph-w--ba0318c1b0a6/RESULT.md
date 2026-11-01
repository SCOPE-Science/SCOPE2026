# Three-stage higher-independence homotopy of the Herschel graph with null transition maps

## Finding

Let \(H\) be the eleven-vertex Herschel graph with the labeled edges specified below. For \(r\in\{1,2,3\}\), let \(\operatorname{Ind}_r(H)\) denote the complex of vertex subsets whose induced connected components have at most \(r\) vertices. Then the integral homotopy types are

\[
\operatorname{Ind}_1(H)\simeq\bigvee^2 S^2,\qquad
\operatorname{Ind}_2(H)\simeq\bigvee^{10}S^3,\qquad
\operatorname{Ind}_3(H)\simeq\bigvee^3 S^4\vee S^5.
\]

The first equivalence was previously established for the ordinary independence complex; the two higher-cutoff classifications are the new results. Both natural simplicial inclusions in the truncated filtration

\[
\operatorname{Ind}_1(H)\hookrightarrow\operatorname{Ind}_2(H)
\hookrightarrow\operatorname{Ind}_3(H)
\]

are nullhomotopic. In particular, no positive-degree reduced integral homology class survives either successive inclusion. At the third cutoff the homotopy type is mixed-dimensional: three four-sphere summands and one five-sphere summand.

## Assumptions and scope

The graph is finite, simple, and undirected, with vertex set \(\{0,1,\ldots,10\}\) and precisely these eighteen edges, written with smaller endpoint first:

```
(0,5) (0,6) (0,9) (0,10)
(1,5) (1,6) (1,7) (1,8)
(2,7) (2,8) (2,9) (2,10)
(3,5) (3,7) (3,9)
(4,6) (4,8) (4,10)
```

This is a standard labeled realization of the Herschel graph. The first five vertices form one bipartition class and the last six form the other. Vertex degrees are \(4,4,4,3,3,3,3,3,3,3,3\). In particular, this is not a tree, a complete multipartite graph, a cycle, a fully whiskered graph or a chordal graph. For cutoff two the face condition is equivalently that the induced subgraph have maximum degree at most one (the dissociation-complex convention).

Every complex includes the empty simplex. Homotopy statements concern geometric realizations. No assertion is made at any cutoff \(r\ge4\), for arbitrary polyhedral graphs, or for graph automorphism actions.

## Proof

**Exact construction.** Encode a vertex subset by the eleven-bit mask \(m=\sum_{v\in\sigma}2^v\). For each \(r\in\{1,2,3\}\), enumerate all \(2^{11}=2048\) masks and retain those for which every connected component of the induced subgraph has at most \(r\) vertices. An independent second test rejects any mask containing a connected \((r+1)\)-vertex induced subset. The tests agree on every mask: there are respectively 124, 346, and 658 augmented faces. The forbidden connected subsets number 18, 42, and 89, respectively.

The complete face counts, with the empty face in dimension minus one, are:

| Cutoff | \(f_{-1}\) | \(f_0\) | \(f_1\) | \(f_2\) | \(f_3\) | \(f_4\) | \(f_5\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 11 | 37 | 45 | 22 | 7 | 1 |
| 2 | 1 | 11 | 55 | 123 | 121 | 34 | 1 |
| 3 | 1 | 11 | 55 | 165 | 241 | 154 | 31 |

**Complete acyclic matchings.** On the augmented face poset, use successive element matchings: at each listed vertex, pair every still-unmatched face not containing that vertex with its single-vertex coface whenever the latter remains available. The deterministic toggle orders for cutoffs one, two, and three are respectively

```
(6,5,8,2,7,1,4,10,9,3,0)
(10,5,4,2,8,6,0,1,7,3,9)
(4,2,3,0,10,6,9,5,8,7,1)
```

Proposition 2.10 in Deshpande–Singh states that successive element matchings are acyclic. Independently, the included checker constructs every codimension-one Hasse incidence, reverses matched incidences, and performs a complete directed acyclicity test. All 349, 1,150 and 2,536 incidences are checked without a cycle. The respective numbers of matching pairs are 61, 168 and 327. In every case the empty simplex is paired, so an implicit basepoint is supplied in the resulting ordinary CW model.

The remaining critical cells are exactly: two dimension-two cells for cutoff one; ten dimension-three cells for cutoff two; and three dimension-four cells plus one dimension-five cell for cutoff three. All other augmented faces have been paired. For auditability, the critical masks at the three cutoffs are

```
r=1: 145,1034
r=2: 27,30,216,269,408,449,582,600,771,792
r=3: 457,1610,1667,2016
```

**Signed integral attachments.** Orient each simplex by ascending vertex order and use the ordinary alternating signed simplicial boundary. The checker eliminates every matched face/coface pair by an exact integral unit-pivot chain contraction. For all 556 matching pairs over the three stages the pivot is \(\pm1\); all coefficients are integers, and every remaining Morse differential is identically zero. At cutoff three this includes the integral matrix from the unique dimension-five critical cell to the three dimension-four critical cells: it is the zero \(3\times1\) column, not merely zero modulo two.

For cutoffs one and two, the associated CW complex is one point with cells concentrated in a single positive dimension, hence the displayed sphere wedges. At cutoff three the four-skeleton is \(\bigvee^3S^4\). This space is three-connected, so its Hurewicz homomorphism \(\pi_4\to H_4(-;\mathbb Z)\) is an isomorphism. The unique five-cell has zero attaching degrees in each four-sphere by the exact integral Morse matrix; its attaching map is therefore nullhomotopic. This proves \(\bigvee^3 S^4\vee S^5\), not only the Betti numbers.

**Inclusion maps.** Every map from the wedge of two two-spheres to the two-connected wedge of ten three-spheres is nullhomotopic. Likewise, every map from the wedge of ten three-spheres to the three-connected third-stage wedge is nullhomotopic. Thus both specific simplicial inclusion maps are nullhomotopic. No statement about the inclusion from cutoff three onward is needed.

## Verification

Run `python3 verify_herschel_higher_independence.py` using Python 3 and only its standard library. The checker reconstructs the graph in two ways, enumerates the exact face sets in two independent ways, checks all Hasse edges and matching acyclicity, performs exact signed integral pivot elimination, and separately computes all simplicial boundary ranks over \(\mathbb F_2\). Its terminal verification marker is `HERSCHEL_HIGHER_INDEPENDENCE_1_2_3_INTEGRAL_OK`; the actual output is included in `verification_herschel_output.txt`.

The independent reduced mod-two Betti groups have ranks two in degree two at cutoff one, ten in degree three at cutoff two, and three in degree four plus one in degree five at cutoff three, with all other reduced ranks zero. The mod-two checks corroborate but do not replace the integral attaching-map proof.

## Relationship to prior work

Deshpande–Singh, *Higher Independence Complexes of graphs and their homotopy types* (arXiv:2001.05448, first public January 15, 2020), introduced systematic homotopy classifications for several families, including complete multipartite, fully whiskered, path, cycle and perfect rooted-tree graphs; it supplies the staged element-matching acyclicity theorem. None of those families contains the explicitly defined Herschel graph. Deshpande–Shukla–Singh, *Distance r-domination number and r-independence complexes of graphs* (arXiv:2001.06775), proves broad connectivity facts and a sphere-wedge theorem for chordal graphs, but the Herschel graph contains induced four-cycles, so that hypothesis does not hold; neither result determines this graph's exact higher-cutoff homotopy type.

The public result *The Herschel graph independence complex and its complete vertex-deletion profile* gives the ordinary case \(\operatorname{Ind}_1(H)\simeq\bigvee^2 S^2\), together with its deletion/link profile, for the identical labeled edge list. That result is properly credited here and does not imply the two higher-cutoff classifications or the maps between their complexes. The terms 'two-independence', 'dissociation complex', and 'induced maximum degree one' were compared as equivalent names for cutoff two. Targeted source and theorem searches found no covering exact result; absence from search results alone is not a proof of novelty.

## Limitations

This is an exhaustive, graph-specific finite calculation, not a general classification of polyhedral graphs. The attaching maps are determined integrally through the displayed algebraic cancellations; the mod-two rank calculations alone would not prove the integral homotopy types. The first-stage homotopy type is acknowledged as previously published, not independently claimed as new. Other historical results may exist outside indexed sources.

## References

- P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448, first public 2020-01-15, https://arxiv.org/abs/2001.05448.
- P. Deshpande, S. Shukla, and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775, first public 2020-01-19, https://arxiv.org/abs/2001.06775.
- *The Herschel graph independence complex and its complete vertex-deletion profile*, publicly available RESULT.md, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-the-herschel-graph-independence-complex-and-its-complete-vertex--e6d752a4b77d/RESULT.md.
- E. W. Weisstein, *Herschel Graph*, MathWorld, https://mathworld.wolfram.com/HerschelGraph.html.
