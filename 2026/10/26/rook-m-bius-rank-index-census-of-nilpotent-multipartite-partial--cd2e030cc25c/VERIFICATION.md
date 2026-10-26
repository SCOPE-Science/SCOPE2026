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

# Reproducible verification and scope

Run `python verify.py` using Python 3 and no third-party packages. The verifier independently (1) enumerates all vertex partial injections, tests every pairwise part-distance constraint, rejects vertex cycles, and calculates rank/index; and (2) evaluates the signed coefficient formula using a labeled-chain recurrence indexed by the first remaining labeled vertex. The two methods return identical rank/index tables for \(K_{2,2}\), \(K_{3,2}\), \(K_{2,2,2}\), and \(K_{3,2,2}\). Counts are respectively \(41\), \(153\), \(835\), and \(3089\). The first two are prior-covered boundary regressions; the latter two are distinct three-part cases. The maximum-index formula is directly checked for the three-part cases and the spanning-index multiplicity is checked there.

## Mathematical checking limits

These finite computations do not certify the unrestricted theorem. The proof depends on the unique induced partial injection on part indices, the exact equivalence between nilpotence and absence of vertex cycles, the exponential formula for labeled chains, the rook-poset extension cancellation identity, and the periodic-color upper/lower construction for maximum index. All of these are explicitly proved in `RESULT.md`. In particular the signed coefficient weights are inclusion–exclusion coefficients, not probabilities or empirical fits.

No independent external audit or validation is claimed.
