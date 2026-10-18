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

# Reproducible checks and limits

Execute `python verify_matching_cycles.py` followed by `python verify_first_orbit_gap.py` with Python 3 and NetworkX 3 installed. The first enumerates alternative perfect matchings with one fixed matching for orders four, six, and eight, compares incidence graphs by an independent side-preserving graph-isomorphism algorithm, and verifies identical first-round joint atomic relation counts. It also checks the sharp distinct-part inequality through two hundred elements. The second constructs the ten-element cycle-pair witness, enumerates all side-preserving automorphisms and derives the two exact edge-orbit sizes. See `verification_output.txt` for the actually observed output. Both programs were executed successfully before packaging.

The infinite logical equivalence proof is mathematical: the \(C^2\) formulas for matching class sizes and singleton intersections and the uniform refinement invariant are independent of finite experiments. The all-order orbit and extremum statements follow from cycle decomposition and integer-partition arithmetic. Independent scientific review and publication-priority certification have not been performed.
