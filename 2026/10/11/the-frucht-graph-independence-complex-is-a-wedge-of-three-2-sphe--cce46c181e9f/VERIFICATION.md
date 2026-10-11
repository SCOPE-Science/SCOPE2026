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

The embedded `verify.py` reconstructs the claim from the explicit graph data.

It checks the following finite facts:

- the graph has \(12\) vertices, \(18\) edges, degree \(3\) at every vertex, is connected, and has one automorphism;
- an explicit relabeling identifies it with the listed Frucht LCF realization;
- the independence complex has exactly \(168\) nonempty faces and face vector \((12,48,73,34,1)\);
- the staged matching has exactly \(82\) pairs and critical faces \(\{8\}\), \(\{5,7,9\}\), \(\{1,9,10\}\), and \(\{0,3,11\}\);
- all \(456\) Hasse covers are reconstructed and the complete matching orientation is acyclic;
- signed boundary ranks over each of \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) are \((11,37,33,1)\), giving Betti vector \((1,0,3,0,0)\).

The proof of the homotopy type uses the standard discrete-Morse consequence that an acyclic matching with one critical \(0\)-cell and three critical \(2\)-cells produces a CW complex with exactly those cells. There are no unverified infinite extrapolations or family-level claims.

The literature search is evidence about coverage, not part of the correctness proof. It cannot rule out every obscure or unindexed source.
