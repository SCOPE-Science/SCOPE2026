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

# Reproduction and limits

Run `python check.py` with Python 3 and NumPy to reproduce the rational polynomial/exponential moments and separate finite Nyström consistency checks. The finite matrices check the signs and first-order coefficients of the first two signed eigenvalues and numerical trace norm at six fractional orders. Their agreement is corroborative only, not an exhaustive eigenvalue certificate.

The infinite trace-norm statement follows analytically from the weighted second-derivative estimate and the nuclear Hankel decomposition through reflected squared Volterra operators. The key formula is \(\|H_h\|_{\mathcal S_1}\le \frac12\int_0^\infty t^2|h''(t)|dt\). When applied to the exact scaled kernel minus its first two Taylor terms, it bounds the *entire nuclear remainder* by \(O(\alpha^{-2})\).

The primary literature check explicitly distinguishes Eveson's leading-order trace equivalence from this new first-order coefficient. Only a self-review has been conducted; external independent audit remains unperformed.
