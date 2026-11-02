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

The field was rewritten in its published compact polynomial form. Symbolic differentiation of \(S=x^2+y^2\), \(E=x^2/a+y^2/b-1\), and \(\rho=S(S-1)/(-E)\) produced and verified the exact identity \(d(\log\rho)/dt=-\lambda\Omega/(ab)\), where \(d\theta/dt=\Omega\). The check uses rational polynomial arithmetic with SymPy, not floating-point sampling. Run `python3 checks/check_annulus.py`; saved output is in `checks/checker_output.txt`.

A high-precision numerical check independently evaluated the original physical-time integrals for the two boundary cycles at three parameter pairs. Those comparisons are checks of the exact formulas, not proofs of universal validity. The proof of the angular return map, all-orbit classification, and period formulas appears in `RESULT.md`, including the strict sign of angular speed and the global radial coordinate's monotonicity. No independent audit or numerical validation of the infinite family has been performed.
