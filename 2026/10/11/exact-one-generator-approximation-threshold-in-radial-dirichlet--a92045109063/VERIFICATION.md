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

The formulas are proved analytically by multinomial expansion, a one-constraint weighted Hilbert-space minimization, torus Parseval, nondegenerate Gaussian localization and asymptotic comparison of positive series. The minimizer is an explicit polynomial at each degree and needs no external data or numerical optimization.

The accompanying `verify_affine_generator.py` is an executable standard-library-only check. Execute `python verify_affine_generator.py` in a directory containing that script. Its exact rational cases cover support sizes one, two and three, polynomial degrees through three, and the central-binomial identity at several degrees through eighty. It additionally calculates the multinomial asymptotic ratios for support sizes two, three and four, at the explicitly reported finite orders. A successful run prints `PASS`.

The finite checks do not certify Gaussian asymptotics, convergence of infinite series, novelty or independent validation. These rely respectively on the stated analytic proof, the investigated source comparisons and any future independent review. No general claim about unrestricted polynomial multipliers is supported by this checker.
