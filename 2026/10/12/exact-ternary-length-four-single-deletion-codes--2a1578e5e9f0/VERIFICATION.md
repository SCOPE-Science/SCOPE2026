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
# Verification

Run `python verify.py`. The verifier uses only the Python standard library. It reconstructs all 81 ternary length-four words and their one-deletion shadows.

It performs two exhaustive exact searches: Bron--Kerbosch enumeration of every maximal compatibility clique, and a separate increasing-vertex recursion that counts size-11 and size-12 cliques directly. Expected outputs include `maximum 11`, `maximum_codes 6`, `count11 6`, and `count12 0`.

The verifier then checks the nine-word common core, the six residual words, the residual compatibility six-cycle, all 12 simultaneous-alphabet-permutation/reversal symmetries, one orbit of size 6, stabilizer order 2, and census SHA-256 `0fdfab77f115f24f9c37c8cf153819f8d380b7e269ae7be3a039a018133a0a16`.

The computation is finite and exhaustive. No conclusion is drawn from a timeout, partial enumeration, randomized search, or numerical tolerance. The literature comparison is not an independent audit and does not exclude inaccessible or unindexed prior work.
