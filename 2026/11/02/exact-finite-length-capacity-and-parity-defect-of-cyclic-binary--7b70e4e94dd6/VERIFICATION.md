---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Define a_i=x_{2i}, b_i=x_{2i+1}; y_i=a_i+a_{i+1}+b_i with cyclic indices and counted multiplicity at m=1. Determinized subset-state transition matrix T has eigenvalues 0,2±sqrt2. A 0 or 3 label synchronizes closed paths; without them only the two even-length alternating 1/2 words have an extra singleton-state closed path. Therefore N_m=tr(T^m)−1−(−1)^m, not uncorrected trace. Independent enumeration of all 4^m binary sources for 1≤m≤9 recovered exact outputs and parity correction.

## originality

PASS

Chee et al. already provide the binary (3,2) automaton and the asymptotic rate; the asserted new fact is the exact marked cyclic-output image cardinality and its exceptional two alternating vectors for even period.

## value

PASS

Cyclic read capacity is an intrinsic finite-block coding invariant. The explicit count separates a closed-path presentation from distinct read vectors and isolates a genuine parity defect, relevant when designing exact short cyclic read codes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
