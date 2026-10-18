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

# Verification methods and boundaries

Run `python3 verify_cactus.py` with Python 3.8 or later; no nonstandard packages are required.

The checker enumerates all orientations for individual cycles, trees, two triangles sharing a vertex, dumbbell cacti, and a triangle-square cactus. It computes indegree-parity signatures, checks that the directed-cycle count is constant in each signature fibre, verifies that every fibre contains exactly \(2^c\) orientations, and compares the observed distribution with the polynomial formula coefficient by coefficient.

A separate checker lists every connected labeled simple graph on one through five vertices (772 cases), discovers its undirected simple cycles, classifies it as a cactus if no edge occurs in two cycles, and tests whether every parity fibre is homogeneous in directed-cycle existence. It verifies the claimed equivalence for 399 cacti and 373 non-cacti. The general argument is given in RESULT.md and does not depend on these enumerations.

The proof uses two standard facts that are reconstructed there: the rank of the binary incidence matrix of a connected graph and the theta characterization of noncactus graphs. No finite enumeration is asserted to prove the infinite case. No independent scientific audit has been performed.
