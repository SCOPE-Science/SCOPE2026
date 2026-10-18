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

The included standard-library programs run from their containing directory and check all rational-point permutations, Fano-line incidence sets, and binary quartic jet constraints specified in the theorem. `verify_quadratic.py` explicitly confirms 168 projective maps, 1344 degree-two permutation images, zero preserved Fano lines and no transpositions; the two quartic programs independently overcount all base-locus types needed for a computational parity cross-check (168 proper and 72 infinitely near configurations). The primary quartic proof uses homaloidal factorization, not exhaustion of geometric birationality tests. Reproduce with `python verify_quadratic.py`, `python verify_quartic_proper.py`, `python verify_quartic_infinitesimal.py` from the extracted directory. Outputs are included alongside the scripts. Published group-theoretic ingredients are cited in `RESULT.md`; no external audit is asserted.
