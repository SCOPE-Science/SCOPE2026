---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify_petersen_matching.py` using Python 3.9+ and only the standard library. No network, external data files, third-party packages or random seeds are needed. The recorded stdout is `verification-output.txt`.

The checker builds the Petersen graph from two-element subsets of five symbols; enumerates matching faces in two structurally different ways; constructs the complete F2 boundary ranks; generates and checks all 158 sequential toggle pairs and their complete acyclic directed Hasse diagram; reduces all matched signed integral boundary incidences using unit pivots; prints its exact critical-cell masks and seven-by-seven boundary matrix; identifies a unit maximal-rank minor; and independently computes the rational group characters from signed simplicial chain actions and images of boundaries, checking all 120 permutations.

The homotopy implication from primitive integral attaching degrees uses the elementary CW fact that degree vectors classify maps from spheres into a simply connected wedge of two-spheres and that attaching maps with a unit coefficient admit cellular cancellations. No assertion of a general-graph theorem, an equivariant homotopy splitting or an external audit is made.
