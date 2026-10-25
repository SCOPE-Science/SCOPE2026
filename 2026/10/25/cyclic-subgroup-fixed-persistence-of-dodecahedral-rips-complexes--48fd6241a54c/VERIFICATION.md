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

# Exact verification of the cyclic fixed-space classification

The included `check_dodeca_cyclic_fixed.py` is executable with the Python 3 standard library. The checker obtains the graph-distance matrix from the explicit thirty-edge definition of \(GP(10,2)\), enumerates all automorphisms by exhaustive vertex-star extension using distance compatibility, and verifies all seven cyclic-subgroup conjugacy classes. It enumerates every orbit flag complex, proves each reported homotopy type either by elementary free-face collapse or by a verified cross-polytope boundary, and checks the signed degree-one homology continuation between the two reflection-fixed circle stages.

Command: `python3 check_dodeca_cyclic_fixed.py`.

Expected completion markers:

`DODECAHEDRAL_CYCLIC_FIXED_PERSISTENCE_VERIFIED 120 63 378`

`REFLECTION_INTEGRAL_H1_PERSISTENCE_ISOMORPHISM_VERIFIED`

Exact outputs were observed on the delivered source script. The exhaustive calculation establishes a finite classification, while the orbit-simplex lemma establishes that those abstract orbit complexes are exactly the geometric fixed spaces. No claim about unsampled infinite metric families is made, and no independent mathematical audit has been performed.
