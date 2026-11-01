# Scientific review

## Correctness — PASS

The distance identity for the Johnson graph is verified directly in the proof and independently by exhaustive vertex-orbit pairs for small parameters. Every fixed point has barycentric weights constant on orbits, so the orbit-barycenter triangulation is exact. The conflict graph has bipartite band edges determined by the integer inequality on orbit indices. The two alternating neighborhood folds are checked using open neighborhoods and leave one isolated graph edge per block of indices; these collapses yield a single cross-polytope boundary. The proof handles \(k=1\), \(r=0\), even and odd \(r\), and the full-simplex threshold \(r=k\). The standalone verifier passed 83 orbit-index comparisons, 198,880 valid fold deletions, and 78 finite homology calculations. These tests cannot prove the infinite statement, which instead follows from the explicit all-parameter folds.

## Originality — PASS, with residual risk

The closest published Johnson-graph Rips result gives the ordinary scale-one homotopy type, not geometric fixed spaces at all radii. The complete Johnson metric-dimension paper gives the exact distance, not Rips fixed loci. The inspected hypercube Rips paper concerns cohomology of a different vertex set, and the inspected Johnson clique reference concerns a different scale-specific question. The full text of the recent equivariant hypercube preprint was not accessible in this execution; its abstract states representation-theoretic rather than Johnson-slice fixed-point results. Named searches for Young-subgroup Johnson Rips fixed points, orbit distances, band independence complexes, and alternate formulations did not identify stronger covering statements. Unindexed or differently named equivalent work remains possible.

## Value — PASS

This identifies the actual geometric fixed-point homotopy type at **every scale** for a natural infinite family of constant-weight hypercube slices, with arbitrarily high-dimensional sphere fixed spaces and a sharp contractible transition at the Johnson diameter. The exact orbit-complex construction and elementary collapses give a reproducible model that cannot be recovered solely from ordinary ambient homology. The all-scale classification is stronger than a handful of numerical checks or a mere reformulation of the Johnson distance metric, though persistence inclusion maps and other subgroups remain open.

## Scientific limitations

The result is a self-review, not independent certification. The originality evidence depends on accessible indexed literature and examined primary material; a covering unindexed theorem cannot be excluded. The theorem does not compute maps between consecutive Rips fixed-space homology groups.

Self-review: passed. Independent audit: not yet performed.
