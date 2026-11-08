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

# Verification of the two-marker Abelian-square limit

`verify.py` performs independent literal-factor enumeration for every two-one binary word of lengths 2 through 33, verifies the exact zero-only and two-marker component formulas, and cross-checks exact finite sums using the independent one-marker-in-each-half double count. It also tests 2,500 longer randomly generated words and the diagonal-difference count identity. Successful execution prints `VERIFY_OK`.

`moment_certificate.py` integrates the constant, strip-area and squared-area polynomials over the six exact rational regions of half the simplex, using only the standard library's exact fractions. Successful execution prints `MOMENT_VERIFY_OK 1/48 1/3456`. The machine calculation confirms the stated rational integrations but the theoretical conclusion also requires the finite factor classification, a uniform linear lattice/area error, and convergence of uniform weak compositions to uniform simplex area measure.

The assertions are conditional on two ones, counted by distinct literal factors. There is no claim of formal proof certification or independent mathematical audit. No finite test establishes the infinite limit by itself.
