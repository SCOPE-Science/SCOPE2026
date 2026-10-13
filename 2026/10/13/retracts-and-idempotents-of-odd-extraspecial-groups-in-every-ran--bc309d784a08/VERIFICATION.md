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
The dependency-free script `artifacts/verify.py` implements the isotropic and idempotent profiles and **independently** enumerates all admissible generator images of both extraspecial groups of order \(p^3\) for \(p=3,5\). It tests the group relations and idempotency on generators, obtaining \(38\) and \(11\) idempotents at \(p=3\), and \(152\) and \(27\) at \(p=5\), for exponent \(p\) and exponent \(p^2\) respectively.

It separately enumerates ordered pairs of independent orthogonal vectors in \(\mathbf F_p^4\) and divides by \(|\operatorname{GL}_2(\mathbf F_p)|\) to enumerate all isotropic planes and those in the power-map hyperplane, for \(p=3,5\). At \(p=3\) these values are \(40\) and \(4\); the full and hyperplane isotropic-line values are \(40\) and \(13\). The checked group-theoretic rank profiles for \(n=2,p=3\) are \((1,3240,29160)\) and \((1,1053,2916)\).

The recorded direct output ends in `VERIFY_OK`.

These finite tests are a replay, not an infinite proof. The all-primes/all-ranks argument is the central-lift and symplectic-hyperplane classification in `RESULT.md`. Characteristic \(2\) and nonprime field-center analogues are outside the claim.
