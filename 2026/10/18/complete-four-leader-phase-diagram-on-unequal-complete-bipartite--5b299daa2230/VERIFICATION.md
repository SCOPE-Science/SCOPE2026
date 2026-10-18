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

# Computational verification and limits

Execute `python verify.py` from a directory containing the packaged checker. It requires Python 3 only. The checker independently constructs the grounded Laplacian for \(K_{2,m}\), performs fraction-exact Gauss–Jordan inversion for 81 instances, and compares their traces with the derived rank-two formula. It checks the polynomial difference identities across 96 parameter pairs, verifies rational root brackets at all exceptional sizes, tests representative optima from every regime, and checks the eventual coefficient-sign pattern for part sizes 11 through 119.

Expected output: `VERIFY_OK exact_inverse_traces=81 rational_phase_and_difference_checks=passed`.

The analytical proof in `RESULT.md` handles every integer \(m\ge4\) and every real \(\kappa>0\), and includes the required uniqueness and boundary arguments. Finite checks do not certify the infinite claim on their own. Neither a computer-assisted infinite formal proof nor any independent audit is claimed.
