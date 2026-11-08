---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A Markov interval partition with open atoms and endpoint singleton states gives exact preimage edges U->V when V is contained in f(U). Every infinite backward orbit lifts a left-infinite graph walk, whose far past eventually lies in one cyclic SCC; inverse-branch contraction produces the upper bound by the closure K_C of periodic code orbits, and paths from C to V(x) give the opposite inclusion. The finite list of cyclic components makes beta constant on open atoms; a finite-step Hausdorff-hyperspace map is Baire one by continuous Minkowski arcs near each partition point. In the four-branch slope-two example the two distinct open SCCs and the endpoint-preimage bridges give beta=[0,1/2], [0,1], [1/2,1] on left, midpoint and right, hence non-continuity. Independently reconstructed the 9-node preimage graph and verified all open atoms reach P2 while left atoms do not reach right open atoms. This finite check does not establish the general SCC argument.

## originality

PASS

PASS qualified: the beta definition and Baire-class problem were explicitly published by Hantáková–Roth; exact SCC formula and a sharp Baire-one result in the specified expanding finite affine Markov subfamily are not supplied by their Problem 49 or the inspected graph-map alpha-limit work.

## value

PASS

Provides a constructive finite graph algorithm and sharp answer to a natural published backward-attractor regularity question for a mathematically important uniformly expanding Markov class; finite state does not trivialize the endpoint/nontrivial Baire jump.

The dated certificate retains the supplied scientific assessment, sources and limitations.
