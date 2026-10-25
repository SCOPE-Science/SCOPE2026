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

Exact analytical checks: the anchored Euclidean Jacobian is \(1/\sqrt{m+2}\); two independent conditional integrals give the hub second moment and leaf noise variance; orthogonal invariant-subspace projection gives the covariance spectrum. A fully factored rational difference determines the one finite crossing; the limiting exponential hub gap yields the asymptotic rates.

The included self-contained `check.py` was run against its real saved bytes and reported: `VERIFY_OK quadrature=14 volume_hulls=2 exact_sign_identities=99 mode_crossing=2,3,4+`. Hull integration tests cover only \(m=2,3\); these finite tests are not an infinite proof. Any independent mathematical or bibliographic verification remains unperformed.
