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

The classification was checked independently by direct factorization of \(n\) and \(\varphi(n)\). For every odd prime \(p<200\) and every \(2\le a,b\le18\), the checker compares the theorem against the definition “both \(n\) and \(\varphi(n)\) are powerful but not perfect powers,” for 13005 exponent pairs in total.

The checker also tests all 21 terms with exact support \(\{2,p\}\) in the displayed OEIS A194085 prefix through 135000 and verifies that theorem-generated terms in that range are present in the prefix. Finally it approximates
\[
\prod_{\ell\ \mathrm{prime}}\left(1-\frac{2}{\ell^2}\right)
\]
using primes through 100000 and obtains approximately \(0.322634616605\), consistent with positivity of the constant.

These computations test arithmetic formulas and boundary cases only. The infinite classification follows from exact prime-exponent identities, and the asymptotic follows from the CRT local-density argument and convergence of \(\sum_\ell \ell^{-2}\); neither is certified by finite enumeration.
