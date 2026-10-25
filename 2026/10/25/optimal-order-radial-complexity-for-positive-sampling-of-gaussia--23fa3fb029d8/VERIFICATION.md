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

Run `python3 checker.py` with a Python 3 standard library interpreter. The recorded output is stored in `checker_output.txt`. It tests the explicit Poisson eigenvalues for degrees up to 4096, separately evaluates weighted complex sample grids against the predicted diagonal forms for small degrees, and checks a range of truncated-Poisson width ratios. The run passed 6,369 assertions.

# Analytical evidence

RESULT.md contains the complete proof of the unconditional positive-weight radius obstruction and the all-degree explicit frame bounds. The nonstandard elementary width estimate is derived separately in its Step 2; no exact certificate is assumed without derivation. The numerical checker is supplementary and is not a proof for untested degrees, intensities, or configurations.

# Scope and external status

The sampling weights must be positive. The \(\Theta(\sqrt N)\) order, not the best coefficient, is proved. Independent audit has not been performed.
