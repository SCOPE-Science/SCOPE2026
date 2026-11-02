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

# Reproducibility

From the same directory run `python3 verify.py`; no third-party dependency or network access is required. The verifier directly enumerates every perfect matching with \(2\le n\le7\), computing its cyclic simple-chord and geometric crossing counts, and compares each entire joint count dictionary with the polynomial prediction. It separately checks the matching counts in cycle graphs, and verifies the Touchard–Riordan numerator cancellation, nonnegativity, normalization, and first and second exact rational moments for \(2\le n\le13\).

Successful output terminates with `ALL 372 EXACT ASSERTIONS PASSED`. For \(n=7\), the exhaustive sample consists of 135,135 matchings; the six full enumerations together cover 146,598 matchings. These are **finite** checks only. The complete bivariate polynomial follows for all \(n\ge2\) from the explicit marked-boundary-pair deletion and cycle-matching bijection in `RESULT.md`. The classical crossing second moment is documented in the references to that proof.

## Interpretation and limits

The verifier does not search the literature, demonstrate independence, certify originality, check the infinite theorem by enumeration, or prove the classical Touchard–Riordan formula. A separate independent audit has not been performed.
