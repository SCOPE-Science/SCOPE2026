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

Execute the standalone standard-library checker with `python checker.py`. It exhaustively evaluates all \(2^{1+n+n^2}\) valuations of the one-letter full height-two tree for each \(n=1,2,3\), comparing direct count semantics to the exact rational binomial formula. A distinct block-enumeration method computes the complement polynomial and matches the formula for \(1\le n\le12\). The checker verifies the surrogate substitution and prints `COUNTING_MODAL_SURROGATE_MAX_GAP_OK` on success.

The proof for every positive branching factor is in `RESULT.md`, based on independence of disjoint subtrees and the central-binomial estimate. Finite tests are only consistency checks. The probability-model conventions and iterated-limit definition are those of arXiv:2610.26187v1. There is no machine-checked infinite proof or independent audit.
