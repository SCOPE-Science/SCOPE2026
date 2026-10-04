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

The infinite theorem is established by the symbolic proof in `RESULT.md`. No finite enumeration is used to infer the theorem.

The standalone script `artifacts/verify.py` performs two independent numerical checks:

1. For every \(5\le N\le1000\), it evaluates the stated closed form, confirms sampled nonnegativity of the factorized extremizer, checks that the two predicted adjacent samples are zeros, and verifies the equality criterion with \(\sqrt2\).
2. For every \(5\le N\le90\), it independently solves the two-variable sampled linear program by enumerating intersections of pairs of active grid constraints and testing each candidate against every grid inequality. The best objective agrees with the theorem to the stated floating-point tolerance.

The script uses standard double-precision trigonometric evaluation only. Accordingly, its role is regression and finite corroboration; the exact all-\(N\) certification is the algebraic argument, including the exact sign and factorization identities.
