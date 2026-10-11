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

The included `verify.py` reconstructs each closed-neighborhood complex at parameters \(q=2,3,4\), sums the signed fixed-face Lefschetz trace for all coordinate permutations and their interchanges, and compares against both formulas. Running `python3 verify.py` emits `VERIFY_OK` after \(1232\) comparisons. The proof of the arbitrary-parameter claim is the equivariant relative-chain decomposition in `RESULT.md`; the finite checks are not a substitute for that proof. No independent audit has been performed.
