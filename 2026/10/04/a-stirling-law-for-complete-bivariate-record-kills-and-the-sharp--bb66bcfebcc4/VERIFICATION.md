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

The proof is analytic. The exact finite-sample step is the conditional-rank argument: under a complete kill, the relative ranks of the first \(n-1\) points are unchanged in law, and their Pareto-minimum count is the left-to-right-minimum count of a uniform permutation. Its probability generating function is \(z(z+1)\cdots(z+n-2)/(n-1)!\).

The asymptotic step uses only fixed-degree elementary symmetric sums: for fixed \(r\), the tuples with repeated indices contribute lower order than \(H_m^r\). Combining this with the exact remainder formula from Theorem 3.9 makes every \(C_{n,j}\) with \(j<k\) negligible relative to \(C_{n,k}\) for fixed \(k\).

`verify.py` independently checks the unsigned-Stirling recurrence, normalization, the source formulas for the first, second, and last \(C\)-entries, and the displayed rows through \(n=5\). A successful run prints `VERIFY_OK`. These calculations are consistency checks only; they do not certify the infinite argument.

Unproved here: any uniform-in-\(k\) sharpening of Theorem 3.9, higher-dimensional analogues of the exact Stirling law, and the empirical-frequency conjectures from Section 4 of the motivating paper.
