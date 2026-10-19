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

# Reproduction and finite proof limits

The code `verify_incidence.cpp` builds an 18-vertex graph over the field of three elements, directly tests every candidate closed-neighborhood signature and visits all 262144 vertex subsets. It generates every permissible delete-one/add-one transition among all valid identifying codes at each cardinality and uses BFS for component counts. For the 1028 minimum codes it also runs BFS from all 1028 roots, giving exact finite within-component eccentricities.

The independent `verify_lcf.py` creates the same 18-vertex graph from its LCF chord sequence, verifies an explicit 18-vertex graph isomorphism, reduces code validity to hitting 18 closed neighborhoods and 153 pairwise symmetric differences, and enumerates all masks. It independently generates and analyzes the size-nine and size-ten exchange graphs, including the minimum-size degree and eccentricity histograms, and confirms identifying-code counts for all larger sizes.

Commands tested:

`c++ -std=c++17 -O2 -Wall -Wextra verify_incidence.cpp -o verify_incidence && ./verify_incidence`

`python3 verify_lcf.py`

The captured outputs `incidence_output.txt` and `lcf_output.txt` end in `VERIFIED`; this only describes program assertions, not independent external review. Correctness of the finite proof relies on the included readable programs, their exhaustive ranges and the transparent neighborhood/signature equivalence; it does not follow merely from these log markers. No theorem is inferred for other graph orders or for stricter token sliding.
