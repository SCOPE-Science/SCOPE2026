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

# Verification and scope

The `verify.py` script runs on Python 3 without external packages. It uses the exponential memoryless property to enumerate the exact first-arrival decomposition for finite cyclic graphs and evaluates the proposed infinite-length formula independently by quadrature in beta-quantile coordinates. Its tests include a twenty-vertex cycle with one length-ten chord, four rates, the special analytic constant \(-e^{-4}\), the sign transition, and both extreme-rate limiting values.

The mathematical proof in `RESULT.md` supplies the infinite-graph cavity identities, cancellation of the bridge and ray contributions, factorial localization of influence, and strict stochastic-order proof. Finite recursion cannot by itself establish any infinite-system limit, and numerical integration does not certify uniqueness of a root; those conclusions rest on the explicit arguments. The full text of some relevant older publications could not be inspected, so the originality assessment is qualified by specific bibliographic uncertainty. Independent validation is not asserted.
