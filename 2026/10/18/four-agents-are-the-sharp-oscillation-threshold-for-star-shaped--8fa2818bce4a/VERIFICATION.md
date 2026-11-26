---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On a finite labeled cycle the nested convex hulls are equal. A vertex of this hull can be an updated opinion only if all averaged opinions, including the updating label's old opinion, were at that vertex. Each vertex's occupancy set decreases by inclusion and is periodic, so is constant. With at most three labels, either all are fixed or just one can move inside a segment with one label fixed at each end. As its normalized coordinate increases it can only drop left-end trust and gain right-end trust. Its average increases with its own coordinate and weakly increases under both trust changes. Thus a strict displacement cannot return, even at a discontinuity. I independently recomputed the witness using squared distances and the integer ray equation 5|dy|=-dx for dx<0: the moving neighborhoods are {x,c} and {x,a,b,c}, all three anchors trust only themselves in both states, and the nonidentical configurations return in two steps.

## originality

PASS

The four-agent witness is already Example 3 of Zabarianska–Proskurnikov (2024) and the record credits it. The supported distinct claim is the dimension-independent lower bound for the homogeneous star-shaped model without pinned agents; the inspected earlier convergence and oscillation results do not provide that lower bound under its hypotheses.

## value

PASS

The lower bound resolves whether the published four-agent construction needs four ordinary agents at all. The persistent extreme-label argument is structural and works despite discontinuous radial boundaries and arbitrary ambient dimension; it is not only a check of special parameter examples or two-cycles. The result supplies an exact population threshold in the stated setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
