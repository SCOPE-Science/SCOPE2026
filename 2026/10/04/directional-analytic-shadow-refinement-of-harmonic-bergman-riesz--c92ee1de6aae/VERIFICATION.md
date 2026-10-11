---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed \(|\zeta|=1\), the analytic series \(F_\zeta(w)=c+\sum_{n\ge1}(a_n\zeta^n+b_n\bar\zeta^n)w^n\) satisfies \(F_\zeta(r)=f(r\zeta)\) exactly. Radial orthogonality gives its weighted Bergman norm coefficient-by-coefficient, and \(|u+v|^2\le2(|u|^2+|v|^2)\) yields \(\lVert F_\zeta\rVert^2\le2\lVert f\rVert^2-|f(0)|^2\). Applying the established analytic Riesz--Fejer inequality then proves the ray bound; evaluating at \(-r\) gives the opposite ray. Boundary checks recover the analytic case with no factor two and correctly give zero for \(f(z)=z-\bar z\) on the real ray.

## originality

PASS

The closest sources give the analytic weighted Bergman Riesz--Fejer inequality, a recent harmonic theorem with an \(f(0)=0\) hypothesis, and a separate two-diameter Frazer theory. None of the inspected statements gives the direction-dependent analytic shadow \(F_\zeta\), its exact norm, or the center correction \(2\lVert f\rVert^2-|f(0)|^2\). The reduction is simple but is not a special case of a stronger harmonic theorem: it transfers a complex harmonic trace to a single analytic function in a direction-dependent way.

## value

PASS

The exact directional shadow removes a published normalization hypothesis, retains analytic/coanalytic cancellation, and identifies a center-energy correction. Those are structurally meaningful refinements of the Hilbert-case trace inequality, not an arbitrary numerical tweak.

The dated certificate retains the supplied scientific assessment, sources and limitations.
