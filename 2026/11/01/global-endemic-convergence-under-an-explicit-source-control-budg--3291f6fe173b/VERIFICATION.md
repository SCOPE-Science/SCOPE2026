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

The accompanying `verify.py` is standalone Python 3 source requiring SymPy. Execute `python3 verify.py` from the directory containing it. It passed on this package, producing exact tests of (i) the coupled entropy derivative including all cross terms; (ii) the simplified source-control quotient; (iii) positive simplex mass balance; (iv) the three equilibrium equations; (v) exact rational values at the exhibited strict interior point; and (vi) the positive damping margin. These tests do not assert any result about untested parameter regimes by enumeration.

The global statement itself follows analytically from positive invariance, the explicit exact dissipation formula, its completed-square bound, properness of the integral potential, and LaSalle's invariance principle. The strict inequalities are checked symbolically or proved by the given parameter bounds, rather than extrapolated from numerical samples. The source date of October 7, 2026 is verified against the initial arXiv submission, not inferred from a later journal or revision date.

Independent audit has not been performed. The theorem is deliberately restricted to permanent immunity, zero conformity and strictly positive initial infection and adherence. The strongest historical risk is possible coverage by a general entropy-stability result not identified during primary-literature comparison.
