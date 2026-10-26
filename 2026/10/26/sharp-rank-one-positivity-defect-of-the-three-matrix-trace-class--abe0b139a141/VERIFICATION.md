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
# Reproducibility

Run `python CHECK.py` using Python 3 with NumPy and SymPy. The checker verifies exact rational/radical two-dimensional witness identities, the derivative and cubic resultant of the extremal overlap, and the rank-one operator formula and eigenvalues on 900 deterministic numerical instances with nontrivial complex phases and unequal positive amplitudes. Its printed maximizing values are \(t_*=0.29559774252208476\ldots\), \(r_*=0.5436890126920764\ldots\), and \(\kappa_*=0.06744224886812294\ldots\).

Finite tests validate algebraic normalizations but cannot prove the universal result. The proof in `RESULT.md` establishes the full complex-dimensional claim by exact two-dimensional reduction, endpoint analysis, polynomial derivative sign and translation covariance.

Independent audit has not been performed.
