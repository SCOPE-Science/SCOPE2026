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

The mathematical proof is contained in `RESULT.md`. The crucial universal steps are an exact separation of Fourier positivity, a regular-polygon supporting-functional lemma for both order parities, and a deficit identity that makes every equality and stability condition explicit.

`verify.py` uses only Python's standard library and checks twelve finite product groups, their proposed extreme points, random convex mixtures of optimizers, and random feasible perturbations. It completed 1,886 tests successfully. All finite-group character values are evaluated directly, including positivity at every character in the tested groups. These floating-point computations are independent corroboration, not an exact certificate for an infinite parameter family; the analytic polygon proof supplies the latter.

The classification requires coordinate orders at least three and support **contained in**, rather than equal to, the coordinate star. Fourier-zero cardinalities apply only to maximizing functions. The sharp stability constants apply only if at least one coordinate order is odd; no all-even transverse stability rate is asserted.
