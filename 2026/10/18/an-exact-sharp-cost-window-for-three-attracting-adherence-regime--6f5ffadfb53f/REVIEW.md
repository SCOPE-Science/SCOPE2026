# Mathematical review: An exact sharp cost window for three attracting adherence regimes

**Correctness — PASS.** The theorem and proof cover the full parameter domain for the at-most-three hyperbolic sink ceiling. The fixed-family stationary incentive has a unique maximum, giving the exact necessary and sufficient cost window. Exact rational Bernstein coefficients certify the cubic Routh–Hurwitz inequalities throughout the upper mixed-endemic branch; boundary eigenvalues and the lower-branch sign are computed symbolically. The accompanying standalone checker was executed on the actual files and its exact tests passed. This does not prove anything about global basins or periodic attractors.

**Originality — PASS, subject to residual risk.** Kumata, Ito and Yamamichi (arXiv:2610.12519v1, October 7, 2026) already describe the qualitative three-way multistability in Figure S3; the present finding explicitly credits it. Earlier analysis also already shows at most two mixed-endemic equilibria and an abandonment/partial-adherence bistability. The new claim is narrowly the exact fixed-parameter if-and-only-if cost interval, the simultaneous stability certificate and robust algebraic witness. Targeted mathematical-record searches and comparisons with the full source main article and supplementary derivations identified no coverage of this numerical/algebraic classification. Saad-Roy–Traulsen (2023) uses a different model. The related Martin–Castella–Hamelin (2026) article was not available in full, so equivalent hidden coverage cannot be excluded.

**Value — PASS.** Three qualitatively distinct locally stable intervention outcomes at the same demographic parameters provide a natural policy-relevant mathematical classification. The sharp, explicit cost interval and strict verified stability conditions quantify a transition left qualitative in the source paper. This is not an empirical effect-size claim or a global basin theorem; no generality beyond the fixed family is attributed to the cutoff.

## Limitations and evidence

The complete derivation and reproduction steps are in RESULT.md and verify.py. All continuum claims are analytic; finite checks merely verify the symbolic certificate. No independent mathematical verification has occurred. The original model, pre-existing structural results, and qualitative multistability are credited.

Self-review: passed. Independent audit: not yet performed.
