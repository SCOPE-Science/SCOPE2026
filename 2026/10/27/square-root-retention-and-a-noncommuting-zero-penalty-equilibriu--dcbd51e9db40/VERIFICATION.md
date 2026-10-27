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

# Verification record

The algebraic proof in `RESULT.md` derives each payoff by geometric summation and each best-response test by differentiation. The accompanying `verify_fractional_cycle.py` is executable with SymPy as specified in `requirements.txt`.

Actual checks completed: symbolic quotient-derivative factorization, exact zero-penalty derivative reduction, exact symmetric indifference polynomial, four rational positive-penalty instances with 12 unilateral evaluations, endpoint signs at penalties \(1/2\) and \(3/4\), and 124 nonzero rational-grid zero-penalty profiles checked against necessary equilibrium signs. The checker completed without assertion failures.

Illustrative self-retentions: at penalty \(10^{-4}\), \(q_\varepsilon\approx0.0171233652176\); at penalty \(0.01\), \(q_\varepsilon\approx0.1558277369823\). The exact asymptotic is proved symbolically, not extrapolated from those values. The finite-grid check is not a complete proof over the continuum; the case split in `RESULT.md` is.

The source's per-step absorption formula was checked directly against the cited full-text definitions. Originality is supported by a focused comparison of the relevant full primary papers and remains subject to independent validation.
