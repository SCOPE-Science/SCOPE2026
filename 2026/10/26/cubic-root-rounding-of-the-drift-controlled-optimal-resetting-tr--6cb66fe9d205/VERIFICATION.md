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

# Verification

Run `python verify.py` using Python 3 with SciPy installed. The program executes 235 numerical derivative/root/asymptotic tests, 45 separate Gaussian-resolvent quadrature comparisons, and prints representative optimal rates and critical-crossover values. Observed execution ended successfully:

`PASS numerical derivative signs, unique-root brackets, asymptotics, crossover: 235 assertions`

`PASS independent Brownian resolvent quadratures: 45`

The quadratures integrate the unabsorbed drifted Gaussian transition density and compare against the analytical free resolvent before introducing the point sink. The stationarity tests differentiate the dimensionless mean independently and compare numerical minima on either side. The near-threshold tests span positive and negative crossover offsets and verify the predicted scaling at increasing sink strength.

The finite checks do not prove global uniqueness or asymptotic statements for infinitely many parameters; those depend on the explicit derivative sign-change argument and uniform Taylor/coercivity proof in `RESULT.md`. Truncation and floating-point error are bounded only to the numerical tolerances stated in `verify.py`. Full-text literature comparison has a documented access limitation. Independent external validation has not occurred.
