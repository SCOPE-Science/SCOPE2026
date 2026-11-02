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

# Reproduction and limits

Run `python3 verify.py` in the directory containing this file and the verifier. The program enumerates reduced row-echelon representatives over \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\), directly computes maximum word weight and exact occupied support, compares all support/rank coefficients with the claimed polynomial, and finishes with `VERIFY_OK` if all comparisons succeed. Ambient lengths checked are zero through five at \(q=3\) and zero through four at \(q=4,5,7\). It does not merely compare total counts: for \(n\ge4\) it explicitly checks support-four rank-two terms. The code uses only the standard library and field multiplication for \(\mathbb F_4\) by reduction modulo \(X^2+X+1\).

The proof analytically excludes all ranks above three and supports above four. Its full-support rank-three exclusion and projective-line coverage lemma establish the general result; finite enumeration is a cross-check and not a proof for untested parameters or for arbitrary field sizes. No independent audit has occurred.
