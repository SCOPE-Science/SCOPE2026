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
# Reproducible finite verification

All verifiers are pure Python 3 and use only the standard library. Running `verify_morse.py` constructs all permissible vertex sets and the exact matching; it orients every Hasse cover, topologically sorts the directed Hasse graph, computes both integral Morse differentials, and checks a unit minor. Running `verify_mod2.py` independently enumerates all \(2^{20}\) subsets and calculates every mod-two simplicial boundary rank. Running `verify_symmetry.py` independently enumerates all graph automorphisms from adjacency constraints, then calculates exact orientation-signed simplicial Lefschetz numbers.

The recorded outputs are in `verification_outputs.txt`. The computations range over the **entire finite instance** rather than samples. Their conclusions depend on the explicit graph and simplex enumeration logic, matching construction, boundary signs, and standard discrete Morse/Hurewicz/Whitehead theorems. Finite computation does not establish an infinite-graph generalization. External independent mathematical audit has not been performed.
