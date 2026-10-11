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

For every rotation and translation, rotation-invariance of the Euclidean ball gives \(\rho(T+rB_2^d)+w=\rho T+w+rB_2^d\). By definition of erosion this is contained in a convex host \(K\) exactly when \(\rho T+w\subset K\ominus rB_2^d\). The eroded host is a nonempty compact convex set whenever the thickened host is Kakeya. Thus the parameter spaces of admissible thickened and unthickened placements are identical and every continuous path transfers both ways. Janzer's segment theorem plus similarity yields the capsule case. The width comparison correctly excludes both segments and balls for nondegenerate \(L\) and \(r>0\).

## originality

PASS

Janzer proves universal path-rotatability for segments and explicitly asks in Question 5.2 for non-segment, non-ball examples in dimension at least three. No inspected source or Resultary hit supplies the ball-thickening inheritance lemma or the capsule consequence. The new exact erosion equivalence transfers the complete placement space, not merely existence at each orientation.

## value

PASS

The inheritance lemma is a clean structural mechanism and its capsule specialization directly resolves an explicit published open question in every requested dimension. The contribution is mathematically motivated even though the transfer argument is short.

The dated certificate retains the supplied scientific assessment, sources and limitations.
