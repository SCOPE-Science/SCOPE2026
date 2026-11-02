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

Run `python3 verify.py` with Python 3.9 or later. No third-party packages, files or external services are needed.

Expected status for the supplied script:

`VERIFY_OK moduli=38 reduced_pair_inputs=286302 original_fraction_inputs=474 exact_arithmetic=yes`

The script performs complete congruence-class enumeration for each of 38 listed parameters and compares its reduced-integer-recurrence failure sets against a separately implemented finite-field prediction. For each modulus it also checks the four rational density formulas against the exact observed residue counts. A second calculation uses the original rational recurrence and `fractions.Fraction` for 474 additional initial values; it checks perfect squares using `math.isqrt`. It verifies the concrete four-cell \(h=65\) frequency table.

The mathematical proof, not finite testing, establishes the theorem for all allowed parameters and all positive starts. A separate check of earlier publication priority has not been independently completed; the related 2026 arithmetic-dynamics preprint named in the motivating paper could not be read.
