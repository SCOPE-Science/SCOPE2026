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
# Verification record

The analytic theorem is proved in RESULT.md. Reproduce executable supporting checks with `python verify.py` using Python 3 and SymPy. The delivered program tests symbolic logarithmic derivative and discriminant identities; 48 parameter pairs over both sides of the sharp threshold; three stationary points and unique equal-revenue crossing for rate ratio 10. The program prints its computed fold weights, coexistence weight and stationary prices, and raises an assertion on failure. All these checks ran successfully on the delivered program content.

No finite collection of parameter examples proves the all-parameter statement. Global uniqueness and all boundary assertions follow from exact sign arguments and a strictly increasing envelope-difference function. Historical literature priority is provisional and independent audit has not been performed.
