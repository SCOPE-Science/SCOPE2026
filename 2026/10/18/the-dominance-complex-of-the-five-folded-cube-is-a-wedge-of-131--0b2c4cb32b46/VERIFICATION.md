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
# Reproducible verification

The delivered executable `evidence/verify_dominance.py` and its exact data files `evidence/matching_pairs.tsv` and `evidence/critical_faces.txt` reconstruct and verify the complete finite certificate. Run `python3 evidence/verify_dominance.py` from the extracted package root, using Python 3.10 or later. No network or external package is needed.

The program constructs the degree-five folded-five-cube Cayley graph and checks all strongly regular pair conditions. It enumerates all \(65536\) vertex masks and checks the defining dominance condition in two distinct formulations. Both yield \(53730\) nonempty simplices. It replays \(26799\) disjoint staged matching pairs, checks them byte-for-byte against the accompanying tab-separated certificate, and compares all critical faces to the provided list. The unmatched profile is \((c_0,c_9)=(1,131)\), with zero critical counts in all other dimensions.

For acyclicity, the checker enumerates **all** \(401088\) Hasse covering edges of the nonempty-face poset, orients every edge downward except a matched edge upward, and completes a topological sort visiting all \(53730\) faces. The result proves an acyclic Forman matching, not just homological vanishing. Standard discrete Morse theory then gives the integral wedge-of-spheres homotopy type.

The recorded output is in `evidence/verification_output.txt`. The auxiliary reduced Euler check returns \(-131\), as required by \(131\) nine-dimensional spheres. The finite enumeration does not imply generalizations to other graphs. These are reproducible calculations, not independent external mathematical certification.
