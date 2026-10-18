# Scientific review: sharp tetrahedral central-section diameter tails

## Correctness

**PASS.** For the stated coordinate normalization, the proof derives both exact quadrilateral diagonal lengths from edge intersections, handles the one-versus-three sign chamber using a harmonic-mean constraint, and proves that the only minimum normals are coordinate axes. The tetrahedron's six edge planes are the only maxima. Independent local spherical charts give uniform expansions of the *actual section diameter* (not just a convenient chord): quadratic, square-shaped deficit at minimizing normals and piecewise-linear, rectangular deficit at maximizing normals. The latter proof explicitly compares the additional crossing vertex in quadrilateral sections. The two surface-area Jacobians and counts of oriented normals yield \(6/\pi\) and \(3/(\pi\sqrt2)\). Reconstructable checks from `verify.py` pass exact rational identities, endpoint bounds, a near-max pairwise distance comparison, and numerical spherical-area convergence. The finite checks are supplementary; the continuum limits follow from the expansion and compactness arguments.

## Originality

**PASS, with residual bibliographic risk.** Query comparisons in the public published-finding corpus mathematics archive located *Exact Haar diameter law for central sections of the regular octahedron* and *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections*, whose inspected proof statements address centrally symmetric \(\ell_1\) bodies, not the noncentrally symmetric tetrahedron. Another relevant tetrahedral result, *Exactly seven centroidal hyperplane sections of every tetrahedron*, concerns centroid coincidence, not diameter statistics. Separate work on tetrahedral silhouette area moments concerns *projections*, whereas the present random variable is a section diameter. The recent manuscript by Guédon, Litvak, Tatarko and Vritsiou (arXiv:2609.24131; public 2026-09-21) motivates random-section diameters, but accessible material described general bounds and \(p\)-ellipsoids, not these exact tetrahedral constants; its full text could not be read, so lack of coverage is not certified. General simplex-section volume sources measure a distinct functional. These comparisons address implication, not only terminology: existing \(\ell_1\)-body identities depend on central symmetry and cannot be transferred by simply changing a parameter. A prior equivalent special-case calculation in unindexed geometric probability remains possible.

## Mathematical value

**PASS.** The random diameter of a central section is a natural shape statistic for an extremal noncentrally symmetric Platonic solid, recently motivated by general random-section diameter estimates. Both distribution endpoints, their equality configurations, sharp tail powers and normalization constants, and conditional rare-direction limit regions are determined within one theorem. The different exponents detect the underlying quadratic versus polyhedral-linear local geometry, a useful benchmark for studying nonsmooth random-section observables. This is not a relabeling of a known tail, a generic textbook moment calculation, or an arbitrary finite parameter slice. No all-dimensional or full-CDF claim is made.

## Closest literature and scope limits

- Guédon, Litvak, Tatarko, Vritsiou, arXiv:2609.24131: abstract inspected; full text unavailable (access risk remains).
- *Exact Haar diameter law for central sections of the regular octahedron*: relevant published statement, proof and related-work comparison inspected; different polytope and symmetry.
- *Exact diameter law and exponential endpoint fluctuations for random cross-polytope hyperplane sections*: published statement and proof inspected; high-dimensional centrally symmetric \(\ell_1\) setting.
- *Exactly seven centroidal hyperplane sections of every tetrahedron*: published statement and proof beginning inspected; different section observable.
- H. Dirksen (2017), volume of regular-simplex sections: abstract inspected; no diameter-tail implication.

The stated constants use the tetrahedron with edge length \(2\sqrt2\). The plane passes through its centroid, and the orientation is Haar-uniform. The approach does not classify all intermediate values of the diameter distribution. Independent evaluation and full-text priority checking remain outstanding.

Self-review: passed. Independent audit: not yet performed.
