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

The arbitrary-dimensional result is proved analytically in `RESULT.md`.

The critical proof steps are:

1. For \(A=\operatorname{aff}C=a+L\), every relative-interior point has normal cone \(L^\perp\).
2. Every relative-boundary point of a non-affine closed convex set has a nonzero relative supporting normal in \(L\).
3. A radius-\(r\) supporting normal is orthogonal to the entire relative-interior truncated normal set, producing distance exactly \(r\).
4. Relative interior is dense, so this fixed separation persists while base points converge.
5. Affine sets have a constant normal cone and therefore a constant truncated map.

`artifacts/verify_boundary_examples.py` checks exact interval, disk, segment, and affine-line instances. Those checks are illustrative only; no finite experiment is used as an infinite proof.
