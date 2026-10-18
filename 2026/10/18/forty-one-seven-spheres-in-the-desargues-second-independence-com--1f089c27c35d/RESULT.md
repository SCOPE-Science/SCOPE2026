# Forty-one seven-spheres in the Desargues second-independence complex

## Finding

Let \(D=GP(10,3)\) be the 20-vertex Desargues graph. Its second-independence complex \(X=\operatorname{Ind}_2(D)\), whose faces are vertex sets inducing components of at most two vertices, has the exact **integral homotopy type**

\[
\boxed{\operatorname{Ind}_2(GP(10,3))\simeq\bigvee^{41}S^7.}
\]

In particular, \(\widetilde H_7(X;\mathbb Z)\cong\mathbb Z^{41}\), every other reduced integral homology group vanishes, and the space is 6-connected. This does not assert an equivariant homotopy equivalence.

## Assumptions and scope

The graph has vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/10\mathbb Z\) and the thirty undirected edges \(\{u_i,u_{i+1}\},\{u_i,v_i\},\{v_i,v_{i+3}\}\). Number the vertices \(u_i=i\) and \(v_i=10+i\). A face is a subset \(\sigma\) for which every vertex in \(D[\sigma]\) has induced degree at most one; this is equivalent to every induced component having at most two vertices. All vertex subsets, including the empty set, are examined by the verification code. For Morse matching, the empty face is excluded so an ordinary 0-cell remains critical. Orient every nonempty face by increasing vertex label. All face counts use these conventions.

## Proof

**Finite exhaustive construction.** Using all \(2^{20}=1{,}048{,}576\) bit masks, two independent membership procedures (an induced-degree bound and a direct connected-component search) agree exactly. There are \(62{,}049\) simplices including the empty face. The counts in dimensions \(0\) through \(11\) are

```
20, 190, 1080, 3985, 9784, 15910, 16600, 10390, 3460, 564, 60, 5
```

The facets have cardinalities \(8,9,10,12\), with respective counts \(65,540,234,5\). Thus \(X\) is nonpure, of maximum dimension \(11\). These ancillary counts are checked independently and are not treated as a homotopy proof.

**A complete acyclic matching.** Start with every nonempty face unmatched. For vertices \(w=0,1,\ldots,19\), match each then-unmatched face \(\sigma\) not containing \(w\) with \(\sigma\cup\{w\}\) whenever both are present and unmatched. Delete matched faces before processing the next vertex. Exactly \(31{,}000\) disjoint pairs are formed, leaving one critical 0-cell, three critical 6-cells, and forty-four critical 7-cells. The critical 6-cells have the bit masks

```
0x10b54, 0x22a52, 0x2a24a
```

The matching is acyclic by the sequential-element-matching theorem [1, Proposition 2.10]. Independently, orient every nonempty face incidence downward unless it belongs to a matched pair, in which case orient it upward. A complete topological sort visits all \(62{,}048\) nonempty faces across the \(400{,}760\) directed incidences. Forman's discrete-Morse theorem therefore gives a CW complex consisting of one 0-cell, three 6-cells and forty-four 7-cells, with no other cells.

**Exact signed attaching degrees.** For an oriented simplex \(\tau\), the coefficient of its face \(\tau\setminus\{i\}\) in the simplicial boundary is

\[
[\tau:\tau\setminus\{i\}]=(-1)^{|\{j\in\tau:j<i\}|}.
\]

Calculate the integral Morse differential \(\partial^{M}_7:\mathbb Z^{44}\longrightarrow\mathbb Z^3\) by repeatedly eliminating a matched 6-face \(\sigma\) with its 7-face \(\tau\) through the unit signed incidence \([\tau:\sigma]\). The recursion follows all relevant gradient paths and evaluates all forty-four integral columns; it does not infer the attaching degrees from mod-two ranks. In the ordered critical 6-cell basis listed above, the 7-cells encoded by

```
0x18e94, 0x55292, 0x61664
```

have respective integral boundary columns

\[
(1,0,0)^T,\qquad(0,0,1)^T,\qquad(0,1,0)^T.
\]

