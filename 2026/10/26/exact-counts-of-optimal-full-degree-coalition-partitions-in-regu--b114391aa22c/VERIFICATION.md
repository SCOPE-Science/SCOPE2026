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

A standalone standard-library verifier `verify.py` independently checks the original neighbor-count definition of full-degree k-domination and enumerates every unlabeled partition of all labeled k-regular graphs on 3–6 vertices, with k at least two. For named graphs through eight vertices, it checks the exact maximum and connected-bipartite four-partition count. It additionally generates global bipartitions and four-block splits for graphs with 2, 3 and 4 connected components, deduplicating by canonical block sets instead of applying the claimed correction in its generating algorithm. The resulting disconnected counts match 97, 3838, 129004, and 1921 in the recorded examples.

Run `python verify.py` from the directory containing the script. The expected output is included in `verification_output.txt`. Finite verification is corroborative only: the infinite proof is in RESULT.md. No independent external audit has been performed.
