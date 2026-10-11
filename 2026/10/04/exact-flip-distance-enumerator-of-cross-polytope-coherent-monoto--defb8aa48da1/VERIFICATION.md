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

Every edge changes one ternary coordinate by one unit, giving the ambient \(\ell_1\) lower bound. If a target-only coordinate exists, or a common support coordinate keeps its sign, that coordinate anchors an ambient geodesic away from the deleted origin. If equal supports have all signs reversed and support size at least two, two supported coordinates can alternate as anchors. Only opposite unit vectors force every two-step ambient geodesic through the deleted origin; bipartiteness excludes distance three and an explicit four-edge detour exists. Removing origin-endpoint pairs from the full ternary-cube product enumerator and moving exactly \(2m\) ordered pairs from degree two to degree four gives the stated polynomial. Differentiation at one gives the Wiener index. The inspected BFS verifier exhausts dimensions \(m=2,3,4,5\) as a consistency check, not as the infinite proof.

## originality

PASS

Black--De Loera's full primary theorem identifies coherent monotone paths with nonzero ternary sign vectors and adjacency with taxicab distance one, and computes the diameter. It does not state the exact all-pairs metric, the unique exceptional pair type, the distance enumerator, or the Wiener index in the inspected text. Resultary's direct exact hit is the audited theorem, with no earlier covering finding.

## value

PASS

Once the coherent-path graph is known, its exact all-pairs metric is the natural next structural invariant. Identifying a single exceptional geodesic type yields a closed distance distribution and Wiener index in every dimension, information not contained in the known diameter alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
