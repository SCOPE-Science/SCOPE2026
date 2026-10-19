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

Run `python3 checker.py` from the directory containing this file and the standalone checker. The program needs only Python's standard library. It directly enumerates all horizontal vector pairs, checks every target against the proven integer formula, and for selected small rings independently computes full group commutators using group multiplication and inversion.

Tested ring families are modular rings \(\mathbb Z/2^n\mathbb Z\) for \(n=1,2,3\), \(\mathbb Z/3^n\mathbb Z\) for \(n=1,2\), and two types of dual-number chain rings \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) and \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\). Both \(m=1\) and \(m=2\) occur. The length-one cases are boundary diagnostics, not part of the claimed novelty. The checker prints `VERIFY_OK` if all assertions pass.

The finite computations do not prove the all-rings theorem: the proof follows from the image of the commutator functional, exact ideal-layer cardinalities, and a valuation-stratified sum. No independent audit or external validation has been performed.
