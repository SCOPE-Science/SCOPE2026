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

# Verification and limits

The exact mathematical proof reduces the count to the determinant of a specified six-by-six integer matrix, a two-by-two Schur transfer matrix, the directed matrix-tree theorem, and the BEST Euler-tour formula. Those steps are detailed in `RESULT.md`.

The standalone `verification.py` script requires only Python 3. Execute `python3 verification.py`. It checks the six-state determinant and transfer by exact integer/rational elimination, computes the full directed matrix-tree cofactors for alphabet sizes \(2\) through \(6\), enumerates all binary cycles with a fixed first edge, and explicitly builds valid universal cycles at sizes \(2\) through \(4\).

All checks produced `VERIFY_OK`. Finite checks support, but do not logically establish, the parameter-uniform assertion. No independent scientific audit has been performed, and the assessed novelty is limited by unindexed literature or alternative formulations that may have escaped comparison.
