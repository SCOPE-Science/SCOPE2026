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

# Exact verification instructions

Run `python3 verify.py` in a directory containing the supplied standalone program. It uses only the Python standard library.

The program generates all \(210\) four-subsets of the ten Petersen vertices; tests induced connectedness directly from disjointness of the underlying two-subsets; retains the complements of precisely \(140\) disconnected quadruples; and generates all \(766\) faces including the empty face. It then performs the lexicographic ten-stage element matching on nonempty faces, verifying \(369\) disjoint pairs and unmatched face counts of one zero-face and \(26\) five-faces.

For the entire nonempty face Hasse graph, orient matched covers upward and unmatched covers downward; an explicit topological sort must process all \(765\) nodes. This is a complete finite acyclicity certificate, not a randomized test or sampled gradient-path enumeration. Forman's theorem then gives the stated wedge homotopy type.

Separately, explicit mod-two boundary matrices of dimensions one through five have ranks \((9,36,84,126,114)\). The group character calculation visits all \(120\) permutations, computes orientation signs on all invariant faces, checks the class traces \((26,6,-2,2,0,0,1)\), and decomposes the character by exact rational inner products, giving multiplicities \((1,2,1,2,0,0,0)\).

The checker prints two lines starting `VERIFY_OK` when all required assertions succeed. The finite proof is exhaustive for this exact graph; it is not evidence for a theorem about arbitrary graph families. Only self-review was performed; independent audit remains not performed.
