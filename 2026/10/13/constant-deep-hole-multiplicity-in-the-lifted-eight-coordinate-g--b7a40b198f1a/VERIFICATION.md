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
# Verification

The proof is symbolic and applies to every extension degree. The critical finite-field facts used are: a rank-two parity-check matrix of the base code has no zero columns; the dual minimum distance \(6\) forces each of the four projective directions over \(\mathbb F_3\) to occur at most twice; and eight columns force all four multiplicities to equal two. Every pair of distinct directions has nonzero determinant already in \(\mathbb F_3\), hence remains a basis over \(\mathbb F_{3^m}\).

`artifacts/verify.py` provides an independent executable anchor. It constructs a canonical doubled-four-direction matrix, checks that the ternary dual row code has eight nonzero words all of weight \(6\), verifies all six determinants, and then exhaustively enumerates the \(\mathbb F_9\) syndrome space. It finds \(48\) deep syndromes and exactly \(24\) weight-two errors for each, with no weight-one errors. A successful run prints `VERIFY_OK`.

The exhaustive \(\mathbb F_9\) computation is not used as an infinite proof. The all-\(m\) conclusion comes from the projective-line decomposition argument in `RESULT.md`.
