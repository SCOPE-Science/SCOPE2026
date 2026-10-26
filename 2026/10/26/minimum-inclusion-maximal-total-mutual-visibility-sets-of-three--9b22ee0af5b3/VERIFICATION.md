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

Execute `python verify.py` using Python 3. The checker independently compares the shortest-geodesic original predicate with the Hamming distance-two criterion for all vertex subsets of the binary three-cube and enumerates all size-minimum independent dominating sets for six Hamming products. It separately computes the restricted Stirling counting formula. `verification_output.txt` gives the observed output from an actual execution of the packaged script. The full cardinality and family classification for arbitrary factor sizes follow from the proof; no extrapolation from finite checks is assumed.

Self-review completed; independent mathematical validation not performed. Bibliographic completeness cannot be certified by targeted searches.
