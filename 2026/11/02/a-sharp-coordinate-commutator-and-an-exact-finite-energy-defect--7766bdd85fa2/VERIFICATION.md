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

# Verification scope

The proof is analytic. The included standard-library-only `checker.py` independently reconstructs finite beta-binomial identities and compares the closed traces with rational sums, checks all small diagonal weights, verifies the maximizing two levels, and samples the asymptotic constant. It passed 3,073 finite assertions when run with Python 3. The Wallis, weakly-null compactness, random-walk and infinite-asymptotic steps are justified in RESULT.md; finite computations are not presented as an infinite certificate.

No external or independent audit has been performed. No formal proof assistant was used.
