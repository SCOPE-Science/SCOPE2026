# Review of the exact fixed-orientation hexagon covering law

## Correctness — PASS

The convex-analytic reduction is exact: the hexagonal gauge is the maximum of its six facet linear forms. The triangle-cover lemma is a complete continuous-coverage certificate because a common point of three centered covering translates, with each of the triangle's three vertices covered, produces six convex triangles tiling the fundamental half-square. Both explicitly constructed witness points lie in the same half-square and have equal gauge distance to its three triangle vertices. The remaining square corner is excluded by one facet functional, and all other integer points are excluded by the Euclidean unit-disk containment of the hexagon. These lower and upper bounds coincide for every orientation, including the branch transition and endpoints. The global equality classes follow from exact monotonicity of two trigonometric branches. The self-contained analytic proof, not finite testing, establishes the theorem.

The independent diagnostic source `verify.py` was executed with Python's standard library and returned `PASS: 119356 deterministic covering-profile diagnostics`; it reproduces lattice witness distances, pointwise square coverage, angle constants and monotonicity checks. It is supporting evidence only.

## Originality — PASS, with residual priority risk

Fei Xue's 2019 full paper (Theorem 4, proof of hexagon case) and the published general regular-polygon extension both solve the much coarser problem of the smallest dilation covering **uniformly over all orientations**. The latter's hexagon value equals the **maximum** of the present exact function. Neither supplies its fixed-orientation minimum, its two distinct active mechanisms, or the nonsymmetric optimizing angle; knowing a maximum cannot entail this function or its minimum. The 2026 full paper of Codenotti–Freyer–Krivokuća establishes general covering and Minkowski-sum inequalities, not the particular sharp angular profile. Targeted searches for the branch constant, algebraic minimum, square-lattice norm equivalence and rotation classification did not identify an equivalent statement. This is best-knowledge originality, not a claim of exhaustive historical priority. An older treatment under hexagonal norm covering or Voronoi critical vertices may exist.

## Mathematical value — PASS

For a natural rigid body/lattice pair, optimization over orientation is a distinct geometric invariant from orientation-robust covering. The exact continuous profile reveals two competing critical-hole configurations, a genuine branch-switch cusp, and a uniquely determined symmetry-breaking optimum (two orientations per period), not an arbitrary extra decimal or an unmotivated finite slice. The closed form can serve as a benchmark for anisotropic lattice covering optimization and exact critical-hole computations.

## Closest literature and limitations

F. Xue (2019), *On the Lattice Point Covering Problem in Dimension 2*, DOI 10.37236/8245; *Exact lattice-point covering radii for all regular polygons with two modulo four sides* (2026-10-04); G. Codenotti, A. Freyer and K. Krivokuća (2026), arXiv:2606.14442. The result pertains only to rotations of Euclidean regular hexagons against \(\mathbb Z^2\), not optimal lattice selection or nonregular polygons. Exact first publication under a different phrasing remains uncertain; independent validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
