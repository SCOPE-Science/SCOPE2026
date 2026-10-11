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

Run `python3 verify.py` in the directory containing the script and the result. The script requires only Python's standard library and prints `VERIFY_OK` after a complete successful execution.

The checks compare the closed-form three-dimensional survival function with a separate direct polar quadrature of directions in the positive octant; check the endpoints and density; recompute small-segment scaling constants using nested quadrature of spherical cap sections in three, four and five dimensions; check unrestricted spherical-cap tails in dimensions three, four, five and seven; and compare values with normalized Gaussian samples, which have uniform spherical directions. Random tests are deterministic under the fixed seed.

The main proof is analytic. A finite quadrature or random sample cannot prove an identity for every real threshold or every dimension. The standalone checks do not provide an independent external audit. In particular, the historical literature comparison is qualified by potential equivalent treatments of the spherical \(\ell_1\)-norm distribution.
