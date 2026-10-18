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

# Mathematical verification

The proof in `RESULT.md` is the basis of the all-graph claim. The accompanying `verify.py` is a standalone Python 3 program using only the standard library; run `python verify.py`.

The program recomputes exact rational matrices for four connected nonbipartite positively weighted graphs with at least two neighbors per vertex (3, 4, 5, and 6 vertices). For every switching length \(1\le k\le12\), it checks the complete-layer projector identity and the exact matrix \(C_k=BA^k\); entry positivity; the resolvent stationary equation and stationary normalization; strict odd–even comparisons of \(\chi^2(\nu_k\|\pi)\) and of the canonical inverse-degree consensus; and a quotient action identity on two independent fixed test vectors per period. The completed replay reported all tests passed.

For the weighted triangle with edge weights \((2,1,1)\), the exact consensus values for the first four switching lengths are \(4/5\), \(10/13\), \(18/23\), and \(38/49\), bounded relative to isolated consensuses \(3/4\) and \(7/9\) as predicted.

Finite examples are **not** a proof for arbitrary graph order or real edge weights, nor do rational tests prove asymptotic limits. Those conclusions follow from the invariant projector formula, the reversible spectral decomposition, the strict scalar derivative formula, and the trace argument in `RESULT.md`. The program separately checks a few characteristic non-Perron eigenvalue scalings numerically only in local exploration; such float checks are not claimed as part of the embedded portable verification.
