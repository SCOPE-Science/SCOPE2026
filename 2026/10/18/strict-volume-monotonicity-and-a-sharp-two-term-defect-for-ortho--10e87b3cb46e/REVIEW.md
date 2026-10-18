# Scientific review: perpendicular-hypercylinder volume defect

## Correctness

**PASS.** The proof's chamber dissection is exact outside the zero-measure set where absolute coordinates tie. On each chamber the strongest defining cylinder constraint omits its minimum-magnitude coordinate, reducing the volume to an integral of the minimum absolute coordinate over the unit ball. Polar integration, a Gaussian radial decomposition and a change of variables establish the normalized all-dimensional integral. A monotone coupling of beta-distributed random variables proves strict decrease, not just numerical decrease. Taylor expansion of the inverse error function, exact beta moments and an exponentially controlled tail give the complete two-term formula with \(O(n^{-6})\) error. The radial estimate follows from an exact formula valid in every unit direction. A standalone independent numerical-algebraic checker verifies low-dimensional benchmark volumes and series coefficients; it is not substituted for the proof.

## Originality

**PASS under the available evidence, with material priority risk.** Classical three-dimensional tricylinder volume and published four- and five-dimensional intersections were explicitly identified as prior work and are not claimed as new. Published OEIS entries A349579 and A349580 state the exact cases and identify 2012–2013 Illinois reports treating higher-dimensional intersections. The complete reports were not accessible for content comparison, so their coverage of the sharp all-dimension strict normalized-volume monotonicity and the two-term asymptotic remains unknown. A full mathematical result on the polar three-disk *hull* was read: it determines dimension-three hull geometry, not relative n-dimensional cylinder volumes. The other checked two-disk-hull article is likewise mathematically different. Public research-record similarity searches located related volume and orthogonal-disk results, but no result asserting the present combined dimension-to-dimension theorem. Failure to locate one is not proof of global novelty. The incomplete report access is a genuine historical-priority risk that requires independent follow-up.

## Mathematical value

**PASS.** The ratio of the intersection volume to the ambient unit-ball volume is a canonical affine-free Euclidean quantity for the family of all mutually orthogonal coordinate cylinders. Two questions are naturally left by earlier exact low-dimensional volumes: whether these normalized volumes form an ordered sequence, and how quickly they approach the unit-ball benchmark in large dimension. The theorem resolves both, rigorously and for all dimensions, with a sharp asymptotic constant and a higher-order correction. The separation between the order \(n^{-1}\) radial defect and the order \(n^{-2}\) volumetric defect gives additional quantitative geometric content. The result does not depend on a selective finite dimension or ad hoc invariant.

## Closest sources and residual risk

The strongest known-source comparisons are the two Illinois reports cited through OEIS A349579 and A349580, the exactly inspected three-disk convex-hull result, and Finch's two-disk article. The Illinois report texts remain unreadable. This prevents absolute claims of priority; it does not affect the analytic proof. The scope is fixed to congruent coordinate-axis cylinders and does not address arbitrary cylinder directions or radii.

Self-review: passed. Independent audit: not yet performed.
