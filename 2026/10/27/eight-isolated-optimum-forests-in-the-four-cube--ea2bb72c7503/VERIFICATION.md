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

Use Python 3 with no external dependencies and execute `python3 verify.py` from the directory containing the supplied files.

The checker reconstructs every binary hypercube graph with \(d\in\{1,2,3,4\}\), tests **every** vertex subset by separately implemented depth-first acyclicity and disjoint-set-union cycle detection, enumerates all maximum induced forests, and constructs all optimum-preserving single-vertex exchanges directly. Its reconstruction checks the exact eight antipodal four-cube configurations and their degree multiset \(1^8,4^2\). It also checks the connectivity of the three-cube optimum exchange graph and a concrete parity-crossing exchange path.

Expected outputs include `Q1_EXHAUSTIVE_OK`, `Q2_EXHAUSTIVE_OK`, `Q3_EXHAUSTIVE_OK`, `Q4_EXHAUSTIVE_OK`, and terminal `ALL_VERIFY_OK`. Exhaustion over the stated finite graphs does not support claims about unexamined dimensions. The text proof separately supplies the upper bound, complete equality classification and reconfiguration conclusions.
