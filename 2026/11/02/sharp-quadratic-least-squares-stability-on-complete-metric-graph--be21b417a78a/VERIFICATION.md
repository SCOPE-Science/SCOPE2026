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

The accompanying `verify.py` was executed with its exact symbolic computations and independently assembled finite Gram matrices. It returned `PASS: exact Gram, inverse, kernel, roots, monotonicity, limits, and 83 independent edge kernels.` The script uses Python 3, SymPy, and mpmath.

Mathematical checks directly establish \(\int h^2=1/30\), the nodal Gram entries, its closed inverse, the roots and absolute integrals of the two edge kernels, the strict derivative sign for all real \(n\ge3\), the exact values on either side of the \(5/2\) threshold, and the inequality \(|\phi|+|\psi|+2h\le1\). The last inequality and the bubble-coefficient estimate are the decisive steps transferring vertex control to the full operator norm when \(n\ge6\).

Independent finite-matrix inversions were performed for \(n=3,4,5,6,7,8\); they are corroborations, not replacements for the all-parameter proof. Published literature comparisons did not discover an exact prior statement, but unindexed or otherwise unavailable equivalent work remains possible. No independent scientific audit has been performed.
