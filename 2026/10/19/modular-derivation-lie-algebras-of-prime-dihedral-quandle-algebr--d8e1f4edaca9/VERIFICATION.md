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

# Reproducible verification

Invoke `python3 check_derivations.py` from a directory containing the supplied standalone checker. It uses only the Python standard library.

The checker creates the original-basis defining equations for every pair \((i,j)\) and every coefficient coordinate in the rank-\(p\) dihedral quandle algebra. The sparse row reduction over \(\mathbb F_p\) is independent of the proposed derivation basis. For \(p=3,5,7,11,13,17,19,23,31,37,41,43\) it produces derivation dimensions \(2,2,2,2,2,4,2,2,6,2,4,6\), respectively. It separately verifies that all proposed homogeneous operators satisfy Leibniz on every monomial pair and that matrix commutators satisfy each displayed bracket, for these primes plus \(p=29\). The final marker is `ALL_CHECKS_PASSED`.

The proof covers arbitrary fields of characteristic \(p\), since its coefficients lie in the prime subfield and it uses no finite-field enumerative assumption. Tested primes are a finite sample, not a substitute for the complete proof. No independent mathematical audit has been performed.
