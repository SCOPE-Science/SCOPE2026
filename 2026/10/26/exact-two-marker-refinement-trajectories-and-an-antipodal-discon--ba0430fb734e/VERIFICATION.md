---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A depth-r initially coloured walk tree determines the retained-colour refinement class and detects each marker exactly when its distance is at most r. With neither visible the trees coincide; with one visible reflect around that marker; with both visible, distinct vertices at equal distances to both would satisfy y=-x and y=2t-x modulo n, so this can happen only in the antipodal case and then precisely within a colour-preserving reflection orbit. For cap c=r+1 in the nonantipodal case, c<t leaves the two neighbours of 0 unresolved, and if c>=t but 2c<n-t, the consecutive positions c,c+1 on the long arc are both capped in both coordinates. Conversely both caps can hold at at most one long-arc position if 2c>=n-t, and a one-cap pair has at most one candidate, since the candidate in the direction of the other marker is at distance at most |j-t|<c when j<c is the exact distance. The antipodal orbit has index j and the capped pairs of (j,t-j) distinguish all orbits iff 2c>=t. A stable partition remains stable thereafter, so these are the exact first stable rounds, including the initially stable C3 and C4 cases. An independently written synchronous refinement check passed 2,499 configurations, 3<=n<=100, and 74,650 round comparisons, including first stability and terminal cells; the unbounded result follows from the proof, not the enumeration. The supplied verifier was inspected, not executed.

## originality

PASS

Supported as a distinct exact two-marker trajectory and stopping-depth theorem for simple cycles, not as priority for prime-order discreteness, the notion of a resolving set, or the general type of two-distance formula.

## value

PASS

Two-marker initialization is a natural finite-round refinement benchmark. The full partition law permits predicting discrimination at every round; the competing separation and long-arc constraints and the sharp antipodal drop are not predicted by eventual discreteness or stable orbit results alone. This gives a useful exact test case for analysis of individualization and refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
