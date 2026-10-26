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

# Reproduction and proof boundaries

Run `python3 verify.py` from the directory containing the standalone verifier. Its only dependencies are Python's standard library. Its stdout is supplied as `verify_output.txt`.

The verifier constructs both cliques and the interlayer matching directly, enumerates all deletion sets of size strictly below the graph's degree for clique-prism sizes three through six, independently computes which index labels are touched, and compares those counts with the inclusion-exclusion formula and the closed-form minimum multiplicities. The number of such enumerated sets is 459723. It also exhausts all ternary vertex assignments for each deletion set below the degree at prism sizes three and four, giving 743 direct graph-feasibility instances and checking the equivalence between total Roman weight four and a surviving dominating edge.

The finite comparisons are not a proof for arbitrary clique size. The unrestricted proof is the structural characterization of feasible weight-four assignments, the exact index-cover reduction, inclusion-exclusion on untouched indices, and the exhaustive structural classification of minimal covers. For failure sizes at least the original vertex degree, isolation can occur and the formula is not claimed to count admissible sets. Independent validation has not been performed.
