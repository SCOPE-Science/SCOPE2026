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

# Verification details
Run `python3 verify.py` beside the supplied `spectrum.tsv` using ordinary Python execution with assertions enabled. The checker reconstructs all \(2048\) rooted Hamiltonian cycles on the five-bit overlap graph and confirms that the alternative four-bit Euler-edge traversal canonicalizes to the same set. Every cyclic word is explicitly checked for its \(32\) distinct length-five windows. The circular scattered-subsequence index of every member is recomputed over all rotations both by a shortest-absent-subsequence dynamic program and by greedy arch counting. Both methods agree everywhere. The checker verifies the principal \(512/1536\) split, the canonical-root joint counts, the complement/reversal orbit counts, and byte-exact equality to `spectrum.tsv`. The certificate is \(73{,}768\) bytes, SHA-256 `23ee91707bce812a56925a20a464ade6ca7e32437b04182f33b031251a97dfaa`.

The underlying graph-circuit bijection and suffix recurrence are set out in `RESULT.md`. The computation is finite and exhaustive for de Bruijn order five; it establishes no infinite-order extrapolation. External independent auditing has not occurred. Full-text comparison with one foundational older paper remains incomplete.
