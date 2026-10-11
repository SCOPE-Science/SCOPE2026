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

The source planar graph gives \(e=v_{\mathrm{bd}}+v_{\mathrm{int}}+t-1\) and \(2e=3t+v_{\mathrm{int}}^*+v_{\mathrm{bd}}\), hence \(t+2=v_{\mathrm{bd}}+2v_{\mathrm{int}}-v_{\mathrm{int}}^*\). Retaining size-two stretches, each such stretch contributes one full shared side and no subdividing vertex; a size-\(s\ge3\) stretch contributes \(s-2\) subdividing vertices. Equating the two exact counts of total nonboundary tile-side incidences yields \(q=v_{\mathrm{bd}}-3+3(v_{\mathrm{int}}-v_{\mathrm{int}}^*)+E\). The inequalities and equality criterion follow because both defect terms are nonnegative.

## originality

PASS

Kupavskii-Pach-Tardos introduce the same planar graph, subdividing vertices and stretches, but their theorem assumes for contradiction that no full side is shared, so every stretch has size at least three, and concludes only existence of a shared side for polygons with more than three sides. The inspected full proof does not state a count for size-two stretches, the sharp \(k-3\) lower bound, the exact defect decomposition, or its equality characterization. Current published-finding searches found no earlier quantitative identity under shared-side, hanging-node, T-junction or non-edge-to-edge aliases.

## value

PASS

The identity upgrades a qualitative existence theorem to a sharp linear lower bound with a complete nonnegative defect decomposition and equality criterion for a natural tiling invariant. That is a meaningful structural refinement rather than an arbitrary finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
