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

# Reproducibility and limits

The included standalone `check_supersingular_as.py` uses only Python 3 standard-library modules. Run it as `python3 check_supersingular_as.py`. It enumerates every \((x,y)\) pair over \(\mathbb F_{3^n}\), \(n=1,2,3,4\), in an explicitly constructed field with separately certified irreducible modulus; each direct count is cross-checked against the trace-zero formula. It yields projective counts \(7,19,28,91\) including the unique place over infinity and prints `EXACT_CERTIFICATE_PASS`.

The certificate also verifies the degree-eight coefficient vector \((1,3,9,18,36,54,81,81,81)\), its factorization, and valuation inequalities for supersingularity. The deduction of the higher-degree coefficients relies on the Weil functional equation for a smooth genus-four curve, rather than numerical enumeration through every extension. The genus, full geometric automorphism group and exclusion of all smaller positive genera rely on stated standard ramification formulas and Tafazolian–Kazemifard, arXiv:2610.13279v1 (Theorem 1.1, Lemma 3.3), with their pivotal automorphism coefficient relations reproduced in the mathematical result.

Independent validation has not been performed.
