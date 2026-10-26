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

# Reproducible checks and limitations

Run `python verify_heisenberg.py` using Python 3 with NumPy installed. The program constructs the Heisenberg superoperators independently on matrix-unit bases for dimensions 2–4 and multiple renewal hazards, checks their one-step inverse intertwiners against the derived analytical formula, checks a three-cycle explicit negative eigenvalue, and tests additional cyclic-shift examples through dimension 6. In the checked environment it returned `PASS 89 independent deterministic finite-matrix comparisons`.

The independent matrix calculations provide finite-parameter verification. Infinite-horizon necessity and sufficiency depend on the exact analytical decomposition and the cyclic-witness construction in `RESULT.md`, not on experiments. The asserted exact rational witness values are derived symbolically in `RESULT.md`; floating-point output is only a cross-check. No independent external mathematical audit or formal certification has been performed.
