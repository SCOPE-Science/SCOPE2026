# The Tietze perfect-matching complex: six circles and its full rational symmetry character

## Finding

Let \(T\) be the Tietze cubic graph, constructed by replacing a single vertex of the Petersen graph with a triangle and attaching one of its three former neighbors to each triangle vertex. Let \(X=\mathcal M_{\mathrm p}(T)\) be the perfect-matching complex: a face is an edge subset extendible to a perfect matching. Then

\[
X\simeq\bigvee^{6}S^1,
\qquad \widetilde H_1(X;\mathbb Z)\cong\mathbb Z^6,
\qquad \widetilde H_j(X;\mathbb Z)=0\quad(j\ne1).
\]

The graph automorphism group is \(G=\operatorname{Aut}(T)\cong S_2\times S_3\), of order \(12\). Its rational first-homology character is completely determined by

\[
\chi_1(g)=\begin{cases}
6,&g=1,\\
-2,&g\text{ is one of the three involutions fixing exactly four graph vertices},\\
0,&\text{otherwise}.
\end{cases}
\]

In particular \(H_1(X;\mathbb Q)^G=0\). This does not assert that the sphere-wedge equivalence is equivariant.

## Assumptions and scope

Start from \(KG(5,2)\), whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), with two vertices adjacent exactly when disjoint. Replace \(\{0,1\}\) by three new vertices \(t_0,t_1,t_2\) spanning a triangle. Connect \(t_j\) to the \(j\)-th member of the ordered list \((\{2,3\},\{2,4\},\{3,4\})\). The other Petersen edges are unchanged. Thus \(T\) is specified without reliance on a drawing: it has 12 graph vertices and 18 graph edges, and exactly one triangle. Denote the 18 graph edges by indices from 0 through 17 as in the verifier (the verifier generates this enumeration deterministically).

A perfect matching means a set of six pairwise disjoint graph edges covering all twelve graph vertices. The complex \(X\) has every such matching as a five-simplex facet and all its subsets as faces. The homotopy statement concerns the geometric realization of this finite simplicial complex.

## Proof

**Perfect matchings.** Each perfect matching uses either exactly one or exactly three edges joining the new triangle to the three old neighbors, because the remaining triangle vertices must be covered internally. With one such spoke, contraction of the triangle recovers a perfect matching of the Petersen graph: there are exactly six. With three spokes, the remaining six old vertices form a six-cycle and admit exactly two matchings. Therefore \(T\) has exactly eight perfect matchings. In deterministic graph-edge indices, the eight sets are:

```
[0,4,6,12,13,14]
[1,3,7,12,13,14]
[1,3,8,10,14,15]
[0,5,6,11,14,15]
[0,4,8,9,13,16]
[2,3,7,11,13,16]
[1,5,7,9,12,17]
[2,4,6,10,12,17]
```

The complete independent enumeration in `verify.py` checks this classification directly.

**A small nerve.** Cover \(X\) by its eight maximal matching simplices \(A_0,\ldots,A_7\) in the displayed order. Each nonempty intersection of these facets is a simplex and hence contractible. The simplicial nerve theorem therefore gives \(X\simeq N\), where a subset of \(\{0,\ldots,7\}\) is a face of \(N\) exactly if the corresponding perfect matchings share a graph edge. Its 15 inclusion-maximal simplices, written as index tuples, are

```
(0,1,2,3) (0,1,4,5) (0,1,6,7)
(0,3,4) (0,3,7) (0,4,7)
(1,2,5) (1,2,6) (1,5,6)
(2,4) (2,7) (3,5) (3,6) (4,6) (5,7)
```

These follow by inspecting the graph edge-index sets of the eight perfect matchings: the collection of matching indices containing any fixed graph edge is a simplex in \(N\), and every simplex of \(N\) arises in this fashion. The nerve has \(8\) vertices, \(28\) edges, \(18\) triangles and \(3\) tetrahedra.

**Explicit elementary collapses.** Each tuple on the left below denotes a free codimension-one face of the unique maximal simplex on the right. Remove the indicated face and coface in the displayed order:

```
(1,2,3) < (0,1,2,3)   (1,4,5) < (0,1,4,5)   (1,6,7) < (0,1,6,7)
(1,3)   < (0,1,3)     (1,4)   < (0,1,4)     (1,7)   < (0,1,7)
(2,3)   < (0,2,3)     (0,2)   < (0,1,2)     (3,4)   < (0,3,4)
(3,7)   < (0,3,7)     (4,5)   < (0,4,5)     (0,5)   < (0,1,5)
(0,1)   < (0,1,6)     (4,7)   < (0,4,7)     (6,7)   < (0,6,7)
(2,5)   < (1,2,5)     (2,6)   < (1,2,6)     (5,6)   < (1,5,6)
```

