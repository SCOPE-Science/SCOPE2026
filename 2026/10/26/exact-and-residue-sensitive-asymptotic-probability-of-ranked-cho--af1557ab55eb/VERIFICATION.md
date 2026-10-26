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

# Reproduction and limits

Run `python verify_center_squeeze.py` from a directory containing that script. The script requires only the Python standard library; the exact expected output is `verification_certificate.json`. It reproduces the exact multinomial favorable counts for odd electorate sizes through 31; checks all four single-peaked ballot types to the seventh voter; independently checks pairwise Condorcet winner selection and all legal first-round IRV tie breaks; and numerically bounds the tails of the three geometric coefficient sums by exact rational arithmetic. No simulation or random approximation is used.

The all-electorate and large-electorate results are analytical; finite exhaustive enumeration does not certify them. The critical inputs for the limit proof are gamma log-convexity, fixed-offset gamma ratios, absolute summability of the geometric dominating function, dominated convergence along each residue class, and Stirling's formula. The deterministic center-elimination behavior was reported previously; this verification does not establish bibliographic uniqueness.
