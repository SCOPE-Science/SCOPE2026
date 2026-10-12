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

# Verification record

The included `verify.py` uses Python 3's standard library only. It constructs the actual convolution-symmetry matrix, enumerates possible vertices through exact rational three-by-three determinant calculations, verifies all four expected vertices for eleven rational parameters, checks symmetry and normalization, and confirms strict dominance comparisons for the two discarded entropy candidates. It performs finite numerical logarithm checks around the phase switch. The observed output was `CHECKS_PASS 189 phase_boundary_midpoint 0.46075138164949586`.

The determinant sign table and the explicit entropy derivative in `RESULT.md` establish the global assertions. Finite replay is not a proof for every real parameter, nor does it establish priority over unindexed publications. The full text of the motivating 2026 preprint was not inspected; its publicly available abstract describes three- and four-element cyclic classifications. No independent scientific audit or external certification has been conducted.
