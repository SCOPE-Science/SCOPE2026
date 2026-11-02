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

The theoretical feasibility, orbit-fiber, singleton, generating-function, and asymptotic claims are proved in RESULT.md. Execute `python3 verify.py` using Python 3 and no third-party packages. The checker reconstructs literal four-gram counts of every cyclic binary word with no cyclic `11` at lengths 1 through 20, removes rotational duplicates, checks all fiber formulas, and compares exact profile counts up to length 60. No finite enumeration is treated as an infinite proof.

The proof uses Burnside's lemma and ordinary generating functions, with the cyclic-gap representation handling periodic words and length below four. The scope is exact read counts on a noiseless restricted cyclic channel; no independent validation or experimental sequencing evaluation is asserted.
