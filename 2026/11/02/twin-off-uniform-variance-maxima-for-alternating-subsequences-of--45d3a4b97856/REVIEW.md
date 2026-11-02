# Scientific review

## Correctness: PASS

The statistic is explicitly defined for \(n\ge4\) and fixed \(q>0\). The deterministic local-extrema identity reduces its length to a boundary descent plus turning-point indicators. Mallows block stationarity and disjoint-block independence reduce all first and second moments to six local probabilities on at most five labels, all enumerated in the standalone checker. Algebra gives \(\operatorname{Var}(L_n)=nV(q)+K(q)\). The derivative factorization and exactly two positive roots of the reciprocal polynomial, established by Descartes' rule and sign changes, prove the global extremizer classification. The checker passed 110,195 exact assertions, but finite enumeration is not substituted for the infinite argument.

## Originality: PASS, with priority uncertainty

The uniform mean/variance and the canonical local-extrema representation belong to Stanley and Romik. Houdré–Restrepo's full-text treatment is uniform or based on words/Markov models. Bhatnagar–Peled's Mallows results concern monotone, not alternating, subsequences. Crane–DeSalvo–Elizalde prove weak dissociation and a generic single-pattern variance identity, which are known ingredients of this proof. Their published statement does not assert the combined turning-point statistic or reciprocal off-uniform global maxima. The combination requires four-pattern overlap covariances and an algebraic classification of a degree-ten stationary equation. A complete priority search cannot exclude a concealed derivation in historical enumerative literature or later work; the novelty assessment is best-knowledge, not a uniqueness certificate.

## Value: PASS

Alternating subsequence length measures the oscillation of a ranked order, while the Mallows inversion parameter describes ranking concentration. The result exposes a nontrivial contrast: expected oscillation density is highest at the uniform law but its fluctuation strength is locally *lowest* there and globally maximized at two specific biased laws. The all-size exact variance enables finite-sample calibration, and the two-maximizer theorem gives a natural global phase classification, not an arbitrary parameter slice.

## Closest literature and limitations

- Stanley (2005) and Romik (2010/2011): uniform law and deterministic representation.
- Houdré–Restrepo (2010): uniform/permutation-word and Markov probabilistic asymptotics.
- Bhatnagar–Peled (2013): Mallows LIS/LDS, different statistics.
- Crane–DeSalvo–Elizalde (2016), especially Section 8: single consecutive-pattern count and weak dissociation; closest general method.
- Fang et al. (2021): Mallows rise/fall generated walks and arcsine behavior, not alternating-subsequence variance.

No new CLT, finite-\(n\) variance maximizer, or independent validation is claimed. Additional older generic inversion-refined alternating-run identities may imply some formulas; this is a residual historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
