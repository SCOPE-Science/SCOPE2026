# A four-point Morse classification of the second independence complexes of Kneser pair graphs

## Finding

**Theorem.** For every integer \(n\geq 6\), let \(KG(n,2)\) be the simple graph whose vertices are the two-element subsets of \(\{0,1,\ldots,n-1\}\), with two vertices adjacent precisely when the corresponding pairs are disjoint. Then

\[
\operatorname{Ind}_2(KG(n,2))\simeq\bigvee^{\binom{n-1}{4}} S^3.
\]

In particular, the only nonzero reduced integral homology is \(\widetilde H_3\cong\mathbb Z^{\binom{n-1}{4}}\). The proof gives an explicit acyclic discrete-Morse matching uniform in \(n\), with precisely \(\binom{n-1}{4}\) critical three-cells and one base vertex; it is a full integral homotopy classification, not an inference from finite ranks. The construction also applies to \(n=5\), recovering the separately known Petersen-graph boundary case \(S^3\); this special case is not claimed as new.

## Assumptions and scope

The parameter \(n\) is an integer at least six, and all graphs are finite, undirected, simple. For a graph \(G\), a simplex of \(\operatorname{Ind}_2(G)\) is a set of graph vertices for which every connected component of the induced graph has one or two vertices. As \(G\) is simple, this is equivalent to requiring maximum induced degree at most one.

Identify a simplex \(F\) with a family of two-element subsets (edges) of the ground set \(\{0,\ldots,n-1\}\). Thus \(F\) is admissible exactly when every chosen edge is disjoint from at most one other chosen edge. We include the empty face in the augmented face poset. No orientation, weights, coefficients, or connectivity assumption beyond those defined here is needed.

## Proof

**Step 1: a canonical partition.** Let \(H(F)=\{e\in F:0\notin e\}\). Split the augmented face poset into class \(A\), where all members of \(H(F)\) are pairwise intersecting, and class \(B\), where \(H(F)\) contains a disjoint pair. Every pairwise-intersecting collection of two-subsets is either a star (the edges have a common endpoint), a subset of a three-edge triangle, or empty. If a nonempty family has no common endpoint, it is exactly a triangle: from intersecting edges \(ab,ac\), an edge avoiding \(a\) must be \(bc\), and any edge intersecting all three is among \(ab,ac,bc\).

**Step 2: match class \(A\) completely.** Fix a fiber with prescribed \(H(F)=H\). If \(H\) has a common endpoint \(i\), choose \(i\); if it is a triangle, choose any of its three endpoints (canonically its least); if \(H\) is empty, choose \(i=1\). In each fiber toggle the edge \(0i\), pairing every face that omits it with its union with \(\{0i\}\). This toggle is always admissible. In a star, \(0i\) meets every edge of \(H\), as well as every other chosen \(0\)-edge, so creates no disjointness. In a triangle \(ab,ac,bc\), any admissible chosen \(0\)-edge must end at one of \(a,b,c\), otherwise it would be disjoint from all three edges of the triangle; toggling \(0a\) therefore adds exactly one disjointness partner, namely \(bc\), whose degree was zero. If \(H=\varnothing\), all chosen edges share \(0\). Hence every fiber of \(A\) is perfectly matched by a cone-edge toggle. Each fiber matching is acyclic, since every reversed matched incidence adds its single fixed pivot edge.

**Step 3: reduce class \(B\) to universal four-point blocks.** Suppose \(H(F)\) contains disjoint edges \(ab\) and \(cd\). Since these are already partners, any further selected edge must meet both. Such an edge has endpoints in \(U=\{a,b,c,d\}\); in particular no edge incident with \(0\) can occur. Every disjoint selected pair determines the same four-set \(U\), so \(B\) separates into incomparable subposets indexed by four-subsets \(U\) of \(\{1,\ldots,n-1\}\). For \(a<b<c<d\) in one block, the six available vertices are

\[
(ab,cd),\quad(ac,bd),\quad(ad,bc),
\]

written as three disjointness-opposite pairs. The block consists exactly of subsets containing both members of at least one displayed pair. It contains \(2^6-3^3=37\) faces; admissibility is automatic within the six vertices, because their disjointness graph is three independent edges.