After these 18 elementary collapses, the remaining simplicial complex is a connected graph with the same eight vertices and these thirteen edges:

```
(0,3) (0,4) (0,6) (0,7) (1,2) (1,5) (1,6)
(2,4) (2,7) (3,5) (3,6) (4,6) (5,7)
```

Its cycle rank is \(13-8+1=6\). Every finite connected graph is homotopy equivalent to a wedge of circles with multiplicity its cycle rank. The displayed free-face sequence and nerve theorem prove the claimed integral homotopy type, rather than only its Euler characteristic or mod-two Betti numbers.

**The complete symmetry character.** The Tietze graph has a unique triangle. Any automorphism fixes this triangle setwise and contracts to an automorphism of the Petersen graph fixing the original vertex \(\{0,1\}\); conversely that vertex stabilizer lifts to \(T\). Thus \(G\cong S_2\times S_3\) and has order twelve. For every automorphism, its action on \(X\) permutes graph edges and hence oriented simplices. The Lefschetz number is the alternating sum of their signed fixed-simplex traces. Since \(X\) is connected and has homology only in degrees zero and one, the integral Lefschetz identity gives

\[
\chi_1(g)=1-\sum_{q\ge0}(-1)^q\operatorname{tr}\bigl(g\mid C_q(X;\mathbb Q)\bigr).
\]

For an invariant oriented simplex, the chain trace is the sign of the induced permutation of its ordered graph edges; non-invariant simplices contribute zero. The finite orbit classification gives three nonidentity automorphisms with four fixed graph vertices, all involutions, and trace \(-2\); the other eight nonidentity automorphisms all have trace zero. The full table is independently reproduced from both the original complex and the eight-vertex nerve in the verifier. Averaging traces over the twelve group elements gives \((6+3(-2))/12=0\) invariant dimensions. This completes the symmetry assertion.

## Verification

Run `python3 verify.py` using Python 3 and the standard library only. The checker constructs the graph from the stated Petersen triangle expansion, independently enumerates perfect matchings by recursion and by examining every six-edge subset, reconstructs all 443 nonempty faces, independently checks the nerve maximal faces and each of the 18 free-face removals, and confirms that the resulting 8-vertex, 13-edge graph is connected. It also builds an independent 218-pair acyclic discrete-Morse matching on the original complex, checks the entire oriented Hasse diagram for directed cycles, enumerates all 12 automorphisms and computes every signed rational character value twice, once on the full complex and once on its nerve. All checks passed. The proof itself uses the finite, explicitly displayed collapse certificate and elementary topological theorems; no inference from a sample of graph orders is involved.

## Relationship to prior work

Bayer, Jelić Milutinović and Vega introduce perfect-matching complexes and determine their topology for certain hexagonal honeycomb families; their full text explicitly applies the nerve theorem and discrete-Morse theory to those families, not this triangle-inflated Petersen graph. Chandrakar and Singh classify such complexes for two-row grids and polygonal line tilings. The Tietze graph is neither an instance of the honeycomb graphs in the former nor of the linear tilings in the latter. The ordinary matching complex and the perfect-matching complex are different constructions; general graph-matching enumeration results do not supply these topological or equivariant invariants. The related Petersen perfect-matching complex has a different face cover, so its invariants do not imply the Tietze result merely by contraction or triangle inflation. No stronger theorem implying this statement was identified among the inspected sources; an unindexed equivalent calculation remains possible.

## Limitations

This is a classification for one canonical graph, not a uniform classification of flower snarks, triangle inflations, or all cubic graphs. The displayed wedge equivalence is not asserted equivariant, although the character is computed for the intrinsic group action. The character is rational; no complete integral isomorphism type of the symmetry module is claimed. Literature coverage is necessarily bounded; absence of indexed exact statements is not proof of absolute publication priority. Independent external auditing has not occurred.

## References

1. M. Bayer, M. Jelić Milutinović, and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1 (first public version 2022-09-06); Electron. J. Combin. 30 (2023), P2.45. https://arxiv.org/abs/2209.02803
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809 (first public version 2024-07-08). https://arxiv.org/abs/2407.05809
3. E. W. Weisstein, *Tietze Graph*, MathWorld, https://mathworld.wolfram.com/TietzeGraph.html (graph description and context).
