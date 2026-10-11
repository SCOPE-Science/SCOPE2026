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

The equilibrium proof is algebraically exhaustive. When \(q=0\), the equilibrium equations force \(p=r=s=0\). When \(q\ne0\), they force \(r^2=50\), \(p=qr/5\), \(s=-52p/21\), and then exactly \(35q^2-52q-1995=0\). Hence no additional real branches remain after the two cases are treated.

The packaged `verify.py` was replayed from the finalized finding package. It uses standard-library exact rational arithmetic plus a two-component representation of numbers \(a+b\sqrt2\). It verifies all four nonzero equilibrium substitutions, reconstructs \(\det(\lambda I-J)\) for both signs of \(r\), reduces the coefficients by the equilibrium quadratic, verifies the stated quartic, and checks the Routh-column formulas and strict sign bounds. Successful execution prints `VERIFY_OK`.

The unstable-index proof is exact: the origin's four diagonal eigenvalues are read directly from its Jacobian, and the nonzero equilibria have three open-right-half-plane roots by the Routh sign changes. No numerical trajectory, finite-time Lyapunov computation, or floating-point root finder is used as an infinite or exhaustive proof.

The result is limited to the stated benchmark parameters. The verification does not prove attractor existence, basin connectivity, hiddenness or self-excitation, or synchronization performance.
