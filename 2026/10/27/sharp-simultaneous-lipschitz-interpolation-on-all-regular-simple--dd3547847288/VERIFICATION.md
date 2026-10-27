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

# Reproducibility and limits

The analytical proof establishes the result for every integer \(n\ge4\) and \(3\le k\le n-1\). The standard-library `verify.py` performs full point-pair enumeration for small instances and exact rational bound checks for the strict integer \(k=17\) comparison. It does not replace the universal parameter argument. Run `python verify.py` from the directory containing the embedded files.

The optional `verify_lp.py` requires SciPy and NumPy and was run with SciPy's HiGHS linear-programming solver. It independently optimizes **all** vertex-to-centroid coefficients, without presupposing equivariance or positivity, for four small inputs. Run `python verify_lp.py` in the same directory. The finite linear programs are numerical corroboration, not a proof of arbitrary-dimensional optimality.

The reviewed claim is limited to finite Euclidean chord-distance point sets and scalar real-linear maps; bibliographic searches do not certify novelty worldwide. No independent audit was performed.
