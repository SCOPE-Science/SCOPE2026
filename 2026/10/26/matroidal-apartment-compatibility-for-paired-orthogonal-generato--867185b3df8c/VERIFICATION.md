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
# Computational verification and limitations

Execute `python verify.py` using standard Python 3. The program implements rational row reduction, computes nullspaces for four explicit alternating matrices, enumerates all coordinate-index subsets, and compares exact column ranks with the predicted independent-set profiles and even rank cutoff. The tested tuples are printed on success with `VERIFY_OK`. Finite examples cannot prove the all-rank apartment equivalence or establish historical novelty; the proof is the bilinear-algebra argument in RESULT.md. No independent audit has been performed.
