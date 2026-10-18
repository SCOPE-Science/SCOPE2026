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

## Reproduction
Use Python 3.8 or later with only the standard library, run `python verify.py` in the directory containing this file. The program constructs the field-linear commutator matrix directly from five upper-triangular parameters over the dual-number algebra and performs modular Gaussian elimination, without using the tangent-stratum formulas of the proof. It exhausts \(2^{10}=1024\) and \(3^{10}=59049\) parameter tuples, multiplies counts by the number of common diagonal choices, checks the seven closed formulas, and prints `VERIFY_UT3_DUAL_OK` on success.

The exact observed frequencies at \(q=2\) are \((4,4,72,112,704,1408,1792)\), and at \(q=3\) are \((9,18,648,2646,25110,122472,380538)\), in ascending rank order. These checks do not establish the infinite family; the general proof is in RESULT.md. No independent audit has been performed.
