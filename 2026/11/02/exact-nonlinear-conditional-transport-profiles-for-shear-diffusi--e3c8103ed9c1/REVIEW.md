# Review of exact nonlinear conditional transport profiles

**Correctness — PASS.** A direct stationary-age and Brownian-bridge derivation proves the normalized formulas at every transverse position, with explicit half-integer Bessel moments. `verify.py` checks global covariance identities from the source, exact algebra, 45 numerical posterior moments, and 15 conditional pairs. This does not replace the analytic proof.

**Originality — PASS, qualified.** Abdoli, Olsen and Löwen (arXiv:2410.10333v1) give the stationary joint renewal representation and unconditional moments, which are prior work, but not the evaluated conditional regression, variance or sharp fiberwise tail profiles. Targeted web/database and related-paper comparisons found no explicit equivalent; a generic theorem or direct exploitation of the prior implicit distribution might subsume the formulas. Publication priority is not established.

**Value — PASS.** The exact quadratic conditional drift and cubic dispersion yield an all-height spatially resolved transport law for sheared particles subject to resetting, clarifying information invisible in global second and fourth moments. The arbitrary-parameter solution and monotonicity are motivated observable predictions rather than routine parameter specialization.

**Scope and limitations.** Two-dimensional independent Brownian noise; linear shear; complete simultaneous resetting; stationary population law. No finite-sample results or general flow extension. Closest primary material is arXiv:2410.10333v1 (stationary renewal representation); related arXiv:2406.10039v1 studies partial resetting with refractory pauses, so does not imply this conditional law.

Self-review: passed. Independent audit: not yet performed.
