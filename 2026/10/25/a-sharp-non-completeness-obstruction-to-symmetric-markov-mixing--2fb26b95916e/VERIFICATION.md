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

The included `verify.py` is standalone Python 3 (standard library). Execute `python3 verify.py` from the package folder; exact output is `EXACT_REPLAY_OK 224`. This checks exact rational symmetry, row sums, nonnegativity, each claimed invariant vector and its eigenvalue, for all parameter pairs with 3 <= n <= 30 and 1 <= k <= floor(n/2). The proof of the universal lower bound and the equality necessity is analytic in RESULT.md and independent of finite samples. The code does not verify other graph topologies by enumeration, nor does it certify uniqueness in the literature.
