# Scientific review: sharp long-polygon contractibility rates on flat two-tori

## Correctness

**PASS.** The almost-sure uniqueness of shortest geodesics allows the first \(n-1\) successive displacements of independent Haar-uniform vertices to be represented as independent uniforms in the centered lattice Voronoi cell. Closure selects the unique lattice label, giving an exact convolution law. Characteristic-function inversion and a two-dimensional Gaussian rescaling give \(p_n=A/(2\pi n\sqrt{\det\Sigma})+O_T(n^{-2})\) at each fixed lattice. Exact shoelace integration of a reduced Voronoi polygon yields the covariance matrix and its normalized determinant; elementary monotonicity supplies both sharp equality classifications. The independent CHECK.py reproduces the symbolic identities and tests geometric endpoint cases. The tests are corroboration, not an infinite proof.

## Originality

**PASS, provisional historical priority.** Glorieux–Yarmola (arXiv:2003.08190, first version March 18, 2020) proves the three-vertex probability and its rectangular/hexagonal optimizers, and derives a three-cell overlap functional. The new object is the full lattice-valued winding distribution for arbitrary vertex count, with a shape-sharp *large-count* probability coefficient from a new exact normalized covariance determinant. Kurlin (arXiv:2201.05150) classifies planar lattice and Voronoi geometry but does not study random minimizing-geodesic polygons or their return probabilities. Targeted searches for longer random geodesic polygons, winding asymptotics, sampled convolution formulas, and the covariance determinant did not expose a dominating statement. Earlier nonindexed results or combinations of classical Fourier methods with geometric moment identities remain possible; the absence of a search hit alone is not asserted as proof of priority.

## Mathematical value

**PASS.** A previous exact three-vertex shape-extremum question motivates the natural many-vertex analogue. The result supplies a full homotopy-class distribution, a precise \(n^{-1}\) return law, and a sharp classification over every Euclidean flat two-torus, including all rectangular shapes and the unique equilateral maximizer. The crucial nontrivial input is the global determinant-of-Voronoi-covariance inequality rather than merely substituting into a Gaussian approximation. This is a structural asymptotic classification, not a single arbitrary parameter value.

## Closest literature and limitations

Primary comparisons: O. Glorieux and A. Yarmola, *Random triangles on flat tori* (arXiv:2003.08190), and V. Kurlin, *Mathematics of 2-Dimensional Lattices* (arXiv:2201.05150). The geometric Voronoi description, characteristic-function argument, and Irwin–Hall density are classical inputs. The new sharp claim concerns only the asymptotic rate, not a finite-sample shape ordering. Error constants may depend on the fixed lattice; curved tori and nonuniform sampling are excluded. Historical priority and all independent validation remain unverified.

Self-review: passed. Independent audit: not yet performed.
