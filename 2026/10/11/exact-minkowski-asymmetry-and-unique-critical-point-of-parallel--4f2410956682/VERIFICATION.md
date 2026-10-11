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

Run `python verify.py` using Python 3.9 or later. The program uses only the Python standard library and exact rational arithmetic. It checks 3,424 admissible coefficient configurations, their six facet support values and the proposed minimizing center; it separately checks 375 linear-program optima by rational Gaussian elimination and exhaustive active-triple enumeration, then tests rational range witnesses. The actual run returned `VERIFY_OK 3424 exact cases; 375 independent rational LP solves and range witnesses`.

A separate exploratory linear-program comparison on 2,000 random positive real configurations agreed numerically to maximal discrepancy less than \(5\times10^{-16}\); this is supplementary numerical evidence, not a proof.

The analytical result applies to **all** real \(a,b,c,t\) satisfying the stated strict positivity restrictions. Exact enumeration is not a substitute for that universally quantified interval argument. Published area inequalities for the same polygon class do not supply this containment formula. Related literature may still contain equivalent computations.
