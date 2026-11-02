# Review

## Correctness: PASS

The killed-generator Feynman–Kac formula gives the hazard comparison and its integrated bound. The renewal/resolvent expansion has leading \(a/r\), yielding the all-rate global limit. Every directed three-state generator with source-to-target rate \(a>0\) reduces to an affine-over-affine mean with a derivative of fixed sign; no isolated strict positive optimum exists. The four-vertex backward equations give \((r^2+7r+9)/(r^2+8r+7)\) exactly and a quadratic derivative with a unique positive root. The minimum is below both endpoint values. Independent exact-rational solver checks passed (1559 checks). Finite enumeration is corroboration, not proof of the universal state-count claim.

## Originality: PASS, best-knowledge only

The main motivating 2025 study (Hartmann–Majumdar, arXiv:2505.19903) establishes infinite-rate optimality on a *homogeneous hypercubic lattice* for a nearest-neighbour source and provides the general renewal formula; it does not give the sharp weighted finite-graph four-state distinction. Earlier general network and absorbing-chain studies (Riascos et al., arXiv:1910.13568; Chen et al., arXiv:2111.01330) can imply computations of individual small generators but were not found to assert the sharp four-state obstruction, witness, and hazard bound as an integrated statement. Multiple semantic searches over published mathematics records and source-centered literature were performed; no covering result was located. Residual risk: more general stochastic comparison results may already imply hazard domination, while a small-state restart example or sharp minimum might exist in a less directly titled paper. No literature-wide uniqueness claim or independent audit is made.

## Value: PASS

The minimal-state classification answers a sharp structural robustness question prompted by nearest-neighbour infinite-rate optimality: the simple law persists under a direct-hazard domination but can fail at exactly four weighted states. The minimal undirected witness shows how a productive fast-target route and a dead end compete, making a finite restart clock genuinely optimal despite direct target adjacency. The state-count barrier and rate-independent hazard criterion matter to rate selection in stochastic search on heterogeneous networks; they are not a mere numerical optimization over arbitrary parameters.

## Limitations

The four-state witness requires heterogeneous edge rates; it does not disprove the published homogeneous-lattice theorem. The all-graph bound concerns the mean and survival; monotonicity is not asserted. Perturbative robustness establishes at least one finite optimum but not uniqueness for all perturbed weights. The directed three-state obstruction assumes the reset vertex can jump directly to the target. The finite checks are not exhaustive over continuous parameter families.

Self-review: passed. Independent audit: not yet performed.
