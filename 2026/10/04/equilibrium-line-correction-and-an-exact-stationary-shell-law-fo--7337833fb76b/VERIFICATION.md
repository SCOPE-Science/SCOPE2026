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
The finding was checked by direct symbolic reconstruction from the displayed integer-order vector field. The equilibrium equations force \(x=y=z=w=0\) and leave \(u\) arbitrary. At every such point the Jacobian has characteristic polynomial \(\lambda(\lambda+a)(\lambda+b)(\lambda^2-c\lambda+d)\).

For the stationary identity, the following exact generator balances were checked:
\[
\langle w\rangle=\langle x\rangle=0,
\qquad
\langle xw\rangle=\langle x^2\rangle=b\langle z\rangle,
\]
\[
b\langle z^2\rangle=c\langle w^2\rangle,
\qquad
\langle\dot x^2\rangle=a^2(\langle w^2\rangle-\langle x^2\rangle).
\]
Combining them gives the claimed shell identity exactly. The equality case was checked separately using compactness of invariant support and the complete-orbit equations; it is not inferred from a numerical tolerance.

The accompanying `verify.py` uses only the Python standard library and exact integer/rational algebra. Running it from the package returns `VERIFY_OK` after checking the energy cancellation, factorized characteristic polynomial coefficients, and the specialization \(a=20\), \(b=2\), \(c=10\).

Limits: no existence theorem for a non-equilibrium invariant measure is claimed; no finite trajectory is used to prove recurrence; and the stationary-measure argument is not transferred to the Caputo fractional-memory system.
