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

Run `python verify.py` from the directory containing the files, after installing the dependency declared in `requirements.txt`.

The checker carries out two exact symbolic rational-function cancellations and rebuilds five finite primitive strongly regular graphs from first principles. In each example it validates the adjacency identity, the three idempotents and their orthogonality, the full Schur-square matrix, and strict positivity and full rank by exact arithmetic. The resulting terminal line is:

`VERIFY_OK symbolic_identities=2 exact_SRG_graphs=5 full_rank_checks=5`

The full theorem is not inferred from these finite examples. Its universal steps are the strongly regular projection calculation, the integrality/conference-spectrum dichotomy, and the complementary-graph positivity argument. The proof does not establish positive definiteness for other classes of distance-regular graphs, nor for arbitrary time-sampling distributions.
