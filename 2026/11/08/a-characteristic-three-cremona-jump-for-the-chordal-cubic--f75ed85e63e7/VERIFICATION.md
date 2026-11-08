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

# Reproducibility and limits

Run `python3 verify_hankel_polar.py` with Python 3.8 or later. The script uses only the standard library. It exhausts projective point sets over the prime fields with characteristics \(3\), \(5\), and \(7\), tests the Pluecker equation, derivative identities, and exact base loci, then prints `HANKEL_POLAR_EXACT_CHECKS_PASSED`. Its `verify_hankel_polar_output.txt` is the reproducibly generated output of this same script. The general statement relies on the algebraic proof in RESULT.md, not finite extrapolation. No independent scientific audit has been performed.
