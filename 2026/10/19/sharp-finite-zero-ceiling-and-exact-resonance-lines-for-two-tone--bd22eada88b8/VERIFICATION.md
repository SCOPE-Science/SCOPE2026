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

# Reproduction and scope of verification

Run `python3 verify.py` with Python 3 and its standard library (no third-party packages). It evaluates the absolutely convergent defining integral via Simpson's rule at 30 representative points, checks 51 resonance-line evaluations for the second and third Hermite windows, and checks the two scalar zero counts at \(\Delta=8\) for each of the orders \(n=0,1,2,3,4,5,6\).

Completed invocation: `python3 verify.py`.

Completed output: `VERIFY_OK 95 integral, resonance, and sharp-count checks; n=0..6; gap=8`.

These are finite floating-point confirmations only. The analytic proof of the unbounded-order theorem, the exact resonance set, and asymptotic sharpness is in `RESULT.md`; the script is not an exhaustive check for all real parameters or all orders. No independent mathematical audit or external certification has been performed.
