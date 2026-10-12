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

The bundled `verify.py` uses exact rational arithmetic. It checks the disease-free behavioral level \(B_0=1/11\), the threshold \(\mathcal R_0=34/11\), all four endemic-equilibrium equations at \(x^*=(27/50,23/100,23/100,5/9)\), the vector field at the witness state, the derivative identity for the displayed Volterra function, and the equation-(13) comparison.

The exact outputs certified by the assertions are
\[
\dot W=\frac{2019503}{13851000}>0,
\qquad
Q_{13}=-\frac{30854209}{1923750}<0.
\]
Thus the inequality \(\dot W\le Q_{13}\) fails at the witness state.

The calculation is finite and exact. It certifies failure of the published derivative bound only; it does not certify instability, nonconvergence, or falsity of the global-stability statement under a different proof.
