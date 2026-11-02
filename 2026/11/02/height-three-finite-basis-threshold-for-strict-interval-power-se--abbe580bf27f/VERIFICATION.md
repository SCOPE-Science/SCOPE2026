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
# Reproducibility and limits

Run `python3 verify.py` with Python 3 and the standard library only. Compare stdout byte-for-byte with `verify_output.txt`; successful execution ends in `VERIFY_OK`. The program checks the interval multiplication for associativity in every strict transitive poset admitting a chosen linear extension on at most five vertices; enumerates 5231 labelled strict transitive orders through six vertices and tests the chain-height/R2-walk boundary; and tests the oriented odd-cycle non-homomorphisms and deletion maps for lengths 3 through 17 against chain targets of four, five, and six vertices.

These are finite checks only. The proof for all posets uses strict-chain multiplication, the universal oriented odd-cycle argument and finite relational duality. The passage from finite duality to finite equational basis invokes Wang–Yin–Wang, arXiv:2610.01329v1 (Theorem 1.1 and Lemma 3.3). The explicit unbounded-variable absorption identities use its Theorem 4.1. No independent audit has been performed; historical priority beyond inspected sources is not certified.
