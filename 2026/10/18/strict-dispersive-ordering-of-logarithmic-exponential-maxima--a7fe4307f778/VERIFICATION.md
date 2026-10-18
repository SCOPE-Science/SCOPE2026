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

The analytical proof is complete under the exact domain and quantifiers in `RESULT.md`: all real \(0<a<b\), all \(0<u<v<1\). Its only nontrivial sign check is \(h'(z)<0\) for every \(z\in(0,1)\), which follows from two strict instances of \(\log x<x-1\).

Run `python verify.py` from the file's directory. The program uses only the Python standard library, checks exact CDF-to-quantile inversion numerically, compares analytic quantile slopes to symmetric finite differences, tests ordered widths for a fixed explicit grid of parameters and probability pairs, and verifies the sign inequality. These finite numerical checks are not an exhaustive proof. In particular, the confidence in the infinite claim rests on the printed algebra, not on program execution.

Prior-work comparisons are recorded in `REVIEW.md` and `AUDIT.json`; an independent scientific or bibliographic audit has not been performed. The full text of the later Giam paper was not available in the inspected sources, leaving residual priority uncertainty.
