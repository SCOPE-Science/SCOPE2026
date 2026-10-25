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

# Reproduction of the arithmetic certificate

The standalone `verify_eleven.py` uses standard-library integer arithmetic only. It enumerates every sorted multiset of \(3\) and \(4\) exponents in \(\{0,\ldots,10\}\), identifies the canonical affine representatives, independently reconstructs each cyclotomic multiplication matrix and its exact determinant, compares all \(16\) table values, and checks their prime factors. It also constructs and verifies direct modular witnesses for all seven exceptional primes.

As a separate cross-check, all sixteen exact determinants were recomputed as \(\operatorname{Res}(\Phi_{11},f_J)\) using SymPy polynomial resultants; all sixteen values agreed, and all seven exceptional moduli passed a primality test. The executable completed successfully with the final line `PASS: all 1287 multisets, 16 affine orbits, exact norms and witnesses`. These are exhaustive finite *symbolic* certificates of the matrices and orbits, not mere data collection from bounded primes. The unrestricted result uses the proved resultant divisibility equivalence, which is valid for every prime whose multiplicative group has an order-eleven subgroup.

No arbitrary precision numerical tolerance, outside database of prime minima, or unperformed external validation is involved. The classification does not assert any exact minimum above four, and full-text comparison with some older related finite-field articles was inaccessible.
