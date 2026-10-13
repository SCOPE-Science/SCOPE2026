# Self-review

## Correctness — PASS

The Nyström term reduces exactly to the projection residual for \(A=I_n\). Conditional on all but two probes, the two residual norms share one spherical angular factor, whose beta second moment gives \(2\nu/(\nu+3)\) covariance; exchangeability then gives both exact variance identities. The fourth-moment bound and Markov–Cauchy argument establish actual nonconcentration even while the reported proxy vanishes. Critical identities and numerical projections were replayed from the packaged verifier. No simulation is used as an asymptotic proof.

## Originality — PASS, with residual priority risk

The closest source is Epperly–Tropp–Webber, arXiv:2301.07825, particularly its XNysTrace Eq. (8), Eq. (9), Proposition 2, Proposition 5, Section 2.3, and proof of Proposition 2. **Proposition 2 already contains a general correlation-versus-calibration identity** and must not be credited to the present result. Its inspected full text does not evaluate the standard-Gaussian identity-matrix pairwise covariance, fixed-codimension variance floor, or explicit nonconcentration bound. The earlier leave-one-out residual literature, arXiv:2207.06342, concerns related algorithms without this exact calculation. Closest binary-probe examples and Gaussian rank-one Nyström approximation results have different probe laws and target statistics. Searches for equivalent trace covariance, Wishart/angle formulations, and stronger general results found no decisive covering statement; this does not establish priority. Unindexed exact-special-case work remains possible.

## Value — PASS, with limitation

The analytical classification determines the calibration factor for a natural flat-spectrum benchmark exactly across all intermediate sketch budgets. Near full rank, the posterior absolute-error estimate can become arbitrarily optimistic even though the true error does not concentrate; precisely one additional column then makes the ideal pseudoinverse method exact. The result identifies a mathematically meaningful distinction between exchangeable estimators and effectively independent replicate diagnostics. The limitation is crucial: the paper recommends a separately normalized version, which does not inherit this flat-spectrum pathology, and relative-trace accuracy can still improve at fixed tolerance.

Self-review: passed. Independent audit: not yet performed.
