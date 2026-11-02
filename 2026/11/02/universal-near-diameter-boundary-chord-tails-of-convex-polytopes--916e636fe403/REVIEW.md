# Scientific assessment

## Correctness — PASS

The claim is an asymptotic for **two independently chosen surface-area-uniform boundary points** of any fixed convex polytope in every fixed dimension \(d\ge3\). Strict convexity of squared distance localizes diametral pairs to finitely many vertex pairs. At a diameter endpoint the axial projection is strictly positive on all tangent rays, so each incident facet contributes a finite positive exactly homogeneous one-point cap measure. Beta integration of independent caps produces the factorial coefficient. Taylor expansion of Euclidean length, with uniform positive axial transversality, supplies the \(O_P(\varepsilon^{2d-1})\) error. Disjoint neighborhoods allow summation over **ordered** diametral pairs. The simplex and cube coefficients follow from explicit incident-facet integrals. All hypotheses, area normalizations, endpoint orientations, and nonuniformity of the constants have been checked. The independent exact and simulation diagnostics in `verify.py` passed. No finite computation is used as proof for arbitrary polytopes.

## Originality — PASS under accessible evidence, historical priority provisional

Full texts of Mayer--Molchanov (2006, arXiv:math/0605289), Lao (2010, Chapter 5), and Brunel (2015, arXiv:1503.01504) were examined in relevant sections. Mayer--Molchanov posit or derive two-point tails for balls and spherical models; Lao computes polygon-edge max-distance laws; Brunel studies random-hull Hausdorff errors and diameter estimation. None of the examined statements yields the exact surface-area-pair cone coefficient for arbitrary \(d\ge3\) convex polytopes. Semantic searches of published research results found related studies of near-zero polygon boundary pairs, interior-uniform samples, and motion-invariant random-line chords, all with materially different measurement distributions. The possible existence of a differently named older tangent-cone formula remains a residual priority risk; neither absence of a search result nor partition ownership proves novelty.

## Value — PASS

The general theorem identifies a universal, sharp near-diameter exponent and a computable, nonzero coefficient depending on **all** diametral vertex neighborhoods, including polytopes with many diametral pairs and nonsimplicial facets. It gives exact all-dimensional benchmark constants for regular simplices and cubes and supplies a needed input to extreme-distance modeling, without claiming a sample-maximum limit law. This structural result is not simply evaluation of a fixed polytope integral or a parameter rescaling.

## Limitations

Historical priority remains provisional, and independent replication or review is outstanding. The result assumes convex polytopes, surface-Hausdorff sampling, fixed dimension, fixed shape, and straight Euclidean chords. Estimates are local to the diameter and do not describe finite-sample maximum statistics.

Self-review: passed. Independent audit: not yet performed.
