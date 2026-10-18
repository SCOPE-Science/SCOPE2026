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

# Reproduction and limits

Execute `python3 verify_hamming_open.py` using Python 3 standard libraries. The script enumerates all faces from each common-neighbor simplex; independently counts faces in every dimension, verifies that distinct maximal neighborhoods share at most two vertices, computes Euler characteristic, and eliminates integer triangle relations by explicit unimodular operations. Tests cover seven cases, including `(3,3)` with second Betti number 56, `(2,4)` with 55, and `(3,4)` with 703. The integer checks also recover three four-letter cases with the prescribed mod-two first-homology torsion.

These finite tests do not prove the theorem for all dimensions. That conclusion follows from the overlap lemma, descending-order elementary simplicial collapse, exact all-parameter Euler count, and published parity-kernel fundamental-group results described in RESULT.md. No independent scientific audit was carried out.
