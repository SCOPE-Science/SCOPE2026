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

# Verification of the sharp harmonic \(L^2\) Landau radius

`python3 check_radius.py` executed successfully under Python 3. The checker evaluates four rational partial sums against the closed-form positive limit, bisects the unique radius equation for seven boundary-norm parameters, and verifies the critical extremal's Parseval energy and half/half Wirtinger derivatives numerically using 1500 modes. Additional tests with 500 modes reproduce the limiting vertical-chord sharpness coefficient on three subcritical disks. Representative values are \(R_2=0.1953328537391\ldots\) and \(R_5=0.0717506123169\ldots\).

These finite calculations do not establish any general infinite-series identity, uniqueness, injectivity, or noninjectivity. The proof in `RESULT.md` provides the series identity from differentiated geometric series, the universal Cauchy–Schwarz chord estimate, and the explicit norm-attaining extremal. Optimality invokes Lewy's classical theorem. No external or independent audit has been performed.
