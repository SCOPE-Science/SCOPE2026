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

# Verification of finite-cutoff zeta and spectral asymptotics

Run `python CHECK.py` with standard Python 3. The script recomputes the full unit-interval adjacency for cutoff levels one to three and the compressed four-adic quotient, and compares their matrix-power traces using integer arithmetic. It also derives determinant polynomial coefficients exactly from Newton's trace identities, checks the first two closed-orbit counts, and iterates positive quotient matrices at 65-digit Decimal precision for levels four through eleven.

Observed result: `CHECK_OK 46 exact matrix/trace/determinant and high-precision asymptotic diagnostics`. At level two the exact zeta denominator is `1-16z+44z^2`. The scaled second-order residual was less than `0.025` across the tested levels four through eleven.

The checker is a finite diagnostic only. It does not prove the existence of all symbolic realizations, exclude extra periodic boundary coding, establish an entropy equivalence, or prove a uniform asymptotic as the cutoff tends to infinity. Those facts follow from the analytic arguments in `RESULT.md`. No independent audit or formal proof certification has been carried out.
