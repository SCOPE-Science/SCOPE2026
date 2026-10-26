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

# Verification notes

The infinite proof uses balanced-ternary uniqueness, the least 3-adic exponent of summands, and the two mod-three residue patterns of primitive triples. The standalone `verify.py` enumerates unordered triples for \(J=3,4,5,7,11\) digits, removing every triple with a pair summing to zero. It checks the bound of three and the complete set \(\{\pm5\cdot3^k,\pm7\cdot3^k:0\le k\le J-3\}\) of finite-truncation threefold targets, rather than just testing a few examples. The observed execution was `VERIFY_OK finite_depths=3,4,5,7,11 max_count=3 exact_triple_fibers=36`.

Finite tests do not certify infinite conclusions, literature priority or independence. No independent scientific audit has been performed.
