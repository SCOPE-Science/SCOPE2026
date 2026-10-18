# Scientific review: exact shortest-arm law for metric-star spline projection

## Correctness — PASS
The nodal Gram matrix follows by integrating the central and leaf hat functions on each arm. Direct Schur complementation gives the displayed inverse, from which the reproducing kernel, exactly integrated absolute row sums, and shortest-arm monotonicity follow. Convexity and strict sign disagreement exclude interior maximizers. The fixed-total-length range follows from the constraint on the shortest length and a continuous degenerating length family. The positive-cone assertion uses exact reproduction of constants. An independent exact-rational matrix and integration checker evaluates 1,982 cases. These finite checks are only support for, not substitutes for, the proof.

## Originality — PASS within the inspected evidence
The full 2006 Oswald source proves a negative uniform-bound statement for Euclidean multivariate triangulations and discusses a uniform interval bound; neither implies an exact metric-star law. The 2013 Passenbrunner–Shadrin paper establishes interval spline projector convergence and inverse-Gram decay. The full inspected published affine-simplex result calculates a local projector without cross-cell continuity, in contrast to the coupled star projector. Multiple published-result searches using the exact expression, star-network aliases, mass-matrix terminology and shortest-arm parameters returned no claim that dominates this formula. This is a reasoned comparison under incomplete historical coverage, not proof of global first discovery.

A plausible related source, Oswald's 2013 *L-infinity Bounds for the L2-Projection onto Linear Spline Spaces*, was available bibliographically but the complete chapter was inaccessible: an attempted authorized full-text route did not provide the chapter. Its abstract emphasizes one-dimensional and planar triangulation results, rather than metric-star graphs; an earlier equivalent graph-spline identity remains possible. The earliest verifiable public-source posting used here is Oswald's 2006-11-19 preprint, with primary mathematical classification 41A15.

## Value — PASS
This is an exact stability constant for a natural globally continuous least-squares finite-element projector on the smallest branched network, not an arbitrary finite table. It classifies all positive arm-length configurations at fixed valence and total length, pinpoints extremizing nodes and forcing signs, and exposes a degree-\(3\)/equal-length threshold at norm \(2\). The universal nonattained ceiling is \(7/3\) despite arbitrary length contrast, while all degrees at least four necessarily have amplification above \(2\). It is a precisely motivated sharp interpolation-stability invariant that cannot be inferred from a uniform 1D bound or the instability examples in multivariate triangulations.

## Scope and residual risks
Only one affine element per arm and unweighted arc length are covered. Further knot subdivision, general metric trees, mass lumping and weighted measures are unproved. Historical priority remains conditional on the accessible literature; in particular, the inaccessible 2013 chapter or older graph-spline vocabulary may contain an equivalent expression. Independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.
