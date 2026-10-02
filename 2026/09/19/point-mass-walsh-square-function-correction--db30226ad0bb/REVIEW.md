# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The singleton identity was reconstructed directly from the Walsh difference definition. Writing the singleton indicator as the product of the coordinate factors shows that a distinct-index derivative survives exactly when every negative coordinate lies in the chosen index set, with magnitude \(2^{-k}\). Counting the surviving index sets at Hamming radius \(r\) gives the exact pointwise formula and, after shell counting, the exact \(L_p\) norm identity. Maximizing the exponent \(r+(k-r)p/2\) gives the three fixed-\(p\) regimes. Keeping \(p=2+\lambda/\log n\) in the same finite sum gives the displayed critical crossover. Most importantly, the primary source was read at Section 6.3: its Lemma 6.3 evaluates the same point as \((-2)^k\), whereas the direct calculation gives \((-1)^k2^{-k}\). The corrected \(r=k\) shell still yields growth of order \(n^{k/p}\), so the source exponent-sharpness conclusion survives although its normalization does not.

Originality: PASS. The exact Resultary search for the singleton Walsh-square-function profile and critical crossover returned this record as the only matching published finding. The primary Jiao--Luo--Zanin--Zhou paper was read in full at the relevant Section 6.3 and contains the erroneous normalization but not the corrected binomial profile or the \(1/\log n\) crossover. Broader searches for higher-order Walsh/Riesz sharpness located the source theorem and general hypercube literature but no earlier statement of this exact correction. The formula is elementary enough that unindexed prior folklore remains a residual risk, but no inspected source implies the complete exact profile or critical-window limit.

Scientific value: PASS. This is not merely a recomputation of a known constant: it corrects a numerical error in the published sharpness witness while proving that the intended exponent remains valid, and it replaces the flawed point estimate by an exact all-shell formula. The resulting phase transition at \(p=2\) and the explicit \(1/\log n\) crossover are natural quantitative information about the standard sharpness example.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
