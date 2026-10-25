# The five-point threshold for verbose Vietoris–Rips barcode rigidity on ultrametrics

## Finding

Among nonempty finite ultrametric spaces, the full verbose Vietoris–Rips barcode over a fixed coefficient field determines the isometry class whenever the cardinality is at most four. A published five-point ultrametric pair has identical verbose barcodes but is not isometric. Thus five is the smallest cardinality at which this invariant can fail to determine isometry.

## Assumptions and scope

An ultrametric is a metric satisfying \(d(x,z)\leq\max\{d(x,y),d(y,z)\}\) for all points. Use the inclusive Vietoris–Rips filtration \(\operatorname{VR}_{\leq r}(X)\), in which a finite subset is a simplex exactly when its diameter is at most \(r\). The verbose barcode means the collection of chain-level intervals, including zero-length intervals, in every degree of the filtered simplicial chain complex over one fixed field. The claim concerns nonempty finite ultrametric spaces and the full verbose barcode, not arbitrary finite metrics or the ordinary concise barcode.

## Proof

First, the verbose barcode determines the filtered-chain-isomorphism class of a filtered chain complex: the elementary decomposition theorem for filtered chain complexes identifies two such complexes up to filtered chain isomorphism exactly when their verbose barcodes agree in every degree. Therefore equality of verbose barcodes for two Vietoris–Rips filtered chain complexes implies equality of \(\dim C_1(\operatorname{VR}_{\leq r}(X))\) at every threshold \(r\). The degree-one chain group has one basis edge for each unordered pair \(\{x,y\}\) with \(d(x,y)\leq r\). Hence the verbose barcode determines the multiset of all pairwise distances.

It remains to show that the pairwise-distance multiset determines an ultrametric space with at most four points. The number of points is itself determined by the degree-zero chain group, so compare spaces of the same cardinality.

For at most three points, the claim follows directly: in a three-point ultrametric the largest distance occurs at least twice, so the sorted distance multiset fixes the unique possible metric up to relabeling. For four points, let \(q\) be the number of distinct positive distances. If \(q=1\), the space is equilateral. If \(q=2\), the blocks at the smaller distance form a partition of type \(3+1\), \(2+2\), or \(2+1+1\); the number of pairs at the smaller distance is respectively \(3\), \(2\), or \(1\), so the distance multiset fixes the partition and hence the isometry class. If \(q=3\), there are only two possible rooted merge patterns: two pairs merge at the first and second levels before the final merge, giving multiplicities \(1,1,4\) for the three distance values; or one pair forms first, a third point joins at the second level, and the last point joins at the third, giving multiplicities \(1,2,3\). These patterns are distinct, and each pattern with its ordered distance values determines the metric up to relabeling. Thus the pairwise-distance multiset, and consequently the verbose barcode, determines every ultrametric space of size at most four.

For sharpness, Mémoli and Zhou give the following two five-point ultrametrics in Example 14 of their paper. Their distance matrices are

\[
D_X=\begin{pmatrix}
0&1/2&2&2&2\\
1/2&0&2&2&2\\
2&2&0&1&1\\
2&2&1&0&1\\
2&2&1&1&0
\end{pmatrix},\qquad
D_Y=\begin{pmatrix}
0&1/2&1&2&2\\
1/2&0&1&2&2\\
1&1&0&2&2\\
2&2&2&0&1\\
2&2&2&1&0
\end{pmatrix}.
\]

The source proves that their Vietoris–Rips filtered chain complexes are filtered-chain-isomorphic but the metric spaces are not isometric. By the same paper's verbose-barcode characterization theorem, their full verbose barcodes agree. Non-isometry can also be seen from the incident-distance profiles: in \(X\), two points have profile \((1/2,2,2,2)\) and three have profile \((1,1,2,2)\); in \(Y\), two have profile \((1/2,1,2,2)\), one has profile \((1,1,2,2)\), and two have profile \((1,2,2,2)\). These multisets differ, which an isometry would preserve. The lower bound for cardinalities at most four and this five-point witness establish the claimed minimum.

## Verification

The small-cardinality classification is exhaustive by the number of distinct positive distance levels in a four-leaf ultrametric dendrogram. The edge-count argument uses the filtration of the degree-one chain group, not a finite numerical experiment. The five-point witness and its filtered-chain-isomorphism/non-isometry properties are stated in the cited primary source; the verbose-barcode conclusion follows from its Theorem 11. No claim is made about cardinalities above five or about general metric spaces.

## Relationship to prior work

Mémoli and Zhou introduced the verbose barcode as a chain-level refinement of ordinary persistent homology and proved that it classifies filtered chain complexes up to filtered chain isomorphism. Their Example 14 supplies a five-point ultrametric counterexample to isometry recovery. The result here adds the complementary lower bound: for every nonempty ultrametric space of cardinality at most four, verbose-barcode equality forces isometry. Their Example 12, where four-point spaces have equal concise barcodes but different verbose barcodes, is consistent with this statement and illustrates why the chain-level invariant is essential.

## Limitations

The conclusion is restricted to finite ultrametric spaces and the full verbose Vietoris–Rips barcode over a fixed coefficient field. It does not assert that concise barcodes determine ultrametrics, that verbose barcodes determine arbitrary finite metric spaces, or that the five-point witness is minimal outside the ultrametric class. Independent audit and independent validation have not been performed.

## References

1. F. Mémoli and L. Zhou, “Ephemeral Persistence Features and the Stability of Filtered Chain Complexes,” 39th International Symposium on Computational Geometry (SoCG 2023), LIPIcs 258, Article 51, published 2023-06-09, DOI: 10.4230/LIPIcs.SoCG.2023.51. First public preprint: arXiv:2208.11770, submitted 2022-08-24. See Definition 3.8, Theorem 11, and Example 14.
2. D. Usher and J. Zhang, “Persistent homology and Floer–Novikov theory,” for the elementary filtered-chain-complex decomposition used by Mémoli–Zhou; see the citation and theorem reproduced in Mémoli–Zhou, Theorem 11.
