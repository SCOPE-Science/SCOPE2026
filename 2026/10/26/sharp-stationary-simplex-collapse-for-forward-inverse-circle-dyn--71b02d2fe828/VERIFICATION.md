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

The proof is an analytic argument applying to every integer degree \(b\ge2\) and every admissible probability-weight triple. The core checks are: \(FQ_b=I\); uniform inverse-preimage grid transport to Haar at cost at most \(1/(4b^j)\); the geometric recurrence for \(F^n\nu\); positivity of its total-variation limit; the explicit inverse simplex map; and first-Fourier-character lower bounds. All infinite conclusions are derived from these identities and completeness, not from finite enumeration.

The standalone Python 3 checker `checks/check.py` uses only the standard library. Running `python checks/check.py` prints the three lines recorded in `checks/output.txt`. It uses `fractions.Fraction` for exact arithmetic and checks 240 finite stationary-truncation residuals, corresponding exact mass identities and bounds, and 45 finite preimage-grid instances. It does not attempt to certify the infinite limit or all parameter values by enumeration.

For exact reproducibility, the checker and its expected output are included with the mathematical report. No external computational datasets or unpublished papers are needed.
