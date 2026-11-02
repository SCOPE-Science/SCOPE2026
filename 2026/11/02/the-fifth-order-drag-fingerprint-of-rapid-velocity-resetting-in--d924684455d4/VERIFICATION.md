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

The result follows analytically from the exact stationary generator identities for \(v\sigma\) and \(v^2\), the Green–Kubo relation and the exact first-reset decomposition
\[
I=I_{\mathrm{nr}}+\frac{rM}{2\lambda}J.
\]
Reset-age moment bounds provide all required asymptotic controls. The supplementary `verify.py` is a separate standard-library rational-arithmetic calculation of the closed generator moment formulas for the linear-drag reference and the exact first variation under a cubic drag perturbation. It checks the sign and approaches the same fifth-order coefficient. No experiment is used as a proof of an infinite asymptotic claim.

To reproduce: run `python3 verify.py` in the directory containing the files. It requires only Python 3 and prints the number of exact-fraction assertions. The verifier concerns a perturbative algebraic consistency condition; it does not separately certify the global proof or publication priority. Independent review remains unperformed.
