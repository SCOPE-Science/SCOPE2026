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

The proof is analytic and appears in RESULT.md, Steps 1–5. The included standard-library checker `verify_projection.py` is a diagnostic aid, not a formal proof and not an independent verification. The checker was run successfully using `python3 verify_projection.py`. Its deterministic normal draws and quadrature produced an equilateral probability of approximately \(0.470339624536\) and passed 2,022 direct comparisons/inequalities plus 125,000 random projected-triangle samples.

The core logical checks are the exact equivalence of the projected inner-product sign with a spherical quadratic inequality; the two independent integral representations; strict positivity of derivatives of the elementary integrand; the strict Jensen equality classification; the exact polynomial certificate separating nonacute source triangles; and realizability of the normalized two-dimensional singular-value map by a three-dimensional orthogonal projection.

The numerical tests range over finitely many angles and shapes, and therefore are not exhaustive. The bibliography does not constitute an independent historical-priority audit. No independent scientific audit is claimed.
