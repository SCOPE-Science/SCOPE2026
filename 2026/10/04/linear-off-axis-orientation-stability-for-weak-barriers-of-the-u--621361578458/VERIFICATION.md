---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Averaging the weak-barrier projection inequalities over all diagonal sign vectors gives an integral deficit for the Rademacher absolute first moment. The exact second and fourth Rademacher moments imply a pointwise lower bound by one minus the fourth-power coordinate sum, up to the stated dimensional factor. On the off-axis set, convex maximization of the squared coordinate masses gives a uniform gap of twice sin²(beta)cos²(beta). Integration yields the claimed linear estimate. The bundled checker verifies the moment identities and pointwise inequalities on finite grids, while the proof is fully analytic.

## originality

PASS

Kiderlen's current paper establishes all-dimensional weak-barrier stability and explicitly notes near-axis concentration for the cube, but the published quantitative result uses a sublinear deficit power in the general polytope setting; the linear cube estimate previously highlighted in that literature is planar. Resultary returned only the assigned higher-dimensional linear theorem. The audited proof exploits all cube diagonal sign directions simultaneously and is not a direct specialization of the general exponent.

## value

PASS

The source explicitly studies quantitative orientation stability near Jones' bound. A dimension-uniform linear deficit law on the canonical cube family is a natural sharpness boundary and rules out the weaker general exponent as intrinsic to this symmetry class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
