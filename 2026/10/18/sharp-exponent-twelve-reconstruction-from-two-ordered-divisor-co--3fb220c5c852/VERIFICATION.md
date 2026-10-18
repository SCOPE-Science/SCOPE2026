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

# Verification instructions

Use Python 3, standard library only: `python3 verify.py`. The executable rebuilds the \(12\times12\) valuation matrix from the defining divisor-function formula and uses exact fraction-free Bareiss elimination. It requires the final determinant to equal \(1\), then checks the exact linear dependence introduced by exponent \(13\), including the two distinct multisets with the same invariant pair \((126,3780)\).

To detect independent implementation errors, it directly counts ordered two-factor and three-factor decompositions for the integers \(2\) through \(400\) and compares each with the multiplicative formula. A bounded exponent-signature enumeration provides further consistency checks. All numerical operations are integral and exact, with assertions on each required division. The universal theorem follows from the prime-exponent factorization formula and invertibility of the full \(12\times12\) matrix; finite checks alone are not an infinite proof.

Scientific limitations: the calculation concerns prime-exponent multisets and does not recover prime bases, determine all collisions beyond exponent \(12\), or constitute an independent validation.
