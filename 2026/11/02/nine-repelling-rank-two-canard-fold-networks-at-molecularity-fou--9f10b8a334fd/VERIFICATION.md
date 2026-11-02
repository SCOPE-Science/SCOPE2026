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

The analytic proof reduces each three-reaction rank-two fold to exact positive-kernel and integer-moment conditions. Re-execution of `computations/check_repelling_canard.py` using standard-library Python returned `PASS: exact exhaustive finite classification and concrete positive-trace witness`. The generated nine-row table was compared byte for byte to `data/repelling_canard_molecularity4.tsv` and matched.

The checker exhaustively enumerates 4,060, 117,480 and 1,521,520 unordered triples at maximal complex molecularity two, three and four, respectively. It found, among the degree-four triples, 1,590 positive rank-two kernel triples, 350 nondegenerate geometric canard folds, and nine folds with strictly positive slow trace. The embedded code displays its classification logic without external data or library dependencies; exact Python integer arithmetic is used for every decision.

For the explicit witness, the formula for the unique positive equilibrium, the derivative matrix, its determinant and its trace are verified analytically in `RESULT.md`. The tests do not certify independent audit, historical novelty or existence of any canard explosion. Generalization beyond the enumerated molecularity bound is not asserted.
