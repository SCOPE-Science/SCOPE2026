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

# Verification and limits

The proved statement uses two successive applications of integral weak Lefschetz, the exponential sequence and Hodge decomposition for \(\operatorname{Pic}(X)\), integral square-zero cup-product analysis, Künneth cohomology, the regular-sequence Koszul resolution, and adjunction. The hypotheses are \(m\geq6\), \(d_i\geq3\) not all equal, a smooth Wehler hypersurface \(F\), and a smooth complete intersection \(X\).

The independent checks within this manuscript are reproducible through `python3 verify.py`. The script calculates actual low-degree Künneth dimensions for the three Koszul twists, the nonzero intersection against an ample divisor, and the primitive square-zero support condition at the boundary \(m=6\). Tested multidegree vectors: \((3,3,3,3,3,4)\), \((3,4,3,5,3,4)\), \((3,3,4,3,3,3,3)\), and \((3,4,4,3,3,5,3,3)\). The recorded output is `VERIFY_OK`.

Those finite symbolic checks do not prove weak Lefschetz or the all-parameter theorem and do not establish originality. In particular no classification is claimed when \(m\leq5\), when any \(d_i<3\), or when the defining complete intersection is singular. No independent external mathematical audit has been performed.
