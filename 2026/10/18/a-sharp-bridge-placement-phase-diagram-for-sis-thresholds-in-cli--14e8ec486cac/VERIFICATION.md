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

# Verification evidence and scope
Execute `python verify_bridge.py` in a Python environment with SymPy installed. It reconstructs the \(13\)-site contact community explicitly, checks the quartic quotient determinant and full characteristic polynomial, derives four symbolic diagonal resolvent inequalities, independently evaluates 16 Green-function entries by exact rational linear solves, checks the integer phase boundary from \(k=5\) to \(k=15\), reproduces the exact \(w_7^2=40\) crossover, and checks all four full \(15\)-vertex example determinants and rational threshold signs. The expected terminal line begins `VERIFY_OK`.

The code checks finite identities and examples, not every real \(w>0\) or unbounded integer \(k\). The symbolic argument in RESULT.md supplies those infinite-parameter proofs. The nonlinear persistence assertion depends on the specified monotone mean-field SIS recurrence and \(0<\delta<1\), not on an individual-level stochastic survival probability. Equality at the epidemic threshold and independent external audit remain unperformed.
