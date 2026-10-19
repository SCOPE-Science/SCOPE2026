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

# Reproduction and proof boundaries

Execute `python3 verify.py` in a directory containing that standalone script. No nonstandard Python packages are required.

The verifier uses `fractions.Fraction` throughout and (i) checks that each row of the interbank-liability matrix has a positive outside share, (ii) computes all fixed-default-set index vectors by solving rational linear systems, (iii) verifies that three exactly specified affine payment branches meet at their boundary values and satisfy the full clearing equation on their intervals, (iv) checks three strict priority orderings, and (v) recomputes clearing payments separately for each injected coordinate at three interior recovery strengths. Printed success markers are not a substitute for the displayed proof; the script includes assertions on the actual rational values.

The network-wide two-bank impossibility is proved analytically by nested default sets and the constant-index formula, not by checking finite samples. Boundary parameters are not claimed to have unique optimal recipients. The normalized model includes outside creditors, so aggregate gross payments should not be conflated with net economic welfare. Published sources establish the clearing mechanism and sensitivity method. Independent audit and independent scientific validation have not been performed.
