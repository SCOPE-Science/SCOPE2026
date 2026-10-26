# Mathematical review

## Correctness: PASS
The exact atom moments give \(v=1+p(a^2-1)\) and fourth moment \(1+p(a^4-1)\). At \(p=1/(2a^4)\) the fourth cumulant is strictly less than \(-3/2\). The one-point MGF witness at \(t=a\) proves failure at every \(a\ge4\) by monotonic positivity of \(g(a)\). Near both endpoints, the fourth-derivative sign controls small \(t\), compact continuity controls middle \(t\), and \(M(t)\le e^{a|t|}\) controls all large \(t\). The sparse asymptotic has matching lower and upper bounds with relative error \(O(1/\log a)\). These are analytic proofs, not extrapolations from finite tests.

## Originality: PASS (bounded literature comparison)
The 2019 source gives the proxy definition and strictness criteria, including a different positive-kurtosis three-mass counterexample. The 2025 three-mass classification does not imply the two-radius four-atom result. Searches against related records and explicit alternative descriptions returned no equivalent, stronger, or tabulated statement. The general methods are known, and unindexed prior results remain a residual priority risk; title or exact-parameter mismatch by itself is not used as proof of novelty.

## Value: PASS
The result establishes a structural gap between a local cumulant criterion and a global MGF concentration guarantee, including two separated regimes of validity within a natural single mixing parameter. The quantitative divergence \(a^2/(8\log a)\) under variance tending to one and negative fourth cumulant gives a sharp asymptotic obstruction in a standard concentration-calibration problem. The result is neither a mere numerical counterexample nor an arbitrary constant gain.

## Closest literature and limits
Arbel–Marchal–Nguyen (2019), arXiv:1901.09188v1, addresses bounded-variable strict sub-Gaussianity and gives the necessary cumulant condition. Atouani–Marchal–Arbel (2025), arXiv:2510.06132v1, classifies three-mass laws. The number of components and exact transition weights of the four-point family are not computed. Global novelty and independent proof validation are not established.

Self-review: passed. Independent audit: not yet performed.
