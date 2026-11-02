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

The exact proof is in `RESULT.md`. Run `python3 verify.py` from this directory using Python 3 standard library only. `checks.txt` is the observed output from the included checker, not evidence of infinite exhaustiveness.

The implementation evaluates field arithmetic over the prime fields of sizes 2 and 3, and over the genuine degree-two extension field with four elements; it evaluates original full three-tensor AYBE products directly rather than assuming the reduced equations. Every nonzero ordered factor pair was checked for \(n=2\), field orders 2, 3, and 4. For \(n=3\), field order 2, reduced conditions were checked for every nonzero factor pair and the original tensor equation was additionally checked for all admitted pairs. Exact total counts and rank distributions matched the proved polynomial.

The resulting output concludes `DECOMPOSABLE_AYBE_ALL_DIRECT_CHECKS_OK`. The checker and observations corroborate, but do not replace, the arbitrary-field classification and finite-field counting proof. Independent audit has not been performed.
