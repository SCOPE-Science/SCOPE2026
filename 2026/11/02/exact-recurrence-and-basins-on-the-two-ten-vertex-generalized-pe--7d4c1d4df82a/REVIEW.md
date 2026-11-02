# Review of the finite generalized-Petersen excitation classification

**Correctness — PASS.** The two graph definitions and the synchronous three-state rule are explicit. There are exactly \(3^{10}=59049\) labelled configurations for each graph. Complete transition arrays were rederived and verified by independent Python indegree-peeling and C++ functional-trajectory methods, which agree exactly on all primitive orbits, basin populations, first-periodic-entry counts and maxima. Exhaustive graph-automorphism backtracking gives the 23 and six geometric temporal-orbit classes. The proof is complete for these two finite graphs; the certificates are replayable using only the files supplied.

**Originality — PASS, qualified.** The original full-text theorem of Gravner–Lyu–Sivakoff (2016) establishes general synchronization and excitation-rate criteria. Those general criteria are not claimed as new. Neither the inspected article nor the Petersen simple-graph cycle data provides the full temporal orbit and basin tables. An earlier linear parity classification on generalized Petersen graphs has a different state space and update map, so does not imply the nonlinear census. The 1995 Fisch–Gravner paper was inspected only through its publisher abstract. Equivalent unpublished or unindexed numerical work remains a priority risk.

**Mathematical value — PASS.** The two most canonical ten-vertex examples in the generalized-Petersen family display distinct exceptional primitive excitation periods, seven and eight; their longest transients differ, and their temporal cycles form 23 and six spatial symmetry classes. The exact basin populations show that the dominant attractor class changes from period four on the prism to period five on the Petersen graph. This is a motivated complete finite dynamical classification, not merely a check of the update normalization.

**Limitations.** No statement about \(GP(n,k)\) for \(n\ne5\) is proved. Lack of a search match does not establish absolute priority. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
