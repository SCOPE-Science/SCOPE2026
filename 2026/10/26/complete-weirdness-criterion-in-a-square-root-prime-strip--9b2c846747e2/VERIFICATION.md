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

# Reproducibility
Execute `python3 verify.py` using only Python's standard library. The verifier enumerates all eligible prime pairs for \(1\le k\le9\), with the finite bound on \(q\) justified by \(a>0\). It independently evaluates the general subset-sum obstruction and the short-gap criterion using exact integers. Recorded output: `VERIFY_OK tested_prime_pairs 48596 weird_witnesses 69`. The proof, rather than this finite check, establishes the unlimited quantifiers. Independent audit is not performed.
