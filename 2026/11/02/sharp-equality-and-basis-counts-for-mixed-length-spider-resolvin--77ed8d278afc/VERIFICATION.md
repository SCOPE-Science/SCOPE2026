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

For vertex domination each terminal long-arm vertex forces one selected member of {u_i,v_i}; short leaves force either all p leaves without root or root with at least p-1 leaves. Root domination excludes all-terminal choices when p=0. Radial edge signatures force all but at most one arm marked, with the exterior-edge domination condition resolving the p=1 exception. The explicit selected marker codes distinguish vertices/edges. Independent BFS edge/vertex code enumeration exactly matched both optimum cardinalities and both basis counts for twelve (p,q) pairs, p=0..3, q=2..4, including the all-short-absent boundary.

## originality

PASS

The source 2022 paper states the general tree inequality and asks to characterize equality; neither the general inequality nor path/star examples implies the complete mixed-length radius-two classification or the number of all minimum labeled bases. This is a best-knowledge original exact family answer, not an assertion that the two parameters or graph algorithms were first introduced here.

## value

PASS

The minimal parameters and complete basis counts answer a specifically published open equality question in a natural two-arm-length tree family; the gap changes at the first short arm. Complete extremizer counts are independently useful structural graph data, not an arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
