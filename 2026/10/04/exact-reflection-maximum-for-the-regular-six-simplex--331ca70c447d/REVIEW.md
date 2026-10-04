# Review

## Correctness

PASS. The proof covers every supporting hyperplane because every exposed face of a simplex contains a vertex, after which the support can be written as \(u^\perp\) at that vertex. The regular-simplex Gram matrix gives the exact unit-normal constraint. The reflected-hull volume is derived by integrating the affine height over projections of all upper facets, producing an exact piecewise-rational objective. Each chamber is reduced rigorously by two sum-of-squares equalization steps, and the remaining one-variable derivatives are checked exactly. The unique global chamber maximum is
\[
6+\frac{2\sqrt{511}}7.
\]
No finite experiment is used to establish the theorem.

## Originality

PASS. The directly relevant 2019 correction states that the formerly claimed all-dimensional value \(2n\) is valid only through dimension four, solves dimension five, and explicitly poses the higher-dimensional problem. The earlier 2013/2014 theorem claiming \(2n\) in all dimensions is therefore not covering and is superseded on this question by the correction. Searches for the six-dimensional formulation, the exact radical \(\sqrt{511}\), the decimal value, supporting-hyperplane/reflection aliases, and later references to arXiv:1811.12399 found no statement implying the six-dimensional exact value or its equality classification. Residual risk remains for unindexed or differently worded literature.

## Value

PASS. The finding resolves the first dimension left open by the corrected primary paper, gives an exact extremal constant rather than a numerical estimate, and classifies all equality supports. The reduction also identifies a reusable structural mechanism: within every six-dimensional upper-facet chamber, an optimizer equalizes both the small and large normal-pairing groups.

## Closest literature and limitations

The closest source is Á. G. Horváth, *An extremal problem of regular simplices: the five-dimensional case*, Journal of Geometry 110, 17 (2019), DOI 10.1007/s00022-019-0472-4, earliest public version arXiv:1811.12399 (2018-11-29). Its Problem 1 leaves dimensions beyond five open. The earlier paper *On an extremal problem connected with simplices* (2014; arXiv:1303.3454) contains the now-corrected all-dimensional \(2n\) claim. The new theorem is limited to dimension six and does not solve dimensions \(n\ge7\).

Same-model review: passed. Independent audit: not yet performed.
