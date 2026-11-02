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
# Reproducibility and limitations

Run `python3 verify.py` using Python 3 with only its standard library. The script independently counts every diagram pair \(\mu\subset\lambda\) at distance two for all positive \(u,v\le4\) and colengths \(0\le n\le13\) (224 exact coefficient comparisons). It also checks all partitions of sizes 2 through 18 against the three-case deletion statistic, checks the explicit \((u,v)=(2,2)\) first eleven coefficients and the \((1,1)\) reduced node, and tests branch-exchange symmetry through coefficient index 31. Successful execution ends in `VERIFY_OK`.

The arbitrary-parameter proof is the partition decomposition and exact boundary-event identity in `RESULT.md`. Finite tests cannot prove a universal theorem; nor do these tests determine Betti numbers, motivic invariants, or historical priority. No independent audit has been performed.
