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

The exact proof uses the planar convex Cheeger inner-parallel characterization, the support-halfspace identity for Euclidean ball erosion of an outer parallel body, and the small-inset quadratic area identity of a polygon. Both one-sided second derivatives are computed from the defining equation, so no numerical estimate is used to establish the theorem.

Run `python checks/check_cheeger_cusp.py` with SymPy and mpmath installed. The checker independently verifies the formal implicit differentiation, the exact inset identities for rectangles and equilateral triangles, high-precision boundary asymptotics for several parameter instances, and consistency of the Cheeger-radius equation. It must print `ALL_CHECKS_PASSED`.

The experiments cover examples only. They do not separately verify the published general Cheeger theorem, nor do they constitute an independent mathematical audit. The result assumes exact geometric parameters and exact Cheeger constants; it does not provide statistical or numerical conditioning guarantees.
