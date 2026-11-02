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

# Verification and limitations

The reproducible standalone verifier is `verify_schur.py` (Python 3 and SymPy; NumPy optional). It constructs the exact quartic, computes the Cayley polynomial and seven Routh–Hurwitz expressions, replaces \(q\) and \(v\) with positive-rational coordinate substitutions, and expands every numerator over \(\mathbb Q\). Every denominator factors into positive powers of \(1+X\) and \(1+Y\); every numerator has exclusively nonnegative rational monomial coefficients and at least one strictly positive term on the declared domain. The exact term counts are \(3,14,16,16,16,63,117\).

The script verifies \(P(1)=6\mu(1-q)(1-v)\) and the rational witness \(W(1/4)=103/192\). The boundary condition uses the positive leading cubic coefficients and strict cubic Hurwitz determinant; the continuous-mode computation and positivity of the series in the proof can be checked directly from the displayed formulas. Optional sample eigenvalue calculations and finite checks are corroboration, not an infinite-dimensional or all-parameter numerical proof. Mathematical claims are specific to the scalar BDF3 tail in exact arithmetic. Independent audit has not been performed.