These form an integer minor of determinant \(-1\). Consequently \(\partial^{M}_7\) is split surjective, has Smith invariants \((1,1,1)\), and its kernel is free abelian of rank \(44-3=41\). The CW 6-skeleton is \(\bigvee^3S^6\). Because \(\pi_6(\bigvee^3S^6)\cong\mathbb Z^3\), the attaching maps of the forty-four 7-cells are completely classified by precisely these signed degree vectors. The unimodular minor allows integer elementary changes of the 6- and 7-cell bases, yielding three cancelling degree-one attachments and forty-one nullhomotopic attachments. Therefore the complete CW complex is homotopy equivalent to \(\bigvee^{41}S^7\), as claimed. This last conclusion is stronger than the homology computation.

## Verification

The supplied standalone `verify.py` uses Python 3 standard library only and reconstructs the graph, all \(2^{20}\) induced subgraphs, all valid simplices, all facets, every matched pair and every directed Hasse incidence. It checks the complete directed acyclicity, all signed integral Morse boundary columns, and the displayed primitive three-column minor. Separately, direct simplicial mod-two boundary ranks in dimensions \(5\) through \(9\) are

```
6708, 9202, 7398, 2951, 509
```

and imply \(\widetilde\beta_7(X;\mathbb F_2)=41\) and \(\widetilde\beta_6(X;\mathbb F_2)=0\). The exact integral Morse proof, not the mod-two calculation, establishes the stated homotopy type. Execute `python3 verify.py` after extraction; success prints `DESARGUES_IND2_INTEGRAL_HOMOTOPY_VERIFIED`. No external files, network access, CAS, or cached computations are needed.

## Relationship to prior work

Deshpande and Singh [1] introduced and analyzed higher-independence homotopy for complete multipartite graphs, fully whiskered graphs, paths, cycles and perfect rooted trees, and provided the acyclic matching method used here. Their classification does not contain this Desargues graph calculation. The subsequent chordal/trees/caterpillar results [2,3] concern graph families other than this nonchordal cubic girth-six graph. They establish no homotopy classification for \(\operatorname{Ind}_2(D)\).

The twenty-vertex graph is also the bipartite Kneser graph \(H(5,2)\), equivalently the canonical bipartite double cover of the Petersen graph [4]. Its *ordinary* independence complex has a separately published integral homotopy classification \(S^4\vee\bigvee^5S^5\) [5]. That different complex allows no induced graph edges; the second-independence complex studied here allows isolated edges. The ordinary matching complex of \(D\) also uses **graph edges** as its simplex vertices and does not imply this result. The published classification of the second-independence complex of the Petersen graph concerns a different ten-vertex graph; it is not transferred automatically through a bipartite double cover. No equivalent determination of the stated forty-one-sphere wedge was identified in the checked sources or equivalent-name searches.

## Limitations

The claim is an exact nonequivariant result for the explicitly defined finite graph. It does not determine the inclusion-induced map from ordinary independence, automorphism representations, or analogous complexes of larger bipartite Kneser graphs. Exhaustiveness is achieved because every vertex subset and every matching incidence is checked, not by extrapolating experiments. An unindexed equivalent classification cannot be ruled out by searches alone. No independent scientific audit has been performed.

## References

1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, first posted January 15, 2020, arXiv:2001.05448v1; especially Proposition 2.10 and Theorems 3.5, 3.8, 4.6, 5.6. https://arxiv.org/abs/2001.05448
2. P. Deshpande, S. Shukla and A. Singh, *Distance r-domination number and r-independence complexes of graphs*, arXiv:2001.06775v1 (2020). https://arxiv.org/abs/2001.06775
3. *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1 (2021), sections 2–4. https://arxiv.org/abs/2106.10863
4. E. W. Weisstein, *Bipartite Kneser Graph*, MathWorld, definition and graph aliases. https://mathworld.wolfram.com/BipartiteKneserGraph.html
5. *The Desargues graph independence complex is \(S^4\vee\bigvee^5S^5\)*, publicly indexed mathematical research finding (October 11, 2026), as available in the published-finding corpus 2026 mathematical records. This source concerns \(\operatorname{Ind}_1(D)\), not \(\operatorname{Ind}_2(D)\).
