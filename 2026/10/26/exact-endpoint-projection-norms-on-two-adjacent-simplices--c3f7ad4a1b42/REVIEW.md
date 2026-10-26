# Scientific review of the two-simplex endpoint norm

## Correctness
**PASS.** The finite-element reproducing rows satisfy the defining Gram identities for every shared and exclusive node. Absolute row integrals reduce to a beta marginal with a single zero, and a closed integral identity gives the exact norm profile. Barycentric convexity reduces the global operator norm to nodes; the derivative of the profile is strictly negative for every positive ratio. Exact-rational independent matrix and integral checks confirm 432 nodal cases, but the analytic argument rather than these finite checks proves the universal claims. The result does not prove that all maximizing evaluation points are vertices.

## Originality
**PASS on the sources examined, with residual bibliographic uncertainty.** The closest full-text source, Karkulik–Pavlicek–Praetorius (2012 preprint), treats mesh-refinement and \(H^1\) stability, not the sharp \(L^\infty\) norm. Crouzeix–Thomée (1987) concerns general stability bounds, not an identified equal-area minimizer or two-simplex exact profile; full-text access was unavailable for this older paper. The published single-simplex affine-projection calculation gives only the shared-vertex row and does not imply the larger exclusive-tip rows. Searches of related terms and published mathematical records did not identify the formula \(N_d(r)\). An unindexed earlier exact computation remains possible.

## Mathematical value
**PASS.** Two simplices sharing a facet are the smallest conforming mesh in dimension at least two whose continuous nodal projector genuinely couples different element volumes. The formula quantifies how grading changes worst-case \(L^\infty\) amplification, proves that equal volumes are uniquely optimal at the level of the volume ratio, isolates a sharp nonattained degeneration boundary, and holds in all spatial dimensions without geometric shape restrictions. Its planar envelope \(7/2\) and balanced value \(49/18\) are exact stability benchmarks.

Self-review: passed. Independent audit: not yet performed.
