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

Run `python3 artifacts/frog_phase_check.py` and `python3 artifacts/test_multiband.py` with Python 3, NumPy and SymPy. The combined stdout is in `artifacts/checks.txt`.

The first script exhaustively constructs exact integer relation lattices for 195 two-band configurations, computing Smith forms rather than approximating group ranks; it also compares a small selection of complex-valued discrete traces and phase-sensitive rows numerically. The second script checks agreement of the full pair-sum lattice and the compressed interval-overlap lattice for 280 seeded multiband unions. The output reports zero assertion failures. Floating-point trace comparisons use thresholds stated in the code and are not a proof of exact equality in arbitrary dimensions.

The all-band theorem is justified by its independent algebraic proof in `RESULT.md`, particularly coefficient comparison at delay zero, affine-phase rigidity on interval bands, and the interval-overlap converse. Numerical tests are only supporting evidence. No independent external mathematical validation has been performed.
