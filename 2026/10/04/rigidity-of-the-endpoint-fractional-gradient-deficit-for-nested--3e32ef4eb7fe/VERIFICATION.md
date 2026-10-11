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

For a positive finite nested tower, the superlevel sets are exactly the balls in the chain, so symmetric decreasing rearrangement recenters each layer without changing its radius. The primary fractional-gradient source gives, for every ball, the required radial-direction, nonvanishing-away-from-center-and-boundary, and integrability facts. Linearity and the pointwise Euclidean triangle inequality then give the claimed reverse endpoint inequality and the exact integrated triangle-defect identity. If the centers agree, all nonzero ball gradients are positively collinear almost everywhere. If two centers differ, then in dimension at least two the corresponding radial directions fail positive collinearity away from the affine line through the centers, while in dimension one they are opposite on the interval between the centers; in both cases strict triangle inequality holds on a positive-measure set. Thus equality is exactly the common-center case, with the one-layer case vacuous.

## originality

PASS

The complete Stefani preprint was inspected. It states the ball-gradient facts in general and uses them for a specific two-ball translated counterexample at the endpoint, but no finite nested-tower theorem, exact all-layer deficit identity, or common-center equality classification was located. The submitted statement is a natural finite-family rigidity theorem rather than a special case of the printed two-ball example: it classifies all positive nested towers and all equality cases. A targeted Resultary search returned the audited result as the direct hit and no stronger published tower theorem. Because the argument is elementary once the source's ball facts are known, an informal or unindexed observation remains a priority risk; best-of-knowledge originality is therefore bounded to the stated finite-tower classification.

## value

PASS

The source identifies a new endpoint rearrangement failure mechanism; the submitted result turns that mechanism into a complete equality classification on the natural finite nested-ball model class. It separates the exact zero-defect geometry from all nonconcentric cases and supplies the exact deficit functional, which is a structurally useful endpoint statement even though the proof is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
