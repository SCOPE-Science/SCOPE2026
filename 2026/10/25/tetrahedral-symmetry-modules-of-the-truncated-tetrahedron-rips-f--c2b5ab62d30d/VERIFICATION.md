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

# Verification

Use `python3 verify_tetrahedral_equivariance.py` with a standard Python 3 interpreter. No network access, source downloads, third-party libraries, or separate certificate files are required. The script independently reconstructs the graph on twelve ordered distinct label pairs and checks that every vertex has graph degree three. It computes all 144 ordered pair distances and their unsigned distribution: eighteen graph edges, twenty-four distance-two pairs, twenty-four distance-three pairs.

It loops over every nonempty subset of the twelve vertices, not a sample, and tests each pair against graph distance at thresholds one and two. The resulting complete face vectors, by face cardinality, are \((12,18,4)\) and \((12,42,48,12)\). The script builds every simplicial boundary column from all codimension-one faces and performs exact bitwise elimination over \(\mathbb F_2\). The ranks are \((11,4)\) at threshold one and \((11,31,12)\) at threshold two. The mathematical proof explains why they determine the corresponding rational ranks; the code alone does not claim the integral Smith normal form.

The script then enumerates every permutation in \(S_4\), verifies equality of signed Lefschetz numbers within each conjugacy class, and checks their ordered vectors \((-2,2,2,1,0)\) and \((6,2,2,3,0)\). It computes the homology characters using the rational rank information, performs the exact \(1/24\)-weighted irreducible character inner products, and checks dimensions one and two for the full and rotation-subgroup invariant spaces. The expected success line is `TETRAHEDRAL_EQUIVARIANT_CHARACTER_OK`. These steps check the finite mathematical certificate; independent review of the proof and mathematical originality has not occurred.
