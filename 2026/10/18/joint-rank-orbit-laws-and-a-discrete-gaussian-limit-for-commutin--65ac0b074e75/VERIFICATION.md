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

## Reproducibility checks

Run `python affine_semilattice_checker.py` with a standard Python 3 interpreter. The checker independently enumerates finite affine maps and tests square-idempotence, commutation by composition, and every product image rank against the theorem's orbit formula. Its prime-field test cases are \((q,n)=(2,1),(3,1),(2,2),(3,2),(2,3)\). Independently the \(n=1\) count for \(k=2,3,4\) is checked for \(q=2,3,5\).

Expected last line: `ALL_AFFINE_CHECKS_PASSED`. Specifically, the exact commuting-pair counts for \((q,n)=(2,1),(3,1),(2,2),(3,2),(2,3)\) are \(7,10,121,460,5233\), respectively. The last tested profile has twenty distinct triple-rank cells.

## Mathematical checks and limits

The infinite-family proof is symbolic and independent of the checker. In particular, the common fixed point is directly constructed and the block decomposition works in every characteristic. The asymptotic limit needs \(q\) and \(k\) held fixed and the residue of \(n\) modulo \(2^k\) held fixed. No numerical experiment can prove that total-variation limit. The checker uses modular prime-field arithmetic and does not claim direct coverage of nonprime prime powers. Independent mathematical audit has not been performed.
