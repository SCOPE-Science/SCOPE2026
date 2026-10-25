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

# Verification of the Ramanujan convolution Smith form

The arithmetic identity \(c_n(t)=\sum_{d\mid\gcd(n,t)}d\mu(n/d)\) was used to assemble each integer matrix \(C(n)=(c_n(i-j))\), including the cases \(n=1\) and powers of \(2\). The attached `verify_ramanujan_smith.py` calls SymPy's exact-domain Smith normal form on the full integer matrix and compares the entire diagonal, including the \(n-\varphi(n)\) trailing zeros, with the closed formula.

Executed check: `VERIFY_OK smith_cases 28 max_modulus 42 max_dimension 42`. No floating-point calculations were used. The executed script file is embedded alongside this document; it uses Python 3 and SymPy 1.13+.

This test is a finite corroboration, not a proof for all moduli. Universal validity follows from the prime-power block decomposition, the determinantal divisors of \(pI_p-J_p\), the integral Chinese remainder tensor factorization, and the prime-by-prime valuation sort in `RESULT.md`. No independent review or external certification has been performed.
