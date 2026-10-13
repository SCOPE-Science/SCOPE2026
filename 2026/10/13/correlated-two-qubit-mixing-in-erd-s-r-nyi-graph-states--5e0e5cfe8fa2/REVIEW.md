# Scientific review: correlated two-qubit mixing in random graph states

## Correctness — PASS
The quantum criterion follows from an explicit computation of reduced graph-state matrix elements, which turn the maximally mixed condition into full row rank of a binary cut matrix. For disjoint pairs, conditioning on the common \(2\times2\) cross-edge block reduces the covariance to the variance of three explicit conditional probabilities. For overlapping pairs, conditioning on the shared outside-neighborhood vector reduces the joint law to three elementary cases. The number of event-pair orbits yields the global variance; an exact isolated-vertex mixed moment and direct moment algebra give the mean-square asymptotic. The proof covers all labeled independent-edge graphs with \(n\ge4\), without extrapolating finite enumeration. All 33,856 graph instances for sizes four through six and direct statevector marginal checks in the accompanying verifier match the formulas.

## Originality — PASS, with priority limitations
The closest source is Miller et al., arXiv:2207.07665, whose paper includes two-body stabilizer/graph-twin identities and random graph-state Shor–Laflamme statistics. Its variance concerns the normalized Pauli-weight distribution *within* a graph state, not the across-graph covariance between particular maximal-mixing marginal events. Its appendix computes first moments of Shor–Laflamme coefficients, not this event-count variance. Zhang and Zhang, arXiv:2608.03102, motivate the Erdős–Rényi graph-state setting but compute different GHZ observables. Sudevan and Das, arXiv:2201.05622, study deterministic uniformly maximally mixed graph states, without the random pair-event covariance. Overlap comparisons with the accessible research records found no equivalent exact law; this is a bounded priority assessment, not a uniqueness proof. An uncatalogued joint twin/leaf-count moment theorem remains a residual risk.

## Value — PASS
The statistic is a natural partial measure of two-uniform entanglement, where every two-qubit reduction should be maximally mixed. A first-moment calculation does not predict sampling variability because overlapping and disjoint pair events are positively correlated; the exact joint-covariance law resolves this gap for every system size. The decomposition showing that rare isolated vertices explain nearly all *variance*, but only one third of mean defects, gives a concrete structural mechanism for fluctuations and provides a benchmark for random graph-state and stabilizer-resource studies.

## Restrictions
Only the independent-edge \(G(n,1/2)\) ensemble is proved. No finite-depth circuit law, higher-point joint distribution, or total variation approximation is asserted. The verifier checks finite sizes; exact algebra provides the infinite-family proof. Literature searches cannot eliminate unpublished, unindexed, or implicitly equivalent identities.

Self-review: passed. Independent audit: not yet performed.
