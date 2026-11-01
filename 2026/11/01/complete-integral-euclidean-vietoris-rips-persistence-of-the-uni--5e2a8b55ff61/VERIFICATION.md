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

# Reproducibility
Run `python prism_proof.py` in a directory containing `hexprism.py` and `prism_proof.py`; install the version-independent Python dependency recorded in `requirements.txt`. The stage enumerator prints all five integral squared-distance complex face vectors. The core verifier computes the 124-face scale-three simplicial complex from the Euclidean coordinates, checks each free face before its elementary collapse, obtains exactly 29 pairs and 66 remaining cells, and eliminates all 20 spanning-tree-loop generators using 20 occurrence-one relators. Three unattached two-cells remain; the script asserts this and terminates with `VERIFY_OK`. Its actual output is included in `verification_output.txt`.

The Euclidean squared-distance identity, the six tetrahedral lateral squares and their annular retractions, the six forbidden cross-layer antipodal pairs at squared threshold four, and the resulting persistence maps are verified by the written proof. The checker is finite and does not establish novelty or generality beyond this twelve-vertex domain. Independent audit is not performed.
