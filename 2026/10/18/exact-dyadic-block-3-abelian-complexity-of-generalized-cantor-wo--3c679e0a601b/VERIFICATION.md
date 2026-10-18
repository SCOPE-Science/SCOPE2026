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

The included `verify_cantor_3abelian.py` constructs the generalized Cantor iterate two independent ways: symbol-by-symbol substitution and a base-\(q\) digit test. It computes all eight length-three contiguous-pattern counts at every start of the next substitution iterate, recovers the number of ones and two-symbol endpoints, and compares against the theorem's explicit complete label set.

Run `python3 verify_cantor_3abelian.py`. Expected result: `VERIFY_OK cases=26`.

Tested are \(q\in\{4,5,6,7,8\}\) and \(1\le k\le6\) with \(q^{k+1}\le200000\), totaling 26 cases. All-depth correctness follows from the factor-block and signature proofs in `RESULT.md`, not from finite sampling. The distinct-class assertion is verified structurally: a 3-Abelian signature uniquely determines the number of ones and two-letter boundaries through shorter-pattern count identities. No independent audit or external certification is claimed.
