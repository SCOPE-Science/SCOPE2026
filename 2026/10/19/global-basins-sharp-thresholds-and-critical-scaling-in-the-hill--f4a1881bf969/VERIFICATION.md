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

The analytic proof is contained in `RESULT.md`; no external computer algebra, private computation or numerical database is needed for any infinite-time statement. In the present package, run `python3 checker.py` using Python 3 and the standard library only. The checker reports 208 passed exact rational and finite numerical diagnostics. Its exact tests use \(m=2\) and rational two-cycles; numerical tests cover noninteger Hill exponents, first and fourth iterates, both hyperbolic cycles, near-critical \(n^{-1/2}\) decay and parameter square-root splitting.

Finite-iteration checks cannot certify global convergence or originality. The proof's substantive ingredients are the strict negative Schwarzian of \(g\), the relation \(T^4=(g^2,g^2)\), the strict contraction \(q<1\), and the critical cubic jet. Independent audit is not performed. A plausible 2015 original-model paper was only available by abstract.
