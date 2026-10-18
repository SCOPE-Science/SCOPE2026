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

Run `python3 check_martingale.py` using the standard Python 3 library. The script separately derives finite matrices of the conditional expectations and computes exact column sums as rational numbers. It exhausts the \(2^d\) path choices for \(3\le b\le8\), \(1\le d\le9\), compares the exact norm formula and unique maximizing signs, and checks selected full matrices and complete small-tree sign choices. The executed script reported `PASS 237 exact-rational cases`.

The general theorem is proved in `RESULT.md` by explicit matrix entries, strict dynamic-programming comparison and a solved geometric recurrence. A finite test cannot certify arbitrary positive depth or unlimited arity. No independent audit or external certificate has been performed.
