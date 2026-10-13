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

The proof was checked by direct substitution into the four equilibrium balances and by symbolic differentiation. The bundled `verify.py` checks the formulas for \(R\), \(C\), \(H\), \(\Delta\), the scalar derivative \(\Phi_\varepsilon'(I)\), and \(\partial_hH\); it prints `VERIFY_OK` when all exact identities hold.

The sign conclusions are analytic. They use only \(\mu,\beta,\alpha,\delta,\gamma>0\), \(0\le\sigma\le1\), \(\varepsilon\ge0\), and \(\mathcal R_0>1\). No finite sample establishes uniqueness or monotonicity. The result does not verify stability, global attraction, unequal-feedback uniqueness, or transmission-driven uniqueness.
