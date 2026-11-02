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

The exact checker `verify.py` enumerates sixteen sign orbits of rational points on a sphere and directly verifies both barycentric signs and supporting-halfspace visibility. Two exact affine stretches preserve the visible count. A rational interior counterexample produces three visible facets. Three reproducible random surface-sampling diagnostics (sphere, nonidentical ellipsoid laws, nonidentical \(\ell_4\)-boundary laws) agree with the analytic masses within a declared tolerance. Run `python3 verify.py`. These tests verify finite and sampled cases only: the universal result is the sign-orbit proof and the convex-boundary lemma in RESULT.md.
