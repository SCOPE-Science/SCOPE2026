---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a noncollapsed fixed base, normalization to length one preserves the Euclidean apex-gradient norm. The stated elliptic metric and derivatives give the squared norm in RESULT.md (1). An independent exact reproduction verified the cleared polynomial, the shifted coefficients and all 128 Bernstein coefficients (minima 1718469527/469762048 and 288; replay: /workspace/branches/3dbda92c-2485-4edd-8898-6d479ecc4c55/record4_math_check.py). There is also a direct check: using t^3 >= 3t/25 - 2/125, P0 is bounded below by 6544t^2 - (65512/25)t + 33008/125, which has negative discriminant. In P1/(t+2), extract 1512t(t-4/5)^2; the remaining 729t^4 - (104/5)t^2 - (2592/25)t + 144, plus higher positive terms, is positive both on [0,1] and on [1,infinity). P2 is nonnegative. On a straight apex path, continuity and vanishing at the base line join the two half-plane gradient bounds for both signs. Coincident fixed endpoints give zero identically. Telescoping gives 9/32 for three moves. The derivative at apex (1/2,1/3) independently reproduces the stated radical and relative gap of about 0.003335 to the upper endpoint; it does not identify the exact optimum. The frozen checker was inspected, not executed.

## originality

PASS

The published qualitative Lipschitz result and its much larger constants do not imply the vertex-coordinate upper bound or its near-optimality bracket. The closest indexed sharp constant concerns a different metric and transfers only to weaker vertex-coordinate bounds.

## value

PASS

This is a global quantitative improvement for a motivated point-cloud invariant, valid through degeneracy and orientation changes. It lowers the all-vertex bound from 2 sqrt(3) to 9/32 and places the intrinsic one-vertex coefficient in a bracket of relative width under 0.4 percent. The narrow bracket is supported by a concrete local shape witness rather than merely an incremental upper-bound adjustment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
