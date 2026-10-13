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

# Reproducible verification

Run `python3 verify.py` using the standard Python library. The program exhaustively enumerates every permutation for orders \(2\) through \(8\) at rational cycle weights \(1/4\), \(1\), \(3/2\), and \(3\). It independently calculates weighted moments and checks the exact finite-cycle formula and beta-integral polynomial expression. Supplementary rational sign checks cover further orders; a numerical bisection confirms the explicit three-element threshold.

The verification intentionally does not treat these bounded computations as proofs of the all-order inequalities, uniqueness, or asymptotic limit. Those conclusions follow from the support-separated integral argument and endpoint asymptotics in `RESULT.md`. No independent audit has been conducted.
