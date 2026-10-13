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

The proof was checked symbolically from the exact source branch formulas. For \(Q\ge40\) and \(1\le m\le\lfloor Q/20\rfloor\), the relevant minimum switches are safely beyond the block: the odd threshold is \(1/10-2/(5Q)\), and the even threshold is \(3/10-1/(5Q)\). The exact summand difference is therefore \(a_Q/[Q(m+\ell_Q(m))]\) for both parities, with \(a_Q=(3/2-1/Q)^{-1}\).

The standalone program `verify.py` checks these branch choices and identities using exact rational arithmetic. It also evaluates the source series at finite cutoffs for several \(Q\) and reports the scaled remainder. Those finite values are corroborative only. The infinite theorem uses the harmonic-sum estimate and the absolute tail bound \(2\sum_{m>N}m^{-2}=O(1/N)\).

Unproved here: the constant term after subtracting \((2/3)(\log Q)/Q\), finite-\(Q\) unimodality, and global optimality of Bai's point.
