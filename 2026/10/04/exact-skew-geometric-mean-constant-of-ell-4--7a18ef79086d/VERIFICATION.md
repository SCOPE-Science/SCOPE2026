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
The proof was checked in four stages: the coordinatewise upper bound; the two-coordinate equality construction; surjectivity of \((u,v)\mapsto(u^2-v^2,2uv)\) onto \(\mathbb R^2\); and the generalized-eigenvalue calculation. The included `verify.py` expands the characteristic polynomial and discriminant as exact integer-coefficient bivariate polynomials and returns `VERIFY_OK` when both identities hold.

The verification establishes the formula for every real \(\ell_4(I)\) with \(|I|\ge2\) and \(lpha,eta>0\). It does not establish a formula for other exponents or complex scalars. Literature coverage remains subject to the indexing limitations stated in the review.
