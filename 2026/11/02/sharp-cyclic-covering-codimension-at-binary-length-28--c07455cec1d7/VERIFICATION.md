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

# Verification of the exact cyclic-covering certificate

Run `python3 verify.py` using an ordinary Python interpreter. The self-contained verifier uses integer arithmetic only and has no external dependencies. Its successful output begins `CYCLICALLY_COVERING_28_VERIFY_OK`.

The program verifies \(P=(t^3+t+1)^3\), polynomial divisibility by \(t^{28}+1\), rank four of the quotient checks and the corresponding length-\(28\) rows, kernel cardinality \(32\), and the complete partition of \(\mathbb F_2^9\) into exactly \(22\) cyclic orbits. It also confirms the recorded orbit representatives, lengths and first kernel witnesses, checks compatibility of all \(28\) standard input coordinates with cyclic shift, and checks the coverage condition for every quotient state.

The finite state computation is exhaustive because the quotient has exactly \(512\) states and the polynomial quotient is surjective; it is **not** a brute-force enumeration of the original \(2^{28}\) vectors. The transfer from quotient to original vectors and the dimension argument are proved in `RESULT.md`. The upper bound follows from a standard subspace union-counting inequality. Independent review has not been performed.
