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

# Verification of the exact-degree prescribed-cycle theorem

Execute the embedded standalone checker with `python3 verify.py`; it uses the Python standard library and no external data. It checks exact rational polynomial substitution, interpolation, the identity \(xP+yQ=yH(x^2+y^2)\), strict angular positivity, the exact degree \(2n\), and prescribed hyperbolic Floquet signs. It also evaluates each full angular quadrature independently at 2,048 midpoint nodes and checks agreement with the closed Floquet formula within \(3\cdot10^{-11}\).

The completed replay printed: `PASS: 1414 exact and numerical consistency assertions across all stability patterns for n=1..5`. The five squared-radius test sets were taken from \(1,2,4,7,11\); each of their \(2^n\) sign choices was checked. This finite experiment does not prove the quantification over all \(n\) and real radii. The universal result is established by the divisibility and Floquet-integral arguments in RESULT.md.

Primary scientific limitations: the construction guarantees the desired circles but does not exclude other periodic orbits or control their periods; exact priority relative to the unavailable full text of Christopher (2001) is not independently resolved. Independent audit has not been performed.
