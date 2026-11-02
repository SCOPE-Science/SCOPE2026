---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python3 VERIFY.py` using Python 3 standard-library modules only. Its exact rational assertions verify (i) clock-correction martingale drift and covariance coefficients for dimensions 2 through 8 and every sign configuration, (ii) the pathwise occupation/embedded-memory/clock identity across every finite probability branch of a two-coordinate memory model through six global updates, (iii) the elephant second-moment recursion by exact probability-tree enumeration for five rational memory parameters through eleven embedded spins, and (iv) the mean and raw second occupation moments under unbiased coordinate refreshing for dimensions 2 through 6. The saved `CHECKS.txt` shows **38,687 exact assertions passed**.

The program also prints three finite approximations to an analytic supercritical second-moment constant. Those numbers are illustrative only; no finite evaluation certifies an infinite stochastic limit. Functional convergence rests on the mathematical proof, including the classical elephant FCLTs, the bounded-observable weak law, conditional martingale functional CLT, random-clock approximation, and beta-integral evaluation.

One limitation in reproducibility is that a full independent mathematical audit has not been carried out. The evidence is sufficient for the self-review specified above but is not a computer-verified formal proof or a definitive priority determination.
