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

The source's predator-free flight is logistic. Its period identity gives
\[
\frac{\eta K-(1-p_1E_l)h_l}{\eta K-h_l}
=(1-p_1E_l)e^{rT}.
\]
Using
\[
\frac{d}{dt}\log x=r-rx/K
\]
in the source's printed convergence ratio yields exactly
\[
\rho=(1-p_2E_l)e^{-\mu T}.
\]

The bundled `verification/verify.py` checks the unsimplified and simplified expressions over multiple admissible parameter sets. For Example 3.1 it verifies
\[
T=\log2,\qquad \bar p_2=0.1875,\qquad
\rho(0.1)=0.4,\qquad \rho(0.2)=0.3.
\]
It prints `VERIFY_OK` on success.

Unproved limits: positive order-1 cycles are not classified. At \(h_l=\eta K\), the hitting time diverges and the finite-cycle calculation does not apply.
