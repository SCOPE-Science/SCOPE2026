# Scientific review: Exact VC dimensions of finite cyclic rectangles on two-dimensional tori

## Correctness — PASS

The claim is a complete classification for arbitrary positive cyclic side lengths, including coordinate ties. The trace-intersection lemma exactly expresses every rectangle trace. The cyclic-order compression and enlargement lemmas reduce all side-length cases to finitely many supports. Splitting ties into consecutive positions reduces all potential seven-point supports to 5,040 permutation order types; none is shattered. Translation allows the origin-fixed obstruction checks for seven small grids. All 77,294 negative supports were exhaustively enumerated; nine explicit matching witnesses were verified both by direct rectangle construction and the optimized trace-mask algorithm. The 1,119 independent small-support cross-checks agree. These are exhaustive finite proof components backed by reductions, not extrapolated experiments. The self-contained executable is essential to the computational portion.

## Originality — PASS under accessible evidence

Gillibert, Lachmann and Müllner (arXiv:2004.13861v1, 2020; Journal of Complexity 2022) already report VC dimension six for **continuous** two-dimensional torus boxes. The one-dimensional cyclic-interval boundaries and the classical nonperiodic rectangle dimension are not new. The assessed result instead determines exactly when a restricted finite cyclic grid attains each possible dimension, particularly the sharp first 5-by-6 realization. Searches across equivalent formulations (cyclic rectangles, products of circular arcs, discretized periodic boxes), stronger continuous results and accessible mathematical records did not reveal an implication or a matching finite table. Search non-detection does not establish global uniqueness; possible alternate terminology and secondary source coverage remain priority risks.

## Mathematical value — PASS

The all-parameter theorem gives the exact resolution requirement for maximal shattering of two-dimensional periodic rectangles, filling a natural gap left by the known continuum value. Its 5-by-5 versus 5-by-6 distinction and the complete behavior of thin grids are structural finite-discretization phenomena. The universal classification and proof are useful independently of any unfinished census of all shattered supports.

## Closest literature and limitations

The closest primary source is Gillibert, Lachmann and Müllner, *The VC-Dimension of Axis-Parallel Boxes on the Torus*, arXiv:2004.13861v1 (28 April 2020), doi:10.1016/j.jco.2021.101600. It establishes asymptotic continuous-torus results and reports the known dimension-six planar case, which is credited. The classification here concerns only unrestricted cyclic intervals on finite coordinate cycles; it does not give online dimensions, fixed-width boxes, or shattering-support polynomials. The finite negative cases are computer-assisted but exhaustively reduced and reproducible. Historical priority under alternate circular-arc terminology remains uncertain.

Self-review: passed. Independent audit: not yet performed.
