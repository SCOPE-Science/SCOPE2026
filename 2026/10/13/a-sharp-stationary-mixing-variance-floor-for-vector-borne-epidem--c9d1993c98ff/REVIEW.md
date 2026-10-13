# Scientific assessment: a stationary-mixing variance floor

## Correctness — PASS

The result is a finite-matrix theorem for every positive integer number of host groups and vector patches, with strictly positive host weights and stationary vector distribution, positive effective host presence in every patch, and an irreducible conservative vector generator with that fixed distribution. The reproduction-number reduction is independently matched to the explicit matrix in Gao–Yuan [1, Eq. (4.4) and Corollary 4.4]. The proof's nonstandard step is the balanced-flow entropy identity \(E=\sum_{i\ne j}F_{ij}(z_j/z_i-1)\ge0\); its equality condition follows from irreducibility. Groupwise Cauchy–Schwarz gives the exact second moment \(M\), not merely its Jensen floor one. Equality at \(M\) forces \(y\) proportional to the stationary distribution and then forces constant group exposure. An explicit rank-one-resolvent family reaches the lower bound in the large-rate limit. The second-moment floor and the equality locus hold without assumptions of migration reversibility or rank conditions on the residence matrix.

A standalone standard-library verifier reconstitutes the two-group matrices and exactly checks the characteristic-polynomial witness. It returns `VERIFY_OK`. That computation is a diagnostic for the example, not the mathematical proof of the quantified assertion.

## Originality — PASS, with documented residual access uncertainty

The closest source [1] contains the same next-generation matrix and already contains the Cauchy–Schwarz intermediate second-moment expression in the proof of its Theorem 4.2. Accordingly, that standalone inequality is **not** claimed novel. But its Corollary 4.4 gives only sufficient equality conditions; Remark 4.8 gives counterexamples to necessity of proportionate patch distributions; and the discussion explicitly requests a necessary and sufficient characterization. No exact fixed-stationary-distribution optimization over **all vector movement generators** or strict finite-rate nonattainment was found in its fully inspected Sections 2–6. The result addresses this mathematical gap through a fixed-stationary-vector sharp infimum, a full equality characterization and a constructive fast-migration limit.

The all-Eulerian equality theorem of Gao–van den Driessche–Cosner [2, Theorem 3] concerns migrating host patch populations, not fixed host residence groups. Gao–Cao's [3] fully Lagrangian model has different vector movement mechanics; its full text was not available and so not ruled out through complete inspection. Gao–Lou [4] addresses Eulerian host dispersal and prevalence, not this fixed-vector-generator optimization. Targeted mathematical searches did not identify another implication-equivalent theorem. The unresolved literature-access issue and unindexed formulations remain risks, and a failed search is not taken as proof of absolute novelty.

## Value — PASS

The theorem gives a sharp answer to what changing **only vector migration rates** can accomplish when vector equilibrium geography is fixed: it reduces reproduction risk no farther than a precisely identified and interpretable variance in host-group exposure. The strict nonattainment result distinguishes realizable finite interventions from their limiting optimum. The equality characterization answers a question raised in the motivating publication and includes nonproportional host/vector patch populations. The invariant \(M\) is intrinsic to the model and motivated by that epidemiological optimization, not an arbitrary numerical slice. Neither the generic groupwise Cauchy–Schwarz computation alone nor the exact two-group example would have carried this value judgment; the complete variational theorem does.

## Limitations and closest literature

The manuscript makes no assertion about infection prevalence, nonhomogeneous rates, vector-free host patches, movement cost, or constrained migration networks. The equality comparison with Gao–Cao [3] is abstract/preview-level only because complete access was not obtained; its different vector movement representation reduces but does not erase the residual risk. The current proof and code are not an independent external audit.

Self-review: passed. Independent audit: not yet performed.
