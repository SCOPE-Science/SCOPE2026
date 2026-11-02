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
# Verification of the cross-polytope distance theorem

The standalone command `python3 verify.py` executed successfully in Python 3 and printed `CHECK_OK 219 finite comparisons, dimension/asymptotic diagnostics`. The checker uses standard-library floating point operations. It compares the full \(2r\times2r\) commutator norm, obtained independently from symmetric Jacobi diagonalization, to the analytic compressed \(2\times2\) Gram expression for \(3\le r\le11\) and 21 trial parameters; it also checks the antipodal norm and positivity, critical-point uniqueness diagnostics, and large-dimension coefficients.

The general statements rest on the explicit symmetry averaging, Gram block reduction, full-column-rank strong-convexity argument, endpoint derivative signs, and uniform perturbative asymptotic expansion in `RESULT.md`; numerical tests neither substitute for these arguments nor exhaust infinitely many dimensions. The exact adjacent value remains an algebraic minimax characterization. Independent audit and external validation have not been performed.
