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

The full published Eq. (1) and region (2) confirm the mismatch. In the sum of the three living-state equations, incidence cancels and the remaining losses are at least natural mortality. This gives the inward living-state face; the deceased-state equation gives its corresponding inward face. For the last coordinate the forcing is a nonnegative linear form under the stated parameter ranges, including the movement probability in [0,1]. Each living-state simplex has support value max(1,lambda) H_j in the relevant direction, and the deceased-state bound is independently attained. Thus on the proposed upper face the derivative is nonpositive; every strictly smaller constant permits an outward derivative at a feasible boundary state. Together with quasipositivity and local smoothness of Eq. (1), this proves compact positive invariance of the product of living-state simplices and coordinate intervals (the record's 'box'). Independent exact arithmetic for the frozen mathematical counterexample gives bracket 3 and live-only bound at most 2 even under the broader independent-coordinate reading of the typeset maximum, so the old face is outward. The unused coordinates can be set within their own bounds, and the stated H_j and L_1 can be realized by the upstream definitions. The sharpness is for independently feasible states, not for trajectories with fixed initial conditions. No unrelated stability theorem was re-audited; the bundled verify.py was inspected, not executed.

## originality

PASS

The supported distinct finding is a correction of a specific published invariance claim, with an outward-boundary counterexample and the least valid constant under its upstream bounds. Maximizing a positive linear form and applying scalar comparison are standard and are not independently credited.

## value

PASS

The erroneous original region is explicitly used as a hypothesis later in the paper. Showing that its face can point outward and replacing it by the least inward cap from the existing upstream bounds repairs a real premise. The significance is limited to the mathematical region and does not validate every downstream conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
