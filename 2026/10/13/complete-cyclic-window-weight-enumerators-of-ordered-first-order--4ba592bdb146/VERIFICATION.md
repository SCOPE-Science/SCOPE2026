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

# Reproducing the finite checks

Execute `python3 verify.py` with Python 3.10 or later. It computes the exact predicted coefficient map from the stated formula, independently enumerates all affine binary truth tables in increasing integer order for every \(1\le m\le8\), and counts all cyclic read windows for each \(1\le b\le2^m\). It also verifies the cardinality identity \(W_{m,b}(1)=2^{m+1}\), the minimum nonzero weight, and the symbol-pair special case.

Expected terminal output ends with `VERIFY_OK all b for m 1..8` and `CONSISTENCY_OK cardinality/minimum-distance/pair-spectrum m=1..8`. These finite checks are corroborative only; infinitely many cases follow from the explicit binary-carry and zero-run argument given in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
