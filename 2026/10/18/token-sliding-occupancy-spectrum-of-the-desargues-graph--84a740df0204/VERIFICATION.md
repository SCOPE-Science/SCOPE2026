---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction instructions

Run `python3 verify.py` with the Python 3 standard library. The program checks a vertex bijection from the disjoint-pair presentation to \(GP(10,3)\), enumerates all independent subsets at occupancies one through ten, constructs the slide graph by host-edge toggles and cross-checks the edge count by all unordered state pairs. It checks component orders and small-component shapes. It then computes exact eccentricities by breadth-first search from every state of each nonsingleton component, and asserts all reported radii and diameters, including occupancies one, two, and three. `ALL_CHECKS_OK` is printed after all assertions succeed. This is an exact finite computation for this graph, not a general theorem for other hosts.
