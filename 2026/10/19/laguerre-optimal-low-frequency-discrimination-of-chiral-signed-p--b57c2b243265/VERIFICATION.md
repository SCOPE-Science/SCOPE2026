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

# Reproducible verification and limits

Execute `python checker.py` with the listed scientific Python requirements. The program enumerates the signed-permutation groups in dimensions \(1\) through \(4\), directly calculates the degree-\(n^2\) alternating moment, and compares it with the closed form. It verifies the exact monic-Laguerre discriminant for the same degrees, as well as the leading Fourier-series ratio at two small frequencies in dimension \(3\). `CHECKER_OUTPUT.txt` records the direct output.

The full statement does not depend on numerical computation. Its unrestricted proof uses polynomial divisibility under signed reflections, the Fischer derivative pairing, strict concavity, Laguerre's differential equation, and a monic-polynomial resultant recurrence. The numerical Fourier evaluations illustrate convergence and are not an infinite proof or independent external review. The uniqueness statement concerns leading-order maximizers, not finite-frequency maximizers.
