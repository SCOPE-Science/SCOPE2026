# Scientific review: strictly positive orthotope central sections

## Correctness — PASS

For almost every normal the central section vertex/edge correspondence holds, so each edge crossing is counted once. Gaussian radial parametrization produces independent normal numerator and denominator for each fixed edge, giving the displayed Cauchy/arcsine crossing probability. The derivative comparison is strict because every pair of normalized squared positive widths sums to less than one in dimensions at least three. A finite chain of equalizing transfers proves Schur monotonicity; merging coordinates proves the sharp infimum, and the Hessian at the diagonal is computed explicitly. Boundary cases include all positive widths, a lower infimum only as widths vanish, and the dimension-two exception. No finite simulation is mistaken for a proof. `verify.py` returned `VERIFY_OK` for the reported geometric counts and checks.

## Originality — PASS, with explicit historical limitations

The primary 2008 source by Marichal and Mossinghoff gives hypercube sectional *volumes*, not the expected vertex count or an orthotope majorization theorem. The 2009 Ball–Prodromou theorem establishes isotropic measures on fixed cube sections, not random direction counts. The closest title, Swan's *Expected Number of Vertices of a Hypercube Slice*, calculates a constant \(2^k\) under uniform **translations** conditional on meeting the cube, whereas every hyperplane here goes through the origin. In dimension four those values are respectively eight and \(32/3\); the statements do not imply each other. A public 2015 question identifies the central model but contains no closed formula or shape-rigidity assertion. Cover–Efron studies random cones, not this anchored box. Previously treated three-dimensional dual shadow probabilities are credited as overlapping lower-dimensional special cases rather than advertised as new results.

The complete text of the most plausible papers and the public discussion were inspected; semantic mathematical-record searches across central section, random cube edge intersection, Gaussian/Cauchy angular, and Schur-concavity aliases found no covering claim. Such searches cannot rule out unindexed or privately derived identities. Independently assessed priority remains unknown.

## Value — PASS

This is a motivated exact statistic of how complicated high-dimensional cube sections look under random orientations. It gives an all-dimensions formula, an anisotropic ordering theorem, a sharp optimizer and infimum, a dimension-four rational landmark and local quantitative stability. Strict Schur-concavity is not a routine application of coordinatewise concavity: the scalar function changes curvature at one half, and the simplex constraint is essential. Uniform translation leads instead to a constant first moment, making the result a substantive distinction between standard geometric sampling models.

## Reproducibility and limits

`python3 verify.py` is standalone and replays six directly edge-enumerated random-section diagnostics (9,000 Gaussian normals per case), 72,000 numerical transfers, and three local expansion checks. The exact proof does not depend on random test coverage. Only positive orthotopes, fixed-center hyperplane sections, and expected vertex count are proved; no noncentral law, higher moment or arbitrary parallelotope theorem is asserted. Published analogues and historical risks are documented in `AUDIT.json` and the references. No independent audit has been performed.

Same-model review: passed. Independent audit: not yet performed.
