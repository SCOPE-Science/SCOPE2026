# Scientific review

## Correctness — PASS
The cubic-interpolatory BDF3 time nodes yield the stated exact companion matrices and positive leading derivative coefficients. Dividing first rows by the appropriate scalar decay coefficients and taking the fixed-positive-\(q\), large-\(r\) limit gives a rank-two period matrix whose nonzero eigenvalue is exactly \(-2/(1+q)\). Root continuity proves the asymptotic threshold. A second exact-rational determinant witness proves finite negative-axis instability. The checker was executed successfully from the supplied file. The result does not assert a finite-\(r\) threshold at \(q=1\) or a general PDE theorem.

## Originality — PASS, with unresolved historical risk
Compared the actual claim, not merely its terminology, with the 2001 BDF3 joint-spectral-radius zero-stability study, the 2015 variable-step explicit SSP study, and the 2022 ratio-restricted BDF3 stability theorem. Zero-equation stability does not imply the positive-damping two-period Floquet spectrum, and sufficient arbitrary-grid step-ratio conditions do not establish the asymptotic large-ratio reversal. A published-record search did not identify this precise limit or finite counterexample. Full text of the closely related 2001 study was not accessible; this residual historical-priority risk must remain explicit. This is not independent novelty certification.

## Value — PASS
The theorem exposes a nontrivial failure of transferring fixed-step negative-real-axis stability to a natural adaptive-step pattern. It separates zero stability from dissipative absolute stability and identifies an exact dimensionless damping boundary under extreme step alternation, with a rational finite witness. The result is a motivated stability obstruction, not an arbitrary parameter computation.

Self-review: passed. Independent audit: not yet performed.
