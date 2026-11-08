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

The exact derivative formulas for \(V_\alpha\) and the transformed stationary equation are displayed in `RESULT.md`. The key asymptotic estimate is the integrable residual of the WKB approximation. Numerically solving a finite ODE is not a substitute for the infinite-interval Volterra argument.

## Reproduction

Run `python check.py` with Python 3 and SciPy available. The checker evaluates the potential derivatives, the exact coefficient \(Q\), and a backward-Riccati approximation to the decaying solution. It exercises the four sample powers \(1/3,1/2,2/3,0.82\) at multiple points on the tail. Expected output: `PASS 106 finite diagnostic assertions; critical logarithmic power 0.057988632165`. The tests use \(D=0.91\), \(r=1.17\), and \(\lambda=1.32\).

The checker does not verify the limiting constants or cover all allowed real parameters. Those are analytical claims established in the proof. No independent scientific audit has been performed.
