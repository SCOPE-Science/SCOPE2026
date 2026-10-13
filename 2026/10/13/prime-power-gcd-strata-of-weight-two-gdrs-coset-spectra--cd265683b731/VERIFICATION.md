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

# Verification details

Run `python3 verify.py` from the package directory (Python 3 standard library only). It prints `VERIFY_OK` after exhaustively comparing all distinct \(k\)-subsets with the Ramanujan-sum identity and the prime-power stratum formulas for every eligible pair \(5\le M\le17\), \(3\le k<M\), for a total of 33 pairs. Exact integer arithmetic is used. It additionally checks the concrete \(q=9,d=6\) three-stratum example and its coset multiplicities.

The general statement is proved by character orthogonality and strict binomial comparison in `RESULT.md`, using GDRS reductions already established in arXiv:2605.10594v1 and subset-sum identity established in arXiv:1112.6294v1. The finite check does not validate all prime powers. Distinct support pairs and nonzero-symbol assignments are counted algebraically, not exhaustively for large fields. No independent audit has occurred.
