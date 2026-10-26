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

# Exact local verification

Execute `python3 mk_kempe_verify.py` using Python 3.10 or later and no third-party packages. The program first constructs the twenty-four edges of the explicitly labeled generalized Petersen graph. It checks that the thirty-three matching masks obtained by first-uncovered-vertex recursion generate precisely the twenty distinct colour-class partitions obtained independently by direct edge-colour assignment. Both recursions are exhaustive: they follow every allowed branch and prune only assignments violating matching or proper-colouring constraints.

For each enumerated state, the program generates all alternating connected components of every bichromatic two-factor and performs all switches. Its separately implemented pairwise state test reconstructs exactly the same twenty-seven undirected edges. A complete component traversal verifies the two component sizes and their degree sequences, while all-pairs breadth-first search establishes component radii and diameters. An embedded explicit sixteen-state bijection checks **all** edges against the Möbius–Kantor graph; bijectivity and the equal edge sets also certify all nonedges. It checks each two-factor's connected-component lengths, yielding the asserted profile multiplicities.

The arguments above certify the finite labeled graph and the exact unoriented/unlabelled colour convention. The code does not attempt to prove any infinite extension, all-graph classification, independent validation, or exhaustive coverage of earlier mathematical literature.