**Step 4: a universal 37-face matching.** On each block make successive element matchings, first toggling \(ab\), then \(ac\), then \(ad\), always pairing both still-unmatched faces when both belong to the current pool. These stages contribute respectively \(14\), \(3\), and \(1\) pairs. Exactly one four-vertex face remains, namely \(\{ab,cd,bd,bc\}\); its simplicial dimension is three. The finite block is an upward-closed Boolean filter on six labeled elements. Its entire matched Hasse orientation is acyclic: all 37 vertices and all covering relations are checked by the standalone reproducibility program (function `verify_universal_block`). This is a universal finite lemma, not a finite approximation to the general case; every block for every \(n\) is canonically isomorphic to it. The local matchings are therefore acyclic.

**Step 5: global acyclicity and homotopy.** Define a target poset consisting of labels \(A_H\) for pairwise-intersecting families \(H\), ordered by inclusion, and incomparable labels \(B_U\) for four-subsets \(U\), each placed above every \(A_H\). Send a face in \(A\) to \(A_{H(F)}\), and a face in \(B\) to \(B_U\) as in Step 3. This map is order-preserving: inclusions within \(A\) enlarge \(H\), inclusions within \(B\) preserve \(U\), and inclusions from \(A\) into \(B\) increase the target label; inclusions from \(B\) into \(A\) are impossible. All described matchings stay within fibers. The patchwork theorem for acyclic poset matchings therefore proves that their union is acyclic on the entire face poset.

Class \(A\) has no critical cells, and each of the \(\binom{n-1}{4}\) blocks \(B_U\) has one critical cell of dimension three. In particular the empty face is paired in class \(A\). By the discrete-Morse CW reduction, this is equivalent to a CW complex with one basepoint and \(\binom{n-1}{4}\) three-cells and no cells of dimensions one or two. Every attaching map of a three-cell lands in the basepoint and is constant. Therefore the CW complex is the asserted wedge of three-spheres, proving the integral homotopy statement for every \(n\ge6\).

## Verification

The included standalone, dependency-free Python 3 program `verify_kneser.py` implements the exact finite six-bit block matching and verifies its full matched-Hasse acyclicity. The output is `universal_6_bit_block faces=37 matched_pairs=18 critical_3=1 acyclic=PASS`.

It also independently enumerates every admissible simplex, constructs the uniform fiberwise matching, and checks all covering incidences and directed acyclicity for \(5\le n\le12\). The verified face counts are respectively \(261,747,1751,3635,7006,12956,23574,43034\), including the empty face, and the critical three-cell counts are \(1,5,15,35,70,126,210,330\). The general theorem is proved by Steps 1–5 rather than inferred from these finite examples. To reproduce, run `python3 verify_kneser.py 5 6 7 8 9 10 11 12`.

## Relationship to prior work

Deshpande and Singh introduced and systematically studied higher independence complexes, proving explicit wedge classifications for complete multipartite, fully whiskered, path, cycle, and perfect-tree families. The pair-disjointness graphs here are not among those families. Braun's stable Kneser complex work and Feng–Wang's Kneser results concern the **ordinary** (first) independence complex, not the second independence complex treated here. A previously indexed Petersen case already gives \(\operatorname{Ind}_2(KG(5,2))\simeq S^3\); the present proof derives an all-parameter classification for \(n\ge6\), which does not follow from the isolated five-point calculation. Likewise an ordinary four-cut calculation on \(KG(6,2)\) is a different simplicial construction. Literature comparison did not identify a stronger result implying the displayed general theorem, but it cannot exclude unpublished or unindexed equivalent results.

## Limitations

No formula is claimed for \(r\)-independence when \(r>2\), for Kneser vertices corresponding to sets larger than pairs, or for equivariant homology representations. The proof uses the special intersection structure of two-element ground-set subsets; it is not asserted to extend to arbitrary Kneser parameters. Reproducibility checks on eight finite sizes do not constitute the infinite-family proof. Originality is supported by comparison with identified primary publications and indexed results, subject to possible inaccessible or unindexed equivalent literature. Independent external mathematical assessment has not been performed.

## References

1. Priyavrat Deshpande and Anurag Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, first version 2020-01-15. https://arxiv.org/abs/2001.05448
2. Benjamin Braun, *Independence Complexes of Stable Kneser Graphs*, arXiv:0912.0720, first version 2009-12-03. https://arxiv.org/abs/0912.0720
3. Ziqin Feng and Guanghui Wang, *Exploring Homological Properties of Independent Complexes of Kneser Graphs*, arXiv:2404.10566, first version 2024-04-16. https://arxiv.org/abs/2404.10566
