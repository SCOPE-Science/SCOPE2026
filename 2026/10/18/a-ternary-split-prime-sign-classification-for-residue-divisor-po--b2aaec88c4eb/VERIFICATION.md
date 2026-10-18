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

# Reproducibility and mathematical limits

Run `python3 verify.py` beside this file (Python 3 standard library only). The script exhausts all integers through 2000 at five integer exponents using exact rational arithmetic and through 2500 at four negative noninteger exponents using floating-point tolerances. It tests the independent divisor and character formulas, sign restrictions, the unweighted zero-support condition, and the opposite-sign same-valuation examples at \(s=-3/4\).

These finitely many checks are regression evidence, not an infinite certificate. The proof for arbitrary positive integers and real exponents is in RESULT.md; its only classical analytic input beyond elementary divisor identities is divergence of the reciprocal-prime sum in a nonzero residue class modulo \(3\), along with elementary Dirichlet-series estimates. Unproved cases include exact positive-value densities at \(-1<s<0\) and the cumulative sign for \(s\ge0\).
