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

The self-contained standard-library script `verify_commuting.py` creates every zero matrix and uninterrupted one-block diagonal rook matrix as a partial integer translation, then computes products through finite-map composition rather than the interval endpoint formulas used in the proof. It checks each of the four nonzero-equality strata and the mutual-zero stratum for every ordered pair for \(1\le n\le12\), totaling 986,374 ordered pairs. Run `python3 verify_commuting.py`; a passing run prints `ALL_CONSECUTIVE_DIAGONAL_COMMUTATION_CHECKS_PASSED 12 986374`.

Analytical verification additionally consists of the independent interval counts and the signs-and-boundaries case partition written in RESULT.md. Finite checks are not a certificate for all \(n\), and no independent human audit has been performed.
