# Review — Residual-volume uniqueness and multiplicity continuity for generic isoperimetry

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The argument uses two inputs from Niu, arXiv:2609.20790: the generic uniqueness statements and Proposition A.1 on compactness and continuity of isoperimetric regions under simultaneous metric and volume convergence.

For the upper semicontinuity of the multiplicity diameter, take a convergent parameter sequence and choose two minimizers realizing the diameter in each compact fiber. Proposition A.1 gives a common subsequence converging to two minimizers in the limiting fiber. Smooth convergence of the metrics and L1 convergence of the characteristic functions imply convergence of normalized symmetric-difference distances. The limsup of the diameters is therefore bounded by the limiting-fiber diameter. This checks the direction of semicontinuity.

The elementary estimate
\[
d_g(E,F)\le 2s
\]
for two sets of normalized volume \(s\), together with the same estimate for complements, gives
\(\Delta_g(s)\le2\min\{s,1-s\}\). Complementation is an isometric bijection between the \(s\) and \(1-s\) minimizer fibers.

A compact fiber has diameter zero exactly when it is a singleton, so uniqueness is the zero locus of a nonnegative upper-semicontinuous function. Hence the uniqueness set is \(G_\delta\) for every fixed metric. Niu's simultaneous rational-fraction corollary gives a generic set of metrics for which all rational non-half fractions are zeros, making the zero locus dense. At half volume Niu's theorem gives exactly \(E\) and \(E^c\); their normalized symmetric difference is one.

For such a generic metric, every zero is a continuity point of the nonnegative upper-semicontinuous profile. Every positive point is a discontinuity because rational zeros approach it. Thus the uniqueness set equals the exact continuity set. Positive superlevels are closed by upper semicontinuity and nowhere dense because the zero set is dense. Their localization follows from the elementary upper bound.

For strict-BV continuity, let volumes approach a unique target and choose arbitrary minimizers. Proposition A.1 makes every subsequence admit a strictly-BV convergent subsubsequence whose limit is a minimizer at the target volume. Uniqueness forces every such limit to be the same region, which promotes subsequential compactness to convergence of the full sequence and, by contradiction, to uniform collapse over the entire minimizer fiber. The half-volume modulo-complement statement is identical with a two-point limiting fiber.

For the pair-space statement, \((g,s)\mapsto(g,s\operatorname{Vol}_g(M))\) is a homeomorphism onto Niu's metric-volume parameter space. His pair theorem supplies density of the zero locus, while the same compactness argument gives upper semicontinuity. Therefore a positive value cannot be a continuity point and every zero is one.

No boundary smoothness, nondegeneracy, or dimension-dependent regularity is used.

## Originality

The full text of Niu's September 2026 preprint was inspected at the main theorems, the simultaneous rational-fraction corollary, the metric-volume pair theorem, and Proposition A.1. The paper explicitly states simultaneous uniqueness at rational fractions and says that it does not assert that the same generic set works for all real fractions. Searches within the paper found no occurrence of “residual”, “comeager”, “multiplicity diameter”, “Hausdorff”, or “upper semicontinuity” in the present sense.

The closest prior work found on uniqueness for many volumes is Antonelli--Pozzetta--Semola (CPAM 2025), which proves uniqueness on a density-one set of sufficiently large volumes for a fixed special class of noncompact manifolds with nonnegative Ricci curvature, Euclidean volume growth, and curvature decay. That is a different geometric regime and does not imply the generic closed-manifold Baire-category statement or the multiplicity-profile structure here.

Targeted literature searches using generic Riemannian metrics together with residual/comeager volume sets, upper-semicontinuous isoperimetric multiplicity, and continuous minimizer selections did not locate the theorem stated here. The current SCOPE archive was also searched by isoperimetric-region, generic-uniqueness, residual-volume, and multiplicity terminology, with no overlap found.

The principal originality risk is conceptual rather than access-related: the residual-volume part is a short consequence of ingredients that are already present in the very recent Niu preprint, so it may have been independently noticed or may appear in a subsequent revision even though it is not stated in the inspected version. Originality is therefore only to the best of our knowledge.

No inaccessible paper was identified that closely matches the generic closed-manifold statement. The most relevant recent sources above were accessible at the theorem/argument level.

## Value

The result upgrades simultaneous generic uniqueness from a countable dense set of prescribed fractions to a dense \(G_\delta\), hence comeagre and uncountable, set for one generic metric. It also gives a natural quantitative organization of all possible failures: the diameter of the minimizer fiber is upper semicontinuous, positive superlevels are closed nowhere dense, and nonuniqueness is exactly the discontinuity set of this profile.

The strict-BV collapse turns pointwise uniqueness into a coherent selection theorem. For a generic metric, the unique isoperimetric regions form a continuous strict-BV “spine” over the comeagre uniqueness set. At half volume the unavoidable complement symmetry is isolated precisely and continuity is recovered after passing to the complement class.

These statements remain valid in dimensions where isoperimetric boundaries may be singular, because only variational compactness is used.

## Limitations

The theorem does not prove uniqueness at every real volume fraction. The exceptional set may still be uncountable, and no measure, Hausdorff-dimension, porosity, or cardinality bound is proved for it.

The main residual-volume statement is structurally elementary once Niu's new generic uniqueness and compactness results are available; it should not be interpreted as a new perturbative proof or as strengthening the local regularity of minimizers.

The strict-BV continuity is a consequence of compactness plus uniqueness and gives no differentiability of the minimizer with respect to volume. No nesting, foliation, smooth dependence, or curvature estimate is asserted.

Because the primary source is extremely recent, an unindexed note or a later revision may state the same Baire-category consequence. Independent audit has not been performed.
