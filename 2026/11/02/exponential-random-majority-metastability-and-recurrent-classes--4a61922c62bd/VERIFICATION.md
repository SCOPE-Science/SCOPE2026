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

## Checks performed

The included `verify.py` was executed using the standard Python interpreter. For each integer \(k\) from \(2\) to \(7\), it reconstructed both trees, counted vertices and edges, verified connectivity and diameter six, and enumerated the exact rational transition matrix of the invariant anchored subsystem. For \(s=k-1\), the only absorbing class found had one state, and the one-step escape rate from the blue-hub region matched \(2^{-k}\). For \(s=k+1\), a closed class of \(2^k\) floating states was found, with each transition probability \(2^{-k}\). In the metastable regime, it also verified the three-round forced-whitening lemma from every compressed initial state. In the metastable regime, it also verified the three-round forced-whitening lemma from every compressed initial state. The script prints `VERIFICATION_OK`.

These checks independently test finite instances; they cannot certify the all-integer theorem. The complete proof is in `RESULT.md`. Source comparison was made against the original arXiv and journal full texts and a distinct deterministic-tree paper, with priority risks stated in `AUDIT.json`.
