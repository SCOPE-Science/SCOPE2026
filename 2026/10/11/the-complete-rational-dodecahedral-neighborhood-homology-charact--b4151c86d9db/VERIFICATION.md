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

# Reproducibility and scope

Run `python3 verify_dodeca_neighborhood.py` using Python 3's standard library. The program builds the dodecahedral graph from an explicit generalized-Petersen edge list, verifies exactly 30 edges and 20 cubic vertex neighborhoods, and constructs exactly 20 neighborhood triangles and 60 unique edges. It checks connectedness and the free-face collapses to a graph of first Betti rank 21.

It then enumerates all automorphisms by distance-signature extensions of root/neighbor images, checks the count 120 and closure through displayed generators, and identifies a 60-element rotation subgroup and its central antipodal coset. It computes oriented chain traces using exact signed fixed-face counts for every automorphism, verifies the 21-dimensional first-homology character by the Lefschetz identity, and checks the decomposition of the even and odd parts against the rational character table of \(A_5\). Expected concluding output: `VERIFY_OK`.

These calculations establish an exact **finite** result. They do not independently validate a publication-priority assertion, an integral lattice decomposition, or a general theorem for other graph families.
