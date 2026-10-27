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

# Verification of two habitat-occupancy sign reversals

The theorem is proved in `RESULT.md` from the exact solutions of the colonization–extinction equations, a one-stationary-point derivative argument, the positive endpoint assumptions and a nondegenerate Taylor expansion at the critical minimum. The checks below do **not** serve as an infinite-domain proof.

Run `python verify_two_reversals.py` using only the standard Python library. It verifies the exact witness \(A(t)=1/10+(1/5)e^{-4t}-(1/4)e^{-t}\), whose signs are \(A(0)=1/20>0\), \(A(\log2)=-1/80<0\), and \(A(\infty)=1/10>0\). Both predicted positive-time roots are obtained by bisection. The program also verifies convergence of the reversal-interval length to the analytical square-root threshold formula at three small offsets and compares 2,456 valid seeded random parameter configurations with the exact threshold (5,000 tuples generated; others fail the required initial occupancy ordering).

Expected output includes the positive crossing times approximately \(0.127598992901\) and \(0.852234164747\), followed by PASS for critical scaling and randomized checks.

Limitations: Finite tests cannot demonstrate absence of missed near-equality cases; the strict mathematical classification is analytical. The ecological expectation model excludes detection noise, inter-habitat feedback and time-dependent rates. No independent audit or field validation has been performed.
