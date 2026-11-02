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

Run `python verify_rank_one_rb.py` from the same directory as this file. The program builds truncated polynomial quotient multiplication over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_4\). It enumerates distinct nonzero rank-one endomorphisms without assuming the classification and tests the defining Rota–Baxter identity against every ordered pair of basis elements. It compares the observed number with the formula in `RESULT.md` for nine configurations and prints `RANK_ONE_RB_SEGRE_STRATA_OK 9 6212` on success.

Observed configuration totals: \((q,n,\text{maps tested},\text{solutions})=(2,2,9,1),(2,3,49,3),(2,4,225,13),(2,5,961,29),(3,2,32,2),(3,3,338,8),(3,4,3200,50),(4,2,75,3),(4,3,1323,15)\). In total, 6212 distinct maps were checked. The remaining general field-size and dimension claims follow from the written symbolic proof, not from extrapolation of these tests. No independent mathematical audit has been conducted.
