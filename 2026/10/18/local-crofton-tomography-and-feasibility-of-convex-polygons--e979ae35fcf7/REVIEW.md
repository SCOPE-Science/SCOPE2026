# Self-review

## Correctness — PASS

The Crofton normalization follows by integrating projected widths; the probability of hitting a side is twice its length divided by the perimeter. For adjacent sides forming two sides of a triangle, their line-hit union equals the triangle-hit event, giving the exact joint-measure formula by inclusion–exclusion. The two-step vertex distance and every interior angle therefore follow from observed probabilities without unidentified geometric parameters. Sequential turning reconstructs all labeled vertices up to similarity and reflection. For the feasibility converse, strictly increasing positive edge directions with one total turn and closure imply that every edge is a supporting line, hence strict convexity. The inverse is smooth on compact nondegenerate domains. The bundled standard-library checker passed 1,162 comparisons, including independently integrated line-hit events; finite checks are corroborative only.

## Originality — PASS relative to inspected sources

Harutyunyan–Ohanyan (2009), DOI 10.1239/aap/1246886615, develops edge-pair integrals and an overall chord-length law for regular polygons, but the inspected sections do not give reconstruction of all labeled strictly convex polygons from just one-edge marginals and *adjacent* pair incidences, nor the exact closure-based feasibility criterion. Bäsel (2012), arXiv:1204.2707, derives chord-length and point-distance distributions for regular polygons, using different observables. Gates (1982) identifies triangles and quadrilaterals from unmarked chord-length information; Nagel (1993) and older X-ray probing research use orientation-dependent or more informative measurements. These richer or different reconstruction inputs do not imply the sufficiency of this sparse local statistic. Published semantic searches and comparisons against accessible prior research claims identified no covering assertion. The Crofton formula and cosine law are classical and excluded from the novelty claim. Historical-priority risk remains in older combinatorial-integral-geometry sources and inaccessible full texts of selected related papers.

## Mathematical value — PASS

This is a complete inverse classification for a natural stochastic-geometric observable on *every* strictly convex polygon, not a one-shape computation: it supplies a finite explicit inverse, necessary-and-sufficient realizability equations, local robustness, and an equilateral data-reduction corollary. Recovering the entire geometry from observations involving only one side or a neighboring side pair is a meaningful shape-tomography statement despite its elementary proof. Applications requiring unordered side labels, finite-sample statistical accuracy, or degenerating polygons are explicitly outside the theorem.

Self-review: passed. Independent audit: not yet performed.
