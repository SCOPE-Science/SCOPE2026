---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

C PASS: For any non-ultimately-periodic one-sided binary word u, its XOR derivative d cannot be ultimately h-periodic because that forces u_(i+2h)=u_i eventually. Every E-antipalindromic factor projects to a palindromic derivative factor with at most two binary lifts; C_d(n-1)<=C_u(n). Shallit Theorem 4 on d yields P_E(n)log(P_E(n)+1)/C_u(n)->0; Shallit also makes ordinary reversal palindromes negligible for u. With H-language invariance, complement fixes no word and Burnside forces C_H(n)/C_u(n)->1/4 without assumed convergence. Odd n and empty factors do not affect asymptotics.

## originality

PASS

Best-of-knowledge original transfer of Shallit ordinary-palindrome sparsity through the binary XOR derivative to antipalindromes and unconditional H-complexity ratio; primary access risk is explicit.

## value

PASS

V PASS: Removes the explicit convergence hypothesis from the most relevant generalized-reflection result for the entire aperiodic H-invariant binary class, using a useful strong E-palindromic sparsity reduction, not a routine table computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
