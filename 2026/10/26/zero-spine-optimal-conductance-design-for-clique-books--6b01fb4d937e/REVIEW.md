# Scientific review: zero-spine conductance optimum for clique books

## Correctness (C): PASS

The object is the simple graph \(K_2\vee(mK_s)\), \(m,s\ge2\), and the target is the all-pairs Kirchhoff index under an exact positive total conductance budget. Strict convexity of the inverse trace and edge-Laplacian injectivity give a unique global optimizer and justify three edge-orbit classes without an assumption of symmetric competitors. The exact Laplacian spectrum yields a strictly convex three-variable transformed problem. Its analytic KKT solution has an active spine-zero constraint and an inactive petal-internal-edge-zero constraint for every stated integer pair. Crucially, the inequalities \(2<y_*/a_*<ms\) are proved for every integer in range and imply both positivity of all other edges and strict positivity of the active KKT multiplier. The matrix-reconstruction and exact-symbolic tests give secondary evidence, not substitutes for the proof.

## Originality (O): PASS, with residual risk

Primary comparison: Ghosh–Boyd–Saberi (DOI:10.1137/050645452) treats convex total-resistance design, including trees, wheels and barbell bridges; its exact barbell geometry differs, and its bridge is not optional under connectivity. Johnson–Chertkov (arXiv:1004.2285) studies power-grid conductances and separately encourages edge sparsity via a nonconvex cost; it does not give the stated zero-spine classification under the unpenalized linear budget. Ellens et al. (DOI:10.1016/j.laa.2011.02.024) optimize graph topologies with order/diameter or edge-addition constraints rather than an individual conductance budget. The closest recoverable comparison claims involving a single-hub clique windmill Kirchhoff-index optimization and a two-hub spectral-gap book optimization do not imply the theorem because the first has no spine and the second optimizes a different spectral functional. Targeted indexed searches for all-pairs effective resistance, the exact graph join, common-spine deletion, and conductance budgets found no equivalent claim. This is a scoped comparison, not an exhaustive global novelty certificate; a specialized source using different graph terminology remains a risk.

## Mathematical value (V): PASS

A dense edge can be present in the candidate topology, strictly lower the electrical resistance when added at fixed other weights, and nonetheless receive **exactly zero optimal budget** under all-pairs resistance minimization. The theorem identifies an infinite natural class where this nonobvious support effect is universal, specifies every optimal individual conductance and the exact value, and rules out asymmetric competitors. It is motivated by practical network allocation and by the theoretical question of which available links are worth funding under a linear budget. The result is not an isolated table entry or a mere reformulation of generic convexity.

## Limitations and relationship to literature

Unit per-conductance costs, equal nontrivial petal cliques and two hubs are essential assumptions of the proved statement. Literature access covered selected full source texts and indexed records; it does not exclude prior specialized coverage. Reproducible finite matrix and symbolic tests are included; independent human verification has not occurred.

Self-review: passed. Independent audit: not yet performed.
