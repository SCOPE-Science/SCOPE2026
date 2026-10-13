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

# Verification and reproducibility

Run `python3 verification.py` using only the Python 3 standard library. The program constructs the six-dimensional nonlinear vector field from its exact rational parameters, uses rational dual-number differentiation at the disease-free equilibrium, and compares the resulting full Jacobian entry by entry with its predicted rational matrix. It then calculates the infected block's trace \(-7/6\), determinant \(1/6\), and exact eigenvalues \(-1\) and \(-1/6\); checks the remaining diagonal block eigenvalues \(-1/2\), each repeated four times; and compares \(\mathcal R_{\mathrm{source}}=5/3\) with \(\mathcal R_{\mathrm{contact}}=5/6\). The successful run prints `VERIFY_OK`.

The proof of cancellation of \(\Lambda/\mu\) follows analytically from the quotient rule and the demographic balance, independent of this code. The program checks the finite-dimensional counterexample exactly; it does **not** certify the spectrum or nonlinear long-time behavior of the general infinite-dimensional age-structured system. All parameter values are explicit and exact. The source's section 2 normalizes infection contact by the number of available half-edges; this convention is essential to the claim.
