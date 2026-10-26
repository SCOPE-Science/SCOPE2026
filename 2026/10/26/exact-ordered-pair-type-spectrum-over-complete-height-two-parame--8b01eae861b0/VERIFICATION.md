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

Run `python verify.py` from this directory. Only the Python 3 standard library is required.

The checker reconstructs every permitted local state, all compatibility edges, and both support coefficient matrices by independent three- and four-point transitivity tests. It then performs the binomial change of basis and tests the exact comparable/incomparable formulas on \(0\le a,b\le7\). An independent exhaustive assignment method tests all ordered-pair extensions over the \(15\) parameter-size pairs satisfying \(a+b\le4\); it does not consult the support coefficients. The complete output is in `verification_output.txt`.

All reported checks passed. The general theorem rests on the combinatorial support decomposition and coefficient extraction, not finite enumeration. Numerical computation cannot establish historical novelty. Independent auditing has not been performed.
